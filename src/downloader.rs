//! Resumable model-file downloader (plan step 11, host part).
//!
//! Dependency-free HTTP/1.1 client supporting `Range` resume and progress
//! callbacks, so the phone binary stays lean. Plain `http://` only for now:
//! `https://` and redirects need a TLS follow-up before real hosts
//! (e.g. Hugging Face) work.

use std::{
    io,
    path::Path,
};
use tokio::{
    fs::OpenOptions,
    io::{AsyncReadExt, AsyncWriteExt},
    net::TcpStream,
};

/// Progress snapshot passed to the download callback.
#[derive(Debug, Clone, Copy)]
pub struct Progress {
    pub downloaded: u64,
    pub total: Option<u64>,
}

/// Download `url` to `dest`, resuming from a partial file when `resume`
/// is set. Calls `on_progress` after every chunk. Returns total bytes on
/// disk. Only `http://` URLs are supported.
pub async fn download(
    url: &str,
    dest: &Path,
    resume: bool,
    on_progress: impl Fn(Progress),
) -> io::Result<u64> {
    let (host, path) = split_http_url(url)?;
    let mut stream = TcpStream::connect(&host).await?;

    let from = if resume {
        tokio::fs::metadata(dest).await.map(|m| m.len()).unwrap_or(0)
    } else {
        0
    };
    let range_header = if from > 0 {
        format!("Range: bytes={from}-\r\n")
    } else {
        String::new()
    };
    let request = format!(
        "GET {path} HTTP/1.1\r\nHost: {host}\r\n{range_header}Connection: close\r\n\r\n"
    );
    stream.write_all(request.as_bytes()).await?;

    let mut head = Vec::new();
    let mut one = [0u8; 1];
    while !head.ends_with(b"\r\n\r\n") {
        if stream.read_exact(&mut one).await.is_err() {
            break;
        }
        head.push(one[0]);
        if head.len() > 32 * 1024 {
            return Err(io::Error::new(io::ErrorKind::InvalidData, "header too large"));
        }
    }
    let head = String::from_utf8_lossy(&head);
    let mut lines = head.lines();
    let status: u16 = lines
        .next()
        .and_then(|l| l.split_whitespace().nth(1))
        .and_then(|c| c.parse().ok())
        .ok_or_else(|| io::Error::new(io::ErrorKind::InvalidData, "bad status line"))?;
    let mut total: Option<u64> = None;
    for line in lines {
        let line = line.trim_end_matches('\r');
        if let Some(v) = line.strip_prefix("Content-Length:") {
            total = v.trim().parse().ok();
        } else if let Some(v) = line.strip_prefix("Content-Range:") {
            // "bytes 100-199/1000" — total is after the slash.
            if let Some((_, t)) = v.trim().rsplit_once('/') {
                total = t.parse().ok();
            }
        }
    }

    let append = match status {
        200 => false,
        206 if from > 0 => true,
        206 => false,
        s => {
            return Err(io::Error::new(
                io::ErrorKind::Other,
                format!("unexpected status {s}"),
            ))
        }
    };
    let mut file = OpenOptions::new()
        .create(true)
        .write(true)
        .truncate(!append)
        .append(append)
        .open(dest)
        .await?;
    if !append {
        // Fresh download: progress starts at zero.
    }
    let mut downloaded = if append { from } else { 0 };
    let mut buf = [0u8; 32 * 1024];
    loop {
        let n = stream.read(&mut buf).await?;
        if n == 0 {
            break;
        }
        file.write_all(&buf[..n]).await?;
        downloaded += n as u64;
        on_progress(Progress { downloaded, total });
    }
    file.flush().await?;
    Ok(downloaded)
}

fn split_http_url(url: &str) -> io::Result<(String, String)> {
    let rest = url
        .strip_prefix("http://")
        .ok_or_else(|| io::Error::new(io::ErrorKind::InvalidInput, "only http:// supported"))?;
    let (host, path) = match rest.find('/') {
        Some(i) => (&rest[..i], rest[i..].to_string()),
        None => (rest, "/".to_string()),
    };
    if host.is_empty() {
        return Err(io::Error::new(io::ErrorKind::InvalidInput, "empty host"));
    }
    Ok((host.to_string(), path))
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::sync::{Arc, Mutex};
    use tokio::net::TcpListener;

    const DATA: &[u8] = b"0123456789abcdef";

    /// Test file server honoring `Range`, always closing the connection.
    async fn serve_once(listener: TcpListener, omit_length: bool) {
        let (mut s, _) = listener.accept().await.unwrap();
        let mut head = Vec::new();
        let mut one = [0u8; 1];
        while !head.ends_with(b"\r\n\r\n") {
            s.read_exact(&mut one).await.unwrap();
            head.push(one[0]);
        }
        let head = String::from_utf8_lossy(&head).into_owned();
        let range_start: Option<u64> = head.lines().find_map(|l| {
            l.trim_end_matches('\r')
                .strip_prefix("Range:")
                .and_then(|v| v.trim().strip_prefix("bytes="))
                .and_then(|v| v.strip_suffix('-'))
                .and_then(|v| v.parse().ok())
        });
        let (status, body) = match range_start {
            Some(n) if (n as usize) < DATA.len() => (
                format!(
                    "HTTP/1.1 206 Partial Content\r\nContent-Range: bytes {}-{}/{}\r\n",
                    n,
                    DATA.len() - 1,
                    DATA.len()
                ),
                &DATA[n as usize..],
            ),
            _ => ("HTTP/1.1 200 OK\r\n".to_string(), &DATA[..]),
        };
        let len_header = if omit_length {
            String::new()
        } else {
            format!("Content-Length: {}\r\n", body.len())
        };
        s.write_all(format!("{status}{len_header}Connection: close\r\n\r\n").as_bytes())
            .await
            .unwrap();
        s.write_all(body).await.unwrap();
    }

    async fn boot(omit_length: bool) -> std::net::SocketAddr {
        let listener = TcpListener::bind("127.0.0.1:0").await.unwrap();
        let addr = listener.local_addr().unwrap();
        tokio::spawn(serve_once(listener, omit_length));
        addr
    }

    #[tokio::test]
    async fn downloads_full_file() {
        let addr = boot(false).await;
        let dir = std::env::temp_dir().join(format!("mdb-dl-{}", std::process::id()));
        let _ = tokio::fs::remove_file(&dir).await;
        let seen = Arc::new(Mutex::new(Vec::new()));
        let seen2 = seen.clone();
        let n = download(
            &format!("http://{addr}/model.gguf"),
            &dir,
            false,
            move |p| seen2.lock().unwrap().push(p.downloaded),
        )
        .await
        .unwrap();
        assert_eq!(n, DATA.len() as u64);
        assert_eq!(tokio::fs::read(&dir).await.unwrap(), DATA);
        let seen = seen.lock().unwrap();
        assert!(!seen.is_empty() && *seen.last().unwrap() == DATA.len() as u64);
        let _ = tokio::fs::remove_file(&dir).await;
    }

    #[tokio::test]
    async fn resumes_partial_file() {
        let addr = boot(false).await;
        let dir = std::env::temp_dir().join(format!("mdb-dl-resume-{}", std::process::id()));
        tokio::fs::write(&dir, &DATA[..6]).await.unwrap();
        let n = download(&format!("http://{addr}/model.gguf"), &dir, true, |_| {})
            .await
            .unwrap();
        assert_eq!(n, DATA.len() as u64);
        assert_eq!(tokio::fs::read(&dir).await.unwrap(), DATA);
        let _ = tokio::fs::remove_file(&dir).await;
    }

    #[tokio::test]
    async fn works_without_content_length() {
        let addr = boot(true).await;
        let dir = std::env::temp_dir().join(format!("mdb-dl-nolen-{}", std::process::id()));
        let _ = tokio::fs::remove_file(&dir).await;
        let n = download(&format!("http://{addr}/model.gguf"), &dir, false, |_| {})
            .await
            .unwrap();
        assert_eq!(n, DATA.len() as u64);
        assert_eq!(tokio::fs::read(&dir).await.unwrap(), DATA);
        let _ = tokio::fs::remove_file(&dir).await;
    }

    #[tokio::test]
    async fn rejects_non_http() {
        let dir = std::env::temp_dir();
        assert!(
            download("https://example.com/x", &dir.join("y"), false, |_| {})
                .await
                .is_err()
        );
    }
}

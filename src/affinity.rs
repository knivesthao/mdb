//! Thread pinning: lock inference work to the phone's Performance cores
//! via `pthread_setaffinity_np` (plan step 7). On non-Android hosts this
//! is a documented no-op so the server stays testable anywhere; the real
//! pinning is proven on-device in step 12.

use std::io;

/// Pin the current thread to the given core ids (e.g. `[4, 5, 6, 7]`).
/// Returns `Ok(())` without doing anything on non-Android targets.
pub fn pin_to_cores(cores: &[usize]) -> io::Result<()> {
    #[cfg(target_os = "android")]
    {
        pin_to_cores_android(cores)
    }
    #[cfg(not(target_os = "android"))]
    {
        let _ = cores;
        Ok(())
    }
}

/// Parse a core list like `"4-7"` or `"4,5,6,7"` into core ids.
pub fn parse_core_list(spec: &str) -> Result<Vec<usize>, String> {
    let mut cores = Vec::new();
    for part in spec.split(',') {
        let part = part.trim();
        if let Some((lo, hi)) = part.split_once('-') {
            let lo: usize = lo.trim().parse().map_err(|_| format!("bad range {part:?}"))?;
            let hi: usize = hi.trim().parse().map_err(|_| format!("bad range {part:?}"))?;
            if lo > hi {
                return Err(format!("inverted range {part:?}"));
            }
            cores.extend(lo..=hi);
        } else if !part.is_empty() {
            cores.push(part.parse().map_err(|_| format!("bad core {part:?}"))?);
        }
    }
    Ok(cores)
}

#[cfg(target_os = "android")]
fn pin_to_cores_android(cores: &[usize]) -> io::Result<()> {
    use std::mem;

    unsafe {
        let mut set: libc::cpu_set_t = mem::zeroed();
        for &core in cores {
            libc::CPU_SET(core, &mut set);
        }
        let rc = libc::sched_setaffinity(0, mem::size_of::<libc::cpu_set_t>(), &set);
        if rc == 0 {
            Ok(())
        } else {
            Err(io::Error::last_os_error())
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parses_ranges_and_lists() {
        assert_eq!(parse_core_list("4-7").unwrap(), vec![4, 5, 6, 7]);
        assert_eq!(parse_core_list("4,5,6,7").unwrap(), vec![4, 5, 6, 7]);
        assert_eq!(parse_core_list("7").unwrap(), vec![7]);
    }

    #[test]
    fn rejects_bad_specs() {
        assert!(parse_core_list("7-4").is_err());
        assert!(parse_core_list("abc").is_err());
        assert!(parse_core_list("4-").is_err());
    }

    #[test]
    fn host_pin_is_noop_ok() {
        // On non-Android this must always succeed without side effects.
        assert!(pin_to_cores(&[0]).is_ok());
    }
}

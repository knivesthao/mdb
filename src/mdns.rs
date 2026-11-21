//! mDNS advertisement (plan step 6): broadcast `mdb.local:8080` so Zed
//! on the LAN finds the phone without typing an IP. USB `adb reverse`
//! remains the reliable primary path; mDNS is best-effort discovery.

use mdns_sd::{ServiceDaemon, ServiceInfo};

pub const SERVICE_TYPE: &str = "_mdb._tcp.local.";
pub const INSTANCE_NAME: &str = "mdb";
pub const HOST_NAME: &str = "mdb.local.";
pub const PORT: u16 = 8080;

/// Registered advertisement; drop it to unpublish.
pub struct Advertiser {
    daemon: ServiceDaemon,
}

impl Advertiser {
    pub fn start(port: u16) -> mdns_sd::Result<Self> {
        let daemon = ServiceDaemon::new()?;
        let info = ServiceInfo::new(SERVICE_TYPE, INSTANCE_NAME, HOST_NAME, "", port, None)?;
        daemon.register(info)?;
        Ok(Self { daemon })
    }
}

impl Drop for Advertiser {
    fn drop(&mut self) {
        let _ = self.daemon.shutdown();
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn service_identifiers() {
        assert!(SERVICE_TYPE.starts_with("_mdb._tcp."));
        assert_eq!(PORT, 8080);
    }
}

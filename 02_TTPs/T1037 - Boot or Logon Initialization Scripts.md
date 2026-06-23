# Boot or Logon Initialization Scripts

## Description

Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence. [1] [2] Initialization scripts can be used to perform administrative functions, which may often execute other programs or send information to an internal logging server. These scripts can vary based on operating system and whether applied locally or remotely.

Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary.

An adversary may also be able to escalate their privileges since some boot or logon initialization scripts run with higher privileges.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0016 | APT29 | APT29 has hijacked legitimate application-specific startup scripts to enable malware to execute on system startup. [1] |
| G0096 | APT41 | APT41 used a hidden shell script in /etc/rc.d/init.d to leverage the ADORE.XSEC backdoor and Adore-NG rootkit. [3] |
| C0046 | ArcaneDoor | ArcaneDoor used malicious boot scripts to install the Line Runner backdoor on victim devices. [4] |
| G0106 | Rocke | Rocke has installed an "init.d" startup script to maintain persistence. [2] |
| S1078 | RotaJakiro | Depending on the Linux distribution and when executing with root permissions, RotaJakiro may install persistence using a .conf file in the /etc/init/ folder. [5] |
| S9024 | SPAWNCHIMERA | SPAWNCHIMERA has modified the boot process files within /tmp/coreboot_fs/bin/init to establish persistence. [6] |
| G1048 | UNC3886 | UNC3886 has attempted to bypass digital signature verification checks at startup by adding a command to the startup config /etc/init.d/localnet within the rootfs.gz archive of both FortiManager and FortiAnalyzer devices. [7] |
| S1217 | VIRTUALPITA | VIRTUALPITA can persist as an init.d startup service on Linux vCenter systems. [8] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1022 | Restrict File and Directory Permissions | Restrict write access to logon scripts to specific administrators. |
| M1024 | Restrict Registry Permissions | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for logon scripts that may lead to persistence. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0112 | Boot or Logon Initialization Scripts Detection Strategy | AN0311 | Monitoring modification and execution of user or system logon scripts such as in registry Run keys or startup folders. |
| AN0312 | Detection of changes or execution of shell initialization scripts like .bashrc, .profile, or /etc/profile for persistence. |  |  |
| AN0313 | Monitoring for modification and execution of login hook scripts or LaunchAgents/LaunchDaemons used for persistence. |  |  |
| AN0314 | Detection of modification to ESXi rc.local.d or rc scripts that are used to execute on boot. |  |  |
| AN0315 | Detection of changes to device startup-config files that include boot scripts or scheduled execution routines. |  |  |

---

## References

- [Mandiant. (2022, May 2). UNC3524: Eye Spy on Your Email. Retrieved August 17, 2023.](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
- [Anomali Labs. (2019, March 15). Rocke Evolves Its Arsenal With a New Malware Family Written in Golang. Retrieved April 24, 2019.](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)
- [Mandiant. (n.d.). APT41, A DUAL ESPIONAGE AND CYBER CRIME OPERATION. Retrieved June 11, 2024.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [Cisco Talos. (2024, April 24). ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices. Retrieved January 6, 2025.](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
- [Alex Turing, Hui Wang. (2021, April 28). RotaJakiro: A long live secret backdoor with 0 VT detection. Retrieved June 14, 2023.](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
- [DHS/CISA. (2026, February 26). MAR-25993211-r1.v2 Ivanti Connect Secure (RESURGE): AR25-087A. Retrieved April 17, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
- [Marvi, A. et al.. (2023, March 16). Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation. Retrieved March 22, 2023.](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
- [Alexander Marvi, Jeremy Koppen, Tufail Ahmed, and Jonathan Lepore. (2022, September 29). Bad VIB(E)s Part One: Investigating Novel Malware Persistence Within ESXi Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)

---

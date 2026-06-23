# Selective Exclusion

## Description

Adversaries may intentionally exclude certain files, folders, directories, file types, or system components from encryption or tampering during a ransomware or malicious payload execution. Some file extensions that adversaries may avoid encrypting include .dll , .exe , and .lnk . [1]

Adversaries may perform this behavior to avoid alerting users, to evade detection by security tools and analysts, or, in the case of ransomware, to ensure that the system remains operational enough to deliver the ransom notice.

Exclusions may target files and components whose corruption would cause instability, break core services, or immediately expose the attack. By carefully avoiding these areas, adversaries maintain system responsiveness while minimizing indicators that could trigger alarms or otherwise inhibit achieving their goals.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S9038 | DynoWiper | DynoWiper has recursively enumerated directories with the exception of the following: System32, Windows, Program Files, Program Files(x86), Temp, Recycle.Bin, $Recycle.Bin, Boot, PerfLogs, AppData, Documents and Settings. [2] [3] |
| S1247 | Embargo | Embargo has avoided encrypting specific files and directories by leveraging a regular expression within the ransomware binary. [4] |
| S1245 | InvisibleFerret | InvisibleFerret has the capability to scan for file names, file extensions, and avoids pre-designated path names and file types. [5] [6] |
| S9039 | LazyWiper | LazyWiper can enumerate the hostname of the system to determine if it is a domain controller and exclude it from being wiped if so. [2] |
| S1244 | Medusa Ransomware | Medusa Ransomware has avoided specified files, file extensions and folders to ensure successful execution of the payload and continued operations of the impacted device. [1] [7] [8] |
| S9030 | SameCoin | SameCoin can avoid overwriting file names that contain "desktop.ini" and "conf.conf." [9] |
| G1055 | VOID MANTICORE | VOID MANTICORE has avoided interacting with specific directories in order to reduce the likelihood of detection. [10] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0897 | Detection of Selective Exclusion | AN2030 | A process with no prior history or outside of known whitelisted tools initiates file or registry modifications to configure exclusion rules for antivirus, backup, or file-handling systems. Or a file system enumeration for specific file names andcritical extensions like .dll, .exe, .sys, or specific directories such as 'Program Files' or security tool paths or system component discovery for the exclusion of the files or components. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0897 | Detection of Selective Exclusion | AN2030 | A process with no prior history or outside of known whitelisted tools initiates file or registry modifications to configure exclusion rules for antivirus, backup, or file-handling systems. Or a file system enumeration for specific file names andcritical extensions like .dll, .exe, .sys, or specific directories such as 'Program Files' or security tool paths or system component discovery for the exclusion of the files or components. |

---

## References

- [Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [ESET. (2026, January 30). DynoWiper update: Technical analysis and attribution. Retrieved April 22, 2026.](https://www.welivesecurity.com/en/eset-research/dynowiper-update-technical-analysis-attribution/)
- [Cyble. (2024, May 24). The Rust Revolution: New Embargo Ransomware Steps In. Retrieved October 19, 2025.](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
- [eSentire Threat Response Unit (TRU). (2024, November 14). Bored BeaverTail & InvisibleFerret Yacht Club – A Lazarus Lure Pt.2. Retrieved October 17, 2025.](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Check Point. (2024, November 12). Hamas-affiliated Threat Actor WIRTE Continues its Middle East Operations and Moves to Disruptive Activity. Retrieved April 20, 2026.](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
- [FBI. (2026, March 20). FBI Flash: FLASH-20260320-001:Government of Iran Cyber Actors Deploy Telegram C2 to Push Malware to Identified Targets. Retrieved April 20, 2026.](https://www.ic3.gov/CSA/2026/260320.pdf)

---

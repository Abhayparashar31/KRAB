# Safe Mode Boot

## Description

Adversaries may abuse Windows safe mode to disable endpoint defenses. Safe mode starts up the Windows operating system with a limited set of drivers and services. Third-party security software such as endpoint detection and response (EDR) tools may not start after booting Windows in safe mode. There are two versions of safe mode: Safe Mode and Safe Mode with Networking. It is possible to start additional services after a safe mode boot. [1] [2]

Adversaries may abuse safe mode to disable endpoint defenses that may not start with a limited boot. Hosts can be forced into safe mode after the next reboot via modifications to Boot Configuration Data (BCD) stores, which are files that manage boot application settings. [3]

Adversaries may also add their malicious applications to the list of minimal services that start in safe mode by modifying relevant Registry values (i.e. Modify Registry ). Malicious Component Object Model (COM) objects may also be registered and loaded in safe mode. [4] [5] [6]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1053 | AvosLocker | AvosLocker can restart a compromised machine in safe mode. [7] [8] |
| S1070 | Black Basta | Black Basta can reboot victim machines in safe mode with networking via bcdedit /set safeboot network . [9] [10] [11] [12] [13] |
| S1247 | Embargo | Embargo has used a DLL variant of MDeployer to disable security solutions through Safe Mode. [14] |
| S1202 | LockBit 3.0 | LockBit 3.0 can reboot the infected host into Safe Mode. [15] |
| S1242 | Qilin | Qilin can reboot targeted systems in safe mode to avoid detection. [16] [17] |
| S1212 | RansomHub | RansomHub can reboot targeted systems into Safe Mode prior to encryption. [18] |
| S0496 | REvil | REvil can force a reboot in safe mode with networking. [6] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1026 | Privileged Account Management | Restrict administrator accounts to as few individuals as possible, following least privilege principles, that may be abused to remotely boot a machine in safe mode. [4] |
| M1054 | Software Configuration | Ensure that endpoint defenses run in safe mode. [4] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0116 | Detection Strategy for Safe Mode Boot Abuse | AN0323 | Abuse of safe mode via BCD modification, boot configuration utilities (bcdedit.exe, bootcfg.exe), and registry persistence under SafeBoot keys. Defender view: suspicious boot configuration changes correlated with registry edits that enable adversary persistence or disable defenses. |

---

## References

- [Microsoft. (n.d.). Retrieved April 15, 2026.](https://support.microsoft.com/en-us/windows/windows-startup-settings-1af6ec8c-4d4a-4b23-adb7-e76eef0b847f)
- [Andrew Brandt. (2019, December 9). Snatch ransomware reboots PCs into Safe Mode to bypass protection. Retrieved April 15, 2026.](https://www.sophos.com/en-us/blog/snatch-ransomware-reboots-pcs-into-safe-mode-to-bypass-protection)
- [Microsoft. (n.d.). Retrieved April 15, 2026.](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit)
- [Naim, D.. (2016, September 15). CyberArk Labs: From Safe Mode to Domain Compromise. Retrieved June 23, 2021.](https://www.cyberark.com/resources/blog/cyberark-labs-from-safe-mode-to-domain-compromise)
- [Cybereason Nocturnus. (n.d.). Cybereason vs. MedusaLocker Ransomware. Retrieved April 15, 2026.](https://www.cybereason.com/blog/research/medusalocker-ransomware)
- [Abrams, L. (2021, March 19). REvil ransomware has a new ‘Windows Safe Mode’ encryption mode. Retrieved June 23, 2021.](https://www.bleepingcomputer.com/news/security/revil-ransomware-has-a-new-windows-safe-mode-encryption-mode/)
- [Trend Micro Research. (2022, April 4). Ransomware Spotlight AvosLocker. Retrieved January 11, 2023.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-avoslocker)
- [Costa, F. (2022, May 1). RaaS AvosLocker Incident Response Analysis. Retrieved January 11, 2023.](https://www.linkedin.com/pulse/raas-avoslocker-incident-response-analysis-fl%C3%A1vio-costa?trk=articles_directory)
- [Zargarov, N. (2022, May 2). New Black Basta Ransomware Hijacks Windows Fax Service. Retrieved March 7, 2023.](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
- [Cyble. (2022, May 6). New ransomware variant targeting high-value organizations. Retrieved November 17, 2024.](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
- [Gonzalez, I., Chavez I., et al. (2022, May 9). Examining the Black Basta Ransomware’s Infection Routine. Retrieved March 7, 2023.](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)
- [Avertium. (2022, June 1). AN IN-DEPTH LOOK AT BLACK BASTA RANSOMWARE. Retrieved March 7, 2023.](https://www.avertium.com/resources/threat-reports/in-depth-look-at-black-basta-ransomware)
- [Elsad, A. (2022, August 25). Threat Assessment: Black Basta Ransomware. Retrieved March 8, 2023.](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)
- [Jan Holman, Tomas Zvara. (2024, October 23). Embargo ransomware: Rock’n’Rust. Retrieved October 19, 2025.](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [Magdy, S. et al. (2022, August 25). New Golang Ransomware Agenda Customizes Attacks. Retrieved September 26, 2025.](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
- [Thomas, W. (2024, June 12). Tracking Adversaries: The Qilin RaaS. Retrieved September 26, 2025.](https://blog.bushidotoken.net/2024/06/tracking-adversaries-qilin-raas.html)
- [Alfano, V. et al. (2025, February 12). RansomHub Never Sleeps Episode 1: The evolution of modern ransomware. Retrieved March 17, 2025.](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)

---

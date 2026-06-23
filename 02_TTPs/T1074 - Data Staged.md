# Data Staged

## Description

Adversaries may stage collected data in a central location or directory prior to Exfiltration. Data may be kept in separate files or combined into one file through techniques such as Archive Collected Data . Interactive command shells may be used, and common functionality within cmd and bash may be used to copy data into a staging location. [1]

In cloud environments, adversaries may stage data within a particular instance or virtual machine before exfiltration. An adversary may Create Cloud Instance and stage data in that instance. [2]

Adversaries may choose to stage data from a victim network in a centralized location prior to Exfiltration to minimize the number of connections made to their C2 server and better evade detection.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1032 | INC Ransom | INC Ransom has staged data on compromised hosts prior to exfiltration. [3] [4] |
| S1020 | Kevin | Kevin can create directories to store logs and other collected data. [5] |
| S0641 | Kobalos | Kobalos can write captured SSH connection credentials to a file under the /var/run directory with a .pid extension for exfiltration. [6] |
| S1076 | QUIETCANARY | QUIETCANARY has the ability to stage data prior to exfiltration. [7] |
| G1015 | Scattered Spider | Scattered Spider stages data in a centralized database prior to exfiltration. [8] |
| S1019 | Shark | Shark has stored information in folders named U1 and U2 prior to exfiltration. [9] |
| G1055 | VOID MANTICORE | VOID MANTICORE has staged compressed files in specified locations prior to exfiltration over C2. [10] |
| G1017 | Volt Typhoon | Volt Typhoon has staged collected data in password-protected archives. [11] |
| G0102 | Wizard Spider | Wizard Spider has collected and staged credentials and network enumeration information, using the networkdll and psfin TrickBot modules. [12] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0014 | Detection of Data Staging Prior to Exfiltration | AN0040 | Detects staging of sensitive files into temporary or public directories, compression with 7zip/WinRAR, or batch copy prior to exfiltration. |
| AN0041 | Detects script or user activity copying files to a central temp or /mnt directory followed by archive/compression utilities. |  |  |
| AN0042 | Detects files collected into user temp or shared directories followed by compression with ditto, zip, or custom scripts. |  |  |
| AN0043 | Detects virtual disk expansion or file copy operations to cloud buckets or mounted volumes from isolated instances. |  |  |
| AN0044 | Detects snapshots or data stored in VMFS volumes from root CLI or remote agents. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0014 | Detection of Data Staging Prior to Exfiltration | AN0040 | Detects staging of sensitive files into temporary or public directories, compression with 7zip/WinRAR, or batch copy prior to exfiltration. |
| AN0041 | Detects script or user activity copying files to a central temp or /mnt directory followed by archive/compression utilities. |  |  |
| AN0042 | Detects files collected into user temp or shared directories followed by compression with ditto, zip, or custom scripts. |  |  |
| AN0043 | Detects virtual disk expansion or file copy operations to cloud buckets or mounted volumes from isolated instances. |  |  |
| AN0044 | Detects snapshots or data stored in VMFS volumes from root CLI or remote agents. |  |  |

---

## References

- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper. Retrieved April 5, 2017.](https://web.archive.org/web/20220224041316/https:/www.pwc.co.uk/cyber-security/pdf/cloud-hopper-report-final-v4.pdf)
- [Mandiant. (2020, February). M-Trends 2020. Retrieved November 17, 2024.](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)
- [Team Huntress. (2023, August 11). Investigating New INC Ransom Group Activity. Retrieved June 5, 2024.](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)
- [SOCRadar. (2024, January 24). Dark Web Profile: INC Ransom. Retrieved June 5, 2024.](https://socradar.io/dark-web-profile-inc-ransom/)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [M.Leveille, M., Sanmillan, I. (2021, January). A WILD KOBALOS APPEARS Tricksy Linux malware goes after HPCs. Retrieved August 24, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [CISA. (2023, November 16). Cybersecurity Advisory: Scattered Spider (AA23-320A). Retrieved March 18, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)
- [ClearSky Cyber Security . (2021, August). New Iranian Espionage Campaign By “Siamesekitten” - Lyceum. Retrieved June 6, 2022.](https://www.clearskysec.com/siamesekitten/)
- [FBI. (2026, March 20). FBI Flash: FLASH-20260320-001:Government of Iran Cyber Actors Deploy Telegram C2 to Push Malware to Identified Targets. Retrieved April 20, 2026.](https://www.ic3.gov/CSA/2026/260320.pdf)
- [Microsoft Threat Intelligence. (2023, May 24). Volt Typhoon targets US critical infrastructure with living-off-the-land techniques. Retrieved July 27, 2023.](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)
- [John, E. and Carvey, H. (2019, May 30). Unraveling the Spiderweb: Timelining ATT&CK Artifacts Used by GRIM SPIDER. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)

---

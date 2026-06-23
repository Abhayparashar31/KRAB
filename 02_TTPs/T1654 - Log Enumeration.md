# Log Enumeration

## Description

Adversaries may enumerate system and service logs to find useful data. These logs may highlight various types of valuable insights for an adversary, such as user authentication records ( Account Discovery ), security or vulnerable software ( Software Discovery ), or hosts within a compromised network ( Remote System Discovery ).

Host binaries may be leveraged to collect system logs. Examples include using wevtutil.exe or PowerShell on Windows to access and/or export security event information. [1] [2] In cloud environments, adversaries may leverage utilities such as the Azure VM Agent’s CollectGuestLogs.exe to collect security logs from cloud hosted infrastructure. [3]

Adversaries may also target centralized logging infrastructure such as SIEMs. Logs may also be bulk exported and sent to adversary-controlled infrastructure for offline analysis.

In addition to gaining a better understanding of the environment, adversaries may also monitor logs in real time to track incident response procedures. This may allow them to adjust their techniques in order to maintain persistence or evade defenses. [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1194 | Akira _v2 | Akira _v2 can enumerate the trace, debug, error, info, and warning logs on targeted systems. [5] [6] |
| G1023 | APT5 | APT5 has used the BLOODMINE utility to parse and extract information from Pulse Secure Connect logs. [7] |
| G0143 | Aquatic Panda | Aquatic Panda enumerated logs related to authentication in Linux environments prior to deleting selective entries for defense evasion purposes. [8] |
| S1246 | BeaverTail | BeaverTail has identified .ldb and .log files stored in browser extension directories for collection and exfiltration. [9] |
| S1159 | DUSTTRAP | DUSTTRAP can identify infected system log information. [10] |
| G1003 | Ember Bear | Ember Bear has enumerated SECURITY and SYSTEM log files during intrusions. [11] |
| S1191 | Megazord | Megazord has the ability to print the trace, debug, error, info, and warning logs. [6] |
| G0129 | Mustang Panda | Mustang Panda has used Wevtutil to gather Windows Security Event Logs. [12] |
| S1091 | Pacu | Pacu can collect CloudTrail event histories and CloudWatch logs. [13] |
| G1017 | Volt Typhoon | Volt Typhoon has used wevtutil.exe and the PowerShell command Get-EventLog security to enumerate Windows logs to search for successful logons. [14] [15] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1018 | User Account Management | Limit the ability to access and export sensitive logs to privileged accounts where possible. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0255 | Detection Strategy for Log Enumeration | AN0705 | Monitor for use of native utilities such as wevtutil.exe or PowerShell cmdlets (Get-WinEvent, Get-EventLog) to enumerate or export logs. Unusual access to security or system event channels, especially by non-administrative users or processes, should be correlated with subsequent file export or network transfer activity. |
| AN0706 | Monitor for suspicious use of commands such as cat, less, grep, or journalctl accessing /var/log/ files. Abnormal enumeration of authentication logs (auth.log, secure) or bulk access to multiple logs in short time windows should be flagged. |  |  |
| AN0707 | Detect abnormal access to unified logs via log show or fs_usage targeting system log files. Monitor for execution of shell utilities (cat, grep) against /var/log/system.log and for plist modifications enabling verbose logging. |  |  |
| AN0708 | Monitor for cloud API calls that export or collect guest or system logs. Abnormal use of Azure VM Agent’s CollectGuestLogs.exe or AWS CloudWatch GetLogEvents across multiple instances should be correlated with lateral movement or data staging. |  |  |
| AN0709 | Monitor ESXi shell or API access to host logs under /var/log/. Abnormal enumeration of vmkernel.log, hostd.log, or vpxa.log by unauthorized accounts should be flagged. |  |  |

---

## References

- [Ruohonen, S. & Robinson, S. (2023, February 2). No Pineapple! -DPRK Targeting of Medical Research and Technology Sector. Retrieved July 10, 2023.](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Lazarus-No-Pineapple-Threat-Intelligence-Report-2023.pdf)
- [Microsoft Threat Intelligence. (2023, June 14). Cadet Blizzard emerges as a novel and distinct Russian threat actor. Retrieved July 10, 2023.](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)
- [Mandiant Intelligence. (2023, May 16). SIM Swapping and Abuse of the Microsoft Azure Serial Console: Serial Is Part of a Well Balanced Attack. Retrieved June 2, 2023.](https://www.mandiant.com/resources/blog/sim-swapping-abuse-azure-serial)
- [Ian Ahl. (2023, May 22). Unmasking GUI-Vil: Financially Motivated Cloud Threat Actor. Retrieved August 30, 2024.](https://permiso.io/blog/s/unmasking-guivil-new-cloud-threat-actor/)
- [Nutland, J. and Szeliga, M. (2024, October 21). Akira ransomware continues to evolve. Retrieved December 10, 2024.](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
- [Zemah, Y. (2024, December 2). Threat Assessment: Howling Scorpius (Akira Ransomware). Retrieved January 8, 2025.](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)
- [Perez, D. et al. (2021, May 27). Re-Checking Your Pulse: Updates on Chinese APT Actors Compromising Pulse Secure VPN Devices. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
- [CrowdStrike. (2023). 2022 Falcon OverWatch Threat Hunting Report. Retrieved May 20, 2024.](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [US Cybersecurity & Infrastructure Security Agency et al. (2024, September 5). Russian Military Cyber Actors Target U.S. and Global Critical Infrastructure. Retrieved September 6, 2024.](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)
- [Lior Rochberger, Tom Fakterman, Robert Falcone. (2023, September 22). Cyberespionage Attacks Against Southeast Asian Government Linked to Stately Taurus, Aka Mustang Panda. Retrieved September 9, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)
- [Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.](https://github.com/RhinoSecurityLabs/pacu)
- [NSA et al. (2023, May 24). People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection. Retrieved July 27, 2023.](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)

---

# Direct Volume Access

## Description

Adversaries may directly access a volume to bypass file access controls and file system monitoring. Windows allows programs to have direct access to logical volumes. Programs with direct access may read and write files directly from the drive by analyzing file system data structures. This technique may bypass Windows file access controls as well as file system monitoring tools. [1]

Utilities, such as NinjaCopy , exist to perform these actions in PowerShell. [2] Adversaries may also use built-in or third-party utilities (such as vssadmin , wbadmin , and esentutl ) to create shadow copies or backups of data from system volumes. [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries copied volume shadow copies through executing vssadmin in order to dump the NTDS.dit file. [4] |
| C0051 | APT28 Nearest Neighbor Campaign | During APT28 Nearest Neighbor Campaign , APT28 accessed volume shadow copies through executing vssadmin in order to dump the NTDS.dit file. [5] |
| S0404 | esentutl | esentutl can use the Volume Shadow Copy service to copy locked files such as ntds.dit . [3] [6] |
| G1015 | Scattered Spider | Scattered Spider has created volume shadow copies of virtual domain controller disks to extract the NTDS.dit file. [7] |
| G1017 | Volt Typhoon | Volt Typhoon has executed the Windows-native vssadmin command to create volume shadow copies. [8] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1040 | Behavior Prevention on Endpoint | Some endpoint security solutions can be configured to block some types of behaviors related to efforts by an adversary to create backups, such as command execution or preventing API calls to backup related services. |
| M1018 | User Account Management | Ensure only accounts required to configure and manage backups have the privileges to do so. Monitor these accounts for unauthorized backup activity. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0426 | Detection of Direct Volume Access for File System Evasion | AN1193 | Processes accessing raw logical drives (e.g., .\C:) to bypass file system protections or directly manipulate data structures. |
| AN1194 | CLI or automated utilities accessing raw device volumes or flash storage directly (e.g., via copy flash: , format , or partition commands). |  |  |

---

## References

- [Hakobyan, A. (2009, January 8). FDump - Dumping File Sectors Directly from Disk using Logical Offsets. Retrieved November 12, 2014.](http://www.codeproject.com/Articles/32169/FDump-Dumping-File-Sectors-Directly-from-Disk-usin)
- [Bialek, J. (2015, December 16). Invoke-NinjaCopy.ps1. Retrieved June 2, 2016.](https://github.com/PowerShellMafia/PowerSploit/blob/master/Exfiltration/Invoke-NinjaCopy.ps1)
- [LOLBAS. (n.d.). Esentutl.exe. Retrieved September 3, 2019.](https://lolbas-project.github.io/lolbas/Binaries/Esentutl/)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Koessel, Sean. Adair, Steven. Lancaster, Tom. (2024, November 22). The Nearest Neighbor Attack: How A Russian APT Weaponized Nearby Wi-Fi Networks for Covert Access. Retrieved February 25, 2025.](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)
- [Cary, M. (2018, December 6). Locked File Access Using ESENTUTL.exe. Retrieved September 5, 2019.](https://dfironthemountain.wordpress.com/2018/12/06/locked-file-access-using-esentutl-exe/)
- [Microsoft. (2023, October 25). Octo Tempest crosses boundaries to facilitate extortion, encryption, and destruction. Retrieved March 18, 2024.](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)

---

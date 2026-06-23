# Permission Groups Discovery

## Description

Adversaries may attempt to discover group and permission settings. This information can help adversaries determine which user accounts and groups are available, the membership of users in particular groups, and which users and groups have elevated permissions.

Adversaries may attempt to discover group permission settings in many different ways. This data may provide the adversary with information about the compromised environment that can be used in follow-on activity and targeting. [1]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0022 | APT3 | APT3 has a tool that can enumerate the permissions associated with Windows groups. [2] |
| G0096 | APT41 | APT41 used net group commands to enumerate various Windows user groups and permissions. [3] |
| S0335 | Carbon | Carbon uses the net group command. [4] |
| G1016 | FIN13 | FIN13 has enumerated all users and roles from a victim's main treasury system. [5] |
| S0483 | IcedID | IcedID has the ability to identify Workgroup membership. [6] |
| S0233 | MURKYTOP | MURKYTOP has the capability to retrieve information about groups. [7] |
| G1015 | Scattered Spider | Scattered Spider has enumerated the vSphere Admins and ESX Admins groups in targeted environments. [8] |
| S0445 | ShimRatReporter | ShimRatReporter gathered the local privileges for the infected host. [9] |
| S0623 | Siloscape | Siloscape checks for Kubernetes node permissions. [10] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 used the Get-ManagementRoleAssignment PowerShell cmdlet to enumerate Exchange management role assignments through an Exchange Management Shell. [11] |
| G0092 | TA505 | TA505 has used TinyMet to enumerate members of privileged groups. [12] TA505 has also run net group /domain . [13] |
| S0266 | TrickBot | TrickBot can identify the groups the user on a compromised host belongs to. [14] |
| G1017 | Volt Typhoon | Volt Typhoon has used commercial tools, LOTL utilities, and appliances already present on the system for group and user discovery. [15] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0179 | Behavioral Detection of Permission Groups Discovery | AN0507 | Detection of adversary enumeration of domain or local group memberships via native tools such as net.exe, PowerShell, or WMI. This activity may precede lateral movement or privilege escalation. |
| AN0508 | Detection of group enumeration using commands like 'id', 'groups', or 'getent group', often followed by privilege escalation or SSH lateral movement. |  |  |
| AN0509 | Group membership checks via 'dscl', 'dscacheutil', or 'id', typically executed via terminal or automation scripts. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0179 | Behavioral Detection of Permission Groups Discovery | AN0507 | Detection of adversary enumeration of domain or local group memberships via native tools such as net.exe, PowerShell, or WMI. This activity may precede lateral movement or privilege escalation. |
| AN0508 | Detection of group enumeration using commands like 'id', 'groups', or 'getent group', often followed by privilege escalation or SSH lateral movement. |  |  |
| AN0509 | Group membership checks via 'dscl', 'dscacheutil', or 'id', typically executed via terminal or automation scripts. |  |  |

---

## References

- [Red Team Labs. (2018, April 24). Hidden Administrative Accounts: BloodHound to the Rescue. Retrieved October 28, 2020.](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)
- [Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
- [Nikita Rostovcev. (2022, August 18). APT41 World Tour 2021 on a tight schedule. Retrieved February 22, 2024.](https://www.group-ib.com/blog/apt41-world-tour-2021/)
- [GovCERT. (2016, May 23). Technical Report about the Espionage Case at RUAG. Retrieved November 7, 2018.](https://web.archive.org/web/20170718174931/https://www.melani.admin.ch/dam/melani/de/dokumente/2016/technical%20report%20ruag.pdf.download.pdf/Report_Ruag-Espionage-Case.pdf)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [Kessem, L., et al. (2017, November 13). New Banking Trojan IcedID Discovered by IBM X-Force Research. Retrieved July 14, 2020.](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [Mandiant Incident Response. (2025, July 23). From Help Desk to Hypervisor: Defending Your VMware vSphere Estate from UNC3944. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Prizmant, D. (2021, June 7). Siloscape: First Known Malware Targeting Windows Containers to Compromise Cloud Environments. Retrieved June 9, 2021.](https://unit42.paloaltonetworks.com/siloscape/)
- [Cash, D. et al. (2020, December 14). Dark Halo Leverages SolarWinds Compromise to Breach Organizations. Retrieved December 29, 2020.](https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/)
- [Frydrych, M. (2020, April 14). TA505 Continues to Infect Networks With SDBbot RAT. Retrieved May 29, 2020.](https://web.archive.org/web/20200420201624/https://securityintelligence.com/posts/ta505-continues-to-infect-networks-with-sdbbot-rat/)
- [Hiroaki, H. and Lu, L. (2019, June 12). Shifting Tactics: Breaking Down TA505 Group’s Use of HTML, RATs and Other Techniques in Latest Campaigns. Retrieved May 29, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/shifting-tactics-breaking-down-ta505-groups-use-of-html-rats-and-other-techniques-in-latest-campaigns/)
- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)

---

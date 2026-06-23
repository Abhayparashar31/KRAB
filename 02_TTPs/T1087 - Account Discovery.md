# Account Discovery

## Description

Adversaries may attempt to get a listing of valid accounts, usernames, or email addresses on a system or within a compromised environment. This information can help adversaries determine which accounts exist, which can aid in follow-on behavior such as brute-forcing, spear-phishing attacks, or account takeovers (e.g., Valid Accounts ).

Adversaries may use several methods to enumerate accounts, including abuse of existing tools, built-in commands, and potential misconfigurations that leak account names and roles or permissions in the targeted environment.

For examples, cloud environments typically provide easily accessible interfaces to obtain user lists. [1] [2] On hosts, adversaries can use default PowerShell and other command line functionality to identify accounts. Information about email addresses and accounts may also be extracted by searching an infected system’s files.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0062 | Anthropic AI-orchestrated Campaign | During the Anthropic AI-orchestrated Campaign , the adversary used Claude Code to query internal database user account tables to enumerate accounts and identify high-privilege accounts within compromised environments. [3] |
| G0143 | Aquatic Panda | Aquatic Panda used the last command in Linux environments to identify recently logged-in users on victim machines. [4] |
| G1016 | FIN13 | FIN13 has enumerated all users and their roles from a victim's main treasury system. [5] |
| S1229 | Havoc | Havoc can identify privileged user accounts on infected systems. [6] |
| G1015 | Scattered Spider | Scattered Spider has identified vSphere administrator accounts. [7] |
| S0445 | ShimRatReporter | ShimRatReporter listed all non-privileged and privileged accounts available on the machine. [8] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 obtained a list of users and their roles from an Exchange server using Get-ManagementRoleAssignment . [9] |
| S1239 | TONESHELL | TONESHELL included functionality to retrieve a list of user accounts. [10] |
| S1065 | Woody RAT | Woody RAT can identify administrator accounts on an infected machine. [11] |
| S0658 | XCSSET | XCSSET attempts to discover accounts from various locations such as a user's Evernote, AppleID, Telegram, Skype, and WeChat data. [12] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1028 | Operating System Configuration | Prevent administrator accounts from being enumerated when an application is elevating through UAC since it can lead to the disclosure of account names. The Registry key is located HKLM\ SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\CredUI\EnumerateAdministrators . It can be disabled through GPO: Computer Configuration > [Policies] > Administrative Templates > Windows Components > Credential User Interface: E numerate administrator accounts on elevation. [13] |
| M1018 | User Account Management | Manage the creation, modification, use, and permissions associated to user accounts. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0587 | Enumeration of User or Account Information Across Platforms | AN1612 | Detection of processes performing local or domain account enumeration by invoking account directory queries or security APIs followed by structured output of account lists. The defender observes command execution or API invocation patterns that retrieve account information and produce enumeration artifacts shortly afterward. |
| AN1613 | Enumeration of users and groups through suspicious shell commands or unauthorized access to /etc/passwd or /etc/shadow. |  |  |
| AN1614 | Detection of account enumeration through directory service queries or system utilities accessing account metadata stores, followed by structured enumeration output. |  |  |
| AN1615 | Detection of enumeration of identity entities through cloud provider APIs where principals retrieve account metadata such as IAM users or roles in rapid succession. |  |  |
| AN1616 | Detection of identity directory enumeration through API calls or administrative queries retrieving multiple account objects within a short interval. |  |  |
| AN1617 | Detection of enumeration activity when system processes query ESXi host account configuration or management APIs to retrieve user account listings. |  |  |
| AN1618 | Account enumeration via bulk access to user directory features or hidden APIs. |  |  |
| AN1619 | Account discovery via VBA macros, COM objects, or embedded scripting. |  |  |

---

## References

- [Amazon. (n.d.). List Users. Retrieved August 11, 2020.](https://docs.aws.amazon.com/cli/latest/reference/iam/list-users.html)
- [Google. (2020, June 23). gcloud iam service-accounts list. Retrieved August 4, 2020.](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list)
- [Anthropic. (2025, November). Disrupting the first reported AI-orchestrated cyber espionage campaign. Retrieved April 20, 2026.](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
- [CrowdStrike. (2023). 2022 Falcon OverWatch Threat Hunting Report. Retrieved May 20, 2024.](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [Wan, Y. (2025, March 3). Havoc: SharePoint with Microsoft Graph API turns into FUD C2. Retrieved August 4, 2025.](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)
- [Mandiant Incident Response. (2025, July 23). From Help Desk to Hypervisor: Defending Your VMware vSphere Estate from UNC3944. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Cash, D. et al. (2020, December 14). Dark Halo Leverages SolarWinds Compromise to Breach Organizations. Retrieved December 29, 2020.](https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: ToneShell and StarProxy | P1. Retrieved July 21, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Mac Threat Response, Mobile Research Team. (2020, August 13). The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSS Backdoor Planting in Safari, and Leverages Two Zero-day Exploits. Retrieved October 5, 2021.](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
- [UCF. (n.d.). The system must require username and password to elevate a running application.. Retrieved December 18, 2017.](https://www.stigviewer.com/stig/microsoft_windows_server_2012_member_server/2013-07-25/finding/WN12-CC-000077)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Lapsus$]] [related_actor:: [[Lapsus$]]]

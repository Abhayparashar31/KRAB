# Account Manipulation

## Description

Adversaries may manipulate accounts to maintain and/or elevate access to victim systems. Account manipulation may consist of any action that preserves or modifies adversary access to a compromised account, such as modifying credentials or permission groups. [1] These actions could also include account activity designed to subvert security policies, such as performing iterative password updates to bypass password duration policies and preserve the life of compromised credentials.

In order to create or manipulate accounts, the adversary must already have sufficient permissions on systems or the domain. However, account manipulation may also lead to privilege escalation where modifications grant access to additional roles, permissions, or higher-privileged Valid Accounts .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0025 | 2016 Ukraine Electric Power Attack | During the 2016 Ukraine Electric Power Attack , Sandworm Team used the sp_addlinkedsrvlogin command in MS-SQL to create a link between a created account and other servers in the network. [2] |
| S0274 | Calisto | Calisto adds permissions and remote logins to all users. [3] |
| G0125 | HAFNIUM | HAFNIUM has granted privileges to domain accounts and reset the password for default admin accounts. [4] [5] |
| G0032 | Lazarus Group | Lazarus Group malware WhiskeyDelta-Two contains a function that attempts to rename the administrator’s account. [6] [7] |
| S0002 | Mimikatz | The Mimikatz credential dumper has been extended to include Skeleton Key domain controller authentication bypass functionality. The LSADUMP::ChangeNTLM and LSADUMP::SetNTLM modules can also manipulate the password hash of an account without knowing the clear text value. [8] [9] |
| G1015 | Scattered Spider | Scattered Spider has added accounts to the ESX Admins group to grant them full admin rights in vSphere. [10] |
| S9008 | Shai-Hulud | Shai-Hulud has modified GitHub account settings for private repositories and changed them to public. [11] [12] [13] [14] |
| G1055 | VOID MANTICORE | VOID MANTICORE has leveraged access to administrative control systems to achieve disruptive effects, consistent with administrative account abuse or privilege escalation within existing access. [15] [16] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1042 | Disable or Remove Feature or Program | Remove unnecessary and potentially abusable authentication and authorization mechanisms where possible. |
| M1032 | Multi-factor Authentication | Use multi-factor authentication for user and privileged accounts. |
| M1030 | Network Segmentation | Configure access controls and firewalls to limit access to critical systems and domain controllers. Most cloud environments support separate virtual private cloud (VPC) instances that enable further segmentation of cloud systems. |
| M1028 | Operating System Configuration | Protect domain controllers by ensuring proper security configuration for critical servers to limit access by potentially unnecessary protocols and services, such as SMB file sharing. |
| M1026 | Privileged Account Management | Do not allow domain administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| M1022 | Restrict File and Directory Permissions | Restrict access to potentially sensitive files that deal with authentication and/or authorization. |
| M1018 | User Account Management | Ensure that low-privileged user accounts do not have permissions to modify accounts or account-related policies. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0096 | Account Manipulation Behavior Chain Detection | AN0265 | Account attribute changes (e.g., password set, group membership, servicePrincipalName, logon hours) correlated with unusual process lineage or timing, indicating privilege escalation or persistence via valid accounts. |
| AN0266 | Use of native tools or scripting (e.g., usermod , passwd , groupmod ) to escalate permissions or persist access on existing users, correlated with login or process events. |  |  |
| AN0267 | Modifications to user accounts via dscl , pwpolicy , or System Preferences CLI ( sysadminctl ) that alter user groups, enable root, or bypass MDM restrictions. |  |  |
| AN0268 | Modifications to SSO/SAML user attributes (e.g., isAdmin , role , MFA bypass, App assignments) often through CLI, API, or rogue IdP apps. |  |  |
| AN0269 | Addition of new users or changes to role permissions (e.g., ReadOnly -> Admin) via API or vSphere Client, particularly from non-jumpbox IPs. |  |  |
| AN0270 | Role escalation (e.g., Editor → Owner) in cloud collaboration tools (Google Workspace, O365) or file sharing apps to maintain elevated access. |  |  |

---

## References

- [FireEye. (2021, June 16). Smoking Out a DARKSIDE Affiliate’s Supply Chain Software Compromise. Retrieved September 22, 2021.](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
- [Joe Slowik. (2018, October 12). Anatomy of an Attack: Detecting and Defeating CRASHOVERRIDE. Retrieved December 18, 2020.](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)
- [Pantig, J. (2018, July 30). OSX.Calisto. Retrieved September 7, 2018.](https://web.archive.org/web/20190111082249/https://www.symantec.com/security-center/writeup/2018-073014-2512-99?om_rssid=sr-latestthreats30days)
- [Gruzweig, J. et al. (2021, March 2). Operation Exchange Marauder: Active Exploitation of Multiple Zero-Day Microsoft Exchange Vulnerabilities. Retrieved March 3, 2021.](https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/)
- [Microsoft Threat Intelligence . (2025, March 5). Silk Typhoon targeting IT supply chain. Retrieved March 20, 2025.](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved November 17, 2024.](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)
- [Metcalf, S. (2015, November 13). Unofficial Guide to Mimikatz & Command Reference. Retrieved December 23, 2015.](https://adsecurity.org/?page_id=1821)
- [Metcalf, S. (2015, January 19). Attackers Can Now Use Mimikatz to Implant Skeleton Key on Domain Controllers & BackDoor Your Active Directory Forest. Retrieved February 3, 2015.](http://adsecurity.org/?p=1275)
- [Mandiant Incident Response. (2025, July 23). From Help Desk to Hypervisor: Defending Your VMware vSphere Estate from UNC3944. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)
- [Charlie Eriksen. (2025, September 16). S1ngularity/nx attackers strike again. Retrieved April 9, 2026.](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
- [Gianpietro Cutolo. (2025, November 26). Shai-Hulud 2.0: Aggressive, Automated, and Fast Spreading. Retrieved April 9, 2026.](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
- [Merav Bar, Rami McCarthy, Barak Sharoni. (2025, September 16). Shai-Hulud: Ongoing Package Supply Chain Worm Delivering Data-Stealing Malware. Retrieved April 9, 2026.](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)
- [Microsoft Defender Security Team. (n.d.). Shai-Hulud 2.0: Guidance for detecting, investigating, and defending against the supply chain attack. Retrieved April 9, 2026.](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/)
- [DomainTools Investigations. (2026, April 6). Handala: MOIS Linked Cyber Influence Ecosystem Threat Intelligence Assessment. Retrieved April 20, 2026.](https://dti.domaintools.com/research/handala-mois-linked-cyber-influence-ecosystem-threat-intelligence-assessment)
- [Troy Bettencourt. (2026, March 20). SEC 8k: Stryker Corporation Partner and Customer Connections to the Stryker Environment. Retrieved April 20, 2026.](https://www.sec.gov/Archives/edgar/data/310764/000119312526118634/d94012dex991.htm)

---

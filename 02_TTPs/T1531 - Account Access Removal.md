# Account Access Removal

## Description

Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utilized by legitimate users. Accounts may be deleted, locked, or manipulated (ex: changed credentials, revoked permissions for SaaS platforms such as Sharepoint) to remove access to accounts. [1] Adversaries may also subsequently log off and/or perform a System Shutdown/Reboot to set malicious changes into place. [2] [3]

In Windows, Net utility, Set-LocalUser and Set-ADAccountPassword PowerShell cmdlets may be used by adversaries to modify user accounts. Accounts could also be disabled by Group Policy. In Linux, the passwd utility may be used to change passwords. On ESXi servers, accounts can be removed or modified via esxcli ( system account set , system account remove ).

Adversaries who use ransomware or similar attacks may first perform this and other Impact behaviors, such as Data Destruction and Defacement , in order to impede incident response/recovery before completing the Data Encrypted for Impact objective.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1024 | Akira | Akira deletes administrator accounts in victim networks prior to encryption. [4] |
| S1134 | DEADWOOD | DEADWOOD changes the password for local and domain users via net.exe to a random 32 character string to prevent these accounts from logging on. Additionally, DEADWOOD will terminate the winlogon.exe process to prevent attempts to log on to the infected system. [5] |
| G1004 | LAPSUS$ | LAPSUS$ has removed a targeted organization's global admin accounts to lock the organization out of all access. [6] |
| S0372 | LockerGoga | LockerGoga has been observed changing account passwords and logging off current users. [2] [3] |
| S0576 | MegaCortex | MegaCortex has changed user account passwords and logged users off the system. [7] |
| S0688 | Meteor | Meteor has the ability to change the password of local users on compromised hosts and can log off users. [8] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0120 | Account Access Removal via Multi-Platform Audit Correlation | AN0334 | Correlated user account modification (reset, disable, deletion) events with anomalous process lineage (e.g., PowerShell or net.exe from an interactive session), especially outside of IT admin change windows or by non-admin users. |
| AN0335 | Password changes or account deletions via 'passwd', 'userdel', or 'chage' preceded by interactive shell or remote command execution from non-privileged accounts. |  |  |
| AN0336 | Execution of dscl or sysadminctl commands to disable, delete, or modify users combined with anomalous process ancestry or terminal session launch. |  |  |
| AN0337 | Invocation of esxcli 'system account remove' from vCLI, SSH, or vSphere API with anomalous user access or outside maintenance windows. |  |  |
| AN0338 | O365 UnifiedAuditLog entries for Remove-Mailbox or Set-Mailbox with account disable or delete actions correlated with suspicious login locations or MFA bypass. |  |  |
| AN0339 | Deletion or disablement of user accounts in platforms like Okta, Salesforce, or Zoom with anomalies in admin session attributes or mass actions within short duration. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0120 | Account Access Removal via Multi-Platform Audit Correlation | AN0334 | Correlated user account modification (reset, disable, deletion) events with anomalous process lineage (e.g., PowerShell or net.exe from an interactive session), especially outside of IT admin change windows or by non-admin users. |
| AN0335 | Password changes or account deletions via 'passwd', 'userdel', or 'chage' preceded by interactive shell or remote command execution from non-privileged accounts. |  |  |
| AN0336 | Execution of dscl or sysadminctl commands to disable, delete, or modify users combined with anomalous process ancestry or terminal session launch. |  |  |
| AN0337 | Invocation of esxcli 'system account remove' from vCLI, SSH, or vSphere API with anomalous user access or outside maintenance windows. |  |  |
| AN0338 | O365 UnifiedAuditLog entries for Remove-Mailbox or Set-Mailbox with account disable or delete actions correlated with suspicious login locations or MFA bypass. |  |  |
| AN0339 | Deletion or disablement of user accounts in platforms like Okta, Salesforce, or Zoom with anomalies in admin session attributes or mass actions within short duration. |  |  |

---

## References

- [Obsidian Threat Research Team. (2023, June 6). SaaS Ransomware Observed in the Wild for Sharepoint in Microsoft 365. Retrieved October 5, 2025.](https://web.archive.org/web/20230608061141/https://www.obsidiansecurity.com/blog/saas-ransomware-observed-sharepoint-microsoft-365/)
- [CarbonBlack Threat Analysis Unit. (2019, March 22). TAU Threat Intelligence Notification – LockerGoga Ransomware. Retrieved April 16, 2019.](https://www.carbonblack.com/2019/03/22/tau-threat-intelligence-notification-lockergoga-ransomware/)
- [Harbison, M. (2019, March 26). Born This Way? Origins of LockerGoga. Retrieved April 16, 2019.](https://unit42.paloaltonetworks.com/born-this-way-origins-of-lockergoga/)
- [Secureworks. (n.d.). GOLD SAHARA. Retrieved February 20, 2024.](https://www.secureworks.com/research/threat-profiles/gold-sahara)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [MSTIC, DART, M365 Defender. (2022, March 24). DEV-0537 Criminal Actor Targeting Organizations for Data Exfiltration and Destruction. Retrieved May 17, 2022.](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)
- [Del Fierro, C. Kessem, L.. (2020, January 8). From Mega to Giga: Cross-Version Comparison of Top MegaCortex Modifications. Retrieved February 15, 2021.](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
- [Check Point Research Team. (2021, August 14). Indra - Hackers Behind Recent Attacks on Iran. Retrieved February 17, 2022.](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)

---

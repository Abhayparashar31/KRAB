# Create Account

## Description

Adversaries may create an account to maintain access to victim systems. [1] With a sufficient level of access, creating such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools to be deployed on the system.

Accounts may be created on the local system or within a domain or cloud tenant. In cloud environments, adversaries may create accounts that only have access to specific services, which can reduce the chance of detection.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0025 | 2016 Ukraine Electric Power Attack | During the 2016 Ukraine Electric Power Attack , Sandworm Team added a login to a SQL Server with sp_addlinkedsrvlogin . [2] |
| G0119 | Indrik Spider | Indrik Spider used wmic.exe to add a new user to the system. [1] |
| S1199 | LockBit 2.0 | LockBit 2.0 has been observed creating accounts for persistence using simple names like "a". [3] |
| G1045 | Salt Typhoon | Salt Typhoon has created Linux-level users on compromised network devices through modification of /etc/shadow and /etc/passwd . [4] |
| G1015 | Scattered Spider | Scattered Spider creates new user identities within the compromised organization. [5] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1032 | Multi-factor Authentication | Use multi-factor authentication for user and privileged accounts. |
| M1030 | Network Segmentation | Configure access controls and firewalls to limit access to domain controllers and systems used to create and manage accounts. |
| M1028 | Operating System Configuration | Protect domain controllers by ensuring proper security configuration for critical servers. |
| M1026 | Privileged Account Management | Limit the number of accounts with permissions to create other accounts. Do not allow domain administrator accounts to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0583 | Detection Strategy for T1136 - Create Account across platforms | AN1604 | Adversary uses built-in OS tools or API calls to create local or domain accounts for persistence or lateral movement. Tools such as 'net user', PowerShell, or MMC snap-ins may be used. Detection focuses on Event ID 4720 paired with process lineage and user context. |
| AN1605 | Adversary invokes 'useradd', 'adduser', or equivalent system commands or scripts to create local users. Detection focuses on command execution and audit trail of passwd/shadow file modifications. |  |  |
| AN1606 | Adversary creates new users using 'dscl' commands, GUI tools, or by modifying user plist files. Detection includes monitoring dscl invocation and user-related plist changes. |  |  |
| AN1607 | Adversary creates users via IAM/IdP API or portal (e.g., Azure AD, Okta). Detection involves monitoring API calls, admin action logs, and correlation with role assignments. |  |  |
| AN1608 | Account creation via cloud service APIs or CLI, often associated with key generation. Monitored via CloudTrail or equivalent audit logs. |  |  |

---

## References

- [Symantec Threat Intelligence. (2020, June 25). WastedLocker: Symantec Identifies Wave of Attacks Against U.S. Organizations. Retrieved May 20, 2021.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)
- [Joe Slowik. (2018, October 12). Anatomy of an Attack: Detecting and Defeating CRASHOVERRIDE. Retrieved December 18, 2020.](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)
- [Elsad, A. et al. (2022, June 9). LockBit 2.0: How This RaaS Operates and How to Protect Against It. Retrieved January 24, 2025.](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
- [Cisco Talos. (2025, February 20). Weathering the storm: In the midst of a Typhoon. Retrieved February 24, 2025.](https://blog.talosintelligence.com/salt-typhoon-analysis/)
- [CISA. (2023, November 16). Cybersecurity Advisory: Scattered Spider (AA23-320A). Retrieved March 18, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)

---

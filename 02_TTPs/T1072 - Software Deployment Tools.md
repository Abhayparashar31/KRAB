# Software Deployment Tools

## Description

Adversaries may gain access to and use centralized software suites installed within an enterprise to execute commands and move laterally through the network. Configuration management and software deployment applications may be used in an enterprise network or cloud environment for routine administration purposes. These systems may also be integrated into CI/CD pipelines. Examples of such solutions include: SCCM, HBSS, Altiris, AWS Systems Manager, Microsoft Intune, Azure Arc, and GCP Deployment Manager.

Access to network-wide or enterprise-wide endpoint management software may enable an adversary to achieve remote code execution on all connected systems. The access may be used to laterally move to other systems, gather information, or cause a specific effect, such as wiping the hard drives on all endpoints.

SaaS-based configuration management services may allow for broad Cloud Administration Command on cloud-hosted instances, as well as the execution of arbitrary commands on on-premises endpoints. For example, Microsoft Configuration Manager allows Global or Intune Administrators to run scripts as SYSTEM on on-premises devices joined to Entra ID. [1] Such services may also utilize Web Protocols to communicate back to adversary owned infrastructure. [2]

Network infrastructure devices may also have configuration management tools that can be similarly abused by adversaries. [3]

The permissions required for this action vary by system configuration; local credentials may be sufficient with direct access to the third-party system, or specific domain credentials may be required. However, the system may require an administrative account to log in or to access specific functionality.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0050 | APT32 | APT32 compromised McAfee ePO to move laterally by distributing malware as a software deployment task. [4] |
| C0018 | C0018 | During C0018 , the threat actors used PDQ Deploy to move AvosLocker and tools across the network. [5] |
| G1051 | Medusa Group | Medusa Group has utilized software deployment and management solutions to deploy their encryption payload to include BigFix and PDQ Deploy. [6] |
| G0129 | Mustang Panda | Mustang Panda has leveraged legitimate software tools such as AntiVirus Agents, Security Services, and App Development tools to execute scripts and to side-load dlls. [7] [8] |
| G0034 | Sandworm Team | Sandworm Team has used the commercially available tool RemoteExec for agentless remote code execution. [9] |
| G0091 | Silence | Silence has used RAdmin, a remote software tool used to remotely control workstations and ATMs. [10] |
| G0028 | Threat Group-1314 | Threat Group-1314 actors used a victim's endpoint management platform, Altiris, for lateral movement. [11] |
| G1055 | VOID MANTICORE | VOID MANTICORE has leveraged legitimate built-in features of cloud-based management platforms to include mobile device management (MDM) and Remote Monitoring and Management (RMM) solutions. [12] [13] VOID MANTICORE has also initiated built-in remote wipe instructions using a privileged account within Microsoft Intune. [12] [13] |
| S0041 | Wiper | It is believed that a patch management system for an anti-virus product commonly installed among targeted companies was used to distribute the Wiper malware. [14] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1015 | Active Directory Configuration | Ensure proper system and access isolation for critical network systems through use of group policy. |
| M1033 | Limit Software Installation | Restrict the use of third-party software suites installed within an enterprise network. |
| M1032 | Multi-factor Authentication | Ensure proper system and access isolation for critical network systems through use of multi-factor authentication. |
| M1030 | Network Segmentation | Ensure proper system isolation for critical network systems through use of firewalls. |
| M1027 | Password Policies | Verify that account credentials that may be used to access deployment systems are unique and not used throughout the enterprise network. |
| M1026 | Privileged Account Management | Grant access to application deployment systems only to a limited number of authorized administrators. |
| M1029 | Remote Data Storage | If the application deployment system can be configured to deploy only signed binaries, then ensure that the trusted signing certificates are not co-located with the application deployment system and are instead located on a system that cannot be accessed remotely or to which remote access is tightly controlled. |
| M1051 | Update Software | Patch deployment systems regularly to prevent potential remote access through Exploitation for Privilege Escalation . |
| M1018 | User Account Management | Ensure that any accounts used by third-party providers to access these systems are traceable to the third-party and are not used throughout the network or used by other third-party providers in the same environment. Ensure there are regular reviews of accounts provisioned to these systems to verify continued business need, and ensure there is governance to trace de-provisioning of access that is no longer required. Ensure proper system and access isolation for critical network systems through use of account privilege separation. |
| M1017 | User Training | Have a strict approval policy for use of deployment systems. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0223 | Detection of Adversary Abuse of Software Deployment Tools | AN0623 | Detects SCCM, Intune, or remote push execution spawning scripts or binaries from SYSTEM context or unusual consoles (e.g., cmtrace.exe launching PowerShell or cmd.exe). |
| AN0624 | Detects remote scripts or binaries deployed via Puppet, Chef, Ansible, or shell scripts from orchestration servers executing outside maintenance windows or in unmanaged nodes. |  |  |
| AN0625 | Detects script or binary execution initiated via JAMF, Munki, or custom MDM agents outside of baseline, or JAMF launching new Terminal or osascript processes from remote command payloads. |  |  |
| AN0626 | Detects cloud-native software deployment or management (e.g., SSM Run Command, Intune) initiating script execution on endpoints outside expected org IDs, admin groups, or maintenance windows. |  |  |
| AN0627 | Detects central router or switch config management tools (e.g., FortiManager, Cisco Prime) triggering device reboots or config pushes using abnormal accounts or IPs. |  |  |

---

## References

- [Andy Robbins. (2020, August 17). Death from Above: Lateral Movement from Azure to On-Prem AD. Retrieved March 13, 2023.](https://posts.specterops.io/death-from-above-lateral-movement-from-azure-to-on-prem-ad-d18cb3959d4d)
- [Ariel Szarf, Or Aspir. (n.d.). Mitiga Security Advisory: Abusing the SSM Agent as a Remote Access Trojan. Retrieved January 31, 2024.](https://www.mitiga.io/blog/mitiga-security-advisory-abusing-the-ssm-agent-as-a-remote-access-trojan)
- [ALEXANDER MARVI, BRAD SLAYBAUGH, DAN EBREO, TUFAIL AHMED, MUHAMMAD UMAIR, TINA JOHNSON. (2023, March 16). Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
- [Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
- [Venere, G. Neal, C. (2022, June 21). Avos ransomware group expands with new attack arsenal. Retrieved January 11, 2023.](https://blog.talosintelligence.com/avoslocker-new-arsenal/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Lior Rochberger, Tom Fakterman, Robert Falcone. (2023, September 22). Cyberespionage Attacks Against Southeast Asian Government Linked to Stately Taurus, Aka Mustang Panda. Retrieved September 9, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)
- [Nathaniel Morales, Nick Dai. (2025, February 18). Earth Preta Mixes Legitimate and Malicious Components to Sidestep Detection. Retrieved September 10, 2025.](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
- [MSTIC. (2022, October 14). New “Prestige” ransomware impacts organizations in Ukraine and Poland. Retrieved January 19, 2023.](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
- [Group-IB. (2018, September). Silence: Moving Into the Darkside. Retrieved May 5, 2020.](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)
- [Dell SecureWorks Counter Threat Unit Special Operations Team. (2015, May 28). Living off the Land. Retrieved January 26, 2016.](https://web.archive.org/web/20150626073312/http://www.secureworks.com/resources/blog/living-off-the-land/)
- [David Ketler. (2026, March 30). Stryker Cyber-Attack: What we Know so Far About the Remote Wipe Attack. Retrieved April 20, 2026.](https://specopssoft.com/blog/stryker-cyber-attack-what-we-know-remote-wipe/)
- [Justin Moore. (2026, March 16). Iranian Cyber Threat Evolution: From MBR Wipers to Identity Weaponization. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/evolution-of-iran-cyber-threats/)
- [Dell SecureWorks. (2013, March 21). Wiper Malware Analysis Attacking Korean Financial Sector. Retrieved May 13, 2015.](http://www.secureworks.com/cyber-threat-intelligence/threats/wiper-malware-analysis-attacking-korean-financial-sector/)

---

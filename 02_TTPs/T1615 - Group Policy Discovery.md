# Group Policy Discovery

## Description

Adversaries may gather information on Group Policy settings to identify paths for privilege escalation, security measures applied within a domain, and to discover patterns in domain objects that can be manipulated or used to blend in the environment. Group Policy allows for centralized management of user and computer settings in Active Directory (AD). Group policy objects (GPOs) are containers for group policy settings made up of files stored within a predictable network path \<DOMAIN>\SYSVOL\<DOMAIN>\Policies\ . [1] [2]

Adversaries may use commands such as gpresult or various publicly available PowerShell functions, such as Get-DomainGPO and Get-DomainGPOLocalGroup , to gather information on Group Policy settings. [3] [4] Adversaries may use this information to shape follow-on behaviors, including determining potential attack paths within the target network as well as opportunities to manipulate Group Policy settings (i.e. Domain or Tenant Policy Modification ) for their benefit.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0521 | BloodHound | BloodHound has the ability to collect local admin information via GPO. [5] |
| S1159 | DUSTTRAP | DUSTTRAP can identify victim environment Group Policy information. [6] |
| S0082 | Emissary | Emissary has the capability to execute gpresult . [7] |
| S0363 | Empire | Empire includes various modules for enumerating Group Policy. [4] |
| C0049 | Leviathan Australian Intrusions | Leviathan performed extensive Active Directory enumeration of victim environments during Leviathan Australian Intrusions . [8] |
| S1141 | LunarWeb | LunarWeb can capture information on group policy settings [9] |
| G0010 | Turla | Turla surveys a system upon check-in to discover Group Policy details using the gpresult command. [10] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0055 | Detection strategy for Group Policy Discovery on Windows | AN0152 | Detection of adversary attempts to enumerate Group Policy settings through suspicious command execution (gpresult), PowerShell enumeration (Get-DomainGPO, Get-DomainGPOLocalGroup), and abnormal LDAP queries targeting groupPolicyContainer objects. Defenders observe unusual process lineage, script execution, or LDAP filter activity against domain controllers. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0055 | Detection strategy for Group Policy Discovery on Windows | AN0152 | Detection of adversary attempts to enumerate Group Policy settings through suspicious command execution (gpresult), PowerShell enumeration (Get-DomainGPO, Get-DomainGPOLocalGroup), and abnormal LDAP queries targeting groupPolicyContainer objects. Defenders observe unusual process lineage, script execution, or LDAP filter activity against domain controllers. |

---

## References

- [srachui. (2012, February 13). Group Policy Basics – Part 1: Understanding the Structure of a Group Policy Object. Retrieved March 5, 2019.](https://blogs.technet.microsoft.com/musings_of_a_technical_tam/2012/02/13/group-policy-basics-part-1-understanding-the-structure-of-a-group-policy-object/)
- [Metcalf, S. (2016, March 14). Sneaky Active Directory Persistence #17: Group Policy. Retrieved March 5, 2019.](https://adsecurity.org/?p=2716)
- [Microsoft. (2017, October 16). gpresult. Retrieved August 6, 2021.](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Robbins, A., Vazarkar, R., and Schroeder, W. (2016, April 17). Bloodhound: Six Degrees of Domain Admin. Retrieved March 5, 2019.](https://github.com/BloodHoundAD/BloodHound)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Falcone, R. and Miller-Osborn, J. (2016, February 3). Emissary Trojan Changelog: Did Operation Lotus Blossom Cause It to Evolve?. Retrieved February 15, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)
- [CISA et al. (2024, July 8). People’s Republic of China (PRC) Ministry of State Security APT40 Tradecraft in Action. Retrieved February 3, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)

---

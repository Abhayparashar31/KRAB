# Unsecured Credentials

## Description

Adversaries may search compromised systems to find and obtain insecurely stored credentials. These credentials can be stored and/or misplaced in many locations on a system, including plaintext files (e.g. Shell History ), operating system or application-specific repositories (e.g. Credentials in Registry ), or other specialized files/artifacts (e.g. Private Keys ). [1]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0373 | Astaroth | Astaroth uses an external software known as NetPass to recover passwords. [2] |
| S1111 | DarkGate | DarkGate uses NirSoft tools to steal user credentials from the infected machine. [3] NirSoft tools are executed via process hollowing in a newly-created instance of vbc.exe or regasm.exe. |
| C0049 | Leviathan Australian Intrusions | Leviathan gathered credentials hardcoded in binaries located on victim devices during Leviathan Australian Intrusions . [4] |
| S1131 | NPPSPY | NPPSPY captures credentials by recording them through an alternative network listener registered to the mpnotify.exe process, allowing for cleartext recording of logon information. [5] |
| S1091 | Pacu | Pacu can search for sensitive data: for example, in Code Build environment variables, EC2 user data, and Cloud Formation templates. [6] |
| G1017 | Volt Typhoon | Volt Typhoon has obtained credentials insecurely stored on targeted network appliances. [7] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1015 | Active Directory Configuration | Remove vulnerable Group Policy Preferences. [8] |
| M1047 | Audit | Preemptively search for files containing passwords or other credentials and take actions to reduce the exposure risk when found. |
| M1041 | Encrypt Sensitive Information | When possible, store keys on separate cryptographic hardware instead of on the local system. |
| M1037 | Filter Network Traffic | Limit access to the Instance Metadata API. A properly configured Web Application Firewall (WAF) may help prevent external adversaries from exploiting Server-side Request Forgery (SSRF) attacks that allow access to the Cloud Instance Metadata API. [9] |
| M1035 | Limit Access to Resource Over Network | Limit network access to sensitive services, such as the Instance Metadata API. |
| M1028 | Operating System Configuration | There are multiple methods of preventing a user's command history from being flushed to their .bash_history file, including use of the following commands: set +o history and set -o history to start logging again; unset HISTFILE being added to a user's .bash_rc file; and ln -s /dev/null ~/.bash_history to write commands to /dev/null instead. |
| M1027 | Password Policies | Use strong passphrases for private keys to make cracking difficult. Do not store credentials within the Registry. Establish an organizational policy that prohibits password storage in files. |
| M1026 | Privileged Account Management | If it is necessary that software must store credentials in the Registry, then ensure the associated accounts have limited permissions so they cannot be abused if obtained by an adversary. |
| M1022 | Restrict File and Directory Permissions | Restrict file shares to specific directories with access only to necessary users. |
| M1051 | Update Software | Apply patch KB2962486 which prevents credentials from being stored in GPPs. [10] [11] |
| M1017 | User Training | Ensure that developers and system administrators are aware of the risk associated with having plaintext passwords in software configuration files that may be left on endpoint systems or servers. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0412 | Detect Access or Search for Unsecured Credentials Across Platforms | AN1153 | Unusual access to bash history, registry credentials paths, or private key files by unauthorized or scripting tools, with correlated file and process activity. |
| AN1154 | Reading of sensitive files like .bash_history, /etc/shadow, or private key directories by unauthorized users or unusual processes. |  |  |
| AN1155 | Unusual access to ~/Library/Keychains, ~/.bash_history, or Terminal command history by unauthorized processes or users. |  |  |
| AN1156 | Unusual web-based access or API scraping of password managers, single sign-on sessions, or credential sync services via browser automation or anomalous API tokens. |  |  |
| AN1157 | Unauthorized API or console calls to retrieve or reset password credentials, download key material, or modify SSO settings. |  |  |
| AN1158 | Access to container image layers or mounted secrets (e.g., Docker secrets) by processes not tied to entrypoint or orchestration context. |  |  |
| AN1159 | Use of configuration backup utilities or CLI access to dump plaintext passwords, local user hashes, or SNMP strings. |  |  |

---

## References

- [Tim Wadhwa-Brown. (2018, November). Where 2 worlds collide Bringing Mimikatz et al to UNIX. Retrieved October 13, 2021.](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)
- [Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [CISA et al. (2024, July 8). People’s Republic of China (PRC) Ministry of State Security APT40 Tradecraft in Action. Retrieved February 3, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a)
- [Dray Agha. (2022, August 16). Cleartext Shenanigans: Gifting User Passwords to Adversaries With NPPSPY. Retrieved May 17, 2024.](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
- [Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.](https://github.com/RhinoSecurityLabs/pacu)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Microsoft. (2014, May 13). MS14-025: Vulnerability in Group Policy Preferences could allow elevation of privilege. Retrieved January 28, 2015.](http://support.microsoft.com/kb/2962486)
- [Higashi, Michael. (2018, May 15). Instance Metadata API: A Modern Day Trojan Horse. Retrieved July 16, 2019.](https://redlock.io/blog/instance-metadata-api-a-modern-day-trojan-horse)
- [Sean Metcalf. (2015, December 28). Finding Passwords in SYSVOL & Exploiting Group Policy Preferences. Retrieved February 17, 2020.](https://adsecurity.org/?p=2288)
- [Microsoft. (2014, May 13). MS14-025: Vulnerability in Group Policy Preferences could allow elevation of privilege. Retrieved February 17, 2020.](https://support.microsoft.com/en-us/help/2962486/ms14-025-vulnerability-in-group-policy-preferences-could-allow-elevati)

---

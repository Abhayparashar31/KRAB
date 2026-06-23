# Email Collection

## Description

Adversaries may target user email to collect sensitive information. Emails may contain sensitive data, including trade secrets or personal information, that can prove valuable to adversaries. Emails may also contain details of ongoing incident response operations, which may allow adversaries to adjust their techniques in order to maintain persistence or evade defenses. [1] [2] Adversaries can collect or forward email from mail servers or clients.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1003 | Ember Bear | Ember Bear attempts to collect mail from accessed systems and servers. [3] [4] |
| S0367 | Emotet | Emotet has been observed leveraging a module that can scrape email addresses from Outlook. [5] [6] [7] |
| G0059 | Magic Hound | Magic Hound has compromised email credentials in order to steal sensitive data. [8] |
| G1015 | Scattered Spider | Scattered Spider searched the victim’s Microsoft Exchange for emails about the intrusion and incident response. [9] |
| G0122 | Silent Librarian | Silent Librarian has exfiltrated entire mailboxes from compromised accounts. [10] |
| S1201 | TRANSLATEXT | TRANSLATEXT has exfiltrated collected email addresses to the C2 server. [11] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Enterprise email solutions have monitoring mechanisms that may include the ability to audit auto-forwarding rules on a regular basis. In an Exchange environment, Administrators can use Get-InboxRule to discover and remove potentially malicious auto-forwarding rules. [12] |
| M1041 | Encrypt Sensitive Information | Use of encryption provides an added layer of security to sensitive information sent over email. Encryption using public key cryptography requires the adversary to obtain the private certificate along with an encryption key to decrypt messages. |
| M1032 | Multi-factor Authentication | Use of multi-factor authentication for public-facing webmail servers is a recommended best practice to minimize the usefulness of usernames and passwords to adversaries. |
| M1060 | Out-of-Band Communications Channel | Use secure out-of-band authentication methods to verify the authenticity of critical actions initiated via email, such as password resets, financial transactions, or access requests. For highly sensitive information, utilize out-of-band communication channels instead of relying solely on email to prevent adversaries from collecting data through compromised email accounts. [1] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0476 | Email Collection via Local Email Access and Auto-Forwarding Behavior | AN1309 | Correlates creation of email forwarding rules or header anomalies (e.g., X-MS-Exchange-Organization-AutoForwarded) with suspicious process execution, file access of .pst/.ost files, and network connections to external SMTP servers. |
| AN1310 | Detects file access to mbox/maildir files in conjunction with curl/wget/postfix execution, or anomalous shell scripts harvesting user mail directories. |  |  |
| AN1311 | Monitors Mail.app database or maildir file access, automation via AppleScript, and abnormal mail rule creation using scripting or UI automation frameworks. |  |  |
| AN1312 | Correlates unusual auto-forwarding rule creation via Exchange Web Services or Outlook rules engine, presence of X-MS-Exchange-Organization-AutoForwarded headers, and logon session anomalies from abnormal IPs. |  |  |

---

## References

- [Tyler Hudak. (2022, December 29). To OOB, or Not to OOB?: Why Out-of-Band Communications are Essential for Incident Response. Retrieved August 30, 2024.](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)
- [CISA. (2021, April 15). Advanced Persistent Threat Compromise of Government Agencies, Critical Infrastructure, and Private Sector Organizations. Retrieved August 30, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a)
- [Microsoft Threat Intelligence. (2023, June 14). Cadet Blizzard emerges as a novel and distinct Russian threat actor. Retrieved July 10, 2023.](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)
- [US Cybersecurity & Infrastructure Security Agency et al. (2024, September 5). Russian Military Cyber Actors Target U.S. and Global Critical Infrastructure. Retrieved September 6, 2024.](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)
- [CIS. (2018, December 12). MS-ISAC Security Primer- Emotet. Retrieved March 25, 2019.](https://www.cisecurity.org/white-papers/ms-isac-security-primer-emotet/)
- [Kessem, L., et al. (2017, November 13). New Banking Trojan IcedID Discovered by IBM X-Force Research. Retrieved July 14, 2020.](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)
- [Binary Defense. (n.d.). Emotet Evolves With new Wi-Fi Spreader. Retrieved September 8, 2023.](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
- [Certfa Labs. (2021, January 8). Charming Kitten’s Christmas Gift. Retrieved May 3, 2021.](https://blog.certfa.com/posts/charming-kitten-christmas-gift/)
- [CISA. (2023, November 16). Cybersecurity Advisory: Scattered Spider (AA23-320A). Retrieved March 18, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)
- [DOJ. (2018, March 23). U.S. v. Rafatnejad et al . Retrieved February 3, 2021.](https://www.justice.gov/usao-sdny/press-release/file/1045781/download)
- [Park, S. (2024, June 27). Kimsuky deploys TRANSLATEXT to target South Korean academia. Retrieved October 14, 2024.](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
- [McMichael, T.. (2015, June 8). Exchange and Office 365 Mail Forwarding. Retrieved October 8, 2019.](https://blogs.technet.microsoft.com/timmcmic/2015/06/08/exchange-and-office-365-mail-forwarding-2/)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[ShinyHunters]] [related_actor:: [[ShinyHunters]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025-2026 SaaS and Cloud Exploitation Wave]] [related_campaign:: [[2025-2026 SaaS and Cloud Exploitation Wave]]]

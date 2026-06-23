# Email Bombing

## Description

Adversaries may flood targeted email addresses with an overwhelming volume of messages. This may bury legitimate emails in a flood of spam and disrupt business operations. [1] [2]

An adversary may accomplish email bombing by leveraging an automated bot to register a targeted address for e-mail lists that do not validate new signups, such as online newsletters. The result can be a wave of thousands of e-mails that effectively overloads the victim’s inbox. [2] [3]

By sending hundreds or thousands of e-mails in quick succession, adversaries may successfully divert attention away from and bury legitimate messages including security alerts, daily business processes like help desk tickets and client correspondence, or ongoing scams. [3] This behavior can also be used as a tool of harassment. [2]

This behavior may be a precursor for Spearphishing Voice . For example, an adversary may email bomb a target and then follow up with a phone call to fraudulently offer assistance. This social engineering may lead to the use of Remote Access Software to steal credentials, deploy ransomware, conduct Financial Theft [1] , or engage in other malicious activity. [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1046 | Storm-1811 | Storm-1811 has deployed large volumes of non-malicious email spam to victims in order to prompt follow-on interactions with the threat actor posing as IT support or helpdesk to resolve the problem. [4] [5] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1054 | Software Configuration | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation. [6] [7] Note that additional filtering may be necessary if emails are coming from legitimate sources. |
| M1017 | User Training | Train users to be aware of access or manipulation attempts by an adversary to reduce the risk of successful social engineering via e-mail bombing. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0355 | Detection Strategy for Email Bombing | AN1008 | Detect abnormally high volume of inbound email messages or repetitive attachments being delivered to a single mailbox within a short time window. Defenders should look for anomalous spikes in message counts and repetitive attachment file creation events correlated with targeted users. |
| AN1009 | Monitor mail server logs (e.g., Postfix, Sendmail) for excessive connections or inbound message counts targeting a single recipient. Correlate with repetitive attachment storage in /var/mail or /var/spool/mail directories. |  |  |
| AN1010 | Detect abnormal use of email clients (e.g., Outlook, Thunderbird) showing mass arrival of messages or repetitive attachments being locally stored. Correlate message volume with file creation activity in mail cache directories. |  |  |
| AN1011 | Monitor unified logs and Mail.app activity for repetitive incoming messages with attachments. Defenders should look for large volumes of incoming mail stored under ~/Library/Mail with unusual timing or repetitive subjects. |  |  |

---

## References

- [Mark Parsons, Colin Cowie, Daniel Souter, Hunter Neal, Anthony Bradshaw, Sean Gallagher. (2025, January 21). Sophos MDR tracks two ransomware campaigns using “email bombing,” Microsoft Teams “vishing”. Retrieved January 31, 2025.](https://news.sophos.com/en-us/2025/01/21/sophos-mdr-tracks-two-ransomware-campaigns-using-email-bombing-microsoft-teams-vishing/)
- [Brian Krebs. (2016, August 18). Massive Email Bombs Target .Gov Addresses. Retrieved January 31, 2025.](https://krebsonsecurity.com/2016/08/massive-email-bombs-target-gov-addresses/)
- [U.S. Department of Health and Human Services. (2024, March 12). Defense and Mitigations from E-mail Bombing. Retrieved January 31, 2025.](https://www.hhs.gov/sites/default/files/email-bombing-sector-alert-tlpclear.pdf)
- [Tyler McGraw, Thomas Elkins, and Evan McCann. (2024, May 10). Ongoing Social Engineering Campaign Linked to Black Basta Ransomware Operators. Retrieved January 31, 2025.](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)
- [Red Canary Intelligence. (2024, December 2). Storm-1811 exploits RMM tools to drop Black Basta ransomware. Retrieved March 14, 2025.](https://redcanary.com/blog/threat-intelligence/storm-1811-black-basta/)
- [Microsoft. (2020, October 13). Anti-spoofing protection in EOP. Retrieved October 19, 2020.](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)
- [Australian Cyber Security Centre. (2012, December). Mitigating Spoofed Emails Using Sender Policy Framework. Retrieved November 17, 2024.](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)

---

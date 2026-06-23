# Internal Spearphishing

## Description

After they already have access to accounts or systems within the environment, adversaries may use internal spearphishing to gain access to additional information or compromise other users within the same organization. Internal spearphishing is multi-staged campaign where a legitimate account is initially compromised either by controlling the user's device or by compromising the account credentials of the user. Adversaries may then attempt to take advantage of the trusted internal account to increase the likelihood of tricking more victims into falling for phish attempts, often incorporating Impersonation . [1]

For example, adversaries may leverage Spearphishing Attachment or Spearphishing Link as part of internal spearphishing to deliver a payload or redirect to an external site to capture credentials through Input Capture on sites that mimic login interfaces.

Adversaries may also leverage internal chat apps, such as Microsoft Teams, to spread malicious content or engage users in attempts to capture sensitive information and/or credentials. [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0099 | APT-C-36 | APT-C-36 has used a compromised account to send a phishing email to an address likely used and monitored by the IT team within the same targeted organization. [3] |
| G0047 | Gamaredon Group | Gamaredon Group has used an Outlook VBA module on infected systems to send phishing emails with malicious attachments to other employees within the organization. [4] |
| G1001 | HEXANE | HEXANE has conducted internal spearphishing attacks against executives, HR, and IT personnel to gain information and access. [5] |
| G0094 | Kimsuky | Kimsuky has sent internal spearphishing emails for lateral movement after stealing victim information. [6] |
| G0065 | Leviathan | Leviathan has conducted internal spearphishing within the victim's environment for lateral movement. [7] |
| G0069 | MuddyWater | MuddyWater has used compromised mailboxes within target organizations to send spearphishing emails. [8] |
| C0022 | Operation Dream Job | During Operation Dream Job , Lazarus Group conducted internal spearphishing from within a compromised organization. [9] |
| S9030 | SameCoin | SameCoin can send its Setup.exe file as an attachment to other addresses in the same compromised organization. [10] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0054 | Internal Spearphishing via Trusted Accounts | AN0147 | Sequence of internal email sent from a recently compromised user account (preceded by abnormal logon or device activity), with attachments or links leading to execution or credential harvesting. Defender observes: internal mail delivery to peers with high entropy attachments, followed by click events, process initiation, or credential prompts. |
| AN0148 | Delivery of suspicious internal communication (e.g., Thunderbird, Evolution) using compromised internal accounts. Sequence of: unexpected user activity + mail transfer logs + download or execution of attachments. |  |  |
| AN0149 | Abnormal Apple Mail use, including internal email relays followed by file execution or script events (e.g., attachments launched via Preview, terminal triggered from Mail.app) |  |  |
| AN0150 | Internal spearphishing via SaaS applications (e.g., Slack, Teams, Gmail): message sent from compromised user with attachment or URL, followed by click and credential access behavior. |  |  |
| AN0151 | Outlook or Word used to forward suspicious internal attachments with macro content. Defender observes attachment forwarding, auto-opening behaviors, or macro prompt interactions. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0054 | Internal Spearphishing via Trusted Accounts | AN0147 | Sequence of internal email sent from a recently compromised user account (preceded by abnormal logon or device activity), with attachments or links leading to execution or credential harvesting. Defender observes: internal mail delivery to peers with high entropy attachments, followed by click events, process initiation, or credential prompts. |
| AN0148 | Delivery of suspicious internal communication (e.g., Thunderbird, Evolution) using compromised internal accounts. Sequence of: unexpected user activity + mail transfer logs + download or execution of attachments. |  |  |
| AN0149 | Abnormal Apple Mail use, including internal email relays followed by file execution or script events (e.g., attachments launched via Preview, terminal triggered from Mail.app) |  |  |
| AN0150 | Internal spearphishing via SaaS applications (e.g., Slack, Teams, Gmail): message sent from compromised user with attachment or URL, followed by click and credential access behavior. |  |  |
| AN0151 | Outlook or Word used to forward suspicious internal attachments with macro content. Defender observes attachment forwarding, auto-opening behaviors, or macro prompt interactions. |  |  |

---

## References

- [Trend Micro. (n.d.). Retrieved February 16, 2024.](https://www.trendmicro.com/en_us/research.html)
- [Microsoft Threat Intelligence. (2023, August 2). Midnight Blizzard conducts targeted social engineering over Microsoft Teams. Retrieved February 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/08/02/midnight-blizzard-conducts-targeted-social-engineering-over-microsoft-teams/)
- [Pellegrino, G. (2025, December 16). BlindEagle Targets Colombian Government Agency with Caminho and DCRAT. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [SecureWorks 2019, August 27 LYCEUM Takes Center Stage in Middle East Campaign Retrieved. 2019/11/19](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)
- [KISA. (2021). Phishing Target Reconnaissance and Attack Resource Analysis Operation Muzabi. Retrieved March 8, 2024.](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
- [CISA. (2021, July 19). (AA21-200A) Joint Cybersecurity Advisory – Tactics, Techniques, and Procedures of Indicted APT40 Actors Associated with China’s MSS Hainan State Security Department. Retrieved August 12, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)
- [FalconFeeds.io. (2026, March 5). The Digital Redoubt: Iran’s National Information Network and the Asymmetry of Modern Cyber Conflict. Retrieved March 9, 2026.](https://falconfeeds.io/blogs/the-digital-redoubt-irans-national-information-network-cyber-conflict)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [Check Point. (2024, November 12). Hamas-affiliated Threat Actor WIRTE Continues its Middle East Operations and Moves to Disruptive Activity. Retrieved April 20, 2026.](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)

---

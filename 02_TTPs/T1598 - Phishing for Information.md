# Phishing for Information

## Description

Adversaries may send phishing messages to elicit sensitive information that can be used during targeting. Phishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Phishing for information is different from Phishing in that the objective is gathering data from the victim rather than executing malicious code.

All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass credential harvesting campaigns.

Adversaries may also try to obtain information directly through the exchange of emails, instant messages, or other electronic conversation means. [1] [2] [3] [4] [5] Victims may also receive phishing messages that direct them to call a phone number where the adversary attempts to collect confidential information. [6]

Phishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: Establish Accounts or Compromise Accounts ) and/or sending multiple, seemingly urgent messages. Another way to accomplish this is by Email Spoofing [7] the identity of the sender, which can be used to fool both the human recipient as well as automated security tools. [8]

Phishing for information may also involve evasive techniques, such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages (e.g., Email Hiding Rules ). [9] [10]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0007 | APT28 | APT28 has used spearphishing to compromise credentials. [11] [12] |
| G0094 | Kimsuky | Kimsuky has used tailored spearphishing emails to gather victim information including contat lists to identify additional targets. [13] |
| G1036 | Moonstone Sleet | Moonstone Sleet has interacted with victims to gather information via email. [14] |
| G1015 | Scattered Spider | Scattered Spider has used a combination of credential phishing and social engineering to capture one-time-password (OTP) codes. [15] |
| G0128 | ZIRCONIUM | ZIRCONIUM targeted presidential campaign staffers with credential phishing e-mails. [16] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1054 | Software Configuration | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation. [17] [18] |
| M1017 | User Training | Users can be trained to identify social engineering techniques and spearphishing attempts. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0823 | Detection of Phishing for Information | AN1955 | Monitor and analyze traffic patterns and packet inspection associated to protocol(s) that do not follow the expected protocol standards and traffic flows (e.g extraneous packets that do not belong to established flows, gratuitous or anomalous traffic patterns, anomalous syntax, or structure). Consider correlation with process monitoring and command line to detect anomalous processes execution and command line arguments associated to traffic patterns (e.g. monitor anomalies in use of files that do not normally initiate connections for respective protocol(s)). Depending on the specific method of phishing, the detections can vary. Monitor for suspicious email activity, such as numerous accounts receiving messages from a single unusual/unknown sender. Filtering based on DKIM+SPF or header analysis can help detect when the email sender is spoofed. [17] [18] When it comes to following links, monitor for references to uncategorized or known-bad sites. URL inspection within email (including expanding shortened links) can also help detect links leading to known malicious sites. Monitor social media traffic for suspicious activity, including messages requesting information as well as abnormal file or data transfers (especially those involving unknown, or otherwise suspicious accounts). Monitor call logs from corporate devices to identify patterns of potential voice phishing, such as calls to/from known malicious phone numbers. Monitor network data for uncommon data flows. Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. |

---

## References

- [O'Donnell, L. (2020, October 20). Facebook: A Top Launching Pad For Phishing Attacks. Retrieved October 20, 2020.](https://threatpost.com/facebook-launching-pad-phishing-attacks/160351/)
- [Babon, P. (2020, September 3). Tricky 'Forms' of Phishing. Retrieved October 20, 2020.](https://www.trendmicro.com/en_us/research/20/i/tricky-forms-of-phishing.html)
- [Kan, M. (2019, October 24). Hackers Try to Phish United Nations Staffers With Fake Login Pages. Retrieved October 20, 2020.](https://www.pcmag.com/news/hackers-try-to-phish-united-nations-staffers-with-fake-login-pages)
- [Ducklin, P. (2020, October 2). Serious Security: Phishing without links – when phishers bring along their own web pages. Retrieved October 20, 2020.](https://nakedsecurity.sophos.com/2020/10/02/serious-security-phishing-without-links-when-phishers-bring-along-their-own-web-pages/)
- [Ryan Hanson. (2016, September 24). phishery. Retrieved October 23, 2020.](https://github.com/ryhanson/phishery)
- [Avertium. (n.d.). EVERYTHING YOU NEED TO KNOW ABOUT CALLBACK PHISHING. Retrieved February 2, 2023.](https://www.avertium.com/resources/threat-reports/everything-you-need-to-know-about-callback-phishing)
- [Proofpoint. (n.d.). What Is Email Spoofing?. Retrieved February 24, 2023.](https://www.proofpoint.com/us/threat-reference/email-spoofing)
- [Itkin, Liora. (2022, September 1). Double-bounced attacks with email spoofing . Retrieved February 24, 2023.](https://blog.cyberproof.com/blog/double-bounced-attacks-with-email-spoofing-2022-trends)
- [Microsoft. (2023, September 22). Malicious OAuth applications abuse cloud email services to spread spam. Retrieved March 13, 2023.](https://www.microsoft.com/en-us/security/blog/2022/09/22/malicious-oauth-applications-used-to-compromise-email-servers-and-spread-spam/)
- [Vicky Ray and Rob Downs. (2014, October 29). Examining a VBA-Initiated Infostealer Campaign. Retrieved March 13, 2023.](https://unit42.paloaltonetworks.com/examining-vba-initiated-infostealer-campaign/)
- [Burt, T. (2020, September 10). New cyberattacks targeting U.S. elections. Retrieved March 24, 2021.](https://blogs.microsoft.com/on-the-issues/2020/09/10/cyberattacks-us-elections-trump-biden/)
- [Secureworks CTU. (2017, March 30). IRON TWILIGHT Supports Active Measures. Retrieved February 28, 2022.](https://www.secureworks.com/research/iron-twilight-supports-active-measures)
- [Mandiant. (2024, March 14). APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations. Retrieved May 3, 2024.](https://services.google.com/fh/files/misc/apt43-report-en.pdf)
- [Microsoft Threat Intelligence. (2024, May 28). Moonstone Sleet emerges as new North Korean threat actor with new bag of tricks. Retrieved August 26, 2024.](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)
- [CrowdStrike. (2023, January 10). SCATTERED SPIDER Exploits Windows Security Deficiencies with Bring-Your-Own-Vulnerable-Driver Tactic in Attempt to Bypass Endpoint Security. Retrieved July 5, 2023.](https://www.crowdstrike.com/blog/scattered-spider-attempts-to-avoid-detection-with-bring-your-own-vulnerable-driver-tactic/)
- [Huntley, S. (2020, October 16). How We're Tackling Evolving Online Threats. Retrieved March 24, 2021.](https://blog.google/threat-analysis-group/how-were-tackling-evolving-online-threats/)
- [Microsoft. (2020, October 13). Anti-spoofing protection in EOP. Retrieved October 19, 2020.](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)
- [Australian Cyber Security Centre. (2012, December). Mitigating Spoofed Emails Using Sender Policy Framework. Retrieved November 17, 2024.](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)

---

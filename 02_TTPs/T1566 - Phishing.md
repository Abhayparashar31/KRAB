# Phishing

## Description

Adversaries may send phishing messages to gain access to victim systems. All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass malware spam campaigns.

Adversaries may send victims emails containing malicious attachments or links, typically to execute malicious code on victim systems. Phishing may also be conducted via third-party services, like social media platforms. Phishing may also involve social engineering techniques, such as posing as a trusted source, as well as evasive techniques such as removing or manipulating emails or metadata/headers from compromised accounts being abused to send messages (e.g., Email Hiding Rules ). [1] [2] Another way to accomplish this is by Email Spoofing [3] the identity of the sender, which can be used to fool both the human recipient as well as automated security tools, [4] or by including the intended target as a party to an existing email thread that includes malicious files or links (i.e., "thread hijacking"). [5]

Victims may also receive phishing messages that instruct them to call a phone number where they are directed to visit a malicious URL, download malware, [6] [7] or install adversary-accessible remote management tools onto their computer (i.e., User Execution ). [8]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1049 | AppleJeus | AppleJeus has used spearphishing emails to distribute malicious payloads. [9] |
| G0001 | Axiom | Axiom has used spear phishing to initially compromise victims. [10] [11] |
| G0115 | GOLD SOUTHFIELD | GOLD SOUTHFIELD has conducted malicious spam (malspam) campaigns to gain access to victim's machines. [12] |
| S0009 | Hikit | Hikit has been spread through spear phishing. [11] |
| G1032 | INC Ransom | INC Ransom has used phishing to gain initial access. [13] [14] |
| S1139 | INC Ransomware | INC Ransomware campaigns have used spearphishing emails for initial access. [14] |
| G0094 | Kimsuky | Kimsuky has used spearphishing to gain initial access and intelligence. [15] [16] |
| G0069 | MuddyWater | MuddyWater has sent phishing emails to targets from the email address support@microsoftonlines[.]com. [17] |
| S1073 | Royal | Royal has been spread through the use of phishing campaigns including "call back phishing" where victims are lured into calling a number provided through email. [18] [19] [20] |
| G1041 | Sea Turtle | Sea Turtle used spear phishing to gain initial access to victims. [21] |
| G1055 | VOID MANTICORE | VOID MANTICORE has emailed victims threatening messages. [22] VOID MANTICORE has used phishing as an initial access vector. [23] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1049 | Antivirus/Antimalware | Anti-virus can automatically quarantine suspicious files. |
| M1047 | Audit | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |
| M1031 | Network Intrusion Prevention | Network intrusion prevention systems and systems designed to scan and remove malicious email attachments or links can be used to block activity. |
| M1021 | Restrict Web-Based Content | Determine if certain websites or attachment types (ex: .scr, .exe, .pif, .cpl, etc.) that can be used for phishing are necessary for business operations and consider blocking access if activity cannot be monitored well or if it poses a significant risk. |
| M1054 | Software Configuration | Use anti-spoofing and email authentication mechanisms to filter messages based on validity checks of the sender domain (using SPF) and integrity of messages (using DKIM). Enabling these mechanisms within an organization (through policies such as DMARC) may enable recipients (intra-org and cross domain) to perform similar message filtering and validation. [24] [25] |
| M1017 | User Training | Users can be trained to identify social engineering techniques and phishing emails. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0070 | Detection Strategy for Phishing across platforms. | AN0188 | Unusual inbound email activity where attachments or embedded URLs are delivered to users followed by execution of new processes or suspicious document behavior. Detection involves correlating email metadata, file creation, and network activity after a phishing message is received. |
| AN0189 | Monitor for malicious payload delivery through phishing where attachments or URLs in email clients (e.g., Thunderbird, mutt) result in unusual file creation or outbound network connections. Focus on correlation between mail logs, file writes, and execution activity. |  |  |
| AN0190 | Detection of phishing through anomalous Mail app activity, such as attachments saved to disk and immediately executed, or Safari/Preview launching URLs and files linked from email messages. Correlate UnifiedLogs events with subsequent process execution. |  |  |
| AN0191 | Phishing via Office documents containing embedded macros or links that spawn processes. Detection relies on correlating Office application logs with suspicious child process execution and outbound network connections. |  |  |
| AN0192 | Phishing attempts targeting IdPs often manifest as anomalous login attempts from suspicious email invitations or fake SSO prompts. Detection correlates login flows, MFA bypass attempts, and anomalous geographic patterns following phishing email delivery. |  |  |
| AN0193 | Phishing delivered via SaaS services (chat, collaboration platforms) where messages contain malicious URLs or attachments. Detect anomalous link clicks, suspicious file uploads, or token misuse after SaaS-based phishing attempts. |  |  |

---

## References

- [Microsoft. (2023, September 22). Malicious OAuth applications abuse cloud email services to spread spam. Retrieved March 13, 2023.](https://www.microsoft.com/en-us/security/blog/2022/09/22/malicious-oauth-applications-used-to-compromise-email-servers-and-spread-spam/)
- [Vicky Ray and Rob Downs. (2014, October 29). Examining a VBA-Initiated Infostealer Campaign. Retrieved March 13, 2023.](https://unit42.paloaltonetworks.com/examining-vba-initiated-infostealer-campaign/)
- [Proofpoint. (n.d.). What Is Email Spoofing?. Retrieved February 24, 2023.](https://www.proofpoint.com/us/threat-reference/email-spoofing)
- [Itkin, Liora. (2022, September 1). Double-bounced attacks with email spoofing . Retrieved February 24, 2023.](https://blog.cyberproof.com/blog/double-bounced-attacks-with-email-spoofing-2022-trends)
- [Brian Krebs. (2024, March 28). Thread Hijacking: Phishes That Prey on Your Curiosity. Retrieved September 27, 2024.](https://krebsonsecurity.com/2024/03/thread-hijacking-phishes-that-prey-on-your-curiosity/)
- [Oren Biderman, Tomer Lahiyani, Noam Lifshitz, Ori Porag. (n.d.). LUNA MOTH: THE THREAT ACTORS BEHIND RECENT FALSE SUBSCRIPTION SCAMS. Retrieved February 2, 2023.](https://blog.sygnia.co/luna-moth-false-subscription-scams)
- [CISA. (n.d.). Protecting Against Malicious Use of Remote Monitoring and Management Software. Retrieved February 2, 2023.](https://www.cisa.gov/uscert/ncas/alerts/aa23-025a)
- [Kristopher Russo. (n.d.). Luna Moth Callback Phishing Campaign. Retrieved February 2, 2023.](https://unit42.paloaltonetworks.com/luna-moth-callback-phishing/)
- [Michael “Barni” Barnhart, DTEX, and Anonymous SMEs. (2025, May 14). Exposing DPRK's Cyber Syndicate and Hidden IT Workforce. Retrieved September 3, 2025.](https://reports.dtexsystems.com/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf)
- [Esler, J., Lee, M., and Williams, C. (2014, October 14). Threat Spotlight: Group 72. Retrieved January 14, 2016.](http://blogs.cisco.com/security/talos/threat-spotlight-group-72)
- [Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [SOCRadar. (2024, January 24). Dark Web Profile: INC Ransom. Retrieved June 5, 2024.](https://socradar.io/dark-web-profile-inc-ransom/)
- [SentinelOne. (n.d.). What Is Inc. Ransomware?. Retrieved June 5, 2024.](https://www.sentinelone.com/anthology/inc-ransom/)
- [Microsoft Threat Intelligence. (2024, February 14). Staying ahead of threat actors in the age of AI. Retrieved March 11, 2024.](https://www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai/)
- [Mandiant. (2024, March 14). APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations. Retrieved May 3, 2024.](https://services.google.com/fh/files/misc/apt43-report-en.pdf)
- [Naumaan, S., et al. (2025, April 17). Around the World in 90 Days: State-Sponsored Actors Try ClickFix . Retrieved January 21, 2026.](https://www.proofpoint.com/us/blog/threat-insight/around-world-90-days-state-sponsored-actors-try-clickfix)
- [Cybereason Global SOC and Cybereason Security Research Teams. (2022, December 14). Royal Rumble: Analysis of Royal Ransomware. Retrieved March 30, 2023.](https://www.cybereason.com/blog/royal-ransomware-analysis)
- [Iacono, L. and Green, S. (2023, February 13). Royal Ransomware Deep Dive. Retrieved March 30, 2023.](https://www.kroll.com/en/insights/publications/cyber/royal-ransomware-deep-dive)
- [CISA. (2023, March 2). #StopRansomware: Royal Ransomware. Retrieved March 31, 2023.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a)
- [Cisco Talos. (2019, April 17). Sea Turtle: DNS Hijacking Abuses Trust In Core Internet Service. Retrieved November 20, 2024.](https://blog.talosintelligence.com/seaturtle/)
- [DOJ/FBI. (2026, March 19). Case 1:26-mj-00683-CDA: Affidavit in Support of Seizure Warrant: In the Matter of the Seizure of Domain Names Justicehomeland[.]org; karmabelow80[.]org; handala-hack[.]to; and handala-redwatned[.]to. Retrieved April 20, 2026.](https://www.justice.gov/opa/media/1431956/dl?inline)
- [DomainTools Investigations. (2026, April 6). Handala: MOIS Linked Cyber Influence Ecosystem Threat Intelligence Assessment. Retrieved April 20, 2026.](https://dti.domaintools.com/research/handala-mois-linked-cyber-influence-ecosystem-threat-intelligence-assessment)
- [Microsoft. (2020, October 13). Anti-spoofing protection in EOP. Retrieved October 19, 2020.](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spoofing-protection?view=o365-worldwide)
- [Australian Cyber Security Centre. (2012, December). Mitigating Spoofed Emails Using Sender Policy Framework. Retrieved November 17, 2024.](https://web.archive.org/web/20210708014107/https://www.cyber.gov.au/sites/default/files/2019-03/spoof_email_sender_policy_framework.pdf)

---

# Financial Theft

## Description

Adversaries may steal monetary resources from targets through extortion, social engineering, technical theft, or other methods aimed at their own financial gain at the expense of the availability of these resources for victims. Financial theft is the ultimate objective of several popular campaign types including extortion by ransomware, [1] business email compromise (BEC) and fraud, [2] "pig butchering," [3] bank hacking, [4] and exploiting cryptocurrency networks. [5]

Adversaries may Compromise Accounts to conduct unauthorized transfers of funds. [6] In the case of business email compromise or email fraud, an adversary may utilize Impersonation of a trusted entity. Once the social engineering is successful, victims can be deceived into sending money to financial accounts controlled by an adversary. [2] This creates the potential for multiple victims (i.e., compromised accounts as well as the ultimate monetary loss) in incidents involving financial theft. [7]

Extortion by ransomware may occur, for example, when an adversary demands payment from a victim after Data Encrypted for Impact [8] and Exfiltration of data, followed by threatening to leak sensitive data to the public unless payment is made to the adversary. [9] Adversaries may use dedicated leak sites to distribute victim data. [10]

Due to the potentially immense business impact of financial theft, an adversary may abuse the possibility of financial theft and seeking monetary gain to divert attention from their true goals such as Data Destruction and business disruption. [11]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1024 | Akira | Akira engages in double-extortion ransomware, exfiltrating files then encrypting them, in order to prompt victims to pay a ransom. [12] [13] |
| G1049 | AppleJeus | AppleJeus has targeted the cryptocurrency industry with the goal of stealing digital assets. [14] |
| S1246 | BeaverTail | BeaverTail has searched the victim device for browser extensions commonly associated with cryptocurrency wallets. [15] [16] [17] [18] [19] |
| G1021 | Cinnamon Tempest | Cinnamon Tempest has maintained leak sites for exfiltrated data in attempt to extort victims into paying a ransom. [20] |
| G1052 | Contagious Interview | Contagious Interview has stolen cryptocurrency wallet credentials and credit card information utilizing BeaverTail and InvisibleFerret malware. [15] [21] [22] [17] [23] [18] [19] |
| S9004 | Crocodilus | Crocodilus has stolen cryptocurrency wallet details from victim devices. [24] [25] |
| S1111 | DarkGate | DarkGate can deploy payloads capable of capturing credentials related to cryptocurrency wallets. [26] |
| S1247 | Embargo | Embargo has been leveraged in double-extortion ransomware, exfiltrating files then encrypting them, to prompt victims to pay a ransom. [27] [28] |
| G1016 | FIN13 | FIN13 has observed the victim's software and infrastructure over several months to understand the technical process of legitimate financial transactions, prior to attempting to conduct fraudulent transactions. [29] |
| S9010 | GlassWorm | GlassWorm has the ability to steal credentials for cryptocurrency wallets. [30] [31] [32] |
| G1032 | INC Ransom | INC Ransom has stolen and encrypted victim's data in order to extort payment for keeping it private or decrypting it. [33] [34] [35] [36] [37] |
| S1245 | InvisibleFerret | InvisibleFerret has searched the victim device credentials and files commonly associated with cryptocurrency wallets. [15] [17] [23] [18] |
| G0094 | Kimsuky | Kimsuky has stolen and laundered cryptocurrency to self-fund operations including the acquisition of infrastructure. [38] |
| G1026 | Malteiro | Malteiro targets organizations in a wide variety of sectors via the use of Mispadu banking trojan with the goal of financial theft. [39] |
| G1051 | Medusa Group | Medusa Group has stolen and encrypted victims' data in order to extort victims into paying a ransom. [40] [41] [42] [43] [44] [45] |
| G1040 | Play | Play demands ransom payments from victims to unencrypt filesystems and to not publish sensitive data exfiltrated from victim networks. [46] |
| S1240 | RedLine Stealer | RedLine Stealer has collected data from cryptocurrency wallets and harvested credit cards details from browsers. [47] [48] [49] [50] [51] |
| G1015 | Scattered Spider | Scattered Spider has deployed ransomware on compromised hosts and threatened to leak stolen data for financial gain. [52] [53] [54] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors demanded ransom payments to unencrypt filesystems and to refrain from publishing sensitive data exfiltrated from victim networks. [55] |
| G0083 | SilverTerrier | SilverTerrier targets organizations in high technology, higher education, and manufacturing for business email compromise (BEC) campaigns with the goal of financial theft. [56] [57] |
| G1053 | Storm-0501 | Storm-0501 has engaged in double-extortion ransomware, exfiltrating data and directly contacting victims when the primary organization refuses to pay along with posting data on their data leak sites. [58] [59] [60] |
| G1055 | VOID MANTICORE | VOID MANTICORE has conducted data exfiltration and posted stolen information on data leak sites for the purposes of financial and political extortion. [61] [62] VOID MANTICORE has also sold stolen data to prospective buyers for cryptocurrency. [62] |
| G1050 | Water Galura | Water Galura has extorted victims for ransomware decryption keys and to prevent publication of data exfiltrated to their Tor data leak site. [63] [64] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1018 | User Account Management | Limit access/authority to execute sensitive transactions, and switch to systems and procedures designed to authenticate/approve payments and purchase requests outside of insecure communication lines such as email. |
| M1017 | User Training | Train and encourage users to identify social engineering techniques used to enable financial theft. Also consider training users on procedures to prevent and respond to swatting and doxing, acts increasingly deployed by financially motivated groups to further coerce victims into satisfying ransom/extortion demands. [65] [66] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0495 | Detection Strategy for Financial Theft | AN1361 | Monitor for anomalous access to financial applications, browser-based banking sessions, or enterprise ERP systems from Windows endpoints. Detect mass emailing of payment instructions, sudden rule changes in Outlook for financial staff, or use of clipboard data exfiltration tied to cryptocurrency wallet addresses. |
| AN1362 | Monitor server and endpoint logs for unusual outbound network connections to cryptocurrency nodes, unauthorized scripts accessing financial systems, or automation targeting payment file formats. Detect curl/wget activity aimed at exfiltrating transaction data or credentials from financial apps. |  |  |
| AN1363 | Monitor unified logs for access to payment applications, browser plug-ins, or Apple Pay services from non-standard processes. Detect anomalous use of Automator scripts or keychain extraction targeting financial account credentials. |  |  |
| AN1364 | Monitor SaaS financial systems (e.g., QuickBooks, Workday, SAP S/4HANA cloud) for unauthorized access, rule changes, or mass export of financial data. Detect anomalous transfers initiated via SaaS APIs or new MFA-disabled logins targeting finance apps. |  |  |
| AN1365 | Monitor email and document management systems for fraudulent invoices, impersonation of vendors, or BEC-style payment redirections. Detect abnormal editing of invoice templates, or emails containing known fraud language combined with attachment delivery. |  |  |

---

## References

- [FBI. (n.d.). Ransomware. Retrieved August 18, 2023.](https://www.cisa.gov/sites/default/files/Ransomware_Trifold_e-version.pdf)
- [FBI. (2022). FBI 2022 Congressional Report on BEC and Real Estate Wire Fraud. Retrieved August 18, 2023.](https://www.fbi.gov/file-repository/fy-2022-fbi-congressional-report-business-email-compromise-and-real-estate-wire-fraud-111422.pdf/view)
- [Lily Hay Newman. (n.d.). ‘Pig Butchering’ Scams Are Now a $3 Billion Threat. Retrieved August 18, 2023.](https://www.wired.com/story/pig-butchering-fbi-ic3-2022-report/)
- [Department of Justice. (2021). 3 North Korean Military Hackers Indicted in Wide-Ranging Scheme to Commit Cyber-attacks and Financial Crimes Across the Globe. Retrieved August 18, 2023.](https://www.justice.gov/usao-cdca/pr/3-north-korean-military-hackers-indicted-wide-ranging-scheme-commit-cyber-attacks-and)
- [Joe Tidy. (2022, March 30). Ronin Network: What a $600m hack says about the state of crypto. Retrieved August 18, 2023.](https://www.bbc.com/news/technology-60933174)
- [IC3. (2022). 2022 Internet Crime Report. Retrieved August 18, 2023.](https://www.ic3.gov/Media/PDF/AnnualReport/2022_IC3Report.pdf)
- [CloudFlare. (n.d.). What is vendor email compromise (VEC)?. Retrieved September 12, 2023.](https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/#:~:text=Vendor%20email%20compromise%2C%20also%20referred,steal%20from%20that%20vendor%27s%20customers.)
- [Nicole Perlroth. (2021, May 13). Colonial Pipeline paid 75 Bitcoin, or roughly $5 million, to hackers.. Retrieved August 18, 2023.](https://www.nytimes.com/2021/05/13/technology/colonial-pipeline-ransom.html)
- [DANIEL KAPELLMANN ZAFRA, COREY HIDELBRANDT, NATHAN BRUBAKER, KEITH LUNDEN. (2022, January 31). 1 in 7 OT Ransomware Extortion Attacks Leak Critical Operational Technology Information. Retrieved August 18, 2023.](https://www.mandiant.com/resources/blog/ransomware-extortion-ot-docs)
- [Crowdstrike. (2020, September 24). Double Trouble: Ransomware with Data Leak Extortion, Part 1. Retrieved December 6, 2023.](https://www.crowdstrike.com/blog/double-trouble-ransomware-data-leak-extortion-part-1/)
- [FRANK BAJAK AND RAPHAEL SATTER. (2017, June 30). Companies still hobbled from fearsome cyberattack. Retrieved August 18, 2023.](https://apnews.com/article/russia-ukraine-technology-business-europe-hacking-ce7a8aca506742ab8e8873e7f9f229c2)
- [Will Thomas. (2023, September 15). Tracking Adversaries: Akira, another descendent of Conti. Retrieved February 21, 2024.](https://blog.bushidotoken.net/2023/09/tracking-adversaries-akira-another.html)
- [CISA et al. (2024, April 18). #StopRansomware: Akira Ransomware. Retrieved December 10, 2024.](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)
- [Michael Barnhart, Austin Larsen, Jeff Johnson, Taylor Long, Michelle Cantos, Adrian Hernandez. (2023, October 10). Assessed Cyber Structure and Alignments of North Korea in 2023. Retrieved August 25, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-cyber-structure-alignment-2023)
- [eSentire Threat Response Unit (TRU). (2024, November 14). Bored BeaverTail & InvisibleFerret Yacht Club – A Lazarus Lure Pt.2. Retrieved October 17, 2025.](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
- [Insikt Group. (2025, February 13). Inside the Scam: North Korea’s IT Worker Threat. Retrieved October 17, 2025.](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Unit42. (2024, October 9). Contagious Interview: DPRK Threat Actors Lure Tech Industry Job Seekers to Install New Variants of BeaverTail and InvisibleFerret Malware. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
- [Microsoft. (2022, May 9). Ransomware as a service: Understanding the cybercrime gig economy and how to protect yourself. Retrieved March 10, 2023.](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)
- [Kirill Boychenko. (2025, July 14). Contagious Interview Campaign Escalates With 67 Malicious npm Packages and New Malware Loader. Retrieved October 19, 2025.](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Seongsu Park. (2024, November 4). From Pyongyang to Your Payroll: The Rise of North Korean Remote Workers in the West. Retrieved October 17, 2025.](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
- [ThreatFabric. (2025, March 28). Exposing Crocodilus: New Device Takeover Malware Targeting Android Devices. Retrieved November 24, 2025.](https://www.threatfabric.com/blogs/exposing-crocodilus-new-device-takeover-malware-targeting-android-devices)
- [ThreatFabric. (2025, June 3). Crocodilus Mobile Malware: Evolving Fast, Going Global. Retrieved November 24, 2025.](https://www.threatfabric.com/blogs/crocodilus-mobile-malware-evolving-fast-going-global)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Cyble. (2024, May 24). The Rust Revolution: New Embargo Ransomware Steps In. Retrieved October 19, 2025.](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
- [Jan Holman, Tomas Zvara. (2024, October 23). Embargo ransomware: Rock’n’Rust. Retrieved October 19, 2025.](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
- [Sygnia Incident Response Team. (2022, January 5). TG2003: ELEPHANT BEETLE UNCOVERING AN ORGANIZED FINANCIAL-THEFT OPERATION. Retrieved February 9, 2023.](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)
- [Gal Hachamov. (2025, December 29). GlassWorm Goes Mac: Fresh Infrastructure, New Tricks. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
- [Idan Dardikman. (2025, October 18). GlassWorm: First Self-Propagating Worm Using Invisible Code Hits OpenVSX Marketplace. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace)
- [Kirill Boychenko. (2026, January 31). GlassWorm Loader Hits Open VSX via Developer Account Compromise. Retrieved April 10, 2026.](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [Toulas, B. (2024, March 27). INC Ransom threatens to leak 3TB of NHS Scotland stolen data. Retrieved June 5, 2024.](https://www.bleepingcomputer.com/news/security/inc-ransom-threatens-to-leak-3tb-of-nhs-scotland-stolen-data/)
- [Counter Threat Unit Research Team. (2024, April 15). GOLD IONIC DEPLOYS INC RANSOMWARE. Retrieved June 5, 2024.](https://www.secureworks.com/blog/gold-ionic-deploys-inc-ransomware)
- [SOCRadar. (2024, January 24). Dark Web Profile: INC Ransom. Retrieved June 5, 2024.](https://socradar.io/dark-web-profile-inc-ransom/)
- [SentinelOne. (n.d.). What Is Inc. Ransomware?. Retrieved June 5, 2024.](https://www.sentinelone.com/anthology/inc-ransom/)
- [Mandiant. (2024, March 14). APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations. Retrieved May 3, 2024.](https://services.google.com/fh/files/misc/apt43-report-en.pdf)
- [SCILabs. (2021, December 23). Cyber Threat Profile Malteiro. Retrieved March 13, 2024.](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
- [Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
- [Check Point. (2025, April 16). The 2025 Ransomware Surge: Context for Medusa’s Rise. Retrieved October 15, 2025.](https://www.checkpoint.com/cyber-hub/threat-prevention/ransomware/medusa-ransomware-group/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Intel471. (2025, May 14). Threat hunting case study: Medusa ransomware. Retrieved October 15, 2025.](https://www.intel471.com/blog/threat-hunting-case-study-medusa-ransomware)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [CISA. (2023, December 18). #StopRansomware: Play Ransomware AA23-352A. Retrieved September 24, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)
- [Alexandre Cote Cyr. (2024, November 8). Life on a crooked RedLine: Analyzing the infamous infostealer’s backend. Retrieved September 17, 2025.](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)
- [George Glass. (2024, August 14). REDLINESTEALER Malware Driving the Initial Access Broker Market. Retrieved September 17, 2025.](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
- [Proofpoint Threat Insight Team, Jeremy H, Axel F. (2020, March 16). New Redline Password Stealer Malware. Retrieved September 17, 2025.](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
- [Splunk Threat Research Team. (2023, June 1). Do Not Cross The 'RedLine' Stealer: Detections and Analysis. Retrieved September 17, 2025.](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
- [Yair Herling. (2023, April 4). From ChatGPT to RedLine Stealer: The Dark Side of OpenAI and Google Bard. Retrieved September 17, 2025.](https://veriti.ai/blog/veriti-research/from-chatgpt-to-redline-stealer-the-dark-side-of-openai-and-google-bard/)
- [CISA. (2023, November 16). Cybersecurity Advisory: Scattered Spider (AA23-320A). Retrieved March 18, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)
- [Trellix et. al.. (2023, August 17). Scattered Spider: The Modus Operandi. Retrieved March 18, 2024.](https://www.trellix.com/blogs/research/scattered-spider-the-modus-operandi/)
- [Counter Adversary Operations. (2025, July 2). CrowdStrike Services Observes SCATTERED SPIDER Escalate Attacks Across Industries. Retrieved October 13, 2025.](https://www.crowdstrike.com/en-us/blog/crowdstrike-services-observes-scattered-spider-escalate-attacks/)
- [Unit 42. (2025, July 31). Active Exploitation of Microsoft SharePoint Vulnerabilities: Threat Brief (Updated). Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/microsoft-sharepoint-cve-2025-49704-cve-2025-49706-cve-2025-53770/)
- [Unit42. (2016). SILVERTERRIER: THE RISE OF NIGERIAN BUSINESS EMAIL COMPROMISE. Retrieved November 13, 2018.](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/unit42-silverterrier-rise-of-nigerian-business-email-compromise)
- [Renals, P., Conant, S. (2016). SILVERTERRIER: The Next Evolution in Nigerian Cybercrime. Retrieved November 13, 2018.](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/Unit_42/silverterrier-next-evolution-in-nigerian-cybercrime.pdf)
- [Avertium. (2022, January 11). An In-Depth Look at Ransomware Gang, Sabbath. Retrieved October 19, 2025.](https://www.avertium.com/resources/threat-reports/in-depth-look-at-sabbath-ransomware-gang)
- [Microsoft Threat Intelligence. (2025, August 27). Storm-0501’s evolving techniques lead to cloud-based ransomware. Retrieved October 19, 2025.](https://www.microsoft.com/en-us/security/blog/2025/08/27/storm-0501s-evolving-techniques-lead-to-cloud-based-ransomware/)
- [Tyler McLellan, Brandan Schondorfer. (2021, November 29). Kitten.gif: Meet the Sabbath Ransomware Affiliate Program, Again. Retrieved October 19, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/sabbath-ransomware-affiliate/)
- [David Ketler. (2026, March 30). Stryker Cyber-Attack: What we Know so Far About the Remote Wipe Attack. Retrieved April 20, 2026.](https://specopssoft.com/blog/stryker-cyber-attack-what-we-know-remote-wipe/)
- [DOJ/FBI. (2026, March 19). Case 1:26-mj-00683-CDA: Affidavit in Support of Seizure Warrant: In the Matter of the Seizure of Domain Names Justicehomeland[.]org; karmabelow80[.]org; handala-hack[.]to; and handala-redwatned[.]to. Retrieved April 20, 2026.](https://www.justice.gov/opa/media/1431956/dl?inline)
- [Thomas, W. (2024, June 12). Tracking Adversaries: The Qilin RaaS. Retrieved September 26, 2025.](https://blog.bushidotoken.net/2024/06/tracking-adversaries-qilin-raas.html)
- [Health Sector Cybersecurity Coordination Center. (2024, June 18). Qilin, aka Agenda Ransomware. Retrieved September 26, 2025.](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)
- [CISA. (2023, August). Cyber Safety Review Board: Lapsus. Retrieved January 5, 2024.](https://www.cisa.gov/sites/default/files/2023-08/CSRB_Lapsus%24_508c.pdf)
- [Giles, Bruce. (2024, January 4). Hackers threaten to send SWAT teams to Fred Hutch patients' homes. Retrieved January 5, 2024.](https://www.beckershospitalreview.com/cybersecurity/hackers-threaten-to-send-swat-teams-to-fred-hutch-patients-homes.html)

---

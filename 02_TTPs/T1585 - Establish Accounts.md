# Establish Accounts

## Description

Adversaries may create and cultivate accounts with services that can be used during targeting. Adversaries can create accounts that can be used to build a persona to further operations. Persona development consists of the development of public information, presence, history and appropriate affiliations. This development could be applied to social media, website, or other publicly available information that could be referenced and scrutinized for legitimacy over the course of an operation using that persona or identity. [1] [2]

For operations incorporating social engineering, the utilization of an online persona may be important. These personas may be fictitious or impersonate real people. The persona may exist on a single site or across multiple sites (ex: Facebook, LinkedIn, Twitter, Google, GitHub, Docker Hub, etc.). Establishing a persona may require development of additional documentation to make them seem real. This could include filling out profile information, developing social networks, or incorporating photos. [1] [2]

Establishing accounts can also include the creation of accounts with email providers, which may be directly leveraged for Phishing for Information or Phishing . [3] In addition, establishing accounts may allow adversaries to abuse free services, such as registering for trial periods to Acquire Infrastructure for malicious purposes. [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0025 | APT17 | APT17 has created and cultivated profile pages in Microsoft TechNet. To make profile pages appear more legitimate, APT17 has created biographical sections and posted in forum threads. [5] |
| G1052 | Contagious Interview | Contagious Interview has created and maintained personas on code repositories to distribute malicious payloads. [6] [7] [8] [9] [10] [11] |
| G1003 | Ember Bear | Ember Bear has created accounts on dark web forums to obtain various tools and malware. [12] |
| G0117 | Fox Kitten | Fox Kitten has created KeyBase accounts to communicate with ransomware victims. [13] [14] |
| G0094 | Kimsuky | Kimsuky has leveraged stolen PII to create accounts. [15] |
| C0059 | Salesforce Data Exfiltration | During Salesforce Data Exfiltration , threat actors created Salesforce trial accounts to register their malicious applications. [16] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0873 | Detection of Establish Accounts | AN2005 | Monitor and analyze traffic patterns and packet inspection associated to protocol(s) that do not follow the expected protocol standards and traffic flows (e.g extraneous packets that do not belong to established flows, gratuitous or anomalous traffic patterns, anomalous syntax, or structure). Consider correlation with process monitoring and command line to detect anomalous processes execution and command line arguments associated to traffic patterns (e.g. monitor anomalies in use of files that do not normally initiate connections for respective protocol(s)). Consider monitoring social media activity related to your organization. Suspicious activity may include personas claiming to work for your organization or recently created/modified accounts making numerous connection requests to accounts affiliated with your organization. Much of this activity will take place outside the visibility of the target organization, making detection of this behavior difficult. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access (ex: Phishing ). |

---

## References

- [Lennon, M. (2014, May 29). Iranian Hackers Targeted US Officials in Elaborate Social Media Attack Operation. Retrieved March 1, 2017.](https://www.securityweek.com/iranian-hackers-targeted-us-officials-elaborate-social-media-attack-operation)
- [Ryan, T. (2010). “Getting In Bed with Robin Sage.”. Retrieved March 6, 2017.](http://media.blackhat.com/bh-us-10/whitepapers/Ryan/BlackHat-USA-2010-Ryan-Getting-In-Bed-With-Robin-Sage-v1.0.pdf)
- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Gamazo, William. Quist, Nathaniel.. (2023, January 5). PurpleUrchin Bypasses CAPTCHA and Steals Cloud Platform Resources. Retrieved February 28, 2024.](https://unit42.paloaltonetworks.com/purpleurchin-steals-cloud-resources/)
- [FireEye Labs/FireEye Threat Intelligence. (2015, May 14). Hiding in Plain Sight: FireEye and Microsoft Expose Obfuscation Tactic. Retrieved November 17, 2024.](https://web.archive.org/web/20240119213200/https://www2.fireeye.com/rs/fireye/images/APT17_Report.pdf)
- [Aleksandar Milenkoski, Sreekar Madabushi, Kenneth Kinion. (2025, September 4). Contagious Interview | North Korean Threat Actors Reveal Plans and Ops by Abusing Cyber Intel Platforms. Retrieved October 20, 2025.](https://www.sentinelone.com/labs/contagious-interview-threat-actors-scout-cyber-intel-platforms-reveal-plans-and-ops/)
- [Efstratios Lontzetidis. (2025, January 16). Lazarus APT: Techniques for Hunting Contagious Interview. Retrieved October 20, 2025.](https://www.validin.com/blog/inoculating_contagious_interview_with_validin/)
- [Kirill Boychenko. (2025, April 4). Lazarus Expands Malicious npm Campaign: 11 New Packages Add Malware Loaders and Bitbucket Payloads. Retrieved October 20, 2025.](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)
- [Kirill Boychenko. (2025, July 14). Contagious Interview Campaign Escalates With 67 Malicious npm Packages and New Malware Loader. Retrieved October 19, 2025.](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [US Cybersecurity & Infrastructure Security Agency et al. (2024, September 5). Russian Military Cyber Actors Target U.S. and Global Critical Infrastructure. Retrieved September 6, 2024.](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)
- [ClearSky. (2020, December 17). Pay2Key Ransomware – A New Campaign by Fox Kitten. Retrieved December 21, 2020.](https://www.clearskysec.com/wp-content/uploads/2020/12/Pay2Kitten.pdf)
- [Check Point. (2020, November 6). Ransomware Alert: Pay2Key. Retrieved January 4, 2021.](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)
- [Mandiant. (2024, March 14). APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations. Retrieved May 3, 2024.](https://services.google.com/fh/files/misc/apt43-report-en.pdf)
- [Google Threat Intelligence Group. (2025, June 4). The Cost of a Call: From Voice Phishing to Data Extortion. Retrieved October 22, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion)

---

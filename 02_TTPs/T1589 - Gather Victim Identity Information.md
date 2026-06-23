# Gather Victim Identity Information

## Description

Adversaries may gather information about the victim's identity that can be used during targeting. Information about identities may include a variety of details, including personal data (ex: employee names, email addresses, security question responses, etc.) as well as sensitive details such as credentials or multi-factor authentication (MFA) configurations.

Adversaries may gather this information in various ways, such as direct elicitation via Phishing for Information . Information about users could also be enumerated via other active means (i.e. Active Scanning ) such as probing and analyzing responses from authentication services that may reveal valid usernames in a system or permitted MFA /methods associated with those usernames. [1] [2] Information about victims may also be exposed to adversaries via online or other accessible data sets (ex: Social Media or Search Victim-Owned Websites ). [3] [4] [5] [6] [7] [8] [9] [10]

Gathering this information may reveal opportunities for other forms of reconnaissance (ex: Search Open Websites/Domains or Phishing for Information ), establishing operational resources (ex: Compromise Accounts ), and/or initial access (ex: Phishing or Valid Accounts ).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0050 | APT32 | APT32 has conducted targeted surveillance against activists and bloggers. [11] |
| G1052 | Contagious Interview | Contagious Interview has researched specific professional groups such as software developers for targeting. [12] [13] [14] [15] [16] [17] Contagious Interview has also researched individuals who work in roles related to cryptocurrency and blockchain technologies. [18] [19] |
| G1016 | FIN13 | FIN13 has researched employees to target for social engineering attacks. [20] |
| G1001 | HEXANE | HEXANE has identified specific potential victims at targeted organizations. [21] |
| G1004 | LAPSUS$ | LAPSUS$ has gathered detailed information of target employees to enhance their social engineering lures. [22] |
| G0059 | Magic Hound | Magic Hound has acquired mobile phone numbers of potential targets, possibly for mobile malware or additional phishing operations. [23] |
| C0022 | Operation Dream Job | For Operation Dream Job , Lazarus Group conducted extensive reconnaissance research on potential targets. [24] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors targeted people based on their organizational roles and privileges. [25] |
| G1015 | Scattered Spider | Scattered Spider has used information from previous data breaches to identify employee names to be used in social engineering. [26] |
| G1033 | Star Blizzard | Star Blizzard has identified ways to engage targets by researching potential victims' interests and social or professional contacts. [27] |
| G1055 | VOID MANTICORE | VOID MANTICORE has gathered details on their intended victims to aid in social engineering efforts for leveraging tailored themes of attacks. [28] |
| G1017 | Volt Typhoon | Volt Typhoon has gathered victim identify information during pre-compromise reconnaissance. [29] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0841 | Detection of Gather Victim Identity Information | AN1973 | Monitor for suspicious network traffic that could be indicative of probing for user information, such as large/iterative quantities of authentication requests originating from a single source (especially if the source is known to be associated with an adversary/botnet). Analyzing web metadata may also reveal artifacts that can be attributed to potentially malicious activity, such as referer or user-agent string HTTP/S fields. |

---

## References

- [GrimHacker. (2017, July 24). Office365 ActiveSync Username Enumeration. Retrieved December 9, 2021.](https://grimhacker.com/2017/07/24/office365-activesync-username-enumeration/)
- [Noah Corradin and Shuyang Wang. (2023, August 1). Behind The Breach: Self-Service Password Reset (SSPR) Abuse in Azure AD. Retrieved March 28, 2024.](https://www.obsidiansecurity.com/blog/behind-the-breach-self-service-password-reset-azure-ad/)
- [Cybersecurity Resource Center. (n.d.). CYBERSECURITY INCIDENTS. Retrieved September 16, 2024.](https://web.archive.org/web/20230602111604/https://www.opm.gov/cybersecurity/cybersecurity-incidents/)
- [Thomson, I. (2017, September 26). Deloitte is a sitting duck: Key systems with RDP open, VPN and proxy 'login details leaked'. Retrieved October 19, 2020.](https://www.theregister.com/2017/09/26/deloitte_leak_github_and_google/)
- [McCarthy, K. (2015, February 28). FORK ME! Uber hauls GitHub into court to find who hacked database of 50,000 drivers. Retrieved October 19, 2020.](https://www.theregister.com/2015/02/28/uber_subpoenas_github_for_hacker_details/)
- [Detectify. (2016, April 28). Slack bot token leakage exposing business critical information. Retrieved November 17, 2024.](https://labs.detectify.com/writeups/slack-bot-token-leakage-exposing-business-critical-information/)
- [Sandvik, R. (2014, January 14). Attackers Scrape GitHub For Cloud Service Credentials, Hijack Account To Mine Virtual Currency. Retrieved October 19, 2020.](https://www.forbes.com/sites/runasandvik/2014/01/14/attackers-scrape-github-for-cloud-service-credentials-hijack-account-to-mine-virtual-currency/#242c479d3196)
- [Dylan Ayrey. (2016, December 31). truffleHog. Retrieved October 19, 2020.](https://github.com/dxa4481/truffleHog)
- [Michael Henriksen. (2018, June 9). Gitrob: Putting the Open Source in OSINT. Retrieved October 19, 2020.](https://github.com/michenriksen/gitrob)
- [Ng, A. (2019, January 17). Massive breach leaks 773 million email addresses, 21 million passwords. Retrieved October 20, 2020.](https://www.cnet.com/news/massive-breach-leaks-773-million-emails-21-million-passwords/)
- [Amnesty International. (2021, February 24). Vietnamese activists targeted by notorious hacking group. Retrieved March 1, 2021.](https://www.amnestyusa.org/wp-content/uploads/2021/02/Click-and-Bait_Vietnamese-Human-Rights-Defenders-Targeted-with-Spyware-Attacks.pdf)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Ryan Sherstobitoff. (2024, October 29). Inside a North Korean Phishing Operation Targeting DevOps Employees. Retrieved October 20, 2025.](https://securityscorecard.com/blog/inside-a-north-korean-phishing-operation-targeting-devops-employees/)
- [Securonix Threat Research, D.Iuzvyk, T. Peck, O.Kolesnikov. (2024, April 24). Analysis of DEV#POPPER: New Attack Campaign Targeting Software Developers Likely Associated With North Korean Threat Actors. Retrieved October 20, 2025.](https://www.securonix.com/blog/analysis-of-devpopper-new-attack-campaign-targeting-software-developers-likely-associated-with-north-korean-threat-actors/)
- [Steve Cobb. (2024, October 29). The Job Offer That Wasn’t: How We Stopped an Espionage Plot. Retrieved October 20, 2025.](https://securityscorecard.com/blog/the-job-offer-that-wasnt-how-we-stopped-an-espionage-plot/)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Unit42. (2024, October 9). Contagious Interview: DPRK Threat Actors Lure Tech Industry Job Seekers to Install New Variants of BeaverTail and InvisibleFerret Malware. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
- [Aleksandar Milenkoski, Sreekar Madabushi, Kenneth Kinion. (2025, September 4). Contagious Interview | North Korean Threat Actors Reveal Plans and Ops by Abusing Cyber Intel Platforms. Retrieved October 20, 2025.](https://www.sentinelone.com/labs/contagious-interview-threat-actors-scout-cyber-intel-platforms-reveal-plans-and-ops/)
- [Amaury G., Coline Chavane, Felix Aimé and Sekoia TDR. (2025, March 31). From Contagious to ClickFake Interview: Lazarus leveraging the ClickFix tactic. Retrieved April 1, 2025.](https://blog.sekoia.io/clickfake-interview-campaign-by-lazarus/)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [ClearSky Cyber Security . (2021, August). New Iranian Espionage Campaign By “Siamesekitten” - Lyceum. Retrieved June 6, 2022.](https://www.clearskysec.com/siamesekitten/)
- [MSTIC, DART, M365 Defender. (2022, March 24). DEV-0537 Criminal Actor Targeting Organizations for Data Exfiltration and Destruction. Retrieved May 17, 2022.](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)
- [Miller, J. et al. (2021, July 13). Operation SpoofedScholars: A Conversation with TA453. Retrieved August 18, 2021.](https://www.proofpoint.com/us/blog/threat-insight/operation-spoofedscholars-conversation-ta453)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Mandiant Incident Response. (2025, July 23). From Help Desk to Hypervisor: Defending Your VMware vSphere Estate from UNC3944. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)
- [CISA, et al. (2023, December 7). Russian FSB Cyber Actor Star Blizzard Continues Worldwide Spear-phishing Campaigns. Retrieved June 13, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-341a)
- [FBI. (2026, March 20). FBI Flash: FLASH-20260320-001:Government of Iran Cyber Actors Deploy Telegram C2 to Push Malware to Identified Targets. Retrieved April 20, 2026.](https://www.ic3.gov/CSA/2026/260320.pdf)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)

---

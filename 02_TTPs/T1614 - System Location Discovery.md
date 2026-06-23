# System Location Discovery

## Description

Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from System Location Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings. [1] [2] [3] Windows API functions such as GetLocaleInfoW can also be used to determine the locale of the host. [1] In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance. [4] [5]

Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services. [6] [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1025 | Amadey | Amadey does not run any tasks or install additional malware if the victim machine is based in Russia. [7] |
| S9031 | AshTag | AshTag can check geolocation on targeted systems. [8] |
| S0115 | Crimson | Crimson can identify the geographical location of a victim host. [9] |
| S1153 | Cuckoo Stealer | Cuckoo Stealer can determine the geographical location of a victim host by checking the language. [10] |
| S1111 | DarkGate | DarkGate queries system locale information during execution. [11] Later versions of DarkGate query GetSystemDefaultLCID for locale information to determine if the malware is executing in Russian-speaking countries. [12] |
| S0673 | DarkWatchman | DarkWatchman can identity the OS locale of a compromised host. [13] |
| S9010 | GlassWorm | GlassWorm has leveraged geofencing logic to detect whether it is operating in a Russian associated time zone to determine whether it continues to execute. [14] |
| S1138 | Gootloader | Gootloader can use IP geolocation to determine if the person browsing to a compromised site is within a targeted territory such as the US, Canada, Germany, and South Korea. [15] |
| S0632 | GrimAgent | GrimAgent can identify the country code on a compromised host. [16] |
| S1249 | HexEval Loader | HexEval Loader has a function where the C2 endpoint can identify the geographical location of a victim host based on request headers, execution environment and runtime conditions. [17] |
| S1245 | InvisibleFerret | InvisibleFerret has collected the internal IP address, IP geolocation information of the infected host and sends the data to a C2 server. [18] InvisibleFerret has also leveraged the "pay" module to obtain region name, country, city, zip code, ISP, latitude and longitude using "http://ip-api.com/json". [19] |
| S0013 | PlugX | PlugX has obtained the location of the victim device by leveraging GetSystemDefaultLCID . [20] |
| S9019 | PureCrypter | PureCrypter can use kernel32!GetGeoInfo to determine system location. [21] |
| S0262 | QuasarRAT | QuasarRAT can determine the country a victim host is located in. [22] |
| S1148 | Raccoon Stealer | Raccoon Stealer collects the Locale Name of the infected device via GetUserDefaultLocaleName to determine whether the string ru is included, but in analyzed samples no action is taken if present. [23] |
| S0481 | Ragnar Locker | Before executing malicious code, Ragnar Locker checks the Windows API GetLocaleInfoW and doesn't encrypt files if it finds a former Soviet country. [1] |
| S1240 | RedLine Stealer | RedLine Stealer has gathered detailed information about victims’ systems, such as IP addresses, and geolocation. [24] [25] [26] RedLine Stealer has also checked the IP from where it was being executed and leveraged an opensource geolocation IP-lookup service. [27] |
| S0332 | Remcos | Remcos can identify the location of targeted devices. [28] |
| S1018 | Saint Bot | Saint Bot has conducted system locale checks to see if the compromised host is in Russia, Ukraine, Belarus, Armenia, Kazakhstan, or Moldova. [29] [30] |
| S9030 | SameCoin | SameCoin can attempt to connect to the Israel Home Front Command site, oref.org[.]il, which is only reachable from within Israel to verify the target's location. [31] |
| S0461 | SDBbot | SDBbot can collected the country code of a compromised machine. [32] |
| G1008 | SideCopy | SideCopy has identified the country location of a compromised host. [33] |
| S1124 | SocGholish | SocGholish can use IP-based geolocation to limit infections to victims in North America, Europe, and a small number of Asian-Pacific nations. [34] |
| S9034 | Tsundere Botnet | Tsundere Botnet has checked the victim machine’s location by obtaining the culture name of the machine. [35] |
| G1017 | Volt Typhoon | Volt Typhoon has obtained the victim's system current location. [36] |
| S1248 | XORIndex Loader | XORIndex Loader can identify the geographical location of a victim host. [37] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0043 | Detection Strategy for System Location Discovery | AN0119 | Unusual process or API usage attempting to query system locale, timezone, or keyboard layout (e.g., calls to GetLocaleInfoW, GetTimeZoneInformation). Detection can be enhanced by correlating with processes not typically associated with system configuration queries, such as unknown binaries or scripts. |
| AN0120 | Detection of commands accessing locale, timezone, or language settings such as 'locale', 'timedatectl', or parsing /etc/timezone. Anomalous execution by unusual users or automation scripts should be flagged. |  |  |
| AN0121 | Detection of system calls or commands accessing system locale (e.g., 'defaults read -g AppleLocale', 'systemsetup -gettimezone'). Correlate with unusual parent processes or execution contexts. |  |  |
| AN0122 | Detection of queries to instance metadata services (e.g., AWS IMDS, Azure Metadata Service) for availability zone, region, or network geolocation details. Correlation with non-management accounts or non-standard workloads may indicate adversary reconnaissance. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0043 | Detection Strategy for System Location Discovery | AN0119 | Unusual process or API usage attempting to query system locale, timezone, or keyboard layout (e.g., calls to GetLocaleInfoW, GetTimeZoneInformation). Detection can be enhanced by correlating with processes not typically associated with system configuration queries, such as unknown binaries or scripts. |
| AN0120 | Detection of commands accessing locale, timezone, or language settings such as 'locale', 'timedatectl', or parsing /etc/timezone. Anomalous execution by unusual users or automation scripts should be flagged. |  |  |
| AN0121 | Detection of system calls or commands accessing system locale (e.g., 'defaults read -g AppleLocale', 'systemsetup -gettimezone'). Correlate with unusual parent processes or execution contexts. |  |  |
| AN0122 | Detection of queries to instance metadata services (e.g., AWS IMDS, Azure Metadata Service) for availability zone, region, or network geolocation details. Correlation with non-management accounts or non-standard workloads may indicate adversary reconnaissance. |  |  |

---

## References

- [FBI. (2020, November 19). Indicators of Compromise Associated with Ragnar Locker Ransomware. Retrieved September 12, 2024.](https://s3.documentcloud.org/documents/20413525/fbi-flash-indicators-of-compromise-ragnar-locker-ransomware-11192020-bc.pdf)
- [Wisniewski, C. (2016, May 3). Location-based threats: How cybercriminals target you based on where you live. Retrieved April 1, 2021.](https://news.sophos.com/en-us/2016/05/03/location-based-ransomware-threat-research/)
- [Abrams, L. (2020, October 23). New RAT malware gets commands via Discord, has ransomware feature. Retrieved April 1, 2021.](https://www.bleepingcomputer.com/news/security/new-rat-malware-gets-commands-via-discord-has-ransomware-feature/)
- [Amazon. (n.d.). Instance identity documents. Retrieved April 2, 2021.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html)
- [Microsoft. (2021, February 21). Azure Instance Metadata Service (Windows). Retrieved April 2, 2021.](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/instance-metadata-service?tabs=windows)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved April 1, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [Kasuya, M. (2020, January 8). Threat Spotlight: Amadey Bot Targets Non-Russian Users. Retrieved July 14, 2022.](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
- [Unit 42. (2025, December 11). Hamas-Affiliated Ashen Lepus Targets Middle Eastern Diplomatic Entities With New AshTag Malware Suite. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [Kohler, A. and Lopez, C. (2024, April 30). Malware: Cuckoo Behaves Like Cross Between Infostealer and Spyware. Retrieved August 20, 2024.](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Ernesto Fernández Provecho, Pham Duy Phuc, Ciana Driscoll & Vinoo Thomas. (2023, November 21). The Continued Evolution of the DarkGate Malware-as-a-Service. Retrieved February 9, 2024.](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [Kirill Boychenko. (2026, January 31). GlassWorm Loader Hits Open VSX via Developer Account Compromise. Retrieved April 10, 2026.](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
- [Pirozzi, A. (2021, June 16). Gootloader: ‘Initial Access as a Service’ Platform Expands Its Search for High Value Targets. Retrieved May 28, 2024.](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)
- [Priego, A. (2021, July). THE BROTHERS GRIM: THE REVERSING TALE OF GRIMAGENT MALWARE USED BY RYUK. Retrieved September 19, 2024.](https://www.group-ib.com/blog/grimagent/)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Dumont, R. (2022, June 13). Technical Analysis of PureCrypter: A Fully-Functional Loader Distributing Remote Access Trojans and Information Stealers. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
- [CISA. (2018, December 18). Analysis Report (AR18-352A) Quasar Open-Source Remote Administration Tool. Retrieved August 1, 2022.](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
- [S2W TALON. (2022, June 16). Raccoon Stealer is Back with a New Version. Retrieved August 1, 2024.](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
- [Alexandre Cote Cyr. (2024, November 8). Life on a crooked RedLine: Analyzing the infamous infostealer’s backend. Retrieved September 17, 2025.](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)
- [George Glass. (2024, August 14). REDLINESTEALER Malware Driving the Initial Access Broker Market. Retrieved September 17, 2025.](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
- [Proofpoint Threat Insight Team, Jeremy H, Axel F. (2020, March 16). New Redline Password Stealer Malware. Retrieved September 17, 2025.](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
- [Mohansundaram M, Neil Tyagi. (2024, April 17). Redline Stealer: A Novel Approach. Retrieved September 17, 2025.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/redline-stealer-a-novel-approach/)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Hasherezade. (2021, April 6). A deep dive into Saint Bot, a new downloader. Retrieved June 9, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Check Point. (2024, November 12). Hamas-affiliated Threat Actor WIRTE Continues its Middle East Operations and Moves to Disruptive Activity. Retrieved April 20, 2026.](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [Secureworks. (n.d.). GOLD PRELUDE . Retrieved March 22, 2024.](https://www.secureworks.com/research/threat-profiles/gold-prelude)
- [Ubiedo, L. (2025, November 20). Blockchain and Node.js abused by Tsundere: an emerging botnet. Retrieved April 6, 2026.](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Kirill Boychenko. (2025, July 14). Contagious Interview Campaign Escalates With 67 Malicious npm Packages and New Malware Loader. Retrieved October 19, 2025.](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)

---

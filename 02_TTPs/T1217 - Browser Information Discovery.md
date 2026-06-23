# Browser Information Discovery

## Description

Adversaries may enumerate information about browsers to learn more about compromised environments. Data saved by browsers (such as bookmarks, accounts, and browsing history) may reveal a variety of personal information about users (e.g., banking sites, relationships/interests, social media, etc.) as well as details about internal network resources such as servers, tools/dashboards, or other related infrastructure. [1]

Browser information may also highlight additional targets after an adversary has access to valid credentials, especially Credentials In Files associated with logins cached by a browser.

Specific storage locations vary based on platform and/or application, but browser information is typically stored in local files and databases (e.g., %APPDATA%/Google/Chrome ). [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0057 | 3CX Supply Chain Attack | During the 3CX Supply Chain Attack , AppleJeus leveraged ICONICSTEALER to steal browser information to include browser history located on the infected host. [3] [4] [5] |
| G0082 | APT38 | APT38 has collected browser bookmark information to learn more about compromised hosts, obtain personal information about users, and acquire details about internal network resources. [6] |
| S1246 | BeaverTail | BeaverTail has searched the victim device for browser extensions including those commonly associated with cryptocurrency wallets. [7] [8] [9] [10] [11] [12] [13] |
| S0274 | Calisto | Calisto collects information on bookmarks from Google Chrome. [14] |
| G0114 | Chimera | Chimera has used type \ \c$\Users\ \Favorites\Links\Bookmarks bar\Imported From IE*citrix* for bookmark discovery. [15] |
| S1153 | Cuckoo Stealer | Cuckoo Stealer can collect bookmarks, cookies, and history from Safari. [16] |
| S0673 | DarkWatchman | DarkWatchman can retrieve browser history. [17] |
| S0567 | Dtrack | Dtrack can retrieve browser history. [18] [19] |
| S0363 | Empire | Empire has the ability to gather browser data such as bookmarks and visited sites. [20] |
| G0117 | Fox Kitten | Fox Kitten has used Google Chrome bookmarks to identify internal resources and assets. [21] |
| S9010 | GlassWorm | GlassWorm has searched browser data for cookies, history, login databases, and cryptocurrency wallets. [22] |
| C0044 | Juicy Mix | During Juicy Mix , OilRig used the CDumper (Chrome browser) and EDumper (Edge browser) data stealers to collect cookies, browsing history, and credentials. [23] |
| G0094 | Kimsuky | Kimsuky has collected sensitive browser data using the function GetBrowserData() to include login credentials, bookmarks, cookies, and encryption keys. [24] |
| S1185 | LightSpy | To collect data on the host's Wi-Fi connection history, LightSpy reads the /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist file. It also utilizes Apple's CWWiFiClient API to scan for nearby Wi-Fi networks and obtain data on the SSID, security type, and RSSI (signal strength) values. [25] |
| S0681 | Lizar | Lizar can retrieve browser history and database files. [26] [27] |
| S1213 | Lumma Stealer | Lumma Stealer has identified and gathered information from two-factor authentication extensions for multiple browsers. [28] |
| S0409 | Machete | Machete retrieves the user profile data (e.g., browsers) from Chrome and Firefox browsers. [29] |
| S1060 | Mafalda | Mafalda can collect the contents of the %USERPROFILE%\AppData\Local\Google\Chrome\User Data\LocalState file. [30] |
| S1122 | Mispadu | Mispadu can monitor browser activity for online banking actions and display full-screen overlay images to block user access to the intended site or present additional data fields. [31] [32] |
| S0079 | MobileOrder | MobileOrder has a command to upload to its C2 server victim browser bookmarks. [33] |
| G1036 | Moonstone Sleet | Moonstone Sleet deployed malware such as YouieLoader capable of capturing victim system browser information. [34] |
| C0060 | Operation AkaiRyū | During Operation AkaiRyū , MirrorFace exported Chrome web data including contact information, keywords, autofill data, and stored credit card information. [35] |
| C0042 | Outer Space | During Outer Space , OilRig used a Chrome data dumper named MKG. [23] |
| S1012 | PowerLess | PowerLess has a browser info stealer module that can read Chrome and Edge browser database files. [36] |
| S1240 | RedLine Stealer | RedLine Stealer can collect information from browsers and browser extensions. [37] |
| G1015 | Scattered Spider | Scattered Spider retrieves browser histories via infostealer malware such as Raccoon Stealer. [38] |
| S1042 | SUGARDUMP | SUGARDUMP has collected browser bookmark and history information. [39] |
| S1196 | Troll Stealer | Troll Stealer collects information from Chromium-based browsers and Firefox such as cookies, history, downloads, and extensions. [40] [41] |
| G1017 | Volt Typhoon | Volt Typhoon has targeted the browsing history of network administrators. [42] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0013 | Detection of Local Browser Artifact Access for Reconnaissance | AN0037 | Access to browser artifact locations (e.g., Chrome, Edge, Firefox) by processes like PowerShell, cmd.exe, or unknown tools, followed by file reads, decoding, or export operations indicating enumeration of bookmarks, autofill, or history databases. |
| AN0038 | Unauthorized shell or script-based access to browser config or SQLite history files, typically in ~/.config/google-chrome/, ~/.mozilla/, or ~/.var/app folders, indicating enumeration of bookmarks or saved credentials. |  |  |
| AN0039 | Scripting or CLI tool access to ~/Library/Application Support/Google/Chrome or ~/Library/Safari bookmarks, cookies, or history databases. Detection relies on unexpected processes accessing or reading from these locations. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0013 | Detection of Local Browser Artifact Access for Reconnaissance | AN0037 | Access to browser artifact locations (e.g., Chrome, Edge, Firefox) by processes like PowerShell, cmd.exe, or unknown tools, followed by file reads, decoding, or export operations indicating enumeration of bookmarks, autofill, or history databases. |
| AN0038 | Unauthorized shell or script-based access to browser config or SQLite history files, typically in ~/.config/google-chrome/, ~/.mozilla/, or ~/.var/app folders, indicating enumeration of bookmarks or saved credentials. |  |  |
| AN0039 | Scripting or CLI tool access to ~/Library/Application Support/Google/Chrome or ~/Library/Safari bookmarks, cookies, or history databases. Detection relies on unexpected processes accessing or reading from these locations. |  |  |

---

## References

- [Golubev, S. (n.d.). How malware steals autofill data from browsers. Retrieved March 28, 2023.](https://www.kaspersky.com/blog/browser-data-theft/27871/)
- [Chrome Enterprise and Education Help. (n.d.). Use Chrome Browser with Roaming User Profiles. Retrieved March 28, 2023.](https://support.google.com/chrome/a/answer/7349337)
- [Ankur Saini, Callum Roxan, Charlie Gardner, Paul Rascagneres, Steven Adair, Tom Lancaster. (2023, March 30). 3CX Supply Chain Compromise Leads to ICONIC Incident. Retrieved October 21, 2025.](https://www.volexity.com/blog/2023/03/30/3cx-supply-chain-compromise-leads-to-iconic-incident/)
- [Jeff Johnson, Fred Plan, Adrian Sanchez, Renato Fontana, Jake Nicastro, Dimiter Andonov, Marius Fodoreanu, Daniel Scott. (2023, April 20). 3CX Software Supply Chain Compromise Initiated by a Prior Software Supply Chain Compromise; Suspected North Korean Actor Responsible. Retrieved August 25, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise/)
- [Trend Micro Research. (2023, March 30). Preventing and Detecting Attacks Involving 3CX Desktop App. Retrieved October 21, 2025.](https://www.trendmicro.com/en_us/research/23/c/information-on-attacks-involving-3cx-desktop-app.html)
- [DHS/CISA. (2020, August 26). FASTCash 2.0: North Korea's BeagleBoyz Robbing Banks. Retrieved September 29, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)
- [eSentire Threat Response Unit (TRU). (2024, November 14). Bored BeaverTail & InvisibleFerret Yacht Club – A Lazarus Lure Pt.2. Retrieved October 17, 2025.](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
- [Insikt Group. (2025, February 13). Inside the Scam: North Korea’s IT Worker Threat. Retrieved October 17, 2025.](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)
- [Kirill Boychenko. (2025, July 14). Contagious Interview Campaign Escalates With 67 Malicious npm Packages and New Malware Loader. Retrieved October 19, 2025.](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Unit42. (2024, October 9). Contagious Interview: DPRK Threat Actors Lure Tech Industry Job Seekers to Install New Variants of BeaverTail and InvisibleFerret Malware. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
- [Kuzin, M., Zelensky S. (2018, July 20). Calisto Trojan for macOS. Retrieved September 7, 2018.](https://securelist.com/calisto-trojan-for-macos/86543/)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Kohler, A. and Lopez, C. (2024, April 30). Malware: Cuckoo Behaves Like Cross Between Infostealer and Spyware. Retrieved August 20, 2024.](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [Konstantin Zykov. (2019, September 23). Hello! My name is Dtrack. Retrieved January 20, 2021.](https://securelist.com/my-name-is-dtrack/93338/)
- [Hod Gavriel. (2019, November 21). Dtrack: In-depth analysis of APT on a nuclear power plant. Retrieved January 20, 2021.](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [CISA. (2020, September 15). Iran-Based Threat Actor Exploits VPN Vulnerabilities. Retrieved December 21, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)
- [Kirill Boychenko. (2026, January 31). GlassWorm Loader Hits Open VSX via Developer Account Compromise. Retrieved April 10, 2026.](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
- [Hromcova, Z. and Burgher, A. (2023, September 21). OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes. Retrieved November 21, 2024.](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Stuart Ashenbrenner, Alden Schmidt. (2024, April 25). LightSpy Malware Variant Targeting macOS. Retrieved January 3, 2025.](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
- [Seals, T. (2021, May 14). FIN7 Backdoor Masquerades as Ethical Hacking Tool. Retrieved February 2, 2022.](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [Cybereaon Security Services Team. (n.d.). Your Data Is Under New Lummanagement: The Rise of LummaStealer. Retrieved March 22, 2025.](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [Pedro Tavares (Segurança Informática). (2020, September 15). Threat analysis: The emergent URSA trojan impacts many countries using a sophisticated loader. Retrieved March 13, 2024.](https://seguranca-informatica.pt/threat-analysis-the-emergent-ursa-trojan-impacts-many-countries-using-a-sophisticated-loader/)
- [SCILabs. (2021, December 23). Cyber Threat Profile Malteiro. Retrieved March 13, 2024.](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
- [Falcone, R. and Miller-Osborn, J.. (2016, January 24). Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists. Retrieved February 10, 2016.](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
- [Microsoft Threat Intelligence. (2024, May 28). Moonstone Sleet emerges as new North Korean threat actor with new bag of tricks. Retrieved August 26, 2024.](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)
- [Dominik Breitenbacher. (2025, March 18). Operation AkaiRyū: MirrorFace invites Europe to Expo 2025 and revives ANEL backdoor. Retrieved May 22, 2025.](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)
- [Cybereason Nocturnus. (2022, February 1). PowerLess Trojan: Iranian APT Phosphorus Adds New PowerShell Backdoor for Espionage. Retrieved June 1, 2022.](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)
- [Splunk Threat Research Team. (2023, June 1). Do Not Cross The 'RedLine' Stealer: Detections and Analysis. Retrieved September 17, 2025.](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
- [CISA. (2023, November 16). Cybersecurity Advisory: Scattered Spider (AA23-320A). Retrieved March 18, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)
- [Mandiant Israel Research Team. (2022, August 17). Suspected Iranian Actor Targeting Israeli Shipping, Healthcare, Government and Energy Sectors. Retrieved September 21, 2022.](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)
- [Jiho Kim & Sebin Lee, S2W. (2024, February 7). Kimsuky disguised as a Korean company signed with a valid certificate to distribute Troll Stealer (English ver.). Retrieved January 17, 2025.](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
- [Symantec Threat Hunter Team. (2024, May 16). Springtail: New Linux Backdoor Added to Toolkit. Retrieved January 17, 2025.](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)

---

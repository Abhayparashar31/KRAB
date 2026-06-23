# Non-Standard Port

## Description

Adversaries may communicate using a protocol and port pairing that are typically not associated. For example, HTTPS over port 8088 [1] or port 587 [2] as opposed to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or muddle analysis/parsing of network data.

Adversaries may also make changes to victim systems to abuse non-standard ports. For example, Registry keys and other configuration settings can be used to modify protocol and port pairings. [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries had created a Reverse SOCKS Proxy and communicated over the non-standard port 8008. [4] [5] |
| G0099 | APT-C-36 | APT-C-36 has used port 4050 for C2 communications. [6] |
| G0050 | APT32 | An APT32 backdoor can use HTTP over a non-standard TCP port (e.g 14146) which is specified in the backdoor configuration. [7] |
| G0064 | APT33 | APT33 has used HTTP over TCP ports 808 and 880 for command and control. [1] |
| S0245 | BADCALL | BADCALL communicates on ports 443 and 8000 with a FakeTLS method. [8] |
| S0239 | Bankshot | Bankshot binds and listens on port 1058 for HTTP traffic while also utilizing a FakeTLS method. [9] |
| S1246 | BeaverTail | BeaverTail has communicated with C2 IP addresses over ports 1224 or 1244. [10] [11] [12] |
| S0574 | BendyBear | BendyBear has used a custom RC4 and XOR encrypted protocol over port 443 for C2. [13] |
| C0018 | C0018 | During C0018 , the threat actors opened a variety of ports, including ports 28035, 32467, 41578, and 46892, to establish RDP connections. [14] |
| C0032 | C0032 | During the C0032 campaign, TEMP.Veles used port-protocol mismatches on ports such as 443, 4444, 8531, and 50501 during C2. [15] |
| G1052 | Contagious Interview | Contagious Interview has used TCP port 1224 for C2. [16] |
| S1155 | Covenant | Covenant listeners and controllers can be configured to use non-standard ports. [17] |
| S0687 | Cyclops Blink | Cyclops Blink can use non-standard ports for C2 not typically associated with HTTP or HTTPS traffic. [18] |
| G0105 | DarkVishnya | DarkVishnya used ports 5190 and 7900 for shellcode listeners, and 4444, 4445, 31337 for shellcode C2. [19] |
| S0021 | Derusbi | Derusbi has used unencrypted HTTP on port 443 for C2. [20] |
| G1003 | Ember Bear | Ember Bear has used various non-standard ports for C2 communication. [21] |
| S0367 | Emotet | Emotet has used HTTP over ports such as 20, 22, 443, 7080, and 50000, in addition to using ports commonly associated with HTTP/S. [22] [23] |
| G0046 | FIN7 | FIN7 has used port-protocol mismatches on ports such as 53, 80, 443, and 8080 during C2. [24] FIN7 has used TCP ports 59999 and 9898 for firewall rules. [25] |
| G0047 | Gamaredon Group | Gamaredon Group has used port 6856 for C2 communications. [26] |
| S9010 | GlassWorm | GlassWorm has distributed C2 using BitTorrent’s Distributed Hash Table (DHT) network to harness a decentralized command capability. [27] |
| S0493 | GoldenSpy | GoldenSpy has used HTTP over ports 9005 and 9006 for network traffic, 9002 for C2 requests, 33666 as a WebSocket, and 8090 to download files. [28] |
| S0237 | GravityRAT | GravityRAT has used HTTP over a non-standard port, such as TCP port 46769. [29] |
| S1211 | Hannotog | Hannotog uses non-standard listening ports, such as UDP 5900, for command and control purposes. [30] |
| S0246 | HARDRAIN | HARDRAIN binds and listens on port 443 with a FakeTLS method. [31] |
| S9023 | HiddenFace | HiddenFace 's passive mode listens on TCP 47000. [32] [33] |
| S0376 | HOPLIGHT | HOPLIGHT has connected outbound over TCP port 443 with a FakeTLS method. [34] |
| C0043 | Indian Critical Infrastructure Intrusions | During Indian Critical Infrastructure Intrusions , RedEcho used non-standard ports such as TCP 8080 for HTTP communication. [35] |
| S1245 | InvisibleFerret | InvisibleFerret has been observed utilizing HTTP communications to the C2 server over ports 1224, 2245 and 8637. [36] |
| C0035 | KV Botnet Activity | KV Botnet Activity generates a random port number greater than 30,000 to serve as the listener for subsequent command and control activity. [37] |
| G0032 | Lazarus Group | Some Lazarus Group malware uses a list of ordered port numbers to choose a port for C2 traffic, creating port-protocol mismatches. [38] [39] |
| S1016 | MacMa | MacMa has used TCP port 5633 for C2 Communication. [40] |
| G0059 | Magic Hound | Magic Hound malware has communicated with its C2 server over TCP ports 4443 and 10151 using HTTP. [41] [42] |
| S0455 | Metamorfo | Metamorfo has communicated with hosts over raw TCP on port 9999. [43] |
| S0149 | MoonWind | MoonWind communicates over ports 80, 443, 53, and 8080 via raw sockets instead of the protocols usually associated with the ports. [44] |
| G0069 | MuddyWater | MuddyWater has used ports 8043 and 8848 for botnet C2 communication. [45] |
| S0385 | njRAT | njRAT has used port 1177 for HTTP C2 communications. [46] |
| C0014 | Operation Wocao | During Operation Wocao , the threat actors used uncommon high ports for its backdoor C2, including ports 25667 and 47000. [47] |
| S0352 | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D has used a custom binary protocol over TCP port 443 for C2. [48] |
| S1145 | Pikabot | Pikabot uses non-standard ports, such as 2967, 2223, and others, for HTTPS command and control communication. [49] |
| S1031 | PingPull | PingPull can use HTTPS over port 8080 for C2. [50] |
| S0013 | PlugX | PlugX has used random, high-number, non-standard ports to listen for subsequent actions and C2 activities. [51] |
| S0428 | PoetRAT | PoetRAT used TLS to encrypt communications over port 143 [52] |
| C0055 | Quad7 Activity | Quad7 Activity has used non-standard TCP ports – such as 7777, 11288, 63256, 63210, 3256, and 3556 for C2. [53] [54] |
| S0262 | QuasarRAT | QuasarRAT can use port 4782 on the compromised host for TCP callbacks. [55] |
| S1130 | Raspberry Robin | Raspberry Robin will communicate via HTTP over port 8080 for command and control traffic. [56] |
| G1042 | RedEcho | RedEcho has used non-standard ports such as TCP 8080 for HTTP communication. [35] |
| S0153 | RedLeaves | RedLeaves can use HTTP over non-standard ports, such as 995, for C2. [57] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 used a backdoor that binds to port 45678 by default. [58] |
| G0106 | Rocke | Rocke 's miner connects to a C2 server using port 51640. [59] |
| S1078 | RotaJakiro | RotaJakiro uses a custom binary protocol over TCP port 443. [60] |
| S0148 | RTM | RTM used Port 44443 for its VNC module. [61] |
| G0034 | Sandworm Team | Sandworm Team has used port 6789 to accept connections on the group's SSH server. [62] |
| S1085 | Sardonic | Sardonic has the ability to connect with actor-controlled C2 servers using a custom binary protocol over port 443. [63] |
| G0091 | Silence | Silence has used port 444 when sending data about the system from the client to the server. [64] |
| S9024 | SPAWNCHIMERA | SPAWNCHIMERA has the ability to bind on a localhost and listen on port 8300. [65] [66] |
| S0491 | StrongPity | StrongPity has used HTTPS over port 1402 in C2 communication. [67] |
| S1049 | SUGARUSH | SUGARUSH has used port 4585 for a TCP connection to its C2. [68] |
| S9001 | SystemBC | The server component of SystemBC has used various TCP ports for C2 communication. [69] |
| S0266 | TrickBot | Some TrickBot samples have used HTTP over ports 447 and 8082 for C2. [70] [71] [72] Newer versions of TrickBot have been known to use a custom communication protocol which sends the data unencrypted over port 443. [73] |
| S0263 | TYPEFRAME | TYPEFRAME has used ports 443, 8080, and 8443 with a FakeTLS method. [74] |
| G1047 | Velvet Ant | Velvet Ant has used random high number ports for PlugX listeners on victim devices. [51] |
| S1218 | VIRTUALPIE | VIRTUALPIE has created listeners on hard coded TCP port 546. [75] |
| S1217 | VIRTUALPITA | VIRTUALPITA has created listeners on hard coded TCP ports such as 2233, 7475, and 18098. [75] |
| S0515 | WellMail | WellMail has been observed using TCP port 25, without using SMTP, to leverage an open port for secure command and control communications. [76] [77] |
| G0090 | WIRTE | WIRTE has used HTTPS over ports 2083 and 2087 for C2. [78] |
| S0412 | ZxShell | ZxShell can use ports 1985 and 1986 in HTTP/S communication. [79] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |
| M1030 | Network Segmentation | Properly configure firewalls and proxies to limit outgoing traffic to only necessary ports for that particular network segment. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0227 | Detection Strategy for Non-Standard Ports | AN0633 | Processes initiating outbound connections on uncommon ports or using protocols inconsistent with the assigned port. Correlating process creation with subsequent network connections reveals anomalies such as svchost.exe or Office applications using high, atypical ports. |
| AN0634 | Unusual daemons or user processes binding/listening on ports outside of standard ranges, or initiating client connections using mismatched protocol/port pairings. |  |  |
| AN0635 | Applications making outbound connections on non-standard ports or launchd services bound to ports inconsistent with system baselines. |  |  |
| AN0636 | VM services or management daemons communicating on ports not defined by VMware defaults, such as vpxa or hostd processes initiating traffic over high-numbered or unexpected ports. |  |  |

---

## References

- [Security Response attack Investigation Team. (2019, March 27). Elfin: Relentless Espionage Group Targets Multiple Organizations in Saudi Arabia and U.S.. Retrieved April 10, 2019.](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)
- [Zhang, X. (2018, April 05). Analysis of New Agent Tesla Spyware Variant. Retrieved November 5, 2018.](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)
- [The DFIR Report. (2022, March 1). "Change RDP port" #ContiLeaks. Retrieved September 12, 2024.](https://x.com/TheDFIRReport/status/1498657772254240768)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [ESET. (2026, January 30). DynoWiper update: Technical analysis and attribution. Retrieved April 22, 2026.](https://www.welivesecurity.com/en/eset-research/dynowiper-update-technical-analysis-attribution/)
- [QiAnXin Threat Intelligence Center. (2019, February 18). APT-C-36: Continuous Attacks Targeting Colombian Government Institutions and Corporations. Retrieved May 5, 2020.](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
- [Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)
- [US-CERT. (2018, February 06). Malware Analysis Report (MAR) - 10135536-G. Retrieved June 7, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)
- [US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Unit42. (2024, October 9). Contagious Interview: DPRK Threat Actors Lure Tech Industry Job Seekers to Install New Variants of BeaverTail and InvisibleFerret Malware. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
- [Harbison, M. (2021, February 9). BendyBear: Novel Chinese Shellcode Linked With Cyber Espionage Group BlackTech. Retrieved February 16, 2021.](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)
- [Costa, F. (2022, May 1). RaaS AvosLocker Incident Response Analysis. Retrieved January 11, 2023.](https://www.linkedin.com/pulse/raas-avoslocker-incident-response-analysis-fl%C3%A1vio-costa?trk=articles_directory)
- [Miller, S, et al. (2019, April 10). TRITON Actor TTP Profile, Custom Attack Tools, Detections, and ATT&CK Mapping. Retrieved April 16, 2019.](https://www.fireeye.com/blog/threat-research/2019/04/triton-actor-ttp-profile-custom-attack-tools-detections.html)
- [Kirill Boychenko. (2025, April 4). Lazarus Expands Malicious npm Campaign: 11 New Packages Add Malware Loaders and Bitbucket Payloads. Retrieved October 20, 2025.](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)
- [cobbr. (2021, April 21). Covenant. Retrieved September 4, 2024.](https://github.com/cobbr/Covenant)
- [NCSC. (2022, February 23). Cyclops Blink Malware Analysis Report. Retrieved March 3, 2022.](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
- [Golovanov, S. (2018, December 6). DarkVishnya: Banks attacked through direct connection to local network. Retrieved May 15, 2020.](https://securelist.com/darkvishnya/89169/)
- [Fidelis Cybersecurity. (2016, February 29). The Turbo Campaign, Featuring Derusbi for 64-bit Linux. Retrieved March 2, 2016.](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
- [US Cybersecurity & Infrastructure Security Agency et al. (2024, September 5). Russian Military Cyber Actors Target U.S. and Global Critical Infrastructure. Retrieved September 6, 2024.](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)
- [Brumaghin, E.. (2019, January 15). Emotet re-emerges after the holidays. Retrieved March 25, 2019.](https://blog.talosintelligence.com/2019/01/return-of-emotet.html)
- [Binary Defense. (n.d.). Emotet Evolves With new Wi-Fi Spreader. Retrieved September 8, 2023.](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
- [Carr, N., et al. (2018, August 01). On the Hunt for FIN7: Pursuing an Enigmatic and Evasive Global Criminal Operation. Retrieved August 23, 2018.](https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html)
- [The BlackBerry Research and Intelligence Team. (2024, April 17). Threat Group FIN7 Targets the U.S. Automotive Industry. Retrieved May 1, 2025.](https://blogs.blackberry.com/en/2024/04/fin7-targets-the-united-states-automotive-industry)
- [Venere, G. (2025, March 28). Gamaredon campaign abuses LNK files to distribute Remcos backdoor. Retrieved July 23, 2025.](https://blog.talosintelligence.com/gamaredon-campaign-distribute-remcos/)
- [Idan Dardikman. (2025, October 18). GlassWorm: First Self-Propagating Worm Using Invisible Code Hits OpenVSX Marketplace. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace)
- [Trustwave SpiderLabs. (2020, June 25). The Golden Tax Department and Emergence of GoldenSpy Malware. Retrieved July 23, 2020.](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)
- [Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
- [Symntec Threat Hunter Team. (2022, November 12). Billbug: State-sponsored Actor Targets Cert Authority, Government Agencies in Multiple Asian Countries. Retrieved March 15, 2025.](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
- [US-CERT. (2018, February 05). Malware Analysis Report (MAR) - 10135536-F. Retrieved June 11, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-F.pdf)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [Recorded Future Insikt Group. (2021, February). China-Linked Group RedEcho Targets the Indian Power Sector Amid Heightened Border Tensions. Retrieved November 21, 2024.](https://go.recordedfuture.com/hubfs/reports/cta-2021-0228.pdf)
- [eSentire Threat Response Unit (TRU). (2024, November 14). Bored BeaverTail & InvisibleFerret Yacht Club – A Lazarus Lure Pt.2. Retrieved October 17, 2025.](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
- [Black Lotus Labs. (2023, December 13). Routers Roasting On An Open Firewall: The KV-Botnet Investigation. Retrieved June 10, 2024.](https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Remote Administration Tools & Content Staging Malware Report. Retrieved March 16, 2016.](https://web.archive.org/web/20220608001455/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Lee, B. and Falcone, R. (2017, February 15). Magic Hound Campaign Attacks Saudi Targets. Retrieved December 27, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [Sierra, E., Iglesias, G.. (2018, April 24). Metamorfo Campaigns Targeting Brazilian Users. Retrieved July 30, 2020.](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
- [Miller-Osborn, J. and Grunzweig, J.. (2017, March 30). Trochilus and New MoonWind RATs Used In Attack Against Thai Organizations. Retrieved March 30, 2017.](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
- [FalconFeeds.io. (2026, March 6). MuddyWater in the Iran–Israel Cyber War: From PowerShell Scripts to Rust Implants. Retrieved March 12, 2026.](https://falconfeeds.io/blogs/muddywater-in-the-iran-israel-cyber-war-from-powershell-scripts-to-rust-implants)
- [Pascual, C. (2018, November 27). AutoIt-Compiled Worm Affecting Removable Media Delivers Fileless Version of BLADABINDI/njRAT Backdoor. Retrieved June 4, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Erye Hernandez and Danny Tsechansky. (2017, June 22). The New and Improved macOS Backdoor from OceanLotus. Retrieved September 8, 2023.](https://unit42.paloaltonetworks.com/unit42-new-improved-macos-backdoor-oceanlotus/)
- [Daniel Stepanic & Salim Bitam. (2024, February 23). PIKABOT, I choose you!. Retrieved July 12, 2024.](https://www.elastic.co/security-labs/pikabot-i-choose-you)
- [Unit 42. (2022, June 13). GALLIUM Expands Targeting Across Telecommunications, Government and Finance Sectors With New PingPull Tool. Retrieved August 7, 2022.](https://unit42.paloaltonetworks.com/pingpull-gallium/)
- [Sygnia Team. (2024, June 3). China-Nexus Threat Group ‘Velvet Ant’ Abuses F5 Load Balancers for Persistence. Retrieved March 14, 2025.](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
- [Mercer, W, et al. (2020, April 16). PoetRAT: Python RAT uses COVID-19 lures to target Azerbaijan public and private sectors. Retrieved April 27, 2020.](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
- [Microsoft Threat Intelligence. (2024, October 31). Chinese threat actor Storm-0940 uses credentials from password spray attacks from a covert network. Retrieved June 4, 2025.](https://www.microsoft.com/en-us/security/blog/2024/10/31/chinese-threat-actor-storm-0940-uses-credentials-from-password-spray-attacks-from-a-covert-network/)
- [Aime, F. et al. (n.d.). Solving the 7777 Botnet enigma: A cybersecurity quest. Retrieved July 23, 2024.](https://blog.sekoia.io/solving-the-7777-botnet-enigma-a-cybersecurity-quest/)
- [CISA. (2018, December 18). Analysis Report (AR18-352A) Quasar Open-Source Remote Administration Tool. Retrieved August 1, 2022.](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
- [Lauren Podber and Stef Rand. (2022, May 5). Raspberry Robin gets the worm early. Retrieved May 17, 2024.](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [Lamparski, L. et al. (2025, March 11). Ghost in the Router: China-Nexus Espionage Actor UNC3886 Targets Juniper Routers. Retrieved June 24, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers)
- [Anomali Labs. (2019, March 15). Rocke Evolves Its Arsenal With a New Malware Family Written in Golang. Retrieved April 24, 2019.](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)
- [Alex Turing. (2021, May 6). RotaJakiro, the Linux version of the OceanLotus. Retrieved June 14, 2023.](https://blog.netlab.360.com/rotajakiro_linux_version_of_oceanlotus/)
- [Faou, M. and Boutin, J. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
- [Cherepanov, A.. (2016, January 3). BlackEnergy by the SSHBearDoor: attacks against Ukrainian news media and electric industry . Retrieved June 10, 2020.](https://www.welivesecurity.com/2016/01/03/blackenergy-sshbeardoor-details-2015-attacks-ukrainian-news-media-electric-industry/)
- [Budaca, E., et al. (2021, August 25). FIN8 Threat Actor Goes Agile with New Sardonic Backdoor. Retrieved August 9, 2023.](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
- [Group-IB. (2018, September). Silence: Moving Into the Darkside. Retrieved May 5, 2020.](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)
- [Matt Lin, Austin Larsen, John Wolfram, Ashley Pearson, Josh Murchie, Lukasz Lamparski, Joseph Pisano, Ryan Hall, Ron Craft, Shawn Crew, Billy Wong, Tyler McLellan. (2024, April 4). Cutting Edge, Part 4: Ivanti Connect Secure VPN Post-Exploitation Lateral Movement Case Studies. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
- [Yuma Masubuchi. (2025, February 20). SPAWNCHIMERA Malware: The Chimera Spawning from Ivanti Connect Secure Vulnerability. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2025/02/spawnchimera.html)
- [Tudorica, R. et al. (2020, June 30). StrongPity APT - Revealing Trojanized Tools, Working Hours and Infrastructure. Retrieved July 20, 2020.](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)
- [Mandiant Israel Research Team. (2022, August 17). Suspected Iranian Actor Targeting Israeli Shipping, Healthcare, Government and Energy Sectors. Retrieved September 21, 2022.](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)
- [Truman, D. (2024, January 19). Inside the SYSTEMBC Command-and-Control Server. Retrieved June 18, 2025.](https://www.kroll.com/en/publications/cyber/inside-the-systembc-malware-server)
- [Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
- [Reaves, J. (2016, October 15). TrickBot: We Missed you, Dyre. Retrieved August 2, 2018.](https://www.fidelissecurity.com/threatgeek/2016/10/trickbot-we-missed-you-dyre)
- [Antazo, F. (2016, October 31). TSPY_TRICKLOAD.N. Retrieved September 14, 2018.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/tspy_trickload.n)
- [Radu Tudorica. (2021, July 12). A Fresh Look at Trickbot’s Ever-Improving VNC Module. Retrieved September 28, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/399/Bitdefender-PR-Whitepaper-Trickbot-creat5515-en-EN.pdf)
- [US-CERT. (2018, June 14). MAR-10135536-12 – North Korean Trojan: TYPEFRAME. Retrieved July 13, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
- [Alexander Marvi, Jeremy Koppen, Tufail Ahmed, and Jonathan Lepore. (2022, September 29). Bad VIB(E)s Part One: Investigating Novel Malware Persistence Within ESXi Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
- [CISA. (2020, July 16). MAR-10296782-3.v1 – WELLMAIL. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
- [National Cyber Security Centre. (2020, July 16). Advisory: APT29 targets COVID-19 vaccine development. Retrieved September 29, 2020.](https://www.ncsc.gov.uk/files/Advisory-APT29-targets-COVID-19-vaccine-development-V1-1.pdf)
- [Yamout, M. (2021, November 29). WIRTE’s campaign in the Middle East ‘living off the land’ since at least 2019. Retrieved February 1, 2022.](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)

---

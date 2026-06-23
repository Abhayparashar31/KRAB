# Fallback Channels

## Description

Adversaries may use fallback or alternate communication channels if the primary channel is compromised or inaccessible in order to maintain reliable command and control and to avoid data transfer thresholds.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0504 | Anchor | Anchor can use secondary C2 servers for communication after establishing connectivity and relaying victim information to primary C2 servers. [1] |
| S0622 | AppleSeed | AppleSeed can use a second channel for C2 when the primary channel is in upload mode. [2] |
| G0096 | APT41 | APT41 used the Steam community page as a fallback mechanism for C2. [3] |
| S0534 | Bazar | Bazar has the ability to use an alternative C2 server if the primary server fails. [4] |
| S0017 | BISCUIT | BISCUIT malware contains a secondary fallback command and control server that is contacted after the primary command and control server. [5] [6] |
| S0089 | BlackEnergy | BlackEnergy has the capability to communicate over a backup channel via plus.google.com. [7] |
| S1039 | Bumblebee | Bumblebee can use backup C2 servers if the primary server fails. [8] |
| S0348 | Cardinal RAT | Cardinal RAT can communicate over multiple C2 host and port combinations. [9] |
| S0674 | CharmPower | CharmPower can change its C2 channel once every 360 loops by retrieving a new domain from the actors’ S3 bucket. [10] |
| S0023 | CHOPSTICK | CHOPSTICK can switch to a new C2 channel if the current one is broken. [11] |
| S0538 | Crutch | Crutch has used a hardcoded GitHub repository as a fallback channel. [12] |
| S0021 | Derusbi | Derusbi uses a backup communication method with an HTTP beacon. [13] |
| S0062 | DustySky | DustySky has two hard-coded domains for C2 servers; if the first does not respond, it will try the second. [14] |
| S0377 | Ebury | Ebury has implemented a fallback mechanism to begin using a DGA when the attacker hasn't connected to the infected system for three days. [15] |
| S0401 | Exaramel for Linux | Exaramel for Linux can attempt to find a new C2 server if it receives an error. [16] |
| S0512 | FatDuke | FatDuke has used several C2 servers per targeted organization. [17] |
| G0046 | FIN7 | FIN7 's Harpy backdoor malware can use DNS as a backup channel for C2 if HTTP fails. [18] |
| S0666 | Gelsemium | Gelsemium can use multiple domains and protocols in C2. [19] |
| S9010 | GlassWorm | GlassWorm has utilized Google Calendar as backup C2. [20] [21] |
| S9023 | HiddenFace | HiddenFace can use active and passive C2 modes that use different encryption algorithms and backdoor commands. [22] |
| S0376 | HOPLIGHT | HOPLIGHT has multiple C2 channels in place in case one fails. [23] |
| S0260 | InvisiMole | InvisiMole has been configured with several servers available for alternate C2 communications. [24] [25] |
| S0044 | JHUHUGIT | JHUHUGIT tests if it can reach its C2 server by first attempting a direct connection, and if it fails, obtaining proxy settings and sending the connection through a proxy, and finally injecting code into a running browser if the proxy method fails. [26] |
| S0265 | Kazuar | Kazuar can accept multiple URLs for C2 servers. [27] |
| S1020 | Kevin | Kevin can assign hard-coded fallback domains for C2. [28] |
| S0236 | Kwampirs | Kwampirs uses a large list of C2 servers that it cycles through until a successful connection is established. [29] |
| G0032 | Lazarus Group | Lazarus Group malware SierraAlfa sends data to one of the hard-coded C2 servers chosen at random, and if the transmission fails, chooses a new C2 server to attempt the transmission again. [30] [31] |
| S0211 | Linfo | Linfo creates a backdoor through which remote attackers can change C2 servers. [32] |
| S0409 | Machete | Machete has sent data over HTTP if FTP failed, and has also used a fallback server. [33] |
| S0051 | MiniDuke | MiniDuke uses Google Search to identify C2 servers if its primary C2 method via Twitter is not working. [34] |
| S0084 | Mis-Type | Mis-Type first attempts to use a Base64-encoded network protocol over a raw TCP socket for C2, and if that method fails, falls back to a secondary HTTP-based protocol to communicate to an alternate C2 server. [35] |
| S0699 | Mythic | Mythic can use a list of C2 URLs as fallback mechanisms in case one IP or domain gets blocked. [36] |
| S0034 | NETEAGLE | NETEAGLE will attempt to detect if the infected host is configured to a proxy. If so, NETEAGLE will send beacons via an HTTP POST request; otherwise it will send beacons via UDP/6000. [37] |
| C0002 | Night Dragon | During Night Dragon , threat actors used company extranet servers as secondary C2 servers. [38] |
| S1172 | OilBooster | OilBooster can use a backup channel to request a new refresh token from its C2 server after 10 consecutive unsuccessful connections to the primary OneDrive C2 server. [39] |
| G0049 | OilRig | OilRig malware ISMAgent falls back to its DNS tunneling mechanism if it is unable to reach the C2 server over HTTP. [40] |
| S0501 | PipeMon | PipeMon can switch to an alternate C2 domain when a particular date has been reached. [41] |
| S0269 | QUADAGENT | QUADAGENT uses multiple protocols (HTTPS, HTTP, DNS) for its C2 server as fallback channels if communication with one is unsuccessful. [42] |
| S1084 | QUIETEXIT | QUIETEXIT can attempt to connect to a second hard-coded C2 if the first hard-coded C2 address fails. [43] |
| S0629 | RainyDay | RainyDay has the ability to switch between TCP and HTTP for C2 if one method is not working. [44] |
| S0495 | RDAT | RDAT has used HTTP if DNS C2 communications were not functioning. [45] |
| S0085 | S-Type | S-Type primarily uses port 80 for C2, but falls back to ports 443 or 8080 if initial communication fails. [35] |
| S1019 | Shark | Shark can update its configuration to use a different C2 server. [46] |
| S0444 | ShimRat | ShimRat has used a secondary C2 location if the first was unavailable. [47] |
| S0610 | SideTwist | SideTwist has primarily used port 443 for C2 but can use port 80 as a fallback. [48] |
| S0058 | SslMM | SslMM has a hard-coded primary and backup C2 string. [49] |
| S0603 | Stuxnet | Stuxnet has the ability to generate new C2 domains. [50] |
| S0586 | TAINTEDSCRIBE | TAINTEDSCRIBE can randomly pick one of five hard-coded IP addresses for C2 communication; if one of the IP fails, it will wait 60 seconds and then try another IP address. [51] |
| S0668 | TinyTurla | TinyTurla can go through a list of C2 server IPs and will try to register with each until one responds. [52] |
| S0266 | TrickBot | TrickBot can use secondary C2 servers for communication after establishing connectivity and relaying victim information to primary C2 servers. [1] |
| G1048 | UNC3886 | UNC3886 has employed layers of redundancy to maintain access to compromised environments including network devices, hypervisors, and virtual machines. [53] |
| S0022 | Uroburos | Uroburos can use up to 10 channels to communicate between implants. [54] |
| S0476 | Valak | Valak can communicate over multiple C2 hosts. [55] |
| S0059 | WinMM | WinMM is usually configured with primary and backup domains for C2 communications. [49] |
| S0117 | XTunnel | The C2 server used by XTunnel provides a port number to the victim to use as a fallback in case the connection closes on the currently used port. [11] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific protocol used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. [56] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0499 | Behavioral Detection of Fallback or Alternate C2 Channels | AN1376 | Establishing network connections on uncommon ports or protocols following C2 disruption or blocking. Often executed by processes that typically exhibit no network activity. |
| AN1377 | Creation of outbound connections on alternate ports or using covert transport (e.g., ICMP, DNS) from non-network-intensive processes, following known disruption or blocked traffic. |  |  |
| AN1378 | Outbound fallback traffic from low-profile or background launch agents using unusual protocols or destinations after primary channel inactivity. |  |  |
| AN1379 | Outbound traffic from host management services or guest-to-host interactions over unusual interfaces (e.g., backdoor API endpoints or external VPN tunnels). |  |  |

---

## References

- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1, 2020.](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Mandiant. (n.d.). Appendix C (Digital) - The Malware Arsenal. Retrieved July 18, 2016.](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)
- [Baumgartner, K. and Garnaeva, M.. (2014, November 3). BE2 custom plugins, router abuse, and target profiles. Retrieved March 24, 2016.](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
- [Merriman, K. and Trouerbach, P. (2022, April 28). This isn't Optimus Prime's Bumblebee but it's Still Transforming. Retrieved August 22, 2022.](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
- [Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
- [Faou, M. (2020, December 2). Turla Crutch: Keeping the “back door” open. Retrieved December 4, 2020.](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
- [Fidelis Cybersecurity. (2016, February 29). The Turbo Campaign, Featuring Derusbi for 64-bit Linux. Retrieved March 2, 2016.](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
- [ClearSky. (2016, January 7). Operation DustySky. Retrieved January 8, 2016.](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
- [Vachon, F. (2017, October 30). Windigo Still not Windigone: An Ebury Update . Retrieved February 10, 2021.](https://www.welivesecurity.com/2017/10/30/windigo-ebury-update-2/)
- [ANSSI. (2021, January 27). SANDWORM INTRUSION SET CAMPAIGN TARGETING CENTREON SYSTEMS. Retrieved March 30, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Crowdstrike. (2020, March 2). 2020 Global Threat Report. Retrieved December 11, 2020.](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Idan Dardikman. (2025, October 18). GlassWorm: First Self-Propagating Worm Using Invisible Code Hits OpenVSX Marketplace. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace)
- [Lotan Sery. (2025, December 10). GlassWorm Goes Native: Same Infrastructure, Hardened Delivery. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [ESET. (2016, October). En Route with Sednit - Part 1: Approaching the Target. Retrieved November 8, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Remote Administration Tools & Content Staging Malware Report. Retrieved March 16, 2016.](https://web.archive.org/web/20220608001455/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf)
- [Zhou, R. (2012, May 15). Backdoor.Linfo. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2013, February 27). The MiniDuke Mystery: PDF 0-day Government Spy Assembler 0x29A Micro Backdoor. Retrieved November 17, 2024.](https://web.archive.org/web/20170630181406/https://cdn.securelist.com/files/2014/07/themysteryofthepdf0-dayassemblermicrobackdoor.pdf)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Thomas, C. (n.d.). Mythc Documentation. Retrieved March 25, 2022.](https://docs.mythic-c2.net/)
- [FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved November 17, 2024.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
- [McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
- [Hromcova, Z. and Burgher, A. (2023, December 14). OilRig’s persistent attacks using cloud service-powered downloaders. Retrieved November 26, 2024.](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
- [Falcone, R. and Lee, B. (2017, July 27). OilRig Uses ISMDoor Variant; Possibly Linked to Greenbug Threat Group. Retrieved January 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/07/unit42-oilrig-uses-ismdoor-variant-possibly-linked-greenbug-threat-group/)
- [Tartare, M. et al. (2020, May 21). No “Game over” for the Winnti Group. Retrieved August 24, 2020.](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
- [Lee, B., Falcone, R. (2018, July 25). OilRig Targets Technology Service Provider and Government Agency with QUADAGENT. Retrieved August 9, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)
- [Mandiant. (2022, May 2). UNC3524: Eye Spy on Your Email. Retrieved August 17, 2023.](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
- [Vrabie, V. (2021, April 23). NAIKON – Traces from a Military Cyber-Espionage Operation. Retrieved June 29, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
- [Falcone, R. (2020, July 22). OilRig Targets Middle Eastern Telecommunications Organization and Adds Novel C2 Channel with Steganography to Its Inventory. Retrieved July 28, 2020.](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
- [ClearSky Cyber Security . (2021, August). New Iranian Espionage Campaign By “Siamesekitten” - Lyceum. Retrieved June 6, 2022.](https://www.clearskysec.com/siamesekitten/)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [Baumgartner, K., Golovkin, M.. (2015, May). The MsnMM Campaigns: The Earliest Naikon APT Campaigns. Retrieved April 10, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [USG. (2020, May 12). MAR-10288834-2.v1 – North Korean Trojan: TAINTEDSCRIBE. Retrieved March 5, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
- [Cisco Talos. (2021, September 21). TinyTurla - Turla deploys new malware to keep a secret backdoor on victim machines. Retrieved December 2, 2021.](https://blog.talosintelligence.com/2021/09/tinyturla.html)
- [Punsaen Boonyakarn, Shawn Chew, Logeswaran Nadarajan, Mathew Potaczek, Jakub Jozwiak, and Alex Marvi. (2024, June 18). Cloaked and Covert: Uncovering UNC3886 Espionage Operations. Retrieved September 24, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Duncan, B. (2020, July 24). Evolution of Valak, from Its Beginnings to Mass Distribution. Retrieved August 31, 2020.](https://unit42.paloaltonetworks.com/valak-evolution/)
- [Gardiner, J., Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

---

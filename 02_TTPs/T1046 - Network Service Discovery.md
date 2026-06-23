# Network Service Discovery

## Description

Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port, vulnerability, and/or wordlist scans using tools that are brought onto a system. [1]

Within cloud environments, adversaries may attempt to discover services running on other cloud hosts. Additionally, if the cloud environment is connected to a on-premises environment, adversaries may be able to identify services running on non-cloud systems as well.

Within macOS environments, adversaries may use the native Bonjour application to discover services running on other macOS hosts within a network. The Bonjour mDNSResponder daemon automatically registers and advertises a host’s registered services on the network. For example, adversaries can use a mDNS query (such as dns-sd -B _ssh._tcp . ) to find other systems broadcasting the ssh service. [2] [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries utilized Ping, the Advanced Port Scanner and Advanced IP Scanner to enumerate network devices. [4] |
| G1030 | Agrius | Agrius used the open-source port scanner WinEggDrop to perform detailed scans of hosts of interest in victim networks. [5] |
| C0062 | Anthropic AI-orchestrated Campaign | During the Anthropic AI-orchestrated Campaign , the adversary used Claude Code to enumerate internal network services and endpoints across targeted environments using browser automation via MCP, including databases, container registries, admin interfaces, and workflow orchestration platforms. [6] |
| G0050 | APT32 | APT32 performed network scanning on the network to search for open ports, services, OS finger-printing, and other vulnerabilities. [7] |
| G0087 | APT39 | APT39 has used CrackMapExec and a custom port scanner known as BLUETORCH for network scanning. [8] [9] |
| G0096 | APT41 | APT41 used a malware variant called WIDETONE to conduct port scans on specified subnets. [10] |
| S0093 | Backdoor.Oldrea | Backdoor.Oldrea can use a network scanning module to identify ICS-related ports. [11] |
| G0135 | BackdoorDiplomacy | BackdoorDiplomacy has used SMBTouch, a vulnerability scanner, to determine whether a target is vulnerable to EternalBlue malware. [12] |
| S1081 | BADHATCH | BADHATCH can check for open ports on a computer by establishing a TCP connection. [13] |
| G1043 | BlackByte | BlackByte has used tools such as NetScan to enumerate network services in victim environments. [14] |
| S1180 | BlackByte Ransomware | BlackByte Ransomware identifies remote systems via active directory queries for hostnames prior to launching remote ransomware payloads. [15] |
| S0089 | BlackEnergy | BlackEnergy has conducted port scans on a host. [16] |
| G0098 | BlackTech | BlackTech has used the SNScan tool to find other potential targets on victim networks. [17] |
| S1063 | Brute Ratel C4 | Brute Ratel C4 can conduct port scanning against targeted systems. [18] |
| C0018 | C0018 | During C0018 , the threat actors used the SoftPerfect Network Scanner for network scanning. [19] |
| C0027 | C0027 | During C0027 , used RustScan to scan for open ports on targeted ESXi appliances. [20] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell has a module to use a port scanner on a system. [21] |
| G0114 | Chimera | Chimera has used the get -b -e -p command for network scanning as well as a custom Python tool packed into a Windows executable named Get.exe to scan IP ranges for HTTP. [22] |
| S0020 | China Chopper | China Chopper 's server component can spider authentication portals. [23] |
| G0080 | Cobalt Group | Cobalt Group leveraged an open-source tool called SoftPerfect Network Scanner to perform network scanning. [24] [25] [26] |
| S0154 | Cobalt Strike | Cobalt Strike can perform port scans from an infected host. [27] [28] [29] |
| S0608 | Conficker | Conficker scans for other machines to infect. [30] |
| C0004 | CostaRicto | During CostaRicto , the threat actors employed nmap and pscan to scan target environments. [31] |
| G0105 | DarkVishnya | DarkVishnya performed port scanning to obtain the list of active services. [32] |
| G1003 | Ember Bear | Ember Bear has used tools such as NMAP for remote system discovery and enumeration in victim environments. [33] |
| S0363 | Empire | Empire can perform port scans from an infected host. [34] |
| G1016 | FIN13 | FIN13 has utilized nmap for reconnaissance efforts. FIN13 has also scanned for internal MS-SQL servers in a compromised network. [35] [36] |
| G0037 | FIN6 | FIN6 used publicly available tools (including Microsoft's built-in SQL querying tool, osql.exe) to map the internal network and conduct reconnaissance against Active Directory, Structured Query Language (SQL) servers, and NetBIOS. [37] |
| G0117 | Fox Kitten | Fox Kitten has used tools including NMAP to conduct broad scanning to identify open ports. [38] [39] |
| S1144 | FRP | As part of load balancing FRP can set healthCheck.type = "tcp" or healthCheck.type = "http" to check service status on specific hosts with TCPing or an HTTP request. [40] |
| S0061 | HDoor | HDoor scans to identify open ports on the victim. [41] |
| S0698 | HermeticWizard | HermeticWizard has the ability to scan ports on a compromised network. [42] |
| S0601 | Hildegard | Hildegard has used masscan to look for kubelets in the internal Kubernetes network. [43] |
| C0038 | HomeLand Justice | During HomeLand Justice , threat actors executed the Advanced Port Scanner tool on compromised systems. [44] [45] |
| G1032 | INC Ransom | INC Ransom has used NETSCAN.EXE for internal reconnaissance. [46] [47] |
| S0604 | Industroyer | Industroyer uses a custom port scanner to map out a network. [48] |
| S0260 | InvisiMole | InvisiMole can scan the network for open ports and vulnerable instances of RDP and SMB protocols. [49] |
| S0250 | Koadic | Koadic can scan for open TCP ports on the target network. [50] |
| G0032 | Lazarus Group | Lazarus Group has used nmap from a router VM to scan ports on systems within the restricted segment of an enterprise network. [51] |
| G0077 | Leafminer | Leafminer scanned network services to search for vulnerabilities in the victim system. [52] |
| S1185 | LightSpy | To collect data on the host's Wi-Fi connection history, LightSpy reads the /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist file .It also utilizes Apple's CWWiFiClient API to scan for nearby Wi-Fi networks and obtain data on the SSID, security type, and RSSI (signal strength) values. [53] |
| G0030 | Lotus Blossom | Lotus Blossom has used port scanners to enumerate services on remote hosts. [54] |
| S0532 | Lucifer | Lucifer can scan for open ports including TCP ports 135 and 1433. [55] |
| G0059 | Magic Hound | Magic Hound has used KPortScan 3.0 to perform SMB, RDP, and LDAP scanning. [56] |
| G1051 | Medusa Group | Medusa Group has the capability to use living off the land (LOTL) binaries to perform network enumeration. [57] Medusa Group has also utilized the publicly available scanning tool SoftPerfect Network Scanner ( netscan.exe ) to discover device hostnames and network services. [58] |
| G0045 | menuPass | menuPass has used tcping.exe, similar to Ping , to probe port status on systems of interest. [59] |
| S1146 | MgBot | MgBot includes modules for performing HTTP and server service scans. [60] |
| S0233 | MURKYTOP | MURKYTOP has the capability to scan for open ports on hosts in a connected network. [23] |
| G0129 | Mustang Panda | Mustang Panda has leveraged NBTscan to scan IP networks. [61] |
| G0019 | Naikon | Naikon has used the LadonGo scanner to scan target networks. [62] |
| S0590 | NBTscan | NBTscan can be used to scan IP networks. [63] [64] |
| G0049 | OilRig | OilRig has used the publicly available tool SoftPerfect Network Scanner as well as a custom tool called GOLDIRONY to conduct network scanning. [65] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors scanned for open ports and used nbtscan to find NETBIOS nameservers. [66] |
| S0598 | P.A.S. Webshell | P.A.S. Webshell can scan networks for open ports and listening services. [67] |
| S0683 | Peirates | Peirates can initiate a port scan against a given IP address. [68] |
| S0378 | PoshC2 | PoshC2 can perform port scans from an infected host. [69] |
| S0192 | Pupy | Pupy has a built-in module for port scanning. [70] |
| S0583 | Pysa | Pysa can perform network reconnaissance using the Advanced Port Scanner tool. [71] |
| S0458 | Ramsay | Ramsay can scan for systems that are vulnerable to the EternalBlue exploit. [72] [73] |
| G1039 | RedCurl | RedCurl has used netstat to check if port 4119 is open. [74] |
| S0125 | Remsec | Remsec has a plugin that can perform ARP scanning as well as port scanning. [75] |
| G0106 | Rocke | Rocke conducted scanning for exposed TCP port 7001 as well as SSH and Redis servers. [76] [77] |
| S1073 | Royal | Royal can scan the network interfaces of targeted systems. [78] |
| S0692 | SILENTTRINITY | SILENTTRINITY can scan for open ports on a compromised machine. [79] |
| S0374 | SpeakUp | SpeakUp checks for availability of specific ports on servers. [80] |
| G0039 | Suckfly | Suckfly the victim's internal network for hosts with ports 8080, 5900, and 40 open. [81] |
| G0139 | TeamTNT | TeamTNT has used masscan to search for open Docker API ports and Kubernetes clusters. [82] [43] [83] TeamTNT has also used malware that utilizes zmap and zgrab to search for vulnerable services in cloud environments. [84] |
| G0027 | Threat Group-3390 | Threat Group-3390 actors use the Hunter tool to conduct network service discovery for vulnerable systems. [85] [86] |
| G0081 | Tropic Trooper | Tropic Trooper used pr and an openly available tool to scan for open ports on target systems. [87] [88] |
| G1017 | Volt Typhoon | Volt Typhoon has used commercial tools, LOTL utilities, and appliances already present on the system for network service discovery. [89] |
| S0341 | Xbash | Xbash can perform port scanning of TCP and UDP ports. [90] |
| S0117 | XTunnel | XTunnel is capable of probing the network for open ports. [91] |
| S0412 | ZxShell | ZxShell can launch port scans. [10] [92] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1042 | Disable or Remove Feature or Program | Ensure that unnecessary ports and services are closed to prevent risk of discovery and potential exploitation. |
| M1031 | Network Intrusion Prevention | Use network intrusion detection/prevention systems to detect and prevent remote service scans. |
| M1030 | Network Segmentation | Ensure proper network segmentation is followed to protect critical servers and devices. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0376 | Behavioral Detection Strategy for Network Service Discovery Across Platforms | AN1057 | Detects processes performing network enumeration (e.g., port scans, service probing) by correlating process creation, socket connections, and sequential destination IP probing within a time window. |
| AN1058 | Detects use of network scanning utilities or scripts performing rapid connections to multiple services or hosts using auditd and netflow/pcap telemetry. |  |  |
| AN1059 | Detects Bonjour-based mDNS enumeration or use of system tools (e.g., dns-sd, nmap) to find active services via multicast probing or targeted scans. |  |  |
| AN1060 | Detects lateral discovery or container breakout attempts using netcat, curl, or custom binaries probing other services within the same namespace or VPC subnet. |  |  |

---

## References

- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [Apple Inc. (2013, April 23). Bonjour Overview. Retrieved October 11, 2021.](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Introduction.html)
- [Jaron Bradley. (2021, November 14). What does APT Activity Look Like on macOS?. Retrieved January 19, 2022.](https://themittenmac.com/what-does-apt-activity-look-like-on-macos/)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [Anthropic. (2025, November). Disrupting the first reported AI-orchestrated cyber espionage campaign. Retrieved April 20, 2026.](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.](https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html)
- [Rusu, B. (2020, May 21). Iranian Chafer APT Targeted Air Transportation and Government in Kuwait and Saudi Arabia. Retrieved May 22, 2020.](https://www.bitdefender.com/blog/labs/iranian-chafer-apt-targeted-air-transportation-and-government-in-kuwait-and-saudi-arabia/)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [Slowik, J. (2021, October). THE BAFFLING BERSERK BEAR: A DECADE’S ACTIVITY TARGETING CRITICAL INFRASTRUCTURE. Retrieved December 6, 2021.](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
- [Adam Burgher. (2021, June 10). BackdoorDiplomacy: Upgrading from Quarian to Turian. Retrieved September 1, 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [Baumgartner, K. and Garnaeva, M.. (2014, November 3). BE2 custom plugins, router abuse, and target profiles. Retrieved March 24, 2016.](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
- [Threat Intelligence. (2020, September 29). Palmerworm: Espionage Gang Targets the Media, Finance, and Other Sectors. Retrieved March 25, 2022.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/palmerworm-blacktech-espionage-apt)
- [Harbison, M. and Renals, P. (2022, July 5). When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors. Retrieved February 1, 2023.](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
- [Venere, G. Neal, C. (2022, June 21). Avos ransomware group expands with new attack arsenal. Retrieved January 11, 2023.](https://blog.talosintelligence.com/avoslocker-new-arsenal/)
- [Parisi, T. (2022, December 2). Not a SIMulation: CrowdStrike Investigations Reveal Intrusion Campaign Targeting Telco and BPO Companies. Retrieved June 30, 2023.](https://www.crowdstrike.com/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [Positive Technologies. (2017, August 16). Cobalt Strikes Back: An Evolving Multinational Threat to Finance. Retrieved September 5, 2018.](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-2017-eng.pdf)
- [Positive Technologies. (2016, December 16). Cobalt Snatch. Retrieved October 9, 2018.](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-Snatch-eng.pdf)
- [Matveeva, V. (2017, August 15). Secrets of Cobalt. Retrieved October 10, 2018.](https://www.group-ib.com/blog/cobalt)
- [Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
- [Mavis, N. (2020, September 21). The Art and Science of Detecting Cobalt Strike. Retrieved September 12, 2024.](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Burton, K. (n.d.). The Conficker Worm. Retrieved February 18, 2021.](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [Golovanov, S. (2018, December 6). DarkVishnya: Banks attacked through direct connection to local network. Retrieved May 15, 2020.](https://securelist.com/darkvishnya/89169/)
- [US Cybersecurity & Infrastructure Security Agency et al. (2024, September 5). Russian Military Cyber Actors Target U.S. and Global Critical Infrastructure. Retrieved September 6, 2024.](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [Sygnia Incident Response Team. (2022, January 5). TG2003: ELEPHANT BEETLE UNCOVERING AN ORGANIZED FINANCIAL-THEFT OPERATION. Retrieved February 9, 2023.](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)
- [FireEye Threat Intelligence. (2016, April). Follow the Money: Dissecting the Operations of the Cyber Crime Group FIN6. Retrieved November 17, 2024.](https://web.archive.org/web/20190807112824/https://www2.fireeye.com/rs/848-DID-242/images/rpt-fin6.pdf)
- [CISA. (2020, September 15). Iran-Based Threat Actor Exploits VPN Vulnerabilities. Retrieved December 21, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)
- [ClearSky. (2020, December 17). Pay2Key Ransomware – A New Campaign by Fox Kitten. Retrieved December 21, 2020.](https://www.clearskysec.com/wp-content/uploads/2020/12/Pay2Kitten.pdf)
- [fatedier. (n.d.). What is frp?. Retrieved July 10, 2024.](https://github.com/fatedier/frp)
- [Baumgartner, K., Golovkin, M.. (2015, May). The MsnMM Campaigns: The Earliest Naikon APT Campaigns. Retrieved April 10, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
- [ESET. (2022, March 1). IsaacWiper and HermeticWizard: New wiper and worm targetingUkraine. Retrieved April 10, 2022.](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
- [Chen, J. et al. (2021, February 3). Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes. Retrieved April 5, 2021.](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [CISA. (2022, September 23). AA22-264A Iranian State Actors Conduct Cyber Operations Against the Government of Albania. Retrieved August 6, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
- [MSTIC. (2022, September 8). Microsoft investigates Iranian attacks against the Albanian government. Retrieved August 6, 2024.](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)
- [SOCRadar. (2024, January 24). Dark Web Profile: INC Ransom. Retrieved June 5, 2024.](https://socradar.io/dark-web-profile-inc-ransom/)
- [SentinelOne. (n.d.). What Is Inc. Ransomware?. Retrieved June 5, 2024.](https://www.sentinelone.com/anthology/inc-ransom/)
- [Anton Cherepanov. (2017, June 12). Win32/Industroyer: A new threat for industrial controls systems. Retrieved December 18, 2020.](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Magius, J., et al. (2017, July 19). Koadic. Retrieved September 27, 2024.](https://github.com/offsecginger/koadic)
- [Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle. Retrieved October 27, 2021.](https://securelist.com/lazarus-threatneedle/100803/)
- [Symantec Security Response. (2018, July 25). Leafminer: New Espionage Campaigns Targeting Middle Eastern Regions. Retrieved August 28, 2018.](https://www.symantec.com/blogs/threat-intelligence/leafminer-espionage-middle-east)
- [Stuart Ashenbrenner, Alden Schmidt. (2024, April 25). LightSpy Malware Variant Targeting macOS. Retrieved January 3, 2025.](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
- [Symntec Threat Hunter Team. (2022, November 12). Billbug: State-sponsored Actor Targets Cert Authority, Government Agencies in Multiple Asian Countries. Retrieved March 15, 2025.](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
- [Hsu, K. et al. (2020, June 24). Lucifer: New Cryptojacking and DDoS Hybrid Malware Exploiting High and Critical Vulnerabilities to Infect Windows Devices. Retrieved November 16, 2020.](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [Threat Hunter Team. (2023, April 20). Daggerfly: APT Actor Targets Telecoms Company in Africa. Retrieved July 25, 2024.](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
- [Lior Rochberger, Tom Fakterman, Robert Falcone. (2023, September 22). Cyberespionage Attacks Against Southeast Asian Government Linked to Stately Taurus, Aka Mustang Panda. Retrieved September 9, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)
- [Vrabie, V. (2021, April 23). NAIKON – Traces from a Military Cyber-Espionage Operation. Retrieved June 29, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
- [Bezroutchko, A. (2019, November 19). NBTscan man page. Retrieved March 17, 2021.](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)
- [SecTools. (2003, June 11). NBTscan. Retrieved March 17, 2021.](https://sectools.org/tool/nbtscan/)
- [Davis, S. and Caban, D. (2017, December 19). APT34 - New Targeted Attack in the Middle East. Retrieved December 20, 2017.](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [ANSSI. (2021, January 27). SANDWORM INTRUSION SET CAMPAIGN TARGETING CENTREON SYSTEMS. Retrieved March 30, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
- [InGuardians. (2022, January 5). Peirates GitHub. Retrieved February 8, 2022.](https://github.com/inguardians/peirates)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [Nicolas Verdier. (n.d.). Retrieved January 29, 2018.](https://github.com/n1nj4sec/pupy)
- [CERT-FR. (2020, April 1). ATTACKS INVOLVING THE MESPINOZA/PYSA RANSOMWARE. Retrieved March 1, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Antiy CERT. (2020, April 20). Analysis of Ramsay components of Darkhotel's infiltration and isolation network. Retrieved March 24, 2021.](https://www.programmersought.com/article/62493896999/)
- [Tancio et al. (2024, March 6). Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence. Retrieved August 9, 2024.](https://www.trendmicro.com/en_us/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
- [Liebenberg, D.. (2018, August 30). Rocke: The Champion of Monero Miners. Retrieved May 26, 2020.](https://blog.talosintelligence.com/2018/08/rocke-champion-of-monero-miners.html)
- [Anomali Labs. (2019, March 15). Rocke Evolves Its Arsenal With a New Malware Family Written in Golang. Retrieved April 24, 2019.](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)
- [Cybereason Global SOC and Cybereason Security Research Teams. (2022, December 14). Royal Rumble: Analysis of Royal Ransomware. Retrieved March 30, 2023.](https://www.cybereason.com/blog/royal-ransomware-analysis)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [Check Point Research. (2019, February 4). SpeakUp: A New Undetected Backdoor Linux Trojan. Retrieved April 17, 2019.](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
- [DiMaggio, J. (2016, May 17). Indian organizations targeted in Suckfly attacks. Retrieved August 3, 2016.](http://www.symantec.com/connect/blogs/indian-organizations-targeted-suckfly-attacks)
- [Cado Security. (2020, August 16). Team TNT – The First Crypto-Mining Worm to Steal AWS Credentials. Retrieved September 22, 2021.](https://www.cadosecurity.com/team-tnt-the-first-crypto-mining-worm-to-steal-aws-credentials/)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Quist, N. (2020, October 5). Black-T: New Cryptojacking Variant from TeamTNT. Retrieved September 22, 2021.](https://unit42.paloaltonetworks.com/black-t-cryptojacking-variant/)
- [Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)
- [Falcone, R. and Lancaster, T. (2019, May 28). Emissary Panda Attacks Middle East Government Sharepoint Servers. Retrieved July 9, 2019.](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)
- [Alintanahin, K. (2015). Operation Tropic Trooper: Relying on Tried-and-Tested Flaws to Infiltrate Secret Keepers. Retrieved June 14, 2019.](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Xiao, C. (2018, September 17). Xbash Combines Botnet, Ransomware, Coinmining in Worm that Targets Linux and Windows. Retrieved November 14, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-xbash-combines-botnet-ransomware-coinmining-worm-targets-linux-windows/)
- [Belcher, P.. (2016, July 28). Tunnel of Gov: DNC Hack and the Russian XTunnel. Retrieved August 3, 2016.](https://www.invincea.com/2016/07/tunnel-of-gov-dnc-hack-and-the-russian-xtunnel/)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)

---


### 🔗 KRAB Intelligence Correlation
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025 Multi-Industry Hypervisor and Retail Extortion Campaign]] [related_campaign:: [[2025 Multi-Industry Hypervisor and Retail Extortion Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025-2026 SaaS Identity Crisis and Help Desk Exploitation Wave]] [related_campaign:: [[2025-2026 SaaS Identity Crisis and Help Desk Exploitation Wave]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2026 Enterprise LMS and Canvas Data Extortion Campaign]] [related_campaign:: [[2026 Enterprise LMS and Canvas Data Extortion Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2026 Oracle PeopleSoft Mass Data Theft Campaign]] [related_campaign:: [[2026 Oracle PeopleSoft Mass Data Theft Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[MGM Resorts and Caesars Entertainment Extortion Campaign]] [related_campaign:: [[MGM Resorts and Caesars Entertainment Extortion Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[Salesforce Massive Corporate Extortion Wave]] [related_campaign:: [[Salesforce Massive Corporate Extortion Wave]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Scattered Lapsus$ Hunters]] [related_actor:: [[Scattered Lapsus$ Hunters]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[RansomHub]] [related_actor:: [[RansomHub]]]

# Remote System Discovery

## Description

Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for Lateral Movement from the current system. Functionality could exist within remote access tools to enable this, but utilities available on the operating system could also be used such as Ping , net view using Net , or, on ESXi servers, esxcli network diag ping .

Adversaries may also analyze data from local host files (ex: C:\Windows\System32\Drivers\etc\hosts or /etc/hosts ) or other passive means (such as local Arp cache entries) in order to discover the presence of remote systems in an environment.

Adversaries may also target discovery of network infrastructure as well as leverage Network Device CLI commands on network devices to gather detailed information about systems within a network (e.g. show cdp neighbors , show arp ). [1] [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0028 | 2015 Ukraine Electric Power Attack | During the 2015 Ukraine Electric Power Attack , Sandworm Team remotely discovered systems over LAN connections. OT systems were visible from the IT network as well, giving adversaries the ability to discover operational assets. [3] |
| C0025 | 2016 Ukraine Electric Power Attack | During the 2016 Ukraine Electric Power Attack , Sandworm Team checked for connectivity to resources within the network and used LDAP to query Active Directory, discovering information about computers listed in AD. [4] |
| S0552 | AdFind | AdFind has the ability to query Active Directory for computers. [5] [6] [7] [8] |
| G1030 | Agrius | Agrius used the tool NBTscan to scan for remote, accessible hosts in victim environments. [9] |
| G1024 | Akira | Akira uses software such as Advanced IP Scanner and MASSCAN to identify remote hosts within victim networks. [10] |
| G0022 | APT3 | APT3 has a tool that can detect the existence of remote systems. [11] [12] |
| G0050 | APT32 | APT32 has enumerated DC servers using the command net group "Domain Controllers" /domain . The group has also used the ping command. [13] |
| G0087 | APT39 | APT39 has used NBTscan and custom tools to discover remote systems. [14] [15] [16] |
| G0096 | APT41 | APT41 has used MiPing to discover active systems in the victim network. [17] |
| S0099 | Arp | Arp can be used to display a host's ARP cache, which may include address resolutions for remote systems. [18] [19] |
| S0093 | Backdoor.Oldrea | Backdoor.Oldrea can enumerate and map ICS-specific systems in victim environments. [20] |
| S1081 | BADHATCH | BADHATCH can use a PowerShell object such as, System.Net.NetworkInformation.Ping to ping a computer. [21] |
| S0534 | Bazar | Bazar can enumerate remote systems using Net View . [22] |
| S0570 | BitPaymer | BitPaymer can use net view to discover remote systems. [23] |
| S1070 | Black Basta | Black Basta can use LDAP queries to connect to AD and iterate over connected workstations. [24] |
| G1043 | BlackByte | BlackByte used tools such as Arp to identify remotely-connected devices. [25] [26] |
| S1068 | BlackCat | BlackCat can broadcasts NetBIOS Name Service (NBNC) messages to search for servers connected to compromised networks. [27] |
| S0521 | BloodHound | BloodHound can enumerate and collect the properties of domain computers, including domain controllers. [28] |
| G0060 | BRONZE BUTLER | BRONZE BUTLER typically use ping and Net to enumerate systems. [29] |
| C0015 | C0015 | During C0015 , the threat actors used the commands net view /all /domain and ping to discover remote systems. They also used PowerView's PowerShell Invoke-ShareFinder script for file share enumeration. [30] |
| S0335 | Carbon | Carbon uses the net view command. [31] |
| G0114 | Chimera | Chimera has utilized various scans and queries to find domain controllers and remote services in the target environment. [32] |
| S0154 | Cobalt Strike | Cobalt Strike uses the native Windows Network Enumeration APIs to interrogate and discover targets in a Windows Active Directory network. [33] [34] [35] |
| S0244 | Comnie | Comnie runs the net view command |
| S0575 | Conti | Conti has the ability to discover hosts on a target network. [36] |
| S0488 | CrackMapExec | CrackMapExec can discover active IP addresses, along with the machine name, within a targeted network. [37] |
| G0009 | Deep Panda | Deep Panda has used ping to identify other machines of interest. [38] |
| S0659 | Diavol | Diavol can use the ARP table to find remote hosts to scan. [39] |
| G0035 | Dragonfly | Dragonfly has likely obtained a list of hosts in the victim environment. [40] |
| S0694 | DRATzarus | DRATzarus can search for other machines connected to compromised host and attempt to map the network. [41] |
| S1159 | DUSTTRAP | DUSTTRAP can use ping to identify remote hosts within the victim network. [42] |
| G1006 | Earth Lusca | Earth Lusca used the command powershell "Get-EventLog -LogName security -Newest 500 | where {$_.EventID -eq 4624} | format-list - property * | findstr "Address"" to find the network information of successfully logged-in accounts to discovery addresses of other machines. Earth Lusca has also used multiple scanning tools to discover other machines within the same compromised network. [43] |
| G1003 | Ember Bear | Ember Bear has used tools such as Nmap and MASSCAN for remote service discovery. [44] |
| S0091 | Epic | Epic uses the net view command on the victim’s machine. [45] |
| G0053 | FIN5 | FIN5 has used the open source tool Essential NetTools to map the network and build a list of targets. [46] |
| G0037 | FIN6 | FIN6 used publicly available tools (including Microsoft's built-in SQL querying tool, osql.exe) to map the internal network and conduct reconnaissance against Active Directory, Structured Query Language (SQL) servers, and NetBIOS. [47] |
| G0061 | FIN8 | FIN8 has used dsquery and other Active Directory utilities to enumerate hosts; they have also used nltest.exe /dclist to retrieve a list of domain controllers. [48] [49] |
| S0696 | Flagpro | Flagpro has been used to execute net view on a targeted system. [50] |
| G0117 | Fox Kitten | Fox Kitten has used Angry IP Scanner to detect remote systems. [51] |
| S1044 | FunnyDream | FunnyDream can collect information about hosts on the victim network. [52] |
| C0007 | FunnyDream | During FunnyDream , the threat actors used several tools and batch files to map victims' internal networks. [53] |
| G0093 | GALLIUM | GALLIUM used a modified version of NBTscan to identify available NetBIOS name servers over the network as well as ping to identify remote systems. [54] |
| S1198 | Gomir | Gomir probes arbitrary network endpoints for TCP connectivity. [55] |
| G0125 | HAFNIUM | HAFNIUM has enumerated domain controllers using net group "Domain computers" and nltest /dclist . [56] |
| S1229 | Havoc | Havoc features a module capable of host enumeration. [57] |
| S0698 | HermeticWizard | HermeticWizard can find machines on the local network by gathering known local IP addresses through DNSGetCacheDataTable , GetIpNetTable , WNetOpenEnumW(RESOURCE_GLOBALNET, RESOURCETYPE_ANY) , NetServerEnum , GetTcpTable , and GetAdaptersAddresses. [58] |
| G1001 | HEXANE | HEXANE has used net view to enumerate domain machines. [59] |
| G0119 | Indrik Spider | Indrik Spider has used PowerView to enumerate all Windows Server, Windows Server 2003, and Windows 7 instances in the Active Directory database. [60] |
| S0604 | Industroyer | Industroyer can enumerate remote computers in the compromised network. [61] |
| G0004 | Ke3chang | Ke3chang has used network scanning and enumeration tools, including Ping . [62] |
| S0599 | Kinsing | Kinsing has used a script to parse files like /etc/hosts and SSH known_hosts to discover remote systems. [63] |
| S0236 | Kwampirs | Kwampirs collects a list of available servers with the command net view . [64] |
| G0077 | Leafminer | Leafminer used Microsoft’s Sysinternals tools to gather detailed information about remote systems. [65] |
| C0049 | Leviathan Australian Intrusions | Leviathan performed extensive remote host enumeration to build their own map of victim networks during Leviathan Australian Intrusions . [66] |
| S9020 | LODEINFO | LODEINFO can run net view and net view /domain for network discovery. [67] |
| G0030 | Lotus Blossom | Lotus Blossom has used Ping to identify remote systems. [68] |
| G0059 | Magic Hound | Magic Hound has used Ping for discovery on targeted networks. [69] |
| G1051 | Medusa Group | Medusa Group has used PDQ Inventory to get an inventory of the endpoints on the network. [70] |
| G0045 | menuPass | menuPass uses scripts to enumerate IP ranges on the victim network. menuPass has also issued the command net view /domain to a PlugX implant to gather information about remote systems on the network. [71] [72] |
| S1146 | MgBot | MgBot includes modules for performing ARP scans of local connected systems. [73] |
| G1054 | MirrorFace | MirrorFace has used Ping for system discovery. [74] |
| S0233 | MURKYTOP | MURKYTOP has the capability to identify remote hosts on connected networks. [75] |
| G0129 | Mustang Panda | Mustang Panda has queried Active Directory for computers using AdFind . [76] Mustang Panda has also utilized SharpNBTScan to scan the victim environment. [77] |
| G0019 | Naikon | Naikon has used a netbios scanner for remote machine identification. [78] |
| S0590 | NBTscan | NBTscan can list NetBIOS computer names. [79] [80] |
| S0039 | Net | Commands such as net view can be used in Net to gather information about available remote systems. [81] |
| S0385 | njRAT | njRAT can identify remote hosts on connected networks. [82] |
| S0359 | Nltest | Nltest may be used to enumerate remote domain controllers using options such as /dclist and /dsgetdc . [83] |
| S0365 | Olympic Destroyer | Olympic Destroyer uses Windows Management Instrumentation to enumerate all systems in the network. [84] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors used the net view and ping commands as part of their advanced reconnaissance. [85] |
| C0061 | Operation Digital Eye | During Operation Digital Eye , threat actors used Ping for reconnaissance. [86] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors used nbtscan and ping to discover remote systems, as well as dsquery subnet on a domain controller to retrieve all subnets in the Active Directory. [87] |
| S0165 | OSInfo | OSInfo performs a connection test to discover remote systems in the network [11] |
| S0097 | Ping | Ping can be used to identify remote systems within a network. [88] |
| G1040 | Play | Play has used tools such as AdFind , Nltest , and BloodHound to enumerate shares and hostnames on compromised networks. [89] |
| S0428 | PoetRAT | PoetRAT used Nmap for remote system discovery. [90] |
| S0650 | QakBot | QakBot can identify remote systems through the net view command. [91] [92] [93] |
| S1242 | Qilin | Qilin can enumerate domain-connected hosts during its discovery phase. [94] [95] [96] |
| S1212 | RansomHub | RansomHub can enumerate all accessible machines from the infected system. [97] |
| S0241 | RATANKBA | RATANKBA runs the net view /domain and net view commands. [98] |
| S0125 | Remsec | Remsec can ping or traceroute a remote host. [99] |
| S0684 | ROADTools | ROADTools can enumerate Azure AD systems and devices. [100] |
| G0106 | Rocke | Rocke has looked for IP addresses in the known_hosts file on the infected system and attempted to SSH into them. [101] |
| G0034 | Sandworm Team | Sandworm Team has used a tool to query Active Directory using LDAP, discovering information about computers listed in AD. [102] [4] |
| G1015 | Scattered Spider | Scattered Spider can enumerate remote systems, such as VMware vCenter infrastructure. [103] |
| S0140 | Shamoon | Shamoon scans the C-class subnet of the IPs on the victim's interfaces. [104] |
| S0063 | SHOTPUT | SHOTPUT has a command to list all servers in the domain, as well as one to locate domain controllers on a domain. [105] |
| G0091 | Silence | Silence has used Nmap to scan the corporate network, build a network topology, and identify vulnerable hosts. [106] |
| S0692 | SILENTTRINITY | SILENTTRINITY can enumerate and collect the properties of domain computers. [107] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 used AdFind to enumerate remote systems. [108] |
| S0646 | SpicyOmelette | SpicyOmelette can identify payment systems, payment gateways, and ATM systems in compromised environments. [109] |
| S0018 | Sykipot | Sykipot may use net view /domain to display hostnames of available systems on a network. [110] |
| S0586 | TAINTEDSCRIBE | The TAINTEDSCRIBE command and execution module can perform target system enumeration. [111] |
| G0027 | Threat Group-3390 | Threat Group-3390 has used the net view command. [112] |
| G1022 | ToddyCat | ToddyCat has used ping %REMOTE_HOST% for post exploit discovery. [113] |
| S0266 | TrickBot | TrickBot can enumerate computers and network devices. [114] |
| G0010 | Turla | Turla surveys a system upon check-in to discover remote systems on a local network using the net view and net view /DOMAIN commands. Turla has also used net group "Domain Computers" /domain , net group "Domain Controllers" /domain , and net group "Exchange Servers" /domain to enumerate domain computers, including the organization's DC and Exchange Server. [45] [115] |
| S0452 | USBferry | USBferry can use net view to gather information about remote systems. [116] |
| G1017 | Volt Typhoon | Volt Typhoon has used multiple methods, including Ping , to enumerate systems on compromised networks. [117] [118] |
| S0366 | WannaCry | WannaCry scans its local network segment for remote systems to try to exploit and copy itself to. [119] |
| G0102 | Wizard Spider | Wizard Spider has used networkdll for network discovery and psfin specifically for financial and point of sale indicators. Wizard Spider has also used AdFind , nltest/dclist , and PowerShell script Get-DataInfo.ps1 to enumerate domain computers, including the domain controller. [7] [120] [121] [5] [122] [123] |
| S0248 | yty | yty uses the net view command for discovery. [124] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0574 | Detection Strategy for Remote System Enumeration Behavior | AN1583 | Execution of network enumeration utilities (e.g., net.exe, ping.exe, tracert.exe) in short succession, often chained with lateral movement tools or system enumeration commands. |
| AN1584 | Use of bash scripts or interactive shells to issue sequential ping, arp, or traceroute commands to map remote hosts. |  |  |
| AN1585 | Execution of built-in or AppleScript-based system enumeration via arp , netstat , ping , and discovery of /etc/hosts contents. |  |  |
| AN1586 | ESXi shell or SSH access issuing esxcli network diag ping or viewing routing tables to identify connected hosts. |  |  |
| AN1587 | Execution of discovery commands like show cdp neighbors , show arp , and other interface-level introspection on Cisco or Juniper devices. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0574 | Detection Strategy for Remote System Enumeration Behavior | AN1583 | Execution of network enumeration utilities (e.g., net.exe, ping.exe, tracert.exe) in short succession, often chained with lateral movement tools or system enumeration commands. |
| AN1584 | Use of bash scripts or interactive shells to issue sequential ping, arp, or traceroute commands to map remote hosts. |  |  |
| AN1585 | Execution of built-in or AppleScript-based system enumeration via arp , netstat , ping , and discovery of /etc/hosts contents. |  |  |
| AN1586 | ESXi shell or SSH access issuing esxcli network diag ping or viewing routing tables to identify connected hosts. |  |  |
| AN1587 | Execution of discovery commands like show cdp neighbors , show arp , and other interface-level introspection on Cisco or Juniper devices. |  |  |

---

## References

- [US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved October 19, 2020.](https://www.us-cert.gov/ncas/alerts/TA18-106A)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [Charles McLellan. (2016, March 4). How hackers attacked Ukraine's power grid: Implications for Industrial IoT security. Retrieved September 27, 2023.](https://www.zdnet.com/article/how-hackers-attacked-ukraines-power-grid-implications-for-industrial-iot-security/)
- [Joe Slowik. (2018, October 12). Anatomy of an Attack: Detecting and Defeating CRASHOVERRIDE. Retrieved December 18, 2020.](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)
- [Brian Donohue, Katie Nickels, Paul Michaud, Adina Bodkins, Taylor Chapman, Tony Lambert, Jeff Felling, Kyle Rainey, Mike Haag, Matt Graeber, Aaron Didier.. (2020, October 29). A Bazar start: How one hospital thwarted a Ryuk ransomware outbreak. Retrieved October 30, 2020.](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)
- [McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)
- [Goody, K., et al (2019, January 11). A Nasty Trick: From Credential Theft Malware to Business Disruption. Retrieved May 12, 2020.](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)
- [Cybereason. (2022, August 17). Bumblebee Loader – The High Road to Enterprise Domain Control. Retrieved August 29, 2022.](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [Steven Campbell, Akshay Suthar, & Connor Belfiorre. (2023, July 26). Conti and Akira: Chained Together. Retrieved February 20, 2024.](https://arcticwolf.com/resources/blog/conti-and-akira-chained-together/)
- [Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
- [Chen, X., Scott, M., Caselden, D.. (2014, April 26). New Zero-Day Exploit targeting Internet Explorer Versions 9 through 11 Identified in Targeted Attacks. Retrieved January 14, 2016.](https://www.fireeye.com/blog/threat-research/2014/04/new-zero-day-exploit-targeting-internet-explorer-versions-9-through-11-identified-in-targeted-attacks.html)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.](https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html)
- [Rusu, B. (2020, May 21). Iranian Chafer APT Targeted Air Transportation and Government in Kuwait and Saudi Arabia. Retrieved May 22, 2020.](https://www.bitdefender.com/blog/labs/iranian-chafer-apt-targeted-air-transportation-and-government-in-kuwait-and-saudi-arabia/)
- [Symantec. (2018, February 28). Chafer: Latest Attacks Reveal Heightened Ambitions. Retrieved May 22, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/chafer-latest-attacks-reveal-heightened-ambitions)
- [DCSO CyTec Blog. (2022, December 24). APT41 — The spy who failed to encrypt me. Retrieved June 13, 2024.](https://medium.com/@DCSO_CyTec/apt41-the-spy-who-failed-to-encrypt-me-24fc0f49cad1)
- [Microsoft. (n.d.). Arp. Retrieved April 17, 2016.](https://technet.microsoft.com/en-us/library/bb490864.aspx)
- [Palo Alto Networks. (2021, November 24). Cortex XDR Analytics Alert Reference: Uncommon ARP cache listing via arp.exe. Retrieved December 7, 2021.](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-analytics-alert-reference/cortex-xdr-analytics-alert-reference/uncommon-arp-cache-listing-via-arp-exe.html)
- [Slowik, J. (2021, October). THE BAFFLING BERSERK BEAR: A DECADE’S ACTIVITY TARGETING CRITICAL INFRASTRUCTURE. Retrieved December 6, 2021.](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Frankoff, S., Hartley, B. (2018, November 14). Big Game Hunting: The Evolution of INDRIK SPIDER From Dridex Wire Fraud to BitPaymer Targeted Ransomware. Retrieved January 6, 2021.](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
- [Check Point. (2022, October 20). BLACK BASTA AND THE UNNOTICED DELIVERY. Retrieved March 8, 2023.](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
- [US Federal Bureau of Investigation & US Secret Service. (2022, February 11). Indicators of Compromise Associated with BlackByte Ransomware. Retrieved December 16, 2024.](https://www.ic3.gov/CSA/2022/220211.pdf)
- [Huseyin Can Yuceel. (2022, February 21). TTPs used by BlackByte Ransomware Targeting Critical Infrastructure. Retrieved December 16, 2024.](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [Red Team Labs. (2018, April 24). Hidden Administrative Accounts: BloodHound to the Rescue. Retrieved October 28, 2020.](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)
- [Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [GovCERT. (2016, May 23). Technical Report about the Espionage Case at RUAG. Retrieved November 7, 2018.](https://web.archive.org/web/20170718174931/https://www.melani.admin.ch/dam/melani/de/dokumente/2016/technical%20report%20ruag.pdf.download.pdf/Report_Ruag-Espionage-Case.pdf)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
- [Mavis, N. (2020, September 21). The Art and Science of Detecting Cobalt Strike. Retrieved September 12, 2024.](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Podlosky, A., Hanel, A. et al. (2020, October 16). WIZARD SPIDER Update: Resilient, Reactive and Resolute. Retrieved June 15, 2021.](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)
- [byt3bl33d3r. (2018, September 8). SMB: Command Reference. Retrieved July 17, 2020.](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
- [Alperovitch, D. (2014, July 7). Deep in Thought: Chinese Targeting of National Security Think Tanks. Retrieved November 12, 2014.](https://web.archive.org/web/20200424075623/https:/www.crowdstrike.com/blog/deep-thought-chinese-targeting-national-security-think-tanks/)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Chen, J., et al. (2022). Delving Deep: An Analysis of Earth Lusca’s Operations. Retrieved July 1, 2022.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
- [US Cybersecurity & Infrastructure Security Agency et al. (2024, September 5). Russian Military Cyber Actors Target U.S. and Global Critical Infrastructure. Retrieved September 6, 2024.](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.](https://www.youtube.com/watch?v=fevGZs0EQu8)
- [FireEye Threat Intelligence. (2016, April). Follow the Money: Dissecting the Operations of the Cyber Crime Group FIN6. Retrieved November 17, 2024.](https://web.archive.org/web/20190807112824/https://www2.fireeye.com/rs/848-DID-242/images/rpt-fin6.pdf)
- [Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy: New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)
- [Martin Zugec. (2021, July 27). Deep Dive Into a FIN8 Attack - A Forensic Investigation. Retrieved September 1, 2021.](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [CISA. (2020, September 15). Iran-Based Threat Actor Exploits VPN Vulnerabilities. Retrieved December 21, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)
- [Global Research and Analysis Team. (2020, April 30). APT trends report Q1 2020. Retrieved September 19, 2022.](https://securelist.com/apt-trends-report-q1-2020/96826/)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Cybereason Nocturnus. (2019, June 25). Operation Soft Cell: A Worldwide Campaign Against Telecommunications Providers. Retrieved July 18, 2019.](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)
- [Symantec Threat Hunter Team. (2024, May 16). Springtail: New Linux Backdoor Added to Toolkit. Retrieved January 17, 2025.](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
- [Eoin Miller. (2021, March 23). Defending Against the Zero Day: Analyzing Attacker Behavior Post-Exploitation of Microsoft Exchange. Retrieved October 27, 2022.](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)
- [Ungur, P. (n.d.). HAVOC. Retrieved August 4, 2025.](https://havocframework.com/docs/welcome)
- [ESET. (2022, March 1). IsaacWiper and HermeticWizard: New wiper and worm targetingUkraine. Retrieved April 10, 2022.](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Symantec Threat Intelligence. (2020, June 25). WastedLocker: Symantec Identifies Wave of Attacks Against U.S. Organizations. Retrieved May 20, 2021.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)
- [Anton Cherepanov. (2017, June 12). Win32/Industroyer: A new threat for industrial controls systems. Retrieved December 18, 2020.](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
- [Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)
- [Singer, G. (2020, April 3). Threat Alert: Kinsing Malware Attacks Targeting Container Environments. Retrieved April 1, 2021.](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
- [Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
- [Symantec Security Response. (2018, July 25). Leafminer: New Espionage Campaigns Targeting Middle Eastern Regions. Retrieved August 28, 2018.](https://www.symantec.com/blogs/threat-intelligence/leafminer-espionage-middle-east)
- [CISA et al. (2024, July 8). People’s Republic of China (PRC) Ministry of State Security APT40 Tradecraft in Action. Retrieved February 3, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a)
- [Breitenbacher, D. (2022, December 14). Unmasking MirrorFace: Operation LiberalFace targeting Japanese political entities. Retrieved April 17, 2026.](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
- [Symntec Threat Hunter Team. (2022, November 12). Billbug: State-sponsored Actor Targets Cert Authority, Government Agencies in Multiple Asian Countries. Retrieved March 15, 2025.](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [FireEye iSIGHT Intelligence. (2017, April 6). APT10 (MenuPass Group): New Tools, Global Campaign Latest Manifestation of Longstanding Threat. Retrieved June 29, 2017.](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)
- [Threat Hunter Team. (2023, April 20). Daggerfly: APT Actor Targets Telecoms Company in Africa. Retrieved July 25, 2024.](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [Lior Rochberger, Tom Fakterman, Robert Falcone. (2023, September 22). Cyberespionage Attacks Against Southeast Asian Government Linked to Stately Taurus, Aka Mustang Panda. Retrieved September 9, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)
- [Tom Fakterman. (2024, September 6). Chinese APT Abuses VSCode to Target Government in Asia. Retrieved March 24, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage/)
- [Vrabie, V. (2021, April 23). NAIKON – Traces from a Military Cyber-Espionage Operation. Retrieved June 29, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
- [Bezroutchko, A. (2019, November 19). NBTscan man page. Retrieved March 17, 2021.](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)
- [SecTools. (2003, June 11). NBTscan. Retrieved March 17, 2021.](https://sectools.org/tool/nbtscan/)
- [Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)
- [Fidelis Cybersecurity. (2013, June 28). Fidelis Threat Advisory #1009: "njRAT" Uncovered. Retrieved June 4, 2019.](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
- [ss64. (n.d.). NLTEST.exe - Network Location Test. Retrieved February 14, 2019.](https://ss64.com/nt/nltest.html)
- [Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [Aleksandar Milenkoski, Luigi Martire. (2024, December 10). Operation Digital Eye | Chinese APT Compromises Critical Digital Infrastructure via Visual Studio Code Tunnels. Retrieved February 27, 2025.](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Microsoft. (n.d.). Ping. Retrieved April 8, 2016.](https://technet.microsoft.com/en-us/library/bb490968.aspx)
- [Trend Micro Research. (2023, July 21). Ransomware Spotlight: Play. Retrieved September 24, 2024.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
- [Mercer, W, et al. (2020, April 16). PoetRAT: Python RAT uses COVID-19 lures to target Azerbaijan public and private sectors. Retrieved April 27, 2020.](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
- [CS. (2020, October 7). Duck Hunting with Falcon Complete: A Fowl Banking Trojan Evolves, Part 2. Retrieved September 27, 2021.](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [Kenefick, I. et al. (2022, October 12). Black Basta Ransomware Gang Infiltrates Networks via QAKBOT, Brute Ratel, and Cobalt Strike. Retrieved February 6, 2023.](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
- [Hacioglu, S. (2025, March 10). Qilin Ransomware: Exposing the TTPs Behind One of the Most Active Ransomware Campaigns of 2024. Retrieved September 26, 2025.](https://www.picussecurity.com/resource/blog/qilin-ransomware)
- [Bradshaw, A. et al. (2025, April 1). Qilin affiliates spear-phish MSP ScreenConnect admin, targeting customers downstream. Retrieved September 26, 2025.](https://news.sophos.com/en-us/2025/04/01/sophos-mdr-tracks-ongoing-campaign-by-qilin-affiliates-targeting-screenconnect/)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [Alfano, V. et al. (2025, February 12). RansomHub Never Sleeps Episode 1: The evolution of modern ransomware. Retrieved March 17, 2025.](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
- [Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
- [Dirk-jan Mollema. (2020, April 16). Introducing ROADtools - The Azure AD exploration framework. Retrieved January 31, 2022.](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)
- [Liebenberg, D.. (2018, August 30). Rocke: The Champion of Monero Miners. Retrieved May 26, 2020.](https://blog.talosintelligence.com/2018/08/rocke-champion-of-monero-miners.html)
- [Cherepanov, A.. (2016, December 13). The rise of TeleBots: Analyzing disruptive KillDisk attacks. Retrieved June 10, 2020.](https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/)
- [CISA. (2023, November 16). Cybersecurity Advisory: Scattered Spider (AA23-320A). Retrieved March 18, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)
- [FireEye. (2016, November 30). FireEye Responds to Wave of Destructive Cyber Attacks in Gulf Region. Retrieved November 17, 2024.](https://web.archive.org/web/20210126065851/https://www.fireeye.com/blog/threat-research/2016/11/fireeye_respondsto.html)
- [Falcone, R. and Wartell, R.. (2015, July 27). Observations on CVE-2015-3113, Prior Zero-Days and the Pirpi Payload. Retrieved January 22, 2016.](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
- [Group-IB. (2018, September). Silence: Moving Into the Darkside. Retrieved May 5, 2020.](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [MSTIC, CDOC, 365 Defender Research Team. (2021, January 20). Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop . Retrieved January 22, 2021.](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
- [CTU. (2018, September 27). Cybercriminals Increasingly Trying to Ensnare the Big Financial Fish. Retrieved September 20, 2021.](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)
- [Blasco, J. (2011, December 12). Another Sykipot sample likely targeting US federal agencies. Retrieved March 28, 2016.](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)
- [USG. (2020, May 12). MAR-10288834-2.v1 – North Korean Trojan: TAINTEDSCRIBE. Retrieved March 5, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
- [Pantazopoulos, N., Henry T. (2018, May 18). Emissary Panda – A potential new malicious tool. Retrieved June 25, 2018.](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Microsoft Threat Intelligence. (2023, May 24). Volt Typhoon targets US critical infrastructure with living-off-the-land techniques. Retrieved July 27, 2023.](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)
- [Counter Threat Unit Research Team. (2023, May 24). Chinese Cyberespionage Group BRONZE SILHOUETTE Targets U.S. Government and Defense Organizations. Retrieved July 27, 2023.](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)
- [Counter Threat Unit Research Team. (2017, May 18). WCry Ransomware Analysis. Retrieved March 26, 2019.](https://www.secureworks.com/research/wcry-ransomware-analysis)
- [John, E. and Carvey, H. (2019, May 30). Unraveling the Spiderweb: Timelining ATT&CK Artifacts Used by GRIM SPIDER. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)
- [Kimberly Goody, Jeremy Kennelly, Joshua Shilko, Steve Elovitz, Douglas Bienstock. (2020, October 28). Unhappy Hour Special: KEGTAP and SINGLEMALT With a Ransomware Chaser. Retrieved October 28, 2020.](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)
- [The DFIR Report. (2020, October 8). Ryuk’s Return. Retrieved October 9, 2020.](https://thedfirreport.com/2020/10/08/ryuks-return/)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [Schwarz, D., Sopko J. (2018, March 08). Donot Team Leverages New Modular Malware Framework in South Asia. Retrieved June 11, 2018.](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)

---

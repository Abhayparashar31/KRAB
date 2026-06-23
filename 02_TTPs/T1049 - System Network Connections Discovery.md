# System Network Connections Discovery

## Description

Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently accessing or from remote systems by querying for information over the network.

An adversary who gains access to a system that is part of a cloud-based environment may map out Virtual Private Clouds or Virtual Networks in order to determine what systems and services are connected. The actions performed are likely the same types of discovery techniques depending on the operating system, but the resulting information may include details about the networked cloud environment relevant to the adversary's goals. Cloud providers may have different ways in which their virtual networks operate. [1] [2] [3] Similarly, adversaries who gain access to network devices may also perform similar discovery activities to gather information about connected systems and services.

Utilities and commands that acquire this information include netstat , "net use," and "net session" with Net . In Mac and Linux, netstat and lsof can be used to list current connections. who -a and w can be used to show which users are currently logged in, similar to "net session". Additionally, built-in features native to network devices and Network Device CLI may be used (e.g. show ip sockets , show tcp brief ). [4] On ESXi servers, the command esxi network ip connection list can be used to list active network connections. [5]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries identified network connections utilizing netstat -nao and netstat -r . [6] |
| G0018 | admin@338 | admin@338 actors used the following command following exploitation of a machine with LOWBALL malware to display network connections: netstat -ano >> %temp%\download [7] |
| G0138 | Andariel | Andariel has used the netstat -naop tcp command to display TCP connections on a victim's machine. [8] |
| C0062 | Anthropic AI-orchestrated Campaign | During the Anthropic AI-orchestrated Campaign , the adversary used Claude Code to map internal network architecture and access relationships. [9] |
| G0006 | APT1 | APT1 used the net use command to get a listing on network connections. [10] |
| G0022 | APT3 | APT3 has a tool that can enumerate current network connections. [11] [12] [13] |
| G0050 | APT32 | APT32 used the netstat -anpo tcp command to display TCP connections on the victim's machine. [14] |
| G0082 | APT38 | APT38 installed a port monitoring tool, MAPMAKER, to print the active TCP connections on the local system. [15] |
| G0096 | APT41 | APT41 has enumerated IP addresses of network resources and used the netstat command as part of network reconnaissance. The group has also used a malware variant, HIGHNOON, to enumerate active RDP sessions. [16] [17] |
| G1023 | APT5 | APT5 has used the BLOODMINE utility to collect data on web requests from Pulse Secure Connect logs. [18] |
| S0456 | Aria-body | Aria-body has the ability to gather TCP and UDP table status listings. [19] |
| S0638 | Babuk | Babuk can use "WNetOpenEnumW" and "WNetEnumResourceW" to enumerate files in network resources for encryption. [20] |
| G0135 | BackdoorDiplomacy | BackdoorDiplomacy has used NetCat and PortQry to enumerate network connections and display the status of related TCP and UDP ports. [21] |
| S1081 | BADHATCH | BADHATCH can execute netstat.exe -f on a compromised machine. [22] |
| S0089 | BlackEnergy | BlackEnergy has gathered information about local network connections using netstat . [23] [24] |
| S0335 | Carbon | Carbon uses the netstat -r and netstat -an commands. [25] |
| G0114 | Chimera | Chimera has used netstat -ano | findstr EST to discover network connections. [26] |
| S0154 | Cobalt Strike | Cobalt Strike can produce a sessions report from compromised hosts. [27] |
| S0244 | Comnie | Comnie executes the netstat -ano command. [28] |
| S0575 | Conti | Conti can enumerate routine network connections from a compromised host. [29] |
| S0488 | CrackMapExec | CrackMapExec can discover active sessions for a targeted system. [30] |
| S0625 | Cuba | Cuba can use the function GetIpNetTable to recover the last connections to the victim's machine. [31] |
| S0567 | Dtrack | Dtrack can collect network and active connection information. [32] |
| S0038 | Duqu | The discovery modules used with Duqu can collect information on network connections. [33] |
| G1006 | Earth Lusca | Earth Lusca employed a PowerShell script called RDPConnectionParser to read and filter the Windows event log "Microsoft-Windows-TerminalServices-RDPClient/Operational" (Event ID 1024) to obtain network information from RDP connections. Earth Lusca has also used netstat from a compromised system to obtain network connection information. [34] |
| S0554 | Egregor | Egregor can enumerate all connected drives. [35] |
| S0363 | Empire | Empire can enumerate the current network connections of a host. [36] |
| S0091 | Epic | Epic uses the net use , net session , and netstat commands to gather information on network connections. [37] [38] |
| G1016 | FIN13 | FIN13 has used netstat and other net commands for network reconnaissance efforts. [39] |
| S0696 | Flagpro | Flagpro has been used to execute netstat -ano on a compromised host. [40] |
| S1144 | FRP | FRP can use a dashboard and U/I to display the status of connections from the FRP client and server. [41] |
| C0007 | FunnyDream | During FunnyDream , the threat actors used netstat to discover network connections on remote systems. [42] |
| G0093 | GALLIUM | GALLIUM used netstat -oan to obtain information about the victim network connections. [43] |
| S0237 | GravityRAT | GravityRAT uses the netstat command to find open ports on the victim’s machine. [44] |
| G1001 | HEXANE | HEXANE has used netstat to monitor connections to specific ports. [45] |
| G1032 | INC Ransom | INC Ransom has used RDP to test network connections. [46] |
| S0283 | jRAT | jRAT can list network connections. [47] |
| G0004 | Ke3chang | Ke3chang performs local network connection discovery using netstat . [48] [49] |
| S0356 | KONNI | KONNI has used net session on the victim's machine. [50] |
| S1075 | KOPILUWAK | KOPILUWAK can use netstat , Arp , and Net to discover current TCP connections. [51] |
| S0236 | Kwampirs | Kwampirs collects a list of active and listening connections by using the command netstat -nao as well as a list of available network mappings with net use . [52] |
| G0032 | Lazarus Group | Lazarus Group has used net use to identify and establish a network connection with a remote host. [53] |
| S0681 | Lizar | Lizar has a plugin to retrieve information about all active network sessions on the infected server. [54] |
| G0030 | Lotus Blossom | Lotus Blossom has used commands such as netstat to identify system network connections. [55] |
| S0532 | Lucifer | Lucifer can identify the IP and port numbers for all remote connections from the compromised host. [56] |
| S1141 | LunarWeb | LunarWeb can enumerate system network connections. [57] |
| S1060 | Mafalda | Mafalda can use the GetExtendedTcpTable function to retrieve information about established TCP connections. [58] |
| G0059 | Magic Hound | Magic Hound has used quser.exe to identify existing RDP connections. [59] |
| S0449 | Maze | Maze has used the "WNetOpenEnumW", "WNetEnumResourceW", "WNetCloseEnum" and "WNetAddConnection2W" functions to enumerate the network resources on the infected machine. [60] |
| G0045 | menuPass | menuPass has used net use to conduct connectivity checks to machines. [61] |
| S0443 | MESSAGETAP | After loading the keyword and phone data files, MESSAGETAP begins monitoring all network connections to and from the victim server. [62] |
| G0069 | MuddyWater | MuddyWater has used a PowerShell backdoor to check for Skype connections on the target machine. [63] |
| G0129 | Mustang Panda | Mustang Panda has used netstat -ano to determine network connection information. [64] |
| S0102 | nbtstat | nbtstat can be used to discover current NetBIOS sessions. |
| S0039 | Net | Commands such as net use and net session can be used in Net to gather information about network connections from a particular host. [65] |
| S0104 | netstat | netstat can be used to enumerate local network connections, including active TCP connections and other network statistics. [66] |
| S0198 | NETWIRE | NETWIRE can capture session logon details from a compromised host. [67] |
| G0049 | OilRig | OilRig has used netstat -an on a victim to get a listing of network connections. [68] |
| S0439 | Okrum | Okrum was seen using NetSess to discover NetBIOS sessions. [69] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors used the net session , net use , and netstat commands as part of their advanced reconnaissance. [70] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors collected a list of open connections on the infected system using netstat and checks whether it has an internet connection. [71] |
| S0165 | OSInfo | OSInfo enumerates the current network connections similar to net use . [11] |
| S1091 | Pacu | Once inside a Virtual Private Cloud, Pacu can attempt to identify DirectConnect, VPN, or VPC Peering. [72] |
| S0013 | PlugX | PlugX has a module for enumerating TCP and UDP network connections and associated processes using the netstat command. [73] |
| G0033 | Poseidon Group | Poseidon Group obtains and saves information about victim network interfaces and addresses. [74] |
| S0378 | PoshC2 | PoshC2 contains an implementation of netstat to enumerate TCP and UDP connections. [75] |
| S0184 | POWRUNER | POWRUNER may collect active network connections by running netstat -an on a victim. [76] |
| S1228 | PUBLOAD | PUBLOAD has used several commands executed in sequence via cmd in a short interval to gather information on network connections. [77] |
| S0192 | Pupy | Pupy has a built-in utility command for netstat , can do net session through PowerView, and has an interactive shell which can be used to discover additional information. [78] |
| S1032 | PyDCrypt | PyDCrypt has used netsh to find RPC connections on remote machines. [79] |
| S0650 | QakBot | QakBot can use netstat to enumerate current network connections. [80] [81] |
| S0458 | Ramsay | Ramsay can use netstat to enumerate network connections. [82] |
| S0241 | RATANKBA | RATANKBA uses netstat -ano to search for specific IP address ranges. [83] |
| S0153 | RedLeaves | RedLeaves can enumerate drives and Remote Desktop sessions. [84] |
| S0125 | Remsec | Remsec can obtain a list of active connections and open ports. [85] |
| G0034 | Sandworm Team | Sandworm Team had gathered user, IP address, and server data related to RDP sessions on a compromised host. It has also accessed network diagram files useful for understanding how a host's network was configured. [86] [87] |
| S1085 | Sardonic | Sardonic has the ability to execute the netstat command. [88] |
| S0445 | ShimRatReporter | ShimRatReporter used the Windows function GetExtendedUdpTable to detect connected UDP endpoints. [89] |
| S0063 | SHOTPUT | SHOTPUT uses netstat to list TCP connection status. [90] |
| S0589 | Sibot | Sibot has retrieved a GUID associated with a present LAN connection on a compromised machine. [91] |
| S0633 | Sliver | Sliver can collect network connection information. [92] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA can enumerate open ports on a victim machine. [93] |
| S0374 | SpeakUp | SpeakUp uses the arp -a command. [94] |
| S0018 | Sykipot | Sykipot may use netstat -ano to display active network connections. [95] |
| G0139 | TeamTNT | TeamTNT has run netstat -anp to search for rival malware connections. [96] TeamTNT has also used libprocesshider to modify /etc/ld.so.preload . [97] |
| G0027 | Threat Group-3390 | Threat Group-3390 has used net use and netstat to conduct internal discovery of systems. The group has also used quser.exe to identify existing RDP sessions on a victim. [98] |
| G1022 | ToddyCat | ToddyCat has used netstat -anop tcp to discover TCP connections to compromised hosts. [99] |
| S0678 | Torisma | Torisma can use WTSEnumerateSessionsW to monitor remote desktop connections. [100] |
| S0094 | Trojan.Karagany | Trojan.Karagany can use netstat to collect a list of network connections. [101] |
| G0081 | Tropic Trooper | Tropic Trooper has tested if the localhost network is available and other connection capability on an infected system using command scripts. [102] |
| G0010 | Turla | Turla surveys a system upon check-in to discover active local network connections using the netstat -an , net use , net file , and net session commands. [37] [103] Turla RPC backdoors have also enumerated the IPv4 TCP connection table via the GetTcpTable2 API call. [104] |
| S0452 | USBferry | USBferry can use netstat and nbtstat to detect active network connections. [102] |
| G1047 | Velvet Ant | Velvet Ant has enumerated existing network connections on victim devices. [105] |
| S0180 | Volgmer | Volgmer can gather information about TCP connection state. [106] |
| G1017 | Volt Typhoon | Volt Typhoon has used netstat -ano on compromised hosts to enumerate network connections. [107] [108] |
| S0579 | Waterbear | Waterbear can use API hooks on GetExtendedTcpTable to retrieve a table containing a list of TCP endpoints available to the application. [109] |
| S0251 | Zebrocy | Zebrocy uses netstat -aon to gather network connection information. [110] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0320 | Detection of System Network Connections Discovery Across Platforms | AN0903 | Detects usage of commands or binaries (e.g., netstat, PowerShell Get-NetTCPConnection) and WMI or API calls to enumerate local or remote network connections. |
| AN0904 | Detects use of netstat, ss, lsof, or custom shell scripts to list current network connections. Often paired with privilege escalation or staging. |  |  |
| AN0905 | Detects shell-based enumeration of active connections using netstat , lsof -i , or AppleScript-based system discovery. |  |  |
| AN0906 | Detects shell or API usage of esxcli network ip connection list or netstat to enumerate ESXi host connections. |  |  |
| AN0907 | Detects interactive or automated use of CLI commands like show ip sockets , show tcp brief , or SNMP queries for active sessions on routers/switches. |  |  |
| AN0908 | Detects enumeration of cloud network interfaces, VPCs, subnets, or peer connections using CLI or SDKs (e.g., AWS CLI, Azure CLI, GCloud CLI). |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0320 | Detection of System Network Connections Discovery Across Platforms | AN0903 | Detects usage of commands or binaries (e.g., netstat, PowerShell Get-NetTCPConnection) and WMI or API calls to enumerate local or remote network connections. |
| AN0904 | Detects use of netstat, ss, lsof, or custom shell scripts to list current network connections. Often paired with privilege escalation or staging. |  |  |
| AN0905 | Detects shell-based enumeration of active connections using netstat , lsof -i , or AppleScript-based system discovery. |  |  |
| AN0906 | Detects shell or API usage of esxcli network ip connection list or netstat to enumerate ESXi host connections. |  |  |
| AN0907 | Detects interactive or automated use of CLI commands like show ip sockets , show tcp brief , or SNMP queries for active sessions on routers/switches. |  |  |
| AN0908 | Detects enumeration of cloud network interfaces, VPCs, subnets, or peer connections using CLI or SDKs (e.g., AWS CLI, Azure CLI, GCloud CLI). |  |  |

---

## References

- [Amazon. (n.d.). What Is Amazon VPC?. Retrieved October 6, 2019.](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Annamalai, N., Casey, C., Almeida, M., et. al.. (2019, June 18). What is Azure Virtual Network?. Retrieved October 6, 2019.](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
- [Google. (2019, September 23). Virtual Private Cloud (VPC) network overview. Retrieved October 6, 2019.](https://cloud.google.com/vpc/docs/vpc)
- [US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved October 19, 2020.](https://www.us-cert.gov/ncas/alerts/TA18-106A)
- [Zhongyuan Hau (Aaron), Ren Jie Yow, and Yoav Mazor. (2025, January 21). ESXi Ransomware Attacks: Stealthy Persistence through. Retrieved March 27, 2025.](https://www.sygnia.co/blog/esxi-ransomware-ssh-tunneling-defense-strategies/)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [FireEye Threat Intelligence. (2015, December 1). China-based Cyber Threat Group Uses Dropbox for Malware Communications and Targets Hong Kong Media Outlets. Retrieved December 4, 2015.](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)
- [Park, S. (2021, June 15). Andariel evolves to target South Korea with ransomware. Retrieved September 29, 2021.](https://securelist.com/andariel-evolves-to-target-south-korea-with-ransomware/102811/)
- [Anthropic. (2025, November). Disrupting the first reported AI-orchestrated cyber espionage campaign. Retrieved April 20, 2026.](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
- [Chen, X., Scott, M., Caselden, D.. (2014, April 26). New Zero-Day Exploit targeting Internet Explorer Versions 9 through 11 Identified in Targeted Attacks. Retrieved January 14, 2016.](https://www.fireeye.com/blog/threat-research/2014/04/new-zero-day-exploit-targeting-internet-explorer-versions-9-through-11-identified-in-targeted-attacks.html)
- [Yates, M. (2017, June 18). APT3 Uncovered: The code evolution of Pirpi. Retrieved September 28, 2017.](https://recon.cx/2017/montreal/resources/slides/RECON-MTL-2017-evolution_of_pirpi.pdf)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [Rostovcev, N. (2021, June 10). Big airline heist APT41 likely behind a third-party attack on Air India. Retrieved August 26, 2021.](https://www.group-ib.com/blog/colunmtk-apt41/)
- [Perez, D. et al. (2021, May 27). Re-Checking Your Pulse: Updates on Chinese APT Actors Compromising Pulse Secure VPN Devices. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Mundo, A. et al. (2021, February). Technical Analysis of Babuk Ransomware. Retrieved August 11, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
- [Adam Burgher. (2021, June 10). BackdoorDiplomacy: Upgrading from Quarian to Turian. Retrieved September 1, 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [F-Secure Labs. (2014). BlackEnergy & Quedagh: The convergence of crimeware and APT attacks. Retrieved March 24, 2016.](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
- [Baumgartner, K. and Garnaeva, M.. (2014, November 3). BE2 custom plugins, router abuse, and target profiles. Retrieved March 24, 2016.](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
- [GovCERT. (2016, May 23). Technical Report about the Espionage Case at RUAG. Retrieved November 7, 2018.](https://web.archive.org/web/20170718174931/https://www.melani.admin.ch/dam/melani/de/dokumente/2016/technical%20report%20ruag.pdf.download.pdf/Report_Ruag-Espionage-Case.pdf)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Mavis, N. (2020, September 21). The Art and Science of Detecting Cobalt Strike. Retrieved September 12, 2024.](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
- [Grunzweig, J. (2018, January 31). Comnie Continues to Target Organizations in East Asia. Retrieved June 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
- [Baskin, B. (2020, July 8). TAU Threat Discovery: Conti Ransomware. Retrieved February 17, 2021.](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [byt3bl33d3r. (2018, September 8). SMB: Command Reference. Retrieved July 17, 2020.](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [Konstantin Zykov. (2019, September 23). Hello! My name is Dtrack. Retrieved January 20, 2021.](https://securelist.com/my-name-is-dtrack/93338/)
- [Symantec Security Response. (2011, November). W32.Duqu: The precursor to the next Stuxnet. Retrieved September 17, 2015.](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
- [Chen, J., et al. (2022). Delving Deep: An Analysis of Earth Lusca’s Operations. Retrieved July 1, 2022.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
- [NHS Digital. (2020, November 26). Egregor Ransomware The RaaS successor to Maze. Retrieved December 29, 2020.](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [Kaspersky Lab's Global Research & Analysis Team. (2014, August 06). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroboros. Retrieved November 7, 2018.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [fatedier. (n.d.). What is frp?. Retrieved July 10, 2024.](https://github.com/fatedier/frp)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Cybereason Nocturnus. (2019, June 25). Operation Soft Cell: A Worldwide Campaign Against Telecommunications Providers. Retrieved July 18, 2019.](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)
- [Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [SOCRadar. (2024, January 24). Dark Web Profile: INC Ransom. Retrieved June 5, 2024.](https://socradar.io/dark-web-profile-inc-ransom/)
- [Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
- [Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)
- [Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)
- [Threat Intelligence Team. (2021, August 23). New variant of Konni malware used in campaign targetting Russia. Retrieved January 5, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
- [Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle. Retrieved October 27, 2021.](https://securelist.com/lazarus-threatneedle/100803/)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [Hsu, K. et al. (2020, June 24). Lucifer: New Cryptojacking and DDoS Hybrid Malware Exploiting High and Critical Vulnerabilities to Infect Windows Devices. Retrieved November 16, 2020.](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [DFIR Report. (2022, March 21). APT35 Automates Initial Access Using ProxyShell. Retrieved May 25, 2022.](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)
- [Mundo, A. (2020, March 26). Ransomware Maze. Retrieved May 18, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper. Retrieved April 5, 2017.](https://web.archive.org/web/20220224041316/https:/www.pwc.co.uk/cyber-security/pdf/cloud-hopper-report-final-v4.pdf)
- [Leong, R., Perez, D., Dean, T. (2019, October 31). MESSAGETAP: Who’s Reading Your Text Messages?. Retrieved May 11, 2020.](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)
- [Peretz, A. and Theck, E. (2021, March 5). Earth Vetala – MuddyWater Continues to Target Organizations in the Middle East. Retrieved March 18, 2021.](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
- [Hamzeloofard, S. (2020, January 31). New wave of PlugX targets Hong Kong | Avira Blog. Retrieved April 13, 2021.](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)
- [Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)
- [Microsoft. (n.d.). Netstat. Retrieved April 17, 2016.](https://technet.microsoft.com/en-us/library/bb490947.aspx)
- [Maniath, S. and Kadam P. (2019, March 19). Dissecting a NETWIRE Phishing Campaign's Usage of Process Hollowing. Retrieved January 7, 2021.](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
- [Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
- [Hromcova, Z. (2019, July). OKRUM AND KETRICAN: AN OVERVIEW OF RECENT KE3CHANG GROUP ACTIVITY. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.](https://github.com/RhinoSecurityLabs/pacu)
- [Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
- [Kaspersky Lab's Global Research and Analysis Team. (2016, February 9). Poseidon Group: a Targeted Attack Boutique specializing in global cyber-espionage. Retrieved March 16, 2016.](https://securelist.com/poseidon-group-a-targeted-attack-boutique-specializing-in-global-cyber-espionage/73673/)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Nicolas Verdier. (n.d.). Retrieved January 29, 2018.](https://github.com/n1nj4sec/pupy)
- [Checkpoint Research. (2021, November 15). Uncovering MosesStaff techniques: Ideology over Money. Retrieved August 11, 2022.](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [Kenefick, I. et al. (2022, October 12). Black Basta Ransomware Gang Infiltrates Networks via QAKBOT, Brute Ratel, and Cobalt Strike. Retrieved February 6, 2023.](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
- [Antiy CERT. (2020, April 20). Analysis of Ramsay components of Darkhotel's infiltration and isolation network. Retrieved March 24, 2021.](https://www.programmersought.com/article/62493896999/)
- [Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
- [Scott W. Brady. (2020, October 15). United States vs. Yuriy Sergeyevich Andrienko et al.. Retrieved November 25, 2020.](https://www.justice.gov/opa/press-release/file/1328521/download)
- [Joe Slowik. (2018, October 12). Anatomy of an Attack: Detecting and Defeating CRASHOVERRIDE. Retrieved December 18, 2020.](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)
- [Budaca, E., et al. (2021, August 25). FIN8 Threat Actor Goes Agile with New Sardonic Backdoor. Retrieved August 9, 2023.](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Falcone, R. and Wartell, R.. (2015, July 27). Observations on CVE-2015-3113, Prior Zero-Days and the Pirpi Payload. Retrieved January 22, 2016.](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [BishopFox. (n.d.). Sliver Netstat. Retrieved September 16, 2021.](https://github.com/BishopFox/sliver/tree/58a56a077f0813bb312f9fa4df7453b510c3a73b/implant/sliver/netstat)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [Check Point Research. (2019, February 4). SpeakUp: A New Undetected Backdoor Linux Trojan. Retrieved April 17, 2019.](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
- [Blasco, J. (2011, December 12). Another Sykipot sample likely targeting US federal agencies. Retrieved March 28, 2016.](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)
- [Fiser, D. Oliveira, A. (n.d.). Tracking the Activities of TeamTNT A Closer Look at a Cloud-Focused Malicious Actor Group. Retrieved September 22, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-tracking-the-activities-of-teamTNT.pdf)
- [AT&T Alien Labs. (2021, September 8). TeamTNT with new campaign aka Chimaera. Retrieved September 22, 2021.](https://cybersecurity.att.com/blogs/labs-research/teamtnt-with-new-campaign-aka-chimaera)
- [Counter Threat Unit Research Team. (2017, June 27). BRONZE UNION Cyberespionage Persists Despite Disclosures. Retrieved July 13, 2017.](https://www.secureworks.com/research/bronze-union)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [Beek, C. (2020, November 5). Operation North Star: Behind The Scenes. Retrieved December 20, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
- [Secureworks. (2019, July 24). Updated Karagany Malware Targets Energy Sector. Retrieved August 12, 2020.](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [Sygnia Team. (2024, June 3). China-Nexus Threat Group ‘Velvet Ant’ Abuses F5 Load Balancers for Persistence. Retrieved March 14, 2025.](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
- [Yagi, J. (2014, August 24). Trojan.Volgmer. Retrieved July 16, 2018.](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)
- [NSA et al. (2023, May 24). People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection. Retrieved July 27, 2023.](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)
- [Counter Threat Unit Research Team. (2023, May 24). Chinese Cyberespionage Group BRONZE SILHOUETTE Targets U.S. Government and Defense Organizations. Retrieved July 27, 2023.](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)
- [Su, V. et al. (2019, December 11). Waterbear Returns, Uses API Hooking to Evade Security. Retrieved February 22, 2021.](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
- [ESET Research. (2019, May 22). A journey to Zebrocy land. Retrieved June 20, 2019.](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)

---

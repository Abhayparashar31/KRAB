# Network Sniffing

## Description

Adversaries may passively sniff network traffic to capture information about an environment, including authentication material passed over the network. Network sniffing refers to using the network interface on a system to monitor or capture information sent over a wired or wireless connection. An adversary may place a network interface into promiscuous mode to passively access data in transit over the network, or use span ports to capture a larger amount of data.

Data captured via this technique may include user credentials, especially those sent over an insecure, unencrypted protocol. Techniques for name service resolution poisoning, such as Name Resolution Poisoning and SMB Relay , can also be used to capture credentials to websites, proxies, and internal systems by redirecting traffic to an adversary.

Network sniffing may reveal configuration details, such as running services, version numbers, and other network characteristics (e.g. IP addresses, hostnames, VLAN IDs) necessary for subsequent Lateral Movement and/or Stealth activities. Adversaries may likely also utilize network sniffing during Adversary-in-the-Middle (AiTM) to passively gain additional knowledge about the environment.

In cloud-based environments, adversaries may still be able to use traffic mirroring services to sniff network traffic from virtual machines. For example, AWS Traffic Mirroring, GCP Packet Mirroring, and Azure vTap allow users to define specified instances to collect traffic from and specified targets to send collected traffic to. [1] [2] [3] Often, much of this traffic will be in cleartext due to the use of TLS termination at the load balancer level to reduce the strain of encrypting and decrypting traffic. [4] [5] The adversary can then use exfiltration techniques such as Transfer Data to Cloud Account in order to access the sniffed traffic. [4]

On network devices, adversaries may perform network captures using Network Device CLI commands such as monitor capture . [6] [7]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0028 | 2015 Ukraine Electric Power Attack | During the 2015 Ukraine Electric Power Attack , Sandworm Team used BlackEnergy ’s network sniffer module to discover user credentials being sent over the network between the local LAN and the power grid’s industrial control systems. [8] |
| G0007 | APT28 | APT28 deployed the open source tool Responder to conduct NetBIOS Name Service poisoning, which captured usernames and hashed passwords that allowed access to legitimate credentials. [9] [10] APT28 close-access teams have used Wi-Fi pineapples to intercept Wi-Fi signals and user credentials. [11] |
| G0064 | APT33 | APT33 has used SniffPass to collect credentials by sniffing network traffic. [12] |
| C0046 | ArcaneDoor | ArcaneDoor included network packet capture and sniffing for data collection in victim environments. [13] [14] |
| S1224 | CASTLETAP | CASTLETAP has the ability to create a raw promiscuous socket to sniff network traffic. [15] |
| S1204 | cd00r | cd00r can use the libpcap library to monitor captured packets for specifc sequences. [16] |
| G0105 | DarkVishnya | DarkVishnya used network sniffing to obtain login data. [17] |
| S0367 | Emotet | Emotet has been observed to hook network APIs to monitor network traffic. [18] |
| S0363 | Empire | Empire can be used to conduct packet captures on target hosts. [19] |
| S0661 | FoggyWeb | FoggyWeb can configure custom listeners to passively monitor all incoming HTTP GET and POST requests sent to the AD FS server from the intranet/internet and intercept HTTP requests that match the custom URI patterns defined by the actor. [20] |
| S0357 | Impacket | Impacket can be used to sniff network traffic via an interface or raw socket. [21] |
| S1203 | J-magic | J-magic has a pcap listener function that can create an Extended Berkley Packet Filter (eBPF) on designated interfaces and ports. [22] |
| S1206 | JumbledPath | JumbledPath has the ability to perform packet capture on remote devices via actor-defined jump-hosts. [23] |
| G0094 | Kimsuky | Kimsuky has used the Nirsoft SniffPass network sniffer to obtain passwords sent over non-secure protocols. [24] [25] |
| S1186 | Line Dancer | Line Dancer can create and exfiltrate packet captures from compromised environments. [13] |
| S0443 | MESSAGETAP | MESSAGETAP uses the libpcap library to listen to all traffic and parses network protocols starting with Ethernet and IP layers. It continues parsing protocol layers including SCTP, SCCP, and TCAP and finally extracts SMS message data and routing metadata. [26] |
| S0590 | NBTscan | NBTscan can dump and print whole packet content. [27] [28] |
| S0587 | Penquin | Penquin can sniff network traffic to look for packets matching specific conditions. [29] [30] |
| S0378 | PoshC2 | PoshC2 contains a module for taking packet captures on compromised hosts. [31] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 used a passive backdoor to act as a libpcap-based packet sniffer. [32] |
| S0019 | Regin | Regin appears to have functionality to sniff for credentials passed over HTTP, SMTP, and SMB. [33] |
| S0174 | Responder | Responder captures hashes and credentials that are sent to the system after the name services have been poisoned. [34] |
| G1045 | Salt Typhoon | Salt Typhoon has used a variety of tools and techniques to capture packet data between network interfaces. [23] |
| G0034 | Sandworm Team | Sandworm Team has used intercepter-NG to sniff passwords in network traffic. [35] |
| S9024 | SPAWNCHIMERA | SPAWNCHIMERA has monitored and filtered network traffic on compromised edge devices, allowing legitimate traffic to pass while redirecting attacker-controlled traffic to infrastructure under adversary control. [36] [37] |
| G1048 | UNC3886 | UNC3886 has used the LOOKOVER sniffer to sniff TACACS+ authentication packets. [38] |
| G1047 | Velvet Ant | Velvet Ant has used a custom tool, "VELVETTAP", to perform packet capture from compromised F5 BIG-IP devices. [39] |
| S1154 | VersaMem | VersaMem hooked the Catalina application filter chain doFilter on compromised systems to monitor all inbound requests to the local Tomcat web server, inspecting them for parameters like passwords and follow-on Java modules. [40] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1041 | Encrypt Sensitive Information | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure web traffic that may contain credentials is protected by SSL/TLS. |
| M1032 | Multi-factor Authentication | Use multi-factor authentication wherever possible. |
| M1030 | Network Segmentation | Deny direct access of broadcasts and multicast sniffing, and prevent attacks such as Name Resolution Poisoning and SMB Relay |
| M1018 | User Account Management | In cloud environments, ensure that users are not granted permissions to create or modify traffic mirrors unless this is explicitly required. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0314 | Detection Strategy for Network Sniffing Across Platforms | AN0875 | Detects suspicious execution of network monitoring tools (e.g., Wireshark, tshark, Microsoft Message Analyzer), driver loading indicative of promiscuous mode, or non-admin user privilege escalation to access NICs for capture. |
| AN0876 | Correlates interface mode changes to promiscuous with execution of sniffing tools like tcpdump, tshark, or custom pcap libraries. Detects abnormal NIC configurations and unauthorized sniffing from non-root sessions. |  |  |
| AN0877 | Detects enabling of interface sniffing via packet capture tools or AppleScript triggering tcpdump . Leverages Unified Logs and process lineage to identify suspicious use of pfctl , tcpdump , or libpcap libraries. |  |  |
| AN0878 | Detects creation of traffic mirroring sessions (e.g., AWS VPC Traffic Mirroring, Azure vTAP) that redirect traffic from critical assets to other virtual instances, often followed by file creation or session establishment. |  |  |
| AN0879 | Detects execution of capture commands via CLI ( monitor capture , debug packet , etc.) or unauthorized CLI access followed by logging configuration changes on Cisco/Juniper/Arista gear. |  |  |

---

## References

- [Amazon Web Services. (n.d.). How Traffic Mirroring works. Retrieved March 17, 2022.](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-how-it-works.html)
- [Google Cloud. (n.d.). Packet Mirroring overview. Retrieved March 17, 2022.](https://cloud.google.com/vpc/docs/packet-mirroring)
- [Microsoft. (2022, February 9). Virtual network TAP. Retrieved March 17, 2022.](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-tap-overview)
- [Spencer Gietzen. (2019, September 17). Abusing VPC Traffic Mirroring in AWS. Retrieved March 17, 2022.](https://rhinosecuritylabs.com/aws/abusing-vpc-traffic-mirroring-in-aws/)
- [Luke Paine. (2020, March 11). Through the Looking Glass — Part 1. Retrieved March 17, 2022.](https://posts.specterops.io/through-the-looking-glass-part-1-f539ae308512)
- [US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved October 19, 2020.](https://www.us-cert.gov/ncas/alerts/TA18-106A)
- [Cisco. (2022, August 17). Configure and Capture Embedded Packet on Software. Retrieved July 13, 2022.](https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-embedded-packet-capture/116045-productconfig-epc-00.html)
- [Charles McLellan. (2016, March 4). How hackers attacked Ukraine's power grid: Implications for Industrial IoT security. Retrieved September 27, 2023.](https://www.zdnet.com/article/how-hackers-attacked-ukraines-power-grid-implications-for-industrial-iot-security/)
- [FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
- [Smith, L. and Read, B.. (2017, August 11). APT28 Targets Hospitality Sector, Presents Threat to Travelers. Retrieved November 17, 2024.](https://web.archive.org/web/20171202185937/https://www.fireeye.com/blog/threat-research/2017/08/apt28-targets-hospitality-sector.html)
- [Brady, S . (2018, October 3). Indictment - United States vs Aleksei Sergeyevich Morenets, et al.. Retrieved October 1, 2020.](https://www.justice.gov/opa/page/file/1098481/download)
- [Security Response attack Investigation Team. (2019, March 27). Elfin: Relentless Espionage Group Targets Multiple Organizations in Saudi Arabia and U.S.. Retrieved April 10, 2019.](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)
- [Cisco Talos. (2024, April 24). ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices. Retrieved January 6, 2025.](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
- [Canadian Centre for Cyber Security. (2024, April 24). Cyber Activity Impacting CISCO ASA VPNs. Retrieved January 6, 2025.](https://www.cyber.gc.ca/en/news-events/cyber-activity-impacting-cisco-asa-vpns)
- [Marvi, A. et al.. (2023, March 16). Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation. Retrieved March 22, 2023.](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
- [Hartrell, Greg. (2002, August). Get a handle on cd00r: The invisible backdoor. Retrieved October 13, 2018.](https://www.giac.org/paper/gcih/342/handle-cd00r-invisible-backdoor/103631)
- [Golovanov, S. (2018, December 6). DarkVishnya: Banks attacked through direct connection to local network. Retrieved May 15, 2020.](https://securelist.com/darkvishnya/89169/)
- [Salvio, J.. (2014, June 27). New Banking Malware Uses Network Sniffing for Data Theft. Retrieved March 25, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/new-banking-malware-uses-network-sniffing-for-data-theft/)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Ramin Nafisi. (2021, September 27). FoggyWeb: Targeted NOBELIUM malware leads to persistent backdoor. Retrieved October 4, 2021.](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
- [SecureAuth. (n.d.). Retrieved January 15, 2019.](https://www.secureauth.com/labs/open-source-tools/impacket)
- [Black Lotus Labs. (2025, January 23). The J-Magic Show: Magic Packets and Where to find them. Retrieved February 17, 2025.](https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/)
- [Cisco Talos. (2025, February 20). Weathering the storm: In the midst of a Typhoon. Retrieved February 24, 2025.](https://blog.talosintelligence.com/salt-typhoon-analysis/)
- [CISA, FBI, CNMF. (2020, October 27). https://us-cert.cisa.gov/ncas/alerts/aa20-301a. Retrieved November 4, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-301a)
- [ASERT team. (2018, December 5). STOLEN PENCIL Campaign Targets Academia. Retrieved February 5, 2019.](https://asert.arbornetworks.com/stolen-pencil-campaign-targets-academia/)
- [Leong, R., Perez, D., Dean, T. (2019, October 31). MESSAGETAP: Who’s Reading Your Text Messages?. Retrieved May 11, 2020.](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)
- [Bezroutchko, A. (2019, November 19). NBTscan man page. Retrieved March 17, 2021.](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)
- [SecTools. (2003, June 11). NBTscan. Retrieved March 17, 2021.](https://sectools.org/tool/nbtscan/)
- [Leonardo. (2020, May 29). MALWARE TECHNICAL INSIGHT TURLA “Penquin_x64”. Retrieved March 11, 2021.](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
- [Baumgartner, K. and Raiu, C. (2014, December 8). The ‘Penquin’ Turla. Retrieved March 11, 2021.](https://securelist.com/the-penquin-turla-2/67962/)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [Lamparski, L. et al. (2025, March 11). Ghost in the Router: China-Nexus Espionage Actor UNC3886 Targets Juniper Routers. Retrieved June 24, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, November 24). THE REGIN PLATFORM NATION-STATE OWNAGE OF GSM NETWORKS. Retrieved December 1, 2014.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070305/Kaspersky_Lab_whitepaper_Regin_platform_eng.pdf)
- [Gaffie, L. (2016, August 25). Responder. Retrieved November 17, 2017.](https://github.com/SpiderLabs/Responder)
- [Cherepanov, A.. (2016, December 13). The rise of TeleBots: Analyzing disruptive KillDisk attacks. Retrieved June 10, 2020.](https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/)
- [John Wolfram, Josh Murchie, Matt Lin, Daniel Ainsworth, Robert Wallace, Dimiter Andonov, Dhanesh Kizhakkinan, Jacob Thompson. (2025, January 8). Ivanti Connect Secure VPN Targeted in New Zero-Day Exploitation. Retrieved April 14, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
- [Matt Lin, Austin Larsen, John Wolfram, Ashley Pearson, Josh Murchie, Lukasz Lamparski, Joseph Pisano, Ryan Hall, Ron Craft, Shawn Crew, Billy Wong, Tyler McLellan. (2024, April 4). Cutting Edge, Part 4: Ivanti Connect Secure VPN Post-Exploitation Lateral Movement Case Studies. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
- [Punsaen Boonyakarn, Shawn Chew, Logeswaran Nadarajan, Mathew Potaczek, Jakub Jozwiak, and Alex Marvi. (2024, June 18). Cloaked and Covert: Uncovering UNC3886 Espionage Operations. Retrieved September 24, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [Sygnia Team. (2024, June 3). China-Nexus Threat Group ‘Velvet Ant’ Abuses F5 Load Balancers for Persistence. Retrieved March 14, 2025.](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
- [Black Lotus Labs. (2024, August 27). Taking The Crossroads: The Versa Director Zero-Day Exploitaiton. Retrieved August 27, 2024.](https://blog.lumen.com/taking-the-crossroads-the-versa-director-zero-day-exploitation/)

---

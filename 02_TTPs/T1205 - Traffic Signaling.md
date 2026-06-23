# Traffic Signaling

## Description

Adversaries may use traffic signaling to hide open ports or other malicious functionality used for persistence or command and control. Traffic signaling involves the use of a magic value or sequence that must be sent to a system to trigger a special response, such as opening a closed port or executing a malicious task. This may take the form of sending a series of packets with certain characteristics before a port will be opened that the adversary can use for command and control. Usually this series of packets consists of attempted connections to a predefined sequence of closed ports (i.e. Port Knocking ), but can involve unusual flags, specific strings, or other unique characteristics. After the sequence is completed, opening a port may be accomplished by the host-based firewall, but could also be implemented by custom software.

Adversaries may also communicate with an already open port, but the service listening on that port will only respond to commands or trigger other malicious functionality if passed the appropriate magic value(s).

The observation of the signal packets to trigger the communication can be conducted through different methods. One means, originally implemented by Cd00r [1] , is to use the libpcap libraries to sniff for the packets in question. Another method leverages raw sockets, which enables the malware to use ports that are already open for use by other programs.

On network devices, adversaries may use crafted packets to enable Network Device Authentication for standard services offered by the device such as telnet. Such signaling may also be used to open a closed service port such as telnet, or to trigger module modification of malware implants on the device, adding, removing, or changing malicious capabilities. Adversaries may use crafted packets to attempt to connect to one or more (open or closed) ports, but may also attempt to connect to a router interface, broadcast, and network address IP on the same port in order to achieve their goals and objectives. [2] [3] [4] To enable this traffic signaling on embedded devices, adversaries must first achieve and leverage Patch System Image due to the monolithic nature of the architecture.

Adversaries may also use the Wake-on-LAN feature to turn on powered off systems. Wake-on-LAN is a hardware feature that allows a powered down system to be powered on, or woken up, by sending a magic packet to it. Once the system is powered on, it may become a target for lateral movement. [5] [6]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S9011 | BRUSHFIRE | BRUSHFIRE has monitored inbound VPN traffic to compromised appliances until specific inbound packets contain a specific magic string/pattern instead of external beaconing. [7] |
| S1118 | BUSHWALK | BUSHWALK can modify the DSUserAgentCap.pm Perl module on Ivanti Connect Secure VPNs and either activate or deactivate depending on the value of the user agent in incoming HTTP requests. [8] |
| S0220 | Chaos | Chaos provides a reverse shell is triggered upon receipt of a packet with a special string, sent to any port. [9] |
| C0029 | Cutting Edge | During Cutting Edge , threat actors sent a magic 48-byte sequence to enable the PITSOCK backdoor to communicate via the /tmp/clientsDownload.sock socket. [8] |
| S1203 | J-magic | J-magic can monitor TCP traffic for packets containing one of five different predefined parameters and will spawn a reverse shell if one of the parameters and the proper response string to a subsequent challenge is received. [10] |
| G0094 | Kimsuky | Kimsuky has used TRANSLATEXT to redirect clients to legitimate Gmail, Naver or Kakao pages if the clients connect with no parameters. [11] |
| S0641 | Kobalos | Kobalos is triggered by an incoming TCP connection to a legitimate service from a specific source port. [12] [13] |
| G0129 | Mustang Panda | Mustang Panda has utilized a magic value in C2 communications and only executes in memory when response packets match specific values of "17 03 03" or "46 77 4d". [14] |
| S0664 | Pandora | Pandora can identify if incoming HTTP traffic contains a token and if so it will intercept the traffic and process the received command. [15] |
| S0587 | Penquin | Penquin will connect to C2 only after sniffing a "magic packet" value in TCP or UDP packets matching specific conditions. [16] [17] |
| S1228 | PUBLOAD | PUBLOAD has utilized a magic value in C2 communications and only executes in memory when response packets match specific values of 17 03 03. [14] [18] [19] [20] [21] PUBLOAD has also used magic bytes consisting of 46 77 4d. [14] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 leveraged malware capable of inpecting packets for a magic-string to activate backdoor functionalities. [22] |
| S1219 | REPTILE | The REPTILE reverse shell component can listen for a specialized packet in TCP, UDP, or ICMP for activation. [23] [24] |
| S0446 | Ryuk | Ryuk has used Wake-on-Lan to power on turned off systems for lateral movement. [5] |
| S0519 | SYNful Knock | SYNful Knock can be sent instructions via special packets to change its functionality. Code for new functionality can be included in these messages. [3] |
| S1239 | TONESHELL | TONESHELL has utilized a magic value in C2 communications and only executes in memory when response packets match specific values. [25] [20] [26] |
| S1201 | TRANSLATEXT | TRANSLATEXT has redirected clients to legitimate Gmail, Naver or Kakao pages if the clients connect with no parameters. [11] |
| S0221 | Umbreon | Umbreon provides additional access using its backdoor Espeon, providing a reverse shell upon receipt of a special packet. [27] |
| G1048 | UNC3886 | UNC3886 has used the TABLEFLIP traffic redirection utility to listen for specialized command packets on compromised FortiManager devices. [24] |
| S0022 | Uroburos | Uroburos can intercept the first client to server packet in the 3-way TCP handshake to determine if the packet contains the correct unique value for a specific Uroburos implant. If the value does not match, the packet and the rest of the TCP session are passed to the legitimate listening application. [28] |
| S0430 | Winnti for Linux | Winnti for Linux has used a passive listener, capable of identifying a specific magic value before executing tasking, as a secondary command and control (C2) mechanism. [29] |
| S1114 | ZIPLINE | ZIPLINE can identify a specific string in intercepted network traffic, SSH-2.0-OpenSSH_0.3xx. , to trigger its command functionality. [30] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1042 | Disable or Remove Feature or Program | Disable Wake-on-LAN if it is not needed within an environment. |
| M1037 | Filter Network Traffic | Mitigation of some variants of this technique could be achieved through the use of stateful firewalls, depending upon how it is implemented. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0524 | Traffic Signaling (Port-knock / magic-packet → firewall or service activation) – T1205 | AN1448 | A remote host sends a short sequence of failed connection attempts (RST/ICMP unreachable) to a set of closed ports. Within a brief window the endpoint (a) adds/enables a firewall rule or (b) a sniffer-backed process begins listening or opens a new socket, after which a successful connection occurs. Also detects Wake-on-LAN magic packets seen on local segment. |
| AN1449 | Closed-port knock sequence from a remote IP followed by on-host firewall change (iptables/nftables) or daemon starts listening (socket open) and a successful TCP/UDP connect. Optional detection of libpcap/raw-socket sniffers spawning to watch for secret values. |  |  |
| AN1450 | Remote knock sequence followed by PF/socketfilterfw rule update or a background process listening on a new port; then a successful TCP session. Also flags WoL magic packets on local segment. |  |  |
| AN1451 | Crafted ‘synful knock’ patterns toward routers/switches (same src hits interface/broadcast/network address on same port in short order) followed by ACL/telnet/SSH enablement or module change. Detect device image/ACL updates then a new mgmt session. |  |  |

---

## References

- [Hartrell, Greg. (2002, August). Get a handle on cd00r: The invisible backdoor. Retrieved October 13, 2018.](https://www.giac.org/paper/gcih/342/handle-cd00r-invisible-backdoor/103631)
- [Graham Holmes. (2015, October 8). Evolution of attacks on Cisco IOS devices. Retrieved October 19, 2020.](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)
- [Bill Hau, Tony Lee, Josh Homan. (2015, September 15). SYNful Knock - A Cisco router implant - Part I. Retrieved November 17, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/synful-knock-acis/)
- [Omar Santos. (2020, October 19). Attackers Continue to Target Legacy Devices. Retrieved October 20, 2020.](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
- [Abrams, L. (2021, January 14). Ryuk Ransomware Uses Wake-on-Lan To Encrypt Offline Devices. Retrieved February 11, 2021.](https://www.bleepingcomputer.com/news/security/ryuk-ransomware-uses-wake-on-lan-to-encrypt-offline-devices/)
- [AMD. (1995, November 1). Magic Packet Technical White Paper. Retrieved February 17, 2021.](https://www.amd.com/system/files/TechDocs/20213.pdf)
- [Sila Ozeren Hacioglu. (2025, May 5). UNC5221’s Latest Exploit: Weaponizing CVE-2025-22457 in Ivanti Connect Secure. Retrieved April 13, 2026.](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
- [Lin, M. et al. (2024, February 27). Cutting Edge, Part 3: Investigating Ivanti Connect Secure VPN Exploitation and Persistence Attempts. Retrieved March 1, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
- [Sebastian Feldmann. (2018, February 14). Chaos: a Stolen Backdoor Rising Again. Retrieved March 5, 2018.](http://gosecure.net/2018/02/14/chaos-stolen-backdoor-rising/)
- [Black Lotus Labs. (2025, January 23). The J-Magic Show: Magic Packets and Where to find them. Retrieved February 17, 2025.](https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/)
- [Park, S. (2024, June 27). Kimsuky deploys TRANSLATEXT to target South Korean academia. Retrieved October 14, 2024.](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
- [M.Leveille, M., Sanmillan, I. (2021, February 2). Kobalos – A complex Linux threat to high performance computing infrastructure. Retrieved August 24, 2021.](https://www.welivesecurity.com/2021/02/02/kobalos-complex-linux-threat-high-performance-computing-infrastructure/)
- [M.Leveille, M., Sanmillan, I. (2021, January). A WILD KOBALOS APPEARS Tricksy Linux malware goes after HPCs. Retrieved August 24, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
- [CSIRT CTI. (2024, January 23). Stately Taurus Targets Myanmar Amidst Concerns over Military Junta’s Handling of Rebel Attacks. Retrieved August 4, 2025.](https://csirt-cti.net/2024/01/23/stately-taurus-targets-myanmar/)
- [Lunghi, D. and Lu, K. (2021, April 9). Iron Tiger APT Updates Toolkit With Evolved SysUpdate Malware. Retrieved November 12, 2021.](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
- [Leonardo. (2020, May 29). MALWARE TECHNICAL INSIGHT TURLA “Penquin_x64”. Retrieved March 11, 2021.](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
- [Baumgartner, K. and Raiu, C. (2014, December 8). The ‘Penquin’ Turla. Retrieved March 11, 2021.](https://securelist.com/the-penquin-turla-2/67962/)
- [Golo Muhr, Joshua Chung. (2025, June 23). Hive0154 aka Mustang Panda shifts focus on Tibetan community to deploy Pubload backdoor. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [Nick Dai, Vickie Su, Sunny Lu. (2022, November 18). Earth Preta Spear-Phishing Governments Worldwide. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
- [Unit42. (2024, March 26). ASEAN Entities in the Spotlight: Chinese APT Group Targeting. Retrieved August 4, 2025.](https://unit42.paloaltonetworks.com/chinese-apts-target-asean-entities/)
- [Lamparski, L. et al. (2025, March 11). Ghost in the Router: China-Nexus Espionage Actor UNC3886 Targets Juniper Routers. Retrieved June 24, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers)
- [Punsaen Boonyakarn, Shawn Chew, Logeswaran Nadarajan, Mathew Potaczek, Jakub Jozwiak, and Alex Marvi. (2024, June 18). Cloaked and Covert: Uncovering UNC3886 Espionage Operations. Retrieved September 24, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [Marvi, A. et al.. (2023, March 16). Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation. Retrieved March 22, 2023.](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
- [Nathaniel Morales, Nick Dai. (2025, February 18). Earth Preta Mixes Legitimate and Malicious Components to Sidestep Detection. Retrieved September 10, 2025.](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
- [Sunny Lu, Vickie Su, Nick Dai. (2023, June 14). Behind the Scenes: Unveiling the Hidden Workings of Earth Preta. Retrieved September 10, 2025.](https://www.trendmicro.com/en_us/research/23/f/behind-the-scenes-unveiling-the-hidden-workings-of-earth-preta.html)
- [Fernando Mercês. (2016, September 5). Pokémon-themed Umbreon Linux Rootkit Hits x86, ARM Systems. Retrieved March 5, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/pokemon-themed-umbreon-linux-rootkit-hits-x86-arm-systems/?_ga=2.180041126.367598458.1505420282-1759340220.1502477046)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Chronicle Blog. (2019, May 15). Winnti: More than just Windows and Gates. Retrieved April 29, 2020.](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)
- [McLellan, T. et al. (2024, January 12). Cutting Edge: Suspected APT Targets Ivanti Connect Secure VPN in New Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)

---

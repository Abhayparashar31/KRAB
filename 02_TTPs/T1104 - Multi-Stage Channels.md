# Multi-Stage Channels

## Description

Adversaries may create multiple stages for command and control that are employed under different conditions or for certain functions. Use of multiple stages may obfuscate the command and control channel to make detection more difficult.

Remote access tools will call back to the first-stage command and control server for instructions. The first stage may have automated capabilities to collect basic host information, update tools, and upload additional files. A second remote access tool (RAT) could be uploaded at that point to redirect the host to the second-stage command and control server. The second stage will likely be more fully featured and allow the adversary to interact with the system through a reverse shell and additional RAT features.

The different stages will likely be hosted separately with no overlapping infrastructure. The loader may also have backup first-stage callbacks or Fallback Channels in case the original first-stage communication path is discovered and blocked.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0022 | APT3 | An APT3 downloader first establishes a SOCKS5 connection to 192.157.198[.]103 using TCP port 1913; once the server response is verified, it then requests a connection to 192.184.60[.]229 on TCP port 81. [1] |
| G0096 | APT41 | APT41 used the storescyncsvc.dll BEACON backdoor to download a secondary backdoor. [2] |
| S0031 | BACKSPACE | BACKSPACE attempts to avoid detection by checking a first stage command and control server to determine if it should connect to the second stage server, which performs "louder" interactions with the malware. [3] |
| S0534 | Bazar | The Bazar loader is used to download and execute the Bazar backdoor. [4] [5] |
| S0069 | BLACKCOFFEE | BLACKCOFFEE uses Microsoft’s TechNet Web portal to obtain an encoded tag containing the IP address of a command and control server and then communicates separately with that IP address for C2. If the C2 server is discovered or shut down, the threat actors can update the encoded IP address on TechNet to maintain control of the victims’ machines. [6] |
| S0220 | Chaos | After initial compromise, Chaos will download a second stage to establish a more permanent presence on the affected system. [7] |
| S1206 | JumbledPath | JumbledPath can communicate over a unique series of connections to send and retrieve data from exploited devices. [8] |
| S1160 | Latrodectus | Latrodectus has used a two-tiered C2 configuration with tier one nodes connecting to the victim and tier two nodes connecting to backend infrastructure. [9] |
| G0032 | Lazarus Group | Lazarus Group has used multi-stage malware components that inject later stages into separate processes. [10] |
| S1141 | LunarWeb | LunarWeb can use one C2 URL for first contact and to upload information about the host computer and two additional C2 URLs for getting commands. [11] |
| G0069 | MuddyWater | MuddyWater has used one C2 to obtain enumeration scripts and monitor web logs, but a different C2 to send data back. [12] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 used malware with separate channels to request and carry out tasks from C2. [13] |
| S1086 | Snip3 | Snip3 can download and execute additional payloads and modules over separate communication channels. [14] [15] |
| S0022 | Uroburos | Individual Uroburos implants can use multiple communication channels based on one of four available modes of operation. [16] |
| S0476 | Valak | Valak can download additional modules and malware capable of using separate C2 channels. [17] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0228 | Detect Multi-Stage Command and Control Channels | AN0637 | Initial process initiates outbound connection to first-stage C2, receives payloads or commands, then spawns or injects into a second process that establishes a new outbound connection to an unrelated destination (second-stage C2). |
| AN0638 | Shell script or binary initiates curl/wget request to staging domain, writes output to disk or memory, and shortly afterward launches another process that establishes new outbound connection to a different IP or hostname. |  |  |
| AN0639 | Initial process using NSURLSession or similar APIs reaches out to known staging domains, followed by creation of a reverse shell or RAT connecting to a second unrelated server. |  |  |
| AN0640 | CLI-based or API-based network call from the hypervisor to external staging host, shortly followed by a connection to a second external IP by a spawned process or scheduled task. |  |  |

---

## References

- [Moran, N., et al. (2014, November 21). Operation Double Tap. Retrieved January 14, 2016.](https://www.fireeye.com/blog/threat-research/2014/11/operation_doubletap.html)
- [Glyer, C, et al. (2020, March). This Is Not a Test: APT41 Initiates Global Intrusion Campaign Using Multiple Exploits. Retrieved April 28, 2020.](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)
- [FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved November 17, 2024.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Sadique, M. and Singh, A. (2020, September 29). Spear Phishing Campaign Delivers Buer and Bazar Malware. Retrieved November 19, 2020.](https://www.zscaler.com/blogs/research/spear-phishing-campaign-delivers-buer-and-bazar-malware)
- [FireEye Labs/FireEye Threat Intelligence. (2015, May 14). Hiding in Plain Sight: FireEye and Microsoft Expose Obfuscation Tactic. Retrieved November 17, 2024.](https://web.archive.org/web/20240119213200/https://www2.fireeye.com/rs/fireye/images/APT17_Report.pdf)
- [Sebastian Feldmann. (2018, February 14). Chaos: a Stolen Backdoor Rising Again. Retrieved March 5, 2018.](http://gosecure.net/2018/02/14/chaos-stolen-backdoor-rising/)
- [Cisco Talos. (2025, February 20). Weathering the storm: In the midst of a Typhoon. Retrieved February 24, 2025.](https://blog.talosintelligence.com/salt-typhoon-analysis/)
- [Proofpoint Threat Research and Team Cymru S2 Threat Research. (2024, April 4). Latrodectus: This Spider Bytes Like Ice . Retrieved May 31, 2024.](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
- [Saini, A. and Hossein, J. (2022, January 27). North Korea’s Lazarus APT leverages Windows Update client, GitHub in latest campaign. Retrieved January 27, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [Adamitis, D. et al. (2019, May 20). Recent MuddyWater-associated BlackWater campaign shows signs of new anti-detection techniques. Retrieved June 5, 2019.](https://blog.talosintelligence.com/2019/05/recent-muddywater-associated-blackwater.html)
- [Lamparski, L. et al. (2025, March 11). Ghost in the Router: China-Nexus Espionage Actor UNC3886 Targets Juniper Routers. Retrieved June 24, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers)
- [Lorber, N. (2021, May 7). Revealing the Snip3 Crypter, a Highly Evasive RAT Loader. Retrieved September 13, 2023.](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
- [Jornet, A. (2021, December 23). Snip3, an investigation into malware. Retrieved September 19, 2023.](https://telefonicatech.com/blog/snip3-investigacion-malware)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Duncan, B. (2020, July 24). Evolution of Valak, from Its Beginnings to Mass Distribution. Retrieved August 31, 2020.](https://unit42.paloaltonetworks.com/valak-evolution/)

---

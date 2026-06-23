# Execution Guardrails

## Description

Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against an intended target and reduces collateral damage from an adversary’s campaign. [1] Values an adversary can provide about a target system or environment to use as guardrails may include specific network share names, attached physical devices, files, joined Active Directory (AD) domains, and local/external IP addresses. [2]

Guardrails can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. This use of guardrails is distinct from typical Virtualization/Sandbox Evasion . While use of Virtualization/Sandbox Evasion may involve checking for known sandbox values and continuing with execution only if there is no match, the use of guardrails will involve checking for an expected target-specific value and only continuing with execution if there is such a match.

Adversaries may identify and block certain user-agents to evade defenses and narrow the scope of their attack to victims and platforms on which it will be most effective. A user-agent self-identifies data such as a user's software application, operating system, vendor, and version. Adversaries may check user-agents for operating system identification and then only serve malware for the exploitable software while ignoring all other operating systems. [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1194 | Akira _v2 | Akira _v2 will fail to execute if the targeted /vmfs/volumes/ path does not exist or is not defined. [4] |
| S0504 | Anchor | Anchor can terminate itself if specific execution flags are not present. [5] |
| S1133 | Apostle | Apostle 's ransomware variant requires that a base64-encoded argument is passed when executed, that is used as the Public Key for subsequent encryption operations. If Apostle is executed without this argument, it automatically runs a self-delete function. [6] |
| G0099 | APT-C-36 | APT-C-36 has used geolocation filtering in malware delivery to redirect traffic not coming from a targeted region or country, such as Ecuador or Colombia, to legitimate sites. [7] [8] |
| S0570 | BitPaymer | BitPaymer compares file names and paths to a list of excluded names and directory names during encryption. [9] |
| G1043 | BlackByte | BlackByte stopped execution if identified language settings on victim machines was Russian or one of several language associated with former Soviet republics. [10] BlackByte has used ransomware variants requiring a key passed on the command line for the malware to execute. [11] |
| S1180 | BlackByte Ransomware | BlackByte Ransomware creates a mutex value with a hard-coded name, and terminates if that mutex already exists on the victim system. BlackByte Ransomware checks the system language to see if it matches one of a list of hard-coded values; if a match is found, the malware will terminate. [12] |
| S1184 | BOLDMOVE | BOLDMOVE verifies it is executing from a specific path during execution. [13] |
| S0635 | BoomBox | BoomBox can check its current working directory and for the presence of a specific file and terminate if specific values are not found. [14] |
| S1161 | BPFDoor | BPFDoor creates a zero byte PID file at /var/run/haldrund.pid . BPFDoor uses this file to determine if it is already running on a system to ensure only one instance is executing at a time. [15] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP can execute a task which leads to execution if it finds a process name containing "creensaver." [16] |
| G1052 | Contagious Interview | Contagious Interview has configured C2 endpoints to review IP geolocation, request headers, victim environment details and runtime conditions prior to delivering payloads. [17] |
| S1111 | DarkGate | DarkGate uses per-victim links for hosting malicious archives, such as ZIP files, in services such as SharePoint to prevent other entities from retrieving them. [18] |
| S1052 | DEADEYE | DEADEYE can ensure it executes only on intended systems by identifying the victim's volume serial number, hostname, and/or DNS domain. [19] |
| S0634 | EnvyScout | EnvyScout can call window.location.pathname to ensure that embedded files are being executed from the C: drive, and will terminate if they are not. [14] |
| S9003 | evilginx2 | evilginx2 can reject requests to phishing URLs if the User-Agent of the visitor doesn't match the allowlist REGEX filter for a specific lure. [20] |
| S1179 | Exbyte | Exbyte checks for the presence of a configuration file before completing execution. [21] |
| G0047 | Gamaredon Group | Gamaredon Group has used geoblocking to limit downloads of the malicious file to specific geographic locations. [22] [23] |
| S9010 | GlassWorm | GlassWorm has utilized logic to avoid executing on Russian based devices. [24] |
| S9023 | HiddenFace | HiddenFace can check for the presence of specific analysis tools and will terminate itself if they are found. [25] |
| S9039 | LazyWiper | LazyWiper can halt execution if [System.Net.Dns]::GetHostName() or $env:COMPUTERNAME contains "pe-dc" . [26] |
| S1185 | LightSpy | On macOS, LightSpy checks the existence of a process identification number (PID) file, /Users/Shared/irc.pid , to verify if LightSpy is currently running. [27] |
| S1199 | LockBit 2.0 | LockBit 2.0 will not execute on hosts where the system language is set to a language spoken in the Commonwealth of Independent States region. [28] [29] |
| S1202 | LockBit 3.0 | LockBit 3.0 can make execution dependent on specific parameters including a unique passphrase and the system language of the targeted host not being found on a set exclusion list. [30] [31] [32] |
| S9020 | LODEINFO | LODEINFO can halt execution if the "en_US" locale is identified on a victim's machine. [33] |
| S1143 | LunarLoader | LunarLoader can use the DNS domain name of a compromised host to create a decryption key to ensure a malicious payload can only execute against the intended targets. [34] |
| S0637 | NativeZone | NativeZone can check for the presence of KM.EkeyAlmaz1C.dll and will halt execution unless it is in the same directory as the rest of the malware's components. [14] [35] |
| S9019 | PureCrypter | PureCrypter code contains an ExclusionRegionNames option where it can compare the results of kernel32!GetGeoInfo with a list of regions. [36] |
| S1242 | Qilin | Qilin can require a specific password to be passed by command-line argument during execution which must match a pre-defined value in the configuration in order for it to continue execution. [37] [38] |
| S1212 | RansomHub | RansomHub will terminate without proceeding to encryption if the infected machine is on a list of allowlisted machines specified in its configuration. [39] |
| S1130 | Raspberry Robin | Raspberry Robin will check for the presence of several security products on victim machines and will avoid UAC bypass mechanisms if they are identified. [40] Raspberry Robin can use specific cookie values in HTTP requests to command and control infrastructure to validate that requests for second stage payloads originate from the initial downloader script. [41] |
| C0047 | RedDelta Modified PlugX Infection Chain Operations | Mustang Panda included the use of Cloudflare geofencing mechanisms to limit payload download activity during RedDelta Modified PlugX Infection Chain Operations . [42] |
| S1240 | RedLine Stealer | RedLine Stealer has built in settings to not operate based on geolocation or country of the victim host. [43] [44] |
| S1150 | ROADSWEEP | ROADSWEEP requires four command line arguments to execute correctly, otherwise it will produce a message box and halt execution. [16] [45] [46] |
| S9026 | ROAMINGHOUSE | ROAMINGHOUSE can change its execution method to create a batch file in the startup folder that executes a legitimate executable if a McAfee product is detected. [47] |
| S1210 | Sagerunex | Sagerunex uses a "servicemain" function to verify its environment to ensure it can only be executed as a service, as well as the existence of a configuration file in a specified directory. [48] |
| S1178 | ShrinkLocker | ShrinkLocker will exit its "main" function if the victim domain name does not match provided criteria. [49] |
| S1035 | Small Sieve | Small Sieve can only execute correctly if the word Platypus is passed to it on the command line. [50] |
| S1200 | StealBit | StealBit will execute an empty infinite loop if it detects it is being run in the context of a debugger. [51] |
| S1183 | StrelaStealer | StrelaStealer variants only execute if the keyboard layout or language matches a set list of variables. [52] [53] |
| S0603 | Stuxnet | Stuxnet checks for specific operating systems on 32-bit machines, Registry keys, and dates for vulnerabilities, and will exit execution if the values are not met. [54] |
| S0562 | SUNSPOT | SUNSPOT only replaces SolarWinds Orion source code if the MD5 checksums of both the original source code file and backdoored replacement source code match hardcoded values. [55] |
| S9001 | SystemBC | SystemBC has checked if the last characters of DNS server names end in .bit before initializing C2 communication. [56] SystemBC has identified running processes associated with anti-virus solutions to include a2guard.exe to determine whether it executes or not. [57] |
| S1239 | TONESHELL | TONESHELL has an exception handler that executes when ESET antivirus applications ekrn.exe and egui.exe are not found and directly injects its code into waitfor.exe using Native Windows API including WriteProcessMemory and CreateRemoteThreadEx . [58] |
| S0678 | Torisma | Torisma is only delivered to a compromised host if the victim's IP address is on an allow-list. [59] |
| S9034 | Tsundere Botnet | Tsundere Botnet has checked the victim machine’s location to avoid infecting in the Commonwealth of Independent States (CIS) region. [60] |
| S0636 | VaporRage | VaporRage has the ability to check for the presence of a specific DLL and terminate if it is not found. [14] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1055 | Do Not Mitigate | Execution Guardrails likely should not be mitigated with preventative controls because it may protect unintended targets from being compromised. If targeted, efforts should be focused on preventing adversary tools from running earlier in the chain of activity and on identifying subsequent malicious behavior if compromised. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0562 | Multi-Platform Execution Guardrails Environmental Validation Detection Strategy | AN1551 | Windows environmental validation behavioral chain: (1) Rapid system discovery reconnaissance through WMI queries, registry enumeration, and network share discovery, (2) Environment-specific artifact collection (hostname, domain, IP addresses, installed software, hardware identifiers), (3) Cryptographic operations or conditional logic based on collected environmental values, (4) Selective payload execution contingent on environmental validation results, (5) Temporal correlation between discovery activities and subsequent execution or network communication |
| AN1552 | Linux environmental validation behavioral chain: (1) Intensive system enumeration through command execution (uname, hostname, ifconfig, lsblk, mount), (2) File system reconnaissance targeting specific paths, network configurations, and installed packages, (3) Process and user enumeration to validate target environment characteristics, (4) Conditional script execution or binary activation based on environmental criteria, (5) Network connectivity validation and external IP address resolution for geolocation verification |  |  |
| AN1553 | macOS environmental validation behavioral chain: (1) System profiling through system_profiler, sysctl, and hardware discovery commands, (2) Network interface and configuration enumeration for geolocation and network environment validation, (3) Application installation and version discovery for software environment fingerprinting, (4) Security feature detection (SIP, Gatekeeper, XProtect status), (5) Conditional payload execution based on macOS-specific environmental criteria and System Integrity Protection bypass validation |  |  |
| AN1554 | ESXi hypervisor environmental validation behavioral chain: (1) Virtual machine inventory and configuration enumeration through vim-cmd and esxcli commands, (2) Host hardware and network configuration discovery for hypervisor environment validation, (3) Datastore and storage configuration reconnaissance, (4) vCenter connectivity and cluster membership validation, (5) Selective malware deployment based on virtualization infrastructure characteristics and target VM validation |  |  |

---

## References

- [Shoorbajee, Z. (2018, June 1). Playing nice? FireEye CEO says U.S. malware is more restrained than adversaries'. Retrieved January 17, 2019.](https://www.cyberscoop.com/kevin-mandia-fireeye-u-s-malware-nice/)
- [McWhirt, M., Carr, N., Bienstock, D. (2019, December 4). Breaking the Rules: A Tough Outlook for Home Page Attacks (CVE-2017-11774). Retrieved June 23, 2020.](https://www.fireeye.com/blog/threat-research/2019/12/breaking-the-rules-tough-outlook-for-home-page-attacks.html)
- [Pham Duy Phuc, John Fokker J.E., Alejandro Houspanossian and Mathanraj Thangaraju. (2023, March 7). Qakbot Evolves to OneNote Malware Distribution. Retrieved June 7, 2024.](https://www.trellix.com/blogs/research/qakbot-evolves-to-onenote-malware-distribution/)
- [Nutland, J. and Szeliga, M. (2024, October 21). Akira ransomware continues to evolve. Retrieved December 10, 2024.](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [Global Research & Analysis Team, Kaspersky. (2024, August 19). BlindEagle flying high in Latin America. Retrieved April 16, 2026.](https://securelist.com/blindeagle-apt/113414/)
- [Insikt Group. (2025, August 26). TAG-144’s Persistent Grip on South American Organizations. Retrieved April 16, 2026.](https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0826.pdf)
- [Frankoff, S., Hartley, B. (2018, November 14). Big Game Hunting: The Evolution of INDRIK SPIDER From Dridex Wire Fraud to BitPaymer Targeted Ransomware. Retrieved January 6, 2021.](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
- [Huseyin Can Yuceel. (2022, February 21). TTPs used by BlackByte Ransomware Targeting Critical Infrastructure. Retrieved December 16, 2024.](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)
- [James Nutland, Craig Jackson, Terryn Valikodath, & Brennan Evans. (2024, August 28). BlackByte blends tried-and-true tradecraft with newly disclosed vulnerabilities to support ongoing attacks. Retrieved December 16, 2024.](https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [Scott Henderson, Cristiana Kittner, Sarah Hawley & Mark Lechtik, Google Cloud. (2023, January 19). Suspected Chinese Threat Actors Exploiting FortiOS Vulnerability (CVE-2022-42475). Retrieved December 31, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
- [MSTIC. (2021, May 28). Breaking down NOBELIUM’s latest early-stage toolset. Retrieved August 4, 2021.](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
- [The Sandfly Security Team. (2022, May 11). BPFDoor - An Evasive Linux Backdoor Technical Analysis. Retrieved September 29, 2023.](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Ernesto Fernández Provecho, Pham Duy Phuc, Ciana Driscoll & Vinoo Thomas. (2023, November 21). The Continued Evolution of the DarkGate Malware-as-a-Service. Retrieved February 9, 2024.](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Gretzky, K. (2020, September 14). Evilginx 2.4 - Gone Phishing. Retrieved January 27, 2026.](https://breakdev.org/evilginx-2-4-gone-phishing/)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [Unit 42. (2022, December 20). Russia’s Trident Ursa (aka Gamaredon APT) Cyber Conflict Operations Unwavering Since Invasion of Ukraine. Retrieved September 12, 2024.](https://unit42.paloaltonetworks.com/trident-ursa/)
- [Venere, G. (2025, March 28). Gamaredon campaign abuses LNK files to distribute Remcos backdoor. Retrieved July 23, 2025.](https://blog.talosintelligence.com/gamaredon-campaign-distribute-remcos/)
- [Kirill Boychenko. (2026, January 31). GlassWorm Loader Hits Open VSX via Developer Account Compromise. Retrieved April 10, 2026.](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Stuart Ashenbrenner, Alden Schmidt. (2024, April 25). LightSpy Malware Variant Targeting macOS. Retrieved January 3, 2025.](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
- [FBI. (2022, February 4). Indicators of Compromise Associated with LockBit 2.0 Ransomware. Retrieved January 24, 2025.](https://www.ic3.gov/CSA/2022/220204.pdf)
- [Elsad, A. et al. (2022, June 9). LockBit 2.0: How This RaaS Operates and How to Protect Against It. Retrieved January 24, 2025.](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
- [CISA et al. (2023, June 14). UNDERSTANDING RANSOMWARE THREAT ACTORS: LOCKBIT. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)
- [Walter, J. (2022, July 21). LockBit 3.0 Update | Unpicking the Ransomware’s Latest Anti-Analysis and Evasion Techniques. Retrieved February 5, 2025.](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part II. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [Guerrero-Saade, J. (2021, June 1). NobleBaron | New Poisoned Installers Could Be Used In Supply Chain Attacks. Retrieved August 4, 2021.](https://labs.sentinelone.com/noblebaron-new-poisoned-installers-could-be-used-in-supply-chain-attacks/)
- [Dumont, R. (2022, June 13). Technical Analysis of PureCrypter: A Fully-Functional Loader Distributing Remote Access Trojans and Information Stealers. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
- [Hacioglu, S. (2025, March 10). Qilin Ransomware: Exposing the TTPs Behind One of the Most Active Ransomware Campaigns of 2024. Retrieved September 26, 2025.](https://www.picussecurity.com/resource/blog/qilin-ransomware)
- [Trend Micro. (2025, October 23). Agenda Ransomware Deploys Linux Variant on Windows Systems Through Remote Management Tools and BYOVD Techniques. Retrieved March 26, 2026.](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)
- [Alfano, V. et al. (2025, February 12). RansomHub Never Sleeps Episode 1: The evolution of modern ransomware. Retrieved March 17, 2025.](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
- [Christopher So. (2022, December 20). Raspberry Robin Malware Targets Telecom, Governments. Retrieved May 17, 2024.](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
- [Patrick Schläpfer . (2024, April 10). Raspberry Robin Now Spreading Through Windows Script Files. Retrieved May 17, 2024.](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
- [Insikt Group. (2025, January 9). Chinese State-Sponsored RedDelta Targeted Taiwan, Mongolia, and Southeast Asia with Adapted PlugX Infection Chain. Retrieved January 14, 2025.](https://go.recordedfuture.com/hubfs/reports/cta-cn-2025-0109.pdf)
- [Alexandre Cote Cyr. (2024, November 8). Life on a crooked RedLine: Analyzing the infamous infostealer’s backend. Retrieved September 17, 2025.](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)
- [Proofpoint Threat Insight Team, Jeremy H, Axel F. (2020, March 16). New Redline Password Stealer Malware. Retrieved September 17, 2025.](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
- [CISA. (2022, September 23). AA22-264A Iranian State Actors Conduct Cyber Operations Against the Government of Albania. Retrieved August 6, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
- [MSTIC. (2022, September 8). Microsoft investigates Iranian attacks against the Albanian government. Retrieved August 6, 2024.](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)
- [Hiroaki, H. (2025, April 30). Earth Kasha Updates TTPs in Latest Campaign Targeting Taiwan and Japan. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [Splunk Threat Research Team , Teoderick Contreras. (2024, September 5). ShrinkLocker Malware: Abusing BitLocker to Lock Your Data. Retrieved December 7, 2024.](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
- [NCSC GCHQ. (2022, January 27). Small Sieve Malware Analysis Report. Retrieved August 22, 2022.](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)
- [Cybereason Global SOC Team. (n.d.). THREAT ANALYSIS REPORT: Inside the LockBit Arsenal - The StealBit Exfiltration Tool. Retrieved January 29, 2025.](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
- [Fortgale. (2023, September 18). StrelaStealer Malware Analysis. Retrieved December 31, 2024.](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)
- [Golo Mühr, Joe Fasulo & Charlotte Hammond, IBM X-Force. (2024, November 12). Strela Stealer: Today’s invoice is tomorrow’s phish. Retrieved December 31, 2024.](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [CrowdStrike Intelligence Team. (2021, January 11). SUNSPOT: An Implant in the Build Process. Retrieved January 11, 2021.](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
- [Harmon, K., et al. (2019, August 1). SystemBC is like Christmas in July for SOCKS5 Malware and Exploit Kits . Retrieved June 13, 2025.](https://www.proofpoint.com/us/threat-insight/post/systembc-christmas-july-socks5-malware-and-exploit-kits)
- [Gallagher, S., Gn, S. (2020, December 16). Ransomware operators use SystemBC RAT as off-the-shelf Tor backdoor. Retrieved May 16, 2025.](https://news.sophos.com/en-us/2020/12/16/systembc/)
- [Nathaniel Morales, Nick Dai. (2025, February 18). Earth Preta Mixes Legitimate and Malicious Components to Sidestep Detection. Retrieved September 10, 2025.](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
- [Beek, C. (2020, November 5). Operation North Star: Behind The Scenes. Retrieved December 20, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
- [Ubiedo, L. (2025, November 20). Blockchain and Node.js abused by Tsundere: an emerging botnet. Retrieved April 6, 2026.](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)

---

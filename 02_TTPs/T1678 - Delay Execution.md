# Delay Execution

## Description

Adversaries may employ various time-based methods to evade detection and analysis. These techniques often exploit system clocks, delays, or timing mechanisms to obscure malicious activity, blend in with benign activity, and avoid scrutiny. Adversaries can perform this behavior within virtualization/sandbox environments or natively on host systems.

Adversaries may utilize programmatic sleep commands or native system scheduling functionality, for example Scheduled Task/Job . Benign commands or other operations may also be used to delay malware execution or ensure prior commands have had time to execute properly. Loops or otherwise needless repetitions of commands, such as ping , may be used to delay malware execution and potentially exceed time thresholds of automated analysis environments. [1] [2] Another variation, commonly referred to as API hammering, involves making various calls to Native API functions in order to delay execution (while also potentially overloading analysis environments with junk data). [3] [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0057 | 3CX Supply Chain Attack | During the 3CX Supply Chain Attack , AppleJeus 's software generates a randomly selected date that is between 1-4 weeks in the future. This timestamp is then checked against the current time of the compromised machine, and the malware will sleep until that time is encountered. [5] |
| S9031 | AshTag | AshTag can use a set sleep time to delay C2 beaconing. [6] |
| S9015 | BRICKSTORM | BRICKSTORM has embedded delayed-start logic that attempts to circumvent detection for long-term persistence. [7] [8] BRICKSTORM has been observed configured with a "delay" timer built-in that waited for a hard-coded date months in the future before beginning to beacon to the configured C2 domain. [9] |
| S9038 | DynoWiper | DynoWiper has utilized a five-second delay using Sleep(5000) between two of the three phases of the attack that involves file overwriting, file deletion, and system reboot. [10] [11] |
| S9033 | Fooder | Fooder has used a custom delay function ( delayExecution(integer) ) and Sleep API calls ( Sleep(integer) ) to slow code execution. [12] |
| S9010 | GlassWorm | GlassWorm has used a timeout function set to 9e5 which delays execution 900,000 milliseconds or 15 minutes to avoid detection. [13] |
| S1230 | HIUPAN | HIUPAN has used a config file "$.ini" to store a sleep multiplier to execute at a set interval value prior to initiating a watcher function that checks for a specific running process, that checks for removable drives and installs itself and supporting files if one is available. [14] [15] |
| G0094 | Kimsuky | Kimsuky has utilized the Sleep function to ensure execution of scripts. [16] [17] |
| S9032 | MuddyViper | MuddyViper has the ability to sleep for a certain amount of time, with the default being one minute. [12] |
| G0129 | Mustang Panda | Mustang Panda has delayed the execution of payloads leveraging ping echo requests cmd /c ping 8.8.8.8 -n 70&&"%temp%\<legitimate executable>" . [18] [19] |
| S9014 | PHASEJAM | PHASEJAM has used the sleep command within its code to generate a fake HTML upgrade progress bar that mimics a running process. [20] |
| S9019 | PureCrypter | PureCrypter has the ability to delay for a specified number of seconds before execution. [21] |
| S1242 | Qilin | Qilin has the ability to delay execution. [22] |
| S9037 | RustyWater | RustyWater has generated random sleep intervals between C2 communication. [23] |
| S9008 | Shai-Hulud | Shai-Hulud has delayed execution of its larger payloads by forking itself into background process. [24] |
| S9024 | SPAWNCHIMERA | SPAWNCHIMERA has used delayed execution to pause for a defined interval before performing environment discovery, repeatedly checking for specific processes, such as the dslogserver process, prior to continuing execution. [25] |
| S9001 | SystemBC | SystemBC has leveraged the Sleep functions before and after commands to ensure execution using the hexadecimal values within commands to include Sleep(0x2710u) that waits 10 seconds, and Sleep(0xEA60u) for 60 seconds. [26] |
| S1239 | TONESHELL | TONESHELL has the ability to pause operations for a specified duration prior to follow-on execution of activities. [27] |
| S0275 | UPPERCUT | UPPERCUT can use a sleep function to delay execution. [28] [29] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0372 | Multi-Platform Detection Strategy for T1678 - Delay Execution | AN1048 | Correlated use of sleep/delay mechanisms (e.g., kernel32!Sleep, NTDLL APIs) in short-lived processes, combined with parent processes invoking suspicious scripts (e.g., wscript, powershell) with minimal user interaction. |
| AN1049 | Shell scripts or binaries invoking repeated 'sleep', 'ping', or low-level syscalls (e.g., nanosleep) in short-lived execution chains with no user or system interaction. Frequently seen in malicious cron jobs or payload stagers. |  |  |
| AN1050 | Execution of AppleScript, bash, or launchd jobs that invoke delay functions (e.g., sleep, delay in AppleScript) with limited parent interaction and staged follow-on commands. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0372 | Multi-Platform Detection Strategy for T1678 - Delay Execution | AN1048 | Correlated use of sleep/delay mechanisms (e.g., kernel32!Sleep, NTDLL APIs) in short-lived processes, combined with parent processes invoking suspicious scripts (e.g., wscript, powershell) with minimal user interaction. |
| AN1049 | Shell scripts or binaries invoking repeated 'sleep', 'ping', or low-level syscalls (e.g., nanosleep) in short-lived execution chains with no user or system interaction. Frequently seen in malicious cron jobs or payload stagers. |  |  |
| AN1050 | Execution of AppleScript, bash, or launchd jobs that invoke delay functions (e.g., sleep, delay in AppleScript) with limited parent interaction and staged follow-on commands. |  |  |

---

## References

- [Loman, M. et al. (2021, July 4). Independence Day: REvil uses supply chain exploit to attack hundreds of businesses. Retrieved September 30, 2021.](https://news.sophos.com/en-us/2021/07/04/independence-day-revil-uses-supply-chain-exploit-to-attack-hundreds-of-businesses/)
- [Malik, A. (2016, October 14). Nitol Botnet makes a resurgence with evasive sandbox analysis technique. Retrieved September 30, 2021.](https://www.netskope.com/blog/nitol-botnet-makes-resurgence-evasive-sandbox-analysis-technique)
- [Joe Security. (2016, April 21). Nymaim - evading Sandboxes with API hammering. Retrieved September 30, 2021.](https://www.joesecurity.org/blog/3660886847485093803)
- [Joe Security. (2020, July 13). TrickBot's new API-Hammering explained. Retrieved September 30, 2021.](https://www.joesecurity.org/blog/498839998833561473)
- [Robert Falcone, Josh Grunzweig. (2023, March 30). Threat Brief: 3CXDesktopApp Supply Chain Attack. Retrieved September 15, 2025.](https://unit42.paloaltonetworks.com/3cxdesktopapp-supply-chain-attack/)
- [Unit 42. (2025, December 11). Hamas-Affiliated Ashen Lepus Targets Middle Eastern Diplomatic Entities With New AshTag Malware Suite. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
- [Huseyin Can Yuceel. (2025, October 1). BRICKSTORM Malware: UNC5221 Targets Tech and Legal Sectors in the United States. Retrieved April 16, 2026.](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)
- [NVISO Incident Response. (2025, April 1). BRICKSTORM Backdoor Analysis: A Persistent Espionage Threat to European Industries. Retrieved April 16, 2026.](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)
- [Sarah Yoder, John Wolfram, Ashley Pearson, Doug Bienstock, Josh Madeley, Josh Murchie, Brad Slaybaugh, Matt Lin, Geoff Carstairs, Austin Larsen. (2025, September 24). Another BRICKSTORM: Stealthy Backdoor Enabling Espionage into Tech and Legal Sectors. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [ESET. (2026, January 30). DynoWiper update: Technical analysis and attribution. Retrieved April 22, 2026.](https://www.welivesecurity.com/en/eset-research/dynowiper-update-technical-analysis-attribution/)
- [ESET Research. (2025, December 2). MuddyWater: Snakes by the riverbank. Retrieved February 17, 2026.](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
- [Gal Hachamov. (2025, December 29). GlassWorm Goes Mac: Fresh Infrastructure, New Tricks. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Alexndru-Cristian Bardas. (2025, October 30). DPRK’s Playbook: Kimsuky’s HttpTroy and Lazarus’s New BLINDINGCAN Variant. Retrieved April 8, 2026.](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Secureworks Counter Threat Unit Research Team. (2022, April 27). BRONZE PRESIDENT Targets Russian Speakers with Updated PlugX. Retrieved September 9, 2025.](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)
- [John Wolfram, Josh Murchie, Matt Lin, Daniel Ainsworth, Robert Wallace, Dimiter Andonov, Dhanesh Kizhakkinan, Jacob Thompson. (2025, January 8). Ivanti Connect Secure VPN Targeted in New Zero-Day Exploitation. Retrieved April 14, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
- [Dumont, R. (2022, June 13). Technical Analysis of PureCrypter: A Fully-Functional Loader Distributing Remote Access Trojans and Information Stealers. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
- [Trend Micro. (2025, October 23). Agenda Ransomware Deploys Linux Variant on Windows Systems Through Remote Management Tools and BYOVD Techniques. Retrieved March 26, 2026.](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)
- [Awasthi, P. (2026, January 8). Reborn in Rust: Muddy Water Evolves Tooling with RustyWater Implant. Retrieved March 19, 2026.](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
- [Justin Moore. (2025, November 25). "Shai-Hulud" Worm Compromises npm Ecosystem in Supply Chain Attack (Updated November 26). Retrieved April 9, 2026.](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
- [DHS/CISA. (2026, February 26). MAR-25993211-r1.v2 Ivanti Connect Secure (RESURGE): AR25-087A. Retrieved April 17, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
- [Gallagher, S., Gn, S. (2020, December 16). Ransomware operators use SystemBC RAT as off-the-shelf Tor backdoor. Retrieved May 16, 2025.](https://news.sophos.com/en-us/2020/12/16/systembc/)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: ToneShell and StarProxy | P1. Retrieved July 21, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
- [Hiroaki, H. (2025, April 30). Earth Kasha Updates TTPs in Latest Campaign Targeting Taiwan and Japan. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
- [Hiroaki, H. (2024, November 26). Guess Who’s Back - The Return of ANEL in the Recent Earth Kasha Spear-phishing Campaign in 2024. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)

---

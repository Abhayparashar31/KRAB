# System Time Discovery

## Description

An adversary may gather the system time and/or time zone settings from a local or remote system. The system time is set and stored by services, such as the Windows Time Service on Windows or systemsetup on macOS. [1] [2] [3] These time settings may also be synchronized between systems and services in an enterprise network, typically accomplished with a network time server within a domain. [4] [5]

System time information may be gathered in a number of ways, such as with Net on Windows by performing net time \hostname to gather the system time on a remote system. The victim's time zone may also be inferred from the current system time or gathered by using w32tm /tz . [2] In addition, adversaries can discover device uptime through functions such as GetTickCount() to determine how long it has been since the system booted up. [6]

On network devices, Network Device CLI commands such as show clock detail can be used to see the current time configuration. [7] On ESXi servers, esxcli system clock get can be used for the same purpose.

In addition, system calls – such as time() – have been used to collect the current time on Linux devices. [8] On macOS systems, adversaries may use commands such as systemsetup -gettimezone or timeIntervalSinceNow to gather current time zone information or current date and time. [9] [10]

This information could be useful for performing other techniques, such as executing a file with a Scheduled Task/Job [11] , or to discover locality information based on time zone to assist in victim targeting (i.e. System Location Discovery ). Adversaries may also use knowledge of system time as part of a time bomb, or delaying execution until a specified date/time. [12]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0331 | Agent Tesla | Agent Tesla can collect the timestamp from the victim’s machine. [13] |
| S0622 | AppleSeed | AppleSeed can pull a timestamp from the victim's machine. [14] |
| S0373 | Astaroth | Astaroth collects the timestamp from the infected machine. [15] |
| S1087 | AsyncRAT | AsyncRAT can check whether the current system hour and day of the week are within operating hours defined it its configuration. [16] |
| S1053 | AvosLocker | AvosLocker has checked the system time before and after encryption. [17] |
| S0344 | Azorult | Azorult can collect the time zone information from the system. [18] [19] |
| S1081 | BADHATCH | BADHATCH can obtain the DATETIME and UPTIME from a compromised machine. [20] |
| S0534 | Bazar | Bazar can collect the time on the compromised host. [21] [22] |
| S1246 | BeaverTail | BeaverTail has obtained and sent the current timestamp associated with the victim device to C2. [23] |
| S0574 | BendyBear | BendyBear has the ability to determine local time on a compromised host. [24] |
| S0017 | BISCUIT | BISCUIT has a command to collect the system UPTIME . [25] |
| S0268 | Bisonal | Bisonal can check the system time set on the infected host. [26] |
| S0657 | BLUELIGHT | BLUELIGHT can collect the local time on a compromised host. [27] |
| G0060 | BRONZE BUTLER | BRONZE BUTLER has used net time to check the local time on a target system. [28] |
| S0471 | build_downer | build_downer has the ability to determine the local time to ensure malware installation only happens during the hours that the infected system is active. [29] |
| C0015 | C0015 | During C0015 , the threat actors used the command net view /all time to gather the local time of a compromised network. [30] |
| S0351 | Cannon | Cannon can collect the current time zone information from the victim’s machine. [31] |
| S0335 | Carbon | Carbon uses the command net time \127.0.0.1 to get information the system’s time. [32] |
| S1043 | ccf32 | ccf32 can determine the local time on targeted machines. [33] |
| G0114 | Chimera | Chimera has used time /t and net time \ip/hostname for system time discovery. [34] |
| S0660 | Clambling | Clambling can determine the current time. [35] |
| S0126 | ComRAT | ComRAT has checked the victim system's date and time to perform tasks during business hours (9 to 5, Monday to Friday). [36] |
| S0608 | Conficker | Conficker uses the current UTC victim system date for domain generation and connects to time servers to determine the current date. [37] [38] |
| S0115 | Crimson | Crimson has the ability to determine the date and time on a compromised host. [39] |
| G1012 | CURIUM | CURIUM deployed mechanisms to check system time information following strategic website compromise attacks. [40] |
| S1111 | DarkGate | DarkGate creates a log file for capturing keylogging, clipboard, and related data using the victim host's current date for the filename. [41] DarkGate queries victim system epoch time during execution. [41] DarkGate captures system time information as part of automated profiling on initial installation. [42] |
| G0012 | Darkhotel | Darkhotel malware can obtain system time from a compromised host. [43] |
| S0673 | DarkWatchman | DarkWatchman can collect time zone information and system UPTIME . [44] |
| S1033 | DCSrv | DCSrv can compare the current time on an infected host with a configuration value to determine when to start the encryption process. [45] |
| S1134 | DEADWOOD | DEADWOOD will set a timestamp value to determine when wiping functionality starts. When the timestamp is met on the system, a trigger file is created on the operating system allowing for execution to proceed. If the timestamp is in the past, the wiper will execute immediately. [46] |
| S0694 | DRATzarus | DRATzarus can use the GetTickCount and GetSystemTimeAsFileTime API calls to inspect system time. [47] |
| S1159 | DUSTTRAP | DUSTTRAP reads the infected system's current time and writes it to a log file during execution. [48] |
| S0554 | Egregor | Egregor contains functionality to query the local/system time. [49] |
| S0091 | Epic | Epic uses the net time command to get the system time from the machine and collect the current date and time zone information. [50] |
| S0396 | EvilBunny | EvilBunny has used the API calls NtQuerySystemTime, GetSystemTimeAsFileTime, and GetTickCount to gather time metrics as part of its checks to see if the malware is running in a sandbox. [51] |
| S0267 | FELIXROOT | FELIXROOT gathers the time zone information from the victim’s machine. [52] |
| G0046 | FIN7 | FIN7 has used the PowerShell script 3CF9.ps1 to execute net time . [53] |
| S1044 | FunnyDream | FunnyDream can check system time to help determine when changes were made to specified files. [33] |
| S9010 | GlassWorm | GlassWorm has the ability to check the system’s time zone on the victim device. [54] |
| S0588 | GoldMax | GoldMax can check the current date-time value of the compromised system, comparing it to the hardcoded execution trigger and can send the current timestamp to the C2 server. [55] [56] |
| S0531 | Grandoreiro | Grandoreiro can determine the time on the victim machine via IPinfo. [57] |
| S0237 | GravityRAT | GravityRAT can obtain the date and time of a system. [58] |
| S0690 | Green Lambert | Green Lambert can collect the date and time from a compromised host. [59] [60] |
| S0417 | GRIFFON | GRIFFON has used a reconnaissance module that can be used to retrieve the date and time of the system. [61] |
| G0126 | Higaisa | Higaisa used a function to gather the current time. [62] |
| S0376 | HOPLIGHT | HOPLIGHT has been observed collecting system time from victim machines. [63] |
| S0260 | InvisiMole | InvisiMole gathers the local system time from the victim’s machine. [64] [65] |
| S1051 | KEYPLUG | KEYPLUG can obtain the current tick count of an infected computer. [66] |
| G0094 | Kimsuky | Kimsuky has gathered the system time of the device using the PowerShell cmdlet Get-Date . [67] |
| G0032 | Lazarus Group | A Destover-like implant used by Lazarus Group can obtain the current system time and send it to the C2 server. [68] |
| S9020 | LODEINFO | LODEINFO can capture system time to send to the C2. [69] |
| S1244 | Medusa Ransomware | Medusa Ransomware has discovered device uptime through GetTickCount() . [70] |
| S0455 | Metamorfo | Metamorfo uses JavaScript to get the system time. [71] |
| S0149 | MoonWind | MoonWind obtains the victim's current time. [72] |
| S0039 | Net | The net time command can be used in Net to determine the local or remote system time. [73] |
| S1147 | Nightdoor | Nightdoor can identify the system local time information. [74] |
| S0353 | NOKKI | NOKKI can collect the current timestamp of the victim's machine. [75] |
| S0439 | Okrum | Okrum can obtain the date and time of the compromised system. [76] |
| S0264 | OopsIE | OopsIE checks to see if the system is configured with "Daylight" time and checks for a specific region to be set for the timezone. [77] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors used the net time command as part of their advanced reconnaissance. [78] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors used the time command to retrieve the current time of a compromised system. [79] |
| S1233 | PAKLOG | PAKLOG has collected a timestamp to log the precise time a key was pressed, formatted as %Y-%m-%d %H:%M:%S. [80] |
| S0501 | PipeMon | PipeMon can send time zone information from a compromised host to C2. [81] |
| S0013 | PlugX | PlugX has identified system time through its GetSystemInfo command. [82] |
| S0139 | PowerDuke | PowerDuke has commands to get the time the machine was built, the time, and the time zone. [83] |
| S0238 | Proxysvc | As part of the data reconnaissance phase, Proxysvc grabs the system time to send back to the control server. [68] |
| S1228 | PUBLOAD | PUBLOAD has collected the machine’s tick count through the use of GetTickCount . [84] |
| S0650 | QakBot | QakBot can identify the system time on a targeted host. [85] |
| S1148 | Raccoon Stealer | Raccoon Stealer gathers victim machine timezone information. [86] [87] |
| S0148 | RTM | RTM can obtain the victim time zone. [88] |
| S0596 | ShadowPad | ShadowPad has collected the current date and time of the victim system. [89] |
| S0140 | Shamoon | Shamoon obtains the system time and will only activate if it is greater than a preset date. [90] [91] |
| S0450 | SHARPSTATS | SHARPSTATS has the ability to identify the current date and time on the compromised host. [92] |
| S1178 | ShrinkLocker | ShrinkLocker retrieves a system timestamp that is used in generating an encryption key. [93] |
| G0121 | Sidewinder | Sidewinder has used tools to obtain the current system time. [94] |
| S0692 | SILENTTRINITY | SILENTTRINITY can collect start time information from a compromised host. [95] |
| S0615 | SombRAT | SombRAT can execute getinfo to discover the current time on a compromised host. [96] [97] |
| S1227 | StarProxy | StarProxy has utilized the windows API call GetLocalTime() to retrieve a SystemTime structure to generate a seed value. [98] |
| S0380 | StoneDrill | StoneDrill can obtain the current date and time of the victim machine. [99] |
| S1034 | StrifeWater | StrifeWater can collect the time zone from the victim's machine. [100] |
| S0603 | Stuxnet | Stuxnet collects the time and date of a system when it is infected. [101] |
| S0559 | SUNBURST | SUNBURST collected device UPTIME . [102] [103] |
| S1064 | SVCReady | SVCReady can collect time zone information. [104] |
| S9001 | SystemBC | SystemBC has leveraged the time of the device to create a text file with a filename that uses the function of uniqid(time()).‘.txt , consisting of the 10 character UNIX timestamp and 13 hexadecimal characters. [105] |
| S0098 | T9000 | T9000 gathers and beacons the system time during installation. [106] |
| S0011 | Taidoor | Taidoor can use GetLocalTime and GetSystemTime to collect system time. [107] |
| S0586 | TAINTEDSCRIBE | TAINTEDSCRIBE can execute GetLocalTime for time discovery. [108] |
| S0467 | TajMahal | TajMahal has the ability to determine local time on a compromised host. [109] |
| G0089 | The White Company | The White Company has checked the current date on the victim system. [110] |
| S0678 | Torisma | Torisma can collect the current time on a victim machine. [111] |
| G0010 | Turla | Turla surveys a system upon check-in to discover the system time by using the net time command. [50] |
| G1048 | UNC3886 | UNC3886 has used installation scripts to collect the system time on targeted ESXi hosts. [112] |
| S0275 | UPPERCUT | UPPERCUT has the capability to obtain the time zone information and the current timestamp of the victim’s machine. [113] |
| G1017 | Volt Typhoon | Volt Typhoon has obtained the victim's system timezone. [114] |
| S0466 | WindTail | WindTail has the ability to generate the current date and time. [115] |
| S0251 | Zebrocy | Zebrocy gathers the current time zone and date information from the system. [116] [117] |
| S0330 | Zeus Panda | Zeus Panda collects the current system time (UTC) and sends it back to the C2 server. [118] |
| G0128 | ZIRCONIUM | ZIRCONIUM has used a tool to capture the time on a compromised host in order to register it with C2. [119] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0151 | Behavior-chain, platform-aware detection strategy for T1124 System Time Discovery | AN0430 | Untrusted or unusual process/script (cmd.exe, powershell.exe, w32tm.exe, net.exe, custom binaries) queries system time/timezone (e.g., w32tm /tz, net time \host, Get-TimeZone, GetTickCount API) and (optionally) is followed within a short window by time-based scheduling or conditional execution (e.g., schtasks /create, at.exe, PowerShell Start-Sleep with large values). |
| AN0431 | A process (often spawned by a shell, interpreter, or malware implant) executes time discovery via commands (date, timedatectl, hwclock, cat /etc/timezone, /proc/uptime) or direct syscalls (time(), clock_gettime) and is (optionally) followed by scheduled task creation/modification (crontab, at) or conditional sleep logic. |  |  |
| AN0432 | Process/script execution of systemsetup -gettimezone, date, ioreg, or API usage (timeIntervalSinceNow, gettimeofday) followed by time-based scheduling (launchd plist modification) or sleep-based execution. |  |  |
| AN0433 | Interactive or remote shell/API invocation of esxcli system clock get or querying time parameters via hostd/vpxa shortly followed by time/ntp configuration checks or scheduled task creation, executed by non-standard accounts or outside maintenance windows. |  |  |
| AN0434 | Non-standard or rare users/locations issue CLI commands like "show clock detail" or "show timezone"; optionally followed by configuration of time/timezone or NTP sources. AAA/TACACS+ accounting and syslog correlate execution to identity, source IP, and privilege level. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0151 | Behavior-chain, platform-aware detection strategy for T1124 System Time Discovery | AN0430 | Untrusted or unusual process/script (cmd.exe, powershell.exe, w32tm.exe, net.exe, custom binaries) queries system time/timezone (e.g., w32tm /tz, net time \host, Get-TimeZone, GetTickCount API) and (optionally) is followed within a short window by time-based scheduling or conditional execution (e.g., schtasks /create, at.exe, PowerShell Start-Sleep with large values). |
| AN0431 | A process (often spawned by a shell, interpreter, or malware implant) executes time discovery via commands (date, timedatectl, hwclock, cat /etc/timezone, /proc/uptime) or direct syscalls (time(), clock_gettime) and is (optionally) followed by scheduled task creation/modification (crontab, at) or conditional sleep logic. |  |  |
| AN0432 | Process/script execution of systemsetup -gettimezone, date, ioreg, or API usage (timeIntervalSinceNow, gettimeofday) followed by time-based scheduling (launchd plist modification) or sleep-based execution. |  |  |
| AN0433 | Interactive or remote shell/API invocation of esxcli system clock get or querying time parameters via hostd/vpxa shortly followed by time/ntp configuration checks or scheduled task creation, executed by non-standard accounts or outside maintenance windows. |  |  |
| AN0434 | Non-standard or rare users/locations issue CLI commands like "show clock detail" or "show timezone"; optionally followed by configuration of time/timezone or NTP sources. AAA/TACACS+ accounting and syslog correlate execution to identity, source IP, and privilege level. |  |  |

---

## References

- [Microsoft. (n.d.). System Time. Retrieved November 25, 2016.](https://msdn.microsoft.com/ms724961.aspx)
- [Mathers, B. (2016, September 30). Windows Time Service Tools and Settings. Retrieved November 25, 2016.](https://technet.microsoft.com/windows-server-docs/identity/ad-ds/get-started/windows-time-service/windows-time-service-tools-and-settings)
- [Apple Support. (n.d.). About systemsetup in Remote Desktop. Retrieved March 27, 2024.](https://support.apple.com/en-gb/guide/remote-desktop/apd95406b8d/mac)
- [Cone, Matt. (2021, January 14). Synchronize your Mac's Clock with a Time Server. Retrieved March 27, 2024.](https://www.macinstruct.com/tutorials/synchronize-your-macs-clock-with-a-time-server/)
- [ArchLinux. (2024, February 1). System Time. Retrieved March 27, 2024.](https://wiki.archlinux.org/title/System_time)
- [YUCEEL, Huseyin Can. Picus Labs. (2022, June 9). Virtualization/Sandbox Evasion - How Attackers Avoid Malware Analysis. Retrieved December 26, 2023.](https://www.picussecurity.com/resource/virtualization/sandbox-evasion-how-attackers-avoid-malware-analysis)
- [Cisco. (2023, March 6). show clock detail - Cisco IOS Security Command Reference: Commands S to Z . Retrieved July 13, 2022.](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s2.html#wp1896741674)
- [Check Point Research. (2024, March 8). MAGNET GOBLIN TARGETS PUBLICLY FACING SERVERS USING 1-DAY VULNERABILITIES. Retrieved March 27, 2024.](https://research.checkpoint.com/2024/magnet-goblin-targets-publicly-facing-servers-using-1-day-vulnerabilities/)
- [YUCEEL, Huseyin Can. Picus Labs. (2022, June 9). The System Information Discovery Technique Explained - MITRE ATT&CK T1082. Retrieved March 27, 2024.](https://www.picussecurity.com/resource/the-system-information-discovery-technique-explained-mitre-attack-t1082)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Rivner, U., Schwartz, E. (2012). They’re Inside… Now What?. Retrieved November 25, 2016.](https://www.rsaconference.com/writable/presentations/file_upload/ht-209_rivner_schwartz.pdf)
- [Malicious History. (2020, September 17). Time Bombs: Malware With Delayed Execution. Retrieved April 22, 2021.](https://any.run/cybersecurity-blog/time-bombs-malware-with-delayed-execution/)
- [The DigiTrust Group. (2017, January 12). The Rise of Agent Tesla. Retrieved November 5, 2018.](https://www.digitrustgroup.com/agent-tesla-keylogger/)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [Doaty, J., Garrett, P.. (2018, September 10). We’re Seeing a Resurgence of the Demonic Astaroth WMIC Trojan. Retrieved September 25, 2024.](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)
- [Dominik Breitenbacher. (2025, March 18). Operation AkaiRyū: MirrorFace invites Europe to Expo 2025 and revives ANEL backdoor. Retrieved May 22, 2025.](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)
- [Hasherezade. (2021, July 23). AvosLocker enters the ransomware scene, asks for partners. Retrieved January 11, 2023.](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
- [Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
- [Proofpoint. (2018, July 30). New version of AZORult stealer improves loading features, spreads alongside ransomware in new campaign. Retrieved November 29, 2018.](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1, 2020.](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Harbison, M. (2021, February 9). BendyBear: Novel Chinese Shellcode Linked With Cyber Espionage Group BlackTech. Retrieved February 16, 2021.](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)
- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Zykov, K. (2020, August 13). CactusPete APT group’s updated Bisonal backdoor. Retrieved May 5, 2021.](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)
- [Cash, D., Grunzweig, J., Meltzer, M., Adair, S., Lancaster, T. (2021, August 17). North Korean APT InkySquid Infects Victims Using Browser Exploits. Retrieved September 30, 2021.](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
- [Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Falcone, R., Lee, B. (2018, November 20). Sofacy Continues Global Attacks and Wheels Out New ‘Cannon’ Trojan. Retrieved November 26, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
- [GovCERT. (2016, May 23). Technical Report about the Espionage Case at RUAG. Retrieved November 7, 2018.](https://web.archive.org/web/20170718174931/https://www.melani.admin.ch/dam/melani/de/dokumente/2016/technical%20report%20ruag.pdf.download.pdf/Report_Ruag-Espionage-Case.pdf)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [CISA. (2020, October 29). Malware Analysis Report (AR20-303A). Retrieved December 9, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303a)
- [Burton, K. (n.d.). The Conficker Worm. Retrieved February 18, 2021.](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
- [Trend Micro. (2014, March 18). Conficker. Retrieved February 18, 2021.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/conficker)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [PwC Threat Intelligence. (2023, October 25). Yellow Liderc ships its scripts and delivers IMAPLoader malware. Retrieved August 14, 2024.](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Ernesto Fernández Provecho, Pham Duy Phuc, Ciana Driscoll & Vinoo Thomas. (2023, November 21). The Continued Evolution of the DarkGate Malware-as-a-Service. Retrieved February 9, 2024.](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
- [Arunpreet Singh, Clemens Kolbitsch. (2015, November 5). Defeating Darkhotel Just-In-Time Decryption. Retrieved April 15, 2021.](https://www.lastline.com/labsblog/defeating-darkhotel-just-in-time-decryption/)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [Checkpoint Research. (2021, November 15). Uncovering MosesStaff techniques: Ideology over Money. Retrieved August 11, 2022.](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Joe Security. (n.d.). Analysis Report fasm.dll. Retrieved November 17, 2024.](https://www.joesandbox.com/analysis/326673/0/pdf)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [Marschalek, M.. (2014, December 16). EvilBunny: Malware Instrumented By Lua. Retrieved June 28, 2019.](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)
- [Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
- [The BlackBerry Research and Intelligence Team. (2024, April 17). Threat Group FIN7 Targets the U.S. Automotive Industry. Retrieved May 1, 2025.](https://blogs.blackberry.com/en/2024/04/fin7-targets-the-united-states-automotive-industry)
- [Kirill Boychenko. (2026, January 31). GlassWorm Loader Hits Open VSX via Developer Account Compromise. Retrieved April 10, 2026.](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [Smith, L., Leathery, J., Read, B. (2021, March 4). New SUNSHUTTLE Second-Stage Backdoor Uncovered Targeting U.S.-Based Entity; Possible Connection to UNC2452. Retrieved March 12, 2021.](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
- [Sandvik, Runa. (2021, October 1). Made In America: Green Lambert for OS X. Retrieved March 21, 2022.](https://objective-see.com/blog/blog_0x68.html)
- [Sandvik, Runa. (2021, October 18). Green Lambert and ATT&CK. Retrieved November 17, 2024.](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)
- [Namestnikov, Y. and Aime, F. (2019, May 8). FIN7.5: the infamous cybercrime rig “FIN7” continues its activities. Retrieved October 11, 2019.](https://securelist.com/fin7-5-the-infamous-cybercrime-rig-fin7-continues-its-activities/90703/)
- [Singh, S. Singh, A. (2020, June 11). The Return on the Higaisa APT. Retrieved March 2, 2021.](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part II. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Erlich, C. (2020, April 3). The Avast Abuser: Metamorfo Banking Malware Hides By Abusing Avast Executable. Retrieved May 26, 2020.](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
- [Miller-Osborn, J. and Grunzweig, J.. (2017, March 30). Trochilus and New MoonWind RATs Used In Attack Against Thai Organizations. Retrieved March 30, 2017.](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
- [Microsoft. (n.d.). Net time. Retrieved November 25, 2016.](https://technet.microsoft.com/bb490716.aspx)
- [Ahn Ho, Facundo Muñoz, & Marc-Etienne M.Léveillé. (2024, March 7). Evasive Panda leverages Monlam Festival to target Tibetans. Retrieved July 25, 2024.](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
- [Grunzweig, J., Lee, B. (2018, September 27). New KONNI Malware attacking Eurasia and Southeast Asia. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
- [Hromcova, Z. (2019, July). OKRUM AND KETRICAN: AN OVERVIEW OF RECENT KE3CHANG GROUP ACTIVITY. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
- [Falcone, R., et al. (2018, September 04). OilRig Targets a Middle Eastern Government and Adds Evasion Techniques to OopsIE. Retrieved September 24, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: PAKLOG, CorKLOG, and SplatCloak | P2. Retrieved September 12, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
- [Tartare, M. et al. (2020, May 21). No “Game over” for the Winnti Group. Retrieved August 24, 2020.](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [S2W TALON. (2022, June 16). Raccoon Stealer is Back with a New Version. Retrieved August 1, 2024.](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Faou, M. and Boutin, J. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
- [Kaspersky Lab. (2017, August). ShadowPad: popular server management software hit in supply chain attack. Retrieved March 22, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
- [Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [Falcone, R. (2018, December 13). Shamoon 3 Targets Oil and Gas Organization. Retrieved March 14, 2019.](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
- [Lunghi, D. and Horejsi, J.. (2019, June 10). MuddyWater Resurfaces, Uses Multi-Stage Backdoor POWERSTATS V3 and New Post-Exploitation Tools. Retrieved May 14, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
- [Splunk Threat Research Team , Teoderick Contreras. (2024, September 5). ShrinkLocker Malware: Abusing BitLocker to Lock Your Data. Retrieved December 7, 2024.](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
- [Hegel, T. (2021, January 13). A Global Perspective of the SideWinder APT. Retrieved January 27, 2021.](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: ToneShell and StarProxy | P1. Retrieved July 21, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
- [Kaspersky Lab. (2017, March 7). From Shamoon to StoneDrill: Wipers attacking Saudi organizations and beyond. Retrieved March 14, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
- [Cybereason Nocturnus. (2022, February 1). StrifeWater RAT: Iranian APT Moses Staff Adds New Trojan to Ransomware Operations. Retrieved August 15, 2022.](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [MSTIC. (2020, December 18). Analyzing Solorigate, the compromised DLL file that started a sophisticated cyberattack, and how Microsoft Defender helps protect customers . Retrieved January 5, 2021.](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [Truman, D. (2024, January 19). Inside the SYSTEMBC Command-and-Control Server. Retrieved June 18, 2025.](https://www.kroll.com/en/publications/cyber/inside-the-systembc-malware-server)
- [Grunzweig, J. and Miller-Osborn, J.. (2016, February 4). T9000: Advanced Modular Backdoor Uses Complex Anti-Analysis Techniques. Retrieved April 15, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
- [CISA, FBI, DOD. (2021, August). MAR-10292089-1.v2 – Chinese Remote Access Trojan: TAIDOOR. Retrieved August 24, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
- [USG. (2020, May 12). MAR-10288834-2.v1 – North Korean Trojan: TAINTEDSCRIBE. Retrieved March 5, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Livelli, K, et al. (2018, November 12). Operation Shaheen. Retrieved May 1, 2019.](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
- [Beek, C. (2020, November 5). Operation North Star: Behind The Scenes. Retrieved December 20, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
- [Alexander Marvi, Brad Slaybaugh, Ron Craft, and Rufus Brown. (2023, June 13). VMware ESXi Zero-Day Used by Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)
- [Matsuda, A., Muhammad I. (2018, September 13). APT10 Targeting Japanese Corporations Using Updated TTPs. Retrieved September 17, 2018.](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Wardle, Patrick. (2018, December 20). Middle East Cyber-Espionage analyzing WindShift's implant: OSX.WindTail (part 1). Retrieved October 3, 2019.](https://objective-see.com/blog/blog_0x3B.html)
- [ESET. (2018, November 20). Sednit: What’s going on with Zebrocy?. Retrieved February 12, 2019.](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
- [CISA. (2020, October 29). Malware Analysis Report (AR20-303B). Retrieved December 9, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
- [Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
- [Singh, S. and Antil, S. (2020, October 27). APT-31 Leverages COVID-19 Vaccine Theme and Abuses Legitimate Online Services. Retrieved March 24, 2021.](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)

---

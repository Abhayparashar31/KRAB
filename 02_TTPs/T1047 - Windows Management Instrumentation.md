# Windows Management Instrumentation

## Description

Adversaries may abuse Windows Management Instrumentation (WMI) to execute malicious commands and payloads. WMI is designed for programmers and is the infrastructure for management data and operations on Windows systems. [1] WMI is an administration feature that provides a uniform environment to access Windows system components.

The WMI service enables both local and remote access, though the latter is facilitated by Remote Services such as Distributed Component Object Model and Windows Remote Management . [1] Remote WMI over DCOM operates using port 135, whereas WMI over WinRM operates over port 5985 when using HTTP and 5986 for HTTPS. [1] [2]

An adversary can use WMI to interact with local and remote systems and use it as a means to execute various behaviors, such as gathering information for Discovery as well as Execution of commands and payloads. [2] For example, wmic.exe can be abused by an adversary to delete shadow copies with the command wmic.exe Shadowcopy Delete (i.e., Inhibit System Recovery ). [3]

Note: wmic.exe is deprecated as of January of 2024, with the WMIC feature being "disabled by default" on Windows 11+. WMIC will be removed from subsequent Windows releases and replaced by PowerShell as the primary WMI interface. [4] In addition to PowerShell and tools like wbemtool.exe , COM APIs can also be used to programmatically interact with WMI via C++, .NET, VBScript, etc. [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0025 | 2016 Ukraine Electric Power Attack | During the 2016 Ukraine Electric Power Attack , WMI in scripts were used for remote execution and system surveys. [5] |
| S1028 | Action RAT | Action RAT can use WMI to gather AV products installed on an infected host. [6] |
| S0331 | Agent Tesla | Agent Tesla has used wmi queries to gather information from the system. [7] |
| S1129 | Akira | Akira will leverage COM objects accessed through WMI during execution to evade detection. [8] |
| G0099 | APT-C-36 | APT-C-36 has used WMI to execute PowerShell. [9] |
| G0016 | APT29 | APT29 used WMI to steal credentials and execute backdoors at a future time. [10] |
| G0050 | APT32 | APT32 used WMI to deploy their tools on remote machines and to gather information about the Outlook process. [11] |
| G0096 | APT41 | APT41 used WMI in several ways, including for execution of commands via WMIEXEC as well as for persistence via PowerSploit . [12] [13] APT41 has executed files through Windows Management Instrumentation (WMI). [14] |
| G1044 | APT42 | APT42 has used Windows Management Instrumentation (WMI) to query anti-virus products. [15] |
| G0143 | Aquatic Panda | Aquatic Panda used WMI for lateral movement in victim environments. [16] |
| S9031 | AshTag | AshTag can use a .NET program to execute WMI queries and send unique victim IDs to C2. [17] |
| S0373 | Astaroth | Astaroth uses WMIC to execute payloads. [18] |
| S0640 | Avaddon | Avaddon uses wmic.exe to delete shadow copies. [19] |
| S1081 | BADHATCH | BADHATCH can utilize WMI to collect system information, create new processes, and run malicious PowerShell scripts on a compromised machine. [20] [21] |
| S0534 | Bazar | Bazar can execute a WMI query to gather information about the installed antivirus engine. [22] [23] |
| S1070 | Black Basta | Black Basta has used WMI to execute files over the network. [24] |
| G1043 | BlackByte | BlackByte used WMI to delete Volume Shadow Copies on victim machines. [25] |
| S1068 | BlackCat | BlackCat can use wmic.exe to delete shadow copies on compromised networks. [26] |
| S0089 | BlackEnergy | A BlackEnergy 2 plug-in uses WMI to gather victim host details. [27] |
| G0108 | Blue Mockingbird | Blue Mockingbird has used wmic.exe to set environment variables. [28] |
| S1063 | Brute Ratel C4 | Brute Ratel C4 can use WMI to move laterally. [29] |
| S1039 | Bumblebee | Bumblebee can use WMI to gather system information and to spawn processes for code injection. [30] [31] [32] |
| C0015 | C0015 | During C0015 , the threat actors used wmic and rundll32 to load Cobalt Strike onto a target host. [33] |
| C0018 | C0018 | During C0018 , the threat actors used WMIC to modify administrative settings on both a local and a remote host, likely as part of the first stages for their lateral movement; they also used WMI Provider Host ( wmiprvse.exe ) to execute a variety of encoded PowerShell scripts using the DownloadString method. [34] [35] |
| C0027 | C0027 | During C0027 , Scattered Spider used Windows Management Instrumentation (WMI) to move laterally via Impacket . [36] |
| S0674 | CharmPower | CharmPower can use wmic to gather information from a system. [37] |
| G0114 | Chimera | Chimera has used WMIC to execute remote commands. [38] [39] |
| G1021 | Cinnamon Tempest | Cinnamon Tempest has used Impacket for lateral movement via WMI. [40] [41] |
| S0154 | Cobalt Strike | Cobalt Strike can use WMI to deliver a payload to a remote host. [42] [43] [33] |
| S1155 | Covenant | Covenant can utilize WMI to install new Grunt listeners through XSL files or command one-liners. [44] |
| S0488 | CrackMapExec | CrackMapExec can execute remote commands using Windows Management Instrumentation. [45] |
| S1111 | DarkGate | DarkGate has used WMI to execute files over the network and to obtain information about the domain. [46] |
| S1066 | DarkTortilla | DarkTortilla can use WMI queries to obtain system information. [47] |
| S0673 | DarkWatchman | DarkWatchman can use WMI to execute commands. [48] |
| S0616 | DEATHRANSOM | DEATHRANSOM has the ability to use WMI to delete volume shadow copies. [49] |
| G0009 | Deep Panda | The Deep Panda group is known to utilize WMI for lateral movement. [50] |
| S0062 | DustySky | The DustySky dropper uses Windows Management Instrumentation to extract information about the operating system and whether an anti-virus is active. [51] |
| G1006 | Earth Lusca | Earth Lusca used a VBA script to execute WMI. [52] |
| S0605 | EKANS | EKANS can use Windows Mangement Instrumentation (WMI) calls to execute operations. [53] |
| G1003 | Ember Bear | Ember Bear has used WMI execution with password hashes for command execution and lateral movement. [54] |
| S0367 | Emotet | Emotet has used WMI to execute powershell.exe. [55] |
| S0363 | Empire | Empire can use WMI to deliver a payload to a remote host. [56] |
| S0396 | EvilBunny | EvilBunny has used WMI to gather information about the system. [57] |
| S0568 | EVILNUM | EVILNUM has used the Windows Management Instrumentation (WMI) tool to enumerate infected machines. [58] |
| S0267 | FELIXROOT | FELIXROOT uses WMI to query the Windows Registry. [59] |
| G1016 | FIN13 | FIN13 has utilized WMI to execute commands and move laterally on compromised Windows machines. [60] [61] |
| G0037 | FIN6 | FIN6 has used WMI to automate the remote execution of PowerShell scripts. [62] |
| G0046 | FIN7 | FIN7 has used WMI to install malware on targeted systems. [63] |
| G0061 | FIN8 | FIN8 's malicious spearphishing payloads use WMI to launch malware and spawn cmd.exe execution. FIN8 has also used WMIC and the Impacket suite for lateral movement, as well as during and post compromise cleanup activities. [64] [65] [66] [67] |
| S0618 | FIVEHANDS | FIVEHANDS can use WMI to delete files on a target machine. [49] [68] |
| S0381 | FlawedAmmyy | FlawedAmmyy leverages WMI to enumerate anti-virus on the victim. [69] |
| C0001 | Frankenstein | During Frankenstein , the threat actors used WMI queries to check if various security applications were running as well as to determine the operating system version. [70] |
| S1044 | FunnyDream | FunnyDream can use WMI to open a Windows command shell on a remote machine. [71] |
| C0007 | FunnyDream | During FunnyDream , the threat actors used wmiexec.vbs to run remote commands. [71] |
| G0093 | GALLIUM | GALLIUM used WMI for execution to assist in lateral movement as well as for installing tools across multiple assets. [72] |
| G0047 | Gamaredon Group | Gamaredon Group has used WMI to execute scripts used for discovery and for determining the C2 IP address. [73] [74] [75] [76] Gamaredon Group has used the following WMI query to search for a ping record: Select * From Win32_PingStatus where Address = 'mil.gov.ua' . [75] |
| S0237 | GravityRAT | GravityRAT collects various information via WMI requests, including CPU information in the Win32_Processor entry (Processor ID, Name, Manufacturer and the clock speed). [77] |
| S0151 | HALFBAKED | HALFBAKED can use WMI queries to gather system information. [78] |
| S0617 | HELLOKITTY | HELLOKITTY can use WMI to delete volume shadow copies. [49] |
| S0698 | HermeticWizard | HermeticWizard can use WMI to create a new process on a remote machine via C:\windows\system32\cmd.exe /c start C:\windows\system32\\regsvr32.exe /s /iC:\windows\<filename>.dll . [79] |
| C0038 | HomeLand Justice | During HomeLand Justice , threat actors used WMI to modify Windows Defender settings. [80] |
| S0376 | HOPLIGHT | HOPLIGHT has used WMI to recompile the Managed Object Format (MOF) files in the WMI repository. [81] |
| S0483 | IcedID | IcedID has used WMI to execute binaries. [82] [83] |
| S1152 | IMAPLoader | IMAPLoader uses WMI queries to query system information on victim hosts. [84] |
| S0357 | Impacket | Impacket 's wmiexec module can be used to execute commands through WMI. [85] [86] |
| G1032 | INC Ransom | INC Ransom has used WMIC to deploy ransomware. [87] [88] [89] |
| S1139 | INC Ransomware | INC Ransomware has the ability to use wmic.exe to spread to multiple endpoints within a compromised environment. [88] [90] |
| G0119 | Indrik Spider | Indrik Spider has used WMIC to execute commands on remote computers. [91] |
| S0283 | jRAT | jRAT uses WMIC to identify anti-virus products installed on the victim’s machine and to obtain firewall details. [92] |
| S0265 | Kazuar | Kazuar obtains a list of running processes through WMI querying. [93] |
| S0250 | Koadic | Koadic can use WMI to execute commands. [94] |
| S0156 | KOMPROGO | KOMPROGO is capable of running WMI queries. [95] |
| S9035 | LAMEHUG | LAMEHUG can use wmic to collect system information. [96] |
| S1160 | Latrodectus | Latrodectus has used WMI in malicious email infection chains to facilitate the installation of remotely-hosted files. [97] [98] |
| G0032 | Lazarus Group | Lazarus Group has used WMIC for discovery as well as to execute payloads for persistence and lateral movement. [99] [100] [101] [102] |
| G0065 | Leviathan | Leviathan has used WMI for execution. [103] |
| S1199 | LockBit 2.0 | LockBit 2.0 can use wmic.exe to delete volume shadow copies. [104] |
| S9020 | LODEINFO | LODEINFO can execute commands with WMI. [105] [106] |
| G0030 | Lotus Blossom | Lotus Blossom has used WMI to enable lateral movement. [107] |
| S0532 | Lucifer | Lucifer can use WMI to log into remote machines for propagation. [108] |
| S1141 | LunarWeb | LunarWeb can use WMI queries for discovery on the victim host. [109] |
| G0059 | Magic Hound | Magic Hound has used a tool to run cmd /c wmic computersystem get domain for discovery. [110] |
| S0449 | Maze | Maze has used WMI to attempt to delete the shadow volumes on a machine, and to connect a virtual machine to the network domain of the victim organization's network. [111] [112] |
| G1051 | Medusa Group | Medusa Group has utilized Windows Management Instrumentation to query system information. [113] [114] [115] |
| G0045 | menuPass | menuPass has used a modified version of pentesting script wmiexec.vbs, which logs into a remote machine using WMI. [116] [117] [118] |
| S0688 | Meteor | Meteor can use wmic.exe as part of its effort to delete shadow copies. [119] |
| S0339 | Micropsia | Micropsia searches for anti-virus software and firewall products installed on the victim’s machine using WMI. [120] [121] |
| G1054 | MirrorFace | MirrorFace has leveraged WMIC on targeted systems post compromise. [122] |
| S0553 | MoleNet | MoleNet can perform WMI commands on the system. [123] |
| S0256 | Mosquito | Mosquito 's installer uses WMI to search for antivirus display names. [124] |
| G0069 | MuddyWater | MuddyWater has used malware that leveraged WMI for execution and querying host information. [125] [126] [127] [128] |
| G0129 | Mustang Panda | Mustang Panda has executed PowerShell scripts via WMI. [129] [130] |
| G0019 | Naikon | Naikon has used WMIC.exe for lateral movement. [131] |
| S0457 | Netwalker | Netwalker can use WMI to delete Shadow Volumes. [132] |
| S0368 | NotPetya | NotPetya can use wmic to help propagate itself across a network. [133] [134] |
| S0340 | Octopus | Octopus has used wmic.exe for local discovery information. [135] |
| G0049 | OilRig | OilRig has used WMI for execution. [136] [137] |
| S0365 | Olympic Destroyer | Olympic Destroyer uses WMI to help propagate itself across a network. [138] |
| S0264 | OopsIE | OopsIE uses WMI to perform discovery techniques. [139] |
| C0060 | Operation AkaiRyū | During Operation AkaiRyū , MirrorFace used WMI to proxy execution of UPPERCUT . [140] |
| C0022 | Operation Dream Job | During Operation Dream Job , Lazarus Group used WMIC to executed a remote XSL script. [141] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors has used WMI to execute commands. [142] |
| S0378 | PoshC2 | PoshC2 has a number of modules that use WMI to execute tasks. [143] |
| S0194 | PowerSploit | PowerSploit 's Invoke-WmiCommand CodeExecution module uses WMI to execute and retrieve the output from a PowerShell payload. [144] [145] |
| S0223 | POWERSTATS | POWERSTATS can use WMI queries to retrieve data from compromised hosts. [146] [126] |
| S0184 | POWRUNER | POWRUNER may use WMI when collecting information about a victim. [147] |
| S0654 | ProLock | ProLock can use WMIC to execute scripts on targeted hosts. [148] |
| S1228 | PUBLOAD | PUBLOAD has used wmic to gather information from the victim device. [149] |
| S1032 | PyDCrypt | PyDCrypt has attempted to execute with WMIC. [150] |
| S0650 | QakBot | QakBot can execute WMI queries to gather information. [151] |
| S1242 | Qilin | Qilin can use WMIC to change the Volume Shadow Copy Service (VSS) startup type to manual. [152] |
| S1130 | Raspberry Robin | Raspberry Robin can execute via LNK containing a command to run a legitimate executable, such as wmic.exe, to download a malicious Windows Installer (MSI) package. [153] |
| S0241 | RATANKBA | RATANKBA uses WMI to perform process monitoring. [154] [155] |
| S0375 | Remexi | Remexi executes received commands with wmic.exe (for WMI commands). [156] |
| S0496 | REvil | REvil can use WMI to monitor for and kill specific processes listed in its configuration file. [157] [158] |
| S9026 | ROAMINGHOUSE | ROAMINGHOUSE can use WMI to launch a legitimate executable later used to enable DLL sideloading. [159] [160] |
| S0270 | RogueRobin | RogueRobin uses various WMI queries to check if the sample is running in a sandbox. [161] [162] |
| G0034 | Sandworm Team | Sandworm Team has used Impacket ’s WMIexec module for remote code execution and VBScript to run WMI queries. [5] [163] |
| S1085 | Sardonic | Sardonic can use WMI to execute PowerShell commands on a compromised machine. [164] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors used WMI for execution. [165] |
| S0546 | SharpStage | SharpStage can use WMI for execution. [123] [166] |
| S1178 | ShrinkLocker | ShrinkLocker uses WMI to query information about the victim operating system. [167] |
| S0589 | Sibot | Sibot has used WMI to discover network connections and configurations. Sibot has also used the Win32_Process class to execute a malicious DLL. [168] |
| S0692 | SILENTTRINITY | SILENTTRINITY can use WMI for lateral movement. [169] |
| S1086 | Snip3 | Snip3 can query the WMI class Win32_ComputerSystem to gather information. [170] |
| S1124 | SocGholish | SocGholish has used WMI calls for script execution and system profiling. [171] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 used WMI for the remote execution of files for lateral movement. [172] [173] |
| G0038 | Stealth Falcon | Stealth Falcon malware gathers system information via Windows Management Instrumentation (WMI). [174] |
| S0380 | StoneDrill | StoneDrill has used the WMI command-line (WMIC) utility to run tasks. [175] |
| S0603 | Stuxnet | Stuxnet used WMI with an explorer.exe token to execute on a remote share. [176] |
| S0559 | SUNBURST | SUNBURST used the WMI query Select * From Win32_SystemDriver to retrieve a driver listing. [177] |
| S1064 | SVCReady | SVCReady can use WMI queries to detect the presence of a virtual machine environment. [178] |
| S0663 | SysUpdate | SysUpdate can use WMI for execution on a compromised host. [179] |
| G1018 | TA2541 | TA2541 has used WMI to query targeted systems for security products. [180] |
| S1193 | TAMECAT | TAMECAT has used Windows Management Instrumentation (WMI) to query anti-virus products. [15] |
| G0027 | Threat Group-3390 | A Threat Group-3390 tool can use WMI to execute a binary. [181] |
| G1022 | ToddyCat | ToddyCat has used WMI to execute scripts for post exploit document collection. [182] |
| S1239 | TONESHELL | TONESHELL has used WMI queries to gather information from the system. [183] |
| S0386 | Ursnif | Ursnif droppers have used WMI classes to execute PowerShell commands. [184] |
| S0476 | Valak | Valak can use wmic process call create in a scheduled task to launch plugins and for execution. [185] |
| G1047 | Velvet Ant | Velvet Ant used the wmiexec.py tool within Impacket for remote process execution via WMI. [86] |
| G1055 | VOID MANTICORE | VOID MANTICORE has utilized WMIC to log into the victim host and create a process process call create "cmd.exe /c copy \\?\\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\system c:\users\public" . [186] |
| G1017 | Volt Typhoon | Volt Typhoon has leveraged WMIC for execution, remote system discovery, and to create and use temporary directories. [187] [188] [189] [190] |
| S0366 | WannaCry | WannaCry utilizes wmic to delete shadow copies. [191] [192] [193] |
| G0112 | Windshift | Windshift has used WMI to collect information about target machines. [194] |
| G0102 | Wizard Spider | Wizard Spider has used WMI and LDAP queries for network discovery and to move laterally. Wizard Spider has also used batch scripts to leverage WMIC to deploy ransomware. [195] [196] [197] [198] [199] |
| S0251 | Zebrocy | One variant of Zebrocy uses WMI queries to gather information. [200] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1040 | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to block processes created by WMI commands from running. Note: many legitimate tools and applications utilize WMI for command execution. [201] |
| M1038 | Execution Prevention | Use application control configured to block execution of wmic.exe if it is not required for a given system or network to prevent potential misuse by adversaries. For example, in Windows 10 and Windows Server 2016 and above, Windows Defender Application Control (WDAC) policy rules may be applied to block the wmic.exe application and to prevent abuse. [202] |
| M1026 | Privileged Account Management | Prevent credential overlap across systems of administrator and privileged accounts. [203] |
| M1018 | User Account Management | By default, only administrators are allowed to connect remotely using WMI. Restrict other users who are allowed to connect, or disallow all users to connect remotely to WMI. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0364 | Behavioral Detection Strategy for WMI Execution Abuse on Windows | AN1031 | Detects adversarial abuse of WMI to execute local or remote commands via WMIC, PowerShell, or COM API through a multi-event chain: process creation, command execution, and corresponding network connection if remote. |

---

## References

- [Microsoft. (2023, March 7). Retrieved February 13, 2024.](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page?redirectedfrom=MSDN)
- [Mandiant. (n.d.). Retrieved February 13, 2024.](https://www.mandiant.com/resources/reports)
- [Microsoft. (2022, June 13). BlackCat. Retrieved February 13, 2024.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [Microsoft. (2024, January 26). WMIC Deprecation. Retrieved February 13, 2024.](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/wmi-command-line-wmic-utility-deprecation-next-steps/ba-p/4039242)
- [Joe Slowik. (2018, October 12). Anatomy of an Attack: Detecting and Defeating CRASHOVERRIDE. Retrieved December 18, 2020.](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [Arsene, L. (2020, April 21). Oil & Gas Spearphishing Campaigns Drop Agent Tesla Spyware in Advance of Historic OPEC+ Deal. Retrieved May 19, 2020.](https://labs.bitdefender.com/2020/04/oil-gas-spearphishing-campaigns-drop-agent-tesla-spyware-in-advance-of-historic-opec-deal/)
- [Max Kersten & Alexandre Mundo. (2023, November 29). Akira Ransomware. Retrieved April 4, 2024.](https://www.trellix.com/blogs/research/akira-ransomware/)
- [Pellegrino, G. (2025, December 16). BlindEagle Targets Colombian Government Agency with Caminho and DCRAT. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)
- [Dunwoody, M. and Carr, N.. (2016, September 27). No Easy Breach DerbyCon 2016. Retrieved September 12, 2024.](https://www.slideshare.net/slideshow/no-easy-breach-derby-con-2016/66447908)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [Rostovcev, N. (2021, June 10). Big airline heist APT41 likely behind a third-party attack on Air India. Retrieved August 26, 2021.](https://www.group-ib.com/blog/colunmtk-apt41/)
- [DCSO CyTec Blog. (2022, December 24). APT41 — The spy who failed to encrypt me. Retrieved June 13, 2024.](https://medium.com/@DCSO_CyTec/apt41-the-spy-who-failed-to-encrypt-me-24fc0f49cad1)
- [Rozmann, O., et al. (2024, May 1). Uncharmed: Untangling Iran's APT42 Operations. Retrieved October 9, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)
- [CrowdStrike. (2023). 2022 Falcon OverWatch Threat Hunting Report. Retrieved May 20, 2024.](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)
- [Unit 42. (2025, December 11). Hamas-Affiliated Ashen Lepus Targets Middle Eastern Diplomatic Entities With New AshTag Malware Suite. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
- [Doaty, J., Garrett, P.. (2018, September 10). We’re Seeing a Resurgence of the Demonic Astaroth WMIC Trojan. Retrieved September 25, 2024.](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)
- [Security Lab. (2020, June 5). Avaddon: From seeking affiliates to in-the-wild in 2 days. Retrieved August 19, 2021.](https://www.hornetsecurity.com/en/security-information/avaddon-from-seeking-affiliates-to-in-the-wild-in-2-days/)
- [Savelesky, K., et al. (2019, July 23). ABADBABE 8BADFOOD: Discovering BADHATCH and a Detailed Look at FIN8's Tooling. Retrieved September 8, 2021.](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [The DFIR Report. (2020, October 8). Ryuk’s Return. Retrieved October 9, 2020.](https://thedfirreport.com/2020/10/08/ryuks-return/)
- [Inman, R. and Gurney, P. (2022, June 6). Shining the Light on Black Basta. Retrieved March 8, 2023.](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)
- [US Federal Bureau of Investigation & US Secret Service. (2022, February 11). Indicators of Compromise Associated with BlackByte Ransomware. Retrieved December 16, 2024.](https://www.ic3.gov/CSA/2022/220211.pdf)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [Baumgartner, K. and Garnaeva, M.. (2015, February 17). BE2 extraordinary plugins, Siemens targeting, dev fails. Retrieved March 24, 2016.](https://securelist.com/be2-extraordinary-plugins-siemens-targeting-dev-fails/68838/)
- [Lambert, T. (2020, May 7). Introducing Blue Mockingbird. Retrieved May 26, 2020.](https://redcanary.com/blog/blue-mockingbird-cryptominer/)
- [Harbison, M. and Renals, P. (2022, July 5). When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors. Retrieved February 1, 2023.](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
- [Stolyarov, V. (2022, March 17). Exposing initial access broker with ties to Conti. Retrieved August 18, 2022.](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)
- [Merriman, K. and Trouerbach, P. (2022, April 28). This isn't Optimus Prime's Bumblebee but it's Still Transforming. Retrieved August 22, 2022.](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
- [Cybereason. (2022, August 17). Bumblebee Loader – The High Road to Enterprise Domain Control. Retrieved August 29, 2022.](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Venere, G. Neal, C. (2022, June 21). Avos ransomware group expands with new attack arsenal. Retrieved January 11, 2023.](https://blog.talosintelligence.com/avoslocker-new-arsenal/)
- [Costa, F. (2022, May 1). RaaS AvosLocker Incident Response Analysis. Retrieved January 11, 2023.](https://www.linkedin.com/pulse/raas-avoslocker-incident-response-analysis-fl%C3%A1vio-costa?trk=articles_directory)
- [Parisi, T. (2022, December 2). Not a SIMulation: CrowdStrike Investigations Reveal Intrusion Campaign Targeting Telco and BPO Companies. Retrieved June 30, 2023.](https://www.crowdstrike.com/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Cycraft. (2020, April 15). APT Group Chimera - APT Operation Skeleton key Targets Taiwan Semiconductor Vendors. Retrieved August 24, 2020..](https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Microsoft. (2022, May 9). Ransomware as a service: Understanding the cybercrime gig economy and how to protect yourself. Retrieved March 10, 2023.](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)
- [Biderman, O. et al. (2022, October 3). REVEALING EMPEROR DRAGONFLY: NIGHT SKY AND CHEERSCRYPT - A SINGLE RANSOMWARE GROUP. Retrieved December 6, 2023.](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)
- [Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [cobbr. (2021, April 21). Covenant. Retrieved September 4, 2024.](https://github.com/cobbr/Covenant)
- [byt3bl33d3r. (2018, September 8). SMB: Command Reference. Retrieved July 17, 2020.](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
- [McGraw, T. (2024, December 4). Black Basta Ransomware Campaign Drops Zbot, DarkGate, and Custom Malware. Retrieved December 9, 2024.](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [McLellan, T. and Moore, J. et al. (2021, April 29). UNC2447 SOMBRAT and FIVEHANDS Ransomware: A Sophisticated Financial Threat. Retrieved June 2, 2021.](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
- [Alperovitch, D. (2014, July 7). Deep in Thought: Chinese Targeting of National Security Think Tanks. Retrieved November 12, 2014.](https://web.archive.org/web/20200424075623/https:/www.crowdstrike.com/blog/deep-thought-chinese-targeting-national-security-think-tanks/)
- [ClearSky. (2016, January 7). Operation DustySky. Retrieved January 8, 2016.](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
- [Chen, J., et al. (2022). Delving Deep: An Analysis of Earth Lusca’s Operations. Retrieved July 1, 2022.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
- [Dragos. (2020, February 3). EKANS Ransomware and ICS Operations. Retrieved February 9, 2021.](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)
- [US Cybersecurity & Infrastructure Security Agency et al. (2024, September 5). Russian Military Cyber Actors Target U.S. and Global Critical Infrastructure. Retrieved September 6, 2024.](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)
- [Lee, S.. (2019, April 24). Emotet Using WMI to Launch PowerShell Encoded Code. Retrieved May 24, 2019.](https://www.carbonblack.com/2019/04/24/cb-tau-threat-intelligence-notification-emotet-utilizing-wmi-to-launch-powershell-encoded-code/)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Marschalek, M.. (2014, December 16). EvilBunny: Malware Instrumented By Lua. Retrieved June 28, 2019.](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)
- [Adamitis, D. (2020, May 6). Phantom in the Command Shell. Retrieved November 17, 2024.](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
- [Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [Sygnia Incident Response Team. (2022, January 5). TG2003: ELEPHANT BEETLE UNCOVERING AN ORGANIZED FINANCIAL-THEFT OPERATION. Retrieved February 9, 2023.](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)
- [Villadsen, O.. (2019, August 29). More_eggs, Anyone? Threat Actor ITG08 Strikes Again. Retrieved September 16, 2019.](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)
- [eSentire. (2021, July 21). Notorious Cybercrime Gang, FIN7, Lands Malware in Law Firm Using Fake Legal Complaint Against Jack Daniels’ Owner, Brown-Forman Inc.. Retrieved September 20, 2021.](https://www.esentire.com/security-advisories/notorious-cybercrime-gang-fin7-lands-malware-in-law-firm-using-fake-legal-complaint-against-jack-daniels-owner-brown-forman-inc)
- [Bohannon, D. & Carr N. (2017, June 30). Obfuscation in the Wild: Targeted Attackers Lead the Way in Evasion Techniques. Retrieved February 12, 2018.](https://web.archive.org/web/20170923102302/https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html)
- [Martin Zugec. (2021, July 27). Deep Dive Into a FIN8 Attack - A Forensic Investigation. Retrieved September 1, 2021.](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation)
- [Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy: New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)
- [Symantec Threat Hunter Team. (2023, July 18). FIN8 Uses Revamped Sardonic Backdoor to Deliver Noberus Ransomware. Retrieved August 9, 2023.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [Proofpoint Staff. (2018, March 7). Leaked Ammyy Admin Source Code Turned into Malware. Retrieved May 28, 2019.](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)
- [Adamitis, D. et al. (2019, June 4). It's alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign. Retrieved May 11, 2020.](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Cybereason Nocturnus. (2019, June 25). Operation Soft Cell: A Worldwide Campaign Against Telecommunications Providers. Retrieved July 18, 2019.](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)
- [CERT-EE. (2021, January 27). Gamaredon Infection: From Dropper to Entry. Retrieved February 17, 2022.](https://www.ria.ee/sites/default/files/content-editors/kuberturve/tale_of_gamaredon_infection.pdf)
- [Unit 42. (2022, December 20). Russia’s Trident Ursa (aka Gamaredon APT) Cyber Conflict Operations Unwavering Since Invasion of Ukraine. Retrieved September 12, 2024.](https://unit42.paloaltonetworks.com/trident-ursa/)
- [Threat Hunter Team, Symantec and Carbon Black. (2025, April 10). Shuckworm Targets Foreign Military Mission Based in Ukraine. Retrieved July 23, 2025.](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
- [Carr, N., et al. (2017, April 24). FIN7 Evolution and the Phishing LNK. Retrieved April 24, 2017.](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)
- [ESET. (2022, March 1). IsaacWiper and HermeticWizard: New wiper and worm targetingUkraine. Retrieved April 10, 2022.](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
- [MSTIC. (2022, September 8). Microsoft investigates Iranian attacks against the Albanian government. Retrieved August 6, 2024.](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [Kimayong, P. (2020, June 18). COVID-19 and FMLA Campaigns used to install new IcedID banking malware. Retrieved July 14, 2020.](https://blogs.juniper.net/en-us/threat-research/covid-19-and-fmla-campaigns-used-to-install-new-icedid-banking-malware)
- [DFIR. (2021, March 29). Sodinokibi (aka REvil) Ransomware. Retrieved July 22, 2024.](https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/)
- [PwC Threat Intelligence. (2023, October 25). Yellow Liderc ships its scripts and delivers IMAPLoader malware. Retrieved August 14, 2024.](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
- [SecureAuth. (n.d.). Retrieved January 15, 2019.](https://www.secureauth.com/labs/open-source-tools/impacket)
- [Sygnia Team. (2024, June 3). China-Nexus Threat Group ‘Velvet Ant’ Abuses F5 Load Balancers for Persistence. Retrieved March 14, 2025.](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [Team Huntress. (2023, August 11). Investigating New INC Ransom Group Activity. Retrieved June 5, 2024.](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)
- [SOCRadar. (2024, January 24). Dark Web Profile: INC Ransom. Retrieved June 5, 2024.](https://socradar.io/dark-web-profile-inc-ransom/)
- [Counter Threat Unit Research Team. (2024, April 15). GOLD IONIC DEPLOYS INC RANSOMWARE. Retrieved June 5, 2024.](https://www.secureworks.com/blog/gold-ionic-deploys-inc-ransomware)
- [Symantec Threat Intelligence. (2020, June 25). WastedLocker: Symantec Identifies Wave of Attacks Against U.S. Organizations. Retrieved May 20, 2021.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)
- [Sharma, R. (2018, August 15). Revamped jRAT Uses New Anti-Parsing Techniques. Retrieved September 21, 2018.](https://www.symantec.com/blogs/threat-intelligence/jrat-new-anti-parsing-techniques)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [Magius, J., et al. (2017, July 19). Koadic. Retrieved September 27, 2024.](https://github.com/offsecginger/koadic)
- [Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
- [Conteras, T., Splunk Research Team. (2025, September 25). From Prompt to Payload: LAMEHUG’s LLM-Driven Cyber Intrusion. Retrieved April 21, 2026.](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
- [Stepanic, D. and Bousseaden, S. (2024, May 15). Spring Cleaning with LATRODECTUS: A Potential Replacement for ICEDID. Retrieved September 13, 2024.](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
- [Batista, J. (2024, June 17). Latrodectus, are you coming back?. Retrieved September 13, 2024.](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Remote Administration Tools & Content Staging Malware Report. Retrieved March 16, 2016.](https://web.archive.org/web/20220608001455/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf)
- [Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle. Retrieved October 27, 2021.](https://securelist.com/lazarus-threatneedle/100803/)
- [Pradhan, A. (2022, February 8). LolZarus: Lazarus Group Incorporating Lolbins into Campaigns. Retrieved March 22, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)
- [Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
- [Cybereason Global SOC Team. (n.d.). THREAT ANALYSIS REPORT: LockBit 2.0 - All Paths Lead to Ransom. Retrieved January 24, 2025.](https://www.cybereason.com/blog/threat-analysis-report-lockbit-2.0-all-paths-lead-to-ransom)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part II. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
- [ITOCHU. (2024, January 24). The Endless Struggle Against APT10: Insights from LODEINFO v0.6.6 - v0.7.3 Analysis. Retrieved April 17, 2026.](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [Hsu, K. et al. (2020, June 24). Lucifer: New Cryptojacking and DDoS Hybrid Malware Exploiting High and Critical Vulnerabilities to Infect Windows Devices. Retrieved November 16, 2020.](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [DFIR Report. (2022, March 21). APT35 Automates Initial Access Using ProxyShell. Retrieved May 25, 2022.](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)
- [Mundo, A. (2020, March 26). Ransomware Maze. Retrieved May 18, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
- [Brandt, A., Mackenzie, P.. (2020, September 17). Maze Attackers Adopt Ragnar Locker Virtual Machine Technique. Retrieved October 9, 2020.](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)
- [Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Intel471. (2025, May 14). Threat hunting case study: Medusa ransomware. Retrieved October 15, 2025.](https://www.intel471.com/blog/threat-hunting-case-study-medusa-ransomware)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [Twi1ight. (2015, July 11). AD-Pentest-Script - wmiexec.vbs. Retrieved June 29, 2017.](https://github.com/Twi1ight/AD-Pentest-Script/blob/master/wmiexec.vbs)
- [Symantec. (2020, November 17). Japan-Linked Organizations Targeted in Long-Running and Sophisticated Attack Campaign. Retrieved December 17, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)
- [Check Point Research Team. (2021, August 14). Indra - Hackers Behind Recent Attacks on Iran. Retrieved February 17, 2022.](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
- [Rascagneres, P., Mercer, W. (2017, June 19). Delphi Used To Score Against Palestine. Retrieved November 13, 2018.](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)
- [Tsarfaty, Y. (2018, July 25). Micropsia Malware. Retrieved November 13, 2018.](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [Cybereason Nocturnus Team. (2020, December 9). MOLERATS IN THE CLOUD: New Malware Arsenal Abuses Cloud Platforms in Middle East Espionage Campaign. Retrieved December 22, 2020.](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
- [ESET, et al. (2018, January). Diplomats in Eastern Europe bitten by a Turla mosquito. Retrieved July 3, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 10). MuddyWater expands operations. Retrieved November 2, 2018.](https://securelist.com/muddywater/88059/)
- [ClearSky Cyber Security. (2018, November). MuddyWater Operations in Lebanon and Oman: Using an Israeli compromised domain for a two-stage campaign. Retrieved November 29, 2018.](https://www.clearskysec.com/wp-content/uploads/2018/11/MuddyWater-Operations-in-Lebanon-and-Oman.pdf)
- [Adamitis, D. et al. (2019, May 20). Recent MuddyWater-associated BlackWater campaign shows signs of new anti-detection techniques. Retrieved June 5, 2019.](https://blog.talosintelligence.com/2019/05/recent-muddywater-associated-blackwater.html)
- [FBI, CISA, CNMF, NCSC-UK. (2022, February 24). Iranian Government-Sponsored Actors Conduct Cyber Operations Against Global Government and Commercial Networks. Retrieved September 27, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
- [Anomali Threat Research. (2019, October 7). China-Based APT Mustang Panda Targets Minority Groups, Public and Private Sector Organizations. Retrieved April 12, 2021.](https://www.anomali.com/blog/china-based-apt-mustang-panda-targets-minority-groups-public-and-private-sector-organizations)
- [Counter Threat Unit Research Team. (2019, December 29). BRONZE PRESIDENT Targets NGOs. Retrieved April 13, 2021.](https://www.secureworks.com/research/bronze-president-targets-ngos)
- [Vrabie, V. (2021, April 23). NAIKON – Traces from a Military Cyber-Espionage Operation. Retrieved June 29, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
- [Victor, K.. (2020, May 18). Netwalker Fileless Ransomware Injected via Reflective Loading . Retrieved May 26, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
- [Chiu, A. (2016, June 27). New Ransomware Variant "Nyetya" Compromises Systems Worldwide. Retrieved March 26, 2019.](https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html)
- [US-CERT. (2017, July 1). Alert (TA17-181A): Petya Ransomware. Retrieved March 15, 2019.](https://www.us-cert.gov/ncas/alerts/TA17-181A)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 15). Octopus-infested seas of Central Asia. Retrieved November 14, 2018.](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
- [Davis, S. and Caban, D. (2017, December 19). APT34 - New Targeted Attack in the Middle East. Retrieved December 20, 2017.](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)
- [Symantec Threat Hunter Team. (2023, October 19). Crambus: New Campaign Targets Middle Eastern Government. Retrieved November 27, 2024.](https://www.security.com/threat-intelligence/crambus-middle-east-government)
- [Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [Falcone, R., et al. (2018, September 04). OilRig Targets a Middle Eastern Government and Adds Evasion Techniques to OopsIE. Retrieved September 24, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)
- [Dominik Breitenbacher. (2025, March 18). Operation AkaiRyū: MirrorFace invites Europe to Expo 2025 and revives ANEL backdoor. Retrieved May 22, 2025.](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)
- [Breitenbacher, D and Osis, K. (2020, June 17). OPERATION IN(TER)CEPTION: Targeted Attacks Against European Aerospace and Military Companies. Retrieved December 20, 2021.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_Operation_Interception.pdf)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.](https://github.com/PowerShellMafia/PowerSploit)
- [PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.](http://powersploit.readthedocs.io)
- [Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
- [Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
- [Group IB. (2020, September). LOCK LIKE A PRO. Retrieved November 17, 2024.](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Checkpoint Research. (2021, November 15). Uncovering MosesStaff techniques: Ideology over Money. Retrieved August 11, 2022.](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [Christopher So. (2022, December 20). Raspberry Robin Malware Targets Telecom, Governments. Retrieved May 17, 2024.](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
- [Lei, C., et al. (2018, January 24). Lazarus Campaign Targeting Cryptocurrencies Reveals Remote Controller Tool, an Evolved RATANKBA, and More. Retrieved May 22, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)
- [Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
- [Legezo, D. (2019, January 30). Chafer used Remexi malware to spy on Iran-based foreign diplomatic entities. Retrieved April 17, 2019.](https://securelist.com/chafer-used-remexi-malware/89538/)
- [Secureworks . (2019, September 24). REvil: The GandCrab Connection. Retrieved August 4, 2020.](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
- [Group IB. (2020, May). Ransomware Uncovered: Attackers’ Latest Methods. Retrieved August 5, 2020.](https://www.group-ib.com/whitepapers/ransomware-uncovered.html)
- [Hiroaki, H. (2025, April 30). Earth Kasha Updates TTPs in Latest Campaign Targeting Taiwan and Japan. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
- [Hiroaki, H. (2024, November 26). Guess Who’s Back - The Return of ANEL in the Recent Earth Kasha Spear-phishing Campaign in 2024. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
- [Falcone, R., et al. (2018, July 27). New Threat Actor Group DarkHydrus Targets Middle East Government. Retrieved August 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
- [Lee, B., Falcone, R. (2019, January 18). DarkHydrus delivers new Trojan that can use Google Drive for C2 communications. Retrieved April 17, 2019.](https://unit42.paloaltonetworks.com/darkhydrus-delivers-new-trojan-that-can-use-google-drive-for-c2-communications/)
- [MSTIC. (2022, October 14). New “Prestige” ransomware impacts organizations in Ukraine and Poland. Retrieved January 19, 2023.](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
- [Budaca, E., et al. (2021, August 25). FIN8 Threat Actor Goes Agile with New Sardonic Backdoor. Retrieved August 9, 2023.](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
- [Microsoft Threat Intelligence. (2025, July 22). Disrupting active exploitation of on-premises SharePoint vulnerabilities. Retrieved October 15, 2025.](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/#storm-2603)
- [Ilascu, I. (2020, December 14). Hacking group’s new malware abuses Google and Facebook services. Retrieved December 28, 2020.](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
- [Cristian Souza, Eduardo Ovalle, Ashley Muñoz, & Christopher Zachor. (2024, May 23). ShrinkLocker: Turning BitLocker into ransomware. Retrieved December 7, 2024.](https://securelist.com/ransomware-abuses-bitlocker/112643/)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [Lorber, N. (2021, May 7). Revealing the Snip3 Crypter, a Highly Evasive RAT Loader. Retrieved September 13, 2023.](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
- [Andrew Northern. (2022, November 22). SocGholish, a very real threat from a very fake update. Retrieved February 13, 2024.](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
- [Microsoft 365 Defender Team. (2020, December 28). Using Microsoft 365 Defender to protect against Solorigate. Retrieved January 7, 2021.](https://www.microsoft.com/security/blog/2020/12/28/using-microsoft-365-defender-to-coordinate-protection-against-solorigate/)
- [MSTIC, CDOC, 365 Defender Research Team. (2021, January 20). Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop . Retrieved January 22, 2021.](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
- [Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.](https://citizenlab.org/2016/05/stealth-falcon/)
- [Kaspersky Lab. (2017, March 7). From Shamoon to StoneDrill: Wipers attacking Saudi organizations and beyond. Retrieved March 14, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [Lunghi, D. and Lu, K. (2021, April 9). Iron Tiger APT Updates Toolkit With Evolved SysUpdate Malware. Retrieved November 12, 2021.](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
- [Larson, S. and Wise, J. (2022, February 15). Charting TA2541's Flight. Retrieved September 12, 2023.](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)
- [Pantazopoulos, N., Henry T. (2018, May 18). Emissary Panda – A potential new malicious tool. Retrieved June 25, 2018.](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [Ken Towne, Francis Guibernau. (2023, March 23). Emulating the Politically Motivated Chinese APT Mustang Panda. Retrieved September 10, 2025.](https://www.attackiq.com/2023/03/23/emulating-the-politically-motivated-chinese-apt-mustang-panda/)
- [Holland, A. (2019, March 7). Tricks and COMfoolery: How Ursnif Evades Detection. Retrieved June 10, 2019.](https://www.bromium.com/how-ursnif-evades-detection/)
- [Reaves, J. and Platt, J. (2020, June). Valak Malware and the Connection to Gozi Loader ConfCrew. Retrieved August 31, 2020.](https://assets.sentinelone.com/labs/sentinel-one-valak-i)
- [Check Point Research. (2026, March 12). “Handala Hack” – Unveiling Group’s Modus Operandi. Retrieved April 20, 2026.](https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/)
- [Microsoft Threat Intelligence. (2023, May 24). Volt Typhoon targets US critical infrastructure with living-off-the-land techniques. Retrieved July 27, 2023.](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)
- [NSA et al. (2023, May 24). People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection. Retrieved July 27, 2023.](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)
- [Counter Threat Unit Research Team. (2023, May 24). Chinese Cyberespionage Group BRONZE SILHOUETTE Targets U.S. Government and Defense Organizations. Retrieved July 27, 2023.](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Noerenberg, E., Costis, A., and Quist, N. (2017, May 16). A Technical Analysis of WannaCry Ransomware. Retrieved December 8, 2024.](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)
- [Berry, A., Homan, J., and Eitzman, R. (2017, May 23). WannaCry Malware Profile. Retrieved March 15, 2019.](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
- [Counter Threat Unit Research Team. (2017, May 18). WCry Ransomware Analysis. Retrieved March 26, 2019.](https://www.secureworks.com/research/wcry-ransomware-analysis)
- [The BlackBerry Research & Intelligence Team. (2020, October). BAHAMUT: Hack-for-Hire Masters of Phishing, Fake News, and Fake Apps. Retrieved February 8, 2021.](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)
- [John, E. and Carvey, H. (2019, May 30). Unraveling the Spiderweb: Timelining ATT&CK Artifacts Used by GRIM SPIDER. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)
- [DHS/CISA. (2020, October 28). Ransomware Activity Targeting the Healthcare and Public Health Sector. Retrieved October 28, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-302a)
- [Kimberly Goody, Jeremy Kennelly, Joshua Shilko, Steve Elovitz, Douglas Bienstock. (2020, October 28). Unhappy Hour Special: KEGTAP and SINGLEMALT With a Ransomware Chaser. Retrieved October 28, 2020.](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)
- [Brian Donohue, Katie Nickels, Paul Michaud, Adina Bodkins, Taylor Chapman, Tony Lambert, Jeff Felling, Kyle Rainey, Mike Haag, Matt Graeber, Aaron Didier.. (2020, October 29). A Bazar start: How one hospital thwarted a Ryuk ransomware outbreak. Retrieved October 30, 2020.](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [Lee, B., Falcone, R. (2018, December 12). Dear Joohn: The Sofacy Group’s Global Campaign. Retrieved April 19, 2019.](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)
- [Microsoft. (2021, July 2). Use attack surface reduction rules to prevent malware infection. Retrieved June 24, 2021.](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
- [Coulter, D. et al.. (2019, April 9). Microsoft recommended block rules. Retrieved August 12, 2021.](https://docs.microsoft.com/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [Ballenthin, W., et al. (2015). Windows Management Instrumentation (WMI) Offense, Defense, and Forensics. Retrieved March 30, 2016.](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[RansomHub]] [related_actor:: [[RansomHub]]]
- 🦠 **Tooling Capability Integration:** Executed via malware family [[Qakbot]] [related_malware:: [[Qakbot]]]

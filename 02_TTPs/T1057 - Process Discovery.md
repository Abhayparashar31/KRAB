# Process Discovery

## Description

Adversaries may attempt to get information about running processes on a system. Information obtained could be used to gain an understanding of common software/applications running on systems within the network. Administrator or otherwise elevated access may provide better process details. Adversaries may use the information from Process Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

In Windows environments, adversaries could obtain details on running processes using the Tasklist utility via cmd or Get-Process via PowerShell . Information about processes can also be extracted from the output of Native API calls such as CreateToolhelp32Snapshot . In Mac and Linux, this is accomplished with the ps command. Adversaries may also opt to enumerate processes via /proc . ESXi also supports use of the ps command, as well as esxcli system process list . [1] [2]

On network devices, Network Device CLI commands such as show processes can be used to display current running processes. [3] [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries enumerated current running processes using tasklist . [5] |
| S0065 | 4H RAT | 4H RAT has the capability to obtain a listing of running processes (including loaded modules). [6] |
| S0045 | ADVSTORESHELL | ADVSTORESHELL can list running processes. [7] |
| S0331 | Agent Tesla | Agent Tesla can list the current running processes on the system. [8] |
| S1129 | Akira | Akira verifies the deletion of volume shadow copies by checking for the existence of the process ID related to the process created to delete these items. [9] |
| G0138 | Andariel | Andariel has used tasklist to enumerate processes and find a specific string. [10] |
| S1133 | Apostle | Apostle retrieves a list of all running processes on a victim host, and stops all services containing the string "sql," likely to propagate ransomware activity to database files. [11] |
| S0622 | AppleSeed | AppleSeed can enumerate the current process on a compromised host. [12] |
| G0006 | APT1 | APT1 gathered a list of running processes on the system using tasklist /v . [13] |
| G0007 | APT28 | An APT28 loader Trojan will enumerate the victim's processes searching for explorer.exe if its current process does not have necessary permissions. [14] |
| G0022 | APT3 | APT3 has a tool that can list out currently running processes. [15] [16] |
| G0067 | APT37 | APT37 's Freenki malware lists running processes using the Microsoft Windows API. [17] |
| G0082 | APT38 | APT38 leveraged Sysmon to understand the processes, services in the organization. [18] |
| G1023 | APT5 | APT5 has used Windows-based utilities to carry out tasks including tasklist.exe. [19] |
| S0456 | Aria-body | Aria-body has the ability to enumerate loaded modules for a process. [20] . |
| S9031 | AshTag | The AshTag AshenOrchestrator component has process management functionality. [21] |
| S0373 | Astaroth | Astaroth searches for different processes on the system. [22] |
| S1087 | AsyncRAT | AsyncRAT can examine running processes to determine if a debugger is present. [23] |
| S0640 | Avaddon | Avaddon has collected information about running processes. [24] |
| S0473 | Avenger | Avenger has the ability to use Tasklist to identify running processes. [25] |
| S1053 | AvosLocker | AvosLocker has discovered system processes by calling RmGetList . [26] |
| S0344 | Azorult | Azorult can collect a list of running processes by calling CreateToolhelp32Snapshot. [27] [28] |
| S0638 | Babuk | Babuk has the ability to check running processes on a targeted system. [29] [30] [31] |
| S0414 | BabyShark | BabyShark has executed the tasklist command. [32] |
| S0093 | Backdoor.Oldrea | Backdoor.Oldrea collects information about running processes. [33] |
| S0031 | BACKSPACE | BACKSPACE may collect information about running processes. [34] |
| S0606 | Bad Rabbit | Bad Rabbit can enumerate all running processes to compare hashes. [35] |
| S1081 | BADHATCH | BADHATCH can retrieve a list of running processes from a compromised machine. [36] |
| S0239 | Bankshot | Bankshot identifies processes and collects the process ids. [37] |
| S0534 | Bazar | Bazar can identity the current process on a compromised host. [38] |
| S0127 | BBSRAT | BBSRAT can list running processes. [39] |
| S0017 | BISCUIT | BISCUIT has a command to enumerate running processes and identify their owners. [40] |
| S0268 | Bisonal | Bisonal can obtain a list of running processes on the victim’s machine. [41] [42] [43] |
| S0069 | BLACKCOFFEE | BLACKCOFFEE has the capability to discover processes. [44] |
| S0089 | BlackEnergy | BlackEnergy has gathered a process list by using Tasklist .exe. [45] [46] [47] |
| S0657 | BLUELIGHT | BLUELIGHT can collect process filenames and SID authority level. [48] |
| S0486 | Bonadan | Bonadan can use the ps command to discover other cryptocurrency miners active on the system. [49] |
| S0252 | Brave Prince | Brave Prince lists the running processes. [50] |
| S9015 | BRICKSTORM | BRICKSTORM has the ability to check if it is running as an active child process through the detection of a specific environment variable. [51] |
| S1063 | Brute Ratel C4 | Brute Ratel C4 can enumerate all processes and locate specific process IDs (PIDs). [52] |
| S1039 | Bumblebee | Bumblebee can identify processes associated with analytical tools. [53] [54] [55] |
| S0482 | Bundlore | Bundlore has used the ps command to list processes. [56] |
| C0015 | C0015 | During C0015 , the threat actors used the tasklist /s command as well as taskmanager to obtain a list of running processes. [57] |
| S0693 | CaddyWiper | CaddyWiper can obtain a list of current processes. [58] |
| S0351 | Cannon | Cannon can obtain a list of processes running on the system. [59] [60] |
| S0030 | Carbanak | Carbanak lists running processes. [61] |
| S0484 | Carberp | Carberp has collected a list of running processes. [62] |
| S0335 | Carbon | Carbon can list the processes on the victim’s machine. [63] |
| S0348 | Cardinal RAT | Cardinal RAT contains watchdog functionality that ensures its process is always running, else spawns a new instance. [64] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell can gather a list of processes running on the machine. [65] |
| S0674 | CharmPower | CharmPower has the ability to list running processes through the use of tasklist . [66] |
| S0144 | ChChes | ChChes collects its process identifier (PID) on the victim. [67] |
| G0114 | Chimera | Chimera has used tasklist to enumerate processes. [68] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP can check if a process name contains "creensaver." [69] |
| S0660 | Clambling | Clambling can enumerate processes on a targeted system. [70] |
| S0611 | Clop | Clop can enumerate all processes on the victim's machine. [71] |
| S1105 | COATHANGER | COATHANGER will query running process information to determine subsequent program execution flow. [72] |
| S0154 | Cobalt Strike | Cobalt Strike 's Beacon payload can collect information on process details. [73] [74] [75] |
| S0244 | Comnie | Comnie uses the tasklist to view running processes on the victim’s machine. [76] |
| S0575 | Conti | Conti can enumerate through all open processes to search for any that have the string "sql" in their process name. [77] |
| S0115 | Crimson | Crimson contains a command to list processes. [78] [79] [80] |
| S0625 | Cuba | Cuba can enumerate processes running on a victim's machine. [81] |
| S1153 | Cuckoo Stealer | Cuckoo Stealer can use ps aux to enumerate running processes. [82] |
| S0687 | Cyclops Blink | Cyclops Blink can enumerate the process it is currently running under. [83] |
| S0497 | Dacls | Dacls can collect data on running and parent processes. [84] |
| S0334 | DarkComet | DarkComet can list active processes running on the victim’s machine. [85] |
| S1111 | DarkGate | DarkGate performs various checks for running processes, including security software by looking for hard-coded process name values. [86] [87] |
| G0012 | Darkhotel | Darkhotel malware can collect a list of running processes on a system. [88] |
| S1066 | DarkTortilla | DarkTortilla can enumerate a list of running processes on a compromised system. [89] |
| G0009 | Deep Panda | Deep Panda uses the Microsoft Tasklist utility to list processes running on systems. [90] |
| S0021 | Derusbi | Derusbi collects current and parent process IDs. [91] [92] |
| S0659 | Diavol | Diavol has used CreateToolhelp32Snapshot , Process32First , and Process32Next API calls to enumerate the running processes in the system. [93] |
| S0600 | Doki | Doki has searched for the current process’s PID. [94] |
| S0695 | Donut | Donut includes subprojects that enumerate and identify information about Process Injection candidates. [95] |
| S0472 | down_new | down_new has the ability to list running processes on a compromised host. [25] |
| S0694 | DRATzarus | DRATzarus can enumerate and examine running processes to determine if a debugger is present. [96] |
| S0567 | Dtrack | Dtrack ’s dropper can list all running processes. [97] [98] |
| S0038 | Duqu | The discovery modules used with Duqu can collect information on process details. [99] |
| S1159 | DUSTTRAP | DUSTTRAP can enumerate running processes. [100] |
| S0062 | DustySky | DustySky collects information about running processes from victims. [101] [102] |
| G1006 | Earth Lusca | Earth Lusca has used Tasklist to obtain information from a compromised host. [103] |
| S0605 | EKANS | EKANS looks for processes from a hard-coded list. [104] [105] [106] |
| S0081 | Elise | Elise enumerates processes via the tasklist command. [107] |
| S0064 | ELMER | ELMER is capable of performing process listings. [108] |
| S1247 | Embargo | Embargo has utilized MS4Killer to detect running processes on the victim device. [109] Embargo has also captured a snapshot of active running processes using the Windows API CreateToolHelp32Snapshot() . [110] |
| S0367 | Emotet | Emotet has been observed enumerating local processes. [111] |
| S0363 | Empire | Empire can find information about processes running on local and remote systems. [112] [113] |
| S0091 | Epic | Epic uses the tasklist /v command to obtain a list of processes. [114] [115] |
| S0396 | EvilBunny | EvilBunny has used EnumProcesses() to identify how many process are running in the environment. [116] |
| S0512 | FatDuke | FatDuke can list running processes on the localhost. [117] |
| S0267 | FELIXROOT | FELIXROOT collects a list of running processes. [118] |
| G0046 | FIN7 | FIN7 has used the PowerShell script 3CF9.ps1 to perform process discovery by executing tasklist /v . Additionally, WsTaskLoad.exe executes tasklist /v to perform process discovery. [119] |
| S0355 | Final1stspy | Final1stspy obtains a list of running processes. [120] |
| S0182 | FinFisher | FinFisher checks its parent process for indications that it is running in a sandbox setup. [121] [122] |
| S0696 | Flagpro | Flagpro has been used to run the tasklist command on a compromised system. [123] |
| S0661 | FoggyWeb | FoggyWeb 's loader can enumerate all Common Language Runtimes (CLRs) and running Application Domains in the compromised AD FS server's Microsoft.IdentityServer.ServiceHost.exe process. [124] |
| S0503 | FrameworkPOS | FrameworkPOS can enumerate and exclude selected processes on a compromised host to speed execution of memory scraping. [125] |
| C0001 | Frankenstein | During Frankenstein , the threat actors used Empire to obtain a list of all running processes. [113] |
| S0277 | FruitFly | FruitFly has the ability to list processes on the system. [126] |
| S1044 | FunnyDream | FunnyDream has the ability to discover processes, including Bka.exe and BkavUtil.exe . [127] |
| C0007 | FunnyDream | During FunnyDream , the threat actors used Tasklist on targeted systems. [127] |
| S0410 | Fysbis | Fysbis can collect information about running processes. [128] |
| G0047 | Gamaredon Group | Gamaredon Group has used tools to enumerate processes on target hosts including Process Explorer. [129] [130] [131] |
| S0666 | Gelsemium | Gelsemium can enumerate running processes. [132] |
| S0049 | GeminiDuke | GeminiDuke collects information on running processes and environment variables from the victim. [133] |
| S0460 | Get2 | Get2 has the ability to identify running processes on an infected host. [134] |
| S0032 | gh0st RAT | gh0st RAT has the capability to list processes. [135] |
| S0249 | Gold Dragon | Gold Dragon checks the running processes on the victim’s machine. [50] |
| S0477 | Goopy | Goopy has checked for the Google Updater process to ensure Goopy was loaded properly. [136] |
| S0531 | Grandoreiro | Grandoreiro can identify installed security tools based on process names. [137] |
| S0237 | GravityRAT | GravityRAT lists the running processes on the system. [138] |
| G0125 | HAFNIUM | HAFNIUM has used tasklist to enumerate processes. [139] |
| S0151 | HALFBAKED | HALFBAKED can obtain information about running processes on the victim. [140] |
| S1229 | Havoc | Havoc can enumerate processes on targeted hosts. [141] [142] [143] |
| S0617 | HELLOKITTY | HELLOKITTY can search for specific processes to terminate. [144] |
| S0170 | Helminth | Helminth has used Tasklist to get information on processes. [14] |
| G1001 | HEXANE | HEXANE has enumerated processes on targeted systems. [145] |
| S1027 | Heyoka Backdoor | Heyoka Backdoor can gather process information. [146] |
| S9023 | HiddenFace | HiddenFace can check running processes against a list of blocklisted applications. [147] |
| G0126 | Higaisa | Higaisa ’s shellcode attempted to find the process ID of the current process. [148] |
| S1230 | HIUPAN | HIUPAN has conducted process discovery to identify the PUBLOAD malware under the process WCBrowserWatcher.exe and will launch it from an install directory if it is not found. [149] |
| S0431 | HotCroissant | HotCroissant has the ability to list running processes on the infected host. [150] |
| S0203 | Hydraq | Hydraq creates a backdoor through which remote attackers can monitor processes. [151] [152] |
| S0278 | iKitten | iKitten lists the current processes running. [126] |
| S0434 | Imminent Monitor | Imminent Monitor has a "Process Watcher" feature to monitor processes in case the client ever crashes or gets closed. [153] |
| S1139 | INC Ransomware | INC Ransomware can use the Microsoft Win32 Restart Manager to kill processes with a specific handle or that are accessing resources it wants to encrypt. [154] |
| G0100 | Inception | Inception has used a reconnaissance module to identify active processes and other associated loaded modules. [155] |
| S1072 | Industroyer2 | Industroyer2 has the ability to cyclically enumerate running processes such as PServiceControl.exe, PService_PDD.exe, and other targets supplied through a hardcoded configuration. [156] |
| S1245 | InvisibleFerret | InvisibleFerret has the capability to query installed programs and running processes. [157] InvisibleFerret has also identified running processes using the Python project "psutil". [158] |
| S0260 | InvisiMole | InvisiMole can obtain a list of running processes. [159] [160] |
| S1132 | IPsec Helper | IPsec Helper can identify the process it is currently running under and its number, and pass this back to a command and control node. [11] |
| S0581 | IronNetInjector | IronNetInjector can identify processes via C# methods such as GetProcessesByName and running Tasklist with the Python os.popen function. [161] |
| S0015 | Ixeshe | Ixeshe can list running processes. [162] |
| S0528 | Javali | Javali can monitor processes for open browsers and custom banking applications. [163] |
| S0044 | JHUHUGIT | JHUHUGIT obtains a list of running processes on the victim. [164] [165] |
| S0201 | JPIN | JPIN can list running processes. [166] |
| S0283 | jRAT | jRAT can query and kill system processes. [167] |
| S0088 | Kasidet | Kasidet has the ability to search for a given process name in processes currently running in the system. [168] |
| S0265 | Kazuar | Kazuar obtains a list of running processes through WMI querying and the ps command. [169] |
| G0004 | Ke3chang | Ke3chang performs process discovery using tasklist commands. [170] [171] |
| S0271 | KEYMARBLE | KEYMARBLE can obtain a list of running processes on the system. [172] |
| S0607 | KillDisk | KillDisk has called GetCurrentProcess . [173] |
| G0094 | Kimsuky | Kimsuky can gather a list of all processes running on a victim's machine. [174] Kimsuky has also obtained running processes on the victim device utilizing PowerShell cmdlet Get-Process . [175] |
| S0599 | Kinsing | Kinsing has used ps to list processes. [176] |
| S0162 | Komplex | The OsInfo function in Komplex collects a running process list. [177] |
| S0356 | KONNI | KONNI has used the command cmd /c tasklist to get a snapshot of the current processes on the target machine. [178] [179] |
| S1075 | KOPILUWAK | KOPILUWAK can enumerate current running processes on the targeted machine. [180] |
| C0035 | KV Botnet Activity | Scripts associated with KV Botnet Activity initial deployment can identify processes related to security tools and other botnet families for follow-on disabling during installation. [181] |
| S0236 | Kwampirs | Kwampirs collects a list of running services with the command tasklist /v . [182] |
| S9035 | LAMEHUG | LAMEHUG can gather process information on targeted systems. [183] [184] |
| S1160 | Latrodectus | Latrodectus can enumerate running processes including process grandchildren on targeted hosts. [185] [186] [187] |
| G0032 | Lazarus Group | Several Lazarus Group malware families gather a list of running processes on a victim system and send it to their C2 server. A Destover-like variant used by Lazarus Group also gathers process times. [188] [189] [190] [191] [84] [192] |
| S1185 | LightSpy | If sent the command 16002 , LightSpy uses the NSWorkspace runningApplications() method to collect the process ID, path to the executable, bundle information, and the filename of the executable for all running applications. [193] |
| S0211 | Linfo | Linfo creates a backdoor through which remote attackers can retrieve a list of running processes. [194] |
| S0681 | Lizar | Lizar has a plugin designed to obtain a list of processes. [195] [196] |
| S1199 | LockBit 2.0 | LockBit 2.0 can determine if a running process has administrative privileges and terminate processes that interfere with encryption or exfiltration. [197] [198] |
| S1202 | LockBit 3.0 | LockBit 3.0 can identify and terminate specific services. [199] [200] |
| S9020 | LODEINFO | LODEINFO can kill a process using specific process ID. [201] [202] |
| S0582 | LookBack | LookBack can list running processes. [203] |
| S0451 | LoudMiner | LoudMiner used the ps command to monitor the running processes on the system. [204] |
| S9036 | LP-Notes | LP-Notes has searched for the process taskhostw.exe. [205] |
| S0532 | Lucifer | Lucifer can identify the process that owns remote connections. [206] |
| S1141 | LunarWeb | LunarWeb has used shell commands to list running processes. [207] |
| S0409 | Machete | Machete has a component to check for running processes to look for web browsers. [208] |
| S1016 | MacMa | MacMa can enumerate running processes. [209] |
| S1048 | macOS.OSAMiner | macOS.OSAMiner has used ps ax | grep <name> | grep -v grep | ... and ps ax | grep -E... to conduct process discovery. [210] |
| S1060 | Mafalda | Mafalda can enumerate running processes on a machine. [211] |
| G0059 | Magic Hound | Magic Hound malware can list running processes. [212] |
| S0652 | MarkiRAT | MarkiRAT can search for different processes on a system. [213] |
| S0449 | Maze | Maze has gathered all of the running system processes. [214] |
| G1051 | Medusa Group | Medusa Group has utilized a hard-coded security tool process list that identifies and terminates using an undocumented IOCTL code 0x222094. [215] |
| S1244 | Medusa Ransomware | Medusa Ransomware has utilized an encoded list of the processes that it detects and terminates. [215] [216] [217] |
| S1191 | Megazord | Megazord can terminate a list of specified services and processes. [218] |
| S1059 | metaMain | metaMain can enumerate the processes that run on the platform. [211] [219] |
| S0455 | Metamorfo | Metamorfo has performed process name checks and has monitored applications. [220] |
| S0688 | Meteor | Meteor can check if a specific process is running, such as Kaspersky's avp.exe . [221] |
| S1146 | MgBot | MgBot includes a module for establishing a process watchdog for itself, identifying if the MgBot process is still running. [222] |
| G1054 | MirrorFace | MirrorFace has used Tasklist on compromised hosts for discovery. [223] |
| S1122 | Mispadu | Mispadu can enumerate the running processes on a compromised host. [224] |
| S0079 | MobileOrder | MobileOrder has a command to upload information about all running processes to its C2 server. [225] |
| G0021 | Molerats | Molerats actors obtained a list of active processes on the victim and sent them to C2 servers. [101] |
| S0149 | MoonWind | MoonWind has a command to return a list of running processes. [226] |
| S0256 | Mosquito | Mosquito runs tasklist to obtain running processes. [227] |
| S9032 | MuddyViper | MuddyViper has the ability to collect running processes. [205] |
| G0069 | MuddyWater | MuddyWater has used malware to obtain a list of running processes on the system. [228] [229] |
| G0129 | Mustang Panda | Mustang Panda has used tasklist /v to determine active process information. [230] Mustang Panda has also used TONESHELL malware to check the process name and process path to ensure it matches the expected one prior to triggering a custom exception handler. [231] |
| S0247 | NavRAT | NavRAT uses tasklist /v to check running processes. [232] |
| S0630 | Nebulae | Nebulae can enumerate processes on a target system. [233] |
| S0034 | NETEAGLE | NETEAGLE can send process listings over the C2 channel. [34] |
| S0198 | NETWIRE | NETWIRE can discover processes on compromised hosts. [234] |
| S1090 | NightClub | NightClub has the ability to use GetWindowThreadProcessId to identify the process behind a specified window. [235] |
| S1147 | Nightdoor | Nightdoor can collect information on installed applications via Windows registry keys, as well as collecting information on running processes. [236] |
| S1100 | Ninja | Ninja can enumerate processes on a targeted host. [237] [238] |
| S0385 | njRAT | njRAT can search a list of running processes for Tr.exe. [239] |
| S1107 | NKAbuse | NKAbuse will check victim systems to ensure only one copy of the malware is running. [240] |
| S0644 | ObliqueRAT | ObliqueRAT can check for blocklisted process names on a compromised host. [241] |
| S0346 | OceanSalt | OceanSalt can collect the name and ID for every process running on the system. [242] |
| G0049 | OilRig | OilRig has run tasklist on a victim's machine and used infostealers to capture processes. [243] [244] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors used the tasklist command as part of their advanced reconnaissance. [245] |
| C0006 | Operation Honeybee | During Operation Honeybee , the threat actors obtained a list of running processes on a victim machine using cmd /c tasklist > %temp%\temp.ini . [246] |
| C0014 | Operation Wocao | During Operation Wocao , the threat actors used tasklist to collect a list of running processes on an infected system. [247] |
| S0229 | Orz | Orz can gather a process list from the victim. [248] |
| S1017 | OutSteel | OutSteel can identify running processes on a compromised host. [249] |
| S0626 | P8RAT | P8RAT can check for specific processes associated with virtual environments. [250] |
| S1233 | PAKLOG | PAKLOG has detected and logged the full path of processes active in the foreground using Windows API calls. [251] |
| S0664 | Pandora | Pandora can monitor processes on a compromised host. [252] |
| S0208 | Pasam | Pasam creates a backdoor through which remote attackers can retrieve lists of running processes. [253] |
| S1050 | PcShare | PcShare can obtain a list of running processes on a compromised host. [127] |
| S0517 | Pillowmint | Pillowmint can iterate through running processes every six seconds collecting a list of processes to capture from later. [254] |
| S0501 | PipeMon | PipeMon can iterate over the running processes to find a suitable injection target. [255] |
| S0254 | PLAINTEE | PLAINTEE performs the tasklist command to list running processes. [256] |
| G1040 | Play | Play has used the information stealer Grixba to check for a list of security processes. [257] |
| S0435 | PLEAD | PLEAD has the ability to list processes on the compromised host. [258] |
| S0013 | PlugX | PlugX has a module to list the processes running on a machine. [259] |
| S0428 | PoetRAT | PoetRAT has the ability to list all running processes. [260] |
| S0216 | POORAIM | POORAIM can enumerate processes. [261] |
| G0033 | Poseidon Group | After compromising a victim, Poseidon Group lists all running processes. [262] |
| S0139 | PowerDuke | PowerDuke has a command to list the victim's processes. [263] |
| S0441 | PowerShower | PowerShower has the ability to deploy a reconnaissance module to retrieve a list of the active processes. [264] |
| S0194 | PowerSploit | PowerSploit 's Get-ProcessTokenPrivilege Privesc-PowerUp module can enumerate privileges for a given process. [265] [266] |
| S0393 | PowerStallion | PowerStallion has been used to monitor process lists. [267] |
| S0223 | POWERSTATS | POWERSTATS has used get_tasklist to discover processes on the compromised host. [268] |
| S0184 | POWRUNER | POWRUNER may collect process information by running tasklist on a victim. [269] |
| S0238 | Proxysvc | Proxysvc lists processes running on the system. [191] |
| S1228 | PUBLOAD | PUBLOAD has used tasklist to gather running processes on victim host. [149] PUBLOAD has also leveraged the OpenEventA Windows API function to check whether the same process was already running. [231] |
| S0192 | Pupy | Pupy can list the running processes and get the process ID and parent process’s ID. [270] |
| S9019 | PureCrypter | PureCrypter can enumerate processes on compromised hosts. [271] |
| S0650 | QakBot | QakBot has the ability to check running processes. [272] |
| S1242 | Qilin | Qilin can define specific processes to be terminated or left alone at execution. [273] [274] [275] [276] [277] [278] |
| S0629 | RainyDay | RainyDay can enumerate processes on a target system. [233] |
| S0458 | Ramsay | Ramsay can gather a list of running processes by using Tasklist . [279] |
| S1212 | RansomHub | RansomHub can stop processes associated with files currently in use to maximize the impact of encryption. [280] |
| S1130 | Raspberry Robin | Raspberry Robin can identify processes running on the victim machine, such as security software, during execution. [281] [282] |
| S0241 | RATANKBA | RATANKBA lists the system’s processes. [283] [284] |
| S0662 | RCSession | RCSession can identify processes based on PID. [285] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 used malware capable of reading the PID for the Junos OS snmpd daemon. [286] |
| S0332 | Remcos | Remcos can discover running processes on compromised machines. [287] |
| S0125 | Remsec | Remsec can obtain a process list from the victim. [288] |
| S0448 | Rising Sun | Rising Sun can enumerate all running processes and process information on an infected machine. [289] |
| G0106 | Rocke | Rocke can detect a running process's PID on the infected machine. [290] |
| S0270 | RogueRobin | RogueRobin checks the running processes for evidence it may be running in a sandbox environment. It specifically enumerates processes for Wireshark and Sysinternals. [291] |
| S0240 | ROKRAT | ROKRAT can list the current running processes on the system. [292] [293] |
| S1078 | RotaJakiro | RotaJakiro can monitor the /proc/[PID] directory of known RotaJakiro processes as a part of its persistence when executing with non-root permissions. If the process is found dead, it resurrects the process. RotaJakiro processes can be matched to an associated Advisory Lock, in the /proc/locks folder, to ensure it doesn't spawn more than one process. [294] |
| S1073 | Royal | Royal can use GetCurrentProcess to enumerate processes. [295] |
| S0148 | RTM | RTM can obtain information about process integrity levels. [296] |
| S0446 | Ryuk | Ryuk has called CreateToolhelp32Snapshot to enumerate all running processes. [297] |
| S1210 | Sagerunex | Sagerunex identifies the explorer.exe process on the executing system. [298] |
| S1018 | Saint Bot | Saint Bot has enumerated running processes on a compromised host to determine if it is running under the process name dfrgui.exe . [249] |
| S1085 | Sardonic | Sardonic has the ability to execute the tasklist command. [299] |
| S0461 | SDBbot | SDBbot can enumerate a list of running processes on a compromised machine. [300] |
| S0345 | Seasalt | Seasalt has a command to perform a process listing. [40] |
| S0596 | ShadowPad | ShadowPad has collected the PID of a malicious process. [301] |
| S0445 | ShimRatReporter | ShimRatReporter listed all running processes on the machine. [302] |
| S0063 | SHOTPUT | SHOTPUT has a command to obtain a process listing. [303] |
| S1178 | ShrinkLocker | ShrinkLocker checks whether the Bitlocker Drive Encryption Tools service is running. [304] |
| G0121 | Sidewinder | Sidewinder has used tools to identify running processes on the victim's machine. [305] |
| S0692 | SILENTTRINITY | SILENTTRINITY can enumerate processes, including properties to determine if they have the Common Language Runtime (CLR) loaded. [306] |
| S0468 | Skidmap | Skidmap has monitored critical processes to ensure resiliency. [307] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA has enumerated processes by ID, name, or privileges. [308] |
| S1124 | SocGholish | SocGholish can list processes on targeted hosts. [309] |
| S0273 | Socksbot | Socksbot can list all running processes. [310] |
| S0627 | SodaMaster | SodaMaster can search a list of running processes. [250] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 used multiple command-line utilities to enumerate running processes. [311] [312] [313] |
| S0615 | SombRAT | SombRAT can use the getprocesslist command to enumerate processes on a compromised host. [314] [144] [315] |
| S0516 | SoreFang | SoreFang can enumerate processes on a victim machine through use of Tasklist . [316] |
| S9024 | SPAWNCHIMERA | SPAWNCHIMERA has searched for running processes to include web or dsmdm. [317] [318] |
| G0038 | Stealth Falcon | Stealth Falcon malware gathers a list of running processes. [319] |
| G1053 | Storm-0501 | Storm-0501 has discovered running processes through tasklist.exe . [320] |
| S0142 | StreamEx | StreamEx has the ability to enumerate processes. [321] |
| S0491 | StrongPity | StrongPity can determine if a user is logged in by checking to see if explorer.exe is running. [322] |
| S0559 | SUNBURST | SUNBURST collected a list of process names that were hashed using a FNV-1a + XOR algorithm to check against similarly-hashed hardcoded blocklists. [323] |
| S0562 | SUNSPOT | SUNSPOT monitored running processes for instances of MsBuild.exe by hashing the name of each running process and comparing it to the corresponding value 0x53D525 . It also extracted command-line arguments and individual arguments from the running MsBuild.exe process to identify the directory path of the Orion software Visual Studio solution. [324] |
| S1064 | SVCReady | SVCReady can collect a list of running processes from an infected host. [325] |
| S0018 | Sykipot | Sykipot may gather a list of running processes by running tasklist /v . [326] |
| S0242 | SynAck | SynAck enumerates all running processes. [327] [328] |
| S0464 | SYSCON | SYSCON has the ability to use Tasklist to list running processes. [329] |
| S9001 | SystemBC | SystemBC has the ability to enumerate running processes. [330] |
| S0663 | SysUpdate | SysUpdate can collect information about running processes. [331] |
| S0011 | Taidoor | Taidoor can use GetCurrentProcessId for process discovery. [332] |
| S0586 | TAINTEDSCRIBE | TAINTEDSCRIBE can execute ProcessList for process discovery. [333] |
| S0467 | TajMahal | TajMahal has the ability to identify running processes and associated plugins on an infected host. [334] |
| S0057 | Tasklist | Tasklist can be used to discover processes running on a system. [335] |
| G0139 | TeamTNT | TeamTNT has searched for rival malware and removes it if found. [336] TeamTNT has also searched for running processes containing the strings aliyun or liyun to identify machines running Alibaba Cloud Security tools. [337] |
| S0595 | ThiefQuest | ThiefQuest obtains a list of running processes using the function kill_unwanted . [338] |
| G1022 | ToddyCat | ToddyCat has run cmd /c start /b tasklist to enumerate processes. [238] |
| S1239 | TONESHELL | TONESHELL has checked the process name and process path to ensure it matches the expected one prior to triggering a custom exception handler. [231] TONESHELL has also searched for running antivirus processes to include ESET’s antivirus associated executables ekrn.exe and egui.exe. [339] |
| S9012 | TRAILBLAZE | TRAILBLAZE has conducted process discovery by searching for specific named processes such as /home/bin/web . [340] [341] |
| S0266 | TrickBot | TrickBot uses module networkDll for process list discovery. [342] [343] |
| S0094 | Trojan.Karagany | Trojan.Karagany can use Tasklist to collect a list of running tasks. [33] [344] |
| G0081 | Tropic Trooper | Tropic Trooper is capable of enumerating the running processes on the system using pslist . [345] [346] |
| S0436 | TSCookie | TSCookie has the ability to list processes on the infected host. [347] |
| G0010 | Turla | Turla surveys a system upon check-in to discover running processes using the tasklist /v command. [114] Turla RPC backdoors have also enumerated processes associated with specific open ports or named pipes. [267] |
| S0333 | UBoatRAT | UBoatRAT can list running processes on the system. [348] |
| G1048 | UNC3886 | UNC3886 has run scripts to list all running processes on a guest VM from an ESXi host. [349] |
| S1164 | UPSTYLE | UPSTYLE has the ability to read /proc/self/cmdline to see if it is running as a monitored process. [350] |
| S0022 | Uroburos | Uroburos can use its Process List command to enumerate processes on compromised hosts. [351] |
| S0386 | Ursnif | Ursnif has gathered information about running processes. [352] [353] |
| S0452 | USBferry | USBferry can use tasklist to gather information about the process running on the infected system. [346] |
| S0476 | Valak | Valak has the ability to enumerate running processes on a compromised host. [354] |
| S0257 | VERMIN | VERMIN can get a list of the processes and running tasks on the system. [355] |
| S0180 | Volgmer | Volgmer can gather a list of processes. [356] |
| G1017 | Volt Typhoon | Volt Typhoon has enumerated running processes on targeted systems including through the use of Tasklist . [357] [358] [359] |
| S0670 | WarzoneRAT | WarzoneRAT can obtain a list of processes on a compromised host. [360] |
| S0579 | Waterbear | Waterbear can identify the process for a specific security product. [361] |
| G0112 | Windshift | Windshift has used malware to enumerate active processes. [362] |
| S0219 | WINERACK | WINERACK can enumerate processes. [261] |
| S0059 | WinMM | WinMM sets a WH_CBT Windows hook to collect information on process creation. [363] |
| S0141 | Winnti for Windows | Winnti for Windows can check if the explorer.exe process is responsible for calling its install function. [364] |
| G0044 | Winnti Group | Winnti Group looked for a specific process running on infected servers. [365] |
| S1065 | Woody RAT | Woody RAT can call NtQuerySystemProcessInformation with SystemProcessInformation to enumerate all running processes, including associated information such as PID, parent PID, image name, and owner. [366] |
| S0161 | XAgentOSX | XAgentOSX contains the getProcessList function to run ps aux to get running processes. [367] |
| S0248 | yty | yty gets an output of running processes using the tasklist command. [368] |
| S0251 | Zebrocy | Zebrocy uses the tasklist and wmic process get Capture, ExecutablePath commands to gather the processes running on the system. [59] [369] [60] [370] [371] |
| S0330 | Zeus Panda | Zeus Panda checks for running processes on the victim’s machine. [372] |
| S1114 | ZIPLINE | ZIPLINE can identify running processes and their names. [373] |
| S0672 | Zox | Zox has the ability to list processes. [374] |
| S0412 | ZxShell | ZxShell has a command, ps, to obtain a listing of processes on the system. [375] |
| S1013 | ZxxZ | ZxxZ has created a snapshot of running processes using CreateToolhelp32Snapshot . [376] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0034 | Detection of Adversarial Process Discovery Behavior | AN0095 | Identifies adversary behavior that launches commands or invokes APIs to enumerate active processes (e.g., tasklist.exe, Get-Process, or CreateToolhelp32Snapshot). Detects execution combined with parent process lineage, network session context, or remote origin. |
| AN0096 | Detects execution of common process enumeration utilities (e.g., ps, top, htop) or access to /proc with suspicious ancestry. Correlates command usage with interactive shell context and user role. |  |  |
| AN0097 | Monitors execution of ps, top, or launchctl with unusual parent processes or from terminal scripts. Also detects AppleScript-based process listing or system_profiler SPApplicationsDataType misuse. |  |  |
| AN0098 | Detects process enumeration using esxcli system process list or ps on ESXi shell or via unauthorized SSH sessions. Correlates with interactive sessions and abnormal user roles. |  |  |
| AN0099 | Monitors CLI-based execution of show process or equivalent on routers/switches. Correlates unusual device access, unauthorized roles, or config mode changes. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0034 | Detection of Adversarial Process Discovery Behavior | AN0095 | Identifies adversary behavior that launches commands or invokes APIs to enumerate active processes (e.g., tasklist.exe, Get-Process, or CreateToolhelp32Snapshot). Detects execution combined with parent process lineage, network session context, or remote origin. |
| AN0096 | Detects execution of common process enumeration utilities (e.g., ps, top, htop) or access to /proc with suspicious ancestry. Correlates command usage with interactive shell context and user role. |  |  |
| AN0097 | Monitors execution of ps, top, or launchctl with unusual parent processes or from terminal scripts. Also detects AppleScript-based process listing or system_profiler SPApplicationsDataType misuse. |  |  |
| AN0098 | Detects process enumeration using esxcli system process list or ps on ESXi shell or via unauthorized SSH sessions. Correlates with interactive sessions and abnormal user roles. |  |  |
| AN0099 | Monitors CLI-based execution of show process or equivalent on routers/switches. Correlates unusual device access, unauthorized roles, or config mode changes. |  |  |

---

## References

- [Zhongyuan Hau (Aaron), Ren Jie Yow, and Yoav Mazor. (2025, January 21). ESXi Ransomware Attacks: Stealthy Persistence through. Retrieved March 27, 2025.](https://www.sygnia.co/blog/esxi-ransomware-ssh-tunneling-defense-strategies/)
- [Michael Dawson. (2021, August 30). Hypervisor Jackpotting, Part 2: eCrime Actors Increase Targeting of ESXi Servers with Ransomware. Retrieved March 26, 2025.](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
- [US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved October 19, 2020.](https://www.us-cert.gov/ncas/alerts/TA18-106A)
- [Cisco. (2022, August 16). show processes - . Retrieved July 13, 2022.](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/show_monitor_permit_list_through_show_process_memory.html#wp3599497760)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Crowdstrike Global Intelligence Team. (2014, June 9). CrowdStrike Intelligence Report: Putter Panda. Retrieved January 22, 2016.](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)
- [ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
- [Zhang, X. (2017, June 28). In-Depth Analysis of A New Variant of .NET Malware AgentTesla. Retrieved November 5, 2018.](https://www.fortinet.com/blog/threat-research/in-depth-analysis-of-net-malware-javaupdtr.html)
- [Max Kersten & Alexandre Mundo. (2023, November 29). Akira Ransomware. Retrieved April 4, 2024.](https://www.trellix.com/blogs/research/akira-ransomware/)
- [Park, S. (2021, June 15). Andariel evolves to target South Korea with ransomware. Retrieved September 29, 2021.](https://securelist.com/andariel-evolves-to-target-south-korea-with-ransomware/102811/)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.](https://pan-unit42.github.io/playbook_viewer/)
- [Chen, X., Scott, M., Caselden, D.. (2014, April 26). New Zero-Day Exploit targeting Internet Explorer Versions 9 through 11 Identified in Targeted Attacks. Retrieved January 14, 2016.](https://www.fireeye.com/blog/threat-research/2014/04/new-zero-day-exploit-targeting-internet-explorer-versions-9-through-11-identified-in-targeted-attacks.html)
- [Yates, M. (2017, June 18). APT3 Uncovered: The code evolution of Pirpi. Retrieved September 28, 2017.](https://recon.cx/2017/montreal/resources/slides/RECON-MTL-2017-evolution_of_pirpi.pdf)
- [Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)
- [FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)
- [Perez, D. et al. (2021, May 27). Re-Checking Your Pulse: Updates on Chinese APT Actors Compromising Pulse Secure VPN Devices. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Unit 42. (2025, December 11). Hamas-Affiliated Ashen Lepus Targets Middle Eastern Diplomatic Entities With New AshTag Malware Suite. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
- [Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
- [Jornet, A. (2021, December 23). Snip3, an investigation into malware. Retrieved September 19, 2023.](https://telefonicatech.com/blog/snip3-investigacion-malware)
- [Yuste, J. Pastrana, S. (2021, February 9). Avaddon ransomware: an in-depth analysis and decryption of infected systems. Retrieved August 19, 2021.](https://arxiv.org/pdf/2102.04796.pdf)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [Hasherezade. (2021, July 23). AvosLocker enters the ransomware scene, asks for partners. Retrieved January 11, 2023.](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
- [Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
- [Proofpoint. (2018, July 30). New version of AZORult stealer improves loading features, spreads alongside ransomware in new campaign. Retrieved November 29, 2018.](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)
- [Sogeti. (2021, March). Babuk Ransomware. Retrieved August 11, 2021.](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
- [Mundo, A. et al. (2021, February). Technical Analysis of Babuk Ransomware. Retrieved August 11, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
- [Centero, R. et al. (2021, February 5). New in Ransomware: Seth-Locker, Babuk Locker, Maoloa, TeslaCrypt, and CobraLocker. Retrieved August 11, 2021.](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)
- [Unit 42. (2019, February 22). New BabyShark Malware Targets U.S. National Security Think Tanks. Retrieved October 7, 2019.](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
- [Symantec Security Response. (2014, June 30). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
- [FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved November 17, 2024.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
- [Mamedov, O. Sinitsyn, F. Ivanov, A.. (2017, October 24). Bad Rabbit ransomware. Retrieved January 28, 2021.](https://securelist.com/bad-rabbit-ransomware/82851/)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Lee, B. Grunzweig, J. (2015, December 22). BBSRAT Attacks Targeting Russian Organizations Linked to Roaming Tiger. Retrieved August 19, 2016.](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)
- [Mandiant. (n.d.). Appendix C (Digital) - The Malware Arsenal. Retrieved July 18, 2016.](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)
- [Hayashi, K., Ray, V. (2018, July 31). Bisonal Malware Used in Attacks Against Russia and South Korea. Retrieved August 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)
- [Zykov, K. (2020, August 13). CactusPete APT group’s updated Bisonal backdoor. Retrieved May 5, 2021.](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [FireEye Labs/FireEye Threat Intelligence. (2015, May 14). Hiding in Plain Sight: FireEye and Microsoft Expose Obfuscation Tactic. Retrieved November 17, 2024.](https://web.archive.org/web/20240119213200/https://www2.fireeye.com/rs/fireye/images/APT17_Report.pdf)
- [F-Secure Labs. (2014). BlackEnergy & Quedagh: The convergence of crimeware and APT attacks. Retrieved March 24, 2016.](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
- [Baumgartner, K. and Garnaeva, M.. (2014, November 3). BE2 custom plugins, router abuse, and target profiles. Retrieved March 24, 2016.](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
- [Cherepanov, A.. (2016, January 3). BlackEnergy by the SSHBearDoor: attacks against Ukrainian news media and electric industry . Retrieved June 10, 2020.](https://www.welivesecurity.com/2016/01/03/blackenergy-sshbeardoor-details-2015-attacks-ukrainian-news-media-electric-industry/)
- [Cash, D., Grunzweig, J., Meltzer, M., Adair, S., Lancaster, T. (2021, August 17). North Korean APT InkySquid Infects Victims Using Browser Exploits. Retrieved September 30, 2021.](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
- [DHS/CISA. (2026, February 11). AR25-338A: BRICKSTORM Backdoor. Retrieved April 16, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
- [Harbison, M. and Renals, P. (2022, July 5). When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors. Retrieved February 1, 2023.](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
- [Merriman, K. and Trouerbach, P. (2022, April 28). This isn't Optimus Prime's Bumblebee but it's Still Transforming. Retrieved August 22, 2022.](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
- [Kamble, V. (2022, June 28). Bumblebee: New Loader Rapidly Assuming Central Position in Cyber-crime Ecosystem. Retrieved August 24, 2022.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)
- [Salem, A. (2022, April 27). The chronicles of Bumblebee: The Hook, the Bee, and the Trickbot connection. Retrieved September 2, 2022.](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
- [Sushko, O. (2019, April 17). macOS Bundlore: Mac Virus Bypassing macOS Security Features. Retrieved June 30, 2020.](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Threat Intelligence Team. (2022, March 18). Double header: IsaacWiper and CaddyWiper . Retrieved April 11, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/03/double-header-isaacwiper-and-caddywiper/)
- [Falcone, R., Lee, B. (2018, November 20). Sofacy Continues Global Attacks and Wheels Out New ‘Cannon’ Trojan. Retrieved November 26, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
- [Lee, B., Falcone, R. (2018, December 12). Dear Joohn: The Sofacy Group’s Global Campaign. Retrieved April 19, 2019.](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)
- [Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)
- [Trusteer Fraud Prevention Center. (2010, October 7). Carberp Under the Hood of Carberp: Malware & Configuration Analysis. Retrieved July 15, 2020.](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)
- [ESET. (2017, March 30). Carbon Paper: Peering into Turla’s second stage backdoor. Retrieved November 7, 2018.](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)
- [Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Miller-Osborn, J. and Grunzweig, J.. (2017, February 16). menuPass Returns with New Malware and New Attacks Against Japanese Academics and Organizations. Retrieved March 1, 2017.](http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Mundo, A. (2019, August 1). Clop Ransomware. Retrieved May 10, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
- [Dutch Military Intelligence and Security Service (MIVD) & Dutch General Intelligence and Security Service (AIVD). (2024, February 6). Ministry of Defense of the Netherlands uncovers COATHANGER, a stealthy Chinese FortiGate RAT. Retrieved February 7, 2024.](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
- [Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
- [Mavis, N. (2020, September 21). The Art and Science of Detecting Cobalt Strike. Retrieved September 12, 2024.](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Grunzweig, J. (2018, January 31). Comnie Continues to Target Organizations in East Asia. Retrieved June 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
- [Baskin, B. (2020, July 8). TAU Threat Discovery: Conti Ransomware. Retrieved February 17, 2021.](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [N. Baisini. (2022, July 13). Transparent Tribe begins targeting education sector in latest campaign. Retrieved September 22, 2022.](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [Kohler, A. and Lopez, C. (2024, April 30). Malware: Cuckoo Behaves Like Cross Between Infostealer and Spyware. Retrieved August 20, 2024.](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
- [NCSC. (2022, February 23). Cyclops Blink Malware Analysis Report. Retrieved March 3, 2022.](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
- [Mabutas, G. (2020, May 11). New MacOS Dacls RAT Backdoor Shows Lazarus’ Multi-Platform Attack Capability. Retrieved August 10, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-dacls-rat-backdoor-show-lazarus-multi-platform-attack-capability/)
- [Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [McGraw, T. (2024, December 4). Black Basta Ransomware Campaign Drops Zbot, DarkGate, and Custom Malware. Retrieved December 9, 2024.](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
- [Kaspersky Lab's Global Research & Analysis Team. (2015, August 10). Darkhotel's attacks in 2015. Retrieved November 2, 2018.](https://securelist.com/darkhotels-attacks-in-2015/71713/)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [Alperovitch, D. (2014, July 7). Deep in Thought: Chinese Targeting of National Security Think Tanks. Retrieved November 12, 2014.](https://web.archive.org/web/20200424075623/https:/www.crowdstrike.com/blog/deep-thought-chinese-targeting-national-security-think-tanks/)
- [Fidelis Cybersecurity. (2016, February 29). The Turbo Campaign, Featuring Derusbi for 64-bit Linux. Retrieved March 2, 2016.](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [Fishbein, N., Kajiloti, M.. (2020, July 28). Watch Your Containers: Doki Infecting Docker Servers in the Cloud. Retrieved March 30, 2021.](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
- [TheWover. (2019, May 9). donut. Retrieved March 25, 2022.](https://github.com/TheWover/donut)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [Konstantin Zykov. (2019, September 23). Hello! My name is Dtrack. Retrieved January 20, 2021.](https://securelist.com/my-name-is-dtrack/93338/)
- [Hod Gavriel. (2019, November 21). Dtrack: In-depth analysis of APT on a nuclear power plant. Retrieved January 20, 2021.](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
- [Symantec Security Response. (2011, November). W32.Duqu: The precursor to the next Stuxnet. Retrieved September 17, 2015.](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [ClearSky. (2016, January 7). Operation DustySky. Retrieved January 8, 2016.](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
- [GReAT. (2019, April 10). Gaza Cybergang Group1, operation SneakyPastes. Retrieved May 13, 2020.](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
- [Chen, J., et al. (2022). Delving Deep: An Analysis of Earth Lusca’s Operations. Retrieved July 1, 2022.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
- [Dragos. (2020, February 3). EKANS Ransomware and ICS Operations. Retrieved February 9, 2021.](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)
- [Zafra, D., et al. (2020, February 24). Ransomware Against the Machine: How Adversaries are Learning to Disrupt Industrial Production by Targeting IT and OT. Retrieved March 2, 2021.](https://www.fireeye.com/blog/threat-research/2020/02/ransomware-against-machine-learning-to-disrupt-industrial-production.html)
- [Singleton, C. and Kiefer, C. (2020, September 28). Ransomware 2020: Attack Trends Affecting Organizations Worldwide. Retrieved September 20, 2021.](https://securityintelligence.com/posts/ransomware-2020-attack-trends-new-techniques-affecting-organizations-worldwide/)
- [Accenture Security. (2018, January 27). DRAGONFISH DELIVERS NEW FORM OF ELISE MALWARE TARGETING ASEAN DEFENCE MINISTERS’ MEETING AND ASSOCIATES. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)
- [Winters, R. (2015, December 20). The EPS Awakens - Part 2. Retrieved January 22, 2016.](https://web.archive.org/web/20151226205946/https://www.fireeye.com/blog/threat-research/2015/12/the-eps-awakens-part-two.html)
- [Jan Holman, Tomas Zvara. (2024, October 23). Embargo ransomware: Rock’n’Rust. Retrieved October 19, 2025.](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
- [Cyble. (2024, May 24). The Rust Revolution: New Embargo Ransomware Steps In. Retrieved October 19, 2025.](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
- [ASEC. (2017). ASEC REPORT VOL.88. Retrieved April 16, 2019.](https://global.ahnlab.com/global/upload/download/asecreport/ASEC%20REPORT_vol.88_ENG.pdf)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Adamitis, D. et al. (2019, June 4). It's alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign. Retrieved May 11, 2020.](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [Kaspersky Lab's Global Research & Analysis Team. (2014, August 06). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroboros. Retrieved November 7, 2018.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
- [Marschalek, M.. (2014, December 16). EvilBunny: Malware Instrumented By Lua. Retrieved June 28, 2019.](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
- [The BlackBerry Research and Intelligence Team. (2024, April 17). Threat Group FIN7 Targets the U.S. Automotive Industry. Retrieved May 1, 2025.](https://blogs.blackberry.com/en/2024/04/fin7-targets-the-united-states-automotive-industry)
- [Grunzweig, J. (2018, October 01). NOKKI Almost Ties the Knot with DOGCALL: Reaper Group Uses New Malware to Deploy RAT. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
- [FinFisher. (n.d.). Retrieved September 12, 2024.](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
- [Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [Ramin Nafisi. (2021, September 27). FoggyWeb: Targeted NOBELIUM malware leads to persistent backdoor. Retrieved October 4, 2021.](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
- [Kremez, V. (2019, September 19). FIN6 “FrameworkPOS”: Point-of-Sale Malware Analysis & Internals. Retrieved September 8, 2020.](https://labs.sentinelone.com/fin6-frameworkpos-point-of-sale-malware-analysis-internals-2/)
- [Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.](https://objective-see.com/blog/blog_0x25.html)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Doctor Web. (2014, November 21). Linux.BackDoor.Fysbis.1. Retrieved December 7, 2017.](https://vms.drweb.com/virus/?i=4276269)
- [Symantec. (2022, January 31). Shuckworm Continues Cyber-Espionage Attacks Against Ukraine. Retrieved February 17, 2022.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shuckworm-gamaredon-espionage-ukraine)
- [Unit 42. (2022, February 3). Russia’s Gamaredon aka Primitive Bear APT Group Actively Targeting Ukraine. Retrieved February 21, 2022.](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)
- [Threat Hunter Team, Symantec and Carbon Black. (2025, April 10). Shuckworm Targets Foreign Military Mission Based in Ukraine. Retrieved July 23, 2025.](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [F-Secure Labs. (2015, September 17). The Dukes: 7 years of Russian cyberespionage. Retrieved December 10, 2015.](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
- [Schwarz, D. et al. (2019, October 16). TA505 Distributes New SDBbot Remote Access Trojan with Get2 Downloader. Retrieved May 29, 2020.](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
- [FireEye Threat Intelligence. (2015, July 13). Demonstrating Hustle, Chinese APT Groups Quickly Use Zero-Day Vulnerability (CVE-2015-5119) Following Hacking Team Leak. Retrieved January 25, 2016.](https://www.fireeye.com/blog/threat-research/2015/07/demonstrating_hustle.html)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
- [Eoin Miller. (2021, March 23). Defending Against the Zero Day: Analyzing Attacker Behavior Post-Exploitation of Microsoft Exchange. Retrieved October 27, 2022.](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)
- [Carr, N., et al. (2017, April 24). FIN7 Evolution and the Phishing LNK. Retrieved April 24, 2017.](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)
- [Ungur, P. (n.d.). HAVOC. Retrieved August 4, 2025.](https://havocframework.com/docs/welcome)
- [Shivtarkar, N. and Jain, S. (2023, February 14). Havoc Across the Cyberspace. Retrieved August 4, 2025.](https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace)
- [Wan, Y. (2025, March 3). Havoc: SharePoint with Microsoft Graph API turns into FUD C2. Retrieved August 4, 2025.](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)
- [McLellan, T. and Moore, J. et al. (2021, April 29). UNC2447 SOMBRAT and FIVEHANDS Ransomware: A Sophisticated Financial Threat. Retrieved June 2, 2021.](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [Breitenbacher, D. (2024). Unmasking HiddenFace. Retrieved April 17, 2026.](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)
- [Singh, S. Singh, A. (2020, June 11). The Return on the Higaisa APT. Retrieved March 2, 2021.](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Knight, S.. (2020, April 16). VMware Carbon Black TAU Threat Analysis: The Evolution of Lazarus. Retrieved May 1, 2020.](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
- [Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
- [Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
- [Unit 42. (2019, December 2). Imminent Monitor – a RAT Down Under. Retrieved May 5, 2020.](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [Symantec. (2018, March 14). Inception Framework: Alive and Well, and Hiding Behind Proxies. Retrieved May 8, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/inception-framework-hiding-behind-proxies)
- [Daniel Kapellmann Zafra, Raymond Leong, Chris Sistrunk, Ken Proska, Corey Hildebrandt, Keith Lunden, Nathan Brubaker. (2022, April 25). INDUSTROYER.V2: Old Malware Learns New Tricks. Retrieved March 30, 2023.](https://www.mandiant.com/resources/blog/industroyer-v2-old-malware-new-tricks)
- [Seongsu Park. (2024, November 4). From Pyongyang to Your Payroll: The Rise of North Korean Remote Workers in the West. Retrieved October 17, 2025.](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Reichel, D. (2021, February 19). IronNetInjector: Turla’s New Malware Loading Tool. Retrieved February 24, 2021.](https://unit42.paloaltonetworks.com/ironnetinjector/)
- [Sancho, D., et al. (2012, May 22). IXESHE An APT Campaign. Retrieved June 7, 2019.](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
- [GReAT. (2020, July 14). The Tetrade: Brazilian banking malware goes global. Retrieved November 9, 2020.](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)
- [ESET. (2016, October). En Route with Sednit - Part 1: Approaching the Target. Retrieved November 8, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)
- [Lee, B, et al. (2018, February 28). Sofacy Attacks Multiple Government Entities. Retrieved March 15, 2018.](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [Bingham, J. (2013, February 11). Cross-Platform Frutas RAT Builder and Back Door. Retrieved April 23, 2019.](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)
- [Yadav, A., et al. (2016, January 29). Malicious Office files dropping Kasidet and Dridex. Retrieved March 24, 2016.](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)
- [Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)
- [US-CERT. (2018, August 09). MAR-10135536-17 – North Korean Trojan: KEYMARBLE. Retrieved August 16, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
- [Gilbert Sison, Rheniel Ramos, Jay Yaneza, Alfredo Oliveira. (2018, January 15). KillDisk Variant Hits Latin American Financial Groups. Retrieved January 12, 2021.](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [Den Iuzvyk, Tim Peck. (2025, February 13). Analyzing DEEP#DRIVE: North Korean Threat Actors Observed Exploiting Trusted Platforms for Targeted Attacks. Retrieved August 19, 2025.](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)
- [Singer, G. (2020, April 3). Threat Alert: Kinsing Malware Attacks Targeting Container Environments. Retrieved April 1, 2021.](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
- [Dani Creus, Tyler Halfpop, Robert Falcone. (2016, September 26). Sofacy's 'Komplex' OS X Trojan. Retrieved July 8, 2017.](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)
- [Karmi, D. (2020, January 4). A Look Into Konni 2019 Campaign. Retrieved April 28, 2020.](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)
- [Threat Intelligence Team. (2021, August 23). New variant of Konni malware used in campaign targetting Russia. Retrieved January 5, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Black Lotus Labs. (2023, December 13). Routers Roasting On An Open Firewall: The KV-Botnet Investigation. Retrieved June 10, 2024.](https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/)
- [Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
- [Google Threat Intelligence Group. (2025, November 5). GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools. Retrieved March 31, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
- [Simonovich, V. (2025, July 23). Cato CTRL™ Threat Research: Analyzing LAMEHUG – First Known LLM-Powered Malware with Links to APT28 (Fancy Bear) . Retrieved April 21, 2026.](https://www.catonetworks.com/blog/cato-ctrl-threat-research-analyzing-lamehug/)
- [Proofpoint Threat Research and Team Cymru S2 Threat Research. (2024, April 4). Latrodectus: This Spider Bytes Like Ice . Retrieved May 31, 2024.](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
- [Stepanic, D. and Bousseaden, S. (2024, May 15). Spring Cleaning with LATRODECTUS: A Potential Replacement for ICEDID. Retrieved September 13, 2024.](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
- [Batista, J. (2024, June 17). Latrodectus, are you coming back?. Retrieved September 13, 2024.](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)
- [Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)
- [Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
- [Saini, A. and Hossein, J. (2022, January 27). North Korea’s Lazarus APT leverages Windows Update client, GitHub in latest campaign. Retrieved January 27, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)
- [Stuart Ashenbrenner, Alden Schmidt. (2024, April 25). LightSpy Malware Variant Targeting macOS. Retrieved January 3, 2025.](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
- [Zhou, R. (2012, May 15). Backdoor.Linfo. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
- [Seals, T. (2021, May 14). FIN7 Backdoor Masquerades as Ethical Hacking Tool. Retrieved February 2, 2022.](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [FBI. (2022, February 4). Indicators of Compromise Associated with LockBit 2.0 Ransomware. Retrieved January 24, 2025.](https://www.ic3.gov/CSA/2022/220204.pdf)
- [SentinelOne. (n.d.). LockBit 2.0: In-Depth Analysis, Detection, Mitigation, and Removal. Retrieved January 24, 2025.](https://www.sentinelone.com/anthology/lockbit-2-0/)
- [Walter, J. (2022, July 21). LockBit 3.0 Update | Unpicking the Ransomware’s Latest Anti-Analysis and Evasion Techniques. Retrieved February 5, 2025.](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
- [CISA et al. (2023, June 14). UNDERSTANDING RANSOMWARE THREAT ACTORS: LOCKBIT. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part II. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
- [ITOCHU. (2024, January 24). The Endless Struggle Against APT10: Insights from LODEINFO v0.6.6 - v0.7.3 Analysis. Retrieved April 17, 2026.](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
- [Raggi, M. Schwarz, D.. (2019, August 1). LookBack Malware Targets the United States Utilities Sector with Phishing Attacks Impersonating Engineering Licensing Boards. Retrieved February 25, 2021.](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
- [Malik, M. (2019, June 20). LoudMiner: Cross-platform mining in cracked VST software. Retrieved May 18, 2020.](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)
- [ESET Research. (2025, December 2). MuddyWater: Snakes by the riverbank. Retrieved February 17, 2026.](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
- [Hsu, K. et al. (2020, June 24). Lucifer: New Cryptojacking and DDoS Hybrid Malware Exploiting High and Critical Vulnerabilities to Infect Windows Devices. Retrieved November 16, 2020.](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Phil Stokes. (2021, January 11). FADE DEAD | Adventures in Reversing Malicious Run-Only AppleScripts. Retrieved September 29, 2022.](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [Lee, B. and Falcone, R. (2017, February 15). Magic Hound Campaign Attacks Saudi Targets. Retrieved December 27, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)
- [GReAT. (2021, June 16). Ferocious Kitten: 6 Years of Covert Surveillance in Iran. Retrieved September 22, 2021.](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
- [Mundo, A. (2020, March 26). Ransomware Maze. Retrieved May 18, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
- [Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Zemah, Y. (2024, December 2). Threat Assessment: Howling Scorpius (Akira Ransomware). Retrieved January 8, 2025.](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [Erlich, C. (2020, April 3). The Avast Abuser: Metamorfo Banking Malware Hides By Abusing Avast Executable. Retrieved May 26, 2020.](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
- [Check Point Research Team. (2021, August 14). Indra - Hackers Behind Recent Attacks on Iran. Retrieved February 17, 2022.](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
- [Threat Hunter Team. (2023, April 20). Daggerfly: APT Actor Targets Telecoms Company in Africa. Retrieved July 25, 2024.](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [ESET Security. (2019, November 19). Mispadu: Advertisement for a discounted Unhappy Meal. Retrieved March 13, 2024.](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
- [Falcone, R. and Miller-Osborn, J.. (2016, January 24). Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists. Retrieved February 10, 2016.](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
- [Miller-Osborn, J. and Grunzweig, J.. (2017, March 30). Trochilus and New MoonWind RATs Used In Attack Against Thai Organizations. Retrieved March 30, 2017.](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
- [ESET, et al. (2018, January). Diplomats in Eastern Europe bitten by a Turla mosquito. Retrieved July 3, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 10). MuddyWater expands operations. Retrieved November 2, 2018.](https://securelist.com/muddywater/88059/)
- [ClearSky. (2019, June). Iranian APT group ‘MuddyWater’ Adds Exploits to Their Arsenal. Retrieved May 14, 2020.](https://www.clearskysec.com/wp-content/uploads/2019/06/Clearsky-Iranian-APT-group-%E2%80%98MuddyWater%E2%80%99-Adds-Exploits-to-Their-Arsenal.pdf)
- [Hamzeloofard, S. (2020, January 31). New wave of PlugX targets Hong Kong | Avira Blog. Retrieved April 13, 2021.](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)
- [Nick Dai, Vickie Su, Sunny Lu. (2022, November 18). Earth Preta Spear-Phishing Governments Worldwide. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
- [Mercer, W., Rascagneres, P. (2018, May 31). NavRAT Uses US-North Korea Summit As Decoy For Attacks In South Korea. Retrieved June 11, 2018.](https://blog.talosintelligence.com/2018/05/navrat.html)
- [Vrabie, V. (2021, April 23). NAIKON – Traces from a Military Cyber-Espionage Operation. Retrieved June 29, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
- [Maniath, S. and Kadam P. (2019, March 19). Dissecting a NETWIRE Phishing Campaign's Usage of Process Hollowing. Retrieved January 7, 2021.](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Ahn Ho, Facundo Muñoz, & Marc-Etienne M.Léveillé. (2024, March 7). Evasive Panda leverages Monlam Festival to target Tibetans. Retrieved July 25, 2024.](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [Pascual, C. (2018, November 27). AutoIt-Compiled Worm Affecting Removable Media Delivers Fileless Version of BLADABINDI/njRAT Backdoor. Retrieved June 4, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
- [KASPERSKY GERT. (2023, December 14). Unveiling NKAbuse: a new multiplatform threat abusing the NKN protocol. Retrieved February 8, 2024.](https://securelist.com/unveiling-nkabuse/111512/)
- [Malhotra, A. (2021, March 2). ObliqueRAT returns with new campaign using hijacked websites. Retrieved September 2, 2021.](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
- [Sherstobitoff, R., Malhotra, A. (2018, October 18). ‘Operation Oceansalt’ Attacks South Korea, U.S., and Canada With Source Code From Chinese Hacker Group. Retrieved November 30, 2018.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)
- [Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
- [Symantec Threat Hunter Team. (2023, October 19). Crambus: New Campaign Targets Middle Eastern Government. Retrieved November 27, 2024.](https://www.security.com/threat-intelligence/crambus-middle-east-government)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-uncovers-operation-honeybee-malicious-document-campaign-targeting-humanitarian-aid-groups/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [GREAT. (2021, March 30). APT10: sophisticated multi-layered loader Ecipekac discovered in A41APT campaign. Retrieved June 17, 2021.](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: PAKLOG, CorKLOG, and SplatCloak | P2. Retrieved September 12, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
- [Lunghi, D. and Lu, K. (2021, April 9). Iron Tiger APT Updates Toolkit With Evolved SysUpdate Malware. Retrieved November 12, 2021.](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
- [Mullaney, C. & Honda, H. (2012, May 4). Trojan.Pasam. Retrieved February 22, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)
- [Trustwave SpiderLabs. (2020, June 22). Pillowmint: FIN7’s Monkey Thief . Retrieved July 27, 2020.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
- [Tartare, M. et al. (2020, May 21). No “Game over” for the Winnti Group. Retrieved August 24, 2020.](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
- [Ash, B., et al. (2018, June 26). RANCOR: Targeted Attacks in South East Asia Using PLAINTEE and DDKONG Malware Families. Retrieved July 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
- [Trend Micro Research. (2023, July 21). Ransomware Spotlight: Play. Retrieved September 24, 2024.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
- [Bermejo, L., et al. (2017, June 22). Following the Trail of BlackTech’s Cyber Espionage Campaigns. Retrieved May 5, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
- [Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
- [Mercer, W, et al. (2020, April 16). PoetRAT: Python RAT uses COVID-19 lures to target Azerbaijan public and private sectors. Retrieved April 27, 2020.](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
- [FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
- [Kaspersky Lab's Global Research and Analysis Team. (2016, February 9). Poseidon Group: a Targeted Attack Boutique specializing in global cyber-espionage. Retrieved March 16, 2016.](https://securelist.com/poseidon-group-a-targeted-attack-boutique-specializing-in-global-cyber-espionage/73673/)
- [Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
- [GReAT. (2019, August 12). Recent Cloud Atlas activity. Retrieved May 8, 2020.](https://securelist.com/recent-cloud-atlas-activity/92016/)
- [PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.](https://github.com/PowerShellMafia/PowerSploit)
- [PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.](http://powersploit.readthedocs.io)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [Lunghi, D. and Horejsi, J.. (2019, June 10). MuddyWater Resurfaces, Uses Multi-Stage Backdoor POWERSTATS V3 and New Post-Exploitation Tools. Retrieved May 14, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
- [Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
- [Nicolas Verdier. (n.d.). Retrieved January 29, 2018.](https://github.com/n1nj4sec/pupy)
- [Check Point Research. (2025, March 10). Blind Eagle: …And Justice for All. Retrieved April 16, 2026.](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
- [Morrow, D. (2021, April 15). The rise of QakBot. Retrieved September 27, 2021.](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)
- [Magdy, S. et al. (2022, August 25). New Golang Ransomware Agenda Customizes Attacks. Retrieved September 26, 2025.](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
- [SentinelOne. (2022, November 30). Agenda (Qilin). Retrieved September 26, 2025.](https://www.sentinelone.com/anthology/agenda-qilin/)
- [Halcyon RISE Team. (2024, October 24). New Qilin.B Ransomware Variant Boasts Enhanced Encryption and Defense Evasion. Retrieved September 26, 2025.](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
- [Health Sector Cybersecurity Coordination Center. (2024, June 18). Qilin, aka Agenda Ransomware. Retrieved September 26, 2025.](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)
- [Trend Micro. (2025, October 23). Agenda Ransomware Deploys Linux Variant on Windows Systems Through Remote Management Tools and BYOVD Techniques. Retrieved March 26, 2026.](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [Antiy CERT. (2020, April 20). Analysis of Ramsay components of Darkhotel's infiltration and isolation network. Retrieved March 24, 2021.](https://www.programmersought.com/article/62493896999/)
- [CISA et al. (2024, August 29). #StopRansomware: RansomHub Ransomware. Retrieved March 17, 2025.](https://www.cisa.gov/sites/default/files/2024-09/aa24-242a-stopransomware-ransomhub-ransomware_1.pdf)
- [Christopher So. (2022, December 20). Raspberry Robin Malware Targets Telecom, Governments. Retrieved May 17, 2024.](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
- [Patrick Schläpfer . (2024, April 10). Raspberry Robin Now Spreading Through Windows Script Files. Retrieved May 17, 2024.](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
- [Lei, C., et al. (2018, January 24). Lazarus Campaign Targeting Cryptocurrencies Reveals Remote Controller Tool, an Evolved RATANKBA, and More. Retrieved May 22, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)
- [Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
- [Global Threat Center, Intelligence Team. (2020, December). APT27 Turns to Ransomware. Retrieved November 12, 2021.](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
- [Juniper Networks, Cybersecurity R&D. (2025, March 11). The RedPenguin Malware Incident. Retrieved June 24, 2025.](https://supportportal.juniper.net/sfc/servlet.shepherd/document/download/069Dp00000FzdmIIAR?operationContext=S1)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [Anomali Labs. (2019, March 15). Rocke Evolves Its Arsenal With a New Malware Family Written in Golang. Retrieved April 24, 2019.](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)
- [Falcone, R., et al. (2018, July 27). New Threat Actor Group DarkHydrus Targets Middle East Government. Retrieved August 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
- [Mercer, W., Rascagneres, P. (2017, April 03). Introducing ROKRAT. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)
- [Pantazopoulos, N.. (2018, November 8). RokRat Analysis. Retrieved May 21, 2020.](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
- [Alex Turing, Hui Wang. (2021, April 28). RotaJakiro: A long live secret backdoor with 0 VT detection. Retrieved June 14, 2023.](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
- [Cybereason Global SOC and Cybereason Security Research Teams. (2022, December 14). Royal Rumble: Analysis of Royal Ransomware. Retrieved March 30, 2023.](https://www.cybereason.com/blog/royal-ransomware-analysis)
- [Faou, M. and Boutin, J. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
- [Hanel, A. (2019, January 10). Big Game Hunting with Ryuk: Another Lucrative Targeted Ransomware. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
- [Symntec Threat Hunter Team. (2022, November 12). Billbug: State-sponsored Actor Targets Cert Authority, Government Agencies in Multiple Asian Countries. Retrieved March 15, 2025.](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
- [Budaca, E., et al. (2021, August 25). FIN8 Threat Actor Goes Agile with New Sardonic Backdoor. Retrieved August 9, 2023.](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [Kaspersky Lab. (2017, August). ShadowPad: popular server management software hit in supply chain attack. Retrieved March 22, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Falcone, R. and Wartell, R.. (2015, July 27). Observations on CVE-2015-3113, Prior Zero-Days and the Pirpi Payload. Retrieved January 22, 2016.](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
- [Splunk Threat Research Team , Teoderick Contreras. (2024, September 5). ShrinkLocker Malware: Abusing BitLocker to Lock Your Data. Retrieved December 7, 2024.](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
- [Hegel, T. (2021, January 13). A Global Perspective of the SideWinder APT. Retrieved January 27, 2021.](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [Remillano, A., Urbanec, J. (2019, September 19). Skidmap Linux Malware Uses Rootkit Capabilities to Hide Cryptocurrency-Mining Payload. Retrieved June 4, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [Secureworks. (n.d.). GOLD PRELUDE . Retrieved March 22, 2024.](https://www.secureworks.com/research/threat-profiles/gold-prelude)
- [Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
- [Cash, D. et al. (2020, December 14). Dark Halo Leverages SolarWinds Compromise to Breach Organizations. Retrieved December 29, 2020.](https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/)
- [MSTIC, CDOC, 365 Defender Research Team. (2021, January 20). Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop . Retrieved January 22, 2021.](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
- [CrowdStrike. (2022, January 27). Early Bird Catches the Wormhole: Observations from the StellarParticle Campaign. Retrieved February 7, 2022.](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [CISA. (2020, July 16). MAR-10296782-1.v1 – SOREFANG. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
- [DHS/CISA. (2026, February 26). MAR-25993211-r1.v2 Ivanti Connect Secure (RESURGE): AR25-087A. Retrieved April 17, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
- [Matt Lin, Austin Larsen, John Wolfram, Ashley Pearson, Josh Murchie, Lukasz Lamparski, Joseph Pisano, Ryan Hall, Ron Craft, Shawn Crew, Billy Wong, Tyler McLellan. (2024, April 4). Cutting Edge, Part 4: Ivanti Connect Secure VPN Post-Exploitation Lateral Movement Case Studies. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
- [Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.](https://citizenlab.org/2016/05/stealth-falcon/)
- [Microsoft Threat Intelligence. (2024, September 26). Storm-0501: Ransomware attacks expanding to hybrid cloud environments. Retrieved October 19, 2025.](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)
- [Cylance SPEAR Team. (2017, February 9). Shell Crew Variants Continue to Fly Under Big AV’s Radar. Retrieved February 15, 2017.](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)
- [Mercer, W. et al. (2020, June 29). PROMETHIUM extends global reach with StrongPity3 APT. Retrieved July 20, 2020.](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [CrowdStrike Intelligence Team. (2021, January 11). SUNSPOT: An Implant in the Build Process. Retrieved January 11, 2021.](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [Blasco, J. (2011, December 12). Another Sykipot sample likely targeting US federal agencies. Retrieved March 28, 2016.](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)
- [Ivanov, A. et al. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
- [Bettencourt, J. (2018, May 7). Kaspersky Lab finds new variant of SynAck ransomware using sophisticated Doppelgänging technique. Retrieved May 24, 2018.](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)
- [McCabe, A. (2020, January 23). The Fractured Statue Campaign: U.S. Government Agency Targeted in Spear-Phishing Attacks. Retrieved June 2, 2020.](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)
- [Gallagher, S., Gn, S. (2020, December 16). Ransomware operators use SystemBC RAT as off-the-shelf Tor backdoor. Retrieved May 16, 2025.](https://news.sophos.com/en-us/2020/12/16/systembc/)
- [Daniel Lunghi. (2023, March 1). Iron Tiger’s SysUpdate Reappears, Adds Linux Targeting. Retrieved March 20, 2023.](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
- [CISA, FBI, DOD. (2021, August). MAR-10292089-1.v2 – Chinese Remote Access Trojan: TAIDOOR. Retrieved August 24, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
- [USG. (2020, May 12). MAR-10288834-2.v1 – North Korean Trojan: TAINTEDSCRIBE. Retrieved March 5, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Microsoft. (n.d.). Tasklist. Retrieved December 23, 2015.](https://technet.microsoft.com/en-us/library/bb491010.aspx)
- [Fiser, D. Oliveira, A. (n.d.). Tracking the Activities of TeamTNT A Closer Look at a Cloud-Focused Malicious Actor Group. Retrieved September 22, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-tracking-the-activities-of-teamTNT.pdf)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Patrick Wardle. (2020, June 29). OSX.EvilQuest Uncovered part i: infection, persistence, and more!. Retrieved March 18, 2021.](https://objective-see.com/blog/blog_0x59.html)
- [Nathaniel Morales, Nick Dai. (2025, February 18). Earth Preta Mixes Legitimate and Malicious Components to Sidestep Detection. Retrieved September 10, 2025.](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
- [John Wolfram, Michael Edie, Jacob Thompson, Matt Lin, Josh Murchie. (2025, April 3). Suspected China-Nexus Threat Actor Actively Exploiting Critical Ivanti Connect Secure Vulnerability (CVE-2025-22457). Retrieved April 13, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)
- [Sila Ozeren Hacioglu. (2025, May 5). UNC5221’s Latest Exploit: Weaponizing CVE-2025-22457 in Ivanti Connect Secure. Retrieved April 13, 2026.](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
- [Boutin, J. (2020, October 12). ESET takes part in global operation to disrupt Trickbot. Retrieved March 15, 2021.](https://www.welivesecurity.com/2020/10/12/eset-takes-part-global-operation-disrupt-trickbot/)
- [Tudorica, R., Maximciuc, A., Vatamanu, C. (2020, March 18). New TrickBot Module Bruteforces RDP Connections, Targets Select Telecommunication Services in US and Hong Kong. Retrieved March 15, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/316/Bitdefender-Whitepaper-TrickBot-en-EN-interactive.pdf)
- [Secureworks. (2019, July 24). Updated Karagany Malware Targets Energy Sector. Retrieved August 12, 2020.](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
- [Ray, V. (2016, November 22). Tropic Trooper Targets Taiwanese Government and Fossil Fuel Provider With Poison Ivy. Retrieved November 9, 2018.](https://researchcenter.paloaltonetworks.com/2016/11/unit42-tropic-trooper-targets-taiwanese-government-and-fossil-fuel-provider-with-poison-ivy/)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Tomonaga, S. (2018, March 6). Malware “TSCookie”. Retrieved May 6, 2020.](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
- [Hayashi, K. (2017, November 28). UBoatRAT Navigates East Asia. Retrieved January 12, 2018.](https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/)
- [Alexander Marvi, Brad Slaybaugh, Ron Craft, and Rufus Brown. (2023, June 13). VMware ESXi Zero-Day Used by Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)
- [Unit 42. (2024, April 12). Threat Brief: Operation MidnightEclipse, Post-Exploitation Activity Related to CVE-2024-3400 . Retrieved January 15, 2025.](https://unit42.paloaltonetworks.com/cve-2024-3400/)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Caragay, R. (2015, March 26). URSNIF: The Multifaceted Malware. Retrieved June 5, 2019.](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
- [Sioting, S. (2013, June 15). BKDR_URSNIF.SM. Retrieved June 5, 2019.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
- [Salem, E. et al. (2020, May 28). VALAK: MORE THAN MEETS THE EYE . Retrieved June 19, 2020.](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
- [Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
- [Yagi, J. (2014, August 24). Trojan.Volgmer. Retrieved July 16, 2018.](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)
- [Microsoft Threat Intelligence. (2023, May 24). Volt Typhoon targets US critical infrastructure with living-off-the-land techniques. Retrieved July 27, 2023.](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)
- [Counter Threat Unit Research Team. (2023, May 24). Chinese Cyberespionage Group BRONZE SILHOUETTE Targets U.S. Government and Defense Organizations. Retrieved July 27, 2023.](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [Su, V. et al. (2019, December 11). Waterbear Returns, Uses API Hooking to Evade Security. Retrieved February 22, 2021.](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
- [The BlackBerry Research & Intelligence Team. (2020, October). BAHAMUT: Hack-for-Hire Masters of Phishing, Fake News, and Fake Apps. Retrieved February 8, 2021.](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)
- [Baumgartner, K., Golovkin, M.. (2015, May). The MsnMM Campaigns: The Earliest Naikon APT Campaigns. Retrieved April 10, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
- [Novetta Threat Research Group. (2015, April 7). Winnti Analysis. Retrieved February 8, 2017.](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
- [Kaspersky Lab's Global Research and Analysis Team. (2013, April 11). Winnti. More than just a game. Retrieved February 8, 2017.](https://securelist.com/winnti-more-than-just-a-game/37029/)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Robert Falcone. (2017, February 14). XAgentOSX: Sofacy's Xagent macOS Tool. Retrieved July 12, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)
- [Schwarz, D., Sopko J. (2018, March 08). Donot Team Leverages New Modular Malware Framework in South Asia. Retrieved June 11, 2018.](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
- [ESET. (2018, November 20). Sednit: What’s going on with Zebrocy?. Retrieved February 12, 2019.](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
- [ESET Research. (2019, May 22). A journey to Zebrocy land. Retrieved June 20, 2019.](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
- [Accenture Security. (2018, November 29). SNAKEMACKEREL. Retrieved April 15, 2019.](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
- [Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
- [McLellan, T. et al. (2024, January 12). Cutting Edge: Suspected APT Targets Ivanti Connect Secure VPN in New Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
- [Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)
- [Raghuprasad, C . (2022, May 11). Bitter APT adds Bangladesh to their targets. Retrieved June 1, 2022.](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)

---

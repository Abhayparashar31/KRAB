# System Information Discovery

## Description

An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use this information to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. This behavior is distinct from Local Storage Discovery which is an adversary's discovery of local drive, disks and/or volumes.

Tools such as Systeminfo can be used to gather detailed system information. If running with privileged access, a breakdown of system data can be gathered through the systemsetup configuration tool on macOS. Adversaries may leverage a Network Device CLI on network devices to gather detailed system information (e.g. show version ). [1] On ESXi servers, threat actors may gather system information from various esxcli utilities, such as system hostname get and system version get . [2] [3]

Infrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine. [4] [5] [6]

System Information Discovery combined with information gathered from other forms of discovery and reconnaissance can drive payload development and concealment. [7] [8]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0065 | 4H RAT | 4H RAT sends an OS version identifier in its beacons. [9] |
| S1167 | AcidPour | AcidPour can identify various system locations and mapped devices on Linux systems as a precursor to wiping activity. [10] |
| S1028 | Action RAT | Action RAT has the ability to collect the hostname, OS version, and OS architecture of an infected host. [11] |
| G0018 | admin@338 | admin@338 actors used the following commands after exploiting a machine with LOWBALL malware to obtain information about the OS: ver >> %temp%\download systeminfo >> %temp%\download [12] |
| S0045 | ADVSTORESHELL | ADVSTORESHELL can run Systeminfo to gather information about the victim. [13] [14] |
| S0331 | Agent Tesla | Agent Tesla can collect the system's computer name and also has the capability to collect information on the processor, memory, OS, and video card from the system. [15] [16] [17] |
| S1129 | Akira | Akira uses the GetSystemInfo Windows function to determine the number of processors on a victim machine. [18] |
| S1025 | Amadey | Amadey has collected the computer name and OS version from a compromised machine. [19] [20] |
| S0504 | Anchor | Anchor can determine the hostname and linux version on a compromised host. [21] |
| C0062 | Anthropic AI-orchestrated Campaign | During the Anthropic AI-orchestrated Campaign , the adversary tasked Claude Code to query databases and systems in order to identify proprietary information, including system configurations and database types. [22] |
| S0584 | AppleJeus | AppleJeus has collected the victim host information after infection. [23] |
| S0622 | AppleSeed | AppleSeed can identify the OS version of a targeted system. [24] |
| G0026 | APT18 | APT18 can collect system information from the victim’s machine. [25] |
| G0073 | APT19 | APT19 collected system architecture information. APT19 used an HTTP malware variant and a Port 22 malware variant to gather the hostname and CPU information from the victim’s machine. [26] [27] |
| G0022 | APT3 | APT3 has a tool that can obtain information about the local system. [28] [29] |
| G0050 | APT32 | APT32 has collected the OS version and computer name from victims. One of the group's backdoors can also query the Windows Registry to gather system information, and another macOS backdoor performs a fingerprint of the machine on its first connection to the C&C server. APT32 executed shellcode to identify the name of the infected host. [30] [31] [32] [33] |
| G0067 | APT37 | APT37 collects the computer name, the BIOS model, and execution path. [34] |
| G0082 | APT38 | APT38 has attempted to get detailed information about a compromised host, including the operating system, version, patches, hotfixes, and service packs. [35] |
| G0096 | APT41 | APT41 uses multiple built-in commands such as systeminfo and net config Workstation to enumerate victim system basic configuration information. [36] |
| G1044 | APT42 | APT42 has used malware, such as GHAMBAR and POWERPOST, to collect system information. [37] |
| G0143 | Aquatic Panda | Aquatic Panda has used native OS commands to understand privilege levels and system details. [38] |
| C0046 | ArcaneDoor | ArcaneDoor included collection of victim device configuration information. [39] |
| S0456 | Aria-body | Aria-body has the ability to identify the hostname, computer name, Windows version, processor speed, and machine GUID on a compromised host. [40] |
| S9031 | AshTag | The AshTag loader and AshenOrchestrator components can collect reconnaissance data from victim machines. [41] |
| S0373 | Astaroth | Astaroth collects the machine name and keyboard language from the system. [42] [43] |
| S1029 | AuTo Stealer | AuTo Stealer has the ability to collect the hostname and OS information from an infected host. [11] |
| S0473 | Avenger | Avenger has the ability to identify the OS architecture on a compromised host. [44] |
| S0344 | Azorult | Azorult can collect the machine information, system architecture, the OS version, computer name, Windows product name, the number of CPU cores, video card information, and the system language. [45] [46] |
| S0414 | BabyShark | BabyShark has executed the ver command. [47] |
| S0475 | BackConfig | BackConfig has the ability to gather the victim's computer name. [48] |
| S0093 | Backdoor.Oldrea | Backdoor.Oldrea collects information about the OS and computer name. [49] [50] |
| S0031 | BACKSPACE | During its initial execution, BACKSPACE extracts operating system information from the infected host. [51] |
| S0245 | BADCALL | BADCALL collects the computer name and host name on the compromised system. [52] |
| S0642 | BADFLICK | BADFLICK has captured victim computer name, memory space, and CPU details. [53] |
| S1081 | BADHATCH | BADHATCH can obtain current system information from a compromised machine such as the SHELL PID , PSVERSION , HOSTNAME , LOGONSERVER , LASTBOOTUP , OS type/version, bitness, and hostname. [54] [55] |
| S0337 | BadPatch | BadPatch collects the OS system, OS version, MAC address, and the computer name from the victim’s machine. [56] |
| S0239 | Bankshot | Bankshot gathers system information, network addresses, and the operation system version. [57] [58] |
| S0534 | Bazar | Bazar can fingerprint architecture, computer name, and OS version on the compromised host. Bazar can also check if the Russian language is installed on the infected machine and terminate if it is found. [59] [60] |
| S1246 | BeaverTail | BeaverTail has been known to collect basic system information. [61] [62] BeaverTail has also collected data to include hostname and current timestamp prior to uploading data to the API endpoint /uploads on the C2 server. [63] |
| S0017 | BISCUIT | BISCUIT has a command to collect the processor type, operation system, computer name, and whether the system is a laptop or PC. [64] |
| S0268 | Bisonal | Bisonal has used commands and API calls to gather system information. [65] [66] [67] |
| S1070 | Black Basta | Black Basta can collect system boot configuration and CPU information. [68] [69] |
| G1043 | BlackByte | BlackByte used various system commands and tools to pull system information during operations. [70] [71] [72] |
| S1180 | BlackByte Ransomware | BlackByte Ransomware gathers victim system information to generate a unique victim identifier. [73] |
| S1068 | BlackCat | BlackCat can obtain the computer name and UUID. [74] |
| S0089 | BlackEnergy | BlackEnergy has used Systeminfo to gather the OS version, as well as information on the system configuration, BIOS, the motherboard, and the processor. [75] [76] |
| S0520 | BLINDINGCAN | BLINDINGCAN has collected from a victim machine the system name, processor information, and OS version. [77] |
| G0108 | Blue Mockingbird | Blue Mockingbird has collected hardware details for the victim's system, including CPU and memory information. [78] |
| S0657 | BLUELIGHT | BLUELIGHT has collected the computer name and OS version from victim machines. [79] |
| S1184 | BOLDMOVE | BOLDMOVE performs system survey actions following initial execution. [80] |
| S0486 | Bonadan | Bonadan has discovered the OS version, CPU model, and RAM size of the system it has been installed on. [81] |
| S0635 | BoomBox | BoomBox can enumerate the hostname, domain, and IP of a compromised host. [82] |
| S0252 | Brave Prince | Brave Prince collects hard drive content and system configuration information. [83] |
| S0043 | BUBBLEWRAP | BUBBLEWRAP collects system information, including the operating system version and hostname. [12] |
| S1039 | Bumblebee | Bumblebee can enumerate the OS version and domain on a targeted system. [84] [85] [86] |
| S0482 | Bundlore | Bundlore will enumerate the macOS version to determine which follow-on behaviors to execute using /usr/bin/sw_vers -productVersion . [87] [8] |
| S0693 | CaddyWiper | CaddyWiper can use DsRoleGetPrimaryDomainInformation to determine the role of the infected machine. CaddyWiper can also halt execution if the compromised host is identified as a domain controller. [88] [89] |
| S0454 | Cadelspy | Cadelspy has the ability to discover information about the compromised host. [90] |
| S0351 | Cannon | Cannon can gather system information from the victim’s machine such as the OS version, and machine name. [91] [92] |
| S0484 | Carberp | Carberp has collected the operating system version from the infected system. [93] |
| S0348 | Cardinal RAT | Cardinal RAT can collect the hostname, Microsoft Windows version, and processor architecture from a victim machine. [94] |
| S0462 | CARROTBAT | CARROTBAT has the ability to determine the operating system of the compromised host and whether Windows is being run with x86 or x64 architecture. [95] [96] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell has a module to gather information from the compromised asset, including the computer version, computer name, IIS version, and more. [97] |
| S0631 | Chaes | Chaes has collected system information, including the machine name and OS version. [98] |
| S0674 | CharmPower | CharmPower can enumerate the OS version and computer name on a targeted system. [99] |
| S0144 | ChChes | ChChes collects the victim hostname, window resolution, and Microsoft Windows version. [100] [101] |
| S0667 | Chrommme | Chrommme has the ability to obtain the computer name of a compromised host. [102] |
| S0660 | Clambling | Clambling can discover the hostname, computer name, and Windows version of a targeted machine. [103] [104] |
| S0106 | cmd | cmd can be used to find information about the operating system. [105] |
| S0244 | Comnie | Comnie collects the hostname of the victim machine. [106] |
| G1052 | Contagious Interview | Contagious Interview has configured malicious webpages to identify the victim’s operating system by reviewing the details of the victims User-Agent of their browser. [107] |
| S0137 | CORESHELL | CORESHELL collects hostname and OS version data from the victim and sends the information to its C2 server. [108] |
| S1155 | Covenant | Covenant implants can gather basic information on infected systems. [109] |
| S0046 | CozyCar | A system info module in CozyCar gathers information on the victim host’s configuration. [110] |
| S0115 | Crimson | Crimson contains a command to collect the victim PC name and operating system. [111] [112] [113] |
| S1153 | Cuckoo Stealer | Cuckoo Stealer can gather information about the OS version and hardware on compromised hosts. [114] [115] |
| G1012 | CURIUM | CURIUM deploys information gathering tools focused on capturing IP configuration, running application, system information, and network connectivity information. [116] |
| C0029 | Cutting Edge | During Cutting Edge , threat actors used the ENUM4LINUX Perl script for discovery on Windows and Samba hosts. [117] |
| S0687 | Cyclops Blink | Cyclops Blink has the ability to query device information. [118] |
| G1034 | Daggerfly | Daggerfly utilizes victim machine operating system information to create custom User Agent strings for subsequent command and control communication. [119] |
| S0334 | DarkComet | DarkComet can collect the computer name, RAM used, and operating system version from the victim’s machine. [120] [121] |
| S1111 | DarkGate | DarkGate will gather various system information such as domain, display adapter description, operating system type and version, processor type, and RAM amount. [122] [123] |
| G0012 | Darkhotel | Darkhotel has collected the hostname, OS version, service pack version, and the processor architecture from the victim’s machine. [124] [125] |
| S1066 | DarkTortilla | DarkTortilla can obtain system information by querying the Win32_ComputerSystem , Win32_BIOS , Win32_MotherboardDevice , Win32_PnPEntity , and Win32_DiskDrive WMI objects. [126] |
| S0673 | DarkWatchman | DarkWatchman can collect the OS version, system architecture, and computer name. [127] |
| S1052 | DEADEYE | DEADEYE can enumerate a victim computer's volume serial number and host name. [128] |
| S0354 | Denis | Denis collects OS information and the computer name from the victim’s machine. [129] [130] |
| S0021 | Derusbi | Derusbi gathers the name of the local host, version of GNU Compiler Collection (GCC), and the system information about the CPU, machine, and operating system. [131] |
| S0659 | Diavol | Diavol can collect the computer name and OS version from the system. [132] |
| S9002 | Diskpart | Diskpart can show information about the selected disk, partition, volume, or virtual hard disk (VHD). [133] |
| S0186 | DownPaper | DownPaper collects the victim host name and serial number, and then sends the information to the C2 server. [134] |
| S0384 | Dridex | Dridex has collected the computer name and OS architecture information from the system. [135] |
| S0547 | DropBook | DropBook has checked for the presence of Arabic language in the infected machine's settings. [136] |
| S0105 | dsquery | dsquery has the ability to enumerate various information, such as the operating system and host name, for systems within a domain. [128] |
| S0567 | Dtrack | Dtrack can collect the victim's computer name, hostname and adapter information to create a unique identifier. [137] [138] |
| S1159 | DUSTTRAP | DUSTTRAP reads the value of the infected system's HKLM\SYSTEM\Microsoft\Cryptography\MachineGUID value. [139] |
| S0062 | DustySky | DustySky extracts basic information about the operating system. [140] |
| S0024 | Dyre | Dyre has the ability to identify the computer name, OS version, and hardware configuration on a compromised host. [141] |
| S0554 | Egregor | Egregor can perform a language check of the infected system and can query the CPU information (cupid). [142] [143] |
| S0081 | Elise | Elise executes systeminfo after initial communication is made to the remote server. [144] |
| S0082 | Emissary | Emissary has the capability to execute ver and systeminfo commands. [145] |
| S0363 | Empire | Empire can enumerate host system information like OS, architecture, domain name, applied patches, and more. [146] [147] |
| S0634 | EnvyScout | EnvyScout can determine whether the ISO payload was received by a Windows or iOS device. [82] |
| S0091 | Epic | Epic collects the OS version, hardware information, computer name, available system memory status, and system and user language settings. [148] |
| S0568 | EVILNUM | EVILNUM can obtain the computer name from the victim's system. [149] |
| S0569 | Explosive | Explosive has collected the computer name from the infected host. [150] |
| S0181 | FALLCHILL | FALLCHILL can collect operating system (OS) version information, processor information, and system name from the victim. [151] |
| S0512 | FatDuke | FatDuke can collect the user name, Windows version, computer name, and available space on discs from a compromised host. [152] |
| S0171 | Felismus | Felismus collects the system information, including hostname and OS version, and sends it to the C2 server. [153] |
| S0267 | FELIXROOT | FELIXROOT collects the victim’s computer name, processor architecture, OS version, and system type. [154] [155] |
| S0679 | Ferocious | Ferocious can use GET.WORKSPACE in Microsoft Excel to determine the OS version of the compromised host. [156] |
| G1016 | FIN13 | FIN13 has collected local host information by utilizing Windows commands systeminfo , fsutil , and fsinfo . FIN13 has also utilized a compromised Symantex Altiris console and LanDesk account to retrieve host information. [157] [158] |
| G0046 | FIN7 | FIN7 has used csvde.exe, which is a built-in Windows command line tool, to export system information. Additionally, WsTaskLoad has gathered system information, such as operating system and hostname. [159] |
| G0061 | FIN8 | FIN8 has used PowerShell Scripts to check the architecture of a compromised machine before the selection of a 32-bit or 64-bit version of a malicious .NET loader. [160] |
| S0355 | Final1stspy | Final1stspy obtains victim Microsoft Windows version information and CPU architecture. [161] |
| S0182 | FinFisher | FinFisher checks if the victim OS is 32 or 64-bit. [162] [163] |
| S0381 | FlawedAmmyy | FlawedAmmyy can collect the victim's operating system and computer name during the initial infection. [164] |
| C0001 | Frankenstein | During Frankenstein , the threat actors used Empire to obtain the compromised machine's name. [147] |
| C0007 | FunnyDream | During FunnyDream , the threat actors used Systeminfo to collect information on targeted hosts. [165] |
| S0410 | Fysbis | Fysbis has used the command ls /etc | egrep -e"fedora*|debian*|gentoo*|mandriva*|mandrake*|meego*|redhat*|lsb-*|sun-*|SUSE*|release" to determine which Linux OS version is running. [166] |
| G0047 | Gamaredon Group | A Gamaredon Group file stealer can gather the victim's computer name and drive serial numbers to send to a C2 server. [167] [168] [169] [170] [171] |
| S0666 | Gelsemium | Gelsemium can determine the operating system and whether a targeted machine has a 32 or 64 bit architecture. [102] |
| S0460 | Get2 | Get2 has the ability to identify the computer name and Windows version of an infected host. [172] |
| S0032 | gh0st RAT | gh0st RAT has gathered system architecture, processor, OS configuration, and installed hardware information. [173] |
| S9010 | GlassWorm | GlassWorm has the ability to check the OS of the victim host. [174] [175] GlassWorm has checked whether the OS platform value includes darwin prior to execution of macOS specific scripts. [174] [175] |
| S0249 | Gold Dragon | Gold Dragon collects endpoint information using the systeminfo command. [83] |
| S0493 | GoldenSpy | GoldenSpy has gathered operating system information. [176] |
| S1198 | Gomir | Gomir collects information on infected systems such as hostname, username, CPU, and RAM information. [177] |
| S1138 | Gootloader | Gootloader can inspect the User-Agent string in GET request header information to determine the operating system of targeted systems. [178] |
| S0531 | Grandoreiro | Grandoreiro can collect the computer name and OS version from a compromised host. [179] |
| S0237 | GravityRAT | GravityRAT collects the MAC address, computer name, and CPU information. [180] |
| S0690 | Green Lambert | Green Lambert can use uname to identify the operating system name, version, and processor type. [181] [182] |
| S0417 | GRIFFON | GRIFFON has used a reconnaissance module that can be used to retrieve information about a victim's computer, including the resolution of the workstation . [183] |
| S0632 | GrimAgent | GrimAgent can collect the OS, and build version on a compromised host. [184] |
| S0151 | HALFBAKED | HALFBAKED can obtain information about the OS, processor, and BIOS. [185] |
| S0214 | HAPPYWORK | can collect system information, including computer name, system manufacturer, IsDebuggerPresent state, and execution path. [186] |
| S1229 | Havoc | Havoc can gather system information including hostname, domain, and OS details. [187] |
| S0391 | HAWKBALL | HAWKBALL can collect the OS version, architecture information, and computer name. [188] |
| S0697 | HermeticWiper | HermeticWiper can determine the OS version and bitness on a targeted host. [189] [190] [191] [192] |
| G1001 | HEXANE | HEXANE has collected the hostname of a compromised machine. [193] |
| S1249 | HexEval Loader | HexEval Loader has identified the OS and MAC address of victim device through host fingerprinting scripting. [194] |
| S9023 | HiddenFace | HiddenFace can enumerate the hostname and username of the compromised system. [195] [196] [197] |
| G0126 | Higaisa | Higaisa collected the system GUID and computer name. [198] [199] |
| S0601 | Hildegard | Hildegard has collected the host's OS, CPU, and memory information. [200] |
| S0376 | HOPLIGHT | HOPLIGHT has been observed collecting victim machine information like OS version. [201] |
| S0431 | HotCroissant | HotCroissant has the ability to determine if the current user is an administrator, Windows product name, processor name, screen resolution, and physical RAM of the infected host. [202] |
| S0203 | Hydraq | Hydraq creates a backdoor through which remote attackers can retrieve information such as computer name, OS version, processor speed, memory size, and CPU speed. [203] |
| S1022 | IceApple | The IceApple Server Variable Dumper module iterates over all server variables present for the current request and returns them to the adversary. [204] |
| S0483 | IcedID | IcedID has the ability to identify the computer name and OS version on a compromised host. [205] [206] |
| S1152 | IMAPLoader | IMAPLoader uses WMI queries to gather information about the victim machine. [207] |
| G0100 | Inception | Inception has used a reconnaissance module to gather information about the operating system and hardware on the infected host. [208] |
| S0604 | Industroyer | Industroyer collects the victim machine’s Windows GUID. [209] |
| S0259 | InnaputRAT | InnaputRAT gathers system information. [210] |
| S1245 | InvisibleFerret | InvisibleFerret has collected OS type, hostname and system version through the "pay" module. [61] [63] InvisibleFerret has also queried the victim device using Python scripts to obtain the User and Hostname. [211] [62] |
| S0260 | InvisiMole | InvisiMole can gather information on the OS version, computer name, DEP policy, and memory size. [212] [213] |
| S9029 | IronWind | IronWind can capture the OS version and computer name of the compromised host. [214] |
| S0015 | Ixeshe | Ixeshe collects the computer name of the victim's system during the initial infection. [215] |
| S0201 | JPIN | JPIN can obtain system information such as OS version and disk space. [216] |
| S0283 | jRAT | jRAT collects information about the OS (version, build type, install date) as well as system up-time upon receiving a connection from a backdoor. [217] |
| C0044 | Juicy Mix | During Juicy Mix , OilRig used a script to send the name of the compromised host via HTTP POST to register it with C2. [218] |
| S1190 | Kapeka | Kapeka utilizes WinAPI calls and registry queries to gather system information. [219] |
| S0215 | KARAE | KARAE can collect system information. [186] |
| S0088 | Kasidet | Kasidet has the ability to obtain a victim's system name and operating system version. [220] |
| S0265 | Kazuar | Kazuar gathers information on the system. [221] |
| G0004 | Ke3chang | Ke3chang performs operating system information discovery using systeminfo and has used implants to identify the system language and computer name. [222] [223] [224] |
| S0585 | Kerrdown | Kerrdown has the ability to determine if the compromised host is running a 32 or 64 bit OS architecture. [225] |
| S0487 | Kessel | Kessel has collected the system architecture, OS version, and MAC address information. [81] |
| S1020 | Kevin | Kevin can enumerate the OS version and hostname of a targeted machine. [193] |
| S0387 | KeyBoy | KeyBoy can gather extended system information, such as information about the operating system and memory. [226] [227] |
| S0271 | KEYMARBLE | KEYMARBLE has the capability to collect the computer name, language settings, the OS version, CPU information, and time elapsed since system start. [228] |
| G0094 | Kimsuky | Kimsuky has enumerated OS type, OS version, and other information using a script or the "systeminfo" command. [229] [230] Kimsuky has also obtained system information such as OS type, OS version, and system type through querying various Windows Management Instrumentation (WMI) classes including Win32_OperatingSystem . [231] [232] |
| S0250 | Koadic | Koadic can obtain the OS version and build, computer name, and processor architecture from a compromised host. [233] |
| S0641 | Kobalos | Kobalos can record the hostname and kernel version of the target machine. [234] |
| S0669 | KOCTOPUS | KOCTOPUS has checked the OS version using wmic.exe and the find command. [233] |
| S0156 | KOMPROGO | KOMPROGO is capable of retrieving information about the infected system. [235] |
| S0356 | KONNI | KONNI can gather the OS version, architecture information, hostname, and RAM size information from the victim’s machine and has used cmd /c systeminfo command to get a snapshot of the current system state of the target machine. [236] [237] [238] |
| C0035 | KV Botnet Activity | KV Botnet Activity includes use of native system tools, such as uname , to obtain information about victim device architecture, as well as gathering other system information such as the victim's hosts file and CPU utilization. [239] |
| S0236 | Kwampirs | Kwampirs collects OS version information such as registered owner details, manufacturer details, processor type, available storage, installed patches, hostname, version info, system date, and other system information by using the commands systeminfo , net config workstation , hostname , ver , set , and date /t . [240] |
| S9035 | LAMEHUG | LAMEHUG has the ability to execute Windows commands returned from C2 to gather system information. [241] [242] |
| S1160 | Latrodectus | Latrodectus can gather operating system information. [243] [244] [244] [245] |
| G0032 | Lazarus Group | Several Lazarus Group malware families collect information on the type and version of the victim OS, as well as the victim computer name and CPU information. [246] [247] [248] [249] [250] [251] |
| S9039 | LazyWiper | LazyWiper has used [System.Net.Dns]::GetHostName() and $env:COMPUTERNAME to enumerate the hostname of a system and determine if it is a domain controller. [252] |
| C0049 | Leviathan Australian Intrusions | Leviathan performed host enumeration and data gathering operations on victim machines during Leviathan Australian Intrusions . [253] |
| S0395 | LightNeuron | LightNeuron gathers the victim computer name using the Win32 API call GetComputerName . [254] |
| S1185 | LightSpy | LightSpy 's second stage implant uses the DeviceInformation class to collect system information, including CPU usage, battery statistics, memory allocations, screen size, etc. [255] |
| S1186 | Line Dancer | Line Dancer can gather system configuration information by running the native show configuration command. [256] |
| S0211 | Linfo | Linfo creates a backdoor through which remote attackers can retrieve system information. [257] |
| S0513 | LiteDuke | LiteDuke can enumerate the CPUID and BIOS version on a compromised system. [152] |
| S0680 | LitePower | LitePower has the ability to enumerate the OS architecture. [156] |
| S1121 | LITTLELAMB.WOOLTEA | LITTLELAMB.WOOLTEA can check the type of Ivanti VPN device it is running on by executing first_run() to identify the first four bytes of the motherboard serial number. [258] |
| S0681 | Lizar | Lizar can collect the computer name from the machine. [259] [260] |
| S1199 | LockBit 2.0 | LockBit 2.0 can enumerate system information including hostname and domain information. [261] [262] |
| S1202 | LockBit 3.0 | LockBit 3.0 can enumerate system hostname and domain. [263] |
| S9020 | LODEINFO | LODEINFO can disover machine information including OS architecture, the ANSI code page (ACP) identifier, and hostname. [264] [265] |
| S0447 | Lokibot | Lokibot has the ability to discover the computer name and Windows product name/version. [266] |
| S0451 | LoudMiner | LoudMiner has monitored CPU usage. [267] |
| S0532 | Lucifer | Lucifer can collect the computer name, system architecture, default language, and processor frequency of a compromised host. [268] |
| S1213 | Lumma Stealer | Lumma Stealer has gathered various system information from victim machines. [269] [270] [271] |
| S1142 | LunarMail | LunarMail can capture environmental variables on compromised hosts. [272] |
| S1141 | LunarWeb | LunarWeb can use WMI queries and shell commands such as systeminfo.exe to collect the operating system, BIOS version, and domain name of the targeted system. [272] |
| S0409 | Machete | Machete collects the hostname of the target computer. [273] |
| S1016 | MacMa | MacMa can collect information about a compromised computer, including: Hardware UUID, Mac serial number, and macOS version. [274] |
| S1048 | macOS.OSAMiner | macOS.OSAMiner can gather the device serial number. [275] |
| S1060 | Mafalda | Mafalda can collect the computer name of a compromised host. [276] [277] |
| G0059 | Magic Hound | Magic Hound malware has used a PowerShell command to check the victim system architecture to determine if it is an x64 machine. Other malware has obtained the OS version, UUID, and computer/host name to send to the C2 server. [278] [279] [280] |
| S1182 | MagicRAT | MagicRAT collects basic system information from victim machines. [281] |
| G1026 | Malteiro | Malteiro collects the machine information, system architecture, the OS version, computer name, and Windows product name. [282] |
| S1169 | Mango | Mango can collect the machine name of a compromised system which is later used as part of a unique victim identifier. [218] |
| S1156 | Manjusaka | Manjusaka performs basic system profiling actions to fingerprint and register the victim system with the C2 controller. [283] |
| S0652 | MarkiRAT | MarkiRAT can obtain the computer name from a compromised host. [284] |
| S0449 | Maze | Maze has checked the language of the infected system using the "GetUSerDefaultUILanguage" function. [285] |
| G1051 | Medusa Group | Medusa Group has leveraged cmd.exe to identify system info cmd.exe /c systeminfo . [286] |
| S1244 | Medusa Ransomware | Medusa Ransomware has collected data from the SMBIOS firmware table using GetSystemFirmwareTable . [287] |
| S1059 | metaMain | metaMain can collect the computer name from a compromised host. [277] |
| S0455 | Metamorfo | Metamorfo has collected the hostname and operating system version from the compromised host. [288] [289] [290] |
| S0688 | Meteor | Meteor has the ability to discover the hostname of a compromised host. [291] |
| S0339 | Micropsia | Micropsia gathers the hostname and OS version from the victim’s machine. [292] [293] |
| S1015 | Milan | Milan can enumerate the targeted machine's name and GUID. [294] [295] |
| S0051 | MiniDuke | MiniDuke can gather the hostname on a compromised machine. [152] |
| S0280 | MirageFox | MirageFox can collect CPU and architecture information from the victim’s machine. [296] |
| G1054 | MirrorFace | MirrorFace has employed malicious macros and native Windows tools such as csvde.exe, nltest.exe and quser.exe for discovery. [265] [196] [197] |
| S0084 | Mis-Type | The initial beacon packet for Mis-Type contains the operating system version and file system of the victim. [297] |
| S0083 | Misdat | The initial beacon packet for Misdat contains the operating system version of the victim. [297] |
| S1122 | Mispadu | Mispadu collects the OS version, computer name, and language ID. [298] |
| S0079 | MobileOrder | MobileOrder has a command to upload to its C2 server victim mobile device information, including IMEI, IMSI, SIM card serial number, phone number, Android version, and other information. [299] |
| S0553 | MoleNet | MoleNet can collect information about the about the system. [136] |
| S1026 | Mongall | Mongall can retrieve the hostname via gethostbyname . [300] |
| G1036 | Moonstone Sleet | Moonstone Sleet has gathered information on victim systems. [301] |
| S0149 | MoonWind | MoonWind can obtain the victim hostname, Windows version, RAM amount, and screen resolution. [302] |
| S0284 | More_eggs | More_eggs has the capability to gather the OS version and computer name. [303] [304] |
| G1009 | Moses Staff | Moses Staff collected information about the infected host, including the machine names and OS architecture. [305] |
| G0069 | MuddyWater | MuddyWater has used malware that can collect the victim’s OS version and machine name. [306] [307] [308] [309] [310] |
| S0233 | MURKYTOP | MURKYTOP has the capability to retrieve information about the OS. [311] |
| G0129 | Mustang Panda | Mustang Panda has gathered system information using systeminfo . [312] |
| G1020 | Mustard Tempest | Mustard Tempest has used implants to perform system reconnaissance on targeted systems. [313] |
| S0205 | Naid | Naid collects a unique identifier (UID) from a compromised host. [314] |
| S0228 | NanHaiShu | NanHaiShu can gather the victim computer name and serial number. [315] |
| S0247 | NavRAT | NavRAT uses systeminfo on a victim’s machine. [316] |
| S0272 | NDiskMonitor | NDiskMonitor obtains the victim computer name and encrypts the information to send over its C2 channel. [317] |
| S0691 | Neoichor | Neoichor can collect the OS version and computer name from a compromised host. [224] |
| S0457 | Netwalker | Netwalker can determine the system architecture it is running on to choose which version of the DLL to use. [318] |
| S0198 | NETWIRE | NETWIRE can discover and collect victim system information. [319] |
| S1147 | Nightdoor | Nightdoor gathers information on the victim system such as CPU and Computer name as well as device drivers. [119] |
| S1100 | Ninja | Ninja can obtain the computer name and information on the OS from targeted hosts. [320] [321] |
| S0385 | njRAT | njRAT enumerates the victim operating system and computer name during the initial infection. [322] |
| S1107 | NKAbuse | NKAbuse conducts multiple system checks and includes these in subsequent "heartbeat" messages to the malware's command and control server. [323] |
| S0353 | NOKKI | NOKKI can gather information on the operating system on the victim’s machine. [324] |
| S9025 | NOOPLDR | NOOPLDR can discover the device ID and hostname from the targeted machine to use for encryption keys. [196] |
| S0644 | ObliqueRAT | ObliqueRAT has the ability to check for blocklisted computer names on infected endpoints. [325] |
| S0346 | OceanSalt | OceanSalt can collect the computer name from the system. [326] |
| S0340 | Octopus | Octopus can collect the computer name, OS version, and OS architecture information. [327] |
| S1172 | OilBooster | OilBooster can identify the compromised system's hostname which is used to create a unique identifier. [328] |
| G0049 | OilRig | OilRig has run hostname and systeminfo on a victim. [329] [330] [331] [332] [333] |
| S0439 | Okrum | Okrum can collect computer name, locale information, and information about the OS and architecture. [334] |
| S0264 | OopsIE | OopsIE checks for information on the CPU fan, temperature, mouse, hard disk, and motherboard as part of its anti-VM checks. [335] |
| C0060 | Operation AkaiRyū | During Operation AkaiRyū , MirrorFace collected system information. [336] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors used the systeminfo command to gather details about a compromised system. [337] |
| C0006 | Operation Honeybee | During Operation Honeybee , the threat actors collected the computer name, OS, and other system information using cmd /c systeminfo > %temp%\ temp.ini . [338] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors discovered the OS versions of systems connected to a targeted network. [339] |
| S0229 | Orz | Orz can gather the victim OS version and whether it is 64 or 32 bit. [315] |
| S0165 | OSInfo | OSInfo discovers information about the infected machine. [28] |
| S0402 | OSX/Shlayer | OSX/Shlayer has collected the IOPlatformUUID, session UID, and the OS version using the command sw_vers -productVersion . [340] [341] |
| S0352 | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D collects processor information, memory information, computer name, hardware UUID, serial number, and operating system version. OSX_OCEANLOTUS.D has used the ioreg command to gather some of this information. [342] [343] [8] |
| S0208 | Pasam | Pasam creates a backdoor through which remote attackers can retrieve information like hostname. [344] |
| G0040 | Patchwork | Patchwork collected the victim computer name, OS version, and architecture type and sent the information to its C2 server. [345] [317] |
| S0556 | Pay2Key | Pay2Key has the ability to gather the hostname of the victim machine. [346] |
| S0587 | Penquin | Penquin can report the file system type of a compromised host to C2. [347] |
| S1145 | Pikabot | Pikabot performs a variety of system checks and gathers system information, including commands such as whoami . [348] [349] |
| S0048 | PinchDuke | PinchDuke gathers system configuration information. [350] |
| S1031 | PingPull | PingPull can retrieve the hostname of a compromised host. [351] |
| S0501 | PipeMon | PipeMon can collect and send OS version and computer name as a part of its C2 beacon. [352] |
| S0124 | Pisloader | Pisloader has a command to collect victim system information, including the system name and OS version. [353] |
| S0254 | PLAINTEE | PLAINTEE collects general system enumeration data about the infected machine and checks the OS version. [354] |
| G1040 | Play | Play has leveraged tools to enumerate system information. [355] |
| S0013 | PlugX | PlugX has collected system information including OS version, processor information, RAM size, location, host name, IP, and screen size of the infected host. [356] |
| S0428 | PoetRAT | PoetRAT has the ability to gather information about the compromised host. [357] |
| S0453 | Pony | Pony has collected the Service Pack, language, and region information to send to the C2. [358] |
| S0216 | POORAIM | POORAIM can identify system information, including battery status. [186] |
| S0378 | PoshC2 | PoshC2 contains modules, such as Get-ComputerInfo , for enumerating common system information. [359] |
| S0139 | PowerDuke | PowerDuke has commands to get information about the victim's name, build, version, serial number, and memory usage. [360] |
| S0441 | PowerShower | PowerShower has collected system information on the infected host. [361] |
| S0223 | POWERSTATS | POWERSTATS can retrieve OS name/architecture and computer/domain name information from compromised hosts. [362] [363] |
| S0184 | POWRUNER | POWRUNER may collect information about the system by running hostname and systeminfo on a victim. [364] |
| S0113 | Prikormka | A module in Prikormka collects information from the victim about Windows OS version, computer name, battery info, and physical memory. [365] |
| S0238 | Proxysvc | Proxysvc collects the OS version, country name, MAC address, computer name, and physical memory statistics. [250] |
| S1228 | PUBLOAD | PUBLOAD has collected and sent system information including volume serial number, computer name, and system uptime to designated C2. [366] [367] PUBLOAD has also used several commands executed in sequence via cmd in a short interval to gather system information about the infected host including systeminfo . [368] PUBLOAD has decrypted shellcode that collects the computer name. [369] |
| S0196 | PUNCHBUGGY | PUNCHBUGGY can gather system information such as computer names. [370] |
| S0192 | Pupy | Pupy can grab a system’s information including the OS version, architecture, etc. [371] |
| S9019 | PureCrypter | PureCrypter can enumerate a targeted system's SerialNumber and Version. [372] [373] |
| S0650 | QakBot | QakBot can collect system information including the OS version and domain on a compromised host. [374] [375] [376] [313] |
| S1242 | Qilin | Qilin can detect whether a system is running FreeBSD, VMkernel (ESXi), Nutanix AHV, or a standard Linux distribution to enable platform-specific encryption behaviors. [377] |
| S0262 | QuasarRAT | QuasarRAT can gather system information from the victim’s machine including the OS type. [378] |
| S1148 | Raccoon Stealer | Raccoon Stealer gathers information on infected systems such as operating system, processor information, RAM, and display information. [379] [380] |
| S1212 | RansomHub | RansomHub can retrieve information about virtual machines. [381] |
| S1130 | Raspberry Robin | Raspberry Robin performs several system checks as part of anti-analysis mechanisms, including querying the operating system build number, processor vendor and type, video controller, and CPU temperature. [382] |
| S0241 | RATANKBA | RATANKBA gathers information about the OS architecture, OS name, and OS version/Service pack. [383] [384] |
| S0662 | RCSession | RCSession can gather system information from a compromised host. [385] |
| S0172 | Reaver | Reaver collects system information from the victim, including CPU speed, computer name, ANSI code page, OEM code page identifier for the OS, Microsoft Windows version, and memory information. [386] |
| G1039 | RedCurl | RedCurl has collected information about the target system, such as system information and list of network connections. [387] [388] |
| C0047 | RedDelta Modified PlugX Infection Chain Operations | Mustang Panda captured victim operating system type via User Agent analysis during RedDelta Modified PlugX Infection Chain Operations . [389] |
| S0153 | RedLeaves | RedLeaves can gather extended system information including the hostname, OS version number, platform, memory information, time elapsed since system startup, and CPU information. [101] [390] |
| S1240 | RedLine Stealer | RedLine Stealer can collect information about the local system. [391] [392] [393] [394] |
| S0332 | Remcos | Remcos can collect the OS version and process architecture of compromised hosts. [395] |
| S0125 | Remsec | Remsec can obtain the OS version information, computer name, processor architecture, machine role, and OS edition. [396] |
| S0379 | Revenge RAT | Revenge RAT collects the CPU information, OS information, and system language. [397] |
| S0496 | REvil | REvil can identify the username, machine name, system language, keyboard layout, and OS version on a compromised host. [398] [399] [400] [401] [401] [402] [403] [404] |
| S0433 | Rifdoor | Rifdoor has the ability to identify the Windows version on the compromised host. [405] |
| S1222 | RIFLESPINE | RIFLESPINE can collect system information after installation on infected systems. [406] |
| S0448 | Rising Sun | Rising Sun can detect the computer name and operating system. [407] |
| G0106 | Rocke | Rocke has used uname -m to collect the name and information about the infected system's kernel. [408] |
| S0270 | RogueRobin | RogueRobin gathers BIOS versions and manufacturers, the number of CPU cores, the total physical memory, and the computer name. [409] |
| S0240 | ROKRAT | ROKRAT can gather the hostname and the OS version to ensure it doesn’t run on a Windows XP or Windows Server 2003 systems. [410] [411] [412] [413] [414] [415] |
| S1078 | RotaJakiro | RotaJakiro executes a set of commands to collect device information, including uname . Another example is the cat /etc/*release | uniq command used to collect the current OS distribution. [416] |
| S1073 | Royal | Royal can use GetNativeSystemInfo to enumerate system processors. [417] [418] |
| S0148 | RTM | RTM can obtain the computer name, OS version, and default language identifier. [419] |
| S0253 | RunningRAT | RunningRAT gathers the OS version and processor information. [83] |
| S9037 | RustyWater | RustyWater has gathered the victim machine’s computer name. [420] |
| S0085 | S-Type | The initial beacon packet for S-Type contains the operating system version and file system of the victim. [297] |
| S1210 | Sagerunex | Sagerunex gathers information from the infected system such as hostname. [421] |
| S1018 | Saint Bot | Saint Bot can identify the OS version, CPU, and other details from a victim's machine. [422] |
| S1168 | SampleCheck5000 | SampleCheck5000 can create unique victim identifiers by using the compromised system’s computer name. [328] |
| G0034 | Sandworm Team | Sandworm Team used a backdoor to enumerate information about the infected system's operating system. [423] [424] |
| S1085 | Sardonic | Sardonic has the ability to collect the computer name, and CPU manufacturer name from a compromised machine. Sardonic also has the ability to execute the ver and systeminfo commands. [425] |
| G1015 | Scattered Spider | Scattered Spider has executed scripts to identify the underlying operating system to ensure it uses the correct installation package for malicious payloads. [426] |
| S0461 | SDBbot | SDBbot has the ability to identify the OS version, OS bit information and computer name. [172] [19] |
| S0382 | ServHelper | ServHelper will attempt to enumerate Windows version and system architecture. [427] |
| S0596 | ShadowPad | ShadowPad has discovered system information including memory status, CPU frequency, and OS versions. [428] |
| S9008 | Shai-Hulud | Shai-Hulud has gathered victim system information. [429] [430] |
| S0140 | Shamoon | Shamoon obtains the victim's operating system version and keyboard layout and sends the information to the C2 server. [431] [432] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors fingerprinted targeted SharePoint servers to identify OS version and running processes. [433] |
| S1019 | Shark | Shark can collect the GUID of a targeted machine. [294] [295] |
| S0546 | SharpStage | SharpStage has checked the system settings to see if Arabic is the configured language. [434] |
| S0450 | SHARPSTATS | SHARPSTATS has the ability to identify the IP address, machine name, and OS of the compromised host. [363] |
| S0445 | ShimRatReporter | ShimRatReporter gathered the operating system name and specific Windows version of an infected machine. [435] |
| S1178 | ShrinkLocker | ShrinkLocker uses WMI queries to gather various information about the victim machine and operating system. [436] [437] |
| S0217 | SHUTTERSPEED | SHUTTERSPEED can collect system information. [186] |
| G1008 | SideCopy | SideCopy has identified the OS version of a compromised host. [11] |
| S0610 | SideTwist | SideTwist can collect the computer name of a targeted system. [332] |
| G0121 | Sidewinder | Sidewinder has used tools to collect the computer name, OS version, installed hotfixes, as well as information regarding the memory and processor on a compromised host. [438] [439] |
| S0692 | SILENTTRINITY | SILENTTRINITY can collect information related to a compromised host, including OS version. [440] |
| S0468 | Skidmap | Skidmap has the ability to check whether the infected system’s OS is Debian or RHEL/CentOS to determine which cryptocurrency miner it should use. [441] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA has collected system name, OS version, adapter information, and memory usage from a victim machine. [442] |
| S0218 | SLOWDRIFT | SLOWDRIFT collects and sends system information to its C2. [186] |
| S0649 | SMOKEDHAM | SMOKEDHAM has used the systeminfo command on a compromised host. [443] |
| S1086 | Snip3 | Snip3 has the ability to query Win32_ComputerSystem for system information. [444] |
| S1124 | SocGholish | SocGholish has the ability to enumerate system information including the victim computer name. [445] [446] [447] |
| S0627 | SodaMaster | SodaMaster can enumerate the host name and OS version on a target system. [448] |
| S1166 | Solar | Solar can send basic information about the infected host to C2. [218] |
| S0615 | SombRAT | SombRAT can execute getinfo to enumerate the computer name and OS version of a compromised system. [449] |
| S0516 | SoreFang | SoreFang can collect the hostname, operating system configuration, and product ID on victim machines by executing Systeminfo . [450] |
| S0157 | SOUNDBITE | SOUNDBITE is capable of gathering system information. [235] |
| G0054 | Sowbug | Sowbug obtained OS version and hardware configuration from a victim. [451] |
| S0543 | Spark | Spark can collect the hostname, keyboard layout, and language from the system. [452] |
| S9024 | SPAWNCHIMERA | SPAWNCHIMERA has obtained system information such as release, uptime, and current time. [453] |
| S0374 | SpeakUp | SpeakUp uses the cat /proc/cpuinfo | grep -c "cpu family" 2>&1 command to gather system information. [454] |
| S0646 | SpicyOmelette | SpicyOmelette can identify the system name of a compromised host. [455] |
| S1234 | SplatCloak | SplatCloak has collected the Windows build number using the windows kernel API RtlGetVersion to determine if the response is 19000 or higher (Windows 10 version 2004 or later). [456] |
| S1030 | Squirrelwaffle | Squirrelwaffle has gathered victim computer information and configurations. [457] |
| S0058 | SslMM | SslMM sends information to its hard-coded C2, including OS version, service pack information, processor speed, system name, and OS install date. [458] |
| S1037 | STARWHALE | STARWHALE can gather the computer name of an infected host. [459] [460] |
| S1200 | StealBit | StealBit can enumerate the computer name and domain membership of the compromised system. [461] |
| G0038 | Stealth Falcon | Stealth Falcon malware gathers system information via WMI, including the system directory, build number, serial number, version, manufacturer, model, and total physical memory. [462] |
| S0380 | StoneDrill | StoneDrill has the capability to discover the system OS, Windows version, architecture and environment. [463] |
| G1053 | Storm-0501 | Storm-0501 has leveraged native Windows tools and commands such as systeminfo and open-source tools including OSQuery and ossec-win32 to query details about the endpoint. [464] |
| S0142 | StreamEx | StreamEx has the ability to enumerate system information. [465] |
| S1183 | StrelaStealer | StrelaStealer variants collect victim system information for exfiltration. [466] |
| S1034 | StrifeWater | StrifeWater can collect the OS version, architecture, and machine name to create a unique token for the infected host. [467] |
| S0603 | Stuxnet | Stuxnet collects system information including computer and domain names, OS version, and S7P paths. [468] |
| S0559 | SUNBURST | SUNBURST collected hostname and OS version. [469] [470] |
| S1064 | SVCReady | SVCReady has the ability to collect information such as computer name, computer manufacturer, BIOS, operating system, and firmware, including through the use of systeminfo.exe . [471] |
| S0242 | SynAck | SynAck gathers computer names, OS version info, and also checks installed keyboard layouts to estimate if it has been launched from a certain list of countries. [472] |
| S0060 | Sys10 | Sys10 collects the computer name, OS versioning information, and OS install date and sends the information to the C2. [458] |
| S0464 | SYSCON | SYSCON has the ability to use Systeminfo to identify system information. [96] |
| S9001 | SystemBC | SystemBC has collected username , build number and serial number, then sent the information to the C2 server. [473] [474] SystemBC has also gathered device name, operating system, and processor type. [475] |
| S0096 | Systeminfo | Systeminfo can be used to gather information about the operating system. [476] |
| S0663 | SysUpdate | SysUpdate can collect a system's architecture, operating system version, and hostname. [477] [478] |
| S0098 | T9000 | T9000 gathers and beacons the operating system build number and CPU Architecture (32-bit/64-bit) during installation. [479] |
| G1018 | TA2541 | TA2541 has collected system information prior to downloading malware on the targeted host. [480] |
| S0467 | TajMahal | TajMahal has the ability to identify hardware information, the computer name, and OS information on an infected host. [481] |
| G0139 | TeamTNT | TeamTNT has searched for system version, architecture, and hostname information. [482] [483] |
| S0665 | ThreatNeedle | ThreatNeedle can collect system profile information from a compromised host. [484] |
| S1239 | TONESHELL | TONESHELL has the ability to retrieve the name of the infected machine. [367] [485] [486] |
| S0266 | TrickBot | TrickBot gathers the OS version, machine name, CPU type, amount of RAM available, and UEFI/BIOS firmware information from the victim’s machine. [487] [488] [489] [490] |
| S0094 | Trojan.Karagany | Trojan.Karagany can capture information regarding the victim's OS, security, and hardware configuration. [491] |
| S1196 | Troll Stealer | Troll Stealer can collect local system information. [492] [177] |
| G0081 | Tropic Trooper | Tropic Trooper has detected a target system’s OS version. [493] [494] |
| S9034 | Tsundere Botnet | Tsundere Botnet has collected the machine’s MAC address, total memory, GPU information and other system information. [495] |
| S0647 | Turian | Turian can retrieve system information including OS version, memory usage, local hostname, and system adapter information. [496] |
| G0010 | Turla | Turla surveys a system upon check-in to discover operating system configuration details using the systeminfo and set commands. [497] [498] |
| S0199 | TURNEDUP | TURNEDUP is capable of gathering system information. [499] |
| S0130 | Unknown Logger | Unknown Logger can obtain information about the victim computer name, physical memory, country, and date. [500] |
| S0275 | UPPERCUT | UPPERCUT has the capability to gather the system’s hostname and OS version. [501] [336] |
| S0022 | Uroburos | Uroburos has the ability to gather basic system information and run the POSIX API gethostbyname . [502] |
| S0386 | Ursnif | Ursnif has used Systeminfo to gather system information. [503] |
| S0476 | Valak | Valak can determine the Windows version and computer name on a compromised host. [504] [505] |
| S0257 | VERMIN | VERMIN collects the OS name, machine name, and architecture information. [506] |
| G1055 | VOID MANTICORE | VOID MANTICORE has gathered system information and disseminated it back to C2. [507] |
| S0180 | Volgmer | Volgmer can gather system information, the computer name, OS version, drive and serial information from the victim's machine. [508] [509] [510] |
| S0670 | WarzoneRAT | WarzoneRAT can collect compromised host information, including OS version, PC name, RAM size, and CPU details. [511] |
| S0514 | WellMess | WellMess can identify the computer name of a compromised host. [512] [513] |
| G0124 | Windigo | Windigo has used a script to detect which Linux distribution and version is currently installed on the system. [81] |
| S0155 | WINDSHIELD | WINDSHIELD can gather the victim computer name. [235] |
| G0112 | Windshift | Windshift has used malware to identify the computer name of a compromised host. [514] |
| S0219 | WINERACK | WINERACK can gather information about the host. [186] |
| S0176 | Wingbird | Wingbird checks the victim OS version after executing to determine where to drop files based on whether the victim is 32-bit or 64-bit. [515] |
| S0059 | WinMM | WinMM collects the system name, OS version including service pack, and system install date and sends the information to the C2 server. [458] |
| S0141 | Winnti for Windows | Winnti for Windows can determine if the OS on a compromised host is newer than Windows XP. [516] |
| G1035 | Winter Vivern | Winter Vivern script execution includes basic victim information gathering steps which are then transmitted to command and control servers. [517] |
| G0102 | Wizard Spider | Wizard Spider has used Systeminfo and similar commands to acquire detailed configuration information of a victim's machine. Wizard Spider has also utilized the PowerShell cmdlet Get-ADComputer to collect DNS hostnames, last logon dates, and operating system information from Active Directory. [518] [519] |
| S1065 | Woody RAT | Woody RAT can retrieve the following information from an infected machine: OS, architecture, computer name, OS build version, and environment variables. [520] |
| S0161 | XAgentOSX | XAgentOSX contains the getInstalledAPP function to run ls -la /Applications to gather what applications are installed. [521] |
| S0658 | XCSSET | XCSSET identifies the macOS version and uses ioreg to determine serial number. [522] |
| S1207 | XLoader | XLoader can collect system information and supported language information from the victim machine. [523] |
| S1248 | XORIndex Loader | XORIndex Loader has the ability to collect the hostname, OS Username, Geolocation, and OS version of an infected host. [524] |
| S0388 | YAHOYAH | YAHOYAH checks for the system’s Windows OS version and hostname. [493] |
| S0248 | yty | yty gathers the computer name, CPU information, Microsoft Windows version, and runs the command systeminfo . [525] |
| S0251 | Zebrocy | Zebrocy collects the OS version and computer name. Zebrocy also runs the systeminfo command to gather system information. [526] [91] [527] [92] [528] [529] [530] |
| S0230 | ZeroT | ZeroT gathers the victim's computer name, Windows version, and system language, and then sends it to its C2 server. [531] |
| S0330 | Zeus Panda | Zeus Panda collects the OS version, system architecture, computer name, product ID, install date, and information on the keyboard mapping to determine the language used on the system. [532] [533] |
| G0128 | ZIRCONIUM | ZIRCONIUM has used a tool to capture the processor architecture of a compromised host in order to register it with C2. [534] |
| S0086 | ZLib | ZLib has the ability to enumerate system information. [297] |
| S0350 | zwShell | zwShell can obtain the victim PC name and OS version. [535] |
| S0412 | ZxShell | ZxShell can collect the local hostname, operating system details, CPU speed, and total physical memory. [536] |
| S1013 | ZxxZ | ZxxZ has collected the host name and operating system product name from a compromised machine. [537] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0525 | System Discovery via Native and Remote Utilities | AN1452 | Detection of processes executing system environment inspection operations followed by access to OS configuration APIs or registry locations that expose OS version, architecture, patch level, or hardware characteristics. Defenders observe process execution retrieving system configuration metadata immediately after process startup. |
| AN1453 | Execution of system enumeration commands such as uname , df , uptime , hostname , lscpu , and cat /etc/os-release through local terminal or scripts. |  |  |
| AN1454 | Execution of system info utilities like systemsetup , sw_vers , uname , or sysctl by terminal or scripted processes. |  |  |
| AN1455 | Execution of esxcli system hostname get , esxcli system version get , or esxcli hardware commands through SSH or local shell. |  |  |
| AN1456 | Use of cloud API calls (e.g., AWS EC2 DescribeInstances, Azure VM Inventory) to enumerate system configurations across assets. |  |  |
| AN1457 | Execution of show version , show hardware , or show system commands through CLI via SSH or console. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0525 | System Discovery via Native and Remote Utilities | AN1452 | Detection of processes executing system environment inspection operations followed by access to OS configuration APIs or registry locations that expose OS version, architecture, patch level, or hardware characteristics. Defenders observe process execution retrieving system configuration metadata immediately after process startup. |
| AN1453 | Execution of system enumeration commands such as uname , df , uptime , hostname , lscpu , and cat /etc/os-release through local terminal or scripts. |  |  |
| AN1454 | Execution of system info utilities like systemsetup , sw_vers , uname , or sysctl by terminal or scripted processes. |  |  |
| AN1455 | Execution of esxcli system hostname get , esxcli system version get , or esxcli hardware commands through SSH or local shell. |  |  |
| AN1456 | Use of cloud API calls (e.g., AWS EC2 DescribeInstances, Azure VM Inventory) to enumerate system configurations across assets. |  |  |
| AN1457 | Execution of show version , show hardware , or show system commands through CLI via SSH or console. |  |  |

---

## References

- [US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved October 19, 2020.](https://www.us-cert.gov/ncas/alerts/TA18-106A)
- [Michael Dawson. (2021, August 30). Hypervisor Jackpotting, Part 2: eCrime Actors Increase Targeting of ESXi Servers with Ransomware. Retrieved March 26, 2025.](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
- [Jason Hill. (2023, February 8). VMware ESXi in the Line of Ransomware Fire. Retrieved March 26, 2025.](https://www.varonis.com/blog/vmware-esxi-in-the-line-of-ransomware-fire)
- [Amazon. (n.d.). describe-instance-information. Retrieved March 3, 2020.](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-instance-information.html)
- [Google. (n.d.). Rest Resource: instance. Retrieved March 3, 2020.](https://cloud.google.com/compute/docs/reference/rest/v1/instances)
- [Microsoft. (2019, March 1). Virtual Machines - Get. Retrieved October 8, 2019.](https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines/get)
- [Phile Stokes. (2018, September 20). On the Trail of OSX.FairyTale | Adware Playing at Malware. Retrieved August 24, 2021.](https://www.sentinelone.com/blog/trail-osx-fairytale-adware-playing-malware/)
- [Phil Stokes. (2021, February 16). 20 Common Tools & Techniques Used by macOS Threat Actors & Malware. Retrieved August 23, 2021.](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
- [Crowdstrike Global Intelligence Team. (2014, June 9). CrowdStrike Intelligence Report: Putter Panda. Retrieved January 22, 2016.](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)
- [Juan Andrés Guerrero-Saade & Tom Hegel. (2024, March 21). AcidPour | New Embedded Wiper Variant of AcidRain Appears in Ukraine. Retrieved November 25, 2024.](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [FireEye Threat Intelligence. (2015, December 1). China-based Cyber Threat Group Uses Dropbox for Malware Communications and Targets Hong Kong Media Outlets. Retrieved December 4, 2015.](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)
- [ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
- [Bitdefender. (2015, December). APT28 Under the Scope. Retrieved February 23, 2017.](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
- [Zhang, X. (2018, April 05). Analysis of New Agent Tesla Spyware Variant. Retrieved November 5, 2018.](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)
- [Zhang, X. (2017, June 28). In-Depth Analysis of A New Variant of .NET Malware AgentTesla. Retrieved November 5, 2018.](https://www.fortinet.com/blog/threat-research/in-depth-analysis-of-net-malware-javaupdtr.html)
- [Jazi, H. (2020, April 16). New AgentTesla variant steals WiFi credentials. Retrieved May 19, 2020.](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)
- [Max Kersten & Alexandre Mundo. (2023, November 29). Akira Ransomware. Retrieved April 4, 2024.](https://www.trellix.com/blogs/research/akira-ransomware/)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [Kasuya, M. (2020, January 8). Threat Spotlight: Amadey Bot Targets Non-Russian Users. Retrieved July 14, 2022.](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
- [Grange, W. (2020, July 13). Anchor_dns malware goes cross platform. Retrieved September 10, 2020.](https://medium.com/stage-2-security/anchor-dns-malware-family-goes-cross-platform-d807ba13ca30)
- [Anthropic. (2025, November). Disrupting the first reported AI-orchestrated cyber espionage campaign. Retrieved April 20, 2026.](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
- [Cybersecurity and Infrastructure Security Agency. (2021, February 21). AppleJeus: Analysis of North Korea’s Cryptocurrency Malware. Retrieved March 1, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [Grunzweig, J., et al. (2016, May 24). New Wekby Attacks Use DNS Requests As Command and Control Mechanism. Retrieved November 15, 2018.](https://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
- [Ahl, I. (2017, June 06). Privileges and Credentials: Phished at the Request of Counsel. Retrieved May 17, 2018.](https://www.fireeye.com/blog/threat-research/2017/06/phished-at-the-request-of-counsel.html)
- [Grunzweig, J., Lee, B. (2016, January 22). New Attacks Linked to C0d0so0 Group. Retrieved August 2, 2018.](https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/)
- [Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
- [Yates, M. (2017, June 18). APT3 Uncovered: The code evolution of Pirpi. Retrieved September 28, 2017.](https://recon.cx/2017/montreal/resources/slides/RECON-MTL-2017-evolution_of_pirpi.pdf)
- [Foltýn, T. (2018, March 13). OceanLotus ships new backdoor using old tricks. Retrieved May 22, 2018.](https://www.welivesecurity.com/2018/03/13/oceanlotus-ships-new-backdoor/)
- [Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)
- [Dumont, R.. (2019, April 9). OceanLotus: macOS malware update. Retrieved April 15, 2019.](https://www.welivesecurity.com/2019/04/09/oceanlotus-macos-malware-update/)
- [Henderson, S., et al. (2020, April 22). Vietnamese Threat Actors APT32 Targeting Wuhan Government and Chinese Ministry of Emergency Management in Latest Example of COVID-19 Related Espionage. Retrieved April 28, 2020.](https://www.fireeye.com/blog/threat-research/2020/04/apt32-targeting-chinese-government-in-covid-19-related-espionage.html)
- [Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)
- [DHS/CISA. (2020, August 26). FASTCash 2.0: North Korea's BeagleBoyz Robbing Banks. Retrieved September 29, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)
- [Nikita Rostovcev. (2022, August 18). APT41 World Tour 2021 on a tight schedule. Retrieved February 22, 2024.](https://www.group-ib.com/blog/apt41-world-tour-2021/)
- [Mandiant. (n.d.). APT42: Crooked Charms, Cons and Compromises. Retrieved October 9, 2024.](https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf)
- [Wiley, B. et al. (2021, December 29). OverWatch Exposes AQUATIC PANDA in Possession of Log4Shell Exploit Tools During Hands-on Intrusion Attempt. Retrieved January 18, 2022.](https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/)
- [Canadian Centre for Cyber Security. (2024, April 24). Cyber Activity Impacting CISCO ASA VPNs. Retrieved January 6, 2025.](https://www.cyber.gc.ca/en/news-events/cyber-activity-impacting-cisco-asa-vpns)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Unit 42. (2025, December 11). Hamas-Affiliated Ashen Lepus Targets Middle Eastern Diplomatic Entities With New AshTag Malware Suite. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
- [Doaty, J., Garrett, P.. (2018, September 10). We’re Seeing a Resurgence of the Demonic Astaroth WMIC Trojan. Retrieved September 25, 2024.](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)
- [Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
- [Proofpoint. (2018, July 30). New version of AZORult stealer improves loading features, spreads alongside ransomware in new campaign. Retrieved November 29, 2018.](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)
- [Unit 42. (2019, February 22). New BabyShark Malware Targets U.S. National Security Think Tanks. Retrieved October 7, 2019.](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
- [Hinchliffe, A. and Falcone, R. (2020, May 11). Updated BackConfig Malware Targeting Government and Military Organizations in South Asia. Retrieved June 17, 2020.](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)
- [Symantec Security Response. (2014, June 30). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
- [Slowik, J. (2021, October). THE BAFFLING BERSERK BEAR: A DECADE’S ACTIVITY TARGETING CRITICAL INFRASTRUCTURE. Retrieved December 6, 2021.](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
- [FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved November 17, 2024.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
- [US-CERT. (2018, February 06). Malware Analysis Report (MAR) - 10135536-G. Retrieved June 7, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)
- [Accenture iDefense Unit. (2019, March 5). Mudcarp's Focus on Submarine Technologies. Retrieved August 24, 2021.](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
- [Savelesky, K., et al. (2019, July 23). ABADBABE 8BADFOOD: Discovering BADHATCH and a Detailed Look at FIN8's Tooling. Retrieved September 8, 2021.](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [Bar, T., Conant, S. (2017, October 20). BadPatch. Retrieved November 13, 2018.](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)
- [Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
- [US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1, 2020.](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
- [eSentire Threat Response Unit (TRU). (2024, November 14). Bored BeaverTail & InvisibleFerret Yacht Club – A Lazarus Lure Pt.2. Retrieved October 17, 2025.](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Hayashi, K., Ray, V. (2018, July 31). Bisonal Malware Used in Attacks Against Russia and South Korea. Retrieved August 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)
- [Zykov, K. (2020, August 13). CactusPete APT group’s updated Bisonal backdoor. Retrieved May 5, 2021.](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [Zargarov, N. (2022, May 2). New Black Basta Ransomware Hijacks Windows Fax Service. Retrieved March 7, 2023.](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
- [Cyble. (2022, May 6). New ransomware variant targeting high-value organizations. Retrieved November 17, 2024.](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
- [US Federal Bureau of Investigation & US Secret Service. (2022, February 11). Indicators of Compromise Associated with BlackByte Ransomware. Retrieved December 16, 2024.](https://www.ic3.gov/CSA/2022/220211.pdf)
- [Symantec Threat Hunter Team. (2022, October 21). Exbyte: BlackByte Ransomware Attackers Deploy New Exfiltration Tool. Retrieved December 16, 2024.](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [F-Secure Labs. (2014). BlackEnergy & Quedagh: The convergence of crimeware and APT attacks. Retrieved March 24, 2016.](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
- [Baumgartner, K. and Garnaeva, M.. (2014, November 3). BE2 custom plugins, router abuse, and target profiles. Retrieved March 24, 2016.](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
- [US-CERT. (2020, August 19). MAR-10295134-1.v1 – North Korean Remote Access Trojan: BLINDINGCAN. Retrieved August 19, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
- [Lambert, T. (2020, May 7). Introducing Blue Mockingbird. Retrieved May 26, 2020.](https://redcanary.com/blog/blue-mockingbird-cryptominer/)
- [Cash, D., Grunzweig, J., Meltzer, M., Adair, S., Lancaster, T. (2021, August 17). North Korean APT InkySquid Infects Victims Using Browser Exploits. Retrieved September 30, 2021.](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
- [Scott Henderson, Cristiana Kittner, Sarah Hawley & Mark Lechtik, Google Cloud. (2023, January 19). Suspected Chinese Threat Actors Exploiting FortiOS Vulnerability (CVE-2022-42475). Retrieved December 31, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [MSTIC. (2021, May 28). Breaking down NOBELIUM’s latest early-stage toolset. Retrieved August 4, 2021.](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
- [Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
- [Stolyarov, V. (2022, March 17). Exposing initial access broker with ties to Conti. Retrieved August 18, 2022.](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)
- [Merriman, K. and Trouerbach, P. (2022, April 28). This isn't Optimus Prime's Bumblebee but it's Still Transforming. Retrieved August 22, 2022.](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
- [Kamble, V. (2022, June 28). Bumblebee: New Loader Rapidly Assuming Central Position in Cyber-crime Ecosystem. Retrieved August 24, 2022.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)
- [Sushko, O. (2019, April 17). macOS Bundlore: Mac Virus Bypassing macOS Security Features. Retrieved June 30, 2020.](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
- [Malhotra, A. (2022, March 15). Threat Advisory: CaddyWiper. Retrieved March 23, 2022.](https://blog.talosintelligence.com/2022/03/threat-advisory-caddywiper.html)
- [Threat Intelligence Team. (2022, March 18). Double header: IsaacWiper and CaddyWiper . Retrieved April 11, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/03/double-header-isaacwiper-and-caddywiper/)
- [Symantec Security Response. (2015, December 7). Iran-based attackers use back door threats to spy on Middle Eastern targets. Retrieved April 17, 2019.](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
- [Falcone, R., Lee, B. (2018, November 20). Sofacy Continues Global Attacks and Wheels Out New ‘Cannon’ Trojan. Retrieved November 26, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
- [Lee, B., Falcone, R. (2018, December 12). Dear Joohn: The Sofacy Group’s Global Campaign. Retrieved April 19, 2019.](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)
- [Giuliani, M., Allievi, A. (2011, February 28). Carberp - a modular information stealing trojan. Retrieved September 12, 2024.](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
- [Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
- [Grunzweig, J. and Wilhoit, K. (2018, November 29). The Fractured Block Campaign: CARROTBAT Used to Deliver Malware Targeting Southeast Asia. Retrieved June 2, 2020.](https://unit42.paloaltonetworks.com/unit42-the-fractured-block-campaign-carrotbat-malware-used-to-deliver-malware-targeting-southeast-asia/)
- [McCabe, A. (2020, January 23). The Fractured Statue Campaign: U.S. Government Agency Targeted in Spear-Phishing Attacks. Retrieved June 2, 2020.](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Salem, E. (2020, November 17). CHAES: Novel Malware Targeting Latin American E-Commerce. Retrieved June 30, 2021.](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Miller-Osborn, J. and Grunzweig, J.. (2017, February 16). menuPass Returns with New Malware and New Attacks Against Japanese Academics and Organizations. Retrieved March 1, 2017.](http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Chen, T. and Chen, Z. (2020, February 17). CLAMBLING - A New Backdoor Base On Dropbox. Retrieved November 12, 2021.](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
- [Microsoft. (n.d.). Dir. Retrieved April 18, 2016.](https://technet.microsoft.com/en-us/library/cc755121.aspx)
- [Grunzweig, J. (2018, January 31). Comnie Continues to Target Organizations in East Asia. Retrieved June 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
- [Amaury G., Coline Chavane, Felix Aimé and Sekoia TDR. (2025, March 31). From Contagious to ClickFake Interview: Lazarus leveraging the ClickFix tactic. Retrieved April 1, 2025.](https://blog.sekoia.io/clickfake-interview-campaign-by-lazarus/)
- [FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
- [cobbr. (2021, April 21). Covenant. Retrieved September 4, 2024.](https://github.com/cobbr/Covenant)
- [F-Secure Labs. (2015, April 22). CozyDuke: Malware Analysis. Retrieved December 10, 2015.](https://www.f-secure.com/documents/996508/1030745/CozyDuke)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [N. Baisini. (2022, July 13). Transparent Tribe begins targeting education sector in latest campaign. Retrieved September 22, 2022.](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
- [Kohler, A. and Lopez, C. (2024, April 30). Malware: Cuckoo Behaves Like Cross Between Infostealer and Spyware. Retrieved August 20, 2024.](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
- [Stokes, P. (2024, May 9). macOS Cuckoo Stealer | Ensuring Detection and Defense as New Samples Rapidly Emerge. Retrieved August 20, 2024.](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)
- [Symantec Threat Hunter Team. (2019, September 18). Tortoiseshell Group Targets IT Providers in Saudi Arabia in Probable Supply Chain Attacks. Retrieved May 20, 2024.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/tortoiseshell-apt-supply-chain)
- [Lin, M. et al. (2024, January 31). Cutting Edge, Part 2: Investigating Ivanti Connect Secure VPN Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
- [NCSC. (2022, February 23). Cyclops Blink Malware Analysis Report. Retrieved March 3, 2022.](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
- [Ahn Ho, Facundo Muñoz, & Marc-Etienne M.Léveillé. (2024, March 7). Evasive Panda leverages Monlam Festival to target Tibetans. Retrieved July 25, 2024.](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
- [TrendMicro. (2014, September 03). DARKCOMET. Retrieved November 6, 2018.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
- [Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [McGraw, T. (2024, December 4). Black Basta Ransomware Campaign Drops Zbot, DarkGate, and Custom Malware. Retrieved December 9, 2024.](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
- [Kaspersky Lab's Global Research & Analysis Team. (2015, August 10). Darkhotel's attacks in 2015. Retrieved November 2, 2018.](https://securelist.com/darkhotels-attacks-in-2015/71713/)
- [Microsoft. (2016, July 14). Reverse engineering DUBNIUM – Stage 2 payload analysis . Retrieved March 31, 2021.](https://www.microsoft.com/security/blog/2016/07/14/reverse-engineering-dubnium-stage-2-payload-analysis/)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Shulmin, A., Yunakovsky, S. (2017, April 28). Use of DNS Tunneling for C&C Communications. Retrieved November 5, 2018.](https://securelist.com/use-of-dns-tunneling-for-cc-communications/78203/)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Fidelis Cybersecurity. (2016, February 29). The Turbo Campaign, Featuring Derusbi for 64-bit Linux. Retrieved March 2, 2016.](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [Microsoft. (2023, February 3). diskpart. Retrieved March 17, 2025.](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskpart)
- [ClearSky Cyber Security. (2017, December). Charming Kitten. Retrieved December 27, 2017.](http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf)
- [Check Point Research. (2021, January 4). Stopping Serial Killer: Catching the Next Strike. Retrieved September 7, 2021.](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)
- [Cybereason Nocturnus Team. (2020, December 9). MOLERATS IN THE CLOUD: New Malware Arsenal Abuses Cloud Platforms in Middle East Espionage Campaign. Retrieved December 22, 2020.](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
- [Konstantin Zykov. (2019, September 23). Hello! My name is Dtrack. Retrieved January 20, 2021.](https://securelist.com/my-name-is-dtrack/93338/)
- [Hod Gavriel. (2019, November 21). Dtrack: In-depth analysis of APT on a nuclear power plant. Retrieved January 20, 2021.](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [ClearSky. (2016, January 7). Operation DustySky. Retrieved January 8, 2016.](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
- [hasherezade. (2015, November 4). A Technical Look At Dyreza. Retrieved June 15, 2020.](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
- [Joe Security. (n.d.). Analysis Report fasm.dll. Retrieved November 17, 2024.](https://www.joesandbox.com/analysis/326673/0/pdf)
- [NHS Digital. (2020, November 26). Egregor Ransomware The RaaS successor to Maze. Retrieved December 29, 2020.](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
- [Falcone, R., et al.. (2015, June 16). Operation Lotus Blossom. Retrieved February 15, 2016.](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)
- [Falcone, R. and Miller-Osborn, J. (2016, February 3). Emissary Trojan Changelog: Did Operation Lotus Blossom Cause It to Evolve?. Retrieved February 15, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Adamitis, D. et al. (2019, June 4). It's alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign. Retrieved May 11, 2020.](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
- [Kaspersky Lab's Global Research & Analysis Team. (2014, August 06). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroboros. Retrieved November 7, 2018.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
- [Adamitis, D. (2020, May 6). Phantom in the Command Shell. Retrieved November 17, 2024.](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
- [Threat Intelligence and Research. (2015, March 30). VOLATILE CEDAR. Retrieved February 8, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
- [US-CERT. (2017, November 22). Alert (TA17-318A): HIDDEN COBRA – North Korean Remote Administration Tool: FALLCHILL. Retrieved December 7, 2017.](https://www.us-cert.gov/ncas/alerts/TA17-318A)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Somerville, L. and Toro, A. (2017, March 30). Playing Cat & Mouse: Introducing the Felismus Malware. Retrieved November 16, 2017.](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)
- [Patil, S. (2018, June 26). Microsoft Office Vulnerabilities Used to Distribute FELIXROOT Backdoor in Recent Campaign. Retrieved November 17, 2024.](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
- [Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
- [Yamout, M. (2021, November 29). WIRTE’s campaign in the Middle East ‘living off the land’ since at least 2019. Retrieved February 1, 2022.](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [Sygnia Incident Response Team. (2022, January 5). TG2003: ELEPHANT BEETLE UNCOVERING AN ORGANIZED FINANCIAL-THEFT OPERATION. Retrieved February 9, 2023.](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)
- [The BlackBerry Research and Intelligence Team. (2024, April 17). Threat Group FIN7 Targets the U.S. Automotive Industry. Retrieved May 1, 2025.](https://blogs.blackberry.com/en/2024/04/fin7-targets-the-united-states-automotive-industry)
- [Symantec Threat Hunter Team. (2023, July 18). FIN8 Uses Revamped Sardonic Backdoor to Deliver Noberus Ransomware. Retrieved August 9, 2023.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)
- [Grunzweig, J. (2018, October 01). NOKKI Almost Ties the Knot with DOGCALL: Reaper Group Uses New Malware to Deploy RAT. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
- [FinFisher. (n.d.). Retrieved September 12, 2024.](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
- [Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
- [Proofpoint Staff. (2018, March 7). Leaked Ammyy Admin Source Code Turned into Malware. Retrieved May 28, 2019.](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Bryan Lee and Rob Downs. (2016, February 12). A Look Into Fysbis: Sofacy’s Linux Backdoor. Retrieved September 10, 2017.](https://researchcenter.paloaltonetworks.com/2016/02/a-look-into-fysbis-sofacys-linux-backdoor/)
- [Kasza, A. and Reichel, D. (2017, February 27). The Gamaredon Group Toolset Evolution. Retrieved March 1, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)
- [Kakara, H., Maruyama, E. (2020, April 17). Gamaredon APT Group Use Covid-19 Lure in Campaigns. Retrieved May 19, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/gamaredon-apt-group-use-covid-19-lure-in-campaigns/)
- [CERT-EE. (2021, January 27). Gamaredon Infection: From Dropper to Entry. Retrieved February 17, 2022.](https://www.ria.ee/sites/default/files/content-editors/kuberturve/tale_of_gamaredon_infection.pdf)
- [Threat Hunter Team, Symantec and Carbon Black. (2025, April 10). Shuckworm Targets Foreign Military Mission Based in Ukraine. Retrieved July 23, 2025.](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Schwarz, D. et al. (2019, October 16). TA505 Distributes New SDBbot Remote Access Trojan with Get2 Downloader. Retrieved May 29, 2020.](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
- [Quinn, J. (2019, March 25). The odd case of a Gh0stRAT variant. Retrieved July 15, 2020.](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
- [Kirill Boychenko. (2026, January 31). GlassWorm Loader Hits Open VSX via Developer Account Compromise. Retrieved April 10, 2026.](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
- [Lotan Sery. (2025, December 10). GlassWorm Goes Native: Same Infrastructure, Hardened Delivery. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)
- [Trustwave SpiderLabs. (2020, June 25). The Golden Tax Department and Emergence of GoldenSpy Malware. Retrieved July 23, 2020.](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)
- [Symantec Threat Hunter Team. (2024, May 16). Springtail: New Linux Backdoor Added to Toolkit. Retrieved January 17, 2025.](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
- [Szappanos, G. & Brandt, A. (2021, March 1). “Gootloader” expands its payload delivery options. Retrieved September 30, 2022.](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
- [Sandvik, Runa. (2021, October 1). Made In America: Green Lambert for OS X. Retrieved March 21, 2022.](https://objective-see.com/blog/blog_0x68.html)
- [Sandvik, Runa. (2021, October 18). Green Lambert and ATT&CK. Retrieved November 17, 2024.](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)
- [Namestnikov, Y. and Aime, F. (2019, May 8). FIN7.5: the infamous cybercrime rig “FIN7” continues its activities. Retrieved October 11, 2019.](https://securelist.com/fin7-5-the-infamous-cybercrime-rig-fin7-continues-its-activities/90703/)
- [Priego, A. (2021, July). THE BROTHERS GRIM: THE REVERSING TALE OF GRIMAGENT MALWARE USED BY RYUK. Retrieved September 19, 2024.](https://www.group-ib.com/blog/grimagent/)
- [Carr, N., et al. (2017, April 24). FIN7 Evolution and the Phishing LNK. Retrieved April 24, 2017.](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)
- [FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
- [Wan, Y. (2025, March 3). Havoc: SharePoint with Microsoft Graph API turns into FUD C2. Retrieved August 4, 2025.](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)
- [Patil, S. and Williams, M.. (2019, June 5). Government Sector in Central Asia Targeted With New HAWKBALL Backdoor Delivered via Microsoft Office Vulnerabilities. Retrieved June 20, 2019.](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)
- [Guerrero-Saade, J. (2022, February 23). HermeticWiper | New Destructive Malware Used In Cyber Attacks on Ukraine. Retrieved March 25, 2022.](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
- [Thomas, W. et al. (2022, February 25). CrowdStrike Falcon Protects from New Wiper Malware Used in Ukraine Cyberattacks. Retrieved March 25, 2022.](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
- [ESET. (2022, March 1). IsaacWiper and HermeticWizard: New wiper and worm targetingUkraine. Retrieved April 10, 2022.](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
- [Dani, M. (2022, March 1). Ukrainian Targets Hit by HermeticWiper, New Datawiper Malware. Retrieved March 25, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Breitenbacher, D. (2024). Unmasking HiddenFace. Retrieved April 17, 2026.](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [PT ESC Threat Intelligence. (2020, June 4). COVID-19 and New Year greetings: an investigation into the tools and methods used by the Higaisa group. Retrieved March 2, 2021.](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/covid-19-and-new-year-greetings-the-higaisa-group/)
- [Malwarebytes Threat Intelligence Team. (2020, June 4). New LNK attack tied to Higaisa APT discovered. Retrieved March 2, 2021.](https://blog.malwarebytes.com/threat-analysis/2020/06/higaisa/)
- [Chen, J. et al. (2021, February 3). Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes. Retrieved April 5, 2021.](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [US-CERT. (2020, February 20). MAR-10271944-1.v1 – North Korean Trojan: HOTCROISSANT. Retrieved May 1, 2020.](https://www.us-cert.gov/ncas/analysis-reports/ar20-045d)
- [Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
- [CrowdStrike. (2022, May). ICEAPPLE: A NOVEL INTERNET INFORMATION SERVICES (IIS) POST-EXPLOITATION FRAMEWORK. Retrieved June 27, 2022.](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
- [Kessem, L., et al. (2017, November 13). New Banking Trojan IcedID Discovered by IBM X-Force Research. Retrieved July 14, 2020.](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)
- [DFIR. (2022, April 25). Quantum Ransomware. Retrieved July 26, 2024.](https://thedfirreport.com/2022/04/25/quantum-ransomware/)
- [PwC Threat Intelligence. (2023, October 25). Yellow Liderc ships its scripts and delivers IMAPLoader malware. Retrieved August 14, 2024.](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
- [Symantec. (2018, March 14). Inception Framework: Alive and Well, and Hiding Behind Proxies. Retrieved May 8, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/inception-framework-hiding-behind-proxies)
- [Dragos Inc.. (2017, June 13). CRASHOVERRIDE Analysis of the Threat to Electric Grid Operations. Retrieved December 18, 2020.](https://dragos.com/blog/crashoverride/CrashOverride-01.pdf)
- [ASERT Team. (2018, April 04). Innaput Actors Utilize Remote Access Trojan Since 2016, Presumably Targeting Victim Files. Retrieved July 9, 2018.](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)
- [Insikt Group. (2025, February 13). Inside the Scam: North Korea’s IT Worker Threat. Retrieved October 17, 2025.](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Check Point. (2024, November 12). Hamas-affiliated Threat Actor WIRTE Continues its Middle East Operations and Moves to Disruptive Activity. Retrieved April 20, 2026.](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
- [Sancho, D., et al. (2012, May 22). IXESHE An APT Campaign. Retrieved June 7, 2019.](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [Bingham, J. (2013, February 11). Cross-Platform Frutas RAT Builder and Back Door. Retrieved April 23, 2019.](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)
- [Hromcova, Z. and Burgher, A. (2023, September 21). OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes. Retrieved November 21, 2024.](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
- [Mohammad Kazem Hassan Nejad, WithSecure. (2024, April 17). KAPEKA A novel backdoor spotted in Eastern Europe. Retrieved January 6, 2025.](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)
- [Yadav, A., et al. (2016, January 29). Malicious Office files dropping Kasidet and Dridex. Retrieved March 24, 2016.](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)
- [Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Ray, V. and Hayashi, K. (2019, February 1). Tracking OceanLotus’ new Downloader, KerrDown. Retrieved October 1, 2021.](https://unit42.paloaltonetworks.com/tracking-oceanlotus-new-downloader-kerrdown/)
- [Parys, B. (2017, February 11). The KeyBoys are back in town. Retrieved June 13, 2019.](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)
- [Guarnieri, C., Schloesser M. (2013, June 7). KeyBoy, Targeted Attacks against Vietnam and India. Retrieved June 14, 2019.](https://blog.rapid7.com/2013/06/07/keyboy-targeted-attacks-against-vietnam-and-india/)
- [US-CERT. (2018, August 09). MAR-10135536-17 – North Korean Trojan: KEYMARBLE. Retrieved August 16, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
- [Tarakanov , D.. (2013, September 11). The “Kimsuky” Operation: A North Korean APT?. Retrieved August 13, 2019.](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [Den Iuzvyk, Tim Peck. (2025, February 13). Analyzing DEEP#DRIVE: North Korean Threat Actors Observed Exploiting Trusted Platforms for Targeted Attacks. Retrieved August 19, 2025.](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Jazi, H. (2021, February). LazyScripter: From Empire to double RAT. Retrieved November 17, 2024.](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
- [M.Leveille, M., Sanmillan, I. (2021, January). A WILD KOBALOS APPEARS Tricksy Linux malware goes after HPCs. Retrieved August 24, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
- [Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
- [Rascagneres, P. (2017, May 03). KONNI: A Malware Under The Radar For Years. Retrieved November 5, 2018.](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
- [Karmi, D. (2020, January 4). A Look Into Konni 2019 Campaign. Retrieved April 28, 2020.](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)
- [Threat Intelligence Team. (2021, August 23). New variant of Konni malware used in campaign targetting Russia. Retrieved January 5, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
- [Black Lotus Labs. (2023, December 13). Routers Roasting On An Open Firewall: The KV-Botnet Investigation. Retrieved June 10, 2024.](https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/)
- [Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
- [Conteras, T., Splunk Research Team. (2025, September 25). From Prompt to Payload: LAMEHUG’s LLM-Driven Cyber Intrusion. Retrieved April 21, 2026.](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
- [Google Threat Intelligence Group. (2025, November 5). GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools. Retrieved March 31, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
- [Proofpoint Threat Research and Team Cymru S2 Threat Research. (2024, April 4). Latrodectus: This Spider Bytes Like Ice . Retrieved May 31, 2024.](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
- [Stepanic, D. and Bousseaden, S. (2024, May 15). Spring Cleaning with LATRODECTUS: A Potential Replacement for ICEDID. Retrieved September 13, 2024.](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
- [Batista, J. (2024, June 17). Latrodectus, are you coming back?. Retrieved September 13, 2024.](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved November 17, 2024.](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)
- [Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)
- [Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
- [Saini, A. and Hossein, J. (2022, January 27). North Korea’s Lazarus APT leverages Windows Update client, GitHub in latest campaign. Retrieved January 27, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [CISA et al. (2024, July 8). People’s Republic of China (PRC) Ministry of State Security APT40 Tradecraft in Action. Retrieved February 3, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a)
- [Faou, M. (2019, May). Turla LightNeuron: One email away from remote code execution. Retrieved June 24, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
- [Stuart Ashenbrenner, Alden Schmidt. (2024, April 25). LightSpy Malware Variant Targeting macOS. Retrieved January 3, 2025.](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
- [Cisco Talos. (2024, April 24). ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices. Retrieved January 6, 2025.](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
- [Zhou, R. (2012, May 15). Backdoor.Linfo. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
- [Lin, M. et al. (2024, February 27). Cutting Edge, Part 3: Investigating Ivanti Connect Secure VPN Exploitation and Persistence Attempts. Retrieved March 1, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [Bourhis, P., Sekoia TDR. (2024, February 1). Unveiling the intricacies of DiceLoader. Retrieved May 14, 2025.](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
- [FBI. (2022, February 4). Indicators of Compromise Associated with LockBit 2.0 Ransomware. Retrieved January 24, 2025.](https://www.ic3.gov/CSA/2022/220204.pdf)
- [Elsad, A. et al. (2022, June 9). LockBit 2.0: How This RaaS Operates and How to Protect Against It. Retrieved January 24, 2025.](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part II. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
- [ITOCHU. (2024, January 24). The Endless Struggle Against APT10: Insights from LODEINFO v0.6.6 - v0.7.3 Analysis. Retrieved April 17, 2026.](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
- [Kazem, M. (2019, November 25). Trojan:W32/Lokibot. Retrieved May 15, 2020.](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)
- [Malik, M. (2019, June 20). LoudMiner: Cross-platform mining in cracked VST software. Retrieved May 18, 2020.](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)
- [Hsu, K. et al. (2020, June 24). Lucifer: New Cryptojacking and DDoS Hybrid Malware Exploiting High and Critical Vulnerabilities to Infect Windows Devices. Retrieved November 16, 2020.](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
- [Cybereaon Security Services Team. (n.d.). Your Data Is Under New Lummanagement: The Rise of LummaStealer. Retrieved March 22, 2025.](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)
- [Cara Lin, Fortinet. (2024, January 8). Deceptive Cracked Software Spreads Lumma Variant on YouTube. Retrieved March 22, 2025.](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)
- [Buddy Tancio, Fe Cureg, and Jovit Samaniego, Trend Micro. (2025, January 30). Lumma Stealer’s GitHub-Based Delivery Explored via Managed Detection and Response. Retrieved March 22, 2025.](https://www.trendmicro.com/en_us/research/25/a/lumma-stealers-github-based-delivery-via-mdr.html)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Phil Stokes. (2021, January 11). FADE DEAD | Adventures in Reversing Malicious Run-Only AppleScripts. Retrieved September 29, 2022.](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [Lee, B. and Falcone, R. (2017, February 15). Magic Hound Campaign Attacks Saudi Targets. Retrieved December 27, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)
- [DFIR Report. (2022, March 21). APT35 Automates Initial Access Using ProxyShell. Retrieved May 25, 2022.](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [Asheer Malhotra, Vitor Ventura & Jungsoo An, Cisco Talos. (2022, September 7). MagicRAT: Lazarus’ latest gateway into victim networks. Retrieved December 30, 2024.](https://blog.talosintelligence.com/lazarus-magicrat/)
- [SCILabs. (2021, December 23). Cyber Threat Profile Malteiro. Retrieved March 13, 2024.](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
- [Asheer Malhotra & Vitor Ventura. (2022, August 2). Manjusaka: A Chinese sibling of Sliver and Cobalt Strike. Retrieved September 4, 2024.](https://blog.talosintelligence.com/manjusaka-offensive-framework/)
- [GReAT. (2021, June 16). Ferocious Kitten: 6 Years of Covert Surveillance in Iran. Retrieved September 22, 2021.](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
- [Mundo, A. (2020, March 26). Ransomware Maze. Retrieved May 18, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Sierra, E., Iglesias, G.. (2018, April 24). Metamorfo Campaigns Targeting Brazilian Users. Retrieved July 30, 2020.](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
- [Zhang, X. (2020, February 4). Another Metamorfo Variant Targeting Customers of Financial Institutions in More Countries. Retrieved July 30, 2020.](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
- [ESET Research. (2019, October 3). Casbaneiro: peculiarities of this banking Trojan that affects Brazil and Mexico. Retrieved September 23, 2021.](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
- [Check Point Research Team. (2021, August 14). Indra - Hackers Behind Recent Attacks on Iran. Retrieved February 17, 2022.](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
- [Rascagneres, P., Mercer, W. (2017, June 19). Delphi Used To Score Against Palestine. Retrieved November 13, 2018.](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)
- [Tsarfaty, Y. (2018, July 25). Micropsia Malware. Retrieved November 13, 2018.](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
- [ClearSky Cyber Security . (2021, August). New Iranian Espionage Campaign By “Siamesekitten” - Lyceum. Retrieved June 6, 2022.](https://www.clearskysec.com/siamesekitten/)
- [Accenture. (2021, November 9). Who are latest targets of cyber group Lyceum?. Retrieved June 16, 2022.](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)
- [Rosenberg, J. (2018, June 14). MirageFox: APT15 Resurfaces With New Tools Based On Old Ones. Retrieved September 21, 2018.](https://web.archive.org/web/20180615122133/https://www.intezer.com/miragefox-apt15-resurfaces-with-new-tools-based-on-old-ones/)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [ESET Security. (2019, November 19). Mispadu: Advertisement for a discounted Unhappy Meal. Retrieved March 13, 2024.](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
- [Falcone, R. and Miller-Osborn, J.. (2016, January 24). Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists. Retrieved February 10, 2016.](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [Microsoft Threat Intelligence. (2024, May 28). Moonstone Sleet emerges as new North Korean threat actor with new bag of tricks. Retrieved August 26, 2024.](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)
- [Miller-Osborn, J. and Grunzweig, J.. (2017, March 30). Trochilus and New MoonWind RATs Used In Attack Against Thai Organizations. Retrieved March 30, 2017.](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
- [Svajcer, V. (2018, July 31). Multiple Cobalt Personality Disorder. Retrieved September 5, 2018.](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)
- [Villadsen, O.. (2019, August 29). More_eggs, Anyone? Threat Actor ITG08 Strikes Again. Retrieved September 16, 2019.](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)
- [Checkpoint Research. (2021, November 15). Uncovering MosesStaff techniques: Ideology over Money. Retrieved August 11, 2022.](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 10). MuddyWater expands operations. Retrieved November 2, 2018.](https://securelist.com/muddywater/88059/)
- [Adamitis, D. et al. (2019, May 20). Recent MuddyWater-associated BlackWater campaign shows signs of new anti-detection techniques. Retrieved June 5, 2019.](https://blog.talosintelligence.com/2019/05/recent-muddywater-associated-blackwater.html)
- [Reaqta. (2017, November 22). A dive into MuddyWater APT targeting Middle-East. Retrieved May 18, 2020.](https://reaqta.com/2017/11/muddywater-apt-targeting-middle-east/)
- [Peretz, A. and Theck, E. (2021, March 5). Earth Vetala – MuddyWater Continues to Target Organizations in the Middle East. Retrieved March 18, 2021.](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
- [Malhortra, A and Ventura, V. (2022, January 31). Iranian APT MuddyWater targets Turkish users via malicious PDFs, executables. Retrieved June 22, 2022.](https://blog.talosintelligence.com/2022/01/iranian-apt-muddywater-targets-turkey.html)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [Hamzeloofard, S. (2020, January 31). New wave of PlugX targets Hong Kong | Avira Blog. Retrieved April 13, 2021.](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)
- [Microsoft. (2022, May 9). Ransomware as a service: Understanding the cybercrime gig economy and how to protect yourself. Retrieved March 10, 2023.](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)
- [Neville, A. (2012, June 15). Trojan.Naid. Retrieved February 22, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-061518-4639-99)
- [Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
- [Mercer, W., Rascagneres, P. (2018, May 31). NavRAT Uses US-North Korea Summit As Decoy For Attacks In South Korea. Retrieved June 11, 2018.](https://blog.talosintelligence.com/2018/05/navrat.html)
- [Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
- [Victor, K.. (2020, May 18). Netwalker Fileless Ransomware Injected via Reflective Loading . Retrieved May 26, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
- [McAfee. (2015, March 2). Netwire RAT Behind Recent Targeted Attacks. Retrieved February 15, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/netwire-rat-behind-recent-targeted-attacks/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [Fidelis Cybersecurity. (2013, June 28). Fidelis Threat Advisory #1009: "njRAT" Uncovered. Retrieved June 4, 2019.](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
- [KASPERSKY GERT. (2023, December 14). Unveiling NKAbuse: a new multiplatform threat abusing the NKN protocol. Retrieved February 8, 2024.](https://securelist.com/unveiling-nkabuse/111512/)
- [Grunzweig, J., Lee, B. (2018, September 27). New KONNI Malware attacking Eurasia and Southeast Asia. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
- [Malhotra, A. (2021, March 2). ObliqueRAT returns with new campaign using hijacked websites. Retrieved September 2, 2021.](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
- [Sherstobitoff, R., Malhotra, A. (2018, October 18). ‘Operation Oceansalt’ Attacks South Korea, U.S., and Canada With Source Code From Chinese Hacker Group. Retrieved November 30, 2018.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 15). Octopus-infested seas of Central Asia. Retrieved November 14, 2018.](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
- [Hromcova, Z. and Burgher, A. (2023, December 14). OilRig’s persistent attacks using cloud service-powered downloaders. Retrieved November 26, 2024.](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
- [Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
- [Grunzweig, J. and Falcone, R.. (2016, October 4). OilRig Malware Campaign Updates Toolset and Expands Targets. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/)
- [Bromiley, M., et al.. (2019, July 18). Hard Pass: Declining APT34’s Invite to Join Their Professional Network. Retrieved August 26, 2019.](https://www.fireeye.com/blog/threat-research/2019/07/hard-pass-declining-apt34-invite-to-join-their-professional-network.html)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [Symantec Threat Hunter Team. (2023, October 19). Crambus: New Campaign Targets Middle Eastern Government. Retrieved November 27, 2024.](https://www.security.com/threat-intelligence/crambus-middle-east-government)
- [Hromcova, Z. (2019, July). OKRUM AND KETRICAN: AN OVERVIEW OF RECENT KE3CHANG GROUP ACTIVITY. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
- [Falcone, R., et al. (2018, September 04). OilRig Targets a Middle Eastern Government and Adds Evasion Techniques to OopsIE. Retrieved September 24, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)
- [Hiroaki, H. (2024, November 26). Guess Who’s Back - The Return of ANEL in the Recent Earth Kasha Spear-phishing Campaign in 2024. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-uncovers-operation-honeybee-malicious-document-campaign-targeting-humanitarian-aid-groups/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Carbon Black Threat Analysis Unit. (2019, February 12). New macOS Malware Variant of Shlayer (OSX) Discovered. Retrieved August 8, 2019.](https://blogs.vmware.com/security/2020/02/vmware-carbon-black-tau-threat-analysis-shlayer-macos.html)
- [Phil Stokes. (2020, September 8). Coming Out of Your Shell: From Shlayer to ZShlayer. Retrieved September 13, 2021.](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)
- [Horejsi, J. (2018, April 04). New MacOS Backdoor Linked to OceanLotus Found. Retrieved November 13, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-backdoor-linked-to-oceanlotus-found/)
- [Magisa, L. (2020, November 27). New MacOS Backdoor Connected to OceanLotus Surfaces. Retrieved December 2, 2020.](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)
- [Mullaney, C. & Honda, H. (2012, May 4). Trojan.Pasam. Retrieved February 22, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)
- [Cymmetria. (2016). Unveiling Patchwork - The Copy-Paste APT. Retrieved November 17, 2024.](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)
- [Check Point. (2020, November 6). Ransomware Alert: Pay2Key. Retrieved January 4, 2021.](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)
- [Leonardo. (2020, May 29). MALWARE TECHNICAL INSIGHT TURLA “Penquin_x64”. Retrieved March 11, 2021.](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
- [Brett Stone-Gross & Nikolaos Pantazopoulos. (2023, May 24). Technical Analysis of Pikabot. Retrieved July 12, 2024.](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)
- [Daniel Stepanic & Salim Bitam. (2024, February 23). PIKABOT, I choose you!. Retrieved July 12, 2024.](https://www.elastic.co/security-labs/pikabot-i-choose-you)
- [F-Secure Labs. (2015, September 17). The Dukes: 7 years of Russian cyberespionage. Retrieved December 10, 2015.](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
- [Unit 42. (2022, June 13). GALLIUM Expands Targeting Across Telecommunications, Government and Finance Sectors With New PingPull Tool. Retrieved August 7, 2022.](https://unit42.paloaltonetworks.com/pingpull-gallium/)
- [Tartare, M. et al. (2020, May 21). No “Game over” for the Winnti Group. Retrieved August 24, 2020.](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
- [Grunzweig, J., et al. (2016, May 24). New Wekby Attacks Use DNS Requests As Command and Control Mechanism. Retrieved August 17, 2016.](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
- [Ash, B., et al. (2018, June 26). RANCOR: Targeted Attacks in South East Asia Using PLAINTEE and DDKONG Malware Families. Retrieved July 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
- [Trend Micro Research. (2023, July 21). Ransomware Spotlight: Play. Retrieved September 24, 2024.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Mercer, W, et al. (2020, April 16). PoetRAT: Python RAT uses COVID-19 lures to target Azerbaijan public and private sectors. Retrieved April 27, 2020.](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
- [hasherezade. (2016, April 11). No money, but Pony! From a mail to a trojan horse. Retrieved May 21, 2020.](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
- [Lancaster, T. (2018, November 5). Inception Attackers Target Europe with Year-old Office Vulnerability. Retrieved May 8, 2020.](https://unit42.paloaltonetworks.com/unit42-inception-attackers-target-europe-year-old-office-vulnerability/)
- [Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
- [Lunghi, D. and Horejsi, J.. (2019, June 10). MuddyWater Resurfaces, Uses Multi-Stage Backdoor POWERSTATS V3 and New Post-Exploitation Tools. Retrieved May 14, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
- [Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
- [Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
- [Asheer Malhotra, Jungsoo An, Kendall Mc. (2022, May 5). Mustang Panda deploys a new wave of malware targeting Europe. Retrieved August 4, 2025.](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Nick Dai, Vickie Su, Sunny Lu. (2022, November 18). Earth Preta Spear-Phishing Governments Worldwide. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
- [Gorelik, M.. (2019, June 10). SECURITY ALERT: FIN8 IS BACK IN BUSINESS, TARGETING THE HOSPITALITY INDUSTRY. Retrieved June 13, 2019.](http://blog.morphisec.com/security-alert-fin8-is-back)
- [Nicolas Verdier. (n.d.). Retrieved January 29, 2018.](https://github.com/n1nj4sec/pupy)
- [Dumont, R. (2022, June 13). Technical Analysis of PureCrypter: A Fully-Functional Loader Distributing Remote Access Trojans and Information Stealers. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
- [Check Point Research. (2025, March 10). Blind Eagle: …And Justice for All. Retrieved April 16, 2026.](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
- [CS. (2020, October 7). Duck Hunting with Falcon Complete: A Fowl Banking Trojan Evolves, Part 2. Retrieved September 27, 2021.](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)
- [Morrow, D. (2021, April 15). The rise of QakBot. Retrieved September 27, 2021.](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)
- [Group IB. (2020, September). LOCK LIKE A PRO. Retrieved November 17, 2024.](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
- [Trend Micro. (2025, October 23). Agenda Ransomware Deploys Linux Variant on Windows Systems Through Remote Management Tools and BYOVD Techniques. Retrieved March 26, 2026.](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)
- [MaxXor. (n.d.). QuasarRAT. Retrieved July 10, 2018.](https://github.com/quasar/QuasarRAT)
- [S2W TALON. (2022, June 16). Raccoon Stealer is Back with a New Version. Retrieved August 1, 2024.](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Alfano, V. et al. (2025, February 12). RansomHub Never Sleeps Episode 1: The evolution of modern ransomware. Retrieved March 17, 2025.](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
- [Patrick Schläpfer . (2024, April 10). Raspberry Robin Now Spreading Through Windows Script Files. Retrieved May 17, 2024.](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
- [Lei, C., et al. (2018, January 24). Lazarus Campaign Targeting Cryptocurrencies Reveals Remote Controller Tool, an Evolved RATANKBA, and More. Retrieved May 22, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)
- [Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
- [Global Threat Center, Intelligence Team. (2020, December). APT27 Turns to Ransomware. Retrieved November 12, 2021.](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
- [Grunzweig, J. and Miller-Osborn, J. (2017, November 10). New Malware with Ties to SunOrcal Discovered. Retrieved November 16, 2017.](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)
- [Group-IB. (2020, August). RedCurl: The Pentest You Didn’t Know About. Retrieved August 9, 2024.](https://www.group-ib.com/resources/research-hub/red-curl/)
- [Group-IB. (2021, November). RedCurl: The Awakening. Retrieved August 14, 2024.](https://www.group-ib.com/resources/research-hub/red-curl-2/)
- [Insikt Group. (2025, January 9). Chinese State-Sponsored RedDelta Targeted Taiwan, Mongolia, and Southeast Asia with Adapted PlugX Infection Chain. Retrieved January 14, 2025.](https://go.recordedfuture.com/hubfs/reports/cta-cn-2025-0109.pdf)
- [Accenture Security. (2018, April 23). Hogfish Redleaves Campaign. Retrieved July 2, 2018.](http://web.archive.org/web/20220810112638/https:/www.accenture.com/t20180423T055005Z_w_/se-en/_acnmedia/PDF-76/Accenture-Hogfish-Threat-Analysis.pdf)
- [George Glass. (2024, August 14). REDLINESTEALER Malware Driving the Initial Access Broker Market. Retrieved September 17, 2025.](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
- [Proofpoint Threat Insight Team, Jeremy H, Axel F. (2020, March 16). New Redline Password Stealer Malware. Retrieved September 17, 2025.](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
- [Splunk Threat Research Team. (2023, June 1). Do Not Cross The 'RedLine' Stealer: Detections and Analysis. Retrieved September 17, 2025.](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
- [Yair Herling. (2023, April 4). From ChatGPT to RedLine Stealer: The Dark Side of OpenAI and Google Bard. Retrieved September 17, 2025.](https://veriti.ai/blog/veriti-research/from-chatgpt-to-redline-stealer-the-dark-side-of-openai-and-google-bard/)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
- [Livelli, K, et al. (2018, November 12). Operation Shaheen. Retrieved May 1, 2019.](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
- [Mamedov, O, et al. (2019, July 3). Sodin ransomware exploits Windows vulnerability and processor architecture. Retrieved August 4, 2020.](https://securelist.com/sodin-ransomware/91473/)
- [Cylance. (2019, July 3). hreat Spotlight: Sodinokibi Ransomware. Retrieved August 4, 2020.](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
- [Secureworks . (2019, September 24). REvil: The GandCrab Connection. Retrieved August 4, 2020.](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
- [McAfee. (2019, October 2). McAfee ATR Analyzes Sodinokibi aka REvil Ransomware-as-a-Service – What The Code Tells Us. Retrieved August 4, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
- [Intel 471 Malware Intelligence team. (2020, March 31). REvil Ransomware-as-a-Service – An analysis of a ransomware affiliate operation. Retrieved August 4, 2020.](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
- [Group IB. (2020, May). Ransomware Uncovered: Attackers’ Latest Methods. Retrieved August 5, 2020.](https://www.group-ib.com/whitepapers/ransomware-uncovered.html)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [Knight, S.. (2020, April 16). VMware Carbon Black TAU Threat Analysis: The Evolution of Lazarus. Retrieved May 1, 2020.](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
- [Punsaen Boonyakarn, Shawn Chew, Logeswaran Nadarajan, Mathew Potaczek, Jakub Jozwiak, and Alex Marvi. (2024, June 18). Cloaked and Covert: Uncovering UNC3886 Espionage Operations. Retrieved September 24, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [Anomali Labs. (2019, March 15). Rocke Evolves Its Arsenal With a New Malware Family Written in Golang. Retrieved April 24, 2019.](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)
- [Falcone, R., et al. (2018, July 27). New Threat Actor Group DarkHydrus Targets Middle East Government. Retrieved August 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
- [Mercer, W., Rascagneres, P. (2017, April 03). Introducing ROKRAT. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)
- [Mercer, W., Rascagneres, P. (2017, November 28). ROKRAT Reloaded. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2017/11/ROKRAT-Reloaded.html)
- [GReAT. (2019, May 13). ScarCruft continues to evolve, introduces Bluetooth harvester. Retrieved June 4, 2019.](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)
- [Pantazopoulos, N.. (2018, November 8). RokRat Analysis. Retrieved May 21, 2020.](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
- [Cash, D., Grunzweig, J., Adair, S., Lancaster, T. (2021, August 25). North Korean BLUELIGHT Special: InkySquid Deploys RokRAT. Retrieved October 1, 2021.](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
- [Jazi, Hossein. (2021, January 6). Retrohunting APT37: North Korean APT used VBA self decode technique to inject RokRat. Retrieved March 22, 2022.](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
- [Alex Turing, Hui Wang. (2021, April 28). RotaJakiro: A long live secret backdoor with 0 VT detection. Retrieved June 14, 2023.](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
- [Cybereason Global SOC and Cybereason Security Research Teams. (2022, December 14). Royal Rumble: Analysis of Royal Ransomware. Retrieved March 30, 2023.](https://www.cybereason.com/blog/royal-ransomware-analysis)
- [Morales, N. et al. (2023, February 20). Royal Ransomware Expands Attacks by Targeting Linux ESXi Servers. Retrieved March 30, 2023.](https://www.trendmicro.com/en_us/research/23/b/royal-ransomware-expands-attacks-by-targeting-linux-esxi-servers.html)
- [Faou, M. and Boutin, J. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
- [Awasthi, P. (2026, January 8). Reborn in Rust: Muddy Water Evolves Tooling with RustyWater Implant. Retrieved March 19, 2026.](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [Hasherezade. (2021, April 6). A deep dive into Saint Bot, a new downloader. Retrieved June 9, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
- [Cherepanov, A.. (2017, July 4). Analysis of TeleBots’ cunning backdoor . Retrieved June 11, 2020.](https://www.welivesecurity.com/2017/07/04/analysis-of-telebots-cunning-backdoor/)
- [Scott W. Brady. (2020, October 15). United States vs. Yuriy Sergeyevich Andrienko et al.. Retrieved November 25, 2020.](https://www.justice.gov/opa/press-release/file/1328521/download)
- [Budaca, E., et al. (2021, August 25). FIN8 Threat Actor Goes Agile with New Sardonic Backdoor. Retrieved August 9, 2023.](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
- [Mandiant Incident Response. (2025, July 23). From Help Desk to Hypervisor: Defending Your VMware vSphere Estate from UNC3944. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)
- [Schwarz, D. and Proofpoint Staff. (2019, January 9). ServHelper and FlawedGrace - New malware introduced by TA505. Retrieved May 28, 2019.](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)
- [Kaspersky Lab. (2017, August). ShadowPad: popular server management software hit in supply chain attack. Retrieved March 22, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
- [Charlie Eriksen. (2025, September 16). S1ngularity/nx attackers strike again. Retrieved April 9, 2026.](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
- [Socket Research Team. (2025, November 24). Shai Hulud Strikes Again (v2). Retrieved April 9, 2026.](https://socket.dev/blog/shai-hulud-strikes-again-v2)
- [Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [Falcone, R. (2018, December 13). Shamoon 3 Targets Oil and Gas Organization. Retrieved March 14, 2019.](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
- [Microsoft Threat Intelligence. (2025, July 22). Disrupting active exploitation of on-premises SharePoint vulnerabilities. Retrieved October 15, 2025.](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/#storm-2603)
- [Ilascu, I. (2020, December 14). Hacking group’s new malware abuses Google and Facebook services. Retrieved December 28, 2020.](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Cristian Souza, Eduardo Ovalle, Ashley Muñoz, & Christopher Zachor. (2024, May 23). ShrinkLocker: Turning BitLocker into ransomware. Retrieved December 7, 2024.](https://securelist.com/ransomware-abuses-bitlocker/112643/)
- [Splunk Threat Research Team , Teoderick Contreras. (2024, September 5). ShrinkLocker Malware: Abusing BitLocker to Lock Your Data. Retrieved December 7, 2024.](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
- [Hegel, T. (2021, January 13). A Global Perspective of the SideWinder APT. Retrieved January 27, 2021.](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)
- [Rewterz. (2020, June 22). Analysis on Sidewinder APT Group – COVID-19. Retrieved January 29, 2021.](https://www.rewterz.com/articles/analysis-on-sidewinder-apt-group-covid-19)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [Remillano, A., Urbanec, J. (2019, September 19). Skidmap Linux Malware Uses Rootkit Capabilities to Hide Cryptocurrency-Mining Payload. Retrieved June 4, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [FireEye. (2021, June 16). Smoking Out a DARKSIDE Affiliate’s Supply Chain Software Compromise. Retrieved September 22, 2021.](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
- [Lorber, N. (2021, May 7). Revealing the Snip3 Crypter, a Highly Evasive RAT Loader. Retrieved September 13, 2023.](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
- [Andrew Northern. (2022, November 22). SocGholish, a very real threat from a very fake update. Retrieved February 13, 2024.](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
- [Red Canary. (2024, March). Red Canary 2024 Threat Detection Report: SocGholish. Retrieved March 22, 2024.](https://redcanary.com/threat-detection-report/threats/socgholish/)
- [Secureworks. (n.d.). GOLD PRELUDE . Retrieved March 22, 2024.](https://www.secureworks.com/research/threat-profiles/gold-prelude)
- [GREAT. (2021, March 30). APT10: sophisticated multi-layered loader Ecipekac discovered in A41APT campaign. Retrieved June 17, 2021.](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [CISA. (2020, July 16). MAR-10296782-1.v1 – SOREFANG. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
- [Symantec Security Response. (2017, November 7). Sowbug: Cyber espionage group targets South American and Southeast Asian governments. Retrieved November 16, 2017.](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)
- [Falcone, R., et al. (2020, March 3). Molerats Delivers Spark Backdoor to Government and Telecommunications Organizations. Retrieved December 14, 2020.](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)
- [Matt Lin, Austin Larsen, John Wolfram, Ashley Pearson, Josh Murchie, Lukasz Lamparski, Joseph Pisano, Ryan Hall, Ron Craft, Shawn Crew, Billy Wong, Tyler McLellan. (2024, April 4). Cutting Edge, Part 4: Ivanti Connect Secure VPN Post-Exploitation Lateral Movement Case Studies. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
- [Check Point Research. (2019, February 4). SpeakUp: A New Undetected Backdoor Linux Trojan. Retrieved April 17, 2019.](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
- [CTU. (2018, September 27). Cybercriminals Increasingly Trying to Ensnare the Big Financial Fish. Retrieved September 20, 2021.](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: PAKLOG, CorKLOG, and SplatCloak | P2. Retrieved September 12, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
- [Kumar, A., Stone-Gross, Brett. (2021, September 28). Squirrelwaffle: New Loader Delivering Cobalt Strike. Retrieved August 9, 2022.](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
- [Baumgartner, K., Golovkin, M.. (2015, May). The MsnMM Campaigns: The Earliest Naikon APT Campaigns. Retrieved April 10, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
- [Tomcik, R. et al. (2022, February 24). Left On Read: Telegram Malware Spotted in Latest Iranian Cyber Espionage Activity. Retrieved August 18, 2022.](https://www.mandiant.com/resources/telegram-malware-iranian-espionage)
- [FBI, CISA, CNMF, NCSC-UK. (2022, February 24). Iranian Government-Sponsored Actors Conduct Cyber Operations Against Global Government and Commercial Networks. Retrieved September 27, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
- [Cybereason Global SOC Team. (n.d.). THREAT ANALYSIS REPORT: Inside the LockBit Arsenal - The StealBit Exfiltration Tool. Retrieved January 29, 2025.](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
- [Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.](https://citizenlab.org/2016/05/stealth-falcon/)
- [Kaspersky Lab. (2017, March 7). From Shamoon to StoneDrill: Wipers attacking Saudi organizations and beyond. Retrieved March 14, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
- [Microsoft Threat Intelligence. (2024, September 26). Storm-0501: Ransomware attacks expanding to hybrid cloud environments. Retrieved October 19, 2025.](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)
- [Cylance SPEAR Team. (2017, February 9). Shell Crew Variants Continue to Fly Under Big AV’s Radar. Retrieved February 15, 2017.](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)
- [Golo Mühr, Joe Fasulo & Charlotte Hammond, IBM X-Force. (2024, November 12). Strela Stealer: Today’s invoice is tomorrow’s phish. Retrieved December 31, 2024.](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
- [Cybereason Nocturnus. (2022, February 1). StrifeWater RAT: Iranian APT Moses Staff Adds New Trojan to Ransomware Operations. Retrieved August 15, 2022.](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [MSTIC. (2020, December 18). Analyzing Solorigate, the compromised DLL file that started a sophisticated cyberattack, and how Microsoft Defender helps protect customers . Retrieved January 5, 2021.](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [Ivanov, A. et al. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
- [Gallagher, S., Gn, S. (2020, December 16). Ransomware operators use SystemBC RAT as off-the-shelf Tor backdoor. Retrieved May 16, 2025.](https://news.sophos.com/en-us/2020/12/16/systembc/)
- [AhnLab. (2022, April 4). SystemBC Being Used by Various Attackers . Retrieved June 18, 2025.](https://asec.ahnlab.com/en/33600/)
- [Harmon, K., et al. (2019, August 1). SystemBC is like Christmas in July for SOCKS5 Malware and Exploit Kits . Retrieved June 13, 2025.](https://www.proofpoint.com/us/threat-insight/post/systembc-christmas-july-socks5-malware-and-exploit-kits)
- [Microsoft. (n.d.). Systeminfo. Retrieved April 8, 2016.](https://technet.microsoft.com/en-us/library/bb491007.aspx)
- [Lunghi, D. and Lu, K. (2021, April 9). Iron Tiger APT Updates Toolkit With Evolved SysUpdate Malware. Retrieved November 12, 2021.](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
- [Daniel Lunghi. (2023, March 1). Iron Tiger’s SysUpdate Reappears, Adds Linux Targeting. Retrieved March 20, 2023.](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
- [Grunzweig, J. and Miller-Osborn, J.. (2016, February 4). T9000: Advanced Modular Backdoor Uses Complex Anti-Analysis Techniques. Retrieved April 15, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
- [Larson, S. and Wise, J. (2022, February 15). Charting TA2541's Flight. Retrieved September 12, 2023.](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [AT&T Alien Labs. (2021, September 8). TeamTNT with new campaign aka Chimaera. Retrieved September 22, 2021.](https://cybersecurity.att.com/blogs/labs-research/teamtnt-with-new-campaign-aka-chimaera)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle. Retrieved October 27, 2021.](https://securelist.com/lazarus-threatneedle/100803/)
- [Nathaniel Morales, Nick Dai. (2025, February 18). Earth Preta Mixes Legitimate and Malicious Components to Sidestep Detection. Retrieved September 10, 2025.](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: ToneShell and StarProxy | P1. Retrieved July 21, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
- [Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
- [Reaves, J. (2016, October 15). TrickBot: We Missed you, Dyre. Retrieved August 2, 2018.](https://www.fidelissecurity.com/threatgeek/2016/10/trickbot-we-missed-you-dyre)
- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [Eclypsium, Advanced Intelligence. (2020, December 1). TRICKBOT NOW OFFERS ‘TRICKBOOT’: PERSIST, BRICK, PROFIT. Retrieved March 15, 2021.](https://eclypsium.com/wp-content/uploads/2020/12/TrickBot-Now-Offers-TrickBoot-Persist-Brick-Profit.pdf)
- [Secureworks. (2019, July 24). Updated Karagany Malware Targets Energy Sector. Retrieved August 12, 2020.](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
- [Jiho Kim & Sebin Lee, S2W. (2024, February 7). Kimsuky disguised as a Korean company signed with a valid certificate to distribute Troll Stealer (English ver.). Retrieved January 17, 2025.](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
- [Alintanahin, K. (2015). Operation Tropic Trooper: Relying on Tried-and-Tested Flaws to Infiltrate Secret Keepers. Retrieved June 14, 2019.](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Ubiedo, L. (2025, November 20). Blockchain and Node.js abused by Tsundere: an emerging botnet. Retrieved April 6, 2026.](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)
- [Adam Burgher. (2021, June 10). BackdoorDiplomacy: Upgrading from Quarian to Turian. Retrieved September 1, 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [O'Leary, J., et al. (2017, September 20). Insights into Iranian Cyber Espionage: APT33 Targets Aerospace and Energy Sectors and has Ties to Destructive Malware. Retrieved February 15, 2018.](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Matsuda, A., Muhammad I. (2018, September 13). APT10 Targeting Japanese Corporations Using Updated TTPs. Retrieved September 17, 2018.](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Caragay, R. (2015, March 26). URSNIF: The Multifaceted Malware. Retrieved June 5, 2019.](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
- [Salem, E. et al. (2020, May 28). VALAK: MORE THAN MEETS THE EYE . Retrieved June 19, 2020.](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
- [Reaves, J. and Platt, J. (2020, June). Valak Malware and the Connection to Gozi Loader ConfCrew. Retrieved August 31, 2020.](https://assets.sentinelone.com/labs/sentinel-one-valak-i)
- [Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
- [FBI. (2026, March 20). FBI Flash: FLASH-20260320-001:Government of Iran Cyber Actors Deploy Telegram C2 to Push Malware to Identified Targets. Retrieved April 20, 2026.](https://www.ic3.gov/CSA/2026/260320.pdf)
- [US-CERT. (2017, November 22). Alert (TA17-318B): HIDDEN COBRA – North Korean Trojan: Volgmer. Retrieved December 7, 2017.](https://www.us-cert.gov/ncas/alerts/TA17-318B)
- [US-CERT. (2017, November 01). Malware Analysis Report (MAR) - 10135536-D. Retrieved July 16, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)
- [Yagi, J. (2014, August 24). Trojan.Volgmer. Retrieved July 16, 2018.](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [PWC. (2020, July 16). How WellMess malware has been used to target COVID-19 vaccines. Retrieved September 24, 2020.](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)
- [CISA. (2020, July 16). MAR-10296782-2.v1 – WELLMESS. Retrieved September 24, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)
- [The BlackBerry Research & Intelligence Team. (2020, October). BAHAMUT: Hack-for-Hire Masters of Phishing, Fake News, and Fake Apps. Retrieved February 8, 2021.](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)
- [Anthe, C. et al. (2016, December 14). Microsoft Security Intelligence Report Volume 21. Retrieved November 27, 2017.](http://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_English.pdf)
- [Novetta Threat Research Group. (2015, April 7). Winnti Analysis. Retrieved February 8, 2017.](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
- [Chad Anderson. (2021, April 27). Winter Vivern: A Look At Re-Crafted Government MalDocs Targeting Multiple Languages. Retrieved July 29, 2024.](https://www.domaintools.com/resources/blog/winter-vivern-a-look-at-re-crafted-government-maldocs/)
- [The DFIR Report. (2020, October 8). Ryuk’s Return. Retrieved October 9, 2020.](https://thedfirreport.com/2020/10/08/ryuks-return/)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Robert Falcone. (2017, February 14). XAgentOSX: Sofacy's Xagent macOS Tool. Retrieved July 12, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)
- [Mac Threat Response, Mobile Research Team. (2020, August 13). The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSS Backdoor Planting in Safari, and Leverages Two Zero-day Exploits. Retrieved October 5, 2021.](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
- [Acronis. (2021, November 26). Trojan-as-a-service: From Formbook to XLoader. Retrieved March 11, 2025.](https://www.acronis.com/en-us/cyber-protection-center/posts/trojan-as-a-service-from-formbook-to-xloader/)
- [Kirill Boychenko. (2025, July 14). Contagious Interview Campaign Escalates With 67 Malicious npm Packages and New Malware Loader. Retrieved October 19, 2025.](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
- [Schwarz, D., Sopko J. (2018, March 08). Donot Team Leverages New Modular Malware Framework in South Asia. Retrieved June 11, 2018.](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
- [Lee, B., Falcone, R. (2018, June 06). Sofacy Group’s Parallel Attacks. Retrieved June 18, 2018.](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)
- [ESET. (2018, November 20). Sednit: What’s going on with Zebrocy?. Retrieved February 12, 2019.](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
- [ESET Research. (2019, May 22). A journey to Zebrocy land. Retrieved June 20, 2019.](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
- [Accenture Security. (2018, November 29). SNAKEMACKEREL. Retrieved April 15, 2019.](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
- [CISA. (2020, October 29). Malware Analysis Report (AR20-303B). Retrieved December 9, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
- [Huss, D., et al. (2017, February 2). Oops, they did it again: APT Targets Russia and Belarus with ZeroT and PlugX. Retrieved April 5, 2018.](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)
- [Brumaghin, E., et al. (2017, November 02). Poisoning the Well: Banking Trojan Targets Google Search Results. Retrieved November 5, 2018.](https://blog.talosintelligence.com/2017/11/zeus-panda-campaign.html#More)
- [Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
- [Singh, S. and Antil, S. (2020, October 27). APT-31 Leverages COVID-19 Vaccine Theme and Abuses Legitimate Online Services. Retrieved March 24, 2021.](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)
- [McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)
- [Raghuprasad, C . (2022, May 11). Bitter APT adds Bangladesh to their targets. Retrieved June 1, 2022.](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[FIN7]] [related_actor:: [[FIN7]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[RansomHub]] [related_actor:: [[RansomHub]]]

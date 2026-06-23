# Data from Local System

## Description

Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration.

Adversaries may do this using a Command and Scripting Interpreter , such as cmd as well as a Network Device CLI , which have functionality to interact with the file system to gather information. [1] Adversaries may also use Automated Collection on the local system.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1028 | Action RAT | Action RAT can collect local data from an infected machine. [2] |
| G1030 | Agrius | Agrius gathered data from database and other critical servers in victim environments, then used wiping mechanisms as an anti-analysis and anti-forensics mechanism. [3] |
| S1025 | Amadey | Amadey can collect information from a compromised host. [4] |
| G0138 | Andariel | Andariel has collected large numbers of files from compromised network systems for later extraction. [5] |
| C0062 | Anthropic AI-orchestrated Campaign | During the Anthropic AI-orchestrated Campaign , the adversary tasked Claude Code to automatically gather sensitive data stored within the local system to include credentials, system configurations and sensitive operational data. [6] |
| S0622 | AppleSeed | AppleSeed can collect data on a compromised host. [7] [8] |
| G0006 | APT1 | APT1 has collected files from a local victim. [9] |
| G0007 | APT28 | APT28 has retrieved internal documents from machines inside victim environments, including by using Forfiles to stage documents before exfiltration. [10] [11] [12] [13] |
| G0016 | APT29 | APT29 has stolen data from compromised hosts. [14] |
| G0022 | APT3 | APT3 will identify Microsoft Office documents on the victim's computer. [15] |
| G0067 | APT37 | APT37 has collected data from victims' local systems. [16] |
| G0082 | APT38 | APT38 has collected data from a compromised host. [17] |
| G0087 | APT39 | APT39 has used various tools to steal files from the compromised host. [18] [19] |
| G0096 | APT41 | APT41 has uploaded files and data from a compromised host. [20] |
| G0143 | Aquatic Panda | Aquatic Panda captured local Windows security event log data from victim machines using the wevtutil utility to extract contents to an evtx output file. [21] |
| S1029 | AuTo Stealer | AuTo Stealer can collect data such as PowerPoint files, Word documents, Excel files, PDF files, text files, database files, and image files from an infected machine. [2] |
| G0001 | Axiom | Axiom has collected data from a compromised network. [22] |
| S0642 | BADFLICK | BADFLICK has uploaded files from victims' machines. [23] |
| S0128 | BADNEWS | When it first starts, BADNEWS crawls the victim's local drives and collects documents with the following extensions: .doc, .docx, .pdf, .ppt, .pptx, and .txt. [24] [25] |
| S0337 | BadPatch | BadPatch collects files from the local system that have the following extensions, then prepares them for exfiltration: .xls, .xlsx, .pdf, .mdb, .rar, .zip, .doc, .docx. [26] |
| S0234 | Bandook | Bandook can collect local files from the system . [27] |
| S0239 | Bankshot | Bankshot collects files from the local system. [28] |
| S0534 | Bazar | Bazar can retrieve information from the infected machine. [29] |
| S1246 | BeaverTail | BeaverTail has exfiltrated data collected from local systems. [30] [31] [32] [33] |
| S0268 | Bisonal | Bisonal has collected information from a compromised host. [34] |
| S0564 | BlackMould | BlackMould can copy files on a compromised host. [35] |
| S0520 | BLINDINGCAN | BLINDINGCAN has uploaded files from victim machines. [36] |
| S0651 | BoxCaon | BoxCaon can upload files from a compromised host. [37] |
| S9015 | BRICKSTORM | BRICKSTORM has commands that allow the actor download files from the compromised host to the C2 server, and to also download specific sections of a file. [38] |
| G0060 | BRONZE BUTLER | BRONZE BUTLER has exfiltrated files stolen from local systems. [39] |
| S1063 | Brute Ratel C4 | Brute Ratel C4 has the ability to upload files from a compromised system. [40] |
| S1039 | Bumblebee | Bumblebee can capture and compress stolen credentials from the Registry and volume shadow copies. [41] |
| C0015 | C0015 | During C0015 , the threat actors obtained files and data from the compromised network. [42] |
| C0017 | C0017 | During C0017 , APT41 collected information related to compromised machines as well as Personal Identifiable Information (PII) from victim networks. [43] |
| C0026 | C0026 | During C0026 , the threat actors collected documents from compromised hosts. [44] |
| S0274 | Calisto | Calisto can collect data from user directories. [45] |
| S1224 | CASTLETAP | CASTLETAP can execute a C2 command to transfer files from victim machines. [46] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell has a module to collect information from the local database. [47] |
| S1043 | ccf32 | ccf32 can collect files from a compromised host. [48] |
| S0674 | CharmPower | CharmPower can collect data and files from a compromised host. [49] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP can collect files from compromised hosts. [50] |
| S0020 | China Chopper | China Chopper 's server component can upload local files. [51] [52] [53] [54] |
| S0667 | Chrommme | Chrommme can collect data from a local system. [55] |
| S0660 | Clambling | Clambling can collect information from a compromised host. [56] |
| S0154 | Cobalt Strike | Cobalt Strike can collect data from a local system. [57] [58] |
| S0492 | CookieMiner | CookieMiner has retrieved iPhone text messages from iTunes phone backup files. [59] |
| S0050 | CosmicDuke | CosmicDuke steals user files from local hard drives with file extensions that match a predefined list. [60] |
| C0004 | CostaRicto | During CostaRicto , the threat actors collected data and files from compromised networks. [61] |
| S1023 | CreepyDrive | CreepyDrive can upload files to C2 from victim machines. [62] |
| S0115 | Crimson | Crimson can collect information from a compromised host. [63] |
| S0538 | Crutch | Crutch can exfiltrate files from compromised systems. [64] |
| S0498 | Cryptoistic | Cryptoistic can retrieve files from the local file system. [65] |
| G1012 | CURIUM | CURIUM has exfiltrated data from a compromised machine. [66] |
| C0029 | Cutting Edge | During Cutting Edge , threat actors stole the running configuration and cache data from targeted Ivanti Connect Secure VPNs. [67] [68] |
| S0687 | Cyclops Blink | Cyclops Blink can upload files from a compromised host. [69] |
| S1014 | DanBot | DanBot can upload files from compromised hosts. [70] |
| G0070 | Dark Caracal | Dark Caracal collected complete contents of the 'Pictures' folder from compromised Windows systems. [71] |
| S1111 | DarkGate | DarkGate has stolen sitemanager.xml and recentservers.xml from %APPDATA%\FileZilla\ if present. [72] |
| S0673 | DarkWatchman | DarkWatchman can collect files from a compromised host. [73] |
| S1021 | DnsSystem | DnsSystem can upload files from infected machines after receiving a command with uploaddd in the string. [74] |
| G0035 | Dragonfly | Dragonfly has collected data from local victim systems. [75] |
| S0694 | DRATzarus | DRATzarus can collect information from a compromised host. [76] |
| S0502 | Drovorub | Drovorub can transfer files from the victim machine. [77] |
| S0567 | Dtrack | Dtrack can collect a variety of information from victim machines. [78] |
| S1159 | DUSTTRAP | DUSTTRAP can gather data from infected systems. [79] |
| G1003 | Ember Bear | Ember Bear gathers victim system information such as enumerating the volume of a given device or extracting system and security event logs for analysis. [80] [81] |
| S0634 | EnvyScout | EnvyScout can collect sensitive NTLM material from a compromised host. [82] |
| S0404 | esentutl | esentutl can be used to collect data from local file systems. [83] |
| S0512 | FatDuke | FatDuke can copy files and directories from a compromised host. [84] |
| G1016 | FIN13 | FIN13 has gathered stolen credentials, sensitive data such as point-of-sale (POS), and ATM data from a compromised network before exfiltration. [85] [86] |
| G0037 | FIN6 | FIN6 has collected and exfiltrated payment card data from compromised systems. [87] [88] [89] |
| G0046 | FIN7 | FIN7 has collected files and other sensitive information from a compromised network. [90] |
| S0696 | Flagpro | Flagpro can collect data from a compromised host, including Windows authentication information. [91] |
| S0036 | FLASHFLOOD | FLASHFLOOD searches for interesting files (either a default or customized set of file extensions) on the local system. FLASHFLOOD will scan the My Recent Documents, Desktop, Temporary Internet Files, and TEMP directories. FLASHFLOOD also collects information stored in the Windows Address Book. [92] |
| S0381 | FlawedAmmyy | FlawedAmmyy has collected information and files from a compromised machine. [93] |
| S0661 | FoggyWeb | FoggyWeb can retrieve configuration data from a compromised AD FS server. [94] |
| S0193 | Forfiles | Forfiles can be used to act on (ex: copy, move, etc.) files/directories in a system during (ex: copy files into a staging area before). [10] |
| G0117 | Fox Kitten | Fox Kitten has searched local system resources to access sensitive documents. [95] |
| S0503 | FrameworkPOS | FrameworkPOS can collect elements related to credit card data from process memory. [96] |
| C0001 | Frankenstein | During Frankenstein , the threat actors used Empire to gather various local system information. [97] |
| S1044 | FunnyDream | FunnyDream can upload files from victims' machines. [48] [98] |
| G0093 | GALLIUM | GALLIUM collected data from the victim's local system, including password hashes from the SAM hive in the Registry. [99] |
| G0047 | Gamaredon Group | Gamaredon Group has collected files from infected systems and uploaded them to a C2 server. [100] [101] |
| S0666 | Gelsemium | Gelsemium can collect data from a compromised host. [55] |
| S9010 | GlassWorm | GlassWorm has collected local data from a compromised host to include desktop cryptocurrency wallet data, and documents from within Desktop, Documents, and Downloads. [102] |
| S0477 | Goopy | Goopy has the ability to exfiltrate documents from infected systems. [103] |
| S0237 | GravityRAT | GravityRAT steals files with the following extensions: .docx, .doc, .pptx, .ppt, .xlsx, .xls, .rtf, and .pdf. [104] |
| S0690 | Green Lambert | Green Lambert can collect data from a compromised host. [105] |
| S0632 | GrimAgent | GrimAgent can collect data and files from a compromised host. [106] |
| G0125 | HAFNIUM | HAFNIUM has collected data and files from a compromised machine. [54] [107] |
| S1229 | Havoc | Havoc can download files from the victim's computer. [108] [109] |
| S9023 | HiddenFace | HiddenFace can upload files from the victim machine to C2 nodes. [110] [111] |
| S0009 | Hikit | Hikit can upload files from compromised machines. [22] |
| S0203 | Hydraq | Hydraq creates a backdoor through which remote attackers can read data from files. [112] [113] |
| S1022 | IceApple | IceApple can collect files, passwords, and other data from a compromised host. [114] |
| G0100 | Inception | Inception used a file hunting plugin to collect .txt, .pdf, .xls or .doc files from the infected host. [115] |
| S1245 | InvisibleFerret | InvisibleFerret has collected data utilizing a script that contained a list of excluded files and directory names and naming patterns of interest such as environment and configuration files, documents, spreadsheets, and other files that contained the words secret, wallet, private, and password. [31] |
| S0260 | InvisiMole | InvisiMole can collect data from the system, and can monitor changes in specified directories. [116] |
| S1132 | IPsec Helper | IPsec Helper can identify specific files and folders for follow-on exfiltration. [117] |
| S0015 | Ixeshe | Ixeshe can collect data from a local system. [118] |
| S0265 | Kazuar | Kazuar uploads files from a specified directory to the C2 server. [119] |
| G0004 | Ke3chang | Ke3chang gathered information and files from local directories for exfiltration. [120] [121] |
| S1020 | Kevin | Kevin can upload logs and other data from a compromised host. [122] |
| S0526 | KGH_SPY | KGH_SPY can send a file containing victim system information to C2. [123] |
| G0094 | Kimsuky | Kimsuky has collected Office, PDF, and HWP documents from its victims. [124] [125] Kimsuky has also harvested victim files through the use of the RecentFiles() function that collects paths of recently accessed files by parsing .lnk shortcuts from %APPDATA%\Microsoft\Windows\Recent . [126] |
| S0250 | Koadic | Koadic can download files off the target system to send back to the server. [127] [128] |
| S0356 | KONNI | KONNI has stored collected information and discovered processes in a tmp file. [129] |
| S1075 | KOPILUWAK | KOPILUWAK can gather information from compromised hosts. [44] |
| S9035 | LAMEHUG | LAMEHUG has the ability to collect system information and files of interest from compromised systems. [130] [131] |
| G1004 | LAPSUS$ | LAPSUS$ uploaded sensitive files, information, and credentials from a targeted organization for extortion or public release. [132] |
| S1160 | Latrodectus | Latrodectus can collect data from a compromised host using a stealer module. [133] |
| G0032 | Lazarus Group | Lazarus Group has collected data and files from compromised networks. [134] [135] [136] [137] |
| S0395 | LightNeuron | LightNeuron can collect files from a local system. [138] |
| S0211 | Linfo | Linfo creates a backdoor through which remote attackers can obtain data from local systems. [139] |
| S9020 | LODEINFO | LODEINFO can upload files from infected hosts to the C2. [140] [141] [142] |
| S1101 | LoFiSe | LoFiSe can collect files of interest from targeted systems. [143] |
| G1014 | LuminousMoth | LuminousMoth has collected files and data from compromised machines. [144] [145] |
| S0409 | Machete | Machete searches the File system for files of interest. [146] |
| S1016 | MacMa | MacMa can collect then exfiltrate files from the compromised system. [147] |
| S1060 | Mafalda | Mafalda can collect files and information from a compromised host. [148] |
| G0059 | Magic Hound | Magic Hound has used a web shell to exfiltrate a ZIP file containing a dump of LSASS memory on a compromised machine. [149] [150] |
| S0652 | MarkiRAT | MarkiRAT can upload data from the victim's machine to the C2 server. [151] |
| S0500 | MCMD | MCMD has the ability to upload files from an infected device. [152] |
| G0045 | menuPass | menuPass has collected various files from the compromised computers. [153] [154] |
| S1059 | metaMain | metaMain can collect files and system information from a compromised host. [148] [155] |
| S1146 | MgBot | MgBot includes modules for collecting files from local systems based on a given set of properties and filenames. [156] |
| S1015 | Milan | Milan can upload files from a compromised host. [157] |
| G1054 | MirrorFace | MirrorFace gathered data and files of interest from victim's systems. [110] |
| S0084 | Mis-Type | Mis-Type has collected files and data from a compromised host. [158] |
| S0083 | Misdat | Misdat has collected files and data from a compromised host. [158] |
| S0079 | MobileOrder | MobileOrder exfiltrates data collected from the victim mobile device. [159] |
| S1026 | Mongall | Mongall has the ability to upload files from victim's machines. [160] |
| S0630 | Nebulae | Nebulae has the capability to upload collected files to C2. [161] |
| S0691 | Neoichor | Neoichor can upload files from a victim's machine. [121] |
| C0002 | Night Dragon | During Night Dragon , the threat actors collected files and other data from compromised systems. [162] |
| S1090 | NightClub | NightClub can use a file monitor to steal specific files from targeted systems. [163] |
| S0385 | njRAT | njRAT can collect data from a local system. [164] |
| S1131 | NPPSPY | NPPSPY records data entered from the local system logon at Winlogon to capture credentials in cleartext. [165] |
| S0340 | Octopus | Octopus can exfiltrate files from the system using a documents collector tool. [166] |
| G0049 | OilRig | OilRig has used PowerShell to upload files from compromised systems. [167] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors collected data, files, and other information from compromised networks. [168] |
| C0022 | Operation Dream Job | During Operation Dream Job , Lazarus Group used malicious Trojans and DLL files to exfiltrate data from an infected host. [76] [169] |
| C0006 | Operation Honeybee | During Operation Honeybee , the threat actors collected data from compromised hosts. [170] |
| C0048 | Operation MidnightEclipse | During Operation MidnightEclipse , threat actors stole saved cookies and login data from targeted systems. [171] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors exfiltrated files and directories of interest from the targeted system. [172] |
| S0352 | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D has the ability to upload files from a compromised host. [173] |
| S0594 | Out1 | Out1 can copy files and Registry data from compromised hosts. [174] |
| S1017 | OutSteel | OutSteel can collect information from a compromised host. [175] |
| S0598 | P.A.S. Webshell | P.A.S. Webshell has the ability to copy files on a compromised host. [176] |
| S0208 | Pasam | Pasam creates a backdoor through which remote attackers can retrieve files. [177] |
| G0040 | Patchwork | Patchwork collected and exfiltrated files from the infected system. [178] |
| S1102 | Pcexter | Pcexter can upload files from targeted systems. [143] |
| S1050 | PcShare | PcShare can collect files and information from a compromised host. [48] |
| S0517 | Pillowmint | Pillowmint has collected credit card data using native API functions. [179] |
| S0048 | PinchDuke | PinchDuke collects user files from the compromised host based on predefined file extensions. [180] |
| S1031 | PingPull | PingPull can collect data from a compromised host. [181] |
| S0012 | PoisonIvy | PoisonIvy creates a backdoor through which remote attackers can steal system information. [182] |
| S1012 | PowerLess | PowerLess has the ability to exfiltrate data, including Chrome and Edge browser database files, from compromised machines. [183] |
| S0194 | PowerSploit | PowerSploit contains a collection of Exfiltration modules that can access data from local files, volumes, and processes. [184] [185] |
| S0223 | POWERSTATS | POWERSTATS can upload files from compromised hosts. [186] |
| S0238 | Proxysvc | Proxysvc searches the local system and gathers data. [187] |
| S0197 | PUNCHTRACK | PUNCHTRACK scrapes memory for properly formatted payment card data. [188] [189] |
| S0650 | QakBot | QakBot can use a variety of commands, including esentutl.exe to steal sensitive data from Internet Explorer and Microsoft Edge, to acquire information that is subsequently exfiltrated. [190] [191] |
| S0262 | QuasarRAT | QuasarRAT can retrieve files from compromised client machines. [192] |
| S0686 | QuietSieve | QuietSieve can collect files from a compromised host. [193] |
| S1148 | Raccoon Stealer | Raccoon Stealer collects data from victim machines based on configuration information received from command and control nodes. [194] [195] |
| S0629 | RainyDay | RainyDay can use a file exfiltration tool to collect recently changed files on a compromised host. [161] |
| S0458 | Ramsay | Ramsay can collect Microsoft Word documents from the target's file system, as well as .txt , .doc , and .xls files from the Internet Explorer cache. [196] [197] |
| S1113 | RAPIDPULSE | RAPIDPULSE retrieves files from the victim system via encrypted commands sent to the web shell. [198] |
| S0169 | RawPOS | RawPOS dumps memory from specific processes on a victim system, parses the dumped files, and scrapes them for credit card data. [199] [200] [201] |
| S0662 | RCSession | RCSession can collect data from a compromised host. [202] [56] |
| G1039 | RedCurl | RedCurl has collected data from the local disk of compromised hosts. [203] [204] |
| S1240 | RedLine Stealer | RedLine Stealer has collected data stored locally including chat logs and files associated with chat services such as Steam, Discord, and Telegram. [205] |
| S0448 | Rising Sun | Rising Sun has collected data and files from a compromised host. [206] |
| S0240 | ROKRAT | ROKRAT can collect host data and specific file types. [207] [208] [209] |
| S0090 | Rover | Rover searches for files on local drives based on a predefined list of file extensions. [210] |
| S1018 | Saint Bot | Saint Bot can collect files and information from a compromised host. [211] |
| S1099 | Samurai | Samurai can leverage an exfiltration module to download arbitrary files from compromised machines. [212] |
| G0034 | Sandworm Team | Sandworm Team has exfiltrated internal documents, files, and other data from compromised hosts. [213] |
| S1085 | Sardonic | Sardonic has the ability to collect data from a compromised machine to deliver to the attacker. [214] |
| S0461 | SDBbot | SDBbot has the ability to access the file system on a compromised host. [215] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors extracted information from the compromised systems. [216] [217] [218] [219] |
| S1019 | Shark | Shark can upload files to its C2. [157] [220] |
| S1089 | SharpDisco | SharpDisco has dropped a recent-files stealer plugin to C:\Users\Public\WinSrcNT\It11.exe . [163] |
| S0444 | ShimRat | ShimRat has the capability to upload collected files to a C2. [221] |
| S0610 | SideTwist | SideTwist has the ability to upload files from a compromised host. [222] |
| S1110 | SLIGHTPULSE | SLIGHTPULSE can read files specified on the local system. [223] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA has uploaded files and information from victim machines. [224] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 extracted files from compromised networks. [225] |
| S0615 | SombRAT | SombRAT has collected data and files from a compromised host. [61] [226] |
| S9024 | SPAWNCHIMERA | SPAWNCHIMERA has extracted the device’s Linux kernel image (vmlinux). [227] [228] [229] |
| S0646 | SpicyOmelette | SpicyOmelette has collected data and other information from a compromised host. [230] |
| S1037 | STARWHALE | STARWHALE can collect data from an infected local host. [231] |
| S1200 | StealBit | StealBit can upload data and files to the LockBit victim-shaming site. [232] [233] |
| G0038 | Stealth Falcon | Stealth Falcon malware gathers data from the local victim system. [234] |
| S1034 | StrifeWater | StrifeWater can collect data from a compromised host. [235] |
| S0559 | SUNBURST | SUNBURST collected information from a compromised host. [236] [237] |
| S1064 | SVCReady | SVCReady can collect data from an infected host. [238] |
| S0663 | SysUpdate | SysUpdate can collect information and files from a compromised host. [239] |
| S0011 | Taidoor | Taidoor can upload data and files from a victim's machine. [240] |
| S0467 | TajMahal | TajMahal has the ability to steal documents from the local system including the print spooler queue. [241] |
| G0027 | Threat Group-3390 | Threat Group-3390 ran a command to compile an archive of file types of interest from the victim user's directories. [242] |
| S0665 | ThreatNeedle | ThreatNeedle can collect data and files from a compromised host. [137] |
| S0668 | TinyTurla | TinyTurla can upload files from a compromised host. [243] |
| G1022 | ToddyCat | ToddyCat has run scripts to collect documents from targeted hosts. [143] |
| S0671 | Tomiris | Tomiris has the ability to collect recent files matching a hardcoded list of extensions prior to exfiltration. [244] |
| S0266 | TrickBot | TrickBot collects local files and information from the victim’s local machine. [245] |
| S1196 | Troll Stealer | Troll Stealer gathers information from infected systems such as SSH information from the victim's .ssh directory. [246] Troll Stealer collects information from local FileZilla installations and Microsoft Sticky Note. [247] |
| S9009 | TruffleHog | TruffleHog has gathered data from home directories of the victim environment. [248] |
| G0010 | Turla | Turla RPC backdoors can upload files from victim machines. [249] |
| S0275 | UPPERCUT | UPPERCUT can upload files to the C2 from infected machines. [250] [251] |
| S0022 | Uroburos | Uroburos can use its Get command to exfiltrate specified files from the compromised system. [252] |
| S0386 | Ursnif | Ursnif has collected files from victim machines, including certificates and cookies. [253] |
| S0452 | USBferry | USBferry can collect information from an air-gapped host machine. [254] |
| G1055 | VOID MANTICORE | VOID MANTICORE has collected cached data and files from within the victim environment. [255] [256] [257] |
| G1017 | Volt Typhoon | Volt Typhoon has stolen files from a sensitive file server and the Active Directory database from targeted environments, and used Wevtutil to extract event log information. [258] [259] [260] |
| S0670 | WarzoneRAT | WarzoneRAT can collect data from a compromised host. [261] |
| S0515 | WellMail | WellMail can exfiltrate files from the victim machine. [262] |
| S0514 | WellMess | WellMess can send files from the victim machine to C2. [263] [264] |
| S0645 | Wevtutil | Wevtutil can be used to export events from a specific log. [265] [266] |
| G0124 | Windigo | Windigo has used a script to gather credentials in files left on disk by OpenSSH backdoors. [267] |
| G0102 | Wizard Spider | Wizard Spider has collected data from a compromised host prior to exfiltration. [268] |
| S1065 | Woody RAT | Woody RAT can collect information from a compromised host. [269] |
| S0653 | xCaon | xCaon has uploaded files from victims' machines. [37] |
| S0658 | XCSSET | XCSSET collects contacts and application data from files in Desktop, Documents, Downloads, Dropbox, and WeChat folders. [270] |
| S0248 | yty | yty collects files with the following extensions: .ppt, .pptx, .pdf, .doc, .docx, .xls, .xlsx, .docm, .rtf, .inp, .xlsm, .csv, .odt, .pps, .vcf and sends them back to the C2 server. [271] |
| S0672 | Zox | Zox has the ability to upload files from a targeted system. [22] |
| S0412 | ZxShell | ZxShell can transfer files from a compromised host. [272] |
| S1013 | ZxxZ | ZxxZ can collect data from a compromised host. [273] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1057 | Data Loss Prevention | Data loss prevention can restrict access to sensitive data and detect sensitive data that is unencrypted. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0380 | Detection of Local Data Collection Prior to Exfiltration | AN1070 | Adversaries collecting local files via PowerShell, WMI, or direct file API calls often include recursive file listings, targeted file reads, and temporary file staging. |
| AN1071 | Adversaries using bash scripts or tools to recursively enumerate user home directories, config files, or SSH keys. |  |  |
| AN1072 | Adversary use of bash/zsh or AppleScript to locate files and exfil targets like user keychains or documents. |  |  |
| AN1073 | Collection of device configuration via CLI commands (e.g., show running-config , copy flash , more ), often followed by TFTP/SCP transfers. |  |  |
| AN1074 | Adversaries accessing datastore or configuration files via vim-cmd , esxcli , or SCP to extract logs, VMs, or host configurations. |  |  |

---

## References

- [Cisco. (2022, August 16). show running-config - Cisco IOS Configuration Fundamentals Command Reference . Retrieved July 13, 2022.](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/show_protocols_through_showmon.html#wp2760878733)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [Kasuya, M. (2020, January 8). Threat Spotlight: Amadey Bot Targets Non-Russian Users. Retrieved July 14, 2022.](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
- [FSI. (2017, July 27). Campaign Rifle - Andariel, the Maiden of Anguish. Retrieved September 12, 2024.](https://fsiceat.tistory.com/2)
- [Anthropic. (2025, November). Disrupting the first reported AI-orchestrated cyber espionage campaign. Retrieved April 20, 2026.](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [KISA. (2021). Phishing Target Reconnaissance and Attack Resource Analysis Operation Muzabi. Retrieved March 8, 2024.](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Guarnieri, C. (2015, June 19). Digital Attack on German Parliament: Investigative Report on the Hack of the Left Party Infrastructure in Bundestag. Retrieved January 22, 2018.](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)
- [Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved November 17, 2024.](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)
- [Hacquebord, F. (n.d.). Pawn Storm in 2019 A Year of Scanning and Credential Phishing on High-Profile Targets. Retrieved December 29, 2020.](https://documents.trendmicro.com/assets/white_papers/wp-pawn-storm-in-2019.pdf)
- [NSA, CISA, FBI, NCSC. (2021, July). Russian GRU Conducting Global Brute Force Campaign to Compromise Enterprise and Cloud Environments. Retrieved July 26, 2021.](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)
- [Mandiant. (2022, May 2). UNC3524: Eye Spy on Your Email. Retrieved August 17, 2023.](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
- [valsmith. (2012, September 21). More on APTSim. Retrieved September 28, 2017.](http://carnal0wnage.attackresearch.com/2012/09/more-on-aptsim.html)
- [FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
- [DHS/CISA. (2020, August 26). FASTCash 2.0: North Korea's BeagleBoyz Robbing Banks. Retrieved September 29, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)
- [Symantec. (2018, February 28). Chafer: Latest Attacks Reveal Heightened Ambitions. Retrieved May 22, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/chafer-latest-attacks-reveal-heightened-ambitions)
- [FBI. (2020, September 17). Indicators of Compromise Associated with Rana Intelligence Computing, also known as Advanced Persistent Threat 39, Chafer, Cadelspy, Remexi, and ITG07. Retrieved December 10, 2020.](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)
- [Rostovcev, N. (2021, June 10). Big airline heist APT41 likely behind a third-party attack on Air India. Retrieved August 26, 2021.](https://www.group-ib.com/blog/colunmtk-apt41/)
- [CrowdStrike. (2023). 2022 Falcon OverWatch Threat Hunting Report. Retrieved May 20, 2024.](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)
- [Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
- [Accenture iDefense Unit. (2019, March 5). Mudcarp's Focus on Submarine Technologies. Retrieved August 24, 2021.](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Levene, B. et al.. (2018, March 7). Patchwork Continues to Deliver BADNEWS to the Indian Subcontinent. Retrieved March 31, 2018.](https://researchcenter.paloaltonetworks.com/2018/03/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/)
- [Bar, T., Conant, S. (2017, October 20). BadPatch. Retrieved November 13, 2018.](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)
- [Check Point. (2020, November 26). Bandook: Signed & Delivered. Retrieved May 31, 2021.](https://research.checkpoint.com/2020/bandook-signed-delivered/)
- [Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Kirill Boychenko. (2025, July 14). Contagious Interview Campaign Escalates With 67 Malicious npm Packages and New Malware Loader. Retrieved October 19, 2025.](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Unit42. (2024, October 9). Contagious Interview: DPRK Threat Actors Lure Tech Industry Job Seekers to Install New Variants of BeaverTail and InvisibleFerret Malware. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [MSTIC. (2019, December 12). GALLIUM: Targeting global telecom. Retrieved January 13, 2021.](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)
- [US-CERT. (2020, August 19). MAR-10295134-1.v1 – North Korean Remote Access Trojan: BLINDINGCAN. Retrieved August 19, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
- [CheckPoint Research. (2021, July 1). IndigoZebra APT continues to attack Central Asia with evolving tools. Retrieved September 24, 2021.](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
- [DHS/CISA. (2026, February 11). AR25-338A: BRICKSTORM Backdoor. Retrieved April 16, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
- [Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)
- [Harbison, M. and Renals, P. (2022, July 5). When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors. Retrieved February 1, 2023.](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
- [Cybereason. (2022, August 17). Bumblebee Loader – The High Road to Enterprise Domain Control. Retrieved August 29, 2022.](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Kuzin, M., Zelensky S. (2018, July 20). Calisto Trojan for macOS. Retrieved September 7, 2018.](https://securelist.com/calisto-trojan-for-macos/86543/)
- [Marvi, A. et al.. (2023, March 16). Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation. Retrieved March 22, 2023.](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [Lee, T., Hanzlik, D., Ahl, I. (2013, August 7). Breaking Down the China Chopper Web Shell - Part I. Retrieved March 27, 2015.](https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-i.html)
- [The Australian Cyber Security Centre (ACSC), the Canadian Centre for Cyber Security (CCCS), the New Zealand National Cyber Security Centre (NZ NCSC), CERT New Zealand, the UK National Cyber Security Centre (UK NCSC) and the US National Cybersecurity and Communications Integration Center (NCCIC). (2018, October 11). Joint report on publicly available hacking tools. Retrieved March 11, 2019.](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
- [Eoin Miller. (2021, March 23). Defending Against the Zero Day: Analyzing Attacker Behavior Post-Exploitation of Microsoft Exchange. Retrieved October 27, 2022.](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Cobalt Strike. (2017, December 8). Tactics, Techniques, and Procedures. Retrieved November 17, 2024.](https://web.archive.org/web/20210924171429/https://www.cobaltstrike.com/downloads/reports/tacticstechniquesandprocedures.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Chen, y., et al. (2019, January 31). Mac Malware Steals Cryptocurrency Exchanges’ Cookies. Retrieved July 22, 2020.](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
- [F-Secure Labs. (2014, July). COSMICDUKE Cosmu with a twist of MiniDuke. Retrieved July 3, 2014.](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [Microsoft. (2022, June 2). Exposing POLONIUM activity and infrastructure targeting Israeli organizations. Retrieved July 1, 2022.](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
- [N. Baisini. (2022, July 13). Transparent Tribe begins targeting education sector in latest campaign. Retrieved September 22, 2022.](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
- [Faou, M. (2020, December 2). Turla Crutch: Keeping the “back door” open. Retrieved December 4, 2020.](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
- [Stokes, P. (2020, July 27). Four Distinct Families of Lazarus Malware Target Apple’s macOS Platform. Retrieved August 7, 2020.](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
- [MSTIC. (2021, November 16). Evolving trends in Iranian threat actor activity – MSTIC presentation at CyberWarCon 2021. Retrieved January 12, 2023.](https://www.microsoft.com/en-us/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021)
- [Meltzer, M. et al. (2024, January 10). Active Exploitation of Two Zero-Day Vulnerabilities in Ivanti Connect Secure VPN. Retrieved February 27, 2024.](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/)
- [Lin, M. et al. (2024, January 31). Cutting Edge, Part 2: Investigating Ivanti Connect Secure VPN Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
- [NCSC. (2022, February 23). Cyclops Blink Malware Analysis Report. Retrieved March 3, 2022.](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
- [SecureWorks 2019, August 27 LYCEUM Takes Center Stage in Middle East Campaign Retrieved. 2019/11/19](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)
- [Blaich, A., et al. (2018, January 18). Dark Caracal: Cyber-espionage at a Global Scale. Retrieved April 11, 2018.](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)
- [McGraw, T. (2024, December 4). Black Basta Ransomware Campaign Drops Zbot, DarkGate, and Custom Malware. Retrieved December 9, 2024.](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [Shivtarkar, N. and Kumar, A. (2022, June 9). Lyceum .NET DNS Backdoor. Retrieved June 23, 2022.](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [NSA/FBI. (2020, August). Russian GRU 85th GTsSS Deploys Previously Undisclosed Drovorub Malware. Retrieved August 25, 2020.](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
- [Hod Gavriel. (2019, November 21). Dtrack: In-depth analysis of APT on a nuclear power plant. Retrieved January 20, 2021.](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Microsoft Threat Intelligence. (2023, June 14). Cadet Blizzard emerges as a novel and distinct Russian threat actor. Retrieved July 10, 2023.](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)
- [US Cybersecurity & Infrastructure Security Agency et al. (2024, September 5). Russian Military Cyber Actors Target U.S. and Global Critical Infrastructure. Retrieved September 6, 2024.](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)
- [MSTIC. (2021, May 28). Breaking down NOBELIUM’s latest early-stage toolset. Retrieved August 4, 2021.](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
- [Red Canary. (2021, March 31). 2021 Threat Detection Report. Retrieved August 31, 2021.](https://resource.redcanary.com/rs/003-YRU-314/images/2021-Threat-Detection-Report.pdf?mkt_tok=MDAzLVlSVS0zMTQAAAF_PIlmhNTaG2McG4X_foM-cIr20UfyB12MIQ10W0HbtMRwxGOJaD0Xj6CRTNg_S-8KniRxtf9xzhz_ACvm_TpbJAIgWCV8yIsFgbhb8cuaZA)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [Sygnia Incident Response Team. (2022, January 5). TG2003: ELEPHANT BEETLE UNCOVERING AN ORGANIZED FINANCIAL-THEFT OPERATION. Retrieved February 9, 2023.](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)
- [Chen, J. (2019, October 10). Magecart Card Skimmers Injected Into Online Shops. Retrieved September 9, 2020.](https://www.trendmicro.com/en_us/research/19/j/fin6-compromised-e-commerce-platform-via-magecart-to-inject-credit-card-skimmers-into-thousands-of-online-shops.html)
- [Klijnsma, Y. (2018, September 11). Inside the Magecart Breach of British Airways: How 22 Lines of Code Claimed 380,000 Victims. Retrieved September 9, 2020.](https://web.archive.org/web/20181231220607/https://riskiq.com/blog/labs/magecart-british-airways-breach/)
- [Klijnsma, Y. (2018, September 19). Another Victim of the Magecart Assault Emerges: Newegg. Retrieved September 9, 2020.](https://web.archive.org/web/20181209083100/https://www.riskiq.com/blog/labs/magecart-newegg/)
- [Loui, E. and Reynolds, J. (2021, August 30). CARBON SPIDER Embraces Big Game Hunting, Part 1. Retrieved September 20, 2021.](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved November 17, 2024.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [Ramin Nafisi. (2021, September 27). FoggyWeb: Targeted NOBELIUM malware leads to persistent backdoor. Retrieved October 4, 2021.](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
- [CISA. (2020, September 15). Iran-Based Threat Actor Exploits VPN Vulnerabilities. Retrieved December 21, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)
- [Kremez, V. (2019, September 19). FIN6 “FrameworkPOS”: Point-of-Sale Malware Analysis & Internals. Retrieved September 8, 2020.](https://labs.sentinelone.com/fin6-frameworkpos-point-of-sale-malware-analysis-internals-2/)
- [Adamitis, D. et al. (2019, June 4). It's alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign. Retrieved May 11, 2020.](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
- [Global Research and Analysis Team. (2020, April 30). APT trends report Q1 2020. Retrieved September 19, 2022.](https://securelist.com/apt-trends-report-q1-2020/96826/)
- [Cybereason Nocturnus. (2019, June 25). Operation Soft Cell: A Worldwide Campaign Against Telecommunications Providers. Retrieved July 18, 2019.](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Kirill Boychenko. (2026, January 31). GlassWorm Loader Hits Open VSX via Developer Account Compromise. Retrieved April 10, 2026.](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
- [Sandvik, Runa. (2021, October 1). Made In America: Green Lambert for OS X. Retrieved March 21, 2022.](https://objective-see.com/blog/blog_0x68.html)
- [Priego, A. (2021, July). THE BROTHERS GRIM: THE REVERSING TALE OF GRIMAGENT MALWARE USED BY RYUK. Retrieved September 19, 2024.](https://www.group-ib.com/blog/grimagent/)
- [Microsoft Threat Intelligence . (2025, March 5). Silk Typhoon targeting IT supply chain. Retrieved March 20, 2025.](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/)
- [Ungur, P. (n.d.). HAVOC. Retrieved August 4, 2025.](https://havocframework.com/docs/welcome)
- [Immersive Content Team. (2024, April 9). Havoc C2 Framework – A Defensive Operator’s Guide. Retrieved August 13, 2025.](https://www.immersivelabs.com/resources/blog/havoc-c2-framework-a-defensive-operators-guide)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
- [Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
- [CrowdStrike. (2022, May). ICEAPPLE: A NOVEL INTERNET INFORMATION SERVICES (IIS) POST-EXPLOITATION FRAMEWORK. Retrieved June 27, 2022.](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
- [GReAT. (2019, August 12). Recent Cloud Atlas activity. Retrieved May 8, 2020.](https://securelist.com/recent-cloud-atlas-activity/92016/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [Sancho, D., et al. (2012, May 22). IXESHE An APT Campaign. Retrieved June 7, 2019.](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Dahan, A. et al. (2020, November 2). Back to the Future: Inside the Kimsuky KGH Spyware Suite. Retrieved November 6, 2020.](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
- [Tarakanov , D.. (2013, September 11). The “Kimsuky” Operation: A North Korean APT?. Retrieved August 13, 2019.](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Magius, J., et al. (2017, July 19). Koadic. Retrieved September 27, 2024.](https://github.com/offsecginger/koadic)
- [Jazi, H. (2021, February). LazyScripter: From Empire to double RAT. Retrieved November 17, 2024.](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
- [Threat Intelligence Team. (2021, August 23). New variant of Konni malware used in campaign targetting Russia. Retrieved January 5, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
- [Conteras, T., Splunk Research Team. (2025, September 25). From Prompt to Payload: LAMEHUG’s LLM-Driven Cyber Intrusion. Retrieved April 21, 2026.](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
- [Google Threat Intelligence Group. (2025, November 5). GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools. Retrieved March 31, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
- [MSTIC, DART, M365 Defender. (2022, March 24). DEV-0537 Criminal Actor Targeting Organizations for Data Exfiltration and Destruction. Retrieved May 17, 2022.](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)
- [Batista, J. (2024, June 17). Latrodectus, are you coming back?. Retrieved September 13, 2024.](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Remote Administration Tools & Content Staging Malware Report. Retrieved March 16, 2016.](https://web.archive.org/web/20220608001455/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf)
- [Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle. Retrieved October 27, 2021.](https://securelist.com/lazarus-threatneedle/100803/)
- [Faou, M. (2019, May). Turla LightNeuron: One email away from remote code execution. Retrieved June 24, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
- [Zhou, R. (2012, May 15). Backdoor.Linfo. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part II. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
- [Breitenbacher, D. (2022, December 14). Unmasking MirrorFace: Operation LiberalFace targeting Japanese political entities. Retrieved April 17, 2026.](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
- [ITOCHU. (2024, January 24). The Endless Struggle Against APT10: Insights from LODEINFO v0.6.6 - v0.7.3 Analysis. Retrieved April 17, 2026.](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [Lechtik, M, and etl. (2021, July 14). LuminousMoth APT: Sweeping attacks for the chosen few. Retrieved October 20, 2022.](https://securelist.com/apt-luminousmoth/103332/)
- [Botezatu, B and etl. (2021, July 21). LuminousMoth - PlugX, File Exfiltration and Persistence Revisited. Retrieved October 20, 2022.](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [DFIR Report. (2022, March 21). APT35 Automates Initial Access Using ProxyShell. Retrieved May 25, 2022.](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [GReAT. (2021, June 16). Ferocious Kitten: 6 Years of Covert Surveillance in Iran. Retrieved September 22, 2021.](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
- [Secureworks. (2019, July 24). MCMD Malware Analysis. Retrieved August 13, 2020.](https://www.secureworks.com/research/mcmd-malware-analysis)
- [United States District Court Southern District of New York (USDC SDNY) . (2018, December 17). United States of America v. Zhu Hua and Zhang Shilong. Retrieved April 17, 2019.](https://www.justice.gov/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion)
- [Symantec. (2020, November 17). Japan-Linked Organizations Targeted in Long-Running and Sophisticated Attack Campaign. Retrieved December 17, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [Facundo Muñoz. (2023, April 26). Evasive Panda APT group delivers malware via updates for popular Chinese software. Retrieved July 25, 2024.](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)
- [ClearSky Cyber Security . (2021, August). New Iranian Espionage Campaign By “Siamesekitten” - Lyceum. Retrieved June 6, 2022.](https://www.clearskysec.com/siamesekitten/)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Falcone, R. and Miller-Osborn, J.. (2016, January 24). Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists. Retrieved February 10, 2016.](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [Vrabie, V. (2021, April 23). NAIKON – Traces from a Military Cyber-Espionage Operation. Retrieved June 29, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
- [McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Fidelis Cybersecurity. (2013, June 28). Fidelis Threat Advisory #1009: "njRAT" Uncovered. Retrieved June 4, 2019.](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
- [Dray Agha. (2022, August 16). Cleartext Shenanigans: Gifting User Passwords to Adversaries With NPPSPY. Retrieved May 17, 2024.](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
- [Cherepanov, A. (2018, October 4). Nomadic Octopus Cyber espionage in Central Asia. Retrieved October 13, 2021.](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)
- [Fahmy, M. et al. (2024, October 11). Earth Simnavaz (aka APT34) Levies Advanced Cyberattacks Against Middle East. Retrieved November 27, 2024.](https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [Cashman, M. (2020, July 29). Operation North Star Campaign. Retrieved December 20, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-a-job-offer-thats-too-good-to-be-true/?hilite=%27Operation%27%2C%27North%27%2C%27Star%27)
- [Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-uncovers-operation-honeybee-malicious-document-campaign-targeting-humanitarian-aid-groups/)
- [Volexity Threat Research. (2024, April 12). Zero-Day Exploitation of Unauthenticated Remote Code Execution Vulnerability in GlobalProtect (CVE-2024-3400). Retrieved November 20, 2024.](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Magisa, L. (2020, November 27). New MacOS Backdoor Connected to OceanLotus Surfaces. Retrieved December 2, 2020.](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)
- [Peretz, A. and Theck, E. (2021, March 5). Earth Vetala – MuddyWater Continues to Target Organizations in the Middle East. Retrieved March 18, 2021.](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [ANSSI. (2021, January 27). SANDWORM INTRUSION SET CAMPAIGN TARGETING CENTREON SYSTEMS. Retrieved March 30, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
- [Mullaney, C. & Honda, H. (2012, May 4). Trojan.Pasam. Retrieved February 22, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)
- [Cymmetria. (2016). Unveiling Patchwork - The Copy-Paste APT. Retrieved November 17, 2024.](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)
- [Trustwave SpiderLabs. (2020, June 22). Pillowmint: FIN7’s Monkey Thief . Retrieved July 27, 2020.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
- [F-Secure Labs. (2015, September 17). The Dukes: 7 years of Russian cyberespionage. Retrieved December 10, 2015.](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
- [Unit 42. (2022, June 13). GALLIUM Expands Targeting Across Telecommunications, Government and Finance Sectors With New PingPull Tool. Retrieved August 7, 2022.](https://unit42.paloaltonetworks.com/pingpull-gallium/)
- [Hayashi, K. (2005, August 18). Backdoor.Darkmoon. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)
- [Cybereason Nocturnus. (2022, February 1). PowerLess Trojan: Iranian APT Phosphorus Adds New PowerShell Backdoor for Espionage. Retrieved June 1, 2022.](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)
- [PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.](https://github.com/PowerShellMafia/PowerSploit)
- [PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.](http://powersploit.readthedocs.io)
- [Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
- [Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
- [Kizhakkinan, D., et al. (2016, May 11). Threat Actor Leverages Windows Zero-day Exploit in Payment Card Data Attacks. Retrieved February 12, 2018.](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html)
- [Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy: New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)
- [Rainey, K. (n.d.). Qbot. Retrieved September 27, 2021.](https://redcanary.com/threat-detection-report/threats/qbot/)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [CISA. (2018, December 18). Analysis Report (AR18-352A) Quasar Open-Source Remote Administration Tool. Retrieved August 1, 2022.](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
- [Microsoft Threat Intelligence Center. (2022, February 4). ACTINIUM targets Ukrainian organizations. Retrieved February 18, 2022.](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
- [S2W TALON. (2022, June 16). Raccoon Stealer is Back with a New Version. Retrieved August 1, 2024.](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Antiy CERT. (2020, April 20). Analysis of Ramsay components of Darkhotel's infiltration and isolation network. Retrieved March 24, 2021.](https://www.programmersought.com/article/62493896999/)
- [Perez, D. et al. (2021, May 27). Re-Checking Your Pulse: Updates on Chinese APT Actors Compromising Pulse Secure VPN Devices. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
- [Nesbit, B. and Ackerman, D. (2017, January). Malware Analysis Report - RawPOS Malware: Deconstructing an Intruder’s Toolkit. Retrieved October 4, 2017.](https://www.kroll.com/en/insights/publications/malware-analysis-report-rawpos-malware)
- [TrendLabs Security Intelligence Blog. (2015, April). RawPOS Technical Brief. Retrieved October 4, 2017.](http://sjc1-te-ftp.trendmicro.com/images/tex/pdf/RawPOS%20Technical%20Brief.pdf)
- [Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.](https://www.youtube.com/watch?v=fevGZs0EQu8)
- [Global Threat Center, Intelligence Team. (2020, December). APT27 Turns to Ransomware. Retrieved November 12, 2021.](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
- [Group-IB. (2020, August). RedCurl: The Pentest You Didn’t Know About. Retrieved August 9, 2024.](https://www.group-ib.com/resources/research-hub/red-curl/)
- [Group-IB. (2021, November). RedCurl: The Awakening. Retrieved August 14, 2024.](https://www.group-ib.com/resources/research-hub/red-curl-2/)
- [Alexandre Cote Cyr. (2024, November 8). Life on a crooked RedLine: Analyzing the infamous infostealer’s backend. Retrieved September 17, 2025.](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [Pantazopoulos, N.. (2018, November 8). RokRat Analysis. Retrieved May 21, 2020.](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
- [Cash, D., Grunzweig, J., Adair, S., Lancaster, T. (2021, August 25). North Korean BLUELIGHT Special: InkySquid Deploys RokRAT. Retrieved October 1, 2021.](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
- [Jazi, Hossein. (2021, January 6). Retrohunting APT37: North Korean APT used VBA self decode technique to inject RokRat. Retrieved March 22, 2022.](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
- [Ray, V., Hayashi, K. (2016, February 29). New Malware ‘Rover’ Targets Indian Ambassador to Afghanistan. Retrieved February 29, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
- [Hasherezade. (2021, April 6). A deep dive into Saint Bot, a new downloader. Retrieved June 9, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Scott W. Brady. (2020, October 15). United States vs. Yuriy Sergeyevich Andrienko et al.. Retrieved November 25, 2020.](https://www.justice.gov/opa/press-release/file/1328521/download)
- [Symantec Threat Hunter Team. (2023, July 18). FIN8 Uses Revamped Sardonic Backdoor to Deliver Noberus Ransomware. Retrieved August 9, 2023.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)
- [Schwarz, D. et al. (2019, October 16). TA505 Distributes New SDBbot Remote Access Trojan with Get2 Downloader. Retrieved May 29, 2020.](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
- [Microsoft Threat Intelligence. (2025, July 22). Disrupting active exploitation of on-premises SharePoint vulnerabilities. Retrieved October 15, 2025.](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/#storm-2603)
- [ESET Research. (2025, July 24). ToolShell: An all-you-can-eat buffet for threat actors. Retrieved October 15, 2025.](https://www.welivesecurity.com/en/eset-research/toolshell-an-all-you-can-eat-buffet-for-threat-actors/)
- [Kenin, S. et al. (2025, July 21). SharePoint ToolShell | Zero-Day Exploited in-the-Wild Targets Enterprise Servers. Retrieved October 15, 2025.](https://www.sentinelone.com/blog/sharepoint-toolshell-zero-day-exploited-in-the-wild-targets-enterprise-servers/)
- [Unit 42. (2025, July 31). Active Exploitation of Microsoft SharePoint Vulnerabilities: Threat Brief (Updated). Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/microsoft-sharepoint-cve-2025-49704-cve-2025-49706-cve-2025-53770/)
- [Accenture. (2021, November 9). Who are latest targets of cyber group Lyceum?. Retrieved June 16, 2022.](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [Perez, D. et al. (2021, April 20). Check Your Pulse: Suspected APT Actors Leverage Authentication Bypass Techniques and Pulse Secure Zero-Day. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [Cash, D. et al. (2020, December 14). Dark Halo Leverages SolarWinds Compromise to Breach Organizations. Retrieved December 29, 2020.](https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [DHS/CISA. (2026, February 26). MAR-25993211-r1.v2 Ivanti Connect Secure (RESURGE): AR25-087A. Retrieved April 17, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
- [John Wolfram, Michael Edie, Jacob Thompson, Matt Lin, Josh Murchie. (2025, April 3). Suspected China-Nexus Threat Actor Actively Exploiting Critical Ivanti Connect Secure Vulnerability (CVE-2025-22457). Retrieved April 13, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)
- [Sila Ozeren Hacioglu. (2025, May 5). UNC5221’s Latest Exploit: Weaponizing CVE-2025-22457 in Ivanti Connect Secure. Retrieved April 13, 2026.](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
- [CTU. (2018, September 27). Cybercriminals Increasingly Trying to Ensnare the Big Financial Fish. Retrieved September 20, 2021.](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)
- [FBI, CISA, CNMF, NCSC-UK. (2022, February 24). Iranian Government-Sponsored Actors Conduct Cyber Operations Against Global Government and Commercial Networks. Retrieved September 27, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
- [FBI. (2022, February 4). Indicators of Compromise Associated with LockBit 2.0 Ransomware. Retrieved January 24, 2025.](https://www.ic3.gov/CSA/2022/220204.pdf)
- [Cybereason Global SOC Team. (n.d.). THREAT ANALYSIS REPORT: Inside the LockBit Arsenal - The StealBit Exfiltration Tool. Retrieved January 29, 2025.](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
- [Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.](https://citizenlab.org/2016/05/stealth-falcon/)
- [Cybereason Nocturnus. (2022, February 1). StrifeWater RAT: Iranian APT Moses Staff Adds New Trojan to Ransomware Operations. Retrieved August 15, 2022.](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
- [MSTIC. (2020, December 18). Analyzing Solorigate, the compromised DLL file that started a sophisticated cyberattack, and how Microsoft Defender helps protect customers . Retrieved January 5, 2021.](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [Daniel Lunghi. (2023, March 1). Iron Tiger’s SysUpdate Reappears, Adds Linux Targeting. Retrieved March 20, 2023.](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
- [Trend Micro. (2012). The Taidoor Campaign. Retrieved November 12, 2014.](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Counter Threat Unit Research Team. (2017, June 27). BRONZE UNION Cyberespionage Persists Despite Disclosures. Retrieved July 13, 2017.](https://www.secureworks.com/research/bronze-union)
- [Cisco Talos. (2021, September 21). TinyTurla - Turla deploys new malware to keep a secret backdoor on victim machines. Retrieved December 2, 2021.](https://blog.talosintelligence.com/2021/09/tinyturla.html)
- [Kwiatkoswki, I. and Delcher, P. (2021, September 29). DarkHalo After SolarWinds: the Tomiris connection. Retrieved December 27, 2021.](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/)
- [Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
- [Symantec Threat Hunter Team. (2024, May 16). Springtail: New Linux Backdoor Added to Toolkit. Retrieved January 17, 2025.](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
- [Jiho Kim & Sebin Lee, S2W. (2024, February 7). Kimsuky disguised as a Korean company signed with a valid certificate to distribute Troll Stealer (English ver.). Retrieved January 17, 2025.](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
- [Gianpietro Cutolo. (2025, November 26). Shai-Hulud 2.0: Aggressive, Automated, and Fast Spreading. Retrieved April 9, 2026.](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [Hiroaki, H. (2025, April 30). Earth Kasha Updates TTPs in Latest Campaign Targeting Taiwan and Japan. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
- [Hiroaki, H. (2024, November 26). Guess Who’s Back - The Return of ANEL in the Recent Earth Kasha Spear-phishing Campaign in 2024. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Sioting, S. (2013, June 15). BKDR_URSNIF.SM. Retrieved June 5, 2019.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [David Ketler. (2026, March 30). Stryker Cyber-Attack: What we Know so Far About the Remote Wipe Attack. Retrieved April 20, 2026.](https://specopssoft.com/blog/stryker-cyber-attack-what-we-know-remote-wipe/)
- [DOJ/FBI. (2026, March 19). Case 1:26-mj-00683-CDA: Affidavit in Support of Seizure Warrant: In the Matter of the Seizure of Domain Names Justicehomeland[.]org; karmabelow80[.]org; handala-hack[.]to; and handala-redwatned[.]to. Retrieved April 20, 2026.](https://www.justice.gov/opa/media/1431956/dl?inline)
- [FBI. (2026, March 20). FBI Flash: FLASH-20260320-001:Government of Iran Cyber Actors Deploy Telegram C2 to Push Malware to Identified Targets. Retrieved April 20, 2026.](https://www.ic3.gov/CSA/2026/260320.pdf)
- [NSA et al. (2023, May 24). People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection. Retrieved July 27, 2023.](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)
- [Counter Threat Unit Research Team. (2023, May 24). Chinese Cyberespionage Group BRONZE SILHOUETTE Targets U.S. Government and Defense Organizations. Retrieved July 27, 2023.](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [CISA. (2020, July 16). MAR-10296782-3.v1 – WELLMAIL. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
- [PWC. (2020, July 16). How WellMess malware has been used to target COVID-19 vaccines. Retrieved September 24, 2020.](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)
- [CISA. (2020, July 16). MAR-10296782-2.v1 – WELLMESS. Retrieved September 24, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)
- [Microsoft. (n.d.). wevtutil. Retrieved September 14, 2021.](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil)
- [F-Secure Labs. (2020, August 18). Lazarus Group Campaign Targeting the Cryptocurrency Vertical. Retrieved September 1, 2020.](https://web.archive.org/web/20200901113617/https://labs.f-secure.com/assets/BlogFiles/f-secureLABS-tlp-white-lazarus-threat-intel-report2.pdf)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Mac Threat Response, Mobile Research Team. (2020, August 13). The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSS Backdoor Planting in Safari, and Leverages Two Zero-day Exploits. Retrieved October 5, 2021.](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
- [Schwarz, D., Sopko J. (2018, March 08). Donot Team Leverages New Modular Malware Framework in South Asia. Retrieved June 11, 2018.](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)
- [Raghuprasad, C . (2022, May 11). Bitter APT adds Bangladesh to their targets. Retrieved June 1, 2022.](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)

---

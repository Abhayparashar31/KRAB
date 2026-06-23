# Exfiltration Over C2 Channel

## Description

Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0045 | ADVSTORESHELL | ADVSTORESHELL exfiltrates data over the same channel used for C2. [1] |
| G1030 | Agrius | Agrius exfiltrated staged data using tools such as Putty and WinSCP, communicating with command and control servers. [2] |
| S1025 | Amadey | Amadey has sent victim data to its C2 servers. [3] |
| S0584 | AppleJeus | AppleJeus has exfiltrated collected host information to a C2 server. [4] |
| S0622 | AppleSeed | AppleSeed can exfiltrate files via the C2 channel. [5] |
| G0022 | APT3 | APT3 has a tool that exfiltrates data over the C2 channel. [6] |
| G0050 | APT32 | APT32 's backdoor has exfiltrated data using the already opened channel with its C&C server. [7] |
| G0087 | APT39 | APT39 has exfiltrated stolen victim data through C2 communications. [8] |
| C0046 | ArcaneDoor | ArcaneDoor included use of existing command and control channels for data exfiltration. [9] [10] |
| S9031 | AshTag | AshTag has exfiltrated reconnaissance data on targeted systems to C2 servers. [11] |
| S0373 | Astaroth | Astaroth exfiltrates collected information from its r1.log file to the external C2 server. [12] |
| S0438 | Attor | Attor has exfiltrated data over the C2 channel. [13] |
| S1029 | AuTo Stealer | AuTo Stealer can exfiltrate data over actor-controlled C2 servers via HTTP or TCP. [14] |
| S0031 | BACKSPACE | Adversaries can direct BACKSPACE to upload files to the C2 Server. [15] |
| S1081 | BADHATCH | BADHATCH can exfiltrate data over the C2 channel. [16] [17] |
| S0234 | Bandook | Bandook can upload files from a victim's machine over the C2 channel. [18] |
| S0239 | Bankshot | Bankshot exfiltrates data over its C2 channel. [19] |
| S1246 | BeaverTail | BeaverTail has exfiltrated data collected from victim devices to C2 servers. [20] [21] [22] |
| S0268 | Bisonal | Bisonal has added the exfiltrated data to the URL over the C2 channel. [23] |
| G1043 | BlackByte | BlackByte transmitted collected victim host information via HTTP POST to command and control infrastructure. [24] |
| S0520 | BLINDINGCAN | BLINDINGCAN has sent user and system information to a C2 server via HTTP POST requests. [25] [26] |
| S0657 | BLUELIGHT | BLUELIGHT has exfiltrated data over its C2 channel. [27] |
| S0651 | BoxCaon | BoxCaon uploads files and data from a compromised host over the existing C2 channel. [28] |
| S9015 | BRICKSTORM | BRICKSTORM has uploaded files from the victim system to C2 servers. [29] [30] [31] [32] [33] [34] [35] |
| S1039 | Bumblebee | Bumblebee can send collected data in JSON format to C2. [36] |
| C0017 | C0017 | During C0017 , APT41 used its Cloudflare services C2 channels for data exfiltration. [37] |
| S0077 | CallMe | CallMe exfiltrates data to its C2 server over the same protocol as C2 communications. [38] |
| S0351 | Cannon | Cannon exfiltrates collected data over email via SMTP/S and POP3/S C2 channels. [39] |
| S0484 | Carberp | Carberp has exfiltrated data via HTTP to already established C2 servers. [40] [41] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell can upload files over the C2 channel. [42] |
| S0674 | CharmPower | CharmPower can exfiltrate gathered data to a hardcoded C2 URL via HTTP POST. [43] |
| G0114 | Chimera | Chimera has used Cobalt Strike C2 beacons for data exfiltration. [44] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP can upload collected files to the command-and-control server. [45] |
| S0667 | Chrommme | Chrommme can exfiltrate collected data via C2. [46] |
| G0142 | Confucius | Confucius has exfiltrated stolen files to its C2 server. [47] |
| G1052 | Contagious Interview | Contagious Interview has exfiltrated data from a compromised host to actor-controlled C2 servers. [48] [49] [50] [51] [20] [52] [53] [54] [21] [22] |
| S1024 | CreepySnail | CreepySnail can connect to C2 for data exfiltration. [55] |
| S0115 | Crimson | Crimson can exfiltrate stolen information over its C2. [56] |
| S0538 | Crutch | Crutch can exfiltrate data over the primary C2 channel (Dropbox HTTP API). [57] |
| S1153 | Cuckoo Stealer | Cuckoo Stealer can send information about the targeted system to C2 including captured passwords, OS build, hostname, and username. [58] |
| G1012 | CURIUM | CURIUM has used IMAP and SMTPS for exfiltration via tools such as IMAPLoader . [59] |
| S0687 | Cyclops Blink | Cyclops Blink has the ability to upload exfiltrated files to a C2 server. [60] |
| S1111 | DarkGate | DarkGate uses existing command and control channels to retrieve captured cryptocurrency wallet credentials. [61] |
| S1021 | DnsSystem | DnsSystem can exfiltrate collected data to its C2 server. [62] |
| S0600 | Doki | Doki has used Ngrok to establish C2 and exfiltrate data. [63] |
| S0502 | Drovorub | Drovorub can exfiltrate files over C2 infrastructure. [64] |
| S1159 | DUSTTRAP | DUSTTRAP can exfiltrate collected data over C2 channels. [65] |
| S0062 | DustySky | DustySky has exfiltrated data to the C2 server. [66] |
| S0024 | Dyre | Dyre has the ability to send information staged on a compromised host externally to C2. [67] |
| S0377 | Ebury | Ebury exfiltrates a list of outbound and inbound SSH sessions using OpenSSH's known_host files and wtmp records. Ebury can exfiltrate SSH credentials through custom DNS queries or use the command Xcat to send the process's ssh session's credentials to the C2 server. [68] [69] |
| S0367 | Emotet | Emotet has exfiltrated data over its C2 channel. [70] [71] |
| S0363 | Empire | Empire can send data gathered from a target through the command and control channel. [72] [73] |
| S0568 | EVILNUM | EVILNUM can upload files over the C2 channel from the infected host. [74] |
| S0696 | Flagpro | Flagpro has exfiltrated data to the C2 server. [75] |
| S0381 | FlawedAmmyy | FlawedAmmyy has sent data collected from a compromised host to its C2 servers. [76] |
| S0661 | FoggyWeb | FoggyWeb can remotely exfiltrate sensitive information from a compromised AD FS server. [77] |
| C0001 | Frankenstein | During Frankenstein , the threat actors collected information via Empire , which sent the data back to the adversary's C2. [73] |
| S1044 | FunnyDream | FunnyDream can execute commands, including gathering user information, and send the results to C2. [78] |
| G0093 | GALLIUM | GALLIUM used Web shells and HTRAN for C2 and to exfiltrate data. [79] |
| G0047 | Gamaredon Group | A Gamaredon Group file stealer can transfer collected files to a hardcoded C2 server. [80] [81] [82] |
| S0493 | GoldenSpy | GoldenSpy has exfiltrated host environment information to an external C2 domain via port 9006. [83] |
| S0588 | GoldMax | GoldMax can exfiltrate files over the existing C2 channel. [84] [85] |
| S0477 | Goopy | Goopy has the ability to exfiltrate data over the Microsoft Outlook C2 channel. [86] |
| S0531 | Grandoreiro | Grandoreiro can send data it retrieves to the C2 server. [87] |
| S0632 | GrimAgent | GrimAgent has sent data related to a compromise host over its C2 channel. [88] |
| S0391 | HAWKBALL | HAWKBALL has sent system information and files over the C2 channel. [89] |
| S1249 | HexEval Loader | HexEval Loader has exfiltrated victim data using HTTPS POST requests to its C2 servers. [51] [52] |
| G0126 | Higaisa | Higaisa exfiltrated data over its C2 channel. [90] |
| C0038 | HomeLand Justice | During HomeLand Justice , threat actors used HTTP to transfer data from compromised Exchange servers. [91] |
| S0376 | HOPLIGHT | HOPLIGHT has used its C2 channel to exfiltrate data. [92] |
| S0431 | HotCroissant | HotCroissant has the ability to download files from the infected host to the command and control (C2) server. [93] |
| S9007 | HTTPTroy | HTTPTroy has exfiltrated encrypted data over the C2 channel using the up <FILENAME> command. [94] |
| S1022 | IceApple | IceApple 's Multi File Exfiltrator module can exfiltrate multiple files from a compromised host as an HTTP response over C2. [95] |
| S0434 | Imminent Monitor | Imminent Monitor has uploaded a file containing debugger logs, network information and system information to the C2. [96] |
| S0604 | Industroyer | Industroyer sends information about hardware profiles and previously-received commands back to the C2 server in a POST-request. [97] |
| S1245 | InvisibleFerret | InvisibleFerret has used HTTP communications to the "/Uploads" URI for file exfiltration. [98] |
| S1132 | IPsec Helper | IPsec Helper exfiltrates specific files through its command and control framework. [99] |
| G0004 | Ke3chang | Ke3chang transferred compressed and encrypted RAR files containing exfiltration through the established backdoor command and control channel during operations. [100] |
| S0487 | Kessel | Kessel has exfiltrated information gathered from the infected system to the C2 server. [101] |
| S1020 | Kevin | Kevin can send data from the victim host through a DNS C2 channel. [102] |
| S0526 | KGH_SPY | KGH_SPY can exfiltrate collected information from the host to the C2 server. [103] |
| G0094 | Kimsuky | Kimsuky has exfiltrated data over its C2 channel. [104] [105] |
| S0356 | KONNI | KONNI has sent data and files to its C2 server. [106] [107] [108] |
| S1075 | KOPILUWAK | KOPILUWAK has exfiltrated collected data to its C2 via POST requests. [109] |
| S9035 | LAMEHUG | LAMEHUG can exfiltrate collected system information and documents to C2. [110] [111] |
| S1160 | Latrodectus | Latrodectus can exfiltrate encrypted system information to the C2 server. [112] [113] |
| G0032 | Lazarus Group | Lazarus Group has exfiltrated data and files over a C2 channel through its various tools and malware. [114] [115] [116] |
| G0065 | Leviathan | Leviathan has exfiltrated data over its C2 channel. [117] |
| C0049 | Leviathan Australian Intrusions | Leviathan exfiltrated collected data over existing command and control channels during Leviathan Australian Intrusions . [118] |
| S0395 | LightNeuron | LightNeuron exfiltrates data over its email C2 channel. [119] |
| S1185 | LightSpy | To exfiltrate data, LightSpy configures each module to send an obfuscated JSON blob to hardcoded URL endpoints or paths aligned to the module name. [120] |
| S1186 | Line Dancer | Line Dancer exfiltrates collected data via command and control channels. [9] |
| S1188 | Line Runner | Line Runner utilizes HTTP to retrieve and exfiltrate information staged using Line Dancer . [9] |
| S0680 | LitePower | LitePower can send collected data, including screenshots, over its C2 channel. [121] |
| S9020 | LODEINFO | LODEINFO can exfiltrate collected credentials and browser cookies to the C2 server. [122] |
| S0447 | Lokibot | Lokibot has the ability to initiate contact with command and control (C2) to exfiltrate stolen data. [123] |
| G1014 | LuminousMoth | LuminousMoth has used malware that exfiltrates stolen data to its C2 server. [124] |
| S1213 | Lumma Stealer | Lumma Stealer has exfiltrated collected data over existing HTTP and HTTPS C2 channels. [125] [126] |
| S1142 | LunarMail | LunarMail can use email image attachments with embedded data for receiving C2 commands and data exfiltration. [127] |
| S0409 | Machete | Machete 's collected data is exfiltrated over the same channel used for C2. [128] |
| S1016 | MacMa | MacMa exfiltrates data from a supplied path over its C2 channel. [129] |
| S1060 | Mafalda | Mafalda can send network system data and files to its C2 server. [130] |
| S1182 | MagicRAT | MagicRAT exfiltrates data via HTTP over existing command and control channels. [131] |
| S1169 | Mango | Mango can use its HTTP C2 channel for exfiltration. [132] |
| S1156 | Manjusaka | Manjusaka data exfiltration takes place over HTTP channels. [133] |
| S0652 | MarkiRAT | MarkiRAT can exfiltrate locally stored data via its C2. [134] |
| S0459 | MechaFlounder | MechaFlounder has the ability to send the compromised user's account name and hostname within a URL to C2. [135] |
| S1059 | metaMain | metaMain can upload collected files and data to its C2 server. [136] |
| S0455 | Metamorfo | Metamorfo can send the data it collects to the C2 server. [137] |
| S0084 | Mis-Type | Mis-Type has transmitted collected files and data to its C2 server. [138] |
| S0083 | Misdat | Misdat has uploaded files and data to its C2 servers. [138] |
| S1122 | Mispadu | Mispadu can sends the collected financial data to the C2 server. [139] [140] |
| S0079 | MobileOrder | MobileOrder exfiltrates data to its C2 server over the same protocol as C2 communications. [38] |
| S1026 | Mongall | Mongall can upload files and information from a compromised host to its C2 server. [141] |
| S9032 | MuddyViper | MuddyViper has uploaded files to the C2 server. Additionally, MuddyViper has the ability to upload the specified file in chunks with sleep time between each chunk. [142] |
| G0069 | MuddyWater | MuddyWater has used C2 infrastructure to receive exfiltrated data. [143] |
| G0129 | Mustang Panda | Mustang Panda has exfiltrated stolen data and files to its C2 server. [144] [145] [146] |
| S0034 | NETEAGLE | NETEAGLE is capable of reading files over the C2 channel. [15] |
| S1090 | NightClub | NightClub can use SMTP and DNS for file exfiltration and C2. [147] |
| S0385 | njRAT | njRAT has used C2 infrastructure to receive stolen information from the infected machine including screenshots and other system information. [148] [149] |
| S0340 | Octopus | Octopus has uploaded stolen files and data from a victim's machine over its C2 channel. [150] |
| S1170 | ODAgent | ODAgent can use an attacker-controlled OneDrive account to receive C2 commands and to exfiltrate files. [151] |
| S1172 | OilBooster | OilBooster can use an actor-controlled OneDrive account for C2 communication and exfiltration. [151] |
| S0439 | Okrum | Data exfiltration is done by Okrum using the already opened channel with the C2 server. [152] |
| S0264 | OopsIE | OopsIE can upload files from the victim's machine to its C2 server. [153] |
| C0022 | Operation Dream Job | During Operation Dream Job , Lazarus Group exfiltrated data from a compromised host to actor-controlled C2 servers. [154] |
| C0006 | Operation Honeybee | During Operation Honeybee , the threat actors uploaded stolen files to their C2 servers. [155] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors used the XServer backdoor to exfiltrate data. [156] |
| S1017 | OutSteel | OutSteel can upload files from a compromised host over its C2 channel. [157] |
| S1050 | PcShare | PcShare can upload files and information from a compromised host to its C2 servers. [78] |
| S0587 | Penquin | Penquin can execute the command code do_upload to send files to C2. [158] |
| S9014 | PHASEJAM | PHASEJAM has the ability to exfiltrate data from the victim appliance. [159] |
| S1145 | Pikabot | During the initial Pikabot command and control check-in, Pikabot will transmit collected system information encrypted using RC4. [160] |
| S1031 | PingPull | PingPull has the ability to exfiltrate stolen victim data through its C2 channel. [161] |
| S0013 | PlugX | PlugX has exfiltrated stolen data and files to its C2 server. [162] [146] |
| S0428 | PoetRAT | PoetRAT has exfiltrated data over the C2 channel. [163] |
| S1173 | PowerExchange | PowerExchange can exfiltrate files via its email C2 channel. [164] |
| S0441 | PowerShower | PowerShower has used a PowerShell document stealer module to pack and exfiltrate .txt, .pdf, .xls or .doc files smaller than 5MB that were modified during the past two days. [165] |
| S0238 | Proxysvc | Proxysvc performs data exfiltration over the control server channel using a custom protocol. [166] |
| S0078 | Psylo | Psylo exfiltrates data to its C2 server over the same protocol as C2 communications. [38] |
| S0147 | Pteranodon | Pteranodon exfiltrates screenshot files to its C2 server. [80] |
| S0192 | Pupy | Pupy can send screenshots files, keylogger data, files, and recorded audio back to the C2 server. [167] |
| S0650 | QakBot | QakBot can send stolen information to C2 nodes including passwords, accounts, and emails. [168] |
| S1148 | Raccoon Stealer | Raccoon Stealer uses existing HTTP-based command and control channels for exfiltration. [169] [170] [171] |
| S0495 | RDAT | RDAT can exfiltrate data gathered from the infected system via the established Exchange Web Services API C2 channel. [172] |
| S1240 | RedLine Stealer | RedLine Stealer has sent victim data to its C2 server or RedLine panel server. [173] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 uploaded specified files from compromised devices to a remote server. [174] |
| S0375 | Remexi | Remexi performs exfiltration over BITSAdmin , which is also used for the C2 channel. [175] |
| S0496 | REvil | REvil can exfiltrate host and malware information to C2 servers. [176] |
| S0448 | Rising Sun | Rising Sun can send data gathered from the infected machine via HTTP POST request to the C2. [177] |
| S0240 | ROKRAT | ROKRAT can send collected files back over same C2 channel. [178] |
| S1078 | RotaJakiro | RotaJakiro sends device and other collected data back to the C2 using the established C2 channels over TCP. [179] |
| S0085 | S-Type | S-Type has uploaded data and files from a compromised host to its C2 servers. [138] |
| S1210 | Sagerunex | Sagerunex encrypts collected system data then exfiltrates via existing command and control channels. [180] |
| G0034 | Sandworm Team | Sandworm Team has sent system information to its C2 server using HTTP. [181] |
| G1015 | Scattered Spider | Scattered Spider has exfiltrated data from compromised VMware vCenter servers through an established C2 channel using the Teleport remote access tool. [182] |
| S0461 | SDBbot | SDBbot has sent collected data from a compromised host to its C2 servers. [76] |
| S9008 | Shai-Hulud | Shai-Hulud has used POST to exfiltrate secrets from the victim environment to an attacker-controlled URL. [183] [184] [185] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors exfiltrated stolen credentials and internal data over HTTPS to C2 infrastructure. [186] |
| S1019 | Shark | Shark has the ability to upload files from the compromised host over a DNS or HTTP C2 channel. [187] |
| S1089 | SharpDisco | SharpDisco can load a plugin to exfiltrate stolen files to SMB shares also used in C2. [147] |
| S0445 | ShimRatReporter | ShimRatReporter sent generated reports to the C2 via HTTP POST requests. [188] |
| S1178 | ShrinkLocker | ShrinkLocker will exfiltrate victim system information along with the encryption key via an HTTP POST. [189] [190] |
| S0610 | SideTwist | SideTwist has exfiltrated data over its C2 channel. [191] |
| S0692 | SILENTTRINITY | SILENTTRINITY can transfer files from an infected host to the C2 server. [192] |
| S0633 | Sliver | Sliver can exfiltrate files from the victim using the download command. [193] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA has sent system information to a C2 server via HTTP and HTTPS POST requests. [194] |
| S0649 | SMOKEDHAM | SMOKEDHAM has exfiltrated data to its C2 server. [195] |
| S1166 | Solar | Solar can send staged files to C2 for exfiltration. [132] |
| S0615 | SombRAT | SombRAT has uploaded collected data and files from a compromised host to its C2 server. [196] |
| S0543 | Spark | Spark has exfiltrated data over the C2 channel. [197] |
| S1030 | Squirrelwaffle | Squirrelwaffle has exfiltrated victim data using HTTP POST requests to its C2 servers. [198] |
| S1037 | STARWHALE | STARWHALE can exfiltrate collected data to its C2 servers. [199] |
| G0038 | Stealth Falcon | After data is collected by Stealth Falcon malware, it is exfiltrated over the existing C2 channel. [200] |
| S1183 | StrelaStealer | StrelaStealer exfiltrates collected email credentials via HTTP POST to command and control servers. [201] [202] [203] [204] |
| S1034 | StrifeWater | StrifeWater can send data and files from a compromised host to its C2 server. [205] |
| S0491 | StrongPity | StrongPity can exfiltrate collected documents through C2 channels. [206] [207] |
| S0603 | Stuxnet | Stuxnet sends compromised victim information via HTTP. [208] |
| S1042 | SUGARDUMP | SUGARDUMP has sent stolen credentials and other data to its C2 server. [209] |
| S1064 | SVCReady | SVCReady can send collected data in JSON format to its C2 server. [210] |
| S0663 | SysUpdate | SysUpdate has exfiltrated data over its C2 channel. [211] |
| S0467 | TajMahal | TajMahal has the ability to send collected files over its C2. [212] |
| S0595 | ThiefQuest | ThiefQuest exfiltrates targeted file extensions in the /Users/ folder to the command and control server via unencrypted HTTP. Network packets contain a string with two pieces of information: a file path and the contents of the file in a base64 encoded string. [213] [214] |
| S0671 | Tomiris | Tomiris can upload files matching a hardcoded set of extensions, such as .doc, .docx, .pdf, and .rar, to its C2 server. [215] |
| S0678 | Torisma | Torisma can send victim data to an actor-controlled C2 server. [216] |
| S1201 | TRANSLATEXT | TRANSLATEXT has exfiltrated collected credentials to the C2 server. [217] |
| S0266 | TrickBot | TrickBot can send information about the compromised host and upload data to a hardcoded C2 server. [218] [219] |
| S1196 | Troll Stealer | Troll Stealer exfiltrates collected information to its command and control infrastructure. [220] |
| S0386 | Ursnif | Ursnif has used HTTP POSTs to exfil gathered information. [221] [222] [223] |
| S0476 | Valak | Valak has the ability to exfiltrate data over the C2 channel. [224] [225] [226] |
| G1055 | VOID MANTICORE | VOID MANTICORE malware has exfiltrated collected data via Telegram bot C2 channels using encrypted communications. [227] |
| S0670 | WarzoneRAT | WarzoneRAT can send collected victim data to its C2 server. [228] |
| G1035 | Winter Vivern | Winter Vivern delivered a PowerShell script capable of recursively scanning victim machines looking for various file types before exfiltrating identified files via HTTP. [229] |
| G0090 | WIRTE | WIRTE has exfiltrated collected victim data to C2 infrastructure. [11] |
| G0102 | Wizard Spider | Wizard Spider has exfiltrated domain credentials and network enumeration information over command and control (C2) channels. [230] [231] |
| S1065 | Woody RAT | Woody RAT can exfiltrate files from an infected machine to its C2 server. [232] |
| S0658 | XCSSET | XCSSET retrieves files that match the pattern defined in the INAME_QUERY variable within the user's home directory, such as *test.txt , and are below a specific size limit. It then archives the files and exfiltrates the data over its C2 channel. [233] [234] |
| S1248 | XORIndex Loader | XORIndex Loader has exfiltrated victim data using HTTPS POST requests to its C2 servers. [20] |
| S0251 | Zebrocy | Zebrocy has exfiltrated data to the designated C2 server using HTTP POST requests. [235] [236] |
| G0128 | ZIRCONIUM | ZIRCONIUM has exfiltrated files via the Dropbox API C2. [237] |
| S0086 | ZLib | ZLib has sent data and files from a compromised host to its C2 servers. [138] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1057 | Data Loss Prevention | Data loss prevention can detect and block sensitive data being sent over unencrypted protocols. |
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool command and control signatures over time or construct protocols in such a way to avoid detection by common defensive tools. [238] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0348 | Detection Strategy for Exfiltration Over C2 Channel | AN0988 | Identifies suspicious outbound traffic volume mismatches from processes that typically do not generate network activity, particularly over C2 protocols like HTTPS, DNS, or custom TCP/UDP ports, following file or data access. |
| AN0989 | Monitors for processes reading sensitive files then immediately initiating unusual outbound connections or bulk transfer sessions over persistent sockets, particularly with encrypted or binary payloads. |  |  |
| AN0990 | Detects unauthorized applications or scripts accessing sensitive data followed by establishing encrypted outbound communication to rare external destinations or with abnormal byte ratios. |  |  |
| AN0991 | Detects VMs sending outbound traffic through non-standard services or to unknown destinations. Exfiltration over reverse shells tunneled via VMkernel or custom payloads routed via hostd/vpxa. |  |  |

---

## References

- [ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [Kasuya, M. (2020, January 8). Threat Spotlight: Amadey Bot Targets Non-Russian Users. Retrieved July 14, 2022.](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
- [Cybersecurity and Infrastructure Security Agency. (2021, February 21). AppleJeus: Analysis of North Korea’s Cryptocurrency Malware. Retrieved March 1, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [Chen, X., Scott, M., Caselden, D.. (2014, April 26). New Zero-Day Exploit targeting Internet Explorer Versions 9 through 11 Identified in Targeted Attacks. Retrieved January 14, 2016.](https://www.fireeye.com/blog/threat-research/2014/04/new-zero-day-exploit-targeting-internet-explorer-versions-9-through-11-identified-in-targeted-attacks.html)
- [Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)
- [FBI. (2020, September 17). Indicators of Compromise Associated with Rana Intelligence Computing, also known as Advanced Persistent Threat 39, Chafer, Cadelspy, Remexi, and ITG07. Retrieved December 10, 2020.](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)
- [Cisco Talos. (2024, April 24). ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices. Retrieved January 6, 2025.](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
- [Canadian Centre for Cyber Security. (2024, April 24). Cyber Activity Impacting CISCO ASA VPNs. Retrieved January 6, 2025.](https://www.cyber.gc.ca/en/news-events/cyber-activity-impacting-cisco-asa-vpns)
- [Unit 42. (2025, December 11). Hamas-Affiliated Ashen Lepus Targets Middle Eastern Diplomatic Entities With New AshTag Malware Suite. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
- [Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved November 17, 2024.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
- [Savelesky, K., et al. (2019, July 23). ABADBABE 8BADFOOD: Discovering BADHATCH and a Detailed Look at FIN8's Tooling. Retrieved September 8, 2021.](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [Check Point. (2020, November 26). Bandook: Signed & Delivered. Retrieved May 31, 2021.](https://research.checkpoint.com/2020/bandook-signed-delivered/)
- [Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
- [Kirill Boychenko. (2025, July 14). Contagious Interview Campaign Escalates With 67 Malicious npm Packages and New Malware Loader. Retrieved October 19, 2025.](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Unit42. (2024, October 9). Contagious Interview: DPRK Threat Actors Lure Tech Industry Job Seekers to Install New Variants of BeaverTail and InvisibleFerret Malware. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [NHS Digital . (2020, August 20). BLINDINGCAN Remote Access Trojan. Retrieved August 20, 2020.](https://digital.nhs.uk/cyber-alerts/2020/cc-3603)
- [US-CERT. (2020, August 19). MAR-10295134-1.v1 – North Korean Remote Access Trojan: BLINDINGCAN. Retrieved August 19, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
- [Cash, D., Grunzweig, J., Meltzer, M., Adair, S., Lancaster, T. (2021, August 17). North Korean APT InkySquid Infects Victims Using Browser Exploits. Retrieved September 30, 2021.](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
- [CheckPoint Research. (2021, July 1). IndigoZebra APT continues to attack Central Asia with evolving tools. Retrieved September 24, 2021.](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
- [CrowdStrike. (2025, December 4). Unveiling WARP PANDA: A New Sophisticated China-Nexus Adversary. Retrieved April 16, 2026.](https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/)
- [DHS/CISA. (2026, February 11). AR25-338A: BRICKSTORM Backdoor. Retrieved April 16, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
- [Huseyin Can Yuceel. (2025, October 1). BRICKSTORM Malware: UNC5221 Targets Tech and Legal Sectors in the United States. Retrieved April 16, 2026.](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)
- [Matt Lin, Austin Larsen, John Wolfram, Ashley Pearson, Josh Murchie, Lukasz Lamparski, Joseph Pisano, Ryan Hall, Ron Craft, Shawn Crew, Billy Wong, Tyler McLellan. (2024, April 4). Cutting Edge, Part 4: Ivanti Connect Secure VPN Post-Exploitation Lateral Movement Case Studies. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
- [NVISO Incident Response. (2025, April 1). BRICKSTORM Backdoor Analysis: A Persistent Espionage Threat to European Industries. Retrieved April 16, 2026.](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)
- [Resecurity Threat Intelligence & Incident Analysis. (2025, October 22). F5 BIG-IP Source Code Leak Tied to State-Linked Campaigns Using BRICKSTORM Backdoor. Retrieved April 16, 2026.](https://www.resecurity.com/blog/article/f5-big-ip-source-code-leak-tied-to-state-linked-campaigns-using-brickstorm-backdoor)
- [Sarah Yoder, John Wolfram, Ashley Pearson, Doug Bienstock, Josh Madeley, Josh Murchie, Brad Slaybaugh, Matt Lin, Geoff Carstairs, Austin Larsen. (2025, September 24). Another BRICKSTORM: Stealthy Backdoor Enabling Espionage into Tech and Legal Sectors. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
- [Stolyarov, V. (2022, March 17). Exposing initial access broker with ties to Conti. Retrieved August 18, 2022.](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Falcone, R. and Miller-Osborn, J.. (2016, January 24). Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists. Retrieved February 10, 2016.](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
- [Falcone, R., Lee, B. (2018, November 20). Sofacy Continues Global Attacks and Wheels Out New ‘Cannon’ Trojan. Retrieved November 26, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
- [Giuliani, M., Allievi, A. (2011, February 28). Carberp - a modular information stealing trojan. Retrieved September 12, 2024.](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
- [Trusteer Fraud Prevention Center. (2010, October 7). Carberp Under the Hood of Carberp: Malware & Configuration Analysis. Retrieved July 15, 2020.](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Lunghi, D. (2021, August 17). Confucius Uses Pegasus Spyware-related Lures to Target Pakistani Military. Retrieved December 26, 2021.](https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html)
- [Aleksandar Milenkoski, Sreekar Madabushi, Kenneth Kinion. (2025, September 4). Contagious Interview | North Korean Threat Actors Reveal Plans and Ops by Abusing Cyber Intel Platforms. Retrieved October 20, 2025.](https://www.sentinelone.com/labs/contagious-interview-threat-actors-scout-cyber-intel-platforms-reveal-plans-and-ops/)
- [eSentire Threat Response Unit (TRU). (2024, November 14). Bored BeaverTail & InvisibleFerret Yacht Club – A Lazarus Lure Pt.2. Retrieved October 17, 2025.](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
- [Insikt Group. (2025, February 13). Inside the Scam: North Korea’s IT Worker Threat. Retrieved October 17, 2025.](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)
- [Kirill Boychenko. (2025, April 4). Lazarus Expands Malicious npm Campaign: 11 New Packages Add Malware Loaders and Bitbucket Payloads. Retrieved October 20, 2025.](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Ryan Sherstobitoff. (2024, October 29). Inside a North Korean Phishing Operation Targeting DevOps Employees. Retrieved October 20, 2025.](https://securityscorecard.com/blog/inside-a-north-korean-phishing-operation-targeting-devops-employees/)
- [Microsoft. (2022, June 2). Exposing POLONIUM activity and infrastructure targeting Israeli organizations. Retrieved July 1, 2022.](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
- [N. Baisini. (2022, July 13). Transparent Tribe begins targeting education sector in latest campaign. Retrieved September 22, 2022.](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
- [Faou, M. (2020, December 2). Turla Crutch: Keeping the “back door” open. Retrieved December 4, 2020.](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
- [Kohler, A. and Lopez, C. (2024, April 30). Malware: Cuckoo Behaves Like Cross Between Infostealer and Spyware. Retrieved August 20, 2024.](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
- [PwC Threat Intelligence. (2023, October 25). Yellow Liderc ships its scripts and delivers IMAPLoader malware. Retrieved August 14, 2024.](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
- [NCSC. (2022, February 23). Cyclops Blink Malware Analysis Report. Retrieved March 3, 2022.](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Shivtarkar, N. and Kumar, A. (2022, June 9). Lyceum .NET DNS Backdoor. Retrieved June 23, 2022.](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)
- [Fishbein, N., Kajiloti, M.. (2020, July 28). Watch Your Containers: Doki Infecting Docker Servers in the Cloud. Retrieved March 30, 2021.](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
- [NSA/FBI. (2020, August). Russian GRU 85th GTsSS Deploys Previously Undisclosed Drovorub Malware. Retrieved August 25, 2020.](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [GReAT. (2019, April 10). Gaza Cybergang Group1, operation SneakyPastes. Retrieved May 13, 2020.](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
- [hasherezade. (2015, November 4). A Technical Look At Dyreza. Retrieved June 15, 2020.](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
- [Bilodeau, O., Bureau, M., Calvet, J., Dorais-Joncas, A., Léveillé, M., Vanheuverzwijn, B. (2014, March 18). Operation Windigo – the vivisection of a large Linux server‑side credential‑stealing malware campaign. Retrieved February 10, 2021.](https://www.welivesecurity.com/2014/03/18/operation-windigo-the-vivisection-of-a-large-linux-server-side-credential-stealing-malware-campaign/)
- [Marc-Etienne M.Léveillé. (2024, May 1). Ebury is alive but unseen. Retrieved May 21, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/ebury-is-alive-but-unseen.pdf)
- [Trend Micro. (2019, January 16). Exploring Emotet's Activities . Retrieved March 25, 2019.](https://documents.trendmicro.com/assets/white_papers/ExploringEmotetsActivities_Final.pdf)
- [Binary Defense. (n.d.). Emotet Evolves With new Wi-Fi Spreader. Retrieved September 8, 2023.](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Adamitis, D. et al. (2019, June 4). It's alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign. Retrieved May 11, 2020.](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
- [Adamitis, D. (2020, May 6). Phantom in the Command Shell. Retrieved November 17, 2024.](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [Ramin Nafisi. (2021, September 27). FoggyWeb: Targeted NOBELIUM malware leads to persistent backdoor. Retrieved October 4, 2021.](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Cybereason Nocturnus. (2019, June 25). Operation Soft Cell: A Worldwide Campaign Against Telecommunications Providers. Retrieved July 18, 2019.](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)
- [Kasza, A. and Reichel, D. (2017, February 27). The Gamaredon Group Toolset Evolution. Retrieved March 1, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Threat Hunter Team, Symantec and Carbon Black. (2025, April 10). Shuckworm Targets Foreign Military Mission Based in Ukraine. Retrieved July 23, 2025.](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)
- [Trustwave SpiderLabs. (2020, June 25). The Golden Tax Department and Emergence of GoldenSpy Malware. Retrieved July 23, 2020.](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [Smith, L., Leathery, J., Read, B. (2021, March 4). New SUNSHUTTLE Second-Stage Backdoor Uncovered Targeting U.S.-Based Entity; Possible Connection to UNC2452. Retrieved March 12, 2021.](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [Priego, A. (2021, July). THE BROTHERS GRIM: THE REVERSING TALE OF GRIMAGENT MALWARE USED BY RYUK. Retrieved September 19, 2024.](https://www.group-ib.com/blog/grimagent/)
- [Patil, S. and Williams, M.. (2019, June 5). Government Sector in Central Asia Targeted With New HAWKBALL Backdoor Delivered via Microsoft Office Vulnerabilities. Retrieved June 20, 2019.](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)
- [Singh, S. Singh, A. (2020, June 11). The Return on the Higaisa APT. Retrieved March 2, 2021.](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)
- [CISA. (2022, September 23). AA22-264A Iranian State Actors Conduct Cyber Operations Against the Government of Albania. Retrieved August 6, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [Knight, S.. (2020, April 16). VMware Carbon Black TAU Threat Analysis: The Evolution of Lazarus. Retrieved May 1, 2020.](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
- [Alexndru-Cristian Bardas. (2025, October 30). DPRK’s Playbook: Kimsuky’s HttpTroy and Lazarus’s New BLINDINGCAN Variant. Retrieved April 8, 2026.](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)
- [CrowdStrike. (2022, May). ICEAPPLE: A NOVEL INTERNET INFORMATION SERVICES (IIS) POST-EXPLOITATION FRAMEWORK. Retrieved June 27, 2022.](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
- [QiAnXin Threat Intelligence Center. (2019, February 18). APT-C-36: Continuous Attacks Targeting Colombian Government Institutions and Corporations. Retrieved May 5, 2020.](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
- [Anton Cherepanov. (2017, June 12). Win32/Industroyer: A new threat for industrial controls systems. Retrieved December 18, 2020.](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
- [Seongsu Park. (2024, November 4). From Pyongyang to Your Payroll: The Rise of North Korean Remote Workers in the West. Retrieved October 17, 2025.](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Dahan, A. et al. (2020, November 2). Back to the Future: Inside the Kimsuky KGH Spyware Suite. Retrieved November 6, 2020.](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
- [Tarakanov , D.. (2013, September 11). The “Kimsuky” Operation: A North Korean APT?. Retrieved August 13, 2019.](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [Rascagneres, P. (2017, May 03). KONNI: A Malware Under The Radar For Years. Retrieved November 5, 2018.](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
- [Threat Intelligence Team. (2021, August 23). New variant of Konni malware used in campaign targetting Russia. Retrieved January 5, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
- [Santos, R. (2022, January 26). KONNI evolves into stealthier RAT. Retrieved April 13, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/01/konni-evolves-into-stealthier-rat/)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Conteras, T., Splunk Research Team. (2025, September 25). From Prompt to Payload: LAMEHUG’s LLM-Driven Cyber Intrusion. Retrieved April 21, 2026.](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
- [Google Threat Intelligence Group. (2025, November 5). GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools. Retrieved March 31, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
- [Proofpoint Threat Research and Team Cymru S2 Threat Research. (2024, April 4). Latrodectus: This Spider Bytes Like Ice . Retrieved May 31, 2024.](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
- [Batista, J. (2024, June 17). Latrodectus, are you coming back?. Retrieved September 13, 2024.](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)
- [Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)
- [CISA. (2021, July 19). (AA21-200A) Joint Cybersecurity Advisory – Tactics, Techniques, and Procedures of Indicted APT40 Actors Associated with China’s MSS Hainan State Security Department. Retrieved August 12, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)
- [CISA et al. (2024, July 8). People’s Republic of China (PRC) Ministry of State Security APT40 Tradecraft in Action. Retrieved February 3, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a)
- [Faou, M. (2019, May). Turla LightNeuron: One email away from remote code execution. Retrieved June 24, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
- [Stuart Ashenbrenner, Alden Schmidt. (2024, April 25). LightSpy Malware Variant Targeting macOS. Retrieved January 3, 2025.](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
- [Yamout, M. (2021, November 29). WIRTE’s campaign in the Middle East ‘living off the land’ since at least 2019. Retrieved February 1, 2022.](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
- [Breitenbacher, D. (2022, December 14). Unmasking MirrorFace: Operation LiberalFace targeting Japanese political entities. Retrieved April 17, 2026.](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
- [Kazem, M. (2019, November 25). Trojan:W32/Lokibot. Retrieved May 15, 2020.](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)
- [Lechtik, M, and etl. (2021, July 14). LuminousMoth APT: Sweeping attacks for the chosen few. Retrieved October 20, 2022.](https://securelist.com/apt-luminousmoth/103332/)
- [Vishwajeet Kumar, Qualys. (2024, October 20). Unmasking Lumma Stealer: Analyzing Deceptive Tactics with Fake CAPTCHA. Retrieved March 22, 2025.](https://blog.qualys.com/vulnerabilities-threat-research/2024/10/20/unmasking-lumma-stealer-analyzing-deceptive-tactics-with-fake-captcha)
- [Cara Lin, Fortinet. (2024, January 8). Deceptive Cracked Software Spreads Lumma Variant on YouTube. Retrieved March 22, 2025.](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [Asheer Malhotra, Vitor Ventura & Jungsoo An, Cisco Talos. (2022, September 7). MagicRAT: Lazarus’ latest gateway into victim networks. Retrieved December 30, 2024.](https://blog.talosintelligence.com/lazarus-magicrat/)
- [Hromcova, Z. and Burgher, A. (2023, September 21). OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes. Retrieved November 21, 2024.](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
- [Asheer Malhotra & Vitor Ventura. (2022, August 2). Manjusaka: A Chinese sibling of Sliver and Cobalt Strike. Retrieved September 4, 2024.](https://blog.talosintelligence.com/manjusaka-offensive-framework/)
- [GReAT. (2021, June 16). Ferocious Kitten: 6 Years of Covert Surveillance in Iran. Retrieved September 22, 2021.](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
- [Falcone, R. (2019, March 4). New Python-Based Payload MechaFlounder Used by Chafer. Retrieved May 27, 2020.](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [ESET Research. (2019, October 3). Casbaneiro: peculiarities of this banking Trojan that affects Brazil and Mexico. Retrieved September 23, 2021.](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [ESET Security. (2019, November 19). Mispadu: Advertisement for a discounted Unhappy Meal. Retrieved March 13, 2024.](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
- [SCILabs. (2021, December 23). Cyber Threat Profile Malteiro. Retrieved March 13, 2024.](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [ESET Research. (2025, December 2). MuddyWater: Snakes by the riverbank. Retrieved February 17, 2026.](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
- [Reaqta. (2017, November 22). A dive into MuddyWater APT targeting Middle-East. Retrieved May 18, 2020.](https://reaqta.com/2017/11/muddywater-apt-targeting-middle-east/)
- [Asheer Malhotra, Jungsoo An, Kendall Mc. (2022, May 5). Mustang Panda deploys a new wave of malware targeting Europe. Retrieved August 4, 2025.](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
- [EclecticIQ Threat Research Team. (2023, February 2). Mustang Panda APT Group Uses European Commission-Themed Lure to Deliver PlugX Malware. Retrieved September 9, 2025.](https://blog.eclecticiq.com/mustang-panda-apt-group-uses-european-commission-themed-lure-to-deliver-plugx-malware)
- [Secureworks Counter Threat Unit Research Team. (2022, April 27). BRONZE PRESIDENT Targets Russian Speakers with Updated PlugX. Retrieved September 9, 2025.](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Pascual, C. (2018, November 27). AutoIt-Compiled Worm Affecting Removable Media Delivers Fileless Version of BLADABINDI/njRAT Backdoor. Retrieved June 4, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
- [Global Research & Analysis Team, Kaspersky. (2024, August 19). BlindEagle flying high in Latin America. Retrieved April 16, 2026.](https://securelist.com/blindeagle-apt/113414/)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 15). Octopus-infested seas of Central Asia. Retrieved November 14, 2018.](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
- [Hromcova, Z. and Burgher, A. (2023, December 14). OilRig’s persistent attacks using cloud service-powered downloaders. Retrieved November 26, 2024.](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
- [Hromcova, Z. (2019, July). OKRUM AND KETRICAN: AN OVERVIEW OF RECENT KE3CHANG GROUP ACTIVITY. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
- [Lee, B., Falcone, R. (2018, February 23). OopsIE! OilRig Uses ThreeDollars to Deliver New Trojan. Retrieved July 16, 2018.](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-uncovers-operation-honeybee-malicious-document-campaign-targeting-humanitarian-aid-groups/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Leonardo. (2020, May 29). MALWARE TECHNICAL INSIGHT TURLA “Penquin_x64”. Retrieved March 11, 2021.](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
- [John Wolfram, Josh Murchie, Matt Lin, Daniel Ainsworth, Robert Wallace, Dimiter Andonov, Dhanesh Kizhakkinan, Jacob Thompson. (2025, January 8). Ivanti Connect Secure VPN Targeted in New Zero-Day Exploitation. Retrieved April 14, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
- [Daniel Stepanic & Salim Bitam. (2024, February 23). PIKABOT, I choose you!. Retrieved July 12, 2024.](https://www.elastic.co/security-labs/pikabot-i-choose-you)
- [Unit 42. (2022, June 13). GALLIUM Expands Targeting Across Telecommunications, Government and Finance Sectors With New PingPull Tool. Retrieved August 7, 2022.](https://unit42.paloaltonetworks.com/pingpull-gallium/)
- [DOJ. (2024, December 20). Mag. No. 24-mj-1387 AFFIDAVIT IN SUPPORT OF AN APPLICATION FOR A NINTH SEARCH AND SEIZURE WARRANT- IN THE MATTER OF THE SEARCH AND SEIZURE OF COMPUTERS IN THE UNITED STATES INFECTED WITH PLUGX MALWARE . Retrieved September 9, 2025.](https://www.justice.gov/archives/opa/media/1384136/dl)
- [Mercer, W. Rascagneres, P. Ventura, V. (2020, October 6). PoetRAT: Malware targeting public and private sector in Azerbaijan evolves . Retrieved April 9, 2021.](https://blog.talosintelligence.com/2020/10/poetrat-update.html)
- [Symantec Threat Hunter Team. (2023, October 19). Crambus: New Campaign Targets Middle Eastern Government. Retrieved November 27, 2024.](https://www.security.com/threat-intelligence/crambus-middle-east-government)
- [GReAT. (2019, August 12). Recent Cloud Atlas activity. Retrieved May 8, 2020.](https://securelist.com/recent-cloud-atlas-activity/92016/)
- [Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
- [Nicolas Verdier. (n.d.). Retrieved January 29, 2018.](https://github.com/n1nj4sec/pupy)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [S2W TALON. (2022, June 16). Raccoon Stealer is Back with a New Version. Retrieved August 1, 2024.](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
- [Quentin Bourgue, Pierre le Bourhis, & Sekoia TDR. (2022, June 28). Raccoon Stealer v2 - Part 1: The return of the dead. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Falcone, R. (2020, July 22). OilRig Targets Middle Eastern Telecommunications Organization and Adds Novel C2 Channel with Steganography to Its Inventory. Retrieved July 28, 2020.](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
- [Proofpoint Threat Insight Team, Jeremy H, Axel F. (2020, March 16). New Redline Password Stealer Malware. Retrieved September 17, 2025.](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
- [Lamparski, L. et al. (2025, March 11). Ghost in the Router: China-Nexus Espionage Actor UNC3886 Targets Juniper Routers. Retrieved June 24, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers)
- [Legezo, D. (2019, January 30). Chafer used Remexi malware to spy on Iran-based foreign diplomatic entities. Retrieved April 17, 2019.](https://securelist.com/chafer-used-remexi-malware/89538/)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [Mercer, W., Rascagneres, P. (2017, April 03). Introducing ROKRAT. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)
- [Alex Turing, Hui Wang. (2021, April 28). RotaJakiro: A long live secret backdoor with 0 VT detection. Retrieved June 14, 2023.](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [Cherepanov, A.. (2016, December 13). The rise of TeleBots: Analyzing disruptive KillDisk attacks. Retrieved June 10, 2020.](https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/)
- [Mandiant Incident Response. (2025, July 23). From Help Desk to Hypervisor: Defending Your VMware vSphere Estate from UNC3944. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)
- [Charlie Eriksen. (2025, September 16). S1ngularity/nx attackers strike again. Retrieved April 9, 2026.](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
- [Justin Moore. (2025, November 25). "Shai-Hulud" Worm Compromises npm Ecosystem in Supply Chain Attack (Updated November 26). Retrieved April 9, 2026.](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
- [Merav Bar, Rami McCarthy, Barak Sharoni. (2025, September 16). Shai-Hulud: Ongoing Package Supply Chain Worm Delivering Data-Stealing Malware. Retrieved April 9, 2026.](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)
- [Microsoft Threat Intelligence. (2025, July 22). Disrupting active exploitation of on-premises SharePoint vulnerabilities. Retrieved October 15, 2025.](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/#storm-2603)
- [ClearSky Cyber Security . (2021, August). New Iranian Espionage Campaign By “Siamesekitten” - Lyceum. Retrieved June 6, 2022.](https://www.clearskysec.com/siamesekitten/)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Cristian Souza, Eduardo Ovalle, Ashley Muñoz, & Christopher Zachor. (2024, May 23). ShrinkLocker: Turning BitLocker into ransomware. Retrieved December 7, 2024.](https://securelist.com/ransomware-abuses-bitlocker/112643/)
- [Splunk Threat Research Team , Teoderick Contreras. (2024, September 5). ShrinkLocker Malware: Abusing BitLocker to Lock Your Data. Retrieved December 7, 2024.](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [BishopFox. (n.d.). Sliver Download. Retrieved September 16, 2021.](https://github.com/BishopFox/sliver/blob/7489c69962b52b09ed377d73d142266564845297/client/command/filesystem/download.go)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [FireEye. (2021, June 16). Smoking Out a DARKSIDE Affiliate’s Supply Chain Software Compromise. Retrieved September 22, 2021.](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [Falcone, R., et al. (2020, March 3). Molerats Delivers Spark Backdoor to Government and Telecommunications Organizations. Retrieved December 14, 2020.](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)
- [Kumar, A., Stone-Gross, Brett. (2021, September 28). Squirrelwaffle: New Loader Delivering Cobalt Strike. Retrieved August 9, 2022.](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
- [FBI, CISA, CNMF, NCSC-UK. (2022, February 24). Iranian Government-Sponsored Actors Conduct Cyber Operations Against Global Government and Commercial Networks. Retrieved September 27, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
- [Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.](https://citizenlab.org/2016/05/stealth-falcon/)
- [DCSO CyTec Blog. (2022, November 8). #ShortAndMalicious: StrelaStealer aims for mail credentials. Retrieved December 31, 2024.](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)
- [Benjamin Chang, Goutam Tripathy, Pranay Kumar Chhaparwal, Anmol Maurya & Vishwa Thothathri, Palo Alto Networks. (2024, March 22). Large-Scale StrelaStealer Campaign in Early 2024. Retrieved December 31, 2024.](https://unit42.paloaltonetworks.com/strelastealer-campaign/)
- [Fortgale. (2023, September 18). StrelaStealer Malware Analysis. Retrieved December 31, 2024.](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)
- [Golo Mühr, Joe Fasulo & Charlotte Hammond, IBM X-Force. (2024, November 12). Strela Stealer: Today’s invoice is tomorrow’s phish. Retrieved December 31, 2024.](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
- [Cybereason Nocturnus. (2022, February 1). StrifeWater RAT: Iranian APT Moses Staff Adds New Trojan to Ransomware Operations. Retrieved August 15, 2022.](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
- [Mercer, W. et al. (2020, June 29). PROMETHIUM extends global reach with StrongPity3 APT. Retrieved July 20, 2020.](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
- [Tudorica, R. et al. (2020, June 30). StrongPity APT - Revealing Trojanized Tools, Working Hours and Infrastructure. Retrieved July 20, 2020.](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [Mandiant Israel Research Team. (2022, August 17). Suspected Iranian Actor Targeting Israeli Shipping, Healthcare, Government and Energy Sectors. Retrieved September 21, 2022.](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [Daniel Lunghi. (2023, March 1). Iron Tiger’s SysUpdate Reappears, Adds Linux Targeting. Retrieved March 20, 2023.](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Patrick Wardle. (2020, July 3). OSX.EvilQuest Uncovered part ii: insidious capabilities. Retrieved March 21, 2021.](https://objective-see.com/blog/blog_0x60.html)
- [Thomas Reed. (2020, July 7). Mac ThiefQuest malware may not be ransomware after all. Retrieved March 22, 2021.](https://blog.malwarebytes.com/mac/2020/07/mac-thiefquest-malware-may-not-be-ransomware-after-all/)
- [Kwiatkoswki, I. and Delcher, P. (2021, September 29). DarkHalo After SolarWinds: the Tomiris connection. Retrieved December 27, 2021.](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/)
- [Beek, C. (2020, November 5). Operation North Star: Behind The Scenes. Retrieved December 20, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
- [Park, S. (2024, June 27). Kimsuky deploys TRANSLATEXT to target South Korean academia. Retrieved October 14, 2024.](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [Radu Tudorica. (2021, July 12). A Fresh Look at Trickbot’s Ever-Improving VNC Module. Retrieved September 28, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/399/Bitdefender-PR-Whitepaper-Trickbot-creat5515-en-EN.pdf)
- [Jiho Kim & Sebin Lee, S2W. (2024, February 7). Kimsuky disguised as a Korean company signed with a valid certificate to distribute Troll Stealer (English ver.). Retrieved January 17, 2025.](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
- [Caragay, R. (2015, March 26). URSNIF: The Multifaceted Malware. Retrieved June 5, 2019.](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
- [Vaish, A. & Nemes, S. (2017, November 28). Newly Observed Ursnif Variant Employs Malicious TLS Callback Technique to Achieve Process Injection. Retrieved June 5, 2019.](https://www.fireeye.com/blog/threat-research/2017/11/ursnif-variant-malicious-tls-callback-technique.html)
- [Proofpoint Staff. (2016, August 25). Nightmare on Tor Street: Ursnif variant Dreambot adds Tor functionality. Retrieved June 5, 2019.](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)
- [Salem, E. et al. (2020, May 28). VALAK: MORE THAN MEETS THE EYE . Retrieved June 19, 2020.](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
- [Duncan, B. (2020, July 24). Evolution of Valak, from Its Beginnings to Mass Distribution. Retrieved August 31, 2020.](https://unit42.paloaltonetworks.com/valak-evolution/)
- [Reaves, J. and Platt, J. (2020, June). Valak Malware and the Connection to Gozi Loader ConfCrew. Retrieved August 31, 2020.](https://assets.sentinelone.com/labs/sentinel-one-valak-i)
- [DomainTools Investigations. (2026, April 6). Handala: MOIS Linked Cyber Influence Ecosystem Threat Intelligence Assessment. Retrieved April 20, 2026.](https://dti.domaintools.com/research/handala-mois-linked-cyber-influence-ecosystem-threat-intelligence-assessment)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [CERT-UA. (2023, February 1). UAC-0114 aka Winter Vivern to target Ukrainian and Polish GOV entities (CERT-UA#5909). Retrieved July 29, 2024.](https://cert.gov.ua/article/3761104)
- [John, E. and Carvey, H. (2019, May 30). Unraveling the Spiderweb: Timelining ATT&CK Artifacts Used by GRIM SPIDER. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Mac Threat Response, Mobile Research Team. (2020, August 13). The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSS Backdoor Planting in Safari, and Leverages Two Zero-day Exploits. Retrieved October 5, 2021.](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
- [Microsoft Threat Intelligence. (2025, March 11). New XCSSET malware adds new obfuscation, persistence techniques to infect Xcode projects. Retrieved April 2, 2025.](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)
- [Accenture Security. (2018, November 29). SNAKEMACKEREL. Retrieved April 15, 2019.](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
- [CISA. (2020, October 29). Malware Analysis Report (AR20-303B). Retrieved December 9, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
- [Singh, S. and Antil, S. (2020, October 27). APT-31 Leverages COVID-19 Vaccine Theme and Abuses Legitimate Online Services. Retrieved March 24, 2021.](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)
- [Gardiner, J., Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Lockbit]] [related_actor:: [[Lockbit]]]
- 🦠 **Tooling Capability Integration:** Executed via malware family [[Lumma Stealer]] [related_malware:: [[Lumma Stealer]]]

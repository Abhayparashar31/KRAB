# System Owner/User Discovery

## Description

Adversaries may attempt to identify the primary user, currently logged in user, set of users that commonly uses a system, or whether a user is actively using the system. They may do this, for example, by retrieving account usernames or by using OS Credential Dumping . The information may be collected in a number of different ways using other Discovery techniques, because user and username details are prevalent throughout a system and include running process ownership, file/directory ownership, session information, and system logs. Adversaries may use the information from System Owner/User Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Various utilities and commands may acquire this information, including whoami . In macOS and Linux, the currently logged in user can be identified with w and who . On macOS the dscl . list /Users | grep -v '_' command can also be used to enumerate user accounts. Environment variables, such as %USERNAME% and $USER , may also be used to access this information.

On network devices, Network Device CLI commands such as show users and show ssh can be used to display users currently logged into the device. [1] [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1028 | Action RAT | Action RAT has the ability to collect the username from an infected host. [3] |
| S0331 | Agent Tesla | Agent Tesla can collect the username from the victim’s machine. [4] [5] [6] |
| S0092 | Agent.btz | Agent.btz obtains the victim username and saves it to a file. [7] |
| S1025 | Amadey | Amadey has collected the user name from a compromised host using GetUserNameA . [8] |
| G0073 | APT19 | APT19 used an HTTP malware variant and a Port 22 malware variant to collect the victim’s username. [9] |
| G0022 | APT3 | An APT3 downloader uses the Windows command "cmd.exe" /C whoami to verify that it is running with the elevated privileges of "System." [10] |
| G0050 | APT32 | APT32 collected the victim's username and executed the whoami command on the victim's machine. APT32 executed shellcode to collect the username on the victim's machine. [11] [12] [13] |
| G0067 | APT37 | APT37 identifies the victim username. [14] |
| G0082 | APT38 | APT38 has identified primary users, currently logged in users, sets of users that commonly use a system, or inactive users. [15] |
| G0087 | APT39 | APT39 used Remexi to collect usernames from the system. [16] |
| G0096 | APT41 | APT41 has executed whoami commands, including using the WMIEXEC utility to execute this on remote machines. [17] [18] |
| G0143 | Aquatic Panda | Aquatic Panda gathers information on recently logged-in users on victim devices. [19] |
| S0456 | Aria-body | Aria-body has the ability to identify the username on a compromised host. [20] |
| S1087 | AsyncRAT | AsyncRAT can check if the current user of a compromised system is an administrator. [21] |
| S1029 | AuTo Stealer | AuTo Stealer has the ability to collect the username from an infected host. [3] |
| S0344 | Azorult | Azorult can collect the username from the victim’s machine. [22] |
| S0414 | BabyShark | BabyShark has executed the whoami command. [23] |
| S0093 | Backdoor.Oldrea | Backdoor.Oldrea collects the current username from the victim. [24] |
| S1081 | BADHATCH | BADHATCH can obtain logged user information from a compromised machine and can execute the command whoami.exe . [25] |
| S0534 | Bazar | Bazar can identify the username of the infected user. [26] |
| S0017 | BISCUIT | BISCUIT has a command to gather the username from the system. [27] |
| S1068 | BlackCat | BlackCat can utilize net use commands to discover the user name on a compromised host. [28] |
| S0521 | BloodHound | BloodHound can collect information on user sessions. [29] |
| S0657 | BLUELIGHT | BLUELIGHT can collect the username on a compromised host. [30] |
| S0486 | Bonadan | Bonadan has discovered the username of the user running the backdoor. [31] |
| S1226 | BOOKWORM | BOOKWORM has obtained the username from an infected host. [32] |
| S0635 | BoomBox | BoomBox can enumerate the username on a compromised host. [33] |
| S1039 | Bumblebee | Bumblebee has the ability to identify the user name. [34] |
| C0017 | C0017 | During C0017 , APT41 used whoami to gather information from victim machines. [35] |
| C0018 | C0018 | During C0018 , the threat actors collected whoami information via PowerShell scripts. [36] |
| S0351 | Cannon | Cannon can gather the username from the system. [37] |
| S0348 | Cardinal RAT | Cardinal RAT can collect the username from a victim machine. [38] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell can obtain a list of user accounts from a victim's machine. [39] |
| S0631 | Chaes | Chaes has collected the username and UID from the infected machine. [40] |
| G0114 | Chimera | Chimera has used the quser command to show currently logged on users. [41] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP has included the victim's computer name and username in C2 messages sent to actor-owned infrastructure. [42] |
| S0667 | Chrommme | Chrommme can retrieve the username from a targeted system. [43] |
| S0660 | Clambling | Clambling can identify the username on a compromised host. [44] [45] |
| S1024 | CreepySnail | CreepySnail can execute getUsername on compromised systems. [46] |
| S0115 | Crimson | Crimson can identify the user on a targeted system. [47] [48] [49] |
| S0498 | Cryptoistic | Cryptoistic can gather data on the user of a compromised host. [50] |
| S1153 | Cuckoo Stealer | Cuckoo Stealer can discover and send the username from a compromised host to C2. [51] |
| S0334 | DarkComet | DarkComet gathers the username from the victim’s machine. [52] |
| S0673 | DarkWatchman | DarkWatchman has collected the username from a victim machine. [53] |
| S0354 | Denis | Denis enumerates and collects the username from the victim’s machine. [54] [13] |
| S0021 | Derusbi | A Linux version of Derusbi checks if the victim user ID is anything other than zero (normally used for root), and the malware will not execute if it does not have root privileges. Derusbi also gathers the username of the victim. [55] |
| S0659 | Diavol | Diavol can collect the username from a compromised host. [56] |
| S1021 | DnsSystem | DnsSystem can use the Windows user name to create a unique identification for infected users and systems. [57] |
| S0186 | DownPaper | DownPaper collects the victim username and sends it to the C2 server. [58] |
| G0035 | Dragonfly | Dragonfly used the command query user on victim hosts. [59] |
| S0694 | DRATzarus | DRATzarus can obtain a list of users from an infected machine. [60] |
| S0024 | Dyre | Dyre has the ability to identify the users on a compromised host. [61] |
| G1006 | Earth Lusca | Earth Lusca collected information on user accounts via the whoami command. [62] |
| S0554 | Egregor | Egregor has used tools to gather information about users. [63] |
| S0367 | Emotet | Emotet has enumerated all users connected to network shares. |
| S0363 | Empire | Empire can enumerate the username on targeted hosts. [64] |
| S0091 | Epic | Epic collects the user name from the victim’s machine. [65] |
| S0568 | EVILNUM | EVILNUM can obtain the username from the victim's machine. [66] |
| S0401 | Exaramel for Linux | Exaramel for Linux can run whoami to identify the system owner. [67] |
| S0569 | Explosive | Explosive has collected the username from the infected host. [68] |
| S0171 | Felismus | Felismus collects the current username and sends it to the C2 server. [69] |
| S0267 | FELIXROOT | FELIXROOT collects the username from the victim’s machine. [70] [71] |
| G0051 | FIN10 | FIN10 has used Meterpreter to enumerate users on remote systems. [72] |
| G0046 | FIN7 | FIN7 has used the command cmd.exe /C quser to collect user session information. [73] |
| G0061 | FIN8 | FIN8 has executed the command quser to display the session details of a compromised machine. [74] |
| S0696 | Flagpro | Flagpro has been used to run the whoami command on the system. [75] |
| S0381 | FlawedAmmyy | FlawedAmmyy enumerates the current user during the initial infection. [76] [77] |
| C0001 | Frankenstein | During Frankenstein , the threat actors used Empire to enumerate hosts and gather username, machine name, and administrative permissions information. [64] |
| S1044 | FunnyDream | FunnyDream has the ability to gather user information from the targeted system using whoami/upn&whoami/fqdn&whoami/logonid&whoami/all . [78] |
| G0093 | GALLIUM | GALLIUM used whoami and query user to obtain information about the victim user. [79] |
| G0047 | Gamaredon Group | A Gamaredon Group file stealer can gather the victim's username to send to a C2 server. [80] |
| S0168 | Gazer | Gazer obtains the current user's security identifier. [81] |
| S0666 | Gelsemium | Gelsemium has the ability to distinguish between a standard user and an administrator on a compromised host. [43] |
| S0460 | Get2 | Get2 has the ability to identify the current username of an infected host. [82] |
| S0249 | Gold Dragon | Gold Dragon collects the endpoint victim's username and uses it as a basis for downloading additional components from the C2 server. [83] |
| S0477 | Goopy | Goopy has the ability to enumerate the infected system's user name. [13] |
| S0531 | Grandoreiro | Grandoreiro can collect the username from the victim's machine. [84] |
| S0237 | GravityRAT | GravityRAT collects the victim username along with other account information (account type, description, full name, SID and status). [85] |
| S0632 | GrimAgent | GrimAgent can identify the user id on a target machine. [86] |
| G0125 | HAFNIUM | HAFNIUM has used whoami to gather user information. [87] |
| S0214 | HAPPYWORK | can collect the victim user name. [88] |
| S1229 | Havoc | Havoc can trigger exection of whoami on the target host to display the current user. [89] [90] |
| S0391 | HAWKBALL | HAWKBALL can collect the user name of the system. [91] |
| G1001 | HEXANE | HEXANE has run whoami on compromised machines to identify the current user. [92] |
| S1249 | HexEval Loader | HexEval Loader has collected the username from the victim host. [93] |
| S9023 | HiddenFace | HiddenFace can collect the username associated with the compromised host. [94] |
| S0431 | HotCroissant | HotCroissant has the ability to collect the username on the infected host. [95] |
| S1245 | InvisibleFerret | InvisibleFerret has identified the user’s UUID and username through the "pay" module. [96] [97] [98] |
| S0260 | InvisiMole | InvisiMole lists local users and session information. [99] |
| S9029 | IronWind | IronWind can enumerate the username on victim's systems. [100] |
| S0015 | Ixeshe | Ixeshe collects the username from the victim’s machine. [101] |
| S0201 | JPIN | JPIN can obtain the victim user name. [102] |
| S0265 | Kazuar | Kazuar gathers information on users. [103] |
| G0004 | Ke3chang | Ke3chang has used implants capable of collecting the signed-in username. [104] |
| G0094 | Kimsuky | Kimsuky has gathered the identity of the user by querying System.Security.Principal namespace using the GetCurrent() method. [105] |
| S0250 | Koadic | Koadic can identify logged in users across the domain and views user sessions. [106] [107] |
| S0162 | Komplex | The OsInfo function in Komplex collects the current running username. [108] |
| S0356 | KONNI | KONNI can collect the username from the victim’s machine. [109] |
| S1075 | KOPILUWAK | KOPILUWAK can conduct basic network reconnaissance on the victim machine with whoami , to get user details. [110] |
| S0236 | Kwampirs | Kwampirs collects registered owner details by using the commands systeminfo and net config workstation . [111] |
| S9035 | LAMEHUG | LAMEHUG can use whoami to enumerate the system user. [112] |
| S1160 | Latrodectus | Latrodectus can discover the username of an infected host. [113] |
| G0032 | Lazarus Group | Various Lazarus Group malware enumerates logged-on users. [114] [115] [116] [117] [118] [50] [119] |
| S0362 | Linux Rabbit | Linux Rabbit opens a socket on port 22 and if it receives a response it attempts to obtain the machine's hostname and Top-Level Domain. [120] |
| S0513 | LiteDuke | LiteDuke can enumerate the account name on a targeted system. [121] |
| S0680 | LitePower | LitePower can determine if the current user has admin privileges. [122] |
| S0681 | Lizar | Lizar can collect the username from the system. [123] [124] |
| S9020 | LODEINFO | LODEINFO can identify the associated username on targeted machines. [125] |
| S0447 | Lokibot | Lokibot has the ability to discover the username on the infected host. [126] |
| S0532 | Lucifer | Lucifer has the ability to identify the username on a compromised host. [127] |
| G1014 | LuminousMoth | LuminousMoth has used a malicious DLL to collect the username from compromised hosts. [128] |
| S1141 | LunarWeb | LunarWeb can collect user information from the targeted host. [129] |
| S1016 | MacMa | MacMa can collect the username from the compromised machine. [130] |
| S1060 | Mafalda | Mafalda can collect the username from a compromised host. [131] |
| G0059 | Magic Hound | Magic Hound malware has obtained the victim username and sent it to the C2 server. [132] [133] [134] |
| S1169 | Mango | Mango can collect the user name from a compromised system which is used to create a unique victim identifier. [135] |
| S0652 | MarkiRAT | MarkiRAT can retrieve the victim’s username. [136] |
| S0459 | MechaFlounder | MechaFlounder has the ability to identify the username and hostname on a compromised host. [137] |
| G1051 | Medusa Group | Medusa Group has utilized PsExec to execute quser to discover the user session information. [138] |
| S1059 | metaMain | metaMain can collect the username from a compromised host. [131] |
| S0455 | Metamorfo | Metamorfo has collected the username from the victim's machine. [139] |
| S1146 | MgBot | MgBot includes modules for identifying local users and administrators on victim machines. [140] |
| S0339 | Micropsia | Micropsia collects the username from the victim’s machine. [141] |
| S1015 | Milan | Milan can identify users registered to a targeted machine. [142] |
| S0280 | MirageFox | MirageFox can gather the username from the victim’s machine. [143] |
| G1054 | MirrorFace | MirrorFace has used Windows native tools to enumerate user information. [144] |
| S0084 | Mis-Type | Mis-Type runs tests to determine the privilege level of the compromised user. [145] |
| G1036 | Moonstone Sleet | Moonstone Sleet deployed various malware such as YouieLoader that can perform system user discovery actions. [146] |
| S0149 | MoonWind | MoonWind obtains the victim username. [147] |
| S0284 | More_eggs | More_eggs has the capability to gather the username from the victim's machine. [148] [149] |
| S0256 | Mosquito | Mosquito runs whoami on the victim’s machine. [150] |
| G0069 | MuddyWater | MuddyWater has used malware that can collect the victim’s username. [151] [152] |
| S0228 | NanHaiShu | NanHaiShu collects the username from the victim. [153] |
| S0590 | NBTscan | NBTscan can list active users on the system. [154] [155] |
| S0272 | NDiskMonitor | NDiskMonitor obtains the victim username and encrypts the information to send over its C2 channel. [156] |
| S0691 | Neoichor | Neoichor can collect the user name from a victim's machine. [104] |
| S1106 | NGLite | NGLite will run the whoami command to gather system information and return this to the command and control server. [157] |
| C0002 | Night Dragon | During Night Dragon , threat actors used password cracking and pass-the-hash tools to discover usernames and passwords. [158] |
| S1147 | Nightdoor | Nightdoor gathers information on victim system users and usernames. [159] |
| S0385 | njRAT | njRAT enumerates the current user during the initial infection. [160] |
| S0353 | NOKKI | NOKKI can collect the username from the victim’s machine. [161] |
| S0644 | ObliqueRAT | ObliqueRAT can check for blocklisted usernames on infected endpoints. [162] |
| S0340 | Octopus | Octopus can collect the username from the victim’s machine. [163] |
| S1172 | OilBooster | OilBooster can identify the compromised system's username which is then used as part of a unique identifier. [164] |
| G0049 | OilRig | OilRig has run whoami on a victim. [165] [166] [167] |
| S0439 | Okrum | Okrum can collect the victim username. [168] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors used the query user and whoami commands as part of their advanced reconnaissance. [169] |
| C0061 | Operation Digital Eye | During Operation Digital Eye , threat actors used GetUserInfo to identify current user information. [170] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors enumerated sessions and users on a remote host, and identified privileged users logged into a targeted system. [171] |
| G0040 | Patchwork | Patchwork collected the victim username and whether it was running as admin, then sent the information to its C2 server. [172] [156] |
| S0013 | PlugX | PlugX has the ability to gather the username from the victim’s machine. [173] |
| S0428 | PoetRAT | PoetRAT sent username, computer name, and the previously generated UUID in reply to a "who" command from C2. [174] |
| S0139 | PowerDuke | PowerDuke has commands to get the current user's name and SID. [175] |
| S0441 | PowerShower | PowerShower has the ability to identify the current user on the infected host. [176] |
| S0223 | POWERSTATS | POWERSTATS has the ability to identify the username on the compromised host. [177] |
| S0184 | POWRUNER | POWRUNER may collect information about the currently logged in user by running whoami on a victim. [178] |
| S0113 | Prikormka | A module in Prikormka collects information from the victim about the current user name. [179] |
| S1228 | PUBLOAD | PUBLOAD has obtained the username from an infected host. [180] [181] [182] [183] |
| S0192 | Pupy | Pupy can enumerate local information for Linux hosts and find currently logged on users for Windows hosts. [184] |
| S9019 | PureCrypter | PureCrypter can retrieve the username from targeted machines. [185] |
| S1032 | PyDCrypt | PyDCrypt has probed victim machines with whoami and has collected the username from the machine. [186] |
| S0650 | QakBot | QakBot can identify the user name on a compromised system. [187] [188] |
| S0269 | QUADAGENT | QUADAGENT gathers the victim username. [189] |
| S0262 | QuasarRAT | QuasarRAT can enumerate the username and account type. [190] |
| S1148 | Raccoon Stealer | Raccoon Stealer gathers information on the infected system owner and user. [191] [192] [193] |
| S1130 | Raspberry Robin | Raspberry Robin determines whether it is successfully running on a victim system by querying the running account information to determine if it is running in Session 0, indicating running with elevated privileges. [194] |
| S0241 | RATANKBA | RATANKBA runs the whoami and query user commands. [195] |
| S0662 | RCSession | RCSession can gather system owner information, including user and administrator privileges. [196] |
| S0172 | Reaver | Reaver collects the victim's username. [197] |
| S0153 | RedLeaves | RedLeaves can obtain information about the logged on user both locally and for Remote Desktop sessions. [198] |
| S1240 | RedLine Stealer | RedLine Stealer has obtained the username from the victim’s machine. [199] [200] [201] |
| S0332 | Remcos | Remcos can enumerate the username on targeted hosts. [202] |
| S0125 | Remsec | Remsec can obtain information about the current user. [203] |
| S0379 | Revenge RAT | Revenge RAT gathers the username from the system. [204] |
| S0258 | RGDoor | RGDoor executes the whoami on the victim’s machine. [205] |
| S0433 | Rifdoor | Rifdoor has the ability to identify the username on the compromised host. [95] |
| S0448 | Rising Sun | Rising Sun can detect the username of the infected host. [206] |
| S0270 | RogueRobin | RogueRobin collects the victim’s username and whether that user is an admin. [207] |
| S0240 | ROKRAT | ROKRAT can collect the username from a compromised host. [208] |
| S0148 | RTM | RTM can obtain the victim username and permissions. [209] |
| S9037 | RustyWater | RustyWater has gathered the victim machine’s username. [210] |
| S0085 | S-Type | S-Type has run tests to determine the privilege level of the compromised user. [145] |
| S1018 | Saint Bot | Saint Bot can collect the username from a compromised host. [211] |
| G0034 | Sandworm Team | Sandworm Team has collected the username from a compromised host. [212] |
| S0461 | SDBbot | SDBbot has the ability to identify the user on a compromised host. [82] |
| S0382 | ServHelper | ServHelper will attempt to enumerate the username of the victim. [213] |
| S0596 | ShadowPad | ShadowPad has collected the username of the victim system. [214] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors executed whoami on victim machines to enumerate user context and validate privilege levels. [215] [216] |
| S0450 | SHARPSTATS | SHARPSTATS has the ability to identify the username on the compromised host. [177] |
| S0610 | SideTwist | SideTwist can collect the username on a targeted system. [167] |
| G0121 | Sidewinder | Sidewinder has used tools to identify the user of a compromised host. [217] |
| S0692 | SILENTTRINITY | SILENTTRINITY can gather a list of logged on users. [218] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA has collected the username from a victim machine. [219] |
| S1035 | Small Sieve | Small Sieve can obtain the id of a logged in user. [220] |
| S0649 | SMOKEDHAM | SMOKEDHAM has used whoami commands to identify system owners. [221] |
| S1124 | SocGholish | SocGholish can use whoami to obtain the username from a compromised host. [222] [223] [224] |
| S0627 | SodaMaster | SodaMaster can identify the username on a compromised host. [225] |
| S0615 | SombRAT | SombRAT can execute getinfo to identify the username on a compromised host. [226] [227] |
| S0543 | Spark | Spark has run the whoami command and has a built-in command to identify the user logged in. [228] |
| S0374 | SpeakUp | SpeakUp uses the whoami command. [229] |
| S1030 | Squirrelwaffle | Squirrelwaffle can collect the user name from a compromised host. [230] |
| S0058 | SslMM | SslMM sends the logged-on username to its hard-coded C2. [231] |
| S1037 | STARWHALE | STARWHALE can gather the username from an infected host. [232] [233] |
| G0038 | Stealth Falcon | Stealth Falcon malware gathers the registered user and primary owner name via WMI. [234] |
| G1046 | Storm-1811 | Storm-1811 has used whoami.exe to determine if the active user on a compromised system is an administrator. [235] |
| S1034 | StrifeWater | StrifeWater can collect the user name from the victim's machine. [236] |
| S0559 | SUNBURST | SUNBURST collected the username from a compromised host. [237] [238] |
| S1064 | SVCReady | SVCReady can collect the username from an infected host. [239] |
| S0242 | SynAck | SynAck gathers user names from infected hosts. [240] |
| S0060 | Sys10 | Sys10 collects the account name of the logged-in user and sends it to the C2. [231] |
| S0663 | SysUpdate | SysUpdate can collect the username from a compromised host. [241] |
| S0098 | T9000 | T9000 gathers and beacons the username of the logged in account during installation. It will also gather the username of running processes to determine if it is running as SYSTEM. [242] |
| G0027 | Threat Group-3390 | Threat Group-3390 has used whoami to collect system user information. [44] |
| S1239 | TONESHELL | TONESHELL has obtained the username from an infected host. [183] |
| S0266 | TrickBot | TrickBot can identify the user and groups the user belongs to on a compromised host. [243] |
| S0094 | Trojan.Karagany | Trojan.Karagany can gather information about the user on a compromised host. [244] |
| G0081 | Tropic Trooper | Tropic Trooper used letmein to scan for saved usernames on the target system. [245] |
| S0647 | Turian | Turian can retrieve usernames. [246] |
| S0130 | Unknown Logger | Unknown Logger can obtain information about the victim usernames. [247] |
| S0275 | UPPERCUT | UPPERCUT has the capability to collect the current logged on user’s username from a machine. [248] |
| S0476 | Valak | Valak can gather information regarding the user. [249] |
| S0257 | VERMIN | VERMIN gathers the username from the victim’s machine. [250] |
| G1017 | Volt Typhoon | Volt Typhoon has used public tools and executed the PowerShell command Get-EventLog security -instanceid 4624 to identify associated user and computer account names. [251] [252] [253] |
| S0515 | WellMail | WellMail can identify the current username on the victim system. [254] |
| S0514 | WellMess | WellMess can collect the username on the victim machine to send to C2. [255] |
| S0155 | WINDSHIELD | WINDSHIELD can gather the victim user name. [256] |
| G0112 | Windshift | Windshift has used malware to identify the username on a compromised host. [257] |
| S0219 | WINERACK | WINERACK can gather information on the victim username. [88] |
| S0059 | WinMM | WinMM uses NetUser-GetInfo to identify that it is running under an "Admin" account on the local system. [231] |
| G1035 | Winter Vivern | Winter Vivern PowerShell scripts execute whoami to identify the executing user. [258] |
| G0102 | Wizard Spider | Wizard Spider has used "whoami" to identify the local user and their privileges. [259] |
| S1065 | Woody RAT | Woody RAT can retrieve a list of user accounts and usernames from an infected machine. [260] |
| S0161 | XAgentOSX | XAgentOSX contains the getInfoOSX function to return the OS X version as well as the current user. [261] |
| S1207 | XLoader | XLoader can identify the username from a victim machine. [262] |
| S1248 | XORIndex Loader | XORIndex Loader has collected the username from the victim host. [263] |
| S0248 | yty | yty collects the victim’s username. [264] |
| S0251 | Zebrocy | Zebrocy gets the username from the system. [265] [266] |
| G0128 | ZIRCONIUM | ZIRCONIUM has used a tool to capture the username on a compromised host in order to register it with C2. [267] |
| S0350 | zwShell | zwShell can obtain the name of the logged-in user on the victim. [158] |
| S0412 | ZxShell | ZxShell can collect the owner and organization information from the target workstation. [268] |
| S1013 | ZxxZ | ZxxZ can collect the username from a compromised host. [269] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0093 | Behavioral Detection of User Discovery via Local and Remote Enumeration | AN0254 | Adversary launches built-in system tools (e.g., whoami, query user, net user) or scripts that enumerate user account information via local execution or remote API queries (e.g., WMI, PowerShell). |
| AN0255 | Adversary runs commands like whoami , id , w , or cat /etc/passwd from non-interactive or scripting contexts to enumerate system user details. |  |  |
| AN0256 | Adversary uses dscl , who , or environment variables like $USER to identify accounts or sessions via Terminal or malicious LaunchAgents. |  |  |
| AN0257 | Adversary executes CLI commands like show users , show ssh , or attempts to dump AAA user lists from routers or switches. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0093 | Behavioral Detection of User Discovery via Local and Remote Enumeration | AN0254 | Adversary launches built-in system tools (e.g., whoami, query user, net user) or scripts that enumerate user account information via local execution or remote API queries (e.g., WMI, PowerShell). |
| AN0255 | Adversary runs commands like whoami , id , w , or cat /etc/passwd from non-interactive or scripting contexts to enumerate system user details. |  |  |
| AN0256 | Adversary uses dscl , who , or environment variables like $USER to identify accounts or sessions via Terminal or malicious LaunchAgents. |  |  |
| AN0257 | Adversary executes CLI commands like show users , show ssh , or attempts to dump AAA user lists from routers or switches. |  |  |

---

## References

- [Cisco. (2023, March 7). Cisco IOS Security Command Reference: Commands S to Z . Retrieved July 13, 2022.](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s5.html)
- [US-CERT. (2018, April 20). Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved October 19, 2020.](https://us-cert.cisa.gov/ncas/alerts/TA18-106A)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [The DigiTrust Group. (2017, January 12). The Rise of Agent Tesla. Retrieved November 5, 2018.](https://www.digitrustgroup.com/agent-tesla-keylogger/)
- [Zhang, X. (2018, April 05). Analysis of New Agent Tesla Spyware Variant. Retrieved November 5, 2018.](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)
- [Jazi, H. (2020, April 16). New AgentTesla variant steals WiFi credentials. Retrieved May 19, 2020.](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)
- [Shevchenko, S.. (2008, November 30). Agent.btz - A Threat That Hit Pentagon. Retrieved April 8, 2016.](http://blog.threatexpert.com/2008/11/agentbtz-threat-that-hit-pentagon.html)
- [Kasuya, M. (2020, January 8). Threat Spotlight: Amadey Bot Targets Non-Russian Users. Retrieved July 14, 2022.](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
- [Grunzweig, J., Lee, B. (2016, January 22). New Attacks Linked to C0d0so0 Group. Retrieved August 2, 2018.](https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/)
- [Moran, N., et al. (2014, November 21). Operation Double Tap. Retrieved January 14, 2016.](https://www.fireeye.com/blog/threat-research/2014/11/operation_doubletap.html)
- [Henderson, S., et al. (2020, April 22). Vietnamese Threat Actors APT32 Targeting Wuhan Government and Chinese Ministry of Emergency Management in Latest Example of COVID-19 Related Espionage. Retrieved April 28, 2020.](https://www.fireeye.com/blog/threat-research/2020/04/apt32-targeting-chinese-government-in-covid-19-related-espionage.html)
- [Foltýn, T. (2018, March 13). OceanLotus ships new backdoor using old tricks. Retrieved May 22, 2018.](https://www.welivesecurity.com/2018/03/13/oceanlotus-ships-new-backdoor/)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)
- [DHS/CISA. (2020, August 26). FASTCash 2.0: North Korea's BeagleBoyz Robbing Banks. Retrieved September 29, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)
- [Symantec Security Response. (2015, December 7). Iran-based attackers use back door threats to spy on Middle Eastern targets. Retrieved April 17, 2019.](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [Nikita Rostovcev. (2022, August 18). APT41 World Tour 2021 on a tight schedule. Retrieved February 22, 2024.](https://www.group-ib.com/blog/apt41-world-tour-2021/)
- [CrowdStrike. (2023). 2022 Falcon OverWatch Threat Hunting Report. Retrieved May 20, 2024.](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Jornet, A. (2021, December 23). Snip3, an investigation into malware. Retrieved September 19, 2023.](https://telefonicatech.com/blog/snip3-investigacion-malware)
- [Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
- [Unit 42. (2019, February 22). New BabyShark Malware Targets U.S. National Security Think Tanks. Retrieved October 7, 2019.](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
- [Symantec Security Response. (2014, June 30). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1, 2020.](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
- [Mandiant. (n.d.). Appendix C (Digital) - The Malware Arsenal. Retrieved July 18, 2016.](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [Red Team Labs. (2018, April 24). Hidden Administrative Accounts: BloodHound to the Rescue. Retrieved October 28, 2020.](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)
- [Cash, D., Grunzweig, J., Meltzer, M., Adair, S., Lancaster, T. (2021, August 17). North Korean APT InkySquid Infects Victims Using Browser Exploits. Retrieved September 30, 2021.](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [Robert Falcone, Mike Scott, Juan Cortes. (2015, November 10). Bookworm Trojan: A Model of Modular Architecture. Retrieved July 21, 2025.](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)
- [MSTIC. (2021, May 28). Breaking down NOBELIUM’s latest early-stage toolset. Retrieved August 4, 2021.](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
- [Stolyarov, V. (2022, March 17). Exposing initial access broker with ties to Conti. Retrieved August 18, 2022.](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Costa, F. (2022, May 1). RaaS AvosLocker Incident Response Analysis. Retrieved January 11, 2023.](https://www.linkedin.com/pulse/raas-avoslocker-incident-response-analysis-fl%C3%A1vio-costa?trk=articles_directory)
- [Falcone, R., Lee, B. (2018, November 20). Sofacy Continues Global Attacks and Wheels Out New ‘Cannon’ Trojan. Retrieved November 26, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
- [Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Salem, E. (2020, November 17). CHAES: Novel Malware Targeting Latin American E-Commerce. Retrieved June 30, 2021.](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Chen, T. and Chen, Z. (2020, February 17). CLAMBLING - A New Backdoor Base On Dropbox. Retrieved November 12, 2021.](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
- [Microsoft. (2022, June 2). Exposing POLONIUM activity and infrastructure targeting Israeli organizations. Retrieved July 1, 2022.](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [N. Baisini. (2022, July 13). Transparent Tribe begins targeting education sector in latest campaign. Retrieved September 22, 2022.](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
- [Stokes, P. (2020, July 27). Four Distinct Families of Lazarus Malware Target Apple’s macOS Platform. Retrieved August 7, 2020.](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
- [Kohler, A. and Lopez, C. (2024, April 30). Malware: Cuckoo Behaves Like Cross Between Infostealer and Spyware. Retrieved August 20, 2024.](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
- [TrendMicro. (2014, September 03). DARKCOMET. Retrieved November 6, 2018.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [Shulmin, A., Yunakovsky, S. (2017, April 28). Use of DNS Tunneling for C&C Communications. Retrieved November 5, 2018.](https://securelist.com/use-of-dns-tunneling-for-cc-communications/78203/)
- [Fidelis Cybersecurity. (2016, February 29). The Turbo Campaign, Featuring Derusbi for 64-bit Linux. Retrieved March 2, 2016.](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [Shivtarkar, N. and Kumar, A. (2022, June 9). Lyceum .NET DNS Backdoor. Retrieved June 23, 2022.](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)
- [ClearSky Cyber Security. (2017, December). Charming Kitten. Retrieved December 27, 2017.](http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [hasherezade. (2015, November 4). A Technical Look At Dyreza. Retrieved June 15, 2020.](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
- [Chen, J., et al. (2022). Delving Deep: An Analysis of Earth Lusca’s Operations. Retrieved July 1, 2022.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
- [Bichet, J. (2020, November 12). Egregor – Prolock: Fraternal Twins ?. Retrieved January 6, 2021.](https://www.intrinsec.com/egregor-prolock/?cn-reloaded=1)
- [Adamitis, D. et al. (2019, June 4). It's alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign. Retrieved May 11, 2020.](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
- [Kaspersky Lab's Global Research & Analysis Team. (2014, August 06). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroboros. Retrieved November 7, 2018.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
- [Adamitis, D. (2020, May 6). Phantom in the Command Shell. Retrieved November 17, 2024.](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
- [ANSSI. (2021, January 27). SANDWORM INTRUSION SET CAMPAIGN TARGETING CENTREON SYSTEMS. Retrieved March 30, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
- [Threat Intelligence and Research. (2015, March 30). VOLATILE CEDAR. Retrieved February 8, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
- [Somerville, L. and Toro, A. (2017, March 30). Playing Cat & Mouse: Introducing the Felismus Malware. Retrieved November 16, 2017.](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)
- [Patil, S. (2018, June 26). Microsoft Office Vulnerabilities Used to Distribute FELIXROOT Backdoor in Recent Campaign. Retrieved November 17, 2024.](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
- [Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
- [FireEye iSIGHT Intelligence. (2017, June 16). FIN10: Anatomy of a Cyber Extortion Operation. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/rpt-fin-10-anatomy-of-a-cyber-en.pdf)
- [Abdo, B., et al. (2022, April 4). FIN7 Power Hour: Adversary Archaeology and the Evolution of FIN7. Retrieved April 5, 2022.](https://www.mandiant.com/resources/evolution-of-fin7)
- [Symantec Threat Hunter Team. (2023, July 18). FIN8 Uses Revamped Sardonic Backdoor to Deliver Noberus Ransomware. Retrieved August 9, 2023.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [Proofpoint Staff. (2018, March 7). Leaked Ammyy Admin Source Code Turned into Malware. Retrieved May 28, 2019.](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Cybereason Nocturnus. (2019, June 25). Operation Soft Cell: A Worldwide Campaign Against Telecommunications Providers. Retrieved July 18, 2019.](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)
- [Kasza, A. and Reichel, D. (2017, February 27). The Gamaredon Group Toolset Evolution. Retrieved March 1, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)
- [Kaspersky Lab's Global Research & Analysis Team. (2017, August 30). Introducing WhiteBear. Retrieved September 21, 2017.](https://securelist.com/introducing-whitebear/81638/)
- [Schwarz, D. et al. (2019, October 16). TA505 Distributes New SDBbot Remote Access Trojan with Get2 Downloader. Retrieved May 29, 2020.](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
- [Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
- [Priego, A. (2021, July). THE BROTHERS GRIM: THE REVERSING TALE OF GRIMAGENT MALWARE USED BY RYUK. Retrieved September 19, 2024.](https://www.group-ib.com/blog/grimagent/)
- [Eoin Miller. (2021, March 23). Defending Against the Zero Day: Analyzing Attacker Behavior Post-Exploitation of Microsoft Exchange. Retrieved October 27, 2022.](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)
- [FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
- [Shivtarkar, N. and Jain, S. (2023, February 14). Havoc Across the Cyberspace. Retrieved August 4, 2025.](https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace)
- [Wan, Y. (2025, March 3). Havoc: SharePoint with Microsoft Graph API turns into FUD C2. Retrieved August 4, 2025.](https://www.fortinet.com/blog/threat-research/havoc-sharepoint-with-microsoft-graph-api-turns-into-fud-c2)
- [Patil, S. and Williams, M.. (2019, June 5). Government Sector in Central Asia Targeted With New HAWKBALL Backdoor Delivered via Microsoft Office Vulnerabilities. Retrieved June 20, 2019.](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Breitenbacher, D. (2024). Unmasking HiddenFace. Retrieved April 17, 2026.](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)
- [Knight, S.. (2020, April 16). VMware Carbon Black TAU Threat Analysis: The Evolution of Lazarus. Retrieved May 1, 2020.](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
- [eSentire Threat Response Unit (TRU). (2024, November 14). Bored BeaverTail & InvisibleFerret Yacht Club – A Lazarus Lure Pt.2. Retrieved October 17, 2025.](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Check Point. (2024, November 12). Hamas-affiliated Threat Actor WIRTE Continues its Middle East Operations and Moves to Disruptive Activity. Retrieved April 20, 2026.](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
- [Sancho, D., et al. (2012, May 22). IXESHE An APT Campaign. Retrieved June 7, 2019.](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Magius, J., et al. (2017, July 19). Koadic. Retrieved September 27, 2024.](https://github.com/offsecginger/koadic)
- [Jazi, H. (2021, February). LazyScripter: From Empire to double RAT. Retrieved November 17, 2024.](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
- [Dani Creus, Tyler Halfpop, Robert Falcone. (2016, September 26). Sofacy's 'Komplex' OS X Trojan. Retrieved July 8, 2017.](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)
- [Rascagneres, P. (2017, May 03). KONNI: A Malware Under The Radar For Years. Retrieved November 5, 2018.](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
- [Conteras, T., Splunk Research Team. (2025, September 25). From Prompt to Payload: LAMEHUG’s LLM-Driven Cyber Intrusion. Retrieved April 21, 2026.](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
- [Stepanic, D. and Bousseaden, S. (2024, May 15). Spring Cleaning with LATRODECTUS: A Potential Replacement for ICEDID. Retrieved September 13, 2024.](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved November 17, 2024.](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Remote Administration Tools & Content Staging Malware Report. Retrieved March 16, 2016.](https://web.archive.org/web/20220608001455/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf)
- [Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)
- [Saini, A. and Hossein, J. (2022, January 27). North Korea’s Lazarus APT leverages Windows Update client, GitHub in latest campaign. Retrieved January 27, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)
- [Anomali Labs. (2018, December 6). Pulling Linux Rabbit/Rabbot Malware Out of a Hat. Retrieved March 4, 2019.](https://www.anomali.com/blog/pulling-linux-rabbit-rabbot-malware-out-of-a-hat)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Yamout, M. (2021, November 29). WIRTE’s campaign in the Middle East ‘living off the land’ since at least 2019. Retrieved February 1, 2022.](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [Bourhis, P., Sekoia TDR. (2024, February 1). Unveiling the intricacies of DiceLoader. Retrieved May 14, 2025.](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
- [ITOCHU. (2024, January 24). The Endless Struggle Against APT10: Insights from LODEINFO v0.6.6 - v0.7.3 Analysis. Retrieved April 17, 2026.](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
- [Kazem, M. (2019, November 25). Trojan:W32/Lokibot. Retrieved May 15, 2020.](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)
- [Hsu, K. et al. (2020, June 24). Lucifer: New Cryptojacking and DDoS Hybrid Malware Exploiting High and Critical Vulnerabilities to Infect Windows Devices. Retrieved November 16, 2020.](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
- [Botezatu, B and etl. (2021, July 21). LuminousMoth - PlugX, File Exfiltration and Persistence Revisited. Retrieved October 20, 2022.](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [Lee, B. and Falcone, R. (2017, February 15). Magic Hound Campaign Attacks Saudi Targets. Retrieved December 27, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)
- [DFIR Report. (2022, March 21). APT35 Automates Initial Access Using ProxyShell. Retrieved May 25, 2022.](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [Hromcova, Z. and Burgher, A. (2023, September 21). OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes. Retrieved November 21, 2024.](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
- [GReAT. (2021, June 16). Ferocious Kitten: 6 Years of Covert Surveillance in Iran. Retrieved September 22, 2021.](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
- [Falcone, R. (2019, March 4). New Python-Based Payload MechaFlounder Used by Chafer. Retrieved May 27, 2020.](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [ESET Research. (2019, October 3). Casbaneiro: peculiarities of this banking Trojan that affects Brazil and Mexico. Retrieved September 23, 2021.](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
- [Threat Hunter Team. (2023, April 20). Daggerfly: APT Actor Targets Telecoms Company in Africa. Retrieved July 25, 2024.](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
- [Rascagneres, P., Mercer, W. (2017, June 19). Delphi Used To Score Against Palestine. Retrieved November 13, 2018.](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)
- [ClearSky Cyber Security . (2021, August). New Iranian Espionage Campaign By “Siamesekitten” - Lyceum. Retrieved June 6, 2022.](https://www.clearskysec.com/siamesekitten/)
- [Rosenberg, J. (2018, June 14). MirageFox: APT15 Resurfaces With New Tools Based On Old Ones. Retrieved September 21, 2018.](https://web.archive.org/web/20180615122133/https://www.intezer.com/miragefox-apt15-resurfaces-with-new-tools-based-on-old-ones/)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Microsoft Threat Intelligence. (2024, May 28). Moonstone Sleet emerges as new North Korean threat actor with new bag of tricks. Retrieved August 26, 2024.](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)
- [Miller-Osborn, J. and Grunzweig, J.. (2017, March 30). Trochilus and New MoonWind RATs Used In Attack Against Thai Organizations. Retrieved March 30, 2017.](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
- [Svajcer, V. (2018, July 31). Multiple Cobalt Personality Disorder. Retrieved September 5, 2018.](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)
- [Villadsen, O.. (2019, August 29). More_eggs, Anyone? Threat Actor ITG08 Strikes Again. Retrieved September 16, 2019.](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)
- [ESET, et al. (2018, January). Diplomats in Eastern Europe bitten by a Turla mosquito. Retrieved July 3, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 10). MuddyWater expands operations. Retrieved November 2, 2018.](https://securelist.com/muddywater/88059/)
- [Peretz, A. and Theck, E. (2021, March 5). Earth Vetala – MuddyWater Continues to Target Organizations in the Middle East. Retrieved March 18, 2021.](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
- [F-Secure Labs. (2016, July). NANHAISHU RATing the South China Sea. Retrieved July 6, 2018.](https://www.f-secure.com/documents/996508/1030745/nanhaishu_whitepaper.pdf)
- [Bezroutchko, A. (2019, November 19). NBTscan man page. Retrieved March 17, 2021.](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)
- [SecTools. (2003, June 11). NBTscan. Retrieved March 17, 2021.](https://sectools.org/tool/nbtscan/)
- [Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
- [Robert Falcone, Jeff White, and Peter Renals. (2021, November 7). Targeted Attack Campaign Against ManageEngine ADSelfService Plus Delivers Godzilla Webshells, NGLite Trojan and KdcSponge Stealer. Retrieved February 8, 2024.](https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/)
- [McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
- [Ahn Ho, Facundo Muñoz, & Marc-Etienne M.Léveillé. (2024, March 7). Evasive Panda leverages Monlam Festival to target Tibetans. Retrieved July 25, 2024.](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
- [Fidelis Cybersecurity. (2013, June 28). Fidelis Threat Advisory #1009: "njRAT" Uncovered. Retrieved June 4, 2019.](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
- [Grunzweig, J., Lee, B. (2018, September 27). New KONNI Malware attacking Eurasia and Southeast Asia. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
- [Malhotra, A. (2021, March 2). ObliqueRAT returns with new campaign using hijacked websites. Retrieved September 2, 2021.](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 15). Octopus-infested seas of Central Asia. Retrieved November 14, 2018.](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
- [Hromcova, Z. and Burgher, A. (2023, December 14). OilRig’s persistent attacks using cloud service-powered downloaders. Retrieved November 26, 2024.](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
- [Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
- [Grunzweig, J. and Falcone, R.. (2016, October 4). OilRig Malware Campaign Updates Toolset and Expands Targets. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [Hromcova, Z. (2019, July). OKRUM AND KETRICAN: AN OVERVIEW OF RECENT KE3CHANG GROUP ACTIVITY. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [Aleksandar Milenkoski, Luigi Martire. (2024, December 10). Operation Digital Eye | Chinese APT Compromises Critical Digital Infrastructure via Visual Studio Code Tunnels. Retrieved February 27, 2025.](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Cymmetria. (2016). Unveiling Patchwork - The Copy-Paste APT. Retrieved November 17, 2024.](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Mercer, W, et al. (2020, April 16). PoetRAT: Python RAT uses COVID-19 lures to target Azerbaijan public and private sectors. Retrieved April 27, 2020.](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
- [Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
- [GReAT. (2019, August 12). Recent Cloud Atlas activity. Retrieved May 8, 2020.](https://securelist.com/recent-cloud-atlas-activity/92016/)
- [Lunghi, D. and Horejsi, J.. (2019, June 10). MuddyWater Resurfaces, Uses Multi-Stage Backdoor POWERSTATS V3 and New Post-Exploitation Tools. Retrieved May 14, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
- [Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
- [Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
- [Asheer Malhotra, Jungsoo An, Kendall Mc. (2022, May 5). Mustang Panda deploys a new wave of malware targeting Europe. Retrieved August 4, 2025.](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
- [CSIRT CTI. (2024, January 23). Stately Taurus Targets Myanmar Amidst Concerns over Military Junta’s Handling of Rebel Attacks. Retrieved August 4, 2025.](https://csirt-cti.net/2024/01/23/stately-taurus-targets-myanmar/)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [Nick Dai, Vickie Su, Sunny Lu. (2022, November 18). Earth Preta Spear-Phishing Governments Worldwide. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
- [Nicolas Verdier. (n.d.). Retrieved January 29, 2018.](https://github.com/n1nj4sec/pupy)
- [Check Point Research. (2025, March 10). Blind Eagle: …And Justice for All. Retrieved April 16, 2026.](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
- [Checkpoint Research. (2021, November 15). Uncovering MosesStaff techniques: Ideology over Money. Retrieved August 11, 2022.](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [Kenefick, I. et al. (2022, October 12). Black Basta Ransomware Gang Infiltrates Networks via QAKBOT, Brute Ratel, and Cobalt Strike. Retrieved February 6, 2023.](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
- [Lee, B., Falcone, R. (2018, July 25). OilRig Targets Technology Service Provider and Government Agency with QUADAGENT. Retrieved August 9, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)
- [CISA. (2018, December 18). Analysis Report (AR18-352A) Quasar Open-Source Remote Administration Tool. Retrieved August 1, 2022.](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
- [S2W TALON. (2022, June 16). Raccoon Stealer is Back with a New Version. Retrieved August 1, 2024.](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
- [Quentin Bourgue, Pierre le Bourhis, & Sekoia TDR. (2022, June 28). Raccoon Stealer v2 - Part 1: The return of the dead. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Christopher So. (2022, December 20). Raspberry Robin Malware Targets Telecom, Governments. Retrieved May 17, 2024.](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
- [Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
- [Global Threat Center, Intelligence Team. (2020, December). APT27 Turns to Ransomware. Retrieved November 12, 2021.](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
- [Grunzweig, J. and Miller-Osborn, J. (2017, November 10). New Malware with Ties to SunOrcal Discovered. Retrieved November 16, 2017.](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [Proofpoint Threat Insight Team, Jeremy H, Axel F. (2020, March 16). New Redline Password Stealer Malware. Retrieved September 17, 2025.](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
- [Splunk Threat Research Team. (2023, June 1). Do Not Cross The 'RedLine' Stealer: Detections and Analysis. Retrieved September 17, 2025.](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
- [Yair Herling. (2023, April 4). From ChatGPT to RedLine Stealer: The Dark Side of OpenAI and Google Bard. Retrieved September 17, 2025.](https://veriti.ai/blog/veriti-research/from-chatgpt-to-redline-stealer-the-dark-side-of-openai-and-google-bard/)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
- [Livelli, K, et al. (2018, November 12). Operation Shaheen. Retrieved May 1, 2019.](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
- [Falcone, R. (2018, January 25). OilRig uses RGDoor IIS Backdoor on Targets in the Middle East. Retrieved July 6, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-oilrig-uses-rgdoor-iis-backdoor-targets-middle-east/)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [Falcone, R., et al. (2018, July 27). New Threat Actor Group DarkHydrus Targets Middle East Government. Retrieved August 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
- [Jazi, Hossein. (2021, January 6). Retrohunting APT37: North Korean APT used VBA self decode technique to inject RokRat. Retrieved March 22, 2022.](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
- [Faou, M. and Boutin, J. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
- [Awasthi, P. (2026, January 8). Reborn in Rust: Muddy Water Evolves Tooling with RustyWater Implant. Retrieved March 19, 2026.](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
- [Hasherezade. (2021, April 6). A deep dive into Saint Bot, a new downloader. Retrieved June 9, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
- [Scott W. Brady. (2020, October 15). United States vs. Yuriy Sergeyevich Andrienko et al.. Retrieved November 25, 2020.](https://www.justice.gov/opa/press-release/file/1328521/download)
- [Schwarz, D. and Proofpoint Staff. (2019, January 9). ServHelper and FlawedGrace - New malware introduced by TA505. Retrieved May 28, 2019.](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)
- [Kaspersky Lab. (2017, August). ShadowPad: popular server management software hit in supply chain attack. Retrieved March 22, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
- [Microsoft Threat Intelligence. (2025, July 22). Disrupting active exploitation of on-premises SharePoint vulnerabilities. Retrieved October 15, 2025.](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/#storm-2603)
- [Kenin, S. et al. (2025, July 21). SharePoint ToolShell | Zero-Day Exploited in-the-Wild Targets Enterprise Servers. Retrieved October 15, 2025.](https://www.sentinelone.com/blog/sharepoint-toolshell-zero-day-exploited-in-the-wild-targets-enterprise-servers/)
- [Hegel, T. (2021, January 13). A Global Perspective of the SideWinder APT. Retrieved January 27, 2021.](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [NCSC GCHQ. (2022, January 27). Small Sieve Malware Analysis Report. Retrieved August 22, 2022.](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)
- [FireEye. (2021, June 16). Smoking Out a DARKSIDE Affiliate’s Supply Chain Software Compromise. Retrieved September 22, 2021.](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
- [Andrew Northern. (2022, November 22). SocGholish, a very real threat from a very fake update. Retrieved February 13, 2024.](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
- [Red Canary. (2024, March). Red Canary 2024 Threat Detection Report: SocGholish. Retrieved March 22, 2024.](https://redcanary.com/threat-detection-report/threats/socgholish/)
- [Secureworks. (n.d.). GOLD PRELUDE . Retrieved March 22, 2024.](https://www.secureworks.com/research/threat-profiles/gold-prelude)
- [GREAT. (2021, March 30). APT10: sophisticated multi-layered loader Ecipekac discovered in A41APT campaign. Retrieved June 17, 2021.](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [Falcone, R., et al. (2020, March 3). Molerats Delivers Spark Backdoor to Government and Telecommunications Organizations. Retrieved December 14, 2020.](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)
- [Check Point Research. (2019, February 4). SpeakUp: A New Undetected Backdoor Linux Trojan. Retrieved April 17, 2019.](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
- [Kumar, A., Stone-Gross, Brett. (2021, September 28). Squirrelwaffle: New Loader Delivering Cobalt Strike. Retrieved August 9, 2022.](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
- [Baumgartner, K., Golovkin, M.. (2015, May). The MsnMM Campaigns: The Earliest Naikon APT Campaigns. Retrieved April 10, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
- [Tomcik, R. et al. (2022, February 24). Left On Read: Telegram Malware Spotted in Latest Iranian Cyber Espionage Activity. Retrieved August 18, 2022.](https://www.mandiant.com/resources/telegram-malware-iranian-espionage)
- [FBI, CISA, CNMF, NCSC-UK. (2022, February 24). Iranian Government-Sponsored Actors Conduct Cyber Operations Against Global Government and Commercial Networks. Retrieved September 27, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
- [Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.](https://citizenlab.org/2016/05/stealth-falcon/)
- [Tyler McGraw, Thomas Elkins, and Evan McCann. (2024, May 10). Ongoing Social Engineering Campaign Linked to Black Basta Ransomware Operators. Retrieved January 31, 2025.](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)
- [Cybereason Nocturnus. (2022, February 1). StrifeWater RAT: Iranian APT Moses Staff Adds New Trojan to Ransomware Operations. Retrieved August 15, 2022.](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [MSTIC. (2020, December 18). Analyzing Solorigate, the compromised DLL file that started a sophisticated cyberattack, and how Microsoft Defender helps protect customers . Retrieved January 5, 2021.](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [Ivanov, A. et al. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
- [Daniel Lunghi. (2023, March 1). Iron Tiger’s SysUpdate Reappears, Adds Linux Targeting. Retrieved March 20, 2023.](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
- [Grunzweig, J. and Miller-Osborn, J.. (2016, February 4). T9000: Advanced Modular Backdoor Uses Complex Anti-Analysis Techniques. Retrieved April 15, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [Secureworks. (2019, July 24). Updated Karagany Malware Targets Energy Sector. Retrieved August 12, 2020.](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
- [Alintanahin, K. (2015). Operation Tropic Trooper: Relying on Tried-and-Tested Flaws to Infiltrate Secret Keepers. Retrieved June 14, 2019.](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)
- [Adam Burgher. (2021, June 10). BackdoorDiplomacy: Upgrading from Quarian to Turian. Retrieved September 1, 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Matsuda, A., Muhammad I. (2018, September 13). APT10 Targeting Japanese Corporations Using Updated TTPs. Retrieved September 17, 2018.](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
- [Salem, E. et al. (2020, May 28). VALAK: MORE THAN MEETS THE EYE . Retrieved June 19, 2020.](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
- [Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
- [NSA et al. (2023, May 24). People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection. Retrieved July 27, 2023.](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)
- [Counter Threat Unit Research Team. (2023, May 24). Chinese Cyberespionage Group BRONZE SILHOUETTE Targets U.S. Government and Defense Organizations. Retrieved July 27, 2023.](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [CISA. (2020, July 16). MAR-10296782-3.v1 – WELLMAIL. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
- [CISA. (2020, July 16). MAR-10296782-2.v1 – WELLMESS. Retrieved September 24, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)
- [Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
- [The BlackBerry Research & Intelligence Team. (2020, October). BAHAMUT: Hack-for-Hire Masters of Phishing, Fake News, and Fake Apps. Retrieved February 8, 2021.](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)
- [Tom Hegel. (2023, March 16). Winter Vivern | Uncovering a Wave of Global Espionage. Retrieved July 29, 2024.](https://www.sentinelone.com/labs/winter-vivern-uncovering-a-wave-of-global-espionage/)
- [Sean Gallagher, Peter Mackenzie, Elida Leite, Syed Shahram, Bill Kearney, Anand Aijan, Sivagnanam Gn, Suraj Mundalik. (2020, October 14). They’re back: inside a new Ryuk ransomware attack. Retrieved October 14, 2020.](https://news.sophos.com/en-us/2020/10/14/inside-a-new-ryuk-ransomware-attack/)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Robert Falcone. (2017, February 14). XAgentOSX: Sofacy's Xagent macOS Tool. Retrieved July 12, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)
- [Acronis. (2021, November 26). Trojan-as-a-service: From Formbook to XLoader. Retrieved March 11, 2025.](https://www.acronis.com/en-us/cyber-protection-center/posts/trojan-as-a-service-from-formbook-to-xloader/)
- [Kirill Boychenko. (2025, July 14). Contagious Interview Campaign Escalates With 67 Malicious npm Packages and New Malware Loader. Retrieved October 19, 2025.](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
- [Schwarz, D., Sopko J. (2018, March 08). Donot Team Leverages New Modular Malware Framework in South Asia. Retrieved June 11, 2018.](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
- [ESET. (2018, November 20). Sednit: What’s going on with Zebrocy?. Retrieved February 12, 2019.](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
- [CISA. (2020, October 29). Malware Analysis Report (AR20-303B). Retrieved December 9, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
- [Singh, S. and Antil, S. (2020, October 27). APT-31 Leverages COVID-19 Vaccine Theme and Abuses Legitimate Online Services. Retrieved March 24, 2021.](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)
- [Raghuprasad, C . (2022, May 11). Bitter APT adds Bangladesh to their targets. Retrieved June 1, 2022.](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)

---

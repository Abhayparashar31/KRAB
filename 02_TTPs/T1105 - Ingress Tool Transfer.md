# Ingress Tool Transfer

## Description

Adversaries may transfer tools or other files from an external system into a compromised environment. Tools or files may be copied from an external adversary-controlled system to the victim network through the command and control channel or through alternate protocols such as ftp . Once present, adversaries may also transfer/spread tools between victim devices within a compromised environment (i.e. Lateral Tool Transfer ).

On Windows, adversaries may use various utilities to download tools, such as copy , finger , certutil , and PowerShell commands such as IEX(New-Object Net.WebClient).downloadString() and Invoke-WebRequest . On Linux and macOS systems, a variety of utilities also exist, such as curl , scp , sftp , tftp , rsync , finger , and wget . [1] A number of these tools, such as wget , curl , and scp , also exist on ESXi. After downloading a file, a threat actor may attempt to verify its integrity by checking its hash value (e.g., via certutil -hashfile ). [2]

Adversaries may also abuse installers and package managers, such as yum or winget , to download tools to victim hosts. Adversaries have also abused file application features, such as the Windows search-ms protocol handler, to deliver malicious files to victims through remote file searches invoked by User Execution (typically after interacting with Phishing lures). [3]

Files can also be transferred using various Web Service s as well as native or otherwise present tools on the victim system. [4] In some cases, adversaries may be able to leverage services that sync between a web-based and an on-premises client, such as Dropbox or OneDrive, to transfer files onto victim systems. For example, by compromising a cloud account and logging into the service's web portal, an adversary may be able to trigger an automatic syncing process that transfers the file onto the victim's machine. [5]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0028 | 2015 Ukraine Electric Power Attack | During the 2015 Ukraine Electric Power Attack , Sandworm Team pushed additional malicious tools onto an infected system to steal user credentials, move laterally, and destroy data. [6] |
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries downloaded malicious payloads to the victim server. [7] |
| S0469 | ABK | ABK has the ability to download files from C2. [8] |
| S1028 | Action RAT | Action RAT has the ability to download additional payloads onto an infected machine. [9] |
| S0331 | Agent Tesla | Agent Tesla can download additional files for execution on the victim’s machine. [10] [11] |
| S0092 | Agent.btz | Agent.btz attempts to download an encrypted binary from a specified domain. [12] |
| G0130 | Ajax Security Team | Ajax Security Team has used Wrapper/Gholee, custom-developed malware, which downloaded additional malware to the infected system. [13] |
| S1025 | Amadey | Amadey can download and execute files to further infect a host machine with additional malware. [14] |
| S0504 | Anchor | Anchor can download additional payloads. [15] [16] |
| G0138 | Andariel | Andariel has downloaded additional tools and malware onto compromised hosts. [17] |
| S1074 | ANDROMEDA | ANDROMEDA can download additional payloads from C2. [18] |
| G0099 | APT-C-36 | APT-C-36 has downloaded binary data from a specified domain after the malicious document is opened. [19] |
| G0026 | APT18 | APT18 can upload a file to the victim’s machine. [20] |
| G0007 | APT28 | APT28 has downloaded additional files, including by using a first-stage downloader to contact the C2 server to obtain the second-stage implant. [21] [22] [23] [24] [25] |
| G0016 | APT29 | APT29 has downloaded additional tools and malware onto compromised networks. [26] [27] [28] [29] |
| G0022 | APT3 | APT3 has a tool that can copy files to remote machines. [30] |
| G0050 | APT32 | APT32 has added JavaScript to victim websites to download additional frameworks that profile and compromise website visitors. [31] |
| G0064 | APT33 | APT33 has downloaded additional files and programs from its C2 server. [32] [33] |
| G0067 | APT37 | APT37 has downloaded second stage malware from compromised websites. [34] [35] [36] [37] |
| G0082 | APT38 | APT38 used a backdoor, NESTEGG, that has the capability to download and upload files to and from a victim’s machine. [38] Additionally, APT38 has downloaded other payloads onto a victim’s machine. [39] |
| G0087 | APT39 | APT39 has downloaded tools to compromised hosts. [40] [41] |
| G0096 | APT41 | APT41 used certutil to download additional files. [42] [43] [44] APT41 downloaded post-exploitation tools such as Cobalt Strike via command shell following initial access. [45] APT41 has uploaded Procdump and NATBypass to a staging directory and has used these tools in follow-on activities. [46] |
| C0040 | APT41 DUST | APT41 DUST involved execution of certutil.exe via web shell to download the DUSTPAN dropper. [47] |
| G0143 | Aquatic Panda | Aquatic Panda has downloaded additional malware onto compromised hosts. [48] |
| S0456 | Aria-body | Aria-body has the ability to download additional payloads from C2. [49] |
| S9031 | AshTag | The AshTag stager component can retrieve and execute the main payload. [50] |
| S0373 | Astaroth | Astaroth uses certutil and BITSAdmin to download additional malware. [51] [52] [53] |
| S1087 | AsyncRAT | AsyncRAT has the ability to download files including over SFTP. [54] [55] |
| S0438 | Attor | Attor can download additional plugins, updates and other files. [56] |
| S0347 | AuditCred | AuditCred can download files and additional malware. [57] |
| S0473 | Avenger | Avenger has the ability to download files from C2 to a compromised host. [8] |
| S0344 | Azorult | Azorult can download and execute additional files. Azorult has also downloaded a ransomware payload called Hermes. [58] [59] |
| S0414 | BabyShark | BabyShark has downloaded additional files from the C2. [60] [61] |
| S0475 | BackConfig | BackConfig can download and execute additional payloads on a compromised host. [62] |
| S0093 | Backdoor.Oldrea | Backdoor.Oldrea can download additional modules from C2. [63] |
| G0135 | BackdoorDiplomacy | BackdoorDiplomacy has downloaded additional files and tools onto a compromised host. [64] |
| S0642 | BADFLICK | BADFLICK has download files from its C2 server. [65] |
| S1081 | BADHATCH | BADHATCH has the ability to load a second stage malicious DLL file onto a compromised machine. [66] |
| S0128 | BADNEWS | BADNEWS is capable of downloading additional files through C2 channels, including a new version of itself. [67] [68] [69] |
| S0337 | BadPatch | BadPatch can download and execute or update malware. [70] |
| S0234 | Bandook | Bandook can download files to the system. [71] |
| S0239 | Bankshot | Bankshot uploads files and secondary payloads to the victim's machine. [72] |
| S0534 | Bazar | Bazar can download and deploy additional payloads, including ransomware and post-exploitation frameworks such as Cobalt Strike . [73] [74] [75] [76] |
| S0470 | BBK | BBK has the ability to download files from C2 to the infected host. [8] |
| S1246 | BeaverTail | BeaverTail has been used to download a malicious payload to include Python based malware InvisibleFerret . [77] [78] [79] [80] [81] [82] |
| S0574 | BendyBear | BendyBear is designed to download an implant from a C2 server. [83] |
| S0017 | BISCUIT | BISCUIT has a command to download a file from the C2 server. [84] |
| S0268 | Bisonal | Bisonal has the capability to download files to execute on the victim’s machine. [85] [86] [87] |
| S0190 | BITSAdmin | BITSAdmin can be used to create BITS Jobs to upload and/or download files. [88] |
| G1002 | BITTER | BITTER has downloaded additional malware and tools onto a compromised host. [89] [90] |
| G1043 | BlackByte | BlackByte has transferred tools such as Cobalt Strike to victim environments from file sharing and hosting websites. [91] |
| S0564 | BlackMould | BlackMould has the ability to download files to the victim's machine. [92] |
| S0520 | BLINDINGCAN | BLINDINGCAN has downloaded files to a victim machine. [93] |
| S0657 | BLUELIGHT | BLUELIGHT can download additional files onto the host. [36] |
| S0486 | Bonadan | Bonadan can download additional modules from the C2 server. [94] |
| S0360 | BONDUPDATER | BONDUPDATER can download or upload files from its C2 server. [95] |
| S0635 | BoomBox | BoomBox has the ability to download next stage malware components to a compromised system. [96] |
| S0651 | BoxCaon | BoxCaon can download files. [97] |
| S0204 | Briba | Briba downloads files onto infected hosts. [98] |
| S9015 | BRICKSTORM | BRICKSTORM has the ability to download files from the Adversaries C2 server to the compromised system. [99] [100] [101] [102] |
| G0060 | BRONZE BUTLER | BRONZE BUTLER has used various tools to download files, including DGet (a similar tool to wget). [103] |
| S1063 | Brute Ratel C4 | Brute Ratel C4 can download files to compromised hosts. [104] [105] |
| S0471 | build_downer | build_downer has the ability to download files from C2 to the infected host. [8] |
| S1039 | Bumblebee | Bumblebee can download and execute additional payloads including through the use of a Dex command. [106] [107] [108] |
| S0482 | Bundlore | Bundlore can download and execute new versions of itself. [109] |
| S1118 | BUSHWALK | BUSHWALK can write malicious payloads sent through a web request’s command parameter. [110] [111] |
| C0010 | C0010 | During C0010 , UNC3890 actors downloaded tools and malware onto a compromised host. [112] |
| C0015 | C0015 | During C0015 , the threat actors downloaded additional tools and files onto a compromised network. [113] |
| C0017 | C0017 | During C0017 , APT41 downloaded malicious payloads onto compromised systems. [114] |
| C0018 | C0018 | During C0018 , the threat actors downloaded additional tools, such as Mimikatz and Sliver , as well as Cobalt Strike and AvosLocker ransomware onto the victim network. [115] [116] |
| C0021 | C0021 | During C0021 , the threat actors downloaded additional tools and files onto victim machines. [117] [118] |
| C0026 | C0026 | During C0026 , the threat actors downloaded malicious payloads onto select compromised hosts. [18] |
| C0027 | C0027 | During C0027 , Scattered Spider downloaded tools using victim organization systems. [119] |
| S0274 | Calisto | Calisto has the capability to upload and download files to the victim's machine. [120] |
| S0077 | CallMe | CallMe has the capability to download a file to the victim from the C2 server. [121] |
| S9016 | Caminho | Caminho has the ability to download files onto compromised hosts. [122] |
| S0351 | Cannon | Cannon can download a payload for execution. [123] |
| S0484 | Carberp | Carberp can download and execute new plugins from the C2 server. [124] [125] |
| S0348 | Cardinal RAT | Cardinal RAT can download and execute additional payloads. [126] |
| S0465 | CARROTBALL | CARROTBALL has the ability to download and install a remote payload. [127] |
| S0462 | CARROTBAT | CARROTBAT has the ability to download and execute a remote file via certutil . [128] |
| S1224 | CASTLETAP | CASTLETAP can transfer files to compromised network devices. [129] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell has a module to download and upload files to the system. [130] |
| S0160 | certutil | certutil can be used to download files from a given URL. [131] [132] |
| S0631 | Chaes | Chaes can download additional files onto an infected machine. [133] |
| S0674 | CharmPower | CharmPower has the ability to download additional modules to a compromised host. [134] |
| S0144 | ChChes | ChChes is capable of downloading files, including additional modules. [135] [136] [137] |
| G0114 | Chimera | Chimera has remotely copied tools and malware onto targeted systems. [138] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP can download additional files from C2. [139] |
| S0020 | China Chopper | China Chopper 's server component can download remote files. [140] [141] [142] [143] [144] |
| S0023 | CHOPSTICK | CHOPSTICK is capable of performing remote file transmission. [145] |
| S0667 | Chrommme | Chrommme can download its code from C2. [146] |
| G1021 | Cinnamon Tempest | Cinnamon Tempest has downloaded files, including Cobalt Strike , to compromised hosts. [147] |
| S0054 | CloudDuke | CloudDuke downloads and executes additional malware from either a Web address or a Microsoft OneDrive account. [28] |
| S0106 | cmd | cmd can be used to copy files to/from a remotely connected external system. [148] |
| G0080 | Cobalt Group | Cobalt Group has used public sites such as github.com and sendspace.com to upload files and then download them to victim computers. [149] [4] The group's JavaScript backdoor is also capable of downloading files. [150] |
| S0154 | Cobalt Strike | Cobalt Strike can deliver additional payloads to victim machines. [151] [152] |
| S0369 | CoinTicker | CoinTicker executes a Python script to download its second stage. [153] |
| S0608 | Conficker | Conficker downloads an HTTP server to the infected machine. [154] |
| G0142 | Confucius | Confucius has downloaded additional files and payloads onto a compromised host following initial access. [155] [156] |
| S0492 | CookieMiner | CookieMiner can download additional scripts from a web server. [157] |
| S0137 | CORESHELL | CORESHELL downloads another dropper from its C2 server. [158] |
| S0614 | CostaBricks | CostaBricks has been used to load SombRAT onto a compromised host. [159] |
| C0004 | CostaRicto | During CostaRicto , the threat actors downloaded malware and tools onto a compromised host. [159] |
| S1023 | CreepyDrive | CreepyDrive can download files to the compromised host. [160] |
| S0115 | Crimson | Crimson contains a command to retrieve files from its C2 server. [161] [162] [163] |
| S0498 | Cryptoistic | Cryptoistic has the ability to send and receive files. [164] |
| S0527 | CSPY Downloader | CSPY Downloader can download additional tools to a compromised host. [165] |
| S0625 | Cuba | Cuba can download files from its C2 server. [166] |
| C0029 | Cutting Edge | During Cutting Edge , threat actors leveraged exploits to download remote files to Ivanti Connect Secure VPNs. [167] |
| S0687 | Cyclops Blink | Cyclops Blink has the ability to download files to target systems. [168] [169] |
| S0497 | Dacls | Dacls can download its payload from a C2 server. [164] [170] |
| G1034 | Daggerfly | Daggerfly has used PowerShell and BITSAdmin to retrieve follow-on payloads from external locations for execution on victim machines. [171] |
| S1014 | DanBot | DanBot can download additional files to a targeted system. [172] |
| S0334 | DarkComet | DarkComet can load any files onto the infected machine to execute. [173] [174] |
| S1111 | DarkGate | DarkGate retrieves cryptocurrency mining payloads and commands in encrypted traffic from its command and control server. [175] DarkGate uses Windows Batch scripts executing the curl command to retrieve follow-on payloads. [176] DarkGate has stolen sitemanager.xml and recentservers.xml from %APPDATA%\FileZilla\ if present. [177] |
| G0012 | Darkhotel | Darkhotel has used first-stage payloads that download additional malware from C2 servers. [178] |
| S1066 | DarkTortilla | DarkTortilla can download additional packages for keylogging, cryptocurrency mining, and other capabilities; it can also retrieve malicious payloads such as Agent Tesla , AsyncRat, NanoCore , RedLine, Cobalt Strike , and Metasploit. [179] |
| S0187 | Daserf | Daserf can download remote files. [180] [103] |
| S0255 | DDKONG | DDKONG downloads and uploads files on the victim’s machine. [181] |
| S0616 | DEATHRANSOM | DEATHRANSOM can download files to a compromised host. [182] |
| S0354 | Denis | Denis deploys additional backdoors and hacking tools to the system. [183] |
| S0659 | Diavol | Diavol can receive configuration updates and additional payloads including wscpy.exe from C2. [184] |
| S0200 | Dipsind | Dipsind can download remote files. [185] |
| S1088 | Disco | Disco can download files to targeted systems via SMB. [186] |
| S1021 | DnsSystem | DnsSystem can download files to compromised systems after receiving a command with the string downloaddd . [187] |
| S0213 | DOGCALL | DOGCALL can download and execute additional payloads. [188] |
| S0600 | Doki | Doki has downloaded scripts from C2. [189] |
| S0695 | Donut | Donut can download and execute previously staged shellcode payloads. [190] |
| S0472 | down_new | down_new has the ability to download files to the compromised host. [8] |
| S0134 | Downdelph | After downloading its main config file, Downdelph downloads multiple payloads from C2 servers. [191] |
| S9021 | DOWNIISSA | DOWNIISSA can download files to the compromised host. [192] |
| G0035 | Dragonfly | Dragonfly has copied and installed tools for operations once in the victim environment. [193] |
| S0694 | DRATzarus | DRATzarus can deploy additional tools onto an infected machine. [194] |
| S0547 | DropBook | DropBook can download and execute additional files. [195] [196] |
| S0502 | Drovorub | Drovorub can download files to a compromised host. [197] |
| S0567 | Dtrack | Dtrack ’s can download and upload a file to the victim’s computer. [198] [199] |
| S1159 | DUSTTRAP | DUSTTRAP can retrieve and load additional payloads. [47] |
| S0024 | Dyre | Dyre has a command to download and executes additional files. [200] |
| S0624 | Ecipekac | Ecipekac can download additional payloads to a compromised host. [201] |
| S0554 | Egregor | Egregor has the ability to download files from its C2 server. [202] [203] |
| G0066 | Elderwood | The Ritsol backdoor trojan used by Elderwood can download files onto a compromised host from a remote location. [204] |
| S0081 | Elise | Elise can download additional files from the C2 server for execution. [205] |
| S0082 | Emissary | Emissary has the capability to download files from the C2 server. [206] |
| S0367 | Emotet | Emotet can download follow-on payloads and items via malicious url parameters in obfuscated PowerShell code. [207] |
| S0363 | Empire | Empire can upload and download to and from a victim machine. [208] |
| S0404 | esentutl | esentutl can be used to copy files from a given URL. [209] |
| S0396 | EvilBunny | EvilBunny has downloaded additional Lua scripts from the C2. [210] |
| S0568 | EVILNUM | EVILNUM can download and upload files to the victim's computer. [211] [212] |
| G0120 | Evilnum | Evilnum can deploy additional components or tools as needed. [211] |
| S0401 | Exaramel for Linux | Exaramel for Linux has a command to download a file from and to a remote C2 server. [213] [214] |
| S0569 | Explosive | Explosive has a function to download a file to the infected system. [215] |
| S0171 | Felismus | Felismus can download files from remote servers. [216] |
| S0267 | FELIXROOT | FELIXROOT downloads and uploads files to and from the victim’s machine. [217] [218] |
| G1016 | FIN13 | FIN13 has downloaded additional tools and malware to compromised systems. [219] [220] |
| G0046 | FIN7 | FIN7 has downloaded additional malware to execute on the victim's machine, including by using a PowerShell script to launch shellcode that retrieves an additional payload. [221] [222] [223] [224] |
| G0061 | FIN8 | FIN8 has used remote code execution to download subsequent payloads. [225] [226] |
| S0696 | Flagpro | Flagpro can download additional malware from the C2 server. [227] |
| S0381 | FlawedAmmyy | FlawedAmmyy can transfer files from C2. [228] |
| S0661 | FoggyWeb | FoggyWeb can receive additional malicious components from an actor controlled C2 server and execute them on a compromised AD FS server. [229] |
| G0117 | Fox Kitten | Fox Kitten has downloaded additional tools including PsExec directly to endpoints. [230] |
| C0001 | Frankenstein | During Frankenstein , the threat actors downloaded files and tools onto a victim machine. [231] |
| S0095 | ftp | ftp may be abused by adversaries to transfer tools or files from an external system into a compromised environment. [232] [233] |
| S1044 | FunnyDream | FunnyDream can download additional files onto a compromised host. [234] |
| C0007 | FunnyDream | During FunnyDream , the threat actors downloaded additional droppers and backdoors onto a compromised system. [234] |
| S0628 | FYAnti | FYAnti can download additional payloads to a compromised host. [201] |
| G0093 | GALLIUM | GALLIUM dropped additional tools to victims during their operation, including portqry.exe, a renamed cmd.exe file, winrar, and HTRAN . [235] [92] |
| G0047 | Gamaredon Group | Gamaredon Group has downloaded additional malware and tools onto a compromised host. [236] [237] [238] [239] [240] [241] For example, Gamaredon Group uses a backdoor script to retrieve and decode additional payloads once in victim environments. [242] |
| S0168 | Gazer | Gazer can execute a task to download a file. [243] [244] |
| S0666 | Gelsemium | Gelsemium can download additional plug-ins to a compromised host. [146] |
| S0032 | gh0st RAT | gh0st RAT can download files to the victim’s machine. [245] [246] |
| S9010 | GlassWorm | GlassWorm has downloaded additional payloads from C2. [247] [248] [249] [250] |
| S0249 | Gold Dragon | Gold Dragon can download additional components from the C2 server. [251] |
| S0493 | GoldenSpy | GoldenSpy constantly attempts to download and execute files from the remote C2, including GoldenSpy itself if not found on the system. [252] |
| S0588 | GoldMax | GoldMax can download and execute additional files. [253] [254] |
| S1138 | Gootloader | Gootloader can fetch second stage code from hardcoded web domains. [255] [256] |
| G0078 | Gorgon Group | Gorgon Group malware can download additional files from C2 servers. [257] |
| S0531 | Grandoreiro | Grandoreiro can download its second stage from a hardcoded URL within the loader's code. [258] [259] |
| S0342 | GreyEnergy | GreyEnergy can download additional modules and payloads. [218] |
| S0632 | GrimAgent | GrimAgent has the ability to download and execute additional payloads. [260] |
| S0561 | GuLoader | GuLoader can download further malware for execution on the victim's machine. [261] |
| S0132 | H1N1 | H1N1 contains a command to download and execute a file from a remotely hosted URL using WinINet HTTP requests. [262] |
| G0125 | HAFNIUM | HAFNIUM has downloaded malware and tools--including Nishang and PowerCat--onto a compromised host. [263] [143] |
| S0499 | Hancitor | Hancitor has the ability to download additional files from C2. [264] |
| S1211 | Hannotog | Hannotog can download additional files to the victim machine. [265] |
| S0214 | HAPPYWORK | can download and execute a second-stage payload. [34] |
| S1229 | Havoc | Havoc has the ability to upload files to infected systems. [266] [267] |
| S0170 | Helminth | Helminth can download additional files. [268] |
| G1001 | HEXANE | HEXANE has downloaded additional payloads and malicious scripts onto a compromised host. [269] |
| S1249 | HexEval Loader | HexEval Loader has been used to download a malicious payload to include BeaverTail . [270] [78] [79] |
| S0087 | Hi-Zor | Hi-Zor has the ability to upload and download files from its C2 server. [271] |
| S9023 | HiddenFace | HiddenFace can download files from the C2 to victim systems. [272] [273] |
| S0394 | HiddenWasp | HiddenWasp downloads a tar compressed archive from a download server to the system. [274] |
| S0009 | Hikit | Hikit has the ability to download files to a compromised host. [275] |
| S0601 | Hildegard | Hildegard has downloaded additional scripts that build and run Monero cryptocurrency miners. [276] |
| C0038 | HomeLand Justice | During HomeLand Justice , threat actors used web shells to download files to compromised infrastructure. [277] |
| S0376 | HOPLIGHT | HOPLIGHT has the ability to connect to a remote host in order to upload and download files. [278] |
| S0431 | HotCroissant | HotCroissant has the ability to upload a file from the command and control (C2) server to the victim machine. [279] |
| S0070 | HTTPBrowser | HTTPBrowser is capable of writing a file to the compromised system from the C2 server. [280] |
| S9007 | HTTPTroy | HTTPTroy has the ability to download files from C2 using the down <FILENAME> command. [281] |
| S0203 | Hydraq | Hydraq creates a backdoor through which remote attackers can download files and additional malware components. [282] [283] |
| S0398 | HyperBro | HyperBro has the ability to download additional files. [284] |
| S0483 | IcedID | IcedID has the ability to download additional modules and a configuration file from C2. [285] [286] [287] [288] |
| S1152 | IMAPLoader | IMAPLoader is a loader used to retrieve follow-on payload encoded in email messages for execution on victim systems. [289] |
| G1032 | INC Ransom | INC Ransom has downloaded tools to compromised servers including Advanced IP Scanner. [290] [291] |
| G0136 | IndigoZebra | IndigoZebra has downloaded additional files and tools from its C2 server. [97] |
| G0119 | Indrik Spider | Indrik Spider has downloaded additional scripts, malware, and tools onto a compromised host. [292] [293] [294] |
| S0604 | Industroyer | Industroyer downloads a shellcode payload from a remote C2 server and loads it into memory. [295] |
| S1245 | InvisibleFerret | InvisibleFerret has downloaded "AnyDesk.exe" into the user’s home directory from the C2 server when checks for the service fail to identify its presence in the victim environment. [80] InvisibleFerret has also been configured to download additional payloads using a command which calls to the /bow URI. [296] [81] |
| S0260 | InvisiMole | InvisiMole can upload files to the victim's machine for operations. [297] [298] |
| S0015 | Ixeshe | Ixeshe can download and execute additional files. [299] |
| S0528 | Javali | Javali can download payloads from remote C2 servers. [53] |
| S0044 | JHUHUGIT | JHUHUGIT can retrieve an additional payload from its C2 server. [300] [301] JHUHUGIT has a command to download files to the victim’s machine. [302] |
| S0201 | JPIN | JPIN can download files and upgrade itself. [185] |
| S0283 | jRAT | jRAT can download and execute files. [303] [304] [305] |
| S0648 | JSS Loader | JSS Loader has the ability to download malicious executables to a compromised host. [306] |
| S0215 | KARAE | KARAE can upload and download files, including second-stage malware. [34] |
| S0088 | Kasidet | Kasidet has the ability to download and execute additional files. [307] |
| S0265 | Kazuar | Kazuar downloads additional plug-ins to load on the victim’s machine, including the ability to upgrade and replace its own binary. [308] |
| G0004 | Ke3chang | Ke3chang has used tools to download files to compromised machines. [309] |
| S0585 | Kerrdown | Kerrdown can download specific payloads to a compromised host based on OS architecture. [310] |
| S0487 | Kessel | Kessel can download additional modules from the C2 server. [94] |
| S1020 | Kevin | Kevin can download files to the compromised host. [269] |
| S0387 | KeyBoy | KeyBoy has a download and upload functionality. [311] [312] |
| S0271 | KEYMARBLE | KEYMARBLE can upload files to the victim’s machine and can download additional payloads. [313] |
| S0526 | KGH_SPY | KGH_SPY has the ability to download and execute code from remote servers. [165] |
| G0094 | Kimsuky | Kimsuky has downloaded additional scripts, tools, and malware onto victim systems. [314] [43] [315] [316] |
| S0599 | Kinsing | Kinsing has downloaded additional lateral movement scripts from C2. [317] |
| S0437 | Kivars | Kivars has the ability to download and execute files. [318] |
| S0250 | Koadic | Koadic can download additional files and tools. [319] [320] |
| S0669 | KOCTOPUS | KOCTOPUS has executed a PowerShell command to download a file to the system. [320] |
| S0356 | KONNI | KONNI can download files and execute them on the victim’s machine. [321] [322] |
| C0035 | KV Botnet Activity | KV Botnet Activity included the use of scripts to download additional payloads when compromising network nodes. [323] |
| S0236 | Kwampirs | Kwampirs downloads additional files from C2 servers. [324] |
| S1160 | Latrodectus | Latrodectus can download and execute PEs, DLLs, and shellcode from C2. [288] [325] [326] |
| G0032 | Lazarus Group | Lazarus Group has downloaded files, malware, and tools from its C2 onto a compromised host. [327] [328] [329] [164] [170] [330] [331] [332] [333] [334] |
| G0140 | LazyScripter | LazyScripter had downloaded additional tools to a compromised host. [320] |
| G0065 | Leviathan | Leviathan has downloaded additional scripts and files from adversary-controlled servers. [335] [140] |
| S0395 | LightNeuron | LightNeuron has the ability to download and execute additional files. [336] |
| S1185 | LightSpy | On macOS, LightSpy downloads a .json file from the C2 server. The .json file contains metadata about the plugins to be downloaded, including their URL, name, version, and MD5 hash. LightSpy retrieves the plugins specified in the .json file, which are compiled .dylib files. These .dylib files provide task and platform specific functionality. LightSpy also imports open-source libraries to manage socket connections. [337] |
| S0211 | Linfo | Linfo creates a backdoor through which remote attackers can download files onto compromised hosts. [338] |
| S0513 | LiteDuke | LiteDuke has the ability to download files. [339] |
| S0680 | LitePower | LitePower has the ability to download payloads containing system commands to a compromised host. [340] |
| S0681 | Lizar | Lizar can download additional plugins, files, and tools. [341] [342] [343] |
| S9020 | LODEINFO | LODEINFO has the ability to download additional files from the C2. [344] [345] [346] |
| S0447 | Lokibot | Lokibot downloaded several staged items onto the victim's machine. [347] |
| S0451 | LoudMiner | LoudMiner used SCP to update the miner from the C2. [348] |
| S0042 | LOWBALL | LOWBALL uses the Dropbox API to request two files, one of which is the same file as the one dropped by the malicious email attachment. This is most likely meant to be a mechanism to update the compromised host with a new version of the LOWBALL malware. [349] |
| S0532 | Lucifer | Lucifer can download and execute a replica of itself using certutil . [350] |
| G1014 | LuminousMoth | LuminousMoth has downloaded additional malware and tools onto a compromised host. [351] [352] |
| S0409 | Machete | Machete can download additional files for execution on the victim’s machine. [353] |
| S1016 | MacMa | MacMa has downloaded additional files, including an exploit for used privilege escalation. [354] [355] |
| S1048 | macOS.OSAMiner | macOS.OSAMiner has used curl to download a Stripped Payloads from a public facing adversary-controlled webpage. |
| S1060 | Mafalda | Mafalda can download additional files onto the compromised host. [356] |
| G0059 | Magic Hound | Magic Hound has downloaded additional code and files from servers onto victims. [357] [358] [359] [360] |
| S1182 | MagicRAT | MagicRAT can import and execute additional payloads. [361] |
| S0652 | MarkiRAT | MarkiRAT can download additional files and tools from its C2 server, including through the use of BITSAdmin . [362] |
| S0500 | MCMD | MCMD can upload additional files to a compromised host. [363] |
| S0459 | MechaFlounder | MechaFlounder has the ability to upload and download files to and from a compromised host. [364] |
| G1051 | Medusa Group | Medusa Group has leveraged certutil , PowerShell, and Windows Command to download additional tools to include RMM services. [365] Medusa Group has also engaged in "Bring Your Own Vulnerable Driver" (BYOVD) and downloaded vulnerable or signed drivers to the victim environment to disable security tools. [365] [366] |
| S0530 | Melcoz | Melcoz has the ability to download additional files to a compromised host. [53] |
| G0045 | menuPass | menuPass has installed updates and new malware on victims. [367] [368] |
| G1013 | Metador | Metador has downloaded tools and malware onto a compromised system. [369] |
| S1059 | metaMain | metaMain can download files onto compromised systems. [369] [356] |
| S0455 | Metamorfo | Metamorfo has used MSI files to download additional files to execute. [370] [371] [372] [373] |
| S0688 | Meteor | Meteor has the ability to download additional files for execution on the victim's machine. [374] |
| S0339 | Micropsia | Micropsia can download and execute an executable from the C2 server. [375] [376] |
| S1015 | Milan | Milan has received files from C2 and stored them in log folders beginning with the character sequence a9850d2f . [377] |
| S0051 | MiniDuke | MiniDuke can download additional encrypted backdoors onto the victim via GIF files. [378] [339] |
| S0084 | Mis-Type | Mis-Type has downloaded additional malware and files onto a compromised host. [379] |
| S0083 | Misdat | Misdat is capable of downloading files from the C2. [379] |
| S0080 | Mivast | Mivast has the capability to download and execute .exe files. [380] |
| S0079 | MobileOrder | MobileOrder has a command to download a file from the C2 server to the victim mobile device's SD card. [121] |
| S0553 | MoleNet | MoleNet can download additional payloads from the C2. [195] |
| G0021 | Molerats | Molerats used executables to download malicious files from different sources. [381] [382] |
| S1026 | Mongall | Mongall can download files to targeted systems. [383] |
| G1036 | Moonstone Sleet | Moonstone Sleet retrieved a final stage payload from command and control infrastructure during initial installation on victim systems. [384] |
| S0284 | More_eggs | More_eggs can download and launch additional payloads. [385] [386] |
| G1009 | Moses Staff | Moses Staff has downloaded and installed web shells to following path C:\inetpub\wwwroot\aspnet_client\system_web\IISpool.aspx . [387] |
| S0256 | Mosquito | Mosquito can upload and download files to the victim. [388] |
| S9032 | MuddyViper | MuddyViper has the ability to download files from the C2 server. Additionally, MuddyViper has the ability to download a file in chunks with sleep time between each chunk. [389] |
| G0069 | MuddyWater | MuddyWater has used malware that can upload additional files to the victim’s machine. [390] [391] [392] [393] MuddyWater has used PowerShell commands to install remote management and monitoring (RMM) software on the victim’s machine to conduct espionage and to exfiltrate data. [394] |
| G0129 | Mustang Panda | Mustang Panda has downloaded additional executables following the initial infection stage. [395] [396] [397] [398] Mustang Panda has also leveraged Visual Studio Code code.exe and Dev Tunnels using DevTunnel.exe to propagate additional tools and payloads. [399] |
| G1020 | Mustard Tempest | Mustard Tempest has deployed secondary payloads and third stage implants to compromised hosts. [400] |
| S0228 | NanHaiShu | NanHaiShu can download additional files from URLs. [335] |
| S0336 | NanoCore | NanoCore has the capability to download and activate additional modules for execution. [401] [402] |
| S0247 | NavRAT | NavRAT can download files remotely. [403] |
| S0272 | NDiskMonitor | NDiskMonitor can download and execute a file from given URL. [69] |
| S0630 | Nebulae | Nebulae can download files from C2. [404] |
| S1189 | Neo-reGeorg | Neo-reGeorg has the ability to download files to targeted systems. [405] |
| S0691 | Neoichor | Neoichor can download additional files onto a compromised host. [309] |
| S0210 | Nerex | Nerex creates a backdoor through which remote attackers can download files onto a compromised host. [204] |
| S0457 | Netwalker | Operators deploying Netwalker have used psexec and certutil to retrieve the Netwalker payload. [406] |
| S0198 | NETWIRE | NETWIRE can downloaded payloads from C2 to the compromised host. [407] [408] |
| S1192 | NICECURL | NICECURL has the ability to download additional content onto an infected machine, e.g. by using curl . [409] |
| S0118 | Nidiran | Nidiran can download and execute files. [410] |
| C0002 | Night Dragon | During Night Dragon , threat actors used administrative utilities to deliver Trojan components to remote systems. [411] |
| S1090 | NightClub | NightClub can load multiple additional plugins on an infected host. [186] |
| S0385 | njRAT | njRAT can download files to the victim’s machine. [412] [413] APT-C-36 has used modified versions of njRAT to enable the download of .NET assemblies. [414] |
| S0353 | NOKKI | NOKKI has downloaded a remote module for execution. [415] |
| G0133 | Nomadic Octopus | Nomadic Octopus has used malicious macros to download additional files to the victim's machine. [416] |
| S0340 | Octopus | Octopus can download additional files and tools onto the victim’s machine. [417] [418] [416] |
| S1170 | ODAgent | ODAgent has the ability to download and execute files on compromised systems. [419] |
| S1172 | OilBooster | OilBooster can download and execute files from an actor-controlled OneDrive account. [419] |
| S1171 | OilCheck | OilCheck can download staged payloads from an actor-controlled infrastructure. [419] |
| G0049 | OilRig | OilRig had downloaded remote files onto victim infrastructure. [420] [421] |
| S0439 | Okrum | Okrum has built-in commands for uploading, downloading, and executing files to the system. [422] |
| S0264 | OopsIE | OopsIE can download files from its C2 server to the victim's machine. [423] [424] |
| C0022 | Operation Dream Job | During Operation Dream Job , Lazarus Group downloaded multistage malware and tools onto a compromised host. [194] [425] [426] |
| C0006 | Operation Honeybee | During Operation Honeybee , the threat actors downloaded additional malware and malicious scripts onto a compromised host. [427] |
| C0048 | Operation MidnightEclipse | During Operation MidnightEclipse , threat actors downloaded additional payloads on compromised devices. [428] [429] |
| C0013 | Operation Sharpshooter | During Operation Sharpshooter , additional payloads were downloaded after a target was infected with a first-stage downloader. [430] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors downloaded additional files to the infected system. [431] |
| S0229 | Orz | Orz can download files onto the victim. [335] |
| S0402 | OSX/Shlayer | OSX/Shlayer can download payloads, and extract bytes from files. OSX/Shlayer uses the curl -fsL "$url" >$tmp_path command to download malicious payloads into a temporary directory. [432] [433] [434] [435] |
| S0352 | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D has a command to download and execute a file on the victim’s machine. [436] [437] |
| C0042 | Outer Space | During Outer Space , OilRig downloaded additional tools to comrpomised infrastructure. [438] |
| S1017 | OutSteel | OutSteel can download files from its C2 server. [439] |
| S0598 | P.A.S. Webshell | P.A.S. Webshell can upload and download files to and from compromised hosts. [214] |
| S0626 | P8RAT | P8RAT can download additional payloads to a target system. [201] |
| S0664 | Pandora | Pandora can load additional drivers and files onto a victim machine. [440] |
| S0208 | Pasam | Pasam creates a backdoor through which remote attackers can upload files. [441] |
| G0040 | Patchwork | Patchwork payloads download additional files from the C2 server. [442] [69] |
| S0587 | Penquin | Penquin can execute the command code do_download to retrieve remote files from C2. [443] |
| S0643 | Peppy | Peppy can download and execute remote files. [161] |
| S9014 | PHASEJAM | PHASEJAM has the ability to upload files onto the compromised appliance. [444] |
| S9028 | PHPsert | PHPsert has the ability to retrieve remote payloads. [445] |
| S0501 | PipeMon | PipeMon can install additional modules via C2 commands. [446] |
| S0124 | Pisloader | Pisloader has a command to upload a file to the victim machine. [447] |
| S0254 | PLAINTEE | PLAINTEE has downloaded and executed additional plugins. [181] |
| G0068 | PLATINUM | PLATINUM has transferred files using the Intel® Active Management Technology (AMT) Serial-over-LAN (SOL) channel. [448] |
| G1040 | Play | Play has used Cobalt Strike to download files to compromised machines. [449] |
| S0435 | PLEAD | PLEAD has the ability to upload and download files to and from an infected host. [450] |
| S0013 | PlugX | PlugX has a module to download and execute files on the compromised machine. [451] [452] [453] [454] |
| S0428 | PoetRAT | PoetRAT has the ability to copy files and download/upload files into C2 channels using FTP and HTTPS. [455] [456] |
| S0012 | PoisonIvy | PoisonIvy creates a backdoor through which remote attackers can upload files. [457] |
| S0518 | PolyglotDuke | PolyglotDuke can retrieve payloads from the C2 server. [339] |
| S0453 | Pony | Pony can download additional files onto the infected system. [458] |
| S0150 | POSHSPY | POSHSPY downloads and executes additional PowerShell code and Windows binaries. [459] |
| S0139 | PowerDuke | PowerDuke has a command to download a file. [460] |
| S1173 | PowerExchange | PowerExchange can decode Base64-encoded files and call WriteAllBytes to write the files to compromised hosts. [461] |
| S1012 | PowerLess | PowerLess can download additional payloads to a compromised host. [462] |
| S0685 | PowerPunch | PowerPunch can download payloads from adversary infrastructure. [239] |
| S0145 | POWERSOURCE | POWERSOURCE has been observed being used to download TEXTMATE and the Cobalt Strike Beacon payload onto victims. [463] |
| S0223 | POWERSTATS | POWERSTATS can retrieve and execute additional PowerShell payloads from the C2 server. [464] |
| S0184 | POWRUNER | POWRUNER can download or upload files from its C2 server. [420] |
| S0613 | PS1 | CostaBricks can download additional payloads onto a compromised host. [159] |
| S0078 | Psylo | Psylo has a command to download a file to the system from its C2 server. [121] |
| S0147 | Pteranodon | Pteranodon can download and execute additional files. [236] [465] [466] |
| S1228 | PUBLOAD | PUBLOAD has acted as a stager that can download the next-stage payload from its C2 server. [467] [468] [469] [470] [471] PUBLOAD has also delivered FDMTP as a secondary control tool and PTSOCKET for exfiltration to some infected systems. [472] |
| S0196 | PUNCHBUGGY | PUNCHBUGGY can download additional files and payloads to compromised hosts. [473] [474] |
| S0192 | Pupy | Pupy can upload and download to/from a victim machine. [475] |
| S9019 | PureCrypter | PureCrypter can download additional payloads for execution on the compromised host. [476] [477] |
| S0650 | QakBot | QakBot has the ability to download additional components and malware. [478] [479] [480] [481] [482] [483] |
| C0055 | Quad7 Activity | Quad7 Activity has downloaded additional binaries from a remote File Transfer Protocol (FTP) server to compromised devices. [484] |
| S0262 | QuasarRAT | QuasarRAT can download files to the victim’s machine and execute them. [485] [486] |
| S0686 | QuietSieve | QuietSieve can download and execute payloads on a target host. [239] |
| S1148 | Raccoon Stealer | Raccoon Stealer downloads various library files enabling interaction with various data stores and structures to facilitate follow-on information theft. [487] [488] |
| S0629 | RainyDay | RainyDay can download files to a compromised host. [404] |
| G0075 | Rancor | Rancor has downloaded additional malware, including by using certutil . [181] |
| S0055 | RARSTONE | RARSTONE downloads its backdoor component from a C2 server and loads it directly into memory. [489] |
| S1130 | Raspberry Robin | Raspberry Robin retrieves its second stage payload in a variety of ways such as through msiexec.exe abuse, or running the curl command to download the payload to the victim's %AppData% folder. [490] [491] |
| S0241 | RATANKBA | RATANKBA uploads and downloads information. [492] [493] |
| S0662 | RCSession | RCSession has the ability to drop additional files to an infected machine. [494] |
| S0495 | RDAT | RDAT can download files via DNS. [495] |
| S0153 | RedLeaves | RedLeaves is capable of downloading a file from a specified URL. [496] |
| S1240 | RedLine Stealer | RedLine Stealer has the ability download additional payloads. [497] [498] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 used backdoor malware capable of downloading files to compromised infrastructure. [499] |
| S0511 | RegDuke | RegDuke can download files from C2. [339] |
| S1187 | reGeorg | reGeorg has the ability to download files to targeted systems. [405] |
| S0332 | Remcos | Remcos can upload and download files to and from the victim’s machine. [500] [501] |
| S0166 | RemoteCMD | RemoteCMD copies a file over to the remote system before execution. [502] |
| S0592 | RemoteUtilities | RemoteUtilities can upload and download files to and from a target machine. [393] |
| S0125 | Remsec | Remsec contains a network loader to receive executable modules from remote attackers and run them on the local victim. It can also upload and download files over HTTP and HTTPS. [503] [504] |
| S0379 | Revenge RAT | Revenge RAT has the ability to upload and download files. [505] |
| S0496 | REvil | REvil can download a copy of itself from an attacker controlled IP address to the victim machine. [506] [507] [508] |
| S0258 | RGDoor | RGDoor uploads and downloads files to and from the victim’s machine. [509] |
| S1222 | RIFLESPINE | RIFLESPINE can download and execute files. [510] |
| G0106 | Rocke | Rocke used malware to download additional malicious files to the target system. [511] |
| S0270 | RogueRobin | RogueRobin can save a new file to the system from the C2 server. [512] [513] |
| S0240 | ROKRAT | ROKRAT can retrieve additional malicious payloads from its C2 server. [514] [515] [37] [516] |
| S0148 | RTM | RTM can download additional files. [517] [518] |
| S0085 | S-Type | S-Type can download additional files onto a compromised host. [379] |
| S1018 | Saint Bot | Saint Bot can download additional files onto a compromised host. [439] |
| S0074 | Sakula | Sakula has the capability to download files. [519] |
| S1168 | SampleCheck5000 | SampleCheck5000 can download additional payloads to compromised hosts. [438] [419] |
| S1099 | Samurai | Samurai has been used to deploy other malware including Ninja . [144] |
| G0034 | Sandworm Team | Sandworm Team has pushed additional malicious tools onto an infected system to steal user credentials, move laterally, and destroy data. [520] [521] |
| S1085 | Sardonic | Sardonic has the ability to upload additional malicious files to a compromised machine. [522] |
| G1015 | Scattered Spider | Scattered Spider has downloaded the Teleport remote access tool to compromised VMware vCenter Servers. [523] |
| S0461 | SDBbot | SDBbot has the ability to download a DLL from C2 to a compromised host. [524] |
| S0053 | SeaDuke | SeaDuke is capable of uploading and downloading files. [525] |
| S0345 | Seasalt | Seasalt has a command to download additional files. [84] [84] |
| S0185 | SEASHARPEE | SEASHARPEE can download remote files onto victims. [526] |
| S0382 | ServHelper | ServHelper may download additional files to execute. [527] [528] |
| S0639 | Seth-Locker | Seth-Locker has the ability to download and execute files on a compromised host. [529] |
| S0596 | ShadowPad | ShadowPad has downloaded code from a C2 server. [530] |
| C0045 | ShadowRay | During ShadowRay , threat actors downloaded and executed the XMRig miner on targeted hosts. [531] |
| S9008 | Shai-Hulud | Shai-Hulud has downloaded packages from code repositories. [532] [533] [534] [535] Shai-Hulud has also downloaded and executed the secrets-discovery tool TruffleHog to gather sensitive data. [536] [533] [537] [534] [535] |
| S0140 | Shamoon | Shamoon can download an executable to run on the victim. [538] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors used a loader to download and execute ransomware. [539] |
| S1019 | Shark | Shark can download additional files from its C2 via HTTP or DNS. [377] [540] |
| S1089 | SharpDisco | SharpDisco has been used to download a Python interpreter to C:\Users\Public\WinTN\WinTN.exe as well as other plugins from external sources. [186] |
| S0546 | SharpStage | SharpStage has the ability to download and execute additional payloads via a DropBox API. [195] [196] |
| S0450 | SHARPSTATS | SHARPSTATS has the ability to upload and download files. [541] |
| S0444 | ShimRat | ShimRat can download additional files. [542] |
| S0445 | ShimRatReporter | ShimRatReporter had the ability to download additional payloads. [542] |
| S0217 | SHUTTERSPEED | SHUTTERSPEED can download and execute an arbitary executable. [34] |
| S0589 | Sibot | Sibot can download and execute a payload onto a compromised system. [253] |
| G1008 | SideCopy | SideCopy has delivered trojanized executables via spearphishing emails that contacts actor-controlled servers to download malicious payloads. [9] |
| S0610 | SideTwist | SideTwist has the ability to download additional files. [543] |
| G0121 | Sidewinder | Sidewinder has used LNK files to download remote files to the victim's network. [544] [545] |
| G0091 | Silence | Silence has downloaded additional modules and malware to victim’s machines. [546] |
| S0692 | SILENTTRINITY | SILENTTRINITY can load additional files and tools, including Mimikatz . [547] |
| S0468 | Skidmap | Skidmap has the ability to download files on an infected host. [548] |
| S1110 | SLIGHTPULSE | RAPIDPULSE can transfer files to and from compromised hosts. [549] |
| S0633 | Sliver | Sliver can download additional content and files from the Sliver server to the client residing on the victim machine using the upload command. [550] [551] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA has downloaded files onto a victim machine. [552] |
| S0218 | SLOWDRIFT | SLOWDRIFT downloads additional payloads. [34] |
| S1035 | Small Sieve | Small Sieve has the ability to download files. [553] |
| S0226 | Smoke Loader | Smoke Loader downloads a new version of itself once it has installed. It also downloads additional plugins. [554] |
| S0649 | SMOKEDHAM | SMOKEDHAM has used Powershell to download UltraVNC and ngrok from third-party file sharing sites. [555] |
| S1086 | Snip3 | Snip3 can download additional payloads to compromised systems. [556] [557] |
| S1124 | SocGholish | SocGholish can download additional malware to infected hosts. [558] [559] |
| S0627 | SodaMaster | SodaMaster has the ability to download additional payloads from C2 to the targeted system. [201] |
| S1166 | Solar | Solar has the ability to download and execute files. [438] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 downloaded additional malware, such as TEARDROP and Cobalt Strike , onto a compromised host following initial access. [560] |
| S0615 | SombRAT | SombRAT has the ability to download and execute additional payloads. [159] [182] [561] |
| S0516 | SoreFang | SoreFang can download additional payloads from C2. [562] [563] |
| S0374 | SpeakUp | SpeakUp downloads and executes additional files from a remote server. [564] |
| S1140 | Spica | Spica can upload and download files to and from compromised hosts. [565] |
| S0646 | SpicyOmelette | SpicyOmelette can download malicious files from threat actor controlled AWS URL's. [566] |
| S0390 | SQLRat | SQLRat can make a direct SQL connection to a Microsoft database controlled by the attackers, retrieve an item from the bindata table, then write and execute the file on disk. [567] |
| S1030 | Squirrelwaffle | Squirrelwaffle has downloaded and executed additional encoded payloads. [568] [569] |
| S1112 | STEADYPULSE | STEADYPULSE can add lines to a Perl script on a targeted server to import additional Perl modules. [570] |
| S0380 | StoneDrill | StoneDrill has downloaded and dropped temporary files containing scripts; it additionally has a function to upload files from the victims machine. [571] |
| G1046 | Storm-1811 | Storm-1811 has used scripted cURL commands, BITSAdmin , and other mechanisms to retrieve follow-on batch scripts and tools for execution on victim devices. [572] [573] [574] |
| S1183 | StrelaStealer | StrelaStealer installers have used obfuscated PowerShell scripts to retrieve follow-on payloads from WebDAV servers. [575] |
| S1034 | StrifeWater | StrifeWater can download updates and auxiliary modules. [576] |
| S0491 | StrongPity | StrongPity can download files to specified targets. [577] |
| S0559 | SUNBURST | SUNBURST delivered different payloads, including TEARDROP in at least one instance. [560] |
| S1064 | SVCReady | SVCReady has the ability to download additional tools such as the RedLine Stealer to an infected host. [578] |
| S9001 | SystemBC | SystemBC has downloaded additional files for execution on the victim’s machine. [579] [580] The server component of SystemBC has the ability to send additional files to victim machines. [580] |
| S0663 | SysUpdate | SysUpdate has the ability to download files to a compromised host. [440] [581] |
| G1018 | TA2541 | TA2541 has used malicious scripts and macros with the ability to download additional payloads. [582] |
| G0092 | TA505 | TA505 has downloaded additional malware to execute on victim systems. [583] [528] [584] |
| G0127 | TA551 | TA551 has retrieved DLLs and installer binaries for malware execution from C2. [585] |
| S0011 | Taidoor | Taidoor has downloaded additional files onto a compromised host. [586] |
| S0586 | TAINTEDSCRIBE | TAINTEDSCRIBE can download additional modules from its C2 server. [587] |
| S1193 | TAMECAT | TAMECAT has used wget and curl to download additional content. [409] |
| S0164 | TDTESS | TDTESS has a command to download and execute an additional file. [588] |
| G0139 | TeamTNT | TeamTNT has the curl and wget commands as well as batch scripts to download new tools. [589] [590] |
| S0595 | ThiefQuest | ThiefQuest can download and execute payloads in-memory or from disk. [591] |
| G0027 | Threat Group-3390 | Threat Group-3390 has downloaded additional malware and tools, including through the use of certutil , onto a compromised host . [280] [592] |
| S0665 | ThreatNeedle | ThreatNeedle can download additional tools to enable lateral movement. [330] |
| S0668 | TinyTurla | TinyTurla has the ability to act as a second-stage dropper used to infect the system with additional malware. [593] |
| S0671 | Tomiris | Tomiris can download files and execute them on a victim's system. [594] |
| S1239 | TONESHELL | TONESHELL has the ability to download additional files to the victim device. [595] |
| G0131 | Tonto Team | Tonto Team has downloaded malicious DLLs which served as a ShadowPad loader. [596] |
| S0266 | TrickBot | TrickBot downloads several additional files and saves them to the victim's machine. [597] [598] |
| S0094 | Trojan.Karagany | Trojan.Karagany can upload, download, and execute files on the victim. [599] [600] |
| G0081 | Tropic Trooper | Tropic Trooper has used a delivered trojan to download additional files. [601] |
| S0436 | TSCookie | TSCookie has the ability to upload and download files to and from the infected host. [602] |
| S9034 | Tsundere Botnet | Tsundere Botnet ’s loader component has downloaded the zip file node-v18.17.0-win-x64.zip from the official Node.js website, as well as pm2, a Node.js process management tool. [603] |
| S0647 | Turian | Turian can download additional files and tools from its C2. [64] |
| G0010 | Turla | Turla has used shellcode to download Meterpreter after compromising a victim. [604] |
| S0199 | TURNEDUP | TURNEDUP is capable of downloading additional files. [605] |
| S0263 | TYPEFRAME | TYPEFRAME can upload and download files to the victim’s machine. [606] |
| S0333 | UBoatRAT | UBoatRAT can upload and download files to the victim’s machine. [607] |
| S0130 | Unknown Logger | Unknown Logger is capable of downloading remote files. [67] |
| S0275 | UPPERCUT | UPPERCUT can download and upload files to and from the victim’s machine. [608] [609] [610] |
| S0022 | Uroburos | Uroburos can use a Put command to write files to an infected machine. [611] |
| S0386 | Ursnif | Ursnif has dropped payload and configuration files to disk. Ursnif has also been used to download and execute additional payloads. [612] [613] |
| S0476 | Valak | Valak has downloaded a variety of modules and payloads to the compromised host, including IcedID and NetSupport Manager RAT-based malware. [614] [615] |
| S0636 | VaporRage | VaporRage has the ability to download malicious shellcode to compromised systems. [96] |
| S0207 | Vasport | Vasport can download files. [616] |
| S0442 | VBShower | VBShower has the ability to download VBS files to the target computer. [617] |
| S0257 | VERMIN | VERMIN can download and upload files to the victim's machine. [618] |
| S1217 | VIRTUALPITA | VIRTUALPITA has the ability to upload and download files. [619] |
| G1055 | VOID MANTICORE | VOID MANTICORE has deployed additional payloads from dedicated C2 servers. [620] [621] [622] VOID MANTICORE has also downloaded legitimate tools and software from publicly available services. [620] VOID MANTICORE had utilized VeraCrypt a legitimate disk encrypting utility that was downloaded directly from the website. [620] |
| G0123 | Volatile Cedar | Volatile Cedar can deploy additional tools. [130] |
| S0180 | Volgmer | Volgmer can download remote files and additional payloads to the victim's machine. [623] [624] [625] |
| G1017 | Volt Typhoon | Volt Typhoon has downloaded an outdated version of comsvcs.dll to a compromised domain controller in a non-standard folder. [626] |
| S0670 | WarzoneRAT | WarzoneRAT can download and execute additional files. [627] |
| C0037 | Water Curupira Pikabot Distribution | Water Curupira Pikabot Distribution used Curl.exe to download the Pikabot payload from an external server, saving the file to the victim machine's temporary directory. [628] |
| S0579 | Waterbear | Waterbear can receive and load executables from remote C2 servers. [629] |
| S0109 | WEBC2 | WEBC2 can download and execute a file. [630] |
| S0515 | WellMail | WellMail can receive data and executable scripts from C2. [631] |
| S0514 | WellMess | WellMess can write files to a compromised host. [27] [632] |
| S0689 | WhisperGate | WhisperGate can download additional stages of malware from a Discord CDN channel. [633] [634] [635] [636] |
| G0107 | Whitefly | Whitefly has the ability to download additional tools from the C2. [637] |
| S0206 | Wiarp | Wiarp creates a backdoor through which remote attackers can download files. [638] |
| G0112 | Windshift | Windshift has used tools to deploy additional payloads to compromised hosts. [639] |
| S0430 | Winnti for Linux | Winnti for Linux has the ability to deploy modules directly from command and control (C2) servers, possibly for remote command execution, file exfiltration, and socks5 proxying on the infected host. [640] |
| S0141 | Winnti for Windows | The Winnti for Windows dropper can place malicious payloads on targeted systems. [641] |
| G0044 | Winnti Group | Winnti Group has downloaded an auxiliary program named ff.exe to infected machines. [642] |
| G1035 | Winter Vivern | Winter Vivern executed PowerShell scripts to create scheduled tasks to retrieve remotely-hosted payloads. [643] |
| S1115 | WIREFIRE | WIREFIRE has the ability to download files to compromised devices. [644] |
| G0090 | WIRTE | WIRTE has downloaded PowerShell code from the C2 server to be executed. [645] |
| G0102 | Wizard Spider | Wizard Spider can transfer malicious payloads such as ransomware to compromised machines. [646] |
| S1065 | Woody RAT | Woody RAT can download files from its C2 server, including the .NET DLLs, WoodySharpExecutor and WoodyPowerSession . [647] |
| S0341 | Xbash | Xbash can download additional malicious files from its C2 server. [648] |
| S0653 | xCaon | xCaon has a command to download files to the victim's machine. [97] |
| S0658 | XCSSET | XCSSET downloads browser specific AppleScript modules using a constructed URL with the curl command, https://" & domain & "/agent/scripts/" & moduleName & ".applescript . [649] |
| S1248 | XORIndex Loader | XORIndex Loader has been used to download a malicious payload to include BeaverTail . [78] |
| S0388 | YAHOYAH | YAHOYAH uses HTTP GET requests to download other files that are executed in memory. [650] |
| S0251 | Zebrocy | Zebrocy obtains additional code to execute on the victim's machine, including the downloading of a secondary payload. [651] [123] [652] [23] |
| S0230 | ZeroT | ZeroT can download additional payloads onto the victim. [653] |
| S0330 | Zeus Panda | Zeus Panda can download additional malware plug-in modules and execute them on the victim’s machine. [654] |
| S1114 | ZIPLINE | ZIPLINE can download files to be saved on the compromised system. [644] [110] |
| G0128 | ZIRCONIUM | ZIRCONIUM has used tools to download malicious files to compromised hosts. [655] |
| S0086 | ZLib | ZLib has the ability to download files. [379] |
| S0672 | Zox | Zox can download files to a compromised machine. [275] |
| S0412 | ZxShell | ZxShell has a command to transfer files from a remote host. [656] |
| S1013 | ZxxZ | ZxxZ can download and execute additional files. [89] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1037 | Filter Network Traffic | Use network filtering to block outbound traffic from compromised systems to unapproved external destinations. Restricting access to known, trusted IP addresses and protocols can prevent attackers from downloading malicious tools or payloads onto compromised servers after gaining initial access. |
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware or unusual data transfer over known protocols like FTP can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. [657] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0060 | Detect Ingress Tool Transfers via Behavioral Chain | AN0165 | Unusual or uncommon processes initiate network connections to external destinations followed by file creation (tools downloaded). |
| AN0166 | Shell-based tools (curl, wget, scp) initiate connections to external domains followed by creation of executable files on disk. |  |  |
| AN0167 | Process execution of curl or wget followed by a network connection and a file created in temporary or user-specific directories. |  |  |
| AN0168 | Command line interface or vCLI triggers remote transfer using wget or curl, writing files into datastore paths or local tmp directories. |  |  |
| AN0169 | Network device logs show anomalous inbound file transfers or uncharacteristic flows with high payload volume to network devices with storage or automation hooks. |  |  |

---

## References

- [LOLBAS. (n.d.). LOLBAS Mapped to T1105. Retrieved March 11, 2022.](https://lolbas-project.github.io/#t1105)
- [COSMICENERGY: New OT Malware Possibly Related To Russian Emergency Response Exercises. (2023, May 25). Ken Proska, Daniel Kapellmann Zafra, Keith Lunden, Corey Hildebrandt, Rushikesh Nandedkar, Nathan Brubaker. Retrieved March 18, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/cosmicenergy-ot-malware-russian-response/)
- [Mathanraj Thangaraju, Sijo Jacob. (2023, July 26). Beyond File Search: A Novel Method for Exploiting the "search-ms" URI Protocol Handler. Retrieved March 15, 2024.](https://www.trellix.com/blogs/research/beyond-file-search-a-novel-method/)
- [Positive Technologies. (2016, December 16). Cobalt Snatch. Retrieved October 9, 2018.](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-Snatch-eng.pdf)
- [David Talbot. (2013, August 21). Dropbox and Similar Services Can Sync Malware. Retrieved May 31, 2023.](https://www.technologyreview.com/2013/08/21/83143/dropbox-and-similar-services-can-sync-malware/)
- [Booz Allen Hamilton. (2016). When The Lights Went Out. Retrieved December 18, 2024.](https://www.boozallen.com/content/dam/boozallen/documents/2016/09/ukraine-report-when-the-lights-went-out.pdf)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [Brumaghin, E., et al. (2018, October 15). Old dog, new tricks - Analysing new RTF-based campaign distributing Agent Tesla, Loki with PyREbox. Retrieved November 5, 2018.](https://blog.talosintelligence.com/2018/10/old-dog-new-tricks-analysing-new-rtf_15.html)
- [The DigiTrust Group. (2017, January 12). The Rise of Agent Tesla. Retrieved November 5, 2018.](https://www.digitrustgroup.com/agent-tesla-keylogger/)
- [Shevchenko, S.. (2008, November 30). Agent.btz - A Threat That Hit Pentagon. Retrieved April 8, 2016.](http://blog.threatexpert.com/2008/11/agentbtz-threat-that-hit-pentagon.html)
- [Check Point Software Technologies. (2015). ROCKET KITTEN: A CAMPAIGN WITH 9 LIVES. Retrieved March 16, 2018.](https://blog.checkpoint.com/wp-content/uploads/2015/11/rocket-kitten-report.pdf)
- [Kasuya, M. (2020, January 8). Threat Spotlight: Amadey Bot Targets Non-Russian Users. Retrieved July 14, 2022.](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [Grange, W. (2020, July 13). Anchor_dns malware goes cross platform. Retrieved September 10, 2020.](https://medium.com/stage-2-security/anchor-dns-malware-family-goes-cross-platform-d807ba13ca30)
- [AhnLab. (2018, June 23). Targeted attacks by Andariel Threat Group, a subgroup of the Lazarus. Retrieved September 29, 2021.](https://web.archive.org/web/20230213154832/http://download.ahnlab.com/global/brochure/%5BAnalysis%5DAndariel_Group.pdf)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [QiAnXin Threat Intelligence Center. (2019, February 18). APT-C-36: Continuous Attacks Targeting Colombian Government Institutions and Corporations. Retrieved May 5, 2020.](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
- [Grunzweig, J., et al. (2016, May 24). New Wekby Attacks Use DNS Requests As Command and Control Mechanism. Retrieved November 15, 2018.](https://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
- [Bitdefender. (2015, December). APT28 Under the Scope. Retrieved February 23, 2017.](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
- [Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.](https://pan-unit42.github.io/playbook_viewer/)
- [Accenture Security. (2018, November 29). SNAKEMACKEREL. Retrieved April 15, 2019.](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
- [Hacquebord, F., Remorin, L. (2020, December 17). Pawn Storm’s Lack of Sophistication as a Strategy. Retrieved January 13, 2021.](https://www.trendmicro.com/en_us/research/20/l/pawn-storm-lack-of-sophistication-as-a-strategy.html)
- [NSA, CISA, FBI, NCSC. (2021, July). Russian GRU Conducting Global Brute Force Campaign to Compromise Enterprise and Cloud Environments. Retrieved July 26, 2021.](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)
- [Dunwoody, M. and Carr, N.. (2016, September 27). No Easy Breach DerbyCon 2016. Retrieved September 12, 2024.](https://www.slideshare.net/slideshow/no-easy-breach-derby-con-2016/66447908)
- [PWC. (2020, July 16). How WellMess malware has been used to target COVID-19 vaccines. Retrieved September 24, 2020.](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)
- [F-Secure Labs. (2015, September 17). The Dukes: 7 years of Russian cyberespionage. Retrieved December 10, 2015.](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
- [Mandiant. (2022, May 2). UNC3524: Eye Spy on Your Email. Retrieved August 17, 2023.](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
- [Chen, X., Scott, M., Caselden, D.. (2014, April 26). New Zero-Day Exploit targeting Internet Explorer Versions 9 through 11 Identified in Targeted Attacks. Retrieved January 14, 2016.](https://www.fireeye.com/blog/threat-research/2014/04/new-zero-day-exploit-targeting-internet-explorer-versions-9-through-11-identified-in-targeted-attacks.html)
- [Lassalle, D., et al. (2017, November 6). OceanLotus Blossoms: Mass Digital Surveillance and Attacks Targeting ASEAN, Asian Nations, the Media, Human Rights Groups, and Civil Society. Retrieved November 6, 2017.](https://www.volexity.com/blog/2017/11/06/oceanlotus-blossoms-mass-digital-surveillance-and-exploitation-of-asean-nations-the-media-human-rights-and-civil-society/)
- [Security Response attack Investigation Team. (2019, March 27). Elfin: Relentless Espionage Group Targets Multiple Organizations in Saudi Arabia and U.S.. Retrieved April 10, 2019.](https://www.symantec.com/blogs/threat-intelligence/elfin-apt33-espionage)
- [Microsoft Threat Protection Intelligence Team. (2020, June 18). Inside Microsoft Threat Protection: Mapping attack chains from cloud to endpoint. Retrieved June 22, 2020.](https://www.microsoft.com/security/blog/2020/06/18/inside-microsoft-threat-protection-mapping-attack-chains-from-cloud-to-endpoint/)
- [FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
- [GReAT. (2019, May 13). ScarCruft continues to evolve, introduces Bluetooth harvester. Retrieved June 4, 2019.](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)
- [Cash, D., Grunzweig, J., Meltzer, M., Adair, S., Lancaster, T. (2021, August 17). North Korean APT InkySquid Infects Victims Using Browser Exploits. Retrieved September 30, 2021.](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
- [Cash, D., Grunzweig, J., Adair, S., Lancaster, T. (2021, August 25). North Korean BLUELIGHT Special: InkySquid Deploys RokRAT. Retrieved October 1, 2021.](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
- [FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)
- [SEONGSU PARK. (2022, December 27). BlueNoroff introduces new methods bypassing MoTW. Retrieved February 6, 2024.](https://securelist.com/bluenoroff-methods-bypass-motw/108383/)
- [Symantec. (2018, February 28). Chafer: Latest Attacks Reveal Heightened Ambitions. Retrieved May 22, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/chafer-latest-attacks-reveal-heightened-ambitions)
- [FBI. (2020, September 17). Indicators of Compromise Associated with Rana Intelligence Computing, also known as Advanced Persistent Threat 39, Chafer, Cadelspy, Remexi, and ITG07. Retrieved December 10, 2020.](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)
- [Glyer, C, et al. (2020, March). This Is Not a Test: APT41 Initiates Global Intrusion Campaign Using Multiple Exploits. Retrieved April 28, 2020.](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)
- [Crowdstrike. (2020, March 2). 2020 Global Threat Report. Retrieved December 11, 2020.](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)
- [Rostovcev, N. (2021, June 10). Big airline heist APT41 likely behind a third-party attack on Air India. Retrieved August 26, 2021.](https://www.group-ib.com/blog/colunmtk-apt41/)
- [Nikita Rostovcev. (2022, August 18). APT41 World Tour 2021 on a tight schedule. Retrieved February 22, 2024.](https://www.group-ib.com/blog/apt41-world-tour-2021/)
- [DCSO CyTec Blog. (2022, December 24). APT41 — The spy who failed to encrypt me. Retrieved June 13, 2024.](https://medium.com/@DCSO_CyTec/apt41-the-spy-who-failed-to-encrypt-me-24fc0f49cad1)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Wiley, B. et al. (2021, December 29). OverWatch Exposes AQUATIC PANDA in Possession of Log4Shell Exploit Tools During Hands-on Intrusion Attempt. Retrieved January 18, 2022.](https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Unit 42. (2025, December 11). Hamas-Affiliated Ashen Lepus Targets Middle Eastern Diplomatic Entities With New AshTag Malware Suite. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
- [Doaty, J., Garrett, P.. (2018, September 10). We’re Seeing a Resurgence of the Demonic Astaroth WMIC Trojan. Retrieved September 25, 2024.](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)
- [Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
- [GReAT. (2020, July 14). The Tetrade: Brazilian banking malware goes global. Retrieved November 9, 2020.](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)
- [Nyan-x-Cat. (n.d.). NYAN-x-CAT / AsyncRAT-C-Sharp. Retrieved October 3, 2023.](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)
- [Dominik Breitenbacher. (2025, March 18). Operation AkaiRyū: MirrorFace invites Europe to Expo 2025 and revives ANEL backdoor. Retrieved May 22, 2025.](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [Trend Micro. (2018, November 20). Lazarus Continues Heists, Mounts Attacks on Financial Organizations in Latin America. Retrieved December 3, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)
- [Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
- [Proofpoint. (2018, July 30). New version of AZORult stealer improves loading features, spreads alongside ransomware in new campaign. Retrieved November 29, 2018.](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)
- [Lim, M.. (2019, April 26). BabyShark Malware Part Two – Attacks Continue Using KimJongRAT and PCRat . Retrieved October 7, 2019.](https://unit42.paloaltonetworks.com/babyshark-malware-part-two-attacks-continue-using-kimjongrat-and-pcrat/)
- [CISA, FBI, CNMF. (2020, October 27). https://us-cert.cisa.gov/ncas/alerts/aa20-301a. Retrieved November 4, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-301a)
- [Hinchliffe, A. and Falcone, R. (2020, May 11). Updated BackConfig Malware Targeting Government and Military Organizations in South Asia. Retrieved June 17, 2020.](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)
- [Slowik, J. (2021, October). THE BAFFLING BERSERK BEAR: A DECADE’S ACTIVITY TARGETING CRITICAL INFRASTRUCTURE. Retrieved December 6, 2021.](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
- [Adam Burgher. (2021, June 10). BackdoorDiplomacy: Upgrading from Quarian to Turian. Retrieved September 1, 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
- [Accenture iDefense Unit. (2019, March 5). Mudcarp's Focus on Submarine Technologies. Retrieved August 24, 2021.](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
- [Savelesky, K., et al. (2019, July 23). ABADBABE 8BADFOOD: Discovering BADHATCH and a Detailed Look at FIN8's Tooling. Retrieved September 8, 2021.](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Levene, B. et al.. (2018, March 7). Patchwork Continues to Deliver BADNEWS to the Indian Subcontinent. Retrieved March 31, 2018.](https://researchcenter.paloaltonetworks.com/2018/03/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/)
- [Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
- [Bar, T., Conant, S. (2017, October 20). BadPatch. Retrieved November 13, 2018.](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)
- [Check Point. (2020, November 26). Bandook: Signed & Delivered. Retrieved May 31, 2021.](https://research.checkpoint.com/2020/bandook-signed-delivered/)
- [US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Sadique, M. and Singh, A. (2020, September 29). Spear Phishing Campaign Delivers Buer and Bazar Malware. Retrieved November 19, 2020.](https://www.zscaler.com/blogs/research/spear-phishing-campaign-delivers-buer-and-bazar-malware)
- [Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1, 2020.](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
- [Podlosky, A., Hanel, A. et al. (2020, October 16). WIZARD SPIDER Update: Resilient, Reactive and Resolute. Retrieved June 15, 2021.](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)
- [eSentire Threat Response Unit (TRU). (2024, November 14). Bored BeaverTail & InvisibleFerret Yacht Club – A Lazarus Lure Pt.2. Retrieved October 17, 2025.](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
- [Kirill Boychenko. (2025, July 14). Contagious Interview Campaign Escalates With 67 Malicious npm Packages and New Malware Loader. Retrieved October 19, 2025.](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Unit42. (2024, October 9). Contagious Interview: DPRK Threat Actors Lure Tech Industry Job Seekers to Install New Variants of BeaverTail and InvisibleFerret Malware. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
- [Harbison, M. (2021, February 9). BendyBear: Novel Chinese Shellcode Linked With Cyber Espionage Group BlackTech. Retrieved February 16, 2021.](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)
- [Mandiant. (n.d.). Appendix C (Digital) - The Malware Arsenal. Retrieved July 18, 2016.](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)
- [Hayashi, K., Ray, V. (2018, July 31). Bisonal Malware Used in Attacks Against Russia and South Korea. Retrieved August 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)
- [Zykov, K. (2020, August 13). CactusPete APT group’s updated Bisonal backdoor. Retrieved May 5, 2021.](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [Microsoft. (n.d.). BITSAdmin Tool. Retrieved January 12, 2018.](https://msdn.microsoft.com/library/aa362813.aspx)
- [Raghuprasad, C . (2022, May 11). Bitter APT adds Bangladesh to their targets. Retrieved June 1, 2022.](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)
- [Dela Paz, R. (2016, October 21). BITTER: a targeted attack against Pakistan. Retrieved June 1, 2022.](https://www.forcepoint.com/blog/x-labs/bitter-targeted-attack-against-pakistan)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [MSTIC. (2019, December 12). GALLIUM: Targeting global telecom. Retrieved January 13, 2021.](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)
- [US-CERT. (2020, August 19). MAR-10295134-1.v1 – North Korean Remote Access Trojan: BLINDINGCAN. Retrieved August 19, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [Wilhoit, K. and Falcone, R. (2018, September 12). OilRig Uses Updated BONDUPDATER to Target Middle Eastern Government. Retrieved February 18, 2019.](https://unit42.paloaltonetworks.com/unit42-oilrig-uses-updated-bondupdater-target-middle-eastern-government/)
- [MSTIC. (2021, May 28). Breaking down NOBELIUM’s latest early-stage toolset. Retrieved August 4, 2021.](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
- [CheckPoint Research. (2021, July 1). IndigoZebra APT continues to attack Central Asia with evolving tools. Retrieved September 24, 2021.](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
- [Ladley, F. (2012, May 15). Backdoor.Briba. Retrieved February 21, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-2843-99)
- [DHS/CISA. (2026, February 11). AR25-338A: BRICKSTORM Backdoor. Retrieved April 16, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
- [Matt Lin, Austin Larsen, John Wolfram, Ashley Pearson, Josh Murchie, Lukasz Lamparski, Joseph Pisano, Ryan Hall, Ron Craft, Shawn Crew, Billy Wong, Tyler McLellan. (2024, April 4). Cutting Edge, Part 4: Ivanti Connect Secure VPN Post-Exploitation Lateral Movement Case Studies. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
- [NVISO Incident Response. (2025, April 1). BRICKSTORM Backdoor Analysis: A Persistent Espionage Threat to European Industries. Retrieved April 16, 2026.](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)
- [Sarah Yoder, John Wolfram, Ashley Pearson, Doug Bienstock, Josh Madeley, Josh Murchie, Brad Slaybaugh, Matt Lin, Geoff Carstairs, Austin Larsen. (2025, September 24). Another BRICKSTORM: Stealthy Backdoor Enabling Espionage into Tech and Legal Sectors. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
- [Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)
- [Harbison, M. and Renals, P. (2022, July 5). When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors. Retrieved February 1, 2023.](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
- [Elkins, T. (2024, July 24). Malware Campaign Lures Users With Fake W2 Form. Retrieved September 13, 2024.](https://www.rapid7.com/blog/post/2024/07/24/malware-campaign-lures-users-with-fake-w2-form/)
- [Stolyarov, V. (2022, March 17). Exposing initial access broker with ties to Conti. Retrieved August 18, 2022.](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)
- [Merriman, K. and Trouerbach, P. (2022, April 28). This isn't Optimus Prime's Bumblebee but it's Still Transforming. Retrieved August 22, 2022.](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
- [Kamble, V. (2022, June 28). Bumblebee: New Loader Rapidly Assuming Central Position in Cyber-crime Ecosystem. Retrieved August 24, 2022.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)
- [Sushko, O. (2019, April 17). macOS Bundlore: Mac Virus Bypassing macOS Security Features. Retrieved June 30, 2020.](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
- [Lin, M. et al. (2024, January 31). Cutting Edge, Part 2: Investigating Ivanti Connect Secure VPN Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
- [Lin, M. et al. (2024, February 27). Cutting Edge, Part 3: Investigating Ivanti Connect Secure VPN Exploitation and Persistence Attempts. Retrieved March 1, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
- [Mandiant Israel Research Team. (2022, August 17). Suspected Iranian Actor Targeting Israeli Shipping, Healthcare, Government and Energy Sectors. Retrieved September 21, 2022.](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Venere, G. Neal, C. (2022, June 21). Avos ransomware group expands with new attack arsenal. Retrieved January 11, 2023.](https://blog.talosintelligence.com/avoslocker-new-arsenal/)
- [Costa, F. (2022, May 1). RaaS AvosLocker Incident Response Analysis. Retrieved January 11, 2023.](https://www.linkedin.com/pulse/raas-avoslocker-incident-response-analysis-fl%C3%A1vio-costa?trk=articles_directory)
- [Microsoft Defender Research Team. (2018, December 3). Analysis of cyberattack on U.S. think tanks, non-profits, public sector by unidentified attackers. Retrieved April 15, 2019.](https://www.microsoft.com/security/blog/2018/12/03/analysis-of-cyberattack-on-u-s-think-tanks-non-profits-public-sector-by-unidentified-attackers/)
- [Dunwoody, M., et al. (2018, November 19). Not So Cozy: An Uncomfortable Examination of a Suspected APT29 Phishing Campaign. Retrieved November 27, 2018.](https://www.fireeye.com/blog/threat-research/2018/11/not-so-cozy-an-uncomfortable-examination-of-a-suspected-apt29-phishing-campaign.html)
- [Parisi, T. (2022, December 2). Not a SIMulation: CrowdStrike Investigations Reveal Intrusion Campaign Targeting Telco and BPO Companies. Retrieved June 30, 2023.](https://www.crowdstrike.com/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/)
- [Pantig, J. (2018, July 30). OSX.Calisto. Retrieved September 7, 2018.](https://web.archive.org/web/20190111082249/https://www.symantec.com/security-center/writeup/2018-073014-2512-99?om_rssid=sr-latestthreats30days)
- [Falcone, R. and Miller-Osborn, J.. (2016, January 24). Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists. Retrieved February 10, 2016.](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
- [Pellegrino, G. (2025, December 16). BlindEagle Targets Colombian Government Agency with Caminho and DCRAT. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)
- [Falcone, R., Lee, B. (2018, November 20). Sofacy Continues Global Attacks and Wheels Out New ‘Cannon’ Trojan. Retrieved November 26, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
- [Giuliani, M., Allievi, A. (2011, February 28). Carberp - a modular information stealing trojan. Retrieved September 12, 2024.](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
- [Trusteer Fraud Prevention Center. (2010, October 7). Carberp Under the Hood of Carberp: Malware & Configuration Analysis. Retrieved July 15, 2020.](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)
- [Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
- [McCabe, A. (2020, January 23). The Fractured Statue Campaign: U.S. Government Agency Targeted in Spear-Phishing Attacks. Retrieved June 2, 2020.](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)
- [Grunzweig, J. and Wilhoit, K. (2018, November 29). The Fractured Block Campaign: CARROTBAT Used to Deliver Malware Targeting Southeast Asia. Retrieved June 2, 2020.](https://unit42.paloaltonetworks.com/unit42-the-fractured-block-campaign-carrotbat-malware-used-to-deliver-malware-targeting-southeast-asia/)
- [Marvi, A. et al.. (2023, March 16). Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation. Retrieved March 22, 2023.](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Microsoft. (2012, November 14). Certutil. Retrieved July 3, 2017.](https://technet.microsoft.com/library/cc732443.aspx)
- [LOLBAS. (n.d.). Certutil.exe. Retrieved July 31, 2019.](https://lolbas-project.github.io/lolbas/Binaries/Certutil/)
- [Salem, E. (2020, November 17). CHAES: Novel Malware Targeting Latin American E-Commerce. Retrieved June 30, 2021.](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Miller-Osborn, J. and Grunzweig, J.. (2017, February 16). menuPass Returns with New Malware and New Attacks Against Japanese Academics and Organizations. Retrieved March 1, 2017.](http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/)
- [Nakamura, Y.. (2017, February 17). ChChes - Malware that Communicates with C&C Servers Using Cookie Headers. Retrieved November 17, 2024.](https://blogs.jpcert.or.jp/en/2017/02/chches-malware--93d6.html)
- [FireEye iSIGHT Intelligence. (2017, April 6). APT10 (MenuPass Group): New Tools, Global Campaign Latest Manifestation of Longstanding Threat. Retrieved June 29, 2017.](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)
- [Cycraft. (2020, April 15). APT Group Chimera - APT Operation Skeleton key Targets Taiwan Semiconductor Vendors. Retrieved August 24, 2020..](https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [Lee, T., Hanzlik, D., Ahl, I. (2013, August 7). Breaking Down the China Chopper Web Shell - Part I. Retrieved March 27, 2015.](https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-i.html)
- [The Australian Cyber Security Centre (ACSC), the Canadian Centre for Cyber Security (CCCS), the New Zealand National Cyber Security Centre (NZ NCSC), CERT New Zealand, the UK National Cyber Security Centre (UK NCSC) and the US National Cybersecurity and Communications Integration Center (NCCIC). (2018, October 11). Joint report on publicly available hacking tools. Retrieved March 11, 2019.](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
- [Eoin Miller. (2021, March 23). Defending Against the Zero Day: Analyzing Attacker Behavior Post-Exploitation of Microsoft Exchange. Retrieved October 27, 2022.](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Alperovitch, D.. (2016, June 15). Bears in the Midst: Intrusion into the Democratic National Committee. Retrieved August 3, 2016.](https://www.crowdstrike.com/blog/bears-midst-intrusion-democratic-national-committee/)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Biderman, O. et al. (2022, October 3). REVEALING EMPEROR DRAGONFLY: NIGHT SKY AND CHEERSCRYPT - A SINGLE RANSOMWARE GROUP. Retrieved December 6, 2023.](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)
- [Microsoft. (n.d.). Copy. Retrieved April 26, 2016.](https://technet.microsoft.com/en-us/library/bb490886.aspx)
- [Positive Technologies. (2017, August 16). Cobalt Strikes Back: An Evolving Multinational Threat to Finance. Retrieved September 5, 2018.](https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-2017-eng.pdf)
- [Gorelik, M. (2018, October 08). Cobalt Group 2.0. Retrieved November 5, 2018.](https://blog.morphisec.com/cobalt-gang-2.0)
- [Mavis, N. (2020, September 21). The Art and Science of Detecting Cobalt Strike. Retrieved September 12, 2024.](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Thomas Reed. (2018, October 29). Mac cryptocurrency ticker app installs backdoors. Retrieved April 23, 2019.](https://blog.malwarebytes.com/threat-analysis/2018/10/mac-cryptocurrency-ticker-app-installs-backdoors/)
- [Burton, K. (n.d.). The Conficker Worm. Retrieved February 18, 2021.](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
- [Uptycs Threat Research Team. (2021, January 12). Confucius APT deploys Warzone RAT. Retrieved December 17, 2021.](https://www.uptycs.com/blog/confucius-apt-deploys-warzone-rat)
- [Lunghi, D. (2021, August 17). Confucius Uses Pegasus Spyware-related Lures to Target Pakistani Military. Retrieved December 26, 2021.](https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html)
- [Chen, y., et al. (2019, January 31). Mac Malware Steals Cryptocurrency Exchanges’ Cookies. Retrieved July 22, 2020.](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
- [FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [Microsoft. (2022, June 2). Exposing POLONIUM activity and infrastructure targeting Israeli organizations. Retrieved July 1, 2022.](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [N. Baisini. (2022, July 13). Transparent Tribe begins targeting education sector in latest campaign. Retrieved September 22, 2022.](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
- [Stokes, P. (2020, July 27). Four Distinct Families of Lazarus Malware Target Apple’s macOS Platform. Retrieved August 7, 2020.](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
- [Dahan, A. et al. (2020, November 2). Back to the Future: Inside the Kimsuky KGH Spyware Suite. Retrieved November 6, 2020.](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [Meltzer, M. et al. (2024, January 10). Active Exploitation of Two Zero-Day Vulnerabilities in Ivanti Connect Secure VPN. Retrieved February 27, 2024.](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/)
- [NCSC. (2022, February 23). Cyclops Blink Malware Analysis Report. Retrieved March 3, 2022.](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
- [Haquebord, F. et al. (2022, March 17). Cyclops Blink Sets Sights on Asus Routers. Retrieved March 17, 2022.](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)
- [Mabutas, G. (2020, May 11). New MacOS Dacls RAT Backdoor Shows Lazarus’ Multi-Platform Attack Capability. Retrieved August 10, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-dacls-rat-backdoor-show-lazarus-multi-platform-attack-capability/)
- [Threat Hunter Team. (2023, April 20). Daggerfly: APT Actor Targets Telecoms Company in Africa. Retrieved July 25, 2024.](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
- [SecureWorks 2019, August 27 LYCEUM Takes Center Stage in Middle East Campaign Retrieved. 2019/11/19](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)
- [TrendMicro. (2014, September 03). DARKCOMET. Retrieved November 6, 2018.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
- [Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Ernesto Fernández Provecho, Pham Duy Phuc, Ciana Driscoll & Vinoo Thomas. (2023, November 21). The Continued Evolution of the DarkGate Malware-as-a-Service. Retrieved February 9, 2024.](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
- [McGraw, T. (2024, December 4). Black Basta Ransomware Campaign Drops Zbot, DarkGate, and Custom Malware. Retrieved December 9, 2024.](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
- [Microsoft. (2016, June 9). Reverse-engineering DUBNIUM. Retrieved March 31, 2021.](https://www.microsoft.com/security/blog/2016/06/09/reverse-engineering-dubnium-2/)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [Chen, J. and Hsieh, M. (2017, November 7). REDBALDKNIGHT/BRONZE BUTLER’s Daserf Backdoor Now Using Steganography. Retrieved December 27, 2017.](http://blog.trendmicro.com/trendlabs-security-intelligence/redbaldknight-bronze-butler-daserf-backdoor-now-using-steganography/)
- [Ash, B., et al. (2018, June 26). RANCOR: Targeted Attacks in South East Asia Using PLAINTEE and DDKONG Malware Families. Retrieved July 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
- [McLellan, T. and Moore, J. et al. (2021, April 29). UNC2447 SOMBRAT and FIVEHANDS Ransomware: A Sophisticated Financial Threat. Retrieved June 2, 2021.](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Shivtarkar, N. and Kumar, A. (2022, June 9). Lyceum .NET DNS Backdoor. Retrieved June 23, 2022.](https://www.zscaler.com/blogs/security-research/lyceum-net-dns-backdoor)
- [Grunzweig, J. (2018, October 01). NOKKI Almost Ties the Knot with DOGCALL: Reaper Group Uses New Malware to Deploy RAT. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
- [Fishbein, N., Kajiloti, M.. (2020, July 28). Watch Your Containers: Doki Infecting Docker Servers in the Cloud. Retrieved March 30, 2021.](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
- [TheWover. (2019, May 9). donut. Retrieved March 25, 2022.](https://github.com/TheWover/donut)
- [ESET. (2016, October). En Route with Sednit - Part 3: A Mysterious Downloader. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part3.pdf)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part I. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [Cybereason Nocturnus Team. (2020, December 9). MOLERATS IN THE CLOUD: New Malware Arsenal Abuses Cloud Platforms in Middle East Espionage Campaign. Retrieved December 22, 2020.](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
- [Ilascu, I. (2020, December 14). Hacking group’s new malware abuses Google and Facebook services. Retrieved December 28, 2020.](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
- [NSA/FBI. (2020, August). Russian GRU 85th GTsSS Deploys Previously Undisclosed Drovorub Malware. Retrieved August 25, 2020.](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
- [Konstantin Zykov. (2019, September 23). Hello! My name is Dtrack. Retrieved January 20, 2021.](https://securelist.com/my-name-is-dtrack/93338/)
- [Hod Gavriel. (2019, November 21). Dtrack: In-depth analysis of APT on a nuclear power plant. Retrieved January 20, 2021.](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
- [Symantec Security Response. (2015, June 23). Dyre: Emerging threat on financial fraud landscape. Retrieved August 23, 2018.](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/dyre-emerging-threat.pdf)
- [GREAT. (2021, March 30). APT10: sophisticated multi-layered loader Ecipekac discovered in A41APT campaign. Retrieved June 17, 2021.](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
- [Rochberger, L. (2020, November 26). Cybereason vs. Egregor Ransomware. Retrieved December 30, 2020.](https://www.cybereason.com/blog/cybereason-vs-egregor-ransomware)
- [Bichet, J. (2020, November 12). Egregor – Prolock: Fraternal Twins ?. Retrieved January 6, 2021.](https://www.intrinsec.com/egregor-prolock/?cn-reloaded=1)
- [Ladley, F. (2012, May 15). Backdoor.Ritsol. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-3909-99)
- [Accenture Security. (2018, January 27). DRAGONFISH DELIVERS NEW FORM OF ELISE MALWARE TARGETING ASEAN DEFENCE MINISTERS’ MEETING AND ASSOCIATES. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)
- [Falcone, R. and Miller-Osborn, J.. (2015, December 18). Attack on French Diplomat Linked to Operation Lotus Blossom. Retrieved February 15, 2016.](http://researchcenter.paloaltonetworks.com/2015/12/attack-on-french-diplomat-linked-to-operation-lotus-blossom/)
- [Süleyman Özarslan, PhD; Pincus Security Inc.. (2020, July 14). An Analysis of Emotet Malware: PowerShell Unobfuscation. Retrieved November 25, 2024.](https://medium.com/picus-security/an-analysis-of-emotet-malware-powershell-unobfuscation-4f46b50dcf2b)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [LOLBAS. (n.d.). Esentutl.exe. Retrieved September 3, 2019.](https://lolbas-project.github.io/lolbas/Binaries/Esentutl/)
- [Marschalek, M.. (2014, December 16). EvilBunny: Malware Instrumented By Lua. Retrieved June 28, 2019.](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)
- [Porolli, M. (2020, July 9). More evil: A deep look at Evilnum and its toolset. Retrieved January 22, 2021.](https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/)
- [Adamitis, D. (2020, May 6). Phantom in the Command Shell. Retrieved November 17, 2024.](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
- [Cherepanov, A., Lipovsky, R. (2018, October 11). New TeleBots backdoor: First evidence linking Industroyer to NotPetya. Retrieved November 27, 2018.](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)
- [ANSSI. (2021, January 27). SANDWORM INTRUSION SET CAMPAIGN TARGETING CENTREON SYSTEMS. Retrieved March 30, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
- [Threat Intelligence and Research. (2015, March 30). VOLATILE CEDAR. Retrieved February 8, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
- [Somerville, L. and Toro, A. (2017, March 30). Playing Cat & Mouse: Introducing the Felismus Malware. Retrieved November 16, 2017.](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)
- [Patil, S. (2018, June 26). Microsoft Office Vulnerabilities Used to Distribute FELIXROOT Backdoor in Recent Campaign. Retrieved November 17, 2024.](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
- [Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [Sygnia Incident Response Team. (2022, January 5). TG2003: ELEPHANT BEETLE UNCOVERING AN ORGANIZED FINANCIAL-THEFT OPERATION. Retrieved February 9, 2023.](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)
- [Carr, N., et al. (2017, April 24). FIN7 Evolution and the Phishing LNK. Retrieved April 24, 2017.](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)
- [Department of Justice. (2018, August 01). HOW FIN7 ATTACKED AND STOLE DATA. Retrieved August 24, 2018.](https://www.justice.gov/opa/press-release/file/1084361/download)
- [Abdo, B., et al. (2022, April 4). FIN7 Power Hour: Adversary Archaeology and the Evolution of FIN7. Retrieved April 5, 2022.](https://www.mandiant.com/resources/evolution-of-fin7)
- [Gemini Advisory. (2022, January 13). FIN7 Uses Flash Drives to Spread Remote Access Trojan. Retrieved May 14, 2025.](https://geminiadvisory.io/fin7-flash-drives-spread-remote-access-trojan/)
- [Kizhakkinan, D., et al. (2016, May 11). Threat Actor Leverages Windows Zero-day Exploit in Payment Card Data Attacks. Retrieved February 12, 2018.](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html)
- [Martin Zugec. (2021, July 27). Deep Dive Into a FIN8 Attack - A Forensic Investigation. Retrieved September 1, 2021.](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [Ramin Nafisi. (2021, September 27). FoggyWeb: Targeted NOBELIUM malware leads to persistent backdoor. Retrieved October 4, 2021.](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
- [CISA. (2020, September 15). Iran-Based Threat Actor Exploits VPN Vulnerabilities. Retrieved December 21, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)
- [Adamitis, D. et al. (2019, June 4). It's alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign. Retrieved May 11, 2020.](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
- [Microsoft. (2021, July 21). ftp. Retrieved February 25, 2022.](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ftp)
- [N/A. (n.d.). ftp(1) - Linux man page. Retrieved February 25, 2022.](https://linux.die.net/man/1/ftp)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Cybereason Nocturnus. (2019, June 25). Operation Soft Cell: A Worldwide Campaign Against Telecommunications Providers. Retrieved July 18, 2019.](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)
- [Kasza, A. and Reichel, D. (2017, February 27). The Gamaredon Group Toolset Evolution. Retrieved March 1, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)
- [Kakara, H., Maruyama, E. (2020, April 17). Gamaredon APT Group Use Covid-19 Lure in Campaigns. Retrieved May 19, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/gamaredon-apt-group-use-covid-19-lure-in-campaigns/)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Microsoft Threat Intelligence Center. (2022, February 4). ACTINIUM targets Ukrainian organizations. Retrieved February 18, 2022.](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Venere, G. (2025, March 28). Gamaredon campaign abuses LNK files to distribute Remcos backdoor. Retrieved July 23, 2025.](https://blog.talosintelligence.com/gamaredon-campaign-distribute-remcos/)
- [Unit 42. (2022, December 20). Russia’s Trident Ursa (aka Gamaredon APT) Cyber Conflict Operations Unwavering Since Invasion of Ukraine. Retrieved September 12, 2024.](https://unit42.paloaltonetworks.com/trident-ursa/)
- [ESET. (2017, August). Gazing at Gazer: Turla’s new second stage backdoor. Retrieved September 14, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2017, August 30). Introducing WhiteBear. Retrieved September 21, 2017.](https://securelist.com/introducing-whitebear/81638/)
- [Pantazopoulos, N. (2018, April 17). Decoding network data from a Gh0st RAT variant. Retrieved November 2, 2018.](https://research.nccgroup.com/2018/04/17/decoding-network-data-from-a-gh0st-rat-variant/)
- [Quinn, J. (2019, March 25). The odd case of a Gh0stRAT variant. Retrieved July 15, 2020.](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
- [Gal Hachamov. (2025, December 29). GlassWorm Goes Mac: Fresh Infrastructure, New Tricks. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
- [Idan Dardikman, Yuval Ronen, Lotan Sery. (2025, November 6). GlassWorm Returns: New Wave Strikes as We Expose Attacker Infrastructure. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-returns-new-wave-openvsx-malware-expose-attacker-infrastructure)
- [Kirill Boychenko. (2026, January 31). GlassWorm Loader Hits Open VSX via Developer Account Compromise. Retrieved April 10, 2026.](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
- [Lotan Sery. (2025, December 10). GlassWorm Goes Native: Same Infrastructure, Hardened Delivery. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)
- [Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
- [Trustwave SpiderLabs. (2020, June 25). The Golden Tax Department and Emergence of GoldenSpy Malware. Retrieved July 23, 2020.](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [Smith, L., Leathery, J., Read, B. (2021, March 4). New SUNSHUTTLE Second-Stage Backdoor Uncovered Targeting U.S.-Based Entity; Possible Connection to UNC2452. Retrieved March 12, 2021.](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)
- [Szappanos, G. & Brandt, A. (2021, March 1). “Gootloader” expands its payload delivery options. Retrieved September 30, 2022.](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)
- [Pirozzi, A. (2021, June 16). Gootloader: ‘Initial Access as a Service’ Platform Expands Its Search for High Value Targets. Retrieved May 28, 2024.](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)
- [Falcone, R., et al. (2018, August 02). The Gorgon Group: Slithering Between Nation State and Cybercrime. Retrieved August 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)
- [Abramov, D. (2020, April 13). Grandoreiro Malware Now Targeting Banks in Spain. Retrieved November 12, 2020.](https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [Priego, A. (2021, July). THE BROTHERS GRIM: THE REVERSING TALE OF GRIMAGENT MALWARE USED BY RYUK. Retrieved September 19, 2024.](https://www.group-ib.com/blog/grimagent/)
- [Salem, E. (2021, April 19). Dancing With Shellcodes: Cracking the latest version of Guloader. Retrieved July 7, 2021.](https://elis531989.medium.com/dancing-with-shellcodes-cracking-the-latest-version-of-guloader-75083fb15cb4)
- [Reynolds, J.. (2016, September 14). H1N1: Technical analysis reveals new capabilities – part 2. Retrieved November 17, 2024.](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)
- [MSTIC. (2021, March 2). HAFNIUM targeting Exchange Servers with 0-day exploits. Retrieved March 3, 2021.](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/)
- [Tom Spring. (2017, January 11). Spammers Revive Hancitor Downloader Campaigns. Retrieved August 13, 2020.](https://threatpost.com/spammers-revive-hancitor-downloader-campaigns/123011/)
- [Symntec Threat Hunter Team. (2022, November 12). Billbug: State-sponsored Actor Targets Cert Authority, Government Agencies in Multiple Asian Countries. Retrieved March 15, 2025.](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
- [Ungur, P. (n.d.). HAVOC. Retrieved August 4, 2025.](https://havocframework.com/docs/welcome)
- [Immersive Content Team. (2024, April 9). Havoc C2 Framework – A Defensive Operator’s Guide. Retrieved August 13, 2025.](https://www.immersivelabs.com/resources/blog/havoc-c2-framework-a-defensive-operators-guide)
- [Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Kirill Boychenko. (2025, April 4). Lazarus Expands Malicious npm Campaign: 11 New Packages Add Malware Loaders and Bitbucket Payloads. Retrieved October 20, 2025.](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)
- [Fidelis Cybersecurity. (2015, December 16). Fidelis Threat Advisory #1020: Dissecting the Malware Involved in the INOCNATION Campaign. Retrieved November 17, 2024.](https://fidelissecurity.com/resource/report/fidelis-threat-advisory-1020-dissecting-the-malware-involved-in-the-inocnation-campaign/)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [Sanmillan, I. (2019, May 29). HiddenWasp Malware Stings Targeted Linux Systems. Retrieved June 24, 2019.](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)
- [Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
- [Chen, J. et al. (2021, February 3). Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes. Retrieved April 5, 2021.](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [MSTIC. (2022, September 8). Microsoft investigates Iranian attacks against the Albanian government. Retrieved August 6, 2024.](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [Knight, S.. (2020, April 16). VMware Carbon Black TAU Threat Analysis: The Evolution of Lazarus. Retrieved May 1, 2020.](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
- [Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)
- [Alexndru-Cristian Bardas. (2025, October 30). DPRK’s Playbook: Kimsuky’s HttpTroy and Lazarus’s New BLINDINGCAN Variant. Retrieved April 8, 2026.](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)
- [Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
- [Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
- [Falcone, R. and Lancaster, T. (2019, May 28). Emissary Panda Attacks Middle East Government Sharepoint Servers. Retrieved July 9, 2019.](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)
- [Kessem, L., et al. (2017, November 13). New Banking Trojan IcedID Discovered by IBM X-Force Research. Retrieved July 14, 2020.](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)
- [Kimayong, P. (2020, June 18). COVID-19 and FMLA Campaigns used to install new IcedID banking malware. Retrieved July 14, 2020.](https://blogs.juniper.net/en-us/threat-research/covid-19-and-fmla-campaigns-used-to-install-new-icedid-banking-malware)
- [DFIR. (2022, April 25). Quantum Ransomware. Retrieved July 26, 2024.](https://thedfirreport.com/2022/04/25/quantum-ransomware/)
- [Proofpoint Threat Research and Team Cymru S2 Threat Research. (2024, April 4). Latrodectus: This Spider Bytes Like Ice . Retrieved May 31, 2024.](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
- [PwC Threat Intelligence. (2023, October 25). Yellow Liderc ships its scripts and delivers IMAPLoader malware. Retrieved August 14, 2024.](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
- [Team Huntress. (2023, August 11). Investigating New INC Ransom Group Activity. Retrieved June 5, 2024.](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)
- [Carvey, H. (2024, May 1). LOLBin to INC Ransomware. Retrieved June 5, 2024.](https://www.huntress.com/blog/lolbin-to-inc-ransomware)
- [Frankoff, S., Hartley, B. (2018, November 14). Big Game Hunting: The Evolution of INDRIK SPIDER From Dridex Wire Fraud to BitPaymer Targeted Ransomware. Retrieved January 6, 2021.](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
- [Symantec Threat Intelligence. (2020, June 25). WastedLocker: Symantec Identifies Wave of Attacks Against U.S. Organizations. Retrieved May 20, 2021.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)
- [Mandiant Intelligence. (2022, June 2). To HADES and Back: UNC2165 Shifts to LOCKBIT to Evade Sanctions. Retrieved July 29, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)
- [Anton Cherepanov. (2017, June 12). Win32/Industroyer: A new threat for industrial controls systems. Retrieved December 18, 2020.](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
- [Seongsu Park. (2024, November 4). From Pyongyang to Your Payroll: The Rise of North Korean Remote Workers in the West. Retrieved October 17, 2025.](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Sancho, D., et al. (2012, May 22). IXESHE An APT Campaign. Retrieved June 7, 2019.](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
- [ESET. (2016, October). En Route with Sednit - Part 1: Approaching the Target. Retrieved November 8, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)
- [Lee, B, et al. (2018, February 28). Sofacy Attacks Multiple Government Entities. Retrieved March 15, 2018.](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)
- [Mercer, W., et al. (2017, October 22). "Cyber Conflict" Decoy Document Used in Real Cyber Conflict. Retrieved November 2, 2018.](https://blog.talosintelligence.com/2017/10/cyber-conflict-decoy-document.html)
- [Sharma, R. (2018, August 15). Revamped jRAT Uses New Anti-Parsing Techniques. Retrieved September 21, 2018.](https://www.symantec.com/blogs/threat-intelligence/jrat-new-anti-parsing-techniques)
- [Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
- [Bingham, J. (2013, February 11). Cross-Platform Frutas RAT Builder and Back Door. Retrieved April 23, 2019.](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)
- [Loui, E. and Reynolds, J. (2021, August 30). CARBON SPIDER Embraces Big Game Hunting, Part 1. Retrieved September 20, 2021.](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)
- [Yadav, A., et al. (2016, January 29). Malicious Office files dropping Kasidet and Dridex. Retrieved March 24, 2016.](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Ray, V. and Hayashi, K. (2019, February 1). Tracking OceanLotus’ new Downloader, KerrDown. Retrieved October 1, 2021.](https://unit42.paloaltonetworks.com/tracking-oceanlotus-new-downloader-kerrdown/)
- [Parys, B. (2017, February 11). The KeyBoys are back in town. Retrieved June 13, 2019.](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)
- [Guarnieri, C., Schloesser M. (2013, June 7). KeyBoy, Targeted Attacks against Vietnam and India. Retrieved June 14, 2019.](https://blog.rapid7.com/2013/06/07/keyboy-targeted-attacks-against-vietnam-and-india/)
- [US-CERT. (2018, August 09). MAR-10135536-17 – North Korean Trojan: KEYMARBLE. Retrieved August 16, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [Den Iuzvyk, Tim Peck. (2025, February 13). Analyzing DEEP#DRIVE: North Korean Threat Actors Observed Exploiting Trusted Platforms for Targeted Attacks. Retrieved August 19, 2025.](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Singer, G. (2020, April 3). Threat Alert: Kinsing Malware Attacks Targeting Container Environments. Retrieved April 1, 2021.](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
- [Bermejo, L., et al. (2017, June 22). Following the Trail of BlackTech’s Cyber Espionage Campaigns. Retrieved May 5, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
- [Magius, J., et al. (2017, July 19). Koadic. Retrieved September 27, 2024.](https://github.com/offsecginger/koadic)
- [Jazi, H. (2021, February). LazyScripter: From Empire to double RAT. Retrieved November 17, 2024.](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
- [Rascagneres, P. (2017, May 03). KONNI: A Malware Under The Radar For Years. Retrieved November 5, 2018.](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
- [Threat Intelligence Team. (2021, August 23). New variant of Konni malware used in campaign targetting Russia. Retrieved January 5, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
- [Black Lotus Labs. (2023, December 13). Routers Roasting On An Open Firewall: The KV-Botnet Investigation. Retrieved June 10, 2024.](https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/)
- [Moench, B. and Aboud, E. (2016, August 23). Trojan.Kwampirs. Retrieved May 10, 2018.](https://www.symantec.com/security-center/writeup/2016-081923-2700-99)
- [Stepanic, D. and Bousseaden, S. (2024, May 15). Spring Cleaning with LATRODECTUS: A Potential Replacement for ICEDID. Retrieved September 13, 2024.](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
- [Batista, J. (2024, June 17). Latrodectus, are you coming back?. Retrieved September 13, 2024.](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved November 17, 2024.](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)
- [Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle. Retrieved October 27, 2021.](https://securelist.com/lazarus-threatneedle/100803/)
- [Weidemann, A. (2021, January 25). New campaign targeting security researchers. Retrieved December 20, 2021.](https://blog.google/threat-analysis-group/new-campaign-targeting-security-researchers/)
- [Saini, A. and Hossein, J. (2022, January 27). North Korea’s Lazarus APT leverages Windows Update client, GitHub in latest campaign. Retrieved January 27, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)
- [Pradhan, A. (2022, February 8). LolZarus: Lazarus Group Incorporating Lolbins into Campaigns. Retrieved March 22, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)
- [Cherepanov, Anton. (2019, November 10). ESETresearch discovered a trojanized IDA Pro installer. Retrieved September 12, 2024.](https://x.com/ESETresearch/status/1458438155149922312)
- [Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
- [Faou, M. (2019, May). Turla LightNeuron: One email away from remote code execution. Retrieved June 24, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
- [Stuart Ashenbrenner, Alden Schmidt. (2024, April 25). LightSpy Malware Variant Targeting macOS. Retrieved January 3, 2025.](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
- [Zhou, R. (2012, May 15). Backdoor.Linfo. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Yamout, M. (2021, November 29). WIRTE’s campaign in the Middle East ‘living off the land’ since at least 2019. Retrieved February 1, 2022.](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [Bourhis, P., Sekoia TDR. (2024, February 1). Unveiling the intricacies of DiceLoader. Retrieved May 14, 2025.](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
- [Cocomazzi, Antonio. (2024, July 17). FIN7 Reboot | Cybercrime Gang Enhances Ops with New EDR Bypasses and Automated Attacks. Retrieved September 24, 2025.](https://www.sentinelone.com/labs/fin7-reboot-cybercrime-gang-enhances-ops-with-new-edr-bypasses-and-automated-attacks/)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part II. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
- [Breitenbacher, D. (2022, December 14). Unmasking MirrorFace: Operation LiberalFace targeting Japanese political entities. Retrieved April 17, 2026.](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
- [ITOCHU. (2024, January 24). The Endless Struggle Against APT10: Insights from LODEINFO v0.6.6 - v0.7.3 Analysis. Retrieved April 17, 2026.](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
- [Muhammad, I., Unterbrink, H.. (2021, January 6). A Deep Dive into Lokibot Infection Chain. Retrieved August 31, 2021.](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
- [Malik, M. (2019, June 20). LoudMiner: Cross-platform mining in cracked VST software. Retrieved May 18, 2020.](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)
- [FireEye Threat Intelligence. (2015, December 1). China-based Cyber Threat Group Uses Dropbox for Malware Communications and Targets Hong Kong Media Outlets. Retrieved December 4, 2015.](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)
- [Hsu, K. et al. (2020, June 24). Lucifer: New Cryptojacking and DDoS Hybrid Malware Exploiting High and Critical Vulnerabilities to Infect Windows Devices. Retrieved November 16, 2020.](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
- [Lechtik, M, and etl. (2021, July 14). LuminousMoth APT: Sweeping attacks for the chosen few. Retrieved October 20, 2022.](https://securelist.com/apt-luminousmoth/103332/)
- [Botezatu, B and etl. (2021, July 21). LuminousMoth - PlugX, File Exfiltration and Persistence Revisited. Retrieved October 20, 2022.](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Wardle, P. (2021, November 11). OSX.CDDS (OSX.MacMa). Retrieved June 30, 2022.](https://objective-see.org/blog/blog_0x69.html)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [Lee, B. and Falcone, R. (2017, February 15). Magic Hound Campaign Attacks Saudi Targets. Retrieved December 27, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)
- [DFIR Report. (2022, March 21). APT35 Automates Initial Access Using ProxyShell. Retrieved May 25, 2022.](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [MSTIC. (2021, November 16). Evolving trends in Iranian threat actor activity – MSTIC presentation at CyberWarCon 2021. Retrieved January 12, 2023.](https://www.microsoft.com/en-us/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021)
- [Asheer Malhotra, Vitor Ventura & Jungsoo An, Cisco Talos. (2022, September 7). MagicRAT: Lazarus’ latest gateway into victim networks. Retrieved December 30, 2024.](https://blog.talosintelligence.com/lazarus-magicrat/)
- [GReAT. (2021, June 16). Ferocious Kitten: 6 Years of Covert Surveillance in Iran. Retrieved September 22, 2021.](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
- [Secureworks. (2019, July 24). MCMD Malware Analysis. Retrieved August 13, 2020.](https://www.secureworks.com/research/mcmd-malware-analysis)
- [Falcone, R. (2019, March 4). New Python-Based Payload MechaFlounder Used by Chafer. Retrieved May 27, 2020.](https://unit42.paloaltonetworks.com/new-python-based-payload-mechaflounder-used-by-chafer/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper. Retrieved April 5, 2017.](https://web.archive.org/web/20220224041316/https:/www.pwc.co.uk/cyber-security/pdf/cloud-hopper-report-final-v4.pdf)
- [US District Court Southern District of New York. (2018, December 17). United States v. Zhu Hua Indictment. Retrieved December 17, 2020.](https://www.justice.gov/opa/page/file/1122671/download)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [Erlich, C. (2020, April 3). The Avast Abuser: Metamorfo Banking Malware Hides By Abusing Avast Executable. Retrieved May 26, 2020.](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
- [Sierra, E., Iglesias, G.. (2018, April 24). Metamorfo Campaigns Targeting Brazilian Users. Retrieved July 30, 2020.](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
- [Zhang, X. (2020, February 4). Another Metamorfo Variant Targeting Customers of Financial Institutions in More Countries. Retrieved July 30, 2020.](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
- [ESET Research. (2019, October 3). Casbaneiro: peculiarities of this banking Trojan that affects Brazil and Mexico. Retrieved September 23, 2021.](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
- [Check Point Research Team. (2021, August 14). Indra - Hackers Behind Recent Attacks on Iran. Retrieved February 17, 2022.](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
- [Rascagneres, P., Mercer, W. (2017, June 19). Delphi Used To Score Against Palestine. Retrieved November 13, 2018.](https://blog.talosintelligence.com/2017/06/palestine-delphi.html)
- [Tsarfaty, Y. (2018, July 25). Micropsia Malware. Retrieved November 13, 2018.](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
- [ClearSky Cyber Security . (2021, August). New Iranian Espionage Campaign By “Siamesekitten” - Lyceum. Retrieved June 6, 2022.](https://www.clearskysec.com/siamesekitten/)
- [Kaspersky Lab's Global Research & Analysis Team. (2013, February 27). The MiniDuke Mystery: PDF 0-day Government Spy Assembler 0x29A Micro Backdoor. Retrieved November 17, 2024.](https://web.archive.org/web/20170630181406/https://cdn.securelist.com/files/2014/07/themysteryofthepdf0-dayassemblermicrobackdoor.pdf)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Stama, D.. (2015, February 6). Backdoor.Mivast. Retrieved February 15, 2016.](http://www.symantec.com/security_response/writeup.jsp?docid=2015-020623-0740-99&tabid=2)
- [GReAT. (2019, April 10). Gaza Cybergang Group1, operation SneakyPastes. Retrieved May 13, 2020.](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
- [Falcone, R., et al. (2020, March 3). Molerats Delivers Spark Backdoor to Government and Telecommunications Organizations. Retrieved December 14, 2020.](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [Microsoft Threat Intelligence. (2024, May 28). Moonstone Sleet emerges as new North Korean threat actor with new bag of tricks. Retrieved August 26, 2024.](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)
- [Svajcer, V. (2018, July 31). Multiple Cobalt Personality Disorder. Retrieved September 5, 2018.](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)
- [Villadsen, O.. (2019, August 29). More_eggs, Anyone? Threat Actor ITG08 Strikes Again. Retrieved September 16, 2019.](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)
- [Checkpoint Research. (2021, November 15). Uncovering MosesStaff techniques: Ideology over Money. Retrieved August 11, 2022.](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
- [ESET, et al. (2018, January). Diplomats in Eastern Europe bitten by a Turla mosquito. Retrieved July 3, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
- [ESET Research. (2025, December 2). MuddyWater: Snakes by the riverbank. Retrieved February 17, 2026.](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 10). MuddyWater expands operations. Retrieved November 2, 2018.](https://securelist.com/muddywater/88059/)
- [ClearSky Cyber Security. (2018, November). MuddyWater Operations in Lebanon and Oman: Using an Israeli compromised domain for a two-stage campaign. Retrieved November 29, 2018.](https://www.clearskysec.com/wp-content/uploads/2018/11/MuddyWater-Operations-in-Lebanon-and-Oman.pdf)
- [Reaqta. (2017, November 22). A dive into MuddyWater APT targeting Middle-East. Retrieved May 18, 2020.](https://reaqta.com/2017/11/muddywater-apt-targeting-middle-east/)
- [Peretz, A. and Theck, E. (2021, March 5). Earth Vetala – MuddyWater Continues to Target Organizations in the Middle East. Retrieved March 18, 2021.](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
- [Naumaan, S., et al. (2025, April 17). Around the World in 90 Days: State-Sponsored Actors Try ClickFix . Retrieved January 21, 2026.](https://www.proofpoint.com/us/blog/threat-insight/around-world-90-days-state-sponsored-actors-try-clickfix)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Asheer Malhotra, Jungsoo An, Kendall Mc. (2022, May 5). Mustang Panda deploys a new wave of malware targeting Europe. Retrieved August 4, 2025.](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
- [Insikt Group. (2020, July 28). CHINESE STATE-SPONSORED GROUP ‘REDDELTA’ TARGETS THE VATICAN AND CATHOLIC ORGANIZATIONS. Retrieved April 13, 2021.](https://go.recordedfuture.com/hubfs/reports/cta-2020-0728.pdf)
- [Secureworks Counter Threat Unit Research Team. (2022, April 27). BRONZE PRESIDENT Targets Russian Speakers with Updated PlugX. Retrieved September 9, 2025.](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)
- [Tom Fakterman. (2024, September 6). Chinese APT Abuses VSCode to Target Government in Asia. Retrieved March 24, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage/)
- [Microsoft. (2022, May 9). Ransomware as a service: Understanding the cybercrime gig economy and how to protect yourself. Retrieved March 10, 2023.](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)
- [The DigiTrust Group. (2017, January 01). NanoCore Is Not Your Average RAT. Retrieved November 9, 2018.](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
- [Kasza, A., Halfpop, T. (2016, February 09). NanoCoreRAT Behind an Increase in Tax-Themed Phishing E-mails. Retrieved November 9, 2018.](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
- [Mercer, W., Rascagneres, P. (2018, May 31). NavRAT Uses US-North Korea Summit As Decoy For Attacks In South Korea. Retrieved June 11, 2018.](https://blog.talosintelligence.com/2018/05/navrat.html)
- [Vrabie, V. (2021, April 23). NAIKON – Traces from a Military Cyber-Espionage Operation. Retrieved June 29, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
- [L-Codes. (2019). Neo-reGeorg. Retrieved December 4, 2024.](https://github.com/L-codes/Neo-reGeorg/blob/master/README-en.md)
- [Szappanos, G., Brandt, A.. (2020, May 27). Netwalker ransomware tools give insight into threat actor. Retrieved May 27, 2020.](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)
- [Maniath, S. and Kadam P. (2019, March 19). Dissecting a NETWIRE Phishing Campaign's Usage of Process Hollowing. Retrieved January 7, 2021.](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
- [Proofpoint. (2020, December 2). Geofenced NetWire Campaigns. Retrieved January 7, 2021.](https://www.proofpoint.com/us/blog/threat-insight/geofenced-netwire-campaigns)
- [Rozmann, O., et al. (2024, May 1). Uncharmed: Untangling Iran's APT42 Operations. Retrieved October 9, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)
- [Sponchioni, R.. (2016, March 11). Backdoor.Nidiran. Retrieved August 3, 2016.](https://www.symantec.com/security_response/writeup.jsp?docid=2015-120123-5521-99)
- [McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
- [Fidelis Cybersecurity. (2013, June 28). Fidelis Threat Advisory #1009: "njRAT" Uncovered. Retrieved June 4, 2019.](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
- [Pascual, C. (2018, November 27). AutoIt-Compiled Worm Affecting Removable Media Delivers Fileless Version of BLADABINDI/njRAT Backdoor. Retrieved June 4, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
- [Global Research & Analysis Team, Kaspersky. (2024, August 19). BlindEagle flying high in Latin America. Retrieved April 16, 2026.](https://securelist.com/blindeagle-apt/113414/)
- [Grunzweig, J., Lee, B. (2018, September 27). New KONNI Malware attacking Eurasia and Southeast Asia. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
- [Cherepanov, A. (2018, October 4). Nomadic Octopus Cyber espionage in Central Asia. Retrieved October 13, 2021.](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 15). Octopus-infested seas of Central Asia. Retrieved November 14, 2018.](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
- [Paganini, P. (2018, October 16). Russia-linked APT group DustSquad targets diplomatic entities in Central Asia. Retrieved August 24, 2021.](https://securityaffairs.co/wordpress/77165/apt/russia-linked-apt-dustsquad.html)
- [Hromcova, Z. and Burgher, A. (2023, December 14). OilRig’s persistent attacks using cloud service-powered downloaders. Retrieved November 26, 2024.](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
- [Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
- [Fahmy, M. et al. (2024, October 11). Earth Simnavaz (aka APT34) Levies Advanced Cyberattacks Against Middle East. Retrieved November 27, 2024.](https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html)
- [Hromcova, Z. (2019, July). OKRUM AND KETRICAN: AN OVERVIEW OF RECENT KE3CHANG GROUP ACTIVITY. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
- [Lee, B., Falcone, R. (2018, February 23). OopsIE! OilRig Uses ThreeDollars to Deliver New Trojan. Retrieved July 16, 2018.](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)
- [Falcone, R., et al. (2018, September 04). OilRig Targets a Middle Eastern Government and Adds Evasion Techniques to OopsIE. Retrieved September 24, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)
- [Breitenbacher, D and Osis, K. (2020, June 17). OPERATION IN(TER)CEPTION: Targeted Attacks Against European Aerospace and Military Companies. Retrieved December 20, 2021.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_Operation_Interception.pdf)
- [Cashman, M. (2020, July 29). Operation North Star Campaign. Retrieved December 20, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-a-job-offer-thats-too-good-to-be-true/?hilite=%27Operation%27%2C%27North%27%2C%27Star%27)
- [Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-uncovers-operation-honeybee-malicious-document-campaign-targeting-humanitarian-aid-groups/)
- [Volexity Threat Research. (2024, April 12). Zero-Day Exploitation of Unauthenticated Remote Code Execution Vulnerability in GlobalProtect (CVE-2024-3400). Retrieved November 20, 2024.](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)
- [Unit 42. (2024, April 12). Threat Brief: Operation MidnightEclipse, Post-Exploitation Activity Related to CVE-2024-3400 . Retrieved January 15, 2025.](https://unit42.paloaltonetworks.com/cve-2024-3400/)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Carbon Black Threat Analysis Unit. (2019, February 12). New macOS Malware Variant of Shlayer (OSX) Discovered. Retrieved August 8, 2019.](https://blogs.vmware.com/security/2020/02/vmware-carbon-black-tau-threat-analysis-shlayer-macos.html)
- [Phil Stokes. (2020, September 8). Coming Out of Your Shell: From Shlayer to ZShlayer. Retrieved September 13, 2021.](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)
- [Phil Stokes. (2021, February 16). 20 Common Tools & Techniques Used by macOS Threat Actors & Malware. Retrieved August 23, 2021.](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
- [Patrick Wardle. (2020, August 30). Apple Approved Malware malicious code ...now notarized!? #2020. Retrieved September 13, 2021.](https://objective-see.com/blog/blog_0x4E.html)
- [Horejsi, J. (2018, April 04). New MacOS Backdoor Linked to OceanLotus Found. Retrieved November 13, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-backdoor-linked-to-oceanlotus-found/)
- [Magisa, L. (2020, November 27). New MacOS Backdoor Connected to OceanLotus Surfaces. Retrieved December 2, 2020.](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)
- [Hromcova, Z. and Burgher, A. (2023, September 21). OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes. Retrieved November 21, 2024.](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Lunghi, D. and Lu, K. (2021, April 9). Iron Tiger APT Updates Toolkit With Evolved SysUpdate Malware. Retrieved November 12, 2021.](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
- [Mullaney, C. & Honda, H. (2012, May 4). Trojan.Pasam. Retrieved February 22, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, July 8). The Dropping Elephant – aggressive cyber-espionage in the Asian region. Retrieved August 3, 2016.](https://securelist.com/the-dropping-elephant-actor/75328/)
- [Leonardo. (2020, May 29). MALWARE TECHNICAL INSIGHT TURLA “Penquin_x64”. Retrieved March 11, 2021.](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
- [John Wolfram, Josh Murchie, Matt Lin, Daniel Ainsworth, Robert Wallace, Dimiter Andonov, Dhanesh Kizhakkinan, Jacob Thompson. (2025, January 8). Ivanti Connect Secure VPN Targeted in New Zero-Day Exploitation. Retrieved April 14, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
- [Aleksandar Milenkoski, Luigi Martire. (2024, December 10). Operation Digital Eye | Chinese APT Compromises Critical Digital Infrastructure via Visual Studio Code Tunnels. Retrieved February 27, 2025.](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels/)
- [Tartare, M. et al. (2020, May 21). No “Game over” for the Winnti Group. Retrieved August 24, 2020.](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
- [Grunzweig, J., et al. (2016, May 24). New Wekby Attacks Use DNS Requests As Command and Control Mechanism. Retrieved August 17, 2016.](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
- [Kaplan, D, et al. (2017, June 7). PLATINUM continues to evolve, find ways to maintain invisibility. Retrieved February 19, 2018.](https://cloudblogs.microsoft.com/microsoftsecure/2017/06/07/platinum-continues-to-evolve-find-ways-to-maintain-invisibility/?source=mmpc)
- [Trend Micro Research. (2023, July 21). Ransomware Spotlight: Play. Retrieved September 24, 2024.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
- [Tomonaga, S. (2018, June 8). PLEAD Downloader Used by BlackTech. Retrieved May 6, 2020.](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
- [Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
- [DOJ. (2024, December 20). Mag. No. 24-mj-1387 AFFIDAVIT IN SUPPORT OF AN APPLICATION FOR A NINTH SEARCH AND SEIZURE WARRANT- IN THE MATTER OF THE SEARCH AND SEIZURE OF COMPUTERS IN THE UNITED STATES INFECTED WITH PLUGX MALWARE . Retrieved September 9, 2025.](https://www.justice.gov/archives/opa/media/1384136/dl)
- [Patrick Whitsell. (2025, August 25). Deception in Depth: PRC-Nexus Espionage Campaign Hijacks Web Traffic to Target Diplomats. Retrieved September 9, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)
- [Raggi, M. et al. (2022, March 7). The Good, the Bad, and the Web Bug: TA416 Increases Operational Tempo Against European Governments as Conflict in Ukraine Escalates. Retrieved March 16, 2022.](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)
- [Mercer, W, et al. (2020, April 16). PoetRAT: Python RAT uses COVID-19 lures to target Azerbaijan public and private sectors. Retrieved April 27, 2020.](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
- [Mercer, W. Rascagneres, P. Ventura, V. (2020, October 6). PoetRAT: Malware targeting public and private sector in Azerbaijan evolves . Retrieved April 9, 2021.](https://blog.talosintelligence.com/2020/10/poetrat-update.html)
- [Hayashi, K. (2005, August 18). Backdoor.Darkmoon. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)
- [hasherezade. (2016, April 11). No money, but Pony! From a mail to a trojan horse. Retrieved May 21, 2020.](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)
- [Dunwoody, M.. (2017, April 3). Dissecting One of APT29’s Fileless WMI and PowerShell Backdoors (POSHSPY). Retrieved April 5, 2017.](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)
- [Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
- [Symantec Threat Hunter Team. (2023, October 19). Crambus: New Campaign Targets Middle Eastern Government. Retrieved November 27, 2024.](https://www.security.com/threat-intelligence/crambus-middle-east-government)
- [Cybereason Nocturnus. (2022, February 1). PowerLess Trojan: Iranian APT Phosphorus Adds New PowerShell Backdoor for Espionage. Retrieved June 1, 2022.](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)
- [Miller, S., et al. (2017, March 7). FIN7 Spear Phishing Campaign Targets Personnel Involved in SEC Filings. Retrieved March 8, 2017.](https://web.archive.org/web/20180808125108/https:/www.fireeye.com/blog/threat-research/2017/03/fin7_spear_phishing.html)
- [Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
- [Symantec. (2022, January 31). Shuckworm Continues Cyber-Espionage Attacks Against Ukraine. Retrieved February 17, 2022.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shuckworm-gamaredon-espionage-ukraine)
- [Unit 42. (2022, February 3). Russia’s Gamaredon aka Primitive Bear APT Group Actively Targeting Ukraine. Retrieved February 21, 2022.](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)
- [Dex. (n.d.). New Mustang Panda’s campaing against Australia. Retrieved August 4, 2025.](https://lab52.io/blog/new-mustang-pandas-campaing-against-australia/)
- [Golo Muhr, Joshua Chung. (2025, June 23). Hive0154 aka Mustang Panda shifts focus on Tibetan community to deploy Pubload backdoor. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [Nick Dai, Vickie Su, Sunny Lu. (2022, November 18). Earth Preta Spear-Phishing Governments Worldwide. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
- [Robert Falcone. (2025, February 20). Stately Taurus Activity in Southeast Asia Links to Bookworm Malware. Retrieved July 21, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-uses-bookworm-malware/)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy: New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)
- [Gorelik, M.. (2019, June 10). SECURITY ALERT: FIN8 IS BACK IN BUSINESS, TARGETING THE HOSPITALITY INDUSTRY. Retrieved June 13, 2019.](http://blog.morphisec.com/security-alert-fin8-is-back)
- [Nicolas Verdier. (n.d.). Retrieved January 29, 2018.](https://github.com/n1nj4sec/pupy)
- [Dumont, R. (2022, June 13). Technical Analysis of PureCrypter: A Fully-Functional Loader Distributing Remote Access Trojans and Information Stealers. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
- [Check Point Research. (2025, March 10). Blind Eagle: …And Justice for All. Retrieved April 16, 2026.](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
- [Mendoza, E. et al. (2020, May 25). Qakbot Resurges, Spreads through VBS Files. Retrieved September 27, 2021.](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)
- [CS. (2020, October 7). Duck Hunting with Falcon Complete: A Fowl Banking Trojan Evolves, Part 2. Retrieved September 27, 2021.](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)
- [Trend Micro. (2020, December 17). QAKBOT: A decade-old malware still with new tricks. Retrieved November 17, 2024.](https://success.trendmicro.com/en-US/solution/KA-0011282)
- [Cyberint. (2021, May 25). Qakbot Banking Trojan. Retrieved September 27, 2021.](https://blog.cyberint.com/qakbot-banking-trojan)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [Group IB. (2020, September). LOCK LIKE A PRO. Retrieved November 17, 2024.](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
- [Microsoft Threat Intelligence. (2024, October 31). Chinese threat actor Storm-0940 uses credentials from password spray attacks from a covert network. Retrieved June 4, 2025.](https://www.microsoft.com/en-us/security/blog/2024/10/31/chinese-threat-actor-storm-0940-uses-credentials-from-password-spray-attacks-from-a-covert-network/)
- [MaxXor. (n.d.). QuasarRAT. Retrieved July 10, 2018.](https://github.com/quasar/QuasarRAT)
- [Meltzer, M, et al. (2018, June 07). Patchwork APT Group Targets US Think Tanks. Retrieved July 16, 2018.](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)
- [S2W TALON. (2022, June 16). Raccoon Stealer is Back with a New Version. Retrieved August 1, 2024.](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Aquino, M. (2013, June 13). RARSTONE Found In Targeted Attacks. Retrieved December 17, 2015.](http://blog.trendmicro.com/trendlabs-security-intelligence/rarstone-found-in-targeted-attacks/)
- [Patrick Schläpfer . (2024, April 10). Raspberry Robin Now Spreading Through Windows Script Files. Retrieved May 17, 2024.](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
- [Lauren Podber and Stef Rand. (2022, May 5). Raspberry Robin gets the worm early. Retrieved May 17, 2024.](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)
- [Lei, C., et al. (2018, January 24). Lazarus Campaign Targeting Cryptocurrencies Reveals Remote Controller Tool, an Evolved RATANKBA, and More. Retrieved May 22, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)
- [Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
- [Global Threat Center, Intelligence Team. (2020, December). APT27 Turns to Ransomware. Retrieved November 12, 2021.](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
- [Falcone, R. (2020, July 22). OilRig Targets Middle Eastern Telecommunications Organization and Adds Novel C2 Channel with Steganography to Its Inventory. Retrieved July 28, 2020.](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [George Glass. (2024, August 14). REDLINESTEALER Malware Driving the Initial Access Broker Market. Retrieved September 17, 2025.](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
- [Yair Herling. (2023, April 4). From ChatGPT to RedLine Stealer: The Dark Side of OpenAI and Google Bard. Retrieved September 17, 2025.](https://veriti.ai/blog/veriti-research/from-chatgpt-to-redline-stealer-the-dark-side-of-openai-and-google-bard/)
- [Lamparski, L. et al. (2025, March 11). Ghost in the Router: China-Nexus Espionage Actor UNC3886 Targets Juniper Routers. Retrieved June 24, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers)
- [Klijnsma, Y. (2018, January 23). Espionage Campaign Leverages Spear Phishing, RATs Against Turkish Defense Contractors. Retrieved November 6, 2018.](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
- [Symantec Security Response. (2016, August 8). Backdoor.Remsec indicators of compromise. Retrieved August 17, 2016.](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/Symantec_Remsec_IOCs.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
- [Livelli, K, et al. (2018, November 12). Operation Shaheen. Retrieved May 1, 2019.](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
- [Cadieux, P, et al (2019, April 30). Sodinokibi ransomware exploits WebLogic Server vulnerability. Retrieved August 4, 2020.](https://blog.talosintelligence.com/2019/04/sodinokibi-ransomware-exploits-weblogic.html)
- [McAfee. (2019, October 2). McAfee ATR Analyzes Sodinokibi aka REvil Ransomware-as-a-Service – What The Code Tells Us. Retrieved August 4, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
- [Ozarslan, S. (2020, January 15). A Brief History of Sodinokibi. Retrieved August 5, 2020.](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)
- [Falcone, R. (2018, January 25). OilRig uses RGDoor IIS Backdoor on Targets in the Middle East. Retrieved July 6, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-oilrig-uses-rgdoor-iis-backdoor-targets-middle-east/)
- [Punsaen Boonyakarn, Shawn Chew, Logeswaran Nadarajan, Mathew Potaczek, Jakub Jozwiak, and Alex Marvi. (2024, June 18). Cloaked and Covert: Uncovering UNC3886 Espionage Operations. Retrieved September 24, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [Liebenberg, D.. (2018, August 30). Rocke: The Champion of Monero Miners. Retrieved May 26, 2020.](https://blog.talosintelligence.com/2018/08/rocke-champion-of-monero-miners.html)
- [Falcone, R., et al. (2018, July 27). New Threat Actor Group DarkHydrus Targets Middle East Government. Retrieved August 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
- [Lee, B., Falcone, R. (2019, January 18). DarkHydrus delivers new Trojan that can use Google Drive for C2 communications. Retrieved April 17, 2019.](https://unit42.paloaltonetworks.com/darkhydrus-delivers-new-trojan-that-can-use-google-drive-for-c2-communications/)
- [Mercer, W., Rascagneres, P. (2017, April 03). Introducing ROKRAT. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)
- [Pantazopoulos, N.. (2018, November 8). RokRat Analysis. Retrieved May 21, 2020.](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
- [Jazi, Hossein. (2021, January 6). Retrohunting APT37: North Korean APT used VBA self decode technique to inject RokRat. Retrieved March 22, 2022.](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
- [Faou, M. and Boutin, J. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
- [Duncan, B., Harbison, M. (2019, January 23). Russian Language Malspam Pushing Redaman Banking Malware. Retrieved June 16, 2020.](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
- [Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, July 30). Sakula Malware Family. Retrieved January 26, 2016.](http://www.secureworks.com/cyber-threat-intelligence/threats/sakula-malware-family/)
- [Cherepanov, A.. (2016, December 13). The rise of TeleBots: Analyzing disruptive KillDisk attacks. Retrieved June 10, 2020.](https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/)
- [Scott W. Brady. (2020, October 15). United States vs. Yuriy Sergeyevich Andrienko et al.. Retrieved November 25, 2020.](https://www.justice.gov/opa/press-release/file/1328521/download)
- [Budaca, E., et al. (2021, August 25). FIN8 Threat Actor Goes Agile with New Sardonic Backdoor. Retrieved August 9, 2023.](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
- [Mandiant Incident Response. (2025, July 23). From Help Desk to Hypervisor: Defending Your VMware vSphere Estate from UNC3944. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)
- [Schwarz, D. et al. (2019, October 16). TA505 Distributes New SDBbot Remote Access Trojan with Get2 Downloader. Retrieved May 29, 2020.](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
- [Grunzweig, J.. (2015, July 14). Unit 42 Technical Analysis: Seaduke. Retrieved August 3, 2016.](http://researchcenter.paloaltonetworks.com/2015/07/unit-42-technical-analysis-seaduke/)
- [Davis, S. and Caban, D. (2017, December 19). APT34 - New Targeted Attack in the Middle East. Retrieved December 20, 2017.](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)
- [Schwarz, D. and Proofpoint Staff. (2019, January 9). ServHelper and FlawedGrace - New malware introduced by TA505. Retrieved May 28, 2019.](https://www.proofpoint.com/us/threat-insight/post/servhelper-and-flawedgrace-new-malware-introduced-ta505)
- [Vilkomir-Preisman, S. (2019, April 2). New ServHelper Variant Employs Excel 4.0 Macro to Drop Signed Payload. Retrieved September 16, 2024..](https://www.deepinstinct.com/blog/new-servhelper-variant-employs-excel-4-0-macro-to-drop-signed-payload)
- [Centero, R. et al. (2021, February 5). New in Ransomware: Seth-Locker, Babuk Locker, Maoloa, TeslaCrypt, and CobraLocker. Retrieved August 11, 2021.](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)
- [GReAT. (2017, August 15). ShadowPad in corporate networks. Retrieved March 22, 2021.](https://securelist.com/shadowpad-in-corporate-networks/81432/)
- [Lumelsly, A. et al. (2024, March 26). ShadowRay: First Known Attack Campaign Targeting AI Workloads Actively Exploited In The Wild. Retrieved December 2, 2024.](https://www.oligo.security/blog/shadowray-attack-ai-workloads-actively-exploited-in-the-wild)
- [Charlie Eriksen. (2025, September 16). S1ngularity/nx attackers strike again. Retrieved April 9, 2026.](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
- [Merav Bar, Rami McCarthy, Barak Sharoni. (2025, September 16). Shai-Hulud: Ongoing Package Supply Chain Worm Delivering Data-Stealing Malware. Retrieved April 9, 2026.](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)
- [Socket Research Team. (2025, November 24). Shai Hulud Strikes Again (v2). Retrieved April 9, 2026.](https://socket.dev/blog/shai-hulud-strikes-again-v2)
- [Socket Research Team. (2025, September 15). Popular Tinycolor npm Package Compromised in Supply Chain Attack Affecting 40+ Packages. Retrieved April 9, 2026.](https://socket.dev/blog/tinycolor-supply-chain-attack-affects-40-packages)
- [Gianpietro Cutolo. (2025, November 26). Shai-Hulud 2.0: Aggressive, Automated, and Fast Spreading. Retrieved April 9, 2026.](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
- [Microsoft Defender Security Team. (n.d.). Shai-Hulud 2.0: Guidance for detecting, investigating, and defending against the supply chain attack. Retrieved April 9, 2026.](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/)
- [Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [Unit 42. (2025, July 31). Active Exploitation of Microsoft SharePoint Vulnerabilities: Threat Brief (Updated). Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/microsoft-sharepoint-cve-2025-49704-cve-2025-49706-cve-2025-53770/)
- [Accenture. (2021, November 9). Who are latest targets of cyber group Lyceum?. Retrieved June 16, 2022.](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)
- [Lunghi, D. and Horejsi, J.. (2019, June 10). MuddyWater Resurfaces, Uses Multi-Stage Backdoor POWERSTATS V3 and New Post-Exploitation Tools. Retrieved May 14, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [Hegel, T. (2021, January 13). A Global Perspective of the SideWinder APT. Retrieved January 27, 2021.](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)
- [Cyble. (2020, September 26). SideWinder APT Targets with futuristic Tactics and Techniques. Retrieved January 29, 2021.](https://cybleinc.com/2020/09/26/sidewinder-apt-targets-with-futuristic-tactics-and-techniques/)
- [Group-IB. (2018, September). Silence: Moving Into the Darkside. Retrieved May 5, 2020.](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [Remillano, A., Urbanec, J. (2019, September 19). Skidmap Linux Malware Uses Rootkit Capabilities to Hide Cryptocurrency-Mining Payload. Retrieved June 4, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
- [Perez, D. et al. (2021, May 27). Re-Checking Your Pulse: Updates on Chinese APT Actors Compromising Pulse Secure VPN Devices. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
- [BishopFox. (n.d.). Sliver Upload. Retrieved September 16, 2021.](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/filesystem/upload.go)
- [Cybereason Global SOC and Incident Response Team. (n.d.). Sliver C2 Leveraged by Many Threat Actors. Retrieved March 24, 2025.](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [NCSC GCHQ. (2022, January 27). Small Sieve Malware Analysis Report. Retrieved August 22, 2022.](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)
- [Hasherezade. (2016, September 12). Smoke Loader – downloader with a smokescreen still alive. Retrieved March 20, 2018.](https://blog.malwarebytes.com/threat-analysis/2016/08/smoke-loader-downloader-with-a-smokescreen-still-alive/)
- [FireEye. (2021, June 16). Smoking Out a DARKSIDE Affiliate’s Supply Chain Software Compromise. Retrieved September 22, 2021.](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
- [Lorber, N. (2021, May 7). Revealing the Snip3 Crypter, a Highly Evasive RAT Loader. Retrieved September 13, 2023.](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
- [Jornet, A. (2021, December 23). Snip3, an investigation into malware. Retrieved September 19, 2023.](https://telefonicatech.com/blog/snip3-investigacion-malware)
- [Red Canary. (2024, March). Red Canary 2024 Threat Detection Report: SocGholish. Retrieved March 22, 2024.](https://redcanary.com/threat-detection-report/threats/socgholish/)
- [Secureworks. (n.d.). GOLD PRELUDE . Retrieved March 22, 2024.](https://www.secureworks.com/research/threat-profiles/gold-prelude)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [CISA. (2020, July 16). MAR-10296782-1.v1 – SOREFANG. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
- [National Cyber Security Centre. (2020, July 16). Advisory: APT29 targets COVID-19 vaccine development. Retrieved September 29, 2020.](https://www.ncsc.gov.uk/files/Advisory-APT29-targets-COVID-19-vaccine-development-V1-1.pdf)
- [Check Point Research. (2019, February 4). SpeakUp: A New Undetected Backdoor Linux Trojan. Retrieved April 17, 2019.](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
- [Shields, W. (2024, January 18). Russian threat group COLDRIVER expands its targeting of Western officials to include the use of malware. Retrieved June 13, 2024.](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)
- [CTU. (2018, September 27). Cybercriminals Increasingly Trying to Ensnare the Big Financial Fish. Retrieved September 20, 2021.](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)
- [Platt, J. and Reeves, J.. (2019, March). FIN7 Revisited: Inside Astra Panel and SQLRat Malware. Retrieved June 18, 2019.](https://www.flashpoint-intel.com/blog/fin7-revisited-inside-astra-panel-and-sqlrat-malware/)
- [Kumar, A., Stone-Gross, Brett. (2021, September 28). Squirrelwaffle: New Loader Delivering Cobalt Strike. Retrieved August 9, 2022.](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
- [Palazolo, G. (2021, October 7). SquirrelWaffle: New Malware Loader Delivering Cobalt Strike and QakBot. Retrieved August 9, 2022.](https://www.netskope.com/blog/squirrelwaffle-new-malware-loader-delivering-cobalt-strike-and-qakbot)
- [Perez, D. et al. (2021, April 20). Check Your Pulse: Suspected APT Actors Leverage Authentication Bypass Techniques and Pulse Secure Zero-Day. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
- [Kaspersky Lab. (2017, March 7). From Shamoon to StoneDrill: Wipers attacking Saudi organizations and beyond. Retrieved March 14, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
- [Microsoft Threat Intelligence. (2024, May 15). Threat actors misusing Quick Assist in social engineering attacks leading to ransomware. Retrieved March 14, 2025.](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)
- [Tyler McGraw, Thomas Elkins, and Evan McCann. (2024, May 10). Ongoing Social Engineering Campaign Linked to Black Basta Ransomware Operators. Retrieved January 31, 2025.](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)
- [The Red Canary Team. (2024, June 20). Intelligence Insights: June 2024. Retrieved March 14, 2025.](https://redcanary.com/blog/threat-intelligence/intelligence-insights-june-2024/)
- [Golo Mühr, Joe Fasulo & Charlotte Hammond, IBM X-Force. (2024, November 12). Strela Stealer: Today’s invoice is tomorrow’s phish. Retrieved December 31, 2024.](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
- [Cybereason Nocturnus. (2022, February 1). StrifeWater RAT: Iranian APT Moses Staff Adds New Trojan to Ransomware Operations. Retrieved August 15, 2022.](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
- [Tudorica, R. et al. (2020, June 30). StrongPity APT - Revealing Trojanized Tools, Working Hours and Infrastructure. Retrieved July 20, 2020.](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [Gallagher, S., Gn, S. (2020, December 16). Ransomware operators use SystemBC RAT as off-the-shelf Tor backdoor. Retrieved May 16, 2025.](https://news.sophos.com/en-us/2020/12/16/systembc/)
- [Truman, D. (2024, January 19). Inside the SYSTEMBC Command-and-Control Server. Retrieved June 18, 2025.](https://www.kroll.com/en/publications/cyber/inside-the-systembc-malware-server)
- [Daniel Lunghi. (2023, March 1). Iron Tiger’s SysUpdate Reappears, Adds Linux Targeting. Retrieved March 20, 2023.](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
- [Ventura, V. (2021, September 16). Operation Layover: How we tracked an attack on the aviation industry to five years of compromise. Retrieved September 15, 2023.](https://blog.talosintelligence.com/operation-layover-how-we-tracked-attack/)
- [Salem, E. (2019, April 25). Threat Actor TA505 Targets Financial Enterprises Using LOLBins and a New Backdoor Malware. Retrieved May 28, 2019.](https://www.cybereason.com/blog/threat-actor-ta505-targets-financial-enterprises-using-lolbins-and-a-new-backdoor-malware)
- [Proofpoint Staff. (2018, July 19). TA505 Abusing SettingContent-ms within PDF files to Distribute FlawedAmmyy RAT. Retrieved April 19, 2019.](https://www.proofpoint.com/us/threat-insight/post/ta505-abusing-settingcontent-ms-within-pdf-files-distribute-flawedammyy-rat)
- [Duncan, B. (2021, January 7). TA551: Email Attack Campaign Switches from Valak to IcedID. Retrieved March 17, 2021.](https://unit42.paloaltonetworks.com/ta551-shathak-icedid/)
- [Trend Micro. (2012). The Taidoor Campaign. Retrieved November 12, 2014.](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)
- [USG. (2020, May 12). MAR-10288834-2.v1 – North Korean Trojan: TAINTEDSCRIBE. Retrieved March 5, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
- [ClearSky Cyber Security and Trend Micro. (2017, July). Operation Wilted Tulip: Exposing a cyber espionage apparatus. Retrieved August 21, 2017.](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)
- [Fishbein, N. (2020, September 8). Attackers Abusing Legitimate Cloud Monitoring Tools to Conduct Cyber Attacks. Retrieved September 22, 2021.](https://www.intezer.com/blog/cloud-security/attackers-abusing-legitimate-cloud-monitoring-tools-to-conduct-cyber-attacks/)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Patrick Wardle. (2020, July 3). OSX.EvilQuest Uncovered part ii: insidious capabilities. Retrieved March 21, 2021.](https://objective-see.com/blog/blog_0x60.html)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Cisco Talos. (2021, September 21). TinyTurla - Turla deploys new malware to keep a secret backdoor on victim machines. Retrieved December 2, 2021.](https://blog.talosintelligence.com/2021/09/tinyturla.html)
- [Kwiatkoswki, I. and Delcher, P. (2021, September 29). DarkHalo After SolarWinds: the Tomiris connection. Retrieved December 27, 2021.](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/)
- [Lior Rochberger, Tom Fakterman, Robert Falcone. (2023, September 22). Cyberespionage Attacks Against Southeast Asian Government Linked to Stately Taurus, Aka Mustang Panda. Retrieved September 9, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)
- [Faou, M., Tartare, M., Dupuy, T. (2021, March 10). Exchange servers under siege from at least 10 APT groups. Retrieved May 21, 2021.](https://www.welivesecurity.com/2021/03/10/exchange-servers-under-siege-10-apt-groups/)
- [Antazo, F. (2016, October 31). TSPY_TRICKLOAD.N. Retrieved September 14, 2018.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/tspy_trickload.n)
- [Radu Tudorica. (2021, July 12). A Fresh Look at Trickbot’s Ever-Improving VNC Module. Retrieved September 28, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/399/Bitdefender-PR-Whitepaper-Trickbot-creat5515-en-EN.pdf)
- [Symantec Security Response. (2014, June 30). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
- [Secureworks. (2019, July 24). Updated Karagany Malware Targets Energy Sector. Retrieved August 12, 2020.](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Tomonaga, S. (2018, March 6). Malware “TSCookie”. Retrieved May 6, 2020.](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
- [Ubiedo, L. (2025, November 20). Blockchain and Node.js abused by Tsundere: an emerging botnet. Retrieved April 6, 2026.](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)
- [ESET Research. (2018, May 22). Turla Mosquito: A shift towards more generic tools. Retrieved July 3, 2018.](https://www.welivesecurity.com/2018/05/22/turla-mosquito-shift-towards-generic-tools/)
- [O'Leary, J., et al. (2017, September 20). Insights into Iranian Cyber Espionage: APT33 Targets Aerospace and Energy Sectors and has Ties to Destructive Malware. Retrieved February 15, 2018.](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)
- [US-CERT. (2018, June 14). MAR-10135536-12 – North Korean Trojan: TYPEFRAME. Retrieved July 13, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
- [Hayashi, K. (2017, November 28). UBoatRAT Navigates East Asia. Retrieved January 12, 2018.](https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/)
- [Matsuda, A., Muhammad I. (2018, September 13). APT10 Targeting Japanese Corporations Using Updated TTPs. Retrieved September 17, 2018.](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
- [Hiroaki, H. (2025, April 30). Earth Kasha Updates TTPs in Latest Campaign Targeting Taiwan and Japan. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
- [Hiroaki, H. (2024, November 26). Guess Who’s Back - The Return of ANEL in the Recent Earth Kasha Spear-phishing Campaign in 2024. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Trend Micro. (2014, December 11). PE_URSNIF.A2. Retrieved June 5, 2019.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/PE_URSNIF.A2?_ga=2.131425807.1462021705.1559742358-1202584019.1549394279)
- [Sioting, S. (2013, June 15). BKDR_URSNIF.SM. Retrieved June 5, 2019.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
- [Duncan, B. (2020, July 24). Evolution of Valak, from Its Beginnings to Mass Distribution. Retrieved August 31, 2020.](https://unit42.paloaltonetworks.com/valak-evolution/)
- [Salem, E. et al. (2020, May 28). VALAK: MORE THAN MEETS THE EYE . Retrieved June 19, 2020.](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
- [Zhou, R. (2012, May 15). Backdoor.Vasport. Retrieved February 22, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-5938-99)
- [GReAT. (2019, August 12). Recent Cloud Atlas activity. Retrieved May 8, 2020.](https://securelist.com/recent-cloud-atlas-activity/92016/)
- [Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
- [Alexander Marvi, Jeremy Koppen, Tufail Ahmed, and Jonathan Lepore. (2022, September 29). Bad VIB(E)s Part One: Investigating Novel Malware Persistence Within ESXi Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
- [Check Point Research. (2026, March 12). “Handala Hack” – Unveiling Group’s Modus Operandi. Retrieved April 20, 2026.](https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/)
- [DOJ/FBI. (2026, March 19). Case 1:26-mj-00683-CDA: Affidavit in Support of Seizure Warrant: In the Matter of the Seizure of Domain Names Justicehomeland[.]org; karmabelow80[.]org; handala-hack[.]to; and handala-redwatned[.]to. Retrieved April 20, 2026.](https://www.justice.gov/opa/media/1431956/dl?inline)
- [FBI. (2026, March 20). FBI Flash: FLASH-20260320-001:Government of Iran Cyber Actors Deploy Telegram C2 to Push Malware to Identified Targets. Retrieved April 20, 2026.](https://www.ic3.gov/CSA/2026/260320.pdf)
- [US-CERT. (2017, November 22). Alert (TA17-318B): HIDDEN COBRA – North Korean Trojan: Volgmer. Retrieved December 7, 2017.](https://www.us-cert.gov/ncas/alerts/TA17-318B)
- [US-CERT. (2017, November 01). Malware Analysis Report (MAR) - 10135536-D. Retrieved July 16, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)
- [Yagi, J. (2014, August 24). Trojan.Volgmer. Retrieved July 16, 2018.](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [Shinji Robert Arasawa, Joshua Aquino, Charles Steven Derion, Juhn Emmanuel Atanque, Francisrey Joshua Castillo, John Carlo Marquez, Henry Salcedo, John Rainier Navato, Arianne Dela Cruz, Raymart Yambot & Ian Kenefick. (2024, January 9). Black Basta-Affiliated Water Curupira’s Pikabot Spam Campaign. Retrieved July 17, 2024.](https://www.trendmicro.com/en_us/research/24/a/a-look-into-pikabot-spam-wave-campaign.html)
- [Su, V. et al. (2019, December 11). Waterbear Returns, Uses API Hooking to Evade Security. Retrieved February 22, 2021.](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [CISA. (2020, July 16). MAR-10296782-3.v1 – WELLMAIL. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
- [CISA. (2020, July 16). MAR-10296782-2.v1 – WELLMESS. Retrieved September 24, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)
- [MSTIC. (2022, January 15). Destructive malware targeting Ukrainian organizations. Retrieved March 10, 2022.](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)
- [Falcone, R. et al.. (2022, January 20). Threat Brief: Ongoing Russia and Ukraine Cyber Conflict. Retrieved March 10, 2022.](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)
- [Biasini, N. et al.. (2022, January 21). Ukraine Campaign Delivers Defacement and Wipers, in Continued Escalation. Retrieved March 14, 2022.](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
- [S2W. (2022, January 18). Analysis of Destructive Malware (WhisperGate) targeting Ukraine. Retrieved March 14, 2022.](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)
- [Symantec. (2019, March 6). Whitefly: Espionage Group has Singapore in Its Sights. Retrieved May 26, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/whitefly-espionage-singapore)
- [Zhou, R. (2012, May 15). Backdoor.Wiarp. Retrieved February 22, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-1005-99)
- [The BlackBerry Research & Intelligence Team. (2020, October). BAHAMUT: Hack-for-Hire Masters of Phishing, Fake News, and Fake Apps. Retrieved February 8, 2021.](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)
- [Chronicle Blog. (2019, May 15). Winnti: More than just Windows and Gates. Retrieved April 29, 2020.](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)
- [Novetta Threat Research Group. (2015, April 7). Winnti Analysis. Retrieved February 8, 2017.](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
- [Kaspersky Lab's Global Research and Analysis Team. (2013, April 11). Winnti. More than just a game. Retrieved February 8, 2017.](https://securelist.com/winnti-more-than-just-a-game/37029/)
- [Chad Anderson. (2021, April 27). Winter Vivern: A Look At Re-Crafted Government MalDocs Targeting Multiple Languages. Retrieved July 29, 2024.](https://www.domaintools.com/resources/blog/winter-vivern-a-look-at-re-crafted-government-maldocs/)
- [McLellan, T. et al. (2024, January 12). Cutting Edge: Suspected APT Targets Ivanti Connect Secure VPN in New Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
- [S2 Grupo. (2019, April 2). WIRTE Group attacking the Middle East. Retrieved May 24, 2019.](https://lab52.io/blog/wirte-group-attacking-the-middle-east/)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Xiao, C. (2018, September 17). Xbash Combines Botnet, Ransomware, Coinmining in Worm that Targets Linux and Windows. Retrieved November 14, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-xbash-combines-botnet-ransomware-coinmining-worm-targets-linux-windows/)
- [Mac Threat Response, Mobile Research Team. (2020, August 13). The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSS Backdoor Planting in Safari, and Leverages Two Zero-day Exploits. Retrieved October 5, 2021.](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
- [Alintanahin, K. (2015). Operation Tropic Trooper: Relying on Tried-and-Tested Flaws to Infiltrate Secret Keepers. Retrieved June 14, 2019.](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)
- [Lee, B., Falcone, R. (2018, June 06). Sofacy Group’s Parallel Attacks. Retrieved June 18, 2018.](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)
- [ESET Research. (2019, May 22). A journey to Zebrocy land. Retrieved June 20, 2019.](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
- [Huss, D., et al. (2017, February 2). Oops, they did it again: APT Targets Russia and Belarus with ZeroT and PlugX. Retrieved April 5, 2018.](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)
- [Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
- [Singh, S. and Antil, S. (2020, October 27). APT-31 Leverages COVID-19 Vaccine Theme and Abuses Legitimate Online Services. Retrieved March 24, 2021.](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)
- [Gardiner, J., Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

---

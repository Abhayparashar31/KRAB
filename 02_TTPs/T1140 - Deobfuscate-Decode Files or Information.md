# Deobfuscate/Decode Files or Information

## Description

Adversaries may use Obfuscated Files or Information to hide artifacts of an intrusion from analysis. They may require separate mechanisms to decode or deobfuscate that information depending on how they intend to use it. Methods for doing that include built-in functionality of malware or by using utilities present on the system.

One such example is the use of certutil to decode a remote access tool portable executable file that has been hidden inside a certificate file. [1] Another example is using the Windows copy /b or type command to reassemble binary fragments into a malicious payload. [2] [3]

Sometimes a user's action may be required to open it for deobfuscation or decryption as part of User Execution . The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary. [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries decoded a Base64-encoded ZIP archive using the built-in certutil . [5] |
| S0469 | ABK | ABK has the ability to decrypt AES encrypted payloads. [6] |
| S1028 | Action RAT | Action RAT can use Base64 to decode actor-controlled C2 server communications. [7] |
| S0331 | Agent Tesla | Agent Tesla has the ability to decrypt strings encrypted with the Rijndael symmetric encryption algorithm. [8] |
| G1030 | Agrius | Agrius has deployed base64-encoded variants of ASPXSpy to evade detection. [9] |
| S1025 | Amadey | Amadey has decoded antivirus name strings. [10] |
| S9027 | ANELLDR | ANELLDR can decrypt encrypted payload data using AES-256-CBC and subsequently execute the payload in memory. [11] |
| S1133 | Apostle | Apostle compiled code is obfuscated in an unspecified fashion prior to delivery to victims. [9] |
| S0584 | AppleJeus | AppleJeus has decoded files received from a C2. [12] |
| S0622 | AppleSeed | AppleSeed can decode its payload prior to execution. [13] |
| G0073 | APT19 | An APT19 HTTP malware variant decrypts strings using single-byte XOR keys. [14] |
| G0007 | APT28 | An APT28 macro uses the command certutil -decode to decode contents of a .txt file storing the base64 encoded payload. [15] [16] |
| C0051 | APT28 Nearest Neighbor Campaign | During APT28 Nearest Neighbor Campaign , APT28 unarchived data using the GUI version of WinRAR. [17] |
| G0082 | APT38 | APT38 has used the RC4 algorithm to decrypt configuration data. [18] |
| G0087 | APT39 | APT39 has used malware to decrypt encrypted CAB files. [19] |
| C0046 | ArcaneDoor | ArcaneDoor involved the use of Base64 obfuscated scripts and commands. [20] |
| S0456 | Aria-body | Aria-body has the ability to decrypt the loader configuration and payload DLL. [21] |
| S9031 | AshTag | The AshTag stager compoment can decode and decrypt Base64 and XOR-encrypted payloads. [22] |
| S0373 | Astaroth | Astaroth uses a fromCharCode() deobfuscation method to avoid explicitly writing execution commands and to hide its code. [23] [24] |
| S0347 | AuditCred | AuditCred uses XOR and RC4 to perform decryption on the code functions. [25] |
| S0640 | Avaddon | Avaddon has decrypted encrypted strings. [26] |
| S0473 | Avenger | Avenger has the ability to decrypt files downloaded from C2. [6] |
| S1053 | AvosLocker | AvosLocker has deobfuscated XOR-encoded strings. [27] |
| S0344 | Azorult | Azorult uses an XOR key to decrypt content and uses Base64 to decode the C2 address. [28] [29] |
| S0638 | Babuk | Babuk has the ability to unpack itself into memory using XOR. [30] [31] |
| S0414 | BabyShark | BabyShark has the ability to decode downloaded files prior to execution. [32] |
| S0475 | BackConfig | BackConfig has used a custom routine to decrypt strings. [33] |
| S0642 | BADFLICK | BADFLICK can decode shellcode using a custom rotating XOR cipher. [34] |
| S0234 | Bandook | Bandook has decoded its PowerShell script. [35] |
| S0239 | Bankshot | Bankshot decodes embedded XOR strings. [36] |
| S0534 | Bazar | Bazar can decrypt downloaded payloads. Bazar also resolves strings and other artifacts at runtime. [37] [38] |
| S0470 | BBK | BBK has the ability to decrypt AES encrypted payloads. [6] |
| S0127 | BBSRAT | BBSRAT uses Expand to decompress a CAB file into executable content. [39] |
| S0574 | BendyBear | BendyBear has decrypted function blocks using a XOR key during runtime to evade detection. [40] |
| S0268 | Bisonal | Bisonal has decoded strings in the malware using XOR and RC4. [41] [42] |
| G1043 | BlackByte | BlackByte has encoded commands in base64-encoded sections concatenated together in PowerShell. [43] BlackByte uses PowerShell commands to disable Windows Defender. [44] |
| S1180 | BlackByte Ransomware | BlackByte Ransomware is distributed as an obfuscated JavaScript launcher file. [45] |
| S0520 | BLINDINGCAN | BLINDINGCAN has used AES and XOR to decrypt its DLLs. [46] |
| S1226 | BOOKWORM | BOOKWORM has decoded its Base64 encoded payload prior to execution. [47] BOOKWORM has also encrypted files with RC4 and has decrypted its payload prior to execution. [48] |
| S0635 | BoomBox | BoomBox can decrypt AES-encrypted files downloaded from C2. [49] |
| S0415 | BOOSTWRITE | BOOSTWRITE has used a a 32-byte long multi-XOR key to decode data inside its payload. [50] |
| S9015 | BRICKSTORM | BRICKSTORM has decoded its encrypted C2 traffic prior to execution. [51] [52] [53] [54] [55] BRICKSTORM also has the ability to decode its obfuscated payload before execution. [53] |
| G0060 | BRONZE BUTLER | BRONZE BUTLER downloads encoded payloads and decodes them on the victim. [56] |
| S9011 | BRUSHFIRE | BRUSHFIRE has decrypted XOR strings prior to execution. [57] |
| S1063 | Brute Ratel C4 | Brute Ratel C4 has the ability to deobfuscate its payload prior to execution. [58] |
| S1039 | Bumblebee | Bumblebee can deobfuscate C2 server responses and unpack its code on targeted hosts. [59] [60] |
| S0482 | Bundlore | Bundlore has used openssl to decrypt AES encrypted payload data. Bundlore has also used base64 and RC4 with a hardcoded key to deobfuscate data. [61] |
| S1118 | BUSHWALK | BUSHWALK can Base64 decode and RC4 decrypt malicious payloads sent through a web request’s command parameter. [62] [63] |
| C0017 | C0017 | During C0017 , APT41 used the DUSTPAN loader to decrypt embedded payloads. [64] |
| C0021 | C0021 | During C0021 , the threat actors deobfuscated encoded PowerShell commands including use of the specific string 'FromBase'+0x40+'String' , in place of FromBase64String which is normally used to decode base64. [65] [66] |
| S9016 | Caminho | Caminho can deobfuscate downloaded files prior to execution. [67] |
| S0335 | Carbon | Carbon decrypts task and configuration files for execution. [68] [69] |
| S0348 | Cardinal RAT | Cardinal RAT decodes many of its artifacts and is decrypted (AES-128) after being downloaded. [70] |
| S1224 | CASTLETAP | CASTLETAP can filter and deobfuscate an XOR encrypted activation string in the payload of an ICMP echo request. [71] |
| S0160 | certutil | certutil has been used to decode binaries hidden inside certificate files as Base64 information. [1] |
| S0631 | Chaes | Chaes has decrypted an AES encrypted binary file to trigger the download of other files. [72] |
| S0674 | CharmPower | CharmPower can decrypt downloaded modules prior to execution. [73] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP can use an embedded RC4 key to decrypt Windows API function strings. [74] |
| S1041 | Chinoxy | The Chinoxy dropping function can initiate decryption of its config file. [75] |
| S0667 | Chrommme | Chrommme can decrypt its encrypted internal code. [76] |
| G1021 | Cinnamon Tempest | Cinnamon Tempest has used weaponized DLLs to load and decrypt payloads. [77] |
| S1236 | CLAIMLOADER | CLAIMLOADER has decoded its payload prior to execution. [78] [79] |
| S0660 | Clambling | Clambling can deobfuscate its payload prior to execution. [80] [81] |
| S0611 | Clop | Clop has used a simple XOR operation to decrypt strings. [82] |
| S1105 | COATHANGER | COATHANGER decodes configuration items from a bundled file for command and control activity. [83] |
| S0154 | Cobalt Strike | Cobalt Strike can deobfuscate shellcode using a rolling XOR and decrypt metadata from Beacon sessions. [84] [85] The Cobalt Strike loader component can also decrypt the .bss section of the Beacon binary prior to execution. [86] |
| S0369 | CoinTicker | CoinTicker decodes the initially-downloaded hidden encoded file using OpenSSL. [87] |
| S0126 | ComRAT | ComRAT has used unique per machine passwords to decrypt the orchestrator payload and a hardcoded XOR key to decrypt its communications module. ComRAT has also used a unique password to decrypt the file used for its hidden file system. [88] [89] |
| S0575 | Conti | Conti has decrypted its payload using a hardcoded AES-256 key. [90] [91] |
| S0492 | CookieMiner | CookieMiner has used Google Chrome's decryption and extraction operations. [92] |
| S1235 | CorKLOG | CorKLOG has decoded XOR encrypted strings. [93] |
| S0614 | CostaBricks | CostaBricks has the ability to use bytecode to decrypt embedded payloads. [94] |
| S0115 | Crimson | Crimson can decode its encoded PE file prior to execution. [95] |
| S1153 | Cuckoo Stealer | Cuckoo Stealer strings are deobfuscated prior to execution. [96] [97] |
| S0687 | Cyclops Blink | Cyclops Blink can decrypt and parse instructions sent from C2. [98] |
| S1014 | DanBot | DanBot can use a VBA macro to decode its payload prior to installation and execution. [99] |
| S1111 | DarkGate | DarkGate installation includes binary code stored in a file located in a hidden directory, such as shell.txt , that is decrypted then executed. [100] DarkGate uses hexadecimal-encoded shellcode payloads during installation that are called via Windows API CallWindowProc() to decode and then execute. [101] |
| G0012 | Darkhotel | Darkhotel has decrypted strings and imports using RC4 during execution. [102] [103] |
| S1066 | DarkTortilla | DarkTortilla can decrypt its payload and associated configuration elements using the Rijndael cipher. [104] |
| S0673 | DarkWatchman | DarkWatchman has the ability to self-extract as a RAR archive. [105] |
| S0255 | DDKONG | DDKONG decodes an embedded configuration using XOR. [106] |
| S1052 | DEADEYE | DEADEYE has the ability to combine multiple sections of a binary which were broken up to evade detection into a single .dll prior to execution. [64] |
| S1134 | DEADWOOD | DEADWOOD XORs some strings within the binary using the value 0xD5 , and deobfuscates these items at runtime. [9] |
| S0354 | Denis | Denis will decrypt important strings used for C&C communication. [107] |
| S9021 | DOWNIISSA | DOWNIISSA can decode strings prior to execution. [108] |
| S0547 | DropBook | DropBook can unarchive data downloaded from the C2 to obtain the payload and persistence modules. [109] |
| S0502 | Drovorub | Drovorub has de-obsfuscated XOR encrypted payloads in WebSocket messages. [110] |
| S0567 | Dtrack | Dtrack has used a decryption routine that is part of an executable physical patch. [111] |
| S1158 | DUSTPAN | DUSTPAN decodes and decrypts embedded payloads. [112] |
| S1159 | DUSTTRAP | DUSTTRAP deobfuscates embedded payloads. [112] |
| S0024 | Dyre | Dyre decrypts resources needed for targeting the victim. [113] [114] |
| G1006 | Earth Lusca | Earth Lusca has used certutil to decode a string into a cabinet file. [115] |
| S0377 | Ebury | Ebury has verified C2 domain ownership by decrypting the TXT record using an embedded RSA public key. [116] |
| S0624 | Ecipekac | Ecipekac has the ability to decrypt fileless loader modules. [117] |
| S0554 | Egregor | Egregor has been decrypted before execution. [118] [119] |
| S1247 | Embargo | Embargo has utilized MDeployer to decrypt two payloads that contain MS4Killer toolkit b.cache and the Embargo ransomware executable a.cache with a hardcoded RC4 key wlQYLoPCil3niI7x8CvR9EtNtL/aeaHrZ23LP3fAsJogVTIzdnZ5Pi09ZVeHFkiB . [120] |
| S0367 | Emotet | Emotet has used a self-extracting RAR file to deliver modules to victims. Emotet has also extracted embedded executables from files using hard-coded buffer offsets. [121] |
| S0634 | EnvyScout | EnvyScout can deobfuscate and write malicious ISO files to disk. [49] |
| S0401 | Exaramel for Linux | Exaramel for Linux can decrypt its configuration file. [122] |
| S1179 | Exbyte | Exbyte decodes and decrypts data stored in the configuration file with a key provided on the command line during execution. [123] |
| S0361 | Expand | Expand can be used to decompress a local or remote CAB file into an executable. [124] |
| S0512 | FatDuke | FatDuke can decrypt AES encrypted C2 communications. [125] |
| G1016 | FIN13 | FIN13 has utilized certutil to decode base64 encoded versions of custom malware. [126] |
| G0046 | FIN7 | FIN7 has decoded a malicious PowerShell script using certutil -decode hex and has decoded an XOR-obfuscated block of data with the key qawsed1q2w3e , which led to the installation of Lizar . [127] |
| S0355 | Final1stspy | Final1stspy uses Python code to deobfuscate base64-encoded strings. [128] |
| S0182 | FinFisher | FinFisher extracts and decrypts stage 3 malware, which is stored in encrypted resources. [129] [130] |
| S0618 | FIVEHANDS | FIVEHANDS has the ability to decrypt its payload prior to execution. [131] [132] [133] |
| S0661 | FoggyWeb | FoggyWeb can be decrypted in memory using a Lightweight Encryption Algorithm (LEA)-128 key and decoded using a XOR key. [134] |
| S9033 | Fooder | Fooder has decrypted payloads using the WinCrypt API and the AES key. [135] |
| S1120 | FRAMESTING | FRAMESTING can decompress data received within POST requests. [62] |
| C0001 | Frankenstein | During Frankenstein , the threat actors deobfuscated Base64-encoded commands following the execution of a malicious script, which revealed a small script designed to obtain an additional payload. [136] |
| S0628 | FYAnti | FYAnti has the ability to decrypt an embedded .NET module. [117] |
| G0047 | Gamaredon Group | Gamaredon Group tools decrypted additional payloads from the C2. Gamaredon Group has also decoded Base64-encoded source code of a downloader. [137] [138] [139] Additionally, Gamaredon Group has decoded Telegram content to reveal the IP address for C2 communications. [140] |
| S0666 | Gelsemium | Gelsemium can decompress and decrypt DLLs and shellcode. [76] |
| S0032 | gh0st RAT | gh0st RAT has decrypted and loaded the gh0st RAT DLL into memory, once the initial dropper executable is launched. [141] |
| S1117 | GLASSTOKEN | GLASSTOKEN has the ability to decode hexadecimal and Base64 C2 requests. [142] |
| S9010 | GlassWorm | GlassWorm has decoded its Base64 instructions. [143] GlassWorm has also decrypted its AES protected payloads. [144] [143] [145] |
| S0588 | GoldMax | GoldMax has decoded and decrypted the configuration file when executed. [146] [147] |
| S0477 | Goopy | Goopy has used a polymorphic decryptor to decrypt itself at runtime. [107] |
| S1138 | Gootloader | Gootloader has the ability to decode and decrypt malicious payloads prior to execution. [148] [149] |
| G0078 | Gorgon Group | Gorgon Group malware can decode contents from a payload that was Base64 encoded and write the contents to a file. [150] |
| S0531 | Grandoreiro | Grandoreiro can decrypt its encrypted internal strings. [151] |
| S0690 | Green Lambert | Green Lambert can use multiple custom routines to decrypt strings prior to execution. [152] [153] |
| S0632 | GrimAgent | GrimAgent can use a decryption algorithm for strings based on Rotate on Right (RoR) and Rotate on Left (RoL) functionality. [154] |
| S0499 | Hancitor | Hancitor has decoded Base64 encoded URLs to insert a recipient’s name into the filename of the Word document. Hancitor has also extracted executables from ZIP files. [155] [156] |
| S9018 | HeartCrypt | HeartCrypt can decrypt payloads prior to execution. [157] [158] |
| S0697 | HermeticWiper | HermeticWiper can decompress and copy driver files using LZCopy . [159] |
| S1249 | HexEval Loader | HexEval Loader has decoded its payload prior to execution. [160] [161] [162] |
| S1027 | Heyoka Backdoor | Heyoka Backdoor can decrypt its payload prior to execution. [163] |
| S9023 | HiddenFace | HiddenFace has the ability to decrypt its payload prior to execution. [164] [165] |
| S0394 | HiddenWasp | HiddenWasp uses a cipher to implement a decoding function. [166] |
| G0126 | Higaisa | Higaisa used certutil to decode Base64 binaries at runtime and a 16-byte XOR key to decrypt data. [167] [168] |
| S0601 | Hildegard | Hildegard has decrypted ELF files with AES. [169] |
| S9007 | HTTPTroy | HTTPTroy has decoded strings encoded with Base64 and XOR prior to execution. [170] |
| S1097 | HUI Loader | HUI Loader can decrypt and load files containing malicious payloads. [171] |
| S0398 | HyperBro | HyperBro can unpack and decrypt its payload prior to execution. [80] [172] |
| S1022 | IceApple | IceApple can use a Base64-encoded AES key to decrypt tasking. [173] |
| S0434 | Imminent Monitor | Imminent Monitor has decoded malware components that are then dropped to the system. [174] |
| S1139 | INC Ransomware | INC Ransomware can run CryptStringToBinaryA to decrypt base64 content containing its ransom note. [175] |
| S0604 | Industroyer | Industroyer decrypts code to connect to a remote C2 server. [176] |
| S1245 | InvisibleFerret | InvisibleFerret has decoded XOR-encrypted and Base-64-encoded payloads prior to execution. [177] |
| S0260 | InvisiMole | InvisiMole can decrypt, unpack and load a DLL from its resources, or from blobs encrypted with Data Protection API, two-key triple DES, and variations of the XOR cipher. [178] [179] |
| S0581 | IronNetInjector | IronNetInjector has the ability to decrypt embedded .NET and PE payloads. [180] |
| S9029 | IronWind | IronWind can deobfuscate the next stage payload using Base64 and XOR operations with the key "53". [181] |
| S0189 | ISMInjector | ISMInjector uses the certutil command to decode a payload file. [182] |
| C0044 | Juicy Mix | During Juicy Mix , OilRig used a script to concatenate and deobfuscate encoded strings in Mango . [183] |
| S1190 | Kapeka | Kapeka utilizes obfuscated JSON structures for various data storage and configuration management items. [184] |
| G0004 | Ke3chang | Ke3chang has deobfuscated Base64-encoded shellcode strings prior to loading them. [185] |
| S0585 | Kerrdown | Kerrdown can decode, decrypt, and decompress multiple layers of shellcode. [186] |
| S0487 | Kessel | Kessel has decrypted the binary's configuration once the main function was launched. [187] |
| S1051 | KEYPLUG | KEYPLUG can decode its configuration file to determine C2 protocols. [64] |
| S0526 | KGH_SPY | KGH_SPY can decrypt encrypted strings and write them to a newly created folder. [188] |
| G0094 | Kimsuky | Kimsuky has decoded malicious VBScripts using Base64. [189] Kimsuky has also decoded malicious PowerShell scripts using Base64. [190] [191] Kimsuky has decoded RC4 obfuscated files prior to downloading files from their infrastructure. [191] |
| S0641 | Kobalos | Kobalos decrypts strings right after the initial communication, but before the authentication process. [192] |
| S0669 | KOCTOPUS | KOCTOPUS has deobfuscated itself before executing its commands. [193] |
| S0356 | KONNI | KONNI has used certutil to download and decode base64 encoded strings and has also devoted a custom section to performing all the components of the deobfuscation process. [194] [195] |
| S0236 | Kwampirs | Kwampirs decrypts and extracts a copy of its main DLL payload when executing. [196] |
| S9035 | LAMEHUG | LAMEHUG can decode and drop a decoy file attached to spearphishing emails. [197] |
| S1160 | Latrodectus | Latrodectus has the ability to deobfuscate encrypted strings. [198] [199] [200] |
| G0032 | Lazarus Group | Lazarus Group has used shellcode within macros to decrypt and manually map DLLs and shellcode into memory at runtime. [201] [202] |
| G0065 | Leviathan | Leviathan has used a DLL known as SeDll to decrypt and execute other JavaScript backdoors. [203] |
| S0395 | LightNeuron | LightNeuron has used AES and XOR to decrypt configuration files and commands. [204] |
| S1119 | LIGHTWIRE | LIGHTWIRE can RC4 decrypt and Base64 decode C2 commands. [62] |
| S1186 | Line Dancer | Line Dancer shellcode payloads are base64 encoded when transmitted to compromised devices. [205] |
| S0513 | LiteDuke | LiteDuke has the ability to decrypt and decode multiple layers of obfuscation. [125] |
| S0681 | Lizar | Lizar has decrypted its configuration data, such as the C2 IP address, ports and other network communication. [206] [207] |
| S1199 | LockBit 2.0 | LockBit 2.0 can decode scripts and strings in loaded modules. [208] [209] |
| S1202 | LockBit 3.0 | The LockBit 3.0 payload is decrypted at runtime. [210] [211] [212] |
| S0447 | Lokibot | Lokibot has decoded and decrypted its stages multiple times using hard-coded keys to deliver the final payload, and has decoded its server response hex string using XOR. [213] |
| S0582 | LookBack | LookBack has a function that decrypts malicious data. [214] |
| S9036 | LP-Notes | LP-Notes has decrypted strings with lengths ranging from 15 to 19 characters using the same decryption key for each string. [135] |
| S0532 | Lucifer | Lucifer can decrypt its C2 address upon execution. [215] |
| S1213 | Lumma Stealer | Lumma Stealer has used Base64-encoded content during execution, decoded via PowerShell. [216] |
| S1143 | LunarLoader | LunarLoader can deobfuscate files containing the next stages in the infection chain. [217] |
| S1142 | LunarMail | LunarMail can decrypt strings to retrieve configuration settings. [217] |
| S1141 | LunarWeb | LunarWeb can decrypt strings related to communication configuration using RC4 with a static key. [217] |
| S0409 | Machete | Machete ’s downloaded data is decrypted using AES. [218] |
| S1016 | MacMa | MacMa decrypts a downloaded file using AES-128-EBC with a custom delta. [219] |
| S1060 | Mafalda | Mafalda can decrypt files and data. [220] |
| S1182 | MagicRAT | MagicRAT stores command and control URLs using base64 encoding in the malware's configuration file. [221] |
| G1026 | Malteiro | Malteiro has the ability to deobfuscate downloaded files prior to execution. [222] |
| S1244 | Medusa Ransomware | Medusa Ransomware has decoded XOR encrypted strings prior to execution in memory. [223] [224] |
| S0576 | MegaCortex | MegaCortex has used a Base64 key to decode its components. [225] |
| G0045 | menuPass | menuPass has used certutil in a macro to decode base64-encoded content contained in a dropper document attached to an email. The group has also used certutil -decode to decode files on the victim’s machine when dropping UPPERCUT . [226] [227] |
| S0443 | MESSAGETAP | After checking for the existence of two files, keyword_parm.txt and parm.txt, MESSAGETAP XOR decodes and read the contents of the files. [228] |
| S1059 | metaMain | metaMain can decrypt and load other modules. [220] |
| S0455 | Metamorfo | Upon execution, Metamorfo has unzipped itself after being downloaded to the system and has performed string decryption. [229] [230] [231] |
| S0280 | MirageFox | MirageFox has a function for decrypting data containing C2 configuration information. [232] |
| S1122 | Mispadu | Mispadu decrypts its encrypted configuration files prior to execution. [222] [233] |
| G0021 | Molerats | Molerats decompresses ZIP files once on the victim machine. [234] |
| S1026 | Mongall | Mongall has the ability to decrypt its payload prior to execution. [163] |
| G1036 | Moonstone Sleet | Moonstone Sleet delivered payloads using multiple rounds of obfuscation and encoding to evade defenses and analysis. [235] |
| S1221 | MOPSLED | MOPSLED can decrypt obfuscated configuration files. [236] |
| S0284 | More_eggs | More_eggs will decode malware components that are then dropped to the system. [237] |
| S1047 | Mori | Mori can resolve networking APIs from strings that are ADD-encrypted. [238] |
| S9032 | MuddyViper | MuddyViper has decrypted the embedded HackBrowserData tool prior to execution. [135] |
| G0069 | MuddyWater | MuddyWater has decoded base64-encoded PowerShell, JavaScript, and VBScript. [239] [240] [241] [242] |
| G0129 | Mustang Panda | Mustang Panda has the ability to decrypt its payload prior to execution. [243] [244] [47] [245] Mustang Panda has also utilized RC4 encryption for malicious payloads. [246] [48] |
| S0637 | NativeZone | NativeZone can decrypt and decode embedded Cobalt Strike beacon stage shellcode. [49] |
| S0457 | Netwalker | Netwalker 's PowerShell script can decode and decrypt multiple layers of obfuscation, leading to the Netwalker DLL being loaded into memory. [247] |
| S1147 | Nightdoor | Nightdoor stores network configuration data in a file XOR encoded with the key value of 0x7A . [248] |
| S1100 | Ninja | The Ninja loader component can decrypt and decompress the payload. [249] [250] |
| S0353 | NOKKI | NOKKI uses a unique, custom de-obfuscation technique. [251] |
| S9025 | NOOPLDR | NOOPLDR can decrypt its payload prior to execution. [252] |
| S1170 | ODAgent | ODAgent can Base64-decode and XOR decrypt received C2 commands. [253] |
| S1172 | OilBooster | OilBooster can Base64-decode and XOR-decrypt C2 commands taken from JSON files. [253] |
| G0049 | OilRig | A OilRig macro has run a PowerShell command to decode file contents. OilRig has also used certutil to decode base64-encoded files on victims. [254] [182] [255] [256] |
| S0439 | Okrum | Okrum 's loader can decrypt the backdoor code, embedded within the loader or within a legitimate PNG file. A custom XOR cipher or RC4 is used for decryption. [257] |
| S0052 | OnionDuke | OnionDuke can use a custom decryption algorithm to decrypt strings. [125] |
| S0264 | OopsIE | OopsIE concatenates then decompresses multiple resources to load an embedded .Net Framework assembly. [255] |
| C0016 | Operation Dust Storm | During Operation Dust Storm , attackers used VBS code to decode payloads. [258] |
| C0006 | Operation Honeybee | During Operation Honeybee , malicious files were decoded prior to execution. [259] |
| C0005 | Operation Spalax | For Operation Spalax , the threat actors used a variety of packers and droppers to decrypt malicious payloads. [260] |
| S0402 | OSX/Shlayer | OSX/Shlayer can base64-decode and AES-decrypt downloaded payloads. [261] Versions of OSX/Shlayer pass encrypted and password-protected code to openssl and then write the payload to the /tmp folder. [262] [263] |
| S0352 | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D uses a decode routine combining bit shifting and XOR operations with a variable key that depends on the length of the string that was encoded. If the computation for the variable XOR key turns out to be 0, the default XOR key of 0x1B is used. This routine is also referenced as the rotate function in reporting. [264] |
| S0598 | P.A.S. Webshell | P.A.S. Webshell can use a decryption mechanism to process a user supplied password and allow execution. [122] |
| S1050 | PcShare | PcShare has decrypted its strings by applying a XOR operation and a decompression using a custom implemented LZM algorithm. [75] |
| S9014 | PHASEJAM | PHASEJAM has the ability to decode Base64 commands and data. [265] |
| S9028 | PHPsert | PHPsert has the ability to decode and decrypt obfuscated strings prior to execution. [266] |
| S1145 | Pikabot | Pikabot decrypts command and control URIs using ADVobfuscator, and decrypts IP addresses and port numbers with a custom algorithm. [267] Other versions of Pikabot decode chunks of stored stage 2 payload content in the initial payload .text section before consolidating them for further execution. [268] Overall LunarMail is associated with multiple encoding and encryption mechanisms to obfuscate the malware's presence and avoid analysis or detection. [269] |
| S0517 | Pillowmint | Pillowmint has been decompressed by included shellcode prior to being launched. [270] |
| S1031 | PingPull | PingPull can decrypt received data from its C2 server by using AES. [271] |
| S0501 | PipeMon | PipeMon can decrypt password-protected executables. [272] |
| S1123 | PITSTOP | PITSTOP can deobfuscate base64 encoded and AES encrypted commands. [63] |
| S0013 | PlugX | PlugX decompresses and decrypts itself using the Microsoft API call RtlDecompressBuffer. [273] [80] [274] PlugX has also decrypted its payloads in memory. [275] [276] [244] [245] |
| S0428 | PoetRAT | PoetRAT has used LZMA and base64 libraries to decode obfuscated scripts. [277] |
| S0518 | PolyglotDuke | PolyglotDuke can use a custom algorithm to decrypt strings used by the malware. [125] |
| S1173 | PowerExchange | PowerExchange can decode and decrypt C2 commands received via email. [278] |
| S1012 | PowerLess | PowerLess can use base64 and AES ECB decryption prior to execution of downloaded modules. [279] |
| S0223 | POWERSTATS | POWERSTATS can deobfuscate the main backdoor code. [241] |
| S1046 | PowGoop | PowGoop can decrypt PowerShell scripts for execution. [238] [280] |
| S0279 | Proton | Proton uses an encrypted file to store commands and configuration values. [281] |
| S0613 | PS1 | PS1 can use an XOR key to decrypt a PowerShell loader and payload binary. [94] |
| S0147 | Pteranodon | Pteranodon can decrypt encrypted data strings prior to using them. [282] |
| S1228 | PUBLOAD | PUBLOAD has decoded its payload prior to execution. [276] [243] [79] [283] [47] |
| S0196 | PUNCHBUGGY | PUNCHBUGGY has used PowerShell to decode base64-encoded assembly. [284] |
| S9019 | PureCrypter | PureCrypter can decrypt downloaded resources and parse internal files to determine its settings. [285] [158] |
| S1032 | PyDCrypt | PyDCrypt has decrypted and dropped the DCSrv payload to disk. [286] |
| S0650 | QakBot | QakBot can deobfuscate and re-assemble code strings for execution. [287] [288] [289] |
| S0269 | QUADAGENT | QUADAGENT uses AES and a preshared key to decrypt the custom Base64 routine used to encode strings and scripts. [290] |
| S1076 | QUIETCANARY | QUIETCANARY can use a custom parsing routine to decode the command codes and additional parameters from the C2 before executing them. [291] |
| S1148 | Raccoon Stealer | Raccoon Stealer uses RC4-encrypted, base64-encoded strings to obfuscate functionality and command and control servers. [292] [293] |
| S0565 | Raindrop | Raindrop decrypted its Cobalt Strike payload using an AES-256 encryption algorithm in CBC mode with a unique key per sample. [294] [295] |
| S0629 | RainyDay | RainyDay can decrypt its payload via a XOR key. [296] |
| S0458 | Ramsay | Ramsay can extract its agent from the body of a malicious document. [297] |
| S1212 | RansomHub | RansomHub can use a provided passphrase to decrypt its configuration file. [298] |
| S1113 | RAPIDPULSE | RAPIDPULSE listens for specific HTTP query parameters in received communications. If specific parameters match, a hard-coded RC4 key is used to decrypt the HTTP query paremter hmacTime . This decrypts to a filename that is then open, read, encrypted with the same RC4 key, base64-encoded, written to standard out, then passed as a response to the HTTP request. [299] |
| S1130 | Raspberry Robin | Raspberry Robin contains several layers of obfuscation to hide malicious code from detection and analysis. [300] |
| S0495 | RDAT | RDAT can deobfuscate the base64-encoded and AES-encrypted files downloaded from the C2 server. [301] |
| S1240 | RedLine Stealer | RedLine Stealer has decoded its payload prior to execution. [302] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 used malware implants to deobfuscate incoming C2 messages and encoded archives. [303] [304] |
| S0511 | RegDuke | RegDuke can decrypt strings with a key either stored in the Registry or hardcoded in the code. [125] |
| S0375 | Remexi | Remexi decrypts the configuration data using XOR with 25-character keys. [305] |
| S1219 | REPTILE | The REPTILE launcher component can decrypt kernel module code from a file and load it into memory. [236] |
| S0496 | REvil | REvil can decode encrypted strings to enable execution of commands and payloads. [306] [307] [308] [309] [310] [311] |
| S0258 | RGDoor | RGDoor decodes Base64 strings and decrypts strings using a custom XOR algorithm. [312] |
| S1222 | RIFLESPINE | RIFLESPINE can deobfuscate encrypted files prior to execution on targeted hosts. [236] |
| S0448 | Rising Sun | Rising Sun has decrypted itself using a single-byte XOR scheme. Additionally, Rising Sun can decrypt its configuration data at runtime. [313] |
| S1150 | ROADSWEEP | ROADSWEEP can decrypt embedded scripts prior to execution. [74] [314] |
| S9026 | ROAMINGHOUSE | ROAMINGHOUSE can decode and drop a malicious ZIP file prior to execution. [315] |
| G0106 | Rocke | Rocke has extracted tar.gz files after downloading them from a C2 server. [316] |
| S0270 | RogueRobin | RogueRobin decodes an embedded executable using base64 and decompresses it. [317] |
| S0240 | ROKRAT | ROKRAT can decrypt strings using the victim's hostname as the key. [318] [319] |
| S1078 | RotaJakiro | RotaJakiro uses the AES algorithm, bit shifts in a function called rotate , and an XOR cipher to decrypt resources required for persistence, process guarding, and file locking. It also performs this same function on encrypted stack strings and the head and key sections in the network packet structure used for C2 communications. [320] |
| S9037 | RustyWater | RustyWater has used the WriteHexToFile function to transform an embedded hex string to the payload CertificationKit.ini. [321] |
| S1210 | Sagerunex | Sagerunex uses a custom decryption routine to unpack itself during installation. [322] |
| S1018 | Saint Bot | Saint Bot can deobfuscate strings and files for execution. [323] |
| S1168 | SampleCheck5000 | SampleCheck5000 can decode and decrypt command line strings and files received through C2. [183] [253] |
| G0034 | Sandworm Team | Sandworm Team 's VBS backdoor can decode Base64-encoded data and save it to the %TEMP% folder. The group also decrypted received information using the Triple DES algorithm and decompresses it using GZip. [324] [325] |
| S1085 | Sardonic | Sardonic can first decrypt with the RC4 algorithm using a hardcoded decryption key before decompressing. [326] |
| S0461 | SDBbot | SDBbot has the ability to decrypt and decompress its payload to enable code execution. [327] [328] |
| S0596 | ShadowPad | ShadowPad has decrypted a binary blob to start execution. [329] |
| S0140 | Shamoon | Shamoon decrypts ciphertext using an XOR cipher and a base64-encoded string. [330] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors decrypted scripts prior to execution. [331] |
| S1019 | Shark | Shark can extract and decrypt downloaded .zip files. [332] |
| S0546 | SharpStage | SharpStage has decompressed data received from the C2 server. [333] |
| S0444 | ShimRat | ShimRat has decompressed its core DLL using shellcode once an impersonated antivirus component was running on a system. [334] |
| S0589 | Sibot | Sibot can decrypt data received from a C2 and save to a file. [146] |
| S0610 | SideTwist | SideTwist can decode and decrypt messages received from C2. [335] |
| S0623 | Siloscape | Siloscape has decrypted the password of the C2 server with a simple byte by byte XOR. Siloscape also writes both an archive of Tor and the unzip binary to disk from data embedded within the payload using Visual Studio’s Resource Manager. [336] |
| S0468 | Skidmap | Skidmap has the ability to download, unpack, and decrypt tar.gz files . [337] |
| S1110 | SLIGHTPULSE | SLIGHTPULSE can deobfuscate base64 encoded and RC4 encrypted C2 messages. [338] |
| S0226 | Smoke Loader | Smoke Loader deobfuscates its code. [339] |
| S1086 | Snip3 | Snip3 can decode its second-stage PowerShell script prior to execution. [340] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 used 7-Zip to decode their Raindrop malware. [294] |
| S0615 | SombRAT | SombRAT can run upload to decrypt and upload files from storage. [94] [132] |
| S0516 | SoreFang | SoreFang can decode and decrypt exfiltrated data sent to C2. [341] |
| S0543 | Spark | Spark has used a custom XOR algorithm to decrypt the payload. [342] |
| S9024 | SPAWNCHIMERA | SPAWNCHIMERA has decoded a XOR encoded private key. [343] |
| S1140 | Spica | Upon execution Spica can decode an embedded .pdf and write it to the desktop as a decoy document. [344] |
| S1232 | SplatDropper | SplatDropper has decoded XOR encrypted payload. [93] |
| S0390 | SQLRat | SQLRat has scripts that are responsible for deobfuscating additional scripts. [345] |
| S1030 | Squirrelwaffle | Squirrelwaffle has decrypted files and payloads using a XOR-based algorithm. [346] [347] |
| S0188 | Starloader | Starloader decrypts and executes shellcode from a file called Stars.jps. [348] |
| S1227 | StarProxy | StarProxy has decrypted network packets using a custom algorithm. [349] |
| S1112 | STEADYPULSE | STEADYPULSE can URL decode key/value pairs sent over C2. [338] |
| S1200 | StealBit | StealBit can deobfuscate loaded modules prior to execution. [208] [350] |
| G1046 | Storm-1811 | Storm-1811 has distributed password-protected archives such as ZIP files during intrusions. [351] |
| S1183 | StrelaStealer | StrelaStealer payloads have included strings encrypted via XOR. [352] StrelaStealer JavaScript payloads utilize Base64-encoded payloads that are decoded via certutil to create a malicious DLL file. [353] [354] |
| S0603 | Stuxnet | Stuxnet decrypts resources that are loaded into memory and executed. [355] |
| S0562 | SUNSPOT | SUNSPOT decrypts SUNBURST , which was stored in AES128-CBC encrypted blobs. [356] |
| S9001 | SystemBC | SystemBC has the ability to decrypt RC4 encrypted packets and to decode obfuscated data before C2 communication. [357] Additionally, SystemBC has decrypted its config file that was encoded with XOR and a hardcoded 40-byte key. [358] |
| S0663 | SysUpdate | SysUpdate can deobfuscate packed binaries in memory. [172] |
| G0092 | TA505 | TA505 has decrypted packed DLLs with an XOR key. [359] |
| S0011 | Taidoor | Taidoor can use a stream cipher to decrypt stings used by the malware. [360] |
| G0139 | TeamTNT | TeamTNT has used a script that decodes a Base64-encoded version of WeaveWorks Scope. [361] |
| S0560 | TEARDROP | TEARDROP was decoded using a custom rolling XOR algorithm to execute a customized Cobalt Strike payload. [362] [363] [295] |
| S1223 | THINCRUST | THINCRUST can deobfuscate RSA encrypted C2 commands received through the DEVICEID cookie. [71] |
| G0027 | Threat Group-3390 | During execution, Threat Group-3390 malware deobfuscates and decompresses code that was encoded with Metasploit’s shikata_ga_nai encoder as well as compressed with LZNT1 compression. [364] |
| S0665 | ThreatNeedle | ThreatNeedle can decrypt its payload using RC4, AES, or one-byte XORing. [365] |
| S1239 | TONESHELL | TONESHELL has decoded its payload prior to execution. [79] [366] [283] [349] [367] |
| S0678 | Torisma | Torisma has used XOR and Base64 to decode C2 data. [368] |
| S0266 | TrickBot | TrickBot decodes the configuration data and modules. [369] [370] [371] |
| G0081 | Tropic Trooper | Tropic Trooper used shellcode with an XOR algorithm to decrypt a payload. Tropic Trooper also decrypted image files which contained a payload. [372] [373] |
| S0436 | TSCookie | TSCookie has the ability to decrypt, load, and execute a DLL and its resources. [374] |
| S9034 | Tsundere Botnet | Tsundere Botnet ’s loader has decrypted obfuscated JavaScript files using the AES-256 CBC algorithm, a build-specific key, and initialization vector. [375] [376] |
| S0647 | Turian | Turian has the ability to use a XOR decryption key to extract C2 server domains and IP addresses. [377] |
| G0010 | Turla | Turla has used a custom decryption routine, which pulls key and salt values from other artifacts such as a WMI filter or PowerShell Profile , to decode encrypted PowerShell payloads. [378] |
| S0263 | TYPEFRAME | One TYPEFRAME variant decrypts an archive using an RC4 key, then decompresses and installs the decrypted malicious DLL module. Another variant decodes the embedded file by XORing it with the value "0x35". [379] |
| S1164 | UPSTYLE | UPSTYLE encodes its main content prior to loading via Python as base64-encoded blobs. [380] [381] |
| S0022 | Uroburos | Uroburos can decrypt command parameters sent through C2 and use unpacking code to extract its packed executable. [382] |
| S0386 | Ursnif | Ursnif has used crypto key information stored in the Registry to decrypt Tor clients dropped to disk. [383] |
| S0476 | Valak | Valak has the ability to decode and decrypt downloaded files. [384] [385] |
| S0636 | VaporRage | VaporRage can deobfuscate XOR-encoded shellcode prior to execution. [49] |
| S0257 | VERMIN | VERMIN decrypts code, strings, and commands to use once it's on the victim's machine. [386] |
| S0180 | Volgmer | Volgmer deobfuscates its strings and APIs once its executed. [387] |
| G1017 | Volt Typhoon | Volt Typhoon has used Base64-encoded data to transfer payloads and commands, including deobfuscation via certutil . [388] |
| S0670 | WarzoneRAT | WarzoneRAT can use XOR 0x45 to decrypt obfuscated code. [389] |
| S0612 | WastedLocker | WastedLocker 's custom cryptor, CryptOne, used an XOR based algorithm to decrypt the payload. [390] |
| C0037 | Water Curupira Pikabot Distribution | Water Curupira Pikabot Distribution used highly obfuscated JavaScript files as one initial installer for Pikabot . [391] |
| S0579 | Waterbear | Waterbear has the ability to decrypt its RC4 encrypted payload for execution. [392] |
| S0515 | WellMail | WellMail can decompress scripts received from C2. [393] |
| S0514 | WellMess | WellMess can decode and decrypt data received from C2. [394] [395] [396] |
| S0689 | WhisperGate | WhisperGate can deobfuscate downloaded files stored in reverse byte order and decrypt embedded resources using multiple XOR operations. [397] [398] |
| S0466 | WindTail | WindTail has the ability to decrypt strings using hard-coded AES keys. [399] |
| S0430 | Winnti for Linux | Winnti for Linux has decoded XOR encoded strings holding its configuration upon execution. [400] |
| S0141 | Winnti for Windows | The Winnti for Windows dropper can decrypt and decompresses a data blob. [401] |
| G1035 | Winter Vivern | Winter Vivern delivered exploit payloads via base64-encoded payloads in malicious email messages. [402] |
| S1115 | WIREFIRE | WIREFIRE can decode, decrypt, and decompress data received in C2 HTTP POST requests. [403] |
| G0090 | WIRTE | WIRTE has used Base64 to decode malicious VBS script. [404] |
| S1065 | Woody RAT | Woody RAT can deobfuscate Base64-encoded strings and scripts. [405] |
| S0653 | xCaon | xCaon has decoded strings from the C2 server before executing commands. [406] |
| S1207 | XLoader | XLoader uses XOR and RC4 algorithms to decrypt payloads and functions. [407] XLoader can be distributed as a self-extracting RAR archive that launches an AutoIT loader. [408] |
| S1248 | XORIndex Loader | XORIndex Loader can decode its payload prior to execution. [161] |
| S0388 | YAHOYAH | YAHOYAH decrypts downloaded files before execution. [409] |
| S0251 | Zebrocy | Zebrocy decodes its secondary payload and writes it to the victim’s machine. Zebrocy also uses AES and XOR to decrypt strings and payloads. [410] [411] |
| S0230 | ZeroT | ZeroT shellcode decrypts and decompresses its RC4-encrypted payload. [412] |
| S0330 | Zeus Panda | Zeus Panda decrypts strings in the code during the execution process. [413] |
| G0128 | ZIRCONIUM | ZIRCONIUM has used the AES256 algorithm with a SHA1 derived key to decrypt exploit code. [414] |
| S1013 | ZxxZ | ZxxZ has used a XOR key to decrypt strings. [415] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0275 | Detect Adversary Deobfuscation or Decoding of Files and Payloads | AN0767 | An adversary leverages built-in tools such as certutil.exe, powershell.exe, or copy.exe to decode, reassemble, or extract hidden malicious content from obfuscated containers or encoded formats. The decoding utility often spawns shortly after file staging or download and may be chained with script interpreters or further payload execution. |
| AN0768 | The adversary uses native utilities like base64, gzip, tar, or openssl to decode, decompress, or decrypt files that were previously staged or downloaded. These tools may be chained with curl/wget and executed via bash/zsh, often to extract an embedded payload or reverse shell script. |  |  |
| AN0769 | The adversary invokes built-in scripting or decoding tools like base64, plutil, or AppleScript-based utilities to decode files embedded in staging artifacts. Decoding often occurs post-download or as part of post-exploitation payload deployment via zsh, python, or osascript. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0275 | Detect Adversary Deobfuscation or Decoding of Files and Payloads | AN0767 | An adversary leverages built-in tools such as certutil.exe, powershell.exe, or copy.exe to decode, reassemble, or extract hidden malicious content from obfuscated containers or encoded formats. The decoding utility often spawns shortly after file staging or download and may be chained with script interpreters or further payload execution. |
| AN0768 | The adversary uses native utilities like base64, gzip, tar, or openssl to decode, decompress, or decrypt files that were previously staged or downloaded. These tools may be chained with curl/wget and executed via bash/zsh, often to extract an embedded payload or reverse shell script. |  |  |
| AN0769 | The adversary invokes built-in scripting or decoding tools like base64, plutil, or AppleScript-based utilities to decode files embedded in staging artifacts. Decoding often occurs post-download or as part of post-exploitation payload deployment via zsh, python, or osascript. |  |  |

---

## References

- [Malwarebytes Labs. (2017, March 27). New targeted attack against Saudi Arabia Government. Retrieved July 3, 2017.](https://blog.malwarebytes.com/cybercrime/social-engineering-cybercrime/2017/03/new-targeted-attack-saudi-arabia-government/)
- [Tedesco, B. (2016, September 23). Security Alert Summary. Retrieved February 12, 2018.](https://www.carbonblack.com/2016/09/23/security-advisory-variants-well-known-adware-families-discovered-include-sophisticated-obfuscation-techniques-previously-associated-nation-state-attacks/)
- [Aleksandar Milenkoski, Juan Andres Guerrero-Saade, and Joey Chen. (2023, March 23). Operation Tainted Love | Chinese APTs Target Telcos in New Attacks. Retrieved March 18, 2025.](https://www.sentinelone.com/labs/operation-tainted-love-chinese-apts-target-telcos-in-new-attacks/)
- [Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [Jazi, H. (2020, April 16). New AgentTesla variant steals WiFi credentials. Retrieved May 19, 2020.](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [Hiroaki, H. (2024, November 26). Guess Who’s Back - The Return of ANEL in the Recent Earth Kasha Spear-phishing Campaign in 2024. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
- [Cybersecurity and Infrastructure Security Agency. (2021, February 21). AppleJeus: Analysis of North Korea’s Cryptocurrency Malware. Retrieved March 1, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [Grunzweig, J., Lee, B. (2016, January 22). New Attacks Linked to C0d0so0 Group. Retrieved August 2, 2018.](https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/)
- [Lee, B, et al. (2018, February 28). Sofacy Attacks Multiple Government Entities. Retrieved March 15, 2018.](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)
- [Lee, B., Falcone, R. (2018, June 06). Sofacy Group’s Parallel Attacks. Retrieved June 18, 2018.](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)
- [Koessel, Sean. Adair, Steven. Lancaster, Tom. (2024, November 22). The Nearest Neighbor Attack: How A Russian APT Weaponized Nearby Wi-Fi Networks for Covert Access. Retrieved February 25, 2025.](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)
- [SEONGSU PARK. (2022, December 27). BlueNoroff introduces new methods bypassing MoTW. Retrieved February 6, 2024.](https://securelist.com/bluenoroff-methods-bypass-motw/108383/)
- [FBI. (2020, September 17). Indicators of Compromise Associated with Rana Intelligence Computing, also known as Advanced Persistent Threat 39, Chafer, Cadelspy, Remexi, and ITG07. Retrieved December 10, 2020.](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)
- [Cisco Talos. (2024, April 24). ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices. Retrieved January 6, 2025.](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Unit 42. (2025, December 11). Hamas-Affiliated Ashen Lepus Targets Middle Eastern Diplomatic Entities With New AshTag Malware Suite. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
- [Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
- [GReAT. (2020, July 14). The Tetrade: Brazilian banking malware goes global. Retrieved November 9, 2020.](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)
- [Trend Micro. (2018, November 20). Lazarus Continues Heists, Mounts Attacks on Financial Organizations in Latin America. Retrieved December 3, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)
- [Yuste, J. Pastrana, S. (2021, February 9). Avaddon ransomware: an in-depth analysis and decryption of infected systems. Retrieved August 19, 2021.](https://arxiv.org/pdf/2102.04796.pdf)
- [Hasherezade. (2021, July 23). AvosLocker enters the ransomware scene, asks for partners. Retrieved January 11, 2023.](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
- [Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
- [Proofpoint. (2018, July 30). New version of AZORult stealer improves loading features, spreads alongside ransomware in new campaign. Retrieved November 29, 2018.](https://www.proofpoint.com/us/threat-insight/post/new-version-azorult-stealer-improves-loading-features-spreads-alongside)
- [Sogeti. (2021, March). Babuk Ransomware. Retrieved August 11, 2021.](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
- [Sebdraven. (2021, February 8). Babuk is distributed packed. Retrieved August 11, 2021.](https://sebdraven.medium.com/babuk-is-distributed-packed-78e2f5dd2e62)
- [CISA, FBI, CNMF. (2020, October 27). https://us-cert.cisa.gov/ncas/alerts/aa20-301a. Retrieved November 4, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-301a)
- [Hinchliffe, A. and Falcone, R. (2020, May 11). Updated BackConfig Malware Targeting Government and Military Organizations in South Asia. Retrieved June 17, 2020.](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)
- [Accenture iDefense Unit. (2019, March 5). Mudcarp's Focus on Submarine Technologies. Retrieved August 24, 2021.](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
- [Check Point. (2020, November 26). Bandook: Signed & Delivered. Retrieved May 31, 2021.](https://research.checkpoint.com/2020/bandook-signed-delivered/)
- [US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1, 2020.](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
- [Lee, B. Grunzweig, J. (2015, December 22). BBSRAT Attacks Targeting Russian Organizations Linked to Roaming Tiger. Retrieved August 19, 2016.](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)
- [Harbison, M. (2021, February 9). BendyBear: Novel Chinese Shellcode Linked With Cyber Espionage Group BlackTech. Retrieved February 16, 2021.](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)
- [Hayashi, K., Ray, V. (2018, July 31). Bisonal Malware Used in Attacks Against Russia and South Korea. Retrieved August 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [US Federal Bureau of Investigation & US Secret Service. (2022, February 11). Indicators of Compromise Associated with BlackByte Ransomware. Retrieved December 16, 2024.](https://www.ic3.gov/CSA/2022/220211.pdf)
- [Huseyin Can Yuceel. (2022, February 21). TTPs used by BlackByte Ransomware Targeting Critical Infrastructure. Retrieved December 16, 2024.](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [US-CERT. (2020, August 19). MAR-10295134-1.v1 – North Korean Remote Access Trojan: BLINDINGCAN. Retrieved August 19, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
- [Robert Falcone. (2025, February 20). Stately Taurus Activity in Southeast Asia Links to Bookworm Malware. Retrieved July 21, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-uses-bookworm-malware/)
- [Robert Falcone, Mike Scott, Juan Cortes. (2015, November 10). Bookworm Trojan: A Model of Modular Architecture. Retrieved July 21, 2025.](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)
- [MSTIC. (2021, May 28). Breaking down NOBELIUM’s latest early-stage toolset. Retrieved August 4, 2021.](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
- [Carr, N, et all. (2019, October 10). Mahalo FIN7: Responding to the Criminal Operators’ New Tools and Techniques. Retrieved October 11, 2019.](https://www.fireeye.com/blog/threat-research/2019/10/mahalo-fin7-responding-to-new-tools-and-techniques.html)
- [CrowdStrike. (2025, December 4). Unveiling WARP PANDA: A New Sophisticated China-Nexus Adversary. Retrieved April 16, 2026.](https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/)
- [DHS/CISA. (2026, February 11). AR25-338A: BRICKSTORM Backdoor. Retrieved April 16, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
- [Huseyin Can Yuceel. (2025, October 1). BRICKSTORM Malware: UNC5221 Targets Tech and Legal Sectors in the United States. Retrieved April 16, 2026.](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)
- [Resecurity Threat Intelligence & Incident Analysis. (2025, October 22). F5 BIG-IP Source Code Leak Tied to State-Linked Campaigns Using BRICKSTORM Backdoor. Retrieved April 16, 2026.](https://www.resecurity.com/blog/article/f5-big-ip-source-code-leak-tied-to-state-linked-campaigns-using-brickstorm-backdoor)
- [Sarah Yoder, John Wolfram, Ashley Pearson, Doug Bienstock, Josh Madeley, Josh Murchie, Brad Slaybaugh, Matt Lin, Geoff Carstairs, Austin Larsen. (2025, September 24). Another BRICKSTORM: Stealthy Backdoor Enabling Espionage into Tech and Legal Sectors. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
- [Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)
- [John Wolfram, Michael Edie, Jacob Thompson, Matt Lin, Josh Murchie. (2025, April 3). Suspected China-Nexus Threat Actor Actively Exploiting Critical Ivanti Connect Secure Vulnerability (CVE-2025-22457). Retrieved April 13, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)
- [Harbison, M. and Renals, P. (2022, July 5). When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors. Retrieved February 1, 2023.](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
- [Merriman, K. and Trouerbach, P. (2022, April 28). This isn't Optimus Prime's Bumblebee but it's Still Transforming. Retrieved August 22, 2022.](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
- [Salem, A. (2022, April 27). The chronicles of Bumblebee: The Hook, the Bee, and the Trickbot connection. Retrieved September 2, 2022.](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
- [Sushko, O. (2019, April 17). macOS Bundlore: Mac Virus Bypassing macOS Security Features. Retrieved June 30, 2020.](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
- [Lin, M. et al. (2024, January 31). Cutting Edge, Part 2: Investigating Ivanti Connect Secure VPN Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
- [Lin, M. et al. (2024, February 27). Cutting Edge, Part 3: Investigating Ivanti Connect Secure VPN Exploitation and Persistence Attempts. Retrieved March 1, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Dunwoody, M., et al. (2018, November 19). Not So Cozy: An Uncomfortable Examination of a Suspected APT29 Phishing Campaign. Retrieved November 27, 2018.](https://www.fireeye.com/blog/threat-research/2018/11/not-so-cozy-an-uncomfortable-examination-of-a-suspected-apt29-phishing-campaign.html)
- [Microsoft Defender Research Team. (2018, December 3). Analysis of cyberattack on U.S. think tanks, non-profits, public sector by unidentified attackers. Retrieved April 15, 2019.](https://www.microsoft.com/security/blog/2018/12/03/analysis-of-cyberattack-on-u-s-think-tanks-non-profits-public-sector-by-unidentified-attackers/)
- [Pellegrino, G. (2025, December 16). BlindEagle Targets Colombian Government Agency with Caminho and DCRAT. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)
- [ESET. (2017, March 30). Carbon Paper: Peering into Turla’s second stage backdoor. Retrieved November 7, 2018.](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)
- [Accenture. (2020, October). Turla uses HyperStack, Carbon, and Kazuar to compromise government entity. Retrieved December 2, 2020.](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)
- [Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
- [Marvi, A. et al.. (2023, March 16). Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation. Retrieved March 22, 2023.](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
- [Salem, E. (2020, November 17). CHAES: Novel Malware Targeting Latin American E-Commerce. Retrieved June 30, 2021.](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Biderman, O. et al. (2022, October 3). REVEALING EMPEROR DRAGONFLY: NIGHT SKY AND CHEERSCRYPT - A SINGLE RANSOMWARE GROUP. Retrieved December 6, 2023.](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)
- [Golo Muhr, Joshua Chung. (2025, June 23). Hive0154 aka Mustang Panda shifts focus on Tibetan community to deploy Pubload backdoor. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Chen, T. and Chen, Z. (2020, February 17). CLAMBLING - A New Backdoor Base On Dropbox. Retrieved November 12, 2021.](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
- [Mundo, A. (2019, August 1). Clop Ransomware. Retrieved May 10, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
- [Dutch Military Intelligence and Security Service (MIVD) & Dutch General Intelligence and Security Service (AIVD). (2024, February 6). Ministry of Defense of the Netherlands uncovers COATHANGER, a stealthy Chinese FortiGate RAT. Retrieved February 7, 2024.](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
- [Mavis, N. (2020, September 21). The Art and Science of Detecting Cobalt Strike. Retrieved September 12, 2024.](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [Thomas Reed. (2018, October 29). Mac cryptocurrency ticker app installs backdoors. Retrieved April 23, 2019.](https://blog.malwarebytes.com/threat-analysis/2018/10/mac-cryptocurrency-ticker-app-installs-backdoors/)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [CISA. (2020, October 29). Malware Analysis Report (AR20-303A). Retrieved December 9, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303a)
- [Rochberger, L. (2021, January 12). Cybereason vs. Conti Ransomware. Retrieved February 17, 2021.](https://www.cybereason.com/blog/cybereason-vs.-conti-ransomware)
- [Baskin, B. (2020, July 8). TAU Threat Discovery: Conti Ransomware. Retrieved February 17, 2021.](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [Chen, y., et al. (2019, January 31). Mac Malware Steals Cryptocurrency Exchanges’ Cookies. Retrieved July 22, 2020.](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: PAKLOG, CorKLOG, and SplatCloak | P2. Retrieved September 12, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Kohler, A. and Lopez, C. (2024, April 30). Malware: Cuckoo Behaves Like Cross Between Infostealer and Spyware. Retrieved August 20, 2024.](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
- [Stokes, P. (2024, May 9). macOS Cuckoo Stealer | Ensuring Detection and Defense as New Samples Rapidly Emerge. Retrieved August 20, 2024.](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)
- [NCSC. (2022, February 23). Cyclops Blink Malware Analysis Report. Retrieved March 3, 2022.](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
- [SecureWorks 2019, August 27 LYCEUM Takes Center Stage in Middle East Campaign Retrieved. 2019/11/19](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Ernesto Fernández Provecho, Pham Duy Phuc, Ciana Driscoll & Vinoo Thomas. (2023, November 21). The Continued Evolution of the DarkGate Malware-as-a-Service. Retrieved February 9, 2024.](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
- [Kaspersky Lab's Global Research & Analysis Team. (2015, August 10). Darkhotel's attacks in 2015. Retrieved November 2, 2018.](https://securelist.com/darkhotels-attacks-in-2015/71713/)
- [Microsoft. (2016, July 14). Reverse engineering DUBNIUM – Stage 2 payload analysis . Retrieved March 31, 2021.](https://www.microsoft.com/security/blog/2016/07/14/reverse-engineering-dubnium-stage-2-payload-analysis/)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [Ash, B., et al. (2018, June 26). RANCOR: Targeted Attacks in South East Asia Using PLAINTEE and DDKONG Malware Families. Retrieved July 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part I. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)
- [Cybereason Nocturnus Team. (2020, December 9). MOLERATS IN THE CLOUD: New Malware Arsenal Abuses Cloud Platforms in Middle East Espionage Campaign. Retrieved December 22, 2020.](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
- [NSA/FBI. (2020, August). Russian GRU 85th GTsSS Deploys Previously Undisclosed Drovorub Malware. Retrieved August 25, 2020.](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
- [Konstantin Zykov. (2019, September 23). Hello! My name is Dtrack. Retrieved January 20, 2021.](https://securelist.com/my-name-is-dtrack/93338/)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Symantec Security Response. (2015, June 23). Dyre: Emerging threat on financial fraud landscape. Retrieved August 23, 2018.](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/dyre-emerging-threat.pdf)
- [hasherezade. (2015, November 4). A Technical Look At Dyreza. Retrieved June 15, 2020.](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
- [Chen, J., et al. (2022). Delving Deep: An Analysis of Earth Lusca’s Operations. Retrieved July 1, 2022.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
- [Vachon, F. (2017, October 30). Windigo Still not Windigone: An Ebury Update . Retrieved February 10, 2021.](https://www.welivesecurity.com/2017/10/30/windigo-ebury-update-2/)
- [GREAT. (2021, March 30). APT10: sophisticated multi-layered loader Ecipekac discovered in A41APT campaign. Retrieved June 17, 2021.](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
- [NHS Digital. (2020, November 26). Egregor Ransomware The RaaS successor to Maze. Retrieved December 29, 2020.](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
- [Rochberger, L. (2020, November 26). Cybereason vs. Egregor Ransomware. Retrieved December 30, 2020.](https://www.cybereason.com/blog/cybereason-vs-egregor-ransomware)
- [Jan Holman, Tomas Zvara. (2024, October 23). Embargo ransomware: Rock’n’Rust. Retrieved October 19, 2025.](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
- [Binary Defense. (n.d.). Emotet Evolves With new Wi-Fi Spreader. Retrieved September 8, 2023.](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
- [ANSSI. (2021, January 27). SANDWORM INTRUSION SET CAMPAIGN TARGETING CENTREON SYSTEMS. Retrieved March 30, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [Microsoft. (2017, October 15). Expand. Retrieved February 19, 2019.](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/expand)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [Gemini Advisory. (2022, January 13). FIN7 Uses Flash Drives to Spread Remote Access Trojan. Retrieved May 14, 2025.](https://geminiadvisory.io/fin7-flash-drives-spread-remote-access-trojan/)
- [Grunzweig, J. (2018, October 01). NOKKI Almost Ties the Knot with DOGCALL: Reaper Group Uses New Malware to Deploy RAT. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
- [FinFisher. (n.d.). Retrieved September 12, 2024.](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
- [Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
- [McLellan, T. and Moore, J. et al. (2021, April 29). UNC2447 SOMBRAT and FIVEHANDS Ransomware: A Sophisticated Financial Threat. Retrieved June 2, 2021.](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [Matthews, M. and Backhouse, W. (2021, June 15). Handy guide to a new Fivehands ransomware variant. Retrieved June 24, 2021.](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)
- [Ramin Nafisi. (2021, September 27). FoggyWeb: Targeted NOBELIUM malware leads to persistent backdoor. Retrieved October 4, 2021.](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
- [ESET Research. (2025, December 2). MuddyWater: Snakes by the riverbank. Retrieved February 17, 2026.](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
- [Adamitis, D. et al. (2019, June 4). It's alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign. Retrieved May 11, 2020.](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
- [Kakara, H., Maruyama, E. (2020, April 17). Gamaredon APT Group Use Covid-19 Lure in Campaigns. Retrieved May 19, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/gamaredon-apt-group-use-covid-19-lure-in-campaigns/)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Unit 42. (2022, December 20). Russia’s Trident Ursa (aka Gamaredon APT) Cyber Conflict Operations Unwavering Since Invasion of Ukraine. Retrieved September 12, 2024.](https://unit42.paloaltonetworks.com/trident-ursa/)
- [Quinn, J. (2019, March 25). The odd case of a Gh0stRAT variant. Retrieved July 15, 2020.](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
- [Meltzer, M. et al. (2024, January 10). Active Exploitation of Two Zero-Day Vulnerabilities in Ivanti Connect Secure VPN. Retrieved February 27, 2024.](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/)
- [Idan Dardikman. (2025, October 18). GlassWorm: First Self-Propagating Worm Using Invisible Code Hits OpenVSX Marketplace. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace)
- [Gal Hachamov. (2025, December 29). GlassWorm Goes Mac: Fresh Infrastructure, New Tricks. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
- [Kirill Boychenko. (2026, January 31). GlassWorm Loader Hits Open VSX via Developer Account Compromise. Retrieved April 10, 2026.](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [Smith, L., Leathery, J., Read, B. (2021, March 4). New SUNSHUTTLE Second-Stage Backdoor Uncovered Targeting U.S.-Based Entity; Possible Connection to UNC2452. Retrieved March 12, 2021.](https://www.fireeye.com/blog/threat-research/2021/03/sunshuttle-second-stage-backdoor-targeting-us-based-entity.html)
- [Szappanos, G. & Brandt, A. (2021, March 1). “Gootloader” expands its payload delivery options. Retrieved September 30, 2022.](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)
- [Pirozzi, A. (2021, June 16). Gootloader: ‘Initial Access as a Service’ Platform Expands Its Search for High Value Targets. Retrieved May 28, 2024.](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)
- [Falcone, R., et al. (2018, August 02). The Gorgon Group: Slithering Between Nation State and Cybercrime. Retrieved August 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [Sandvik, Runa. (2021, October 1). Made In America: Green Lambert for OS X. Retrieved March 21, 2022.](https://objective-see.com/blog/blog_0x68.html)
- [Sandvik, Runa. (2021, October 18). Green Lambert and ATT&CK. Retrieved November 17, 2024.](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)
- [Priego, A. (2021, July). THE BROTHERS GRIM: THE REVERSING TALE OF GRIMAGENT MALWARE USED BY RYUK. Retrieved September 19, 2024.](https://www.group-ib.com/blog/grimagent/)
- [Tom Spring. (2017, January 11). Spammers Revive Hancitor Downloader Campaigns. Retrieved August 13, 2020.](https://threatpost.com/spammers-revive-hancitor-downloader-campaigns/123011/)
- [Anubhav, A., Jallepalli, D. (2016, September 23). Hancitor (AKA Chanitor) observed using multiple attack approaches. Retrieved August 13, 2020.](https://www.fireeye.com/blog/threat-research/2016/09/hancitor_aka_chanit.html)
- [Tujague, J., Bunce, D. (n.d.). Crypted Hearts: Exposing the HeartCrypt Packer-as-a-Service Operation. Retrieved April 16, 2026.](https://unit42.paloaltonetworks.com/packer-as-a-service-heartcrypt-malware/)
- [Check Point Research. (2025, March 10). Blind Eagle: …And Justice for All. Retrieved April 16, 2026.](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
- [Thomas, W. et al. (2022, February 25). CrowdStrike Falcon Protects from New Wiper Malware Used in Ukraine Cyberattacks. Retrieved March 25, 2022.](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
- [Kirill Boychenko. (2025, April 4). Lazarus Expands Malicious npm Campaign: 11 New Packages Add Malware Loaders and Bitbucket Payloads. Retrieved October 20, 2025.](https://socket.dev/blog/lazarus-expands-malicious-npm-campaign-11-new-packages-add-malware-loaders-and-bitbucket)
- [Kirill Boychenko. (2025, July 14). Contagious Interview Campaign Escalates With 67 Malicious npm Packages and New Malware Loader. Retrieved October 19, 2025.](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [Breitenbacher, D. (2024). Unmasking HiddenFace. Retrieved April 17, 2026.](https://jsac.jpcert.or.jp/archive/2024/pdf/JSAC2024_2_8_Breitenbacher_en.pdf)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [Sanmillan, I. (2019, May 29). HiddenWasp Malware Stings Targeted Linux Systems. Retrieved June 24, 2019.](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)
- [Malwarebytes Threat Intelligence Team. (2020, June 4). New LNK attack tied to Higaisa APT discovered. Retrieved March 2, 2021.](https://blog.malwarebytes.com/threat-analysis/2020/06/higaisa/)
- [Singh, S. Singh, A. (2020, June 11). The Return on the Higaisa APT. Retrieved March 2, 2021.](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)
- [Chen, J. et al. (2021, February 3). Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes. Retrieved April 5, 2021.](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [Alexndru-Cristian Bardas. (2025, October 30). DPRK’s Playbook: Kimsuky’s HttpTroy and Lazarus’s New BLINDINGCAN Variant. Retrieved April 8, 2026.](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)
- [Counter Threat Unit Research Team . (2022, June 23). BRONZE STARLIGHT RANSOMWARE OPERATIONS USE HUI LOADER. Retrieved December 7, 2023.](https://www.secureworks.com/research/bronze-starlight-ransomware-operations-use-hui-loader)
- [Lunghi, D. and Lu, K. (2021, April 9). Iron Tiger APT Updates Toolkit With Evolved SysUpdate Malware. Retrieved November 12, 2021.](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
- [CrowdStrike. (2022, May). ICEAPPLE: A NOVEL INTERNET INFORMATION SERVICES (IIS) POST-EXPLOITATION FRAMEWORK. Retrieved June 27, 2022.](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
- [QiAnXin Threat Intelligence Center. (2019, February 18). APT-C-36: Continuous Attacks Targeting Colombian Government Institutions and Corporations. Retrieved May 5, 2020.](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [Anton Cherepanov. (2017, June 12). Win32/Industroyer: A new threat for industrial controls systems. Retrieved December 18, 2020.](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Reichel, D. (2021, February 19). IronNetInjector: Turla’s New Malware Loading Tool. Retrieved February 24, 2021.](https://unit42.paloaltonetworks.com/ironnetinjector/)
- [Check Point. (2024, November 12). Hamas-affiliated Threat Actor WIRTE Continues its Middle East Operations and Moves to Disruptive Activity. Retrieved April 20, 2026.](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
- [Falcone, R. and Lee, B. (2017, October 9). OilRig Group Steps Up Attacks with New Delivery Documents and New Injector Trojan. Retrieved January 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/10/unit42-oilrig-group-steps-attacks-new-delivery-documents-new-injector-trojan/)
- [Hromcova, Z. and Burgher, A. (2023, September 21). OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes. Retrieved November 21, 2024.](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
- [Mohammad Kazem Hassan Nejad, WithSecure. (2024, April 17). KAPEKA A novel backdoor spotted in Eastern Europe. Retrieved January 6, 2025.](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Ray, V. and Hayashi, K. (2019, February 1). Tracking OceanLotus’ new Downloader, KerrDown. Retrieved October 1, 2021.](https://unit42.paloaltonetworks.com/tracking-oceanlotus-new-downloader-kerrdown/)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [Dahan, A. et al. (2020, November 2). Back to the Future: Inside the Kimsuky KGH Spyware Suite. Retrieved November 6, 2020.](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [Den Iuzvyk, Tim Peck. (2025, February 13). Analyzing DEEP#DRIVE: North Korean Threat Actors Observed Exploiting Trusted Platforms for Targeted Attacks. Retrieved August 19, 2025.](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [M.Leveille, M., Sanmillan, I. (2021, January). A WILD KOBALOS APPEARS Tricksy Linux malware goes after HPCs. Retrieved August 24, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
- [Jazi, H. (2021, February). LazyScripter: From Empire to double RAT. Retrieved November 17, 2024.](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
- [Karmi, D. (2020, January 4). A Look Into Konni 2019 Campaign. Retrieved April 28, 2020.](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)
- [Threat Intelligence Team. (2021, August 23). New variant of Konni malware used in campaign targetting Russia. Retrieved January 5, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
- [Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
- [Conteras, T., Splunk Research Team. (2025, September 25). From Prompt to Payload: LAMEHUG’s LLM-Driven Cyber Intrusion. Retrieved April 21, 2026.](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
- [Proofpoint Threat Research and Team Cymru S2 Threat Research. (2024, April 4). Latrodectus: This Spider Bytes Like Ice . Retrieved May 31, 2024.](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
- [Stepanic, D. and Bousseaden, S. (2024, May 15). Spring Cleaning with LATRODECTUS: A Potential Replacement for ICEDID. Retrieved September 13, 2024.](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
- [Batista, J. (2024, June 17). Latrodectus, are you coming back?. Retrieved September 13, 2024.](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
- [Saini, A. and Hossein, J. (2022, January 27). North Korea’s Lazarus APT leverages Windows Update client, GitHub in latest campaign. Retrieved January 27, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)
- [Pradhan, A. (2022, February 8). LolZarus: Lazarus Group Incorporating Lolbins into Campaigns. Retrieved March 22, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)
- [Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
- [Faou, M. (2019, May). Turla LightNeuron: One email away from remote code execution. Retrieved June 24, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
- [Canadian Centre for Cyber Security. (2024, April 24). Cyber Activity Impacting CISCO ASA VPNs. Retrieved January 6, 2025.](https://www.cyber.gc.ca/en/news-events/cyber-activity-impacting-cisco-asa-vpns)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [Bourhis, P., Sekoia TDR. (2024, February 1). Unveiling the intricacies of DiceLoader. Retrieved May 14, 2025.](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
- [FBI. (2022, February 4). Indicators of Compromise Associated with LockBit 2.0 Ransomware. Retrieved January 24, 2025.](https://www.ic3.gov/CSA/2022/220204.pdf)
- [Elsad, A. et al. (2022, June 9). LockBit 2.0: How This RaaS Operates and How to Protect Against It. Retrieved January 24, 2025.](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
- [Walter, J. (2022, July 21). LockBit 3.0 Update | Unpicking the Ransomware’s Latest Anti-Analysis and Evasion Techniques. Retrieved February 5, 2025.](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [INCIBE-CERT. (2024, March 14). LockBit: response and recovery actions. Retrieved February 5, 2025.](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
- [Muhammad, I., Unterbrink, H.. (2021, January 6). A Deep Dive into Lokibot Infection Chain. Retrieved August 31, 2021.](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
- [Raggi, M. Schwarz, D.. (2019, August 1). LookBack Malware Targets the United States Utilities Sector with Phishing Attacks Impersonating Engineering Licensing Boards. Retrieved February 25, 2021.](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
- [Hsu, K. et al. (2020, June 24). Lucifer: New Cryptojacking and DDoS Hybrid Malware Exploiting High and Critical Vulnerabilities to Infect Windows Devices. Retrieved November 16, 2020.](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
- [Leandro Fróes, Netskope. (2025, January 23). Lumma Stealer: Fake CAPTCHAs & New Techniques to Evade Detection. Retrieved March 22, 2025.](https://www.netskope.com/blog/lumma-stealer-fake-captchas-new-techniques-to-evade-detection)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [Asheer Malhotra, Vitor Ventura & Jungsoo An, Cisco Talos. (2022, September 7). MagicRAT: Lazarus’ latest gateway into victim networks. Retrieved December 30, 2024.](https://blog.talosintelligence.com/lazarus-magicrat/)
- [SCILabs. (2021, December 23). Cyber Threat Profile Malteiro. Retrieved March 13, 2024.](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
- [Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Del Fierro, C. Kessem, L.. (2020, January 8). From Mega to Giga: Cross-Version Comparison of Top MegaCortex Modifications. Retrieved February 15, 2021.](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
- [Accenture Security. (2018, April 23). Hogfish Redleaves Campaign. Retrieved July 2, 2018.](http://web.archive.org/web/20220810112638/https:/www.accenture.com/t20180423T055005Z_w_/se-en/_acnmedia/PDF-76/Accenture-Hogfish-Threat-Analysis.pdf)
- [Matsuda, A., Muhammad I. (2018, September 13). APT10 Targeting Japanese Corporations Using Updated TTPs. Retrieved September 17, 2018.](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
- [Leong, R., Perez, D., Dean, T. (2019, October 31). MESSAGETAP: Who’s Reading Your Text Messages?. Retrieved May 11, 2020.](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)
- [Erlich, C. (2020, April 3). The Avast Abuser: Metamorfo Banking Malware Hides By Abusing Avast Executable. Retrieved May 26, 2020.](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
- [Sierra, E., Iglesias, G.. (2018, April 24). Metamorfo Campaigns Targeting Brazilian Users. Retrieved July 30, 2020.](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
- [ESET Research. (2019, October 3). Casbaneiro: peculiarities of this banking Trojan that affects Brazil and Mexico. Retrieved September 23, 2021.](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
- [Rosenberg, J. (2018, June 14). MirageFox: APT15 Resurfaces With New Tools Based On Old Ones. Retrieved September 21, 2018.](https://web.archive.org/web/20180615122133/https://www.intezer.com/miragefox-apt15-resurfaces-with-new-tools-based-on-old-ones/)
- [ESET Security. (2019, November 19). Mispadu: Advertisement for a discounted Unhappy Meal. Retrieved March 13, 2024.](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
- [GReAT. (2019, April 10). Gaza Cybergang Group1, operation SneakyPastes. Retrieved May 13, 2020.](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
- [Microsoft Threat Intelligence. (2024, May 28). Moonstone Sleet emerges as new North Korean threat actor with new bag of tricks. Retrieved August 26, 2024.](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)
- [Punsaen Boonyakarn, Shawn Chew, Logeswaran Nadarajan, Mathew Potaczek, Jakub Jozwiak, and Alex Marvi. (2024, June 18). Cloaked and Covert: Uncovering UNC3886 Espionage Operations. Retrieved September 24, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [Villadsen, O.. (2019, August 29). More_eggs, Anyone? Threat Actor ITG08 Strikes Again. Retrieved September 16, 2019.](https://securityintelligence.com/posts/more_eggs-anyone-threat-actor-itg08-strikes-again/)
- [FBI, CISA, CNMF, NCSC-UK. (2022, February 24). Iranian Government-Sponsored Actors Conduct Cyber Operations Against Global Government and Commercial Networks. Retrieved September 27, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
- [Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
- [Villanueva, M., Co, M. (2018, June 14). Another Potential MuddyWater Campaign uses Powershell-based PRB-Backdoor. Retrieved July 3, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/another-potential-muddywater-campaign-uses-powershell-based-prb-backdoor/)
- [ClearSky Cyber Security. (2018, November). MuddyWater Operations in Lebanon and Oman: Using an Israeli compromised domain for a two-stage campaign. Retrieved November 29, 2018.](https://www.clearskysec.com/wp-content/uploads/2018/11/MuddyWater-Operations-in-Lebanon-and-Oman.pdf)
- [Malhortra, A and Ventura, V. (2022, January 31). Iranian APT MuddyWater targets Turkish users via malicious PDFs, executables. Retrieved June 22, 2022.](https://blog.talosintelligence.com/2022/01/iranian-apt-muddywater-targets-turkey.html)
- [Dex. (n.d.). New Mustang Panda’s campaing against Australia. Retrieved August 4, 2025.](https://lab52.io/blog/new-mustang-pandas-campaing-against-australia/)
- [EclecticIQ Threat Research Team. (2023, February 2). Mustang Panda APT Group Uses European Commission-Themed Lure to Deliver PlugX Malware. Retrieved September 9, 2025.](https://blog.eclecticiq.com/mustang-panda-apt-group-uses-european-commission-themed-lure-to-deliver-plugx-malware)
- [Secureworks Counter Threat Unit Research Team. (2022, September 8). BRONZE PRESIDENT Targets Government Officials. Retrieved September 9, 2025.](https://www.secureworks.com/blog/bronze-president-targets-government-officials)
- [Patrick Whitsell. (2025, August 25). Deception in Depth: PRC-Nexus Espionage Campaign Hijacks Web Traffic to Target Diplomats. Retrieved September 9, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)
- [Szappanos, G., Brandt, A.. (2020, May 27). Netwalker ransomware tools give insight into threat actor. Retrieved May 27, 2020.](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)
- [Threat Hunter Team. (2024, July 23). Daggerfly: Espionage Group Makes Major Update to Toolset. Retrieved July 25, 2024.](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [Grunzweig, J., Lee, B. (2018, September 27). New KONNI Malware attacking Eurasia and Southeast Asia. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [Hromcova, Z. and Burgher, A. (2023, December 14). OilRig’s persistent attacks using cloud service-powered downloaders. Retrieved November 26, 2024.](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
- [Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
- [Lee, B., Falcone, R. (2018, February 23). OopsIE! OilRig Uses ThreeDollars to Deliver New Trojan. Retrieved July 16, 2018.](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)
- [Crowdstrike. (2020, March 2). 2020 Global Threat Report. Retrieved December 11, 2020.](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)
- [Hromcova, Z. (2019, July). OKRUM AND KETRICAN: AN OVERVIEW OF RECENT KE3CHANG GROUP ACTIVITY. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-uncovers-operation-honeybee-malicious-document-campaign-targeting-humanitarian-aid-groups/)
- [M. Porolli. (2021, January 21). Operation Spalax: Targeted malware attacks in Colombia. Retrieved September 16, 2022.](https://www.welivesecurity.com/2021/01/12/operation-spalax-targeted-malware-attacks-colombia/)
- [Carbon Black Threat Analysis Unit. (2019, February 12). New macOS Malware Variant of Shlayer (OSX) Discovered. Retrieved August 8, 2019.](https://blogs.vmware.com/security/2020/02/vmware-carbon-black-tau-threat-analysis-shlayer-macos.html)
- [Phil Stokes. (2020, September 8). Coming Out of Your Shell: From Shlayer to ZShlayer. Retrieved September 13, 2021.](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)
- [Phil Stokes. (2021, February 16). 20 Common Tools & Techniques Used by macOS Threat Actors & Malware. Retrieved August 23, 2021.](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
- [Erye Hernandez and Danny Tsechansky. (2017, June 22). The New and Improved macOS Backdoor from OceanLotus. Retrieved September 8, 2023.](https://unit42.paloaltonetworks.com/unit42-new-improved-macos-backdoor-oceanlotus/)
- [John Wolfram, Josh Murchie, Matt Lin, Daniel Ainsworth, Robert Wallace, Dimiter Andonov, Dhanesh Kizhakkinan, Jacob Thompson. (2025, January 8). Ivanti Connect Secure VPN Targeted in New Zero-Day Exploitation. Retrieved April 14, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
- [Aleksandar Milenkoski, Luigi Martire. (2024, December 10). Operation Digital Eye | Chinese APT Compromises Critical Digital Infrastructure via Visual Studio Code Tunnels. Retrieved February 27, 2025.](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels/)
- [Brett Stone-Gross & Nikolaos Pantazopoulos. (2023, May 24). Technical Analysis of Pikabot. Retrieved July 12, 2024.](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)
- [Daniel Stepanic & Salim Bitam. (2024, February 23). PIKABOT, I choose you!. Retrieved July 12, 2024.](https://www.elastic.co/security-labs/pikabot-i-choose-you)
- [Swachchhanda Shrawan Poudel. (2024, February). Pikabot: A Sophisticated and Modular Backdoor Trojan with Advanced Evasion Techniques. Retrieved July 12, 2024.](https://www.logpoint.com/wp-content/uploads/2024/02/logpoint-etpr-pikabot.pdf)
- [Trustwave SpiderLabs. (2020, June 22). Pillowmint: FIN7’s Monkey Thief . Retrieved July 27, 2020.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
- [Unit 42. (2022, June 13). GALLIUM Expands Targeting Across Telecommunications, Government and Finance Sectors With New PingPull Tool. Retrieved August 7, 2022.](https://unit42.paloaltonetworks.com/pingpull-gallium/)
- [Tartare, M. et al. (2020, May 21). No “Game over” for the Winnti Group. Retrieved August 24, 2020.](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
- [Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
- [Raggi, M. et al. (2022, March 7). The Good, the Bad, and the Web Bug: TA416 Increases Operational Tempo Against European Governments as Conflict in Ukraine Escalates. Retrieved March 16, 2022.](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Asheer Malhotra, Jungsoo An, Kendall Mc. (2022, May 5). Mustang Panda deploys a new wave of malware targeting Europe. Retrieved August 4, 2025.](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
- [Mercer, W. Rascagneres, P. Ventura, V. (2020, October 6). PoetRAT: Malware targeting public and private sector in Azerbaijan evolves . Retrieved April 9, 2021.](https://blog.talosintelligence.com/2020/10/poetrat-update.html)
- [Symantec Threat Hunter Team. (2023, October 19). Crambus: New Campaign Targets Middle Eastern Government. Retrieved November 27, 2024.](https://www.security.com/threat-intelligence/crambus-middle-east-government)
- [Cybereason Nocturnus. (2022, February 1). PowerLess Trojan: Iranian APT Phosphorus Adds New PowerShell Backdoor for Espionage. Retrieved June 1, 2022.](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)
- [Cyber National Mission Force. (2022, January 12). Iranian intel cyber suite of malware uses open source tools. Retrieved September 30, 2022.](https://www.cybercom.mil/Media/News/Article/2897570/iranian-intel-cyber-suite-of-malware-uses-open-source-tools/)
- [Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.](https://objective-see.com/blog/blog_0x25.html)
- [Microsoft Threat Intelligence Center. (2022, February 4). ACTINIUM targets Ukrainian organizations. Retrieved February 18, 2022.](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
- [Nick Dai, Vickie Su, Sunny Lu. (2022, November 18). Earth Preta Spear-Phishing Governments Worldwide. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
- [Gorelik, M.. (2019, June 10). SECURITY ALERT: FIN8 IS BACK IN BUSINESS, TARGETING THE HOSPITALITY INDUSTRY. Retrieved June 13, 2019.](http://blog.morphisec.com/security-alert-fin8-is-back)
- [Dumont, R. (2022, June 13). Technical Analysis of PureCrypter: A Fully-Functional Loader Distributing Remote Access Trojans and Information Stealers. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
- [Checkpoint Research. (2021, November 15). Uncovering MosesStaff techniques: Ideology over Money. Retrieved August 11, 2022.](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
- [Cyberint. (2021, May 25). Qakbot Banking Trojan. Retrieved September 27, 2021.](https://blog.cyberint.com/qakbot-banking-trojan)
- [Morrow, D. (2021, April 15). The rise of QakBot. Retrieved September 27, 2021.](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [Lee, B., Falcone, R. (2018, July 25). OilRig Targets Technology Service Provider and Government Agency with QUADAGENT. Retrieved August 9, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [S2W TALON. (2022, June 16). Raccoon Stealer is Back with a New Version. Retrieved August 1, 2024.](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
- [Quentin Bourgue, Pierre le Bourhis, & Sekoia TDR. (2022, June 28). Raccoon Stealer v2 - Part 1: The return of the dead. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
- [Symantec Threat Hunter Team. (2021, January 18). Raindrop: New Malware Discovered in SolarWinds Investigation. Retrieved January 19, 2021.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-raindrop-malware)
- [MSTIC, CDOC, 365 Defender Research Team. (2021, January 20). Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop . Retrieved January 22, 2021.](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
- [Vrabie, V. (2021, April 23). NAIKON – Traces from a Military Cyber-Espionage Operation. Retrieved June 29, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Alfano, V. et al. (2025, February 12). RansomHub Never Sleeps Episode 1: The evolution of modern ransomware. Retrieved March 17, 2025.](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
- [Perez, D. et al. (2021, May 27). Re-Checking Your Pulse: Updates on Chinese APT Actors Compromising Pulse Secure VPN Devices. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
- [Christopher So. (2022, December 20). Raspberry Robin Malware Targets Telecom, Governments. Retrieved May 17, 2024.](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
- [Falcone, R. (2020, July 22). OilRig Targets Middle Eastern Telecommunications Organization and Adds Novel C2 Channel with Steganography to Its Inventory. Retrieved July 28, 2020.](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
- [Splunk Threat Research Team. (2023, June 1). Do Not Cross The 'RedLine' Stealer: Detections and Analysis. Retrieved September 17, 2025.](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
- [Lamparski, L. et al. (2025, March 11). Ghost in the Router: China-Nexus Espionage Actor UNC3886 Targets Juniper Routers. Retrieved June 24, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers)
- [Juniper Networks, Cybersecurity R&D. (2025, March 11). The RedPenguin Malware Incident. Retrieved June 24, 2025.](https://supportportal.juniper.net/sfc/servlet.shepherd/document/download/069Dp00000FzdmIIAR?operationContext=S1)
- [Legezo, D. (2019, January 30). Chafer used Remexi malware to spy on Iran-based foreign diplomatic entities. Retrieved April 17, 2019.](https://securelist.com/chafer-used-remexi-malware/89538/)
- [Han, Karsten. (2019, June 4). Strange Bits: Sodinokibi Spam, CinaRAT, and Fake G DATA. Retrieved August 4, 2020.](https://www.gdatasoftware.com/blog/2019/06/31724-strange-bits-sodinokibi-spam-cinarat-and-fake-g-data)
- [Mamedov, O, et al. (2019, July 3). Sodin ransomware exploits Windows vulnerability and processor architecture. Retrieved August 4, 2020.](https://securelist.com/sodin-ransomware/91473/)
- [Cylance. (2019, July 3). hreat Spotlight: Sodinokibi Ransomware. Retrieved August 4, 2020.](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
- [McAfee. (2019, October 2). McAfee ATR Analyzes Sodinokibi aka REvil Ransomware-as-a-Service – What The Code Tells Us. Retrieved August 4, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
- [Intel 471 Malware Intelligence team. (2020, March 31). REvil Ransomware-as-a-Service – An analysis of a ransomware affiliate operation. Retrieved August 4, 2020.](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [Falcone, R. (2018, January 25). OilRig uses RGDoor IIS Backdoor on Targets in the Middle East. Retrieved July 6, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-oilrig-uses-rgdoor-iis-backdoor-targets-middle-east/)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [CISA. (2022, September 23). AA22-264A Iranian State Actors Conduct Cyber Operations Against the Government of Albania. Retrieved August 6, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
- [Hiroaki, H. (2025, April 30). Earth Kasha Updates TTPs in Latest Campaign Targeting Taiwan and Japan. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
- [Liebenberg, D.. (2018, August 30). Rocke: The Champion of Monero Miners. Retrieved May 26, 2020.](https://blog.talosintelligence.com/2018/08/rocke-champion-of-monero-miners.html)
- [Lee, B., Falcone, R. (2019, January 18). DarkHydrus delivers new Trojan that can use Google Drive for C2 communications. Retrieved April 17, 2019.](https://unit42.paloaltonetworks.com/darkhydrus-delivers-new-trojan-that-can-use-google-drive-for-c2-communications/)
- [Cash, D., Grunzweig, J., Adair, S., Lancaster, T. (2021, August 25). North Korean BLUELIGHT Special: InkySquid Deploys RokRAT. Retrieved October 1, 2021.](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
- [Jazi, Hossein. (2021, January 6). Retrohunting APT37: North Korean APT used VBA self decode technique to inject RokRat. Retrieved March 22, 2022.](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
- [Alex Turing, Hui Wang. (2021, April 28). RotaJakiro: A long live secret backdoor with 0 VT detection. Retrieved June 14, 2023.](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
- [Awasthi, P. (2026, January 8). Reborn in Rust: Muddy Water Evolves Tooling with RustyWater Implant. Retrieved March 19, 2026.](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [Hasherezade. (2021, April 6). A deep dive into Saint Bot, a new downloader. Retrieved June 9, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
- [Cherepanov, A.. (2016, December 13). The rise of TeleBots: Analyzing disruptive KillDisk attacks. Retrieved June 10, 2020.](https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/)
- [Cherepanov, A.. (2017, July 4). Analysis of TeleBots’ cunning backdoor . Retrieved June 11, 2020.](https://www.welivesecurity.com/2017/07/04/analysis-of-telebots-cunning-backdoor/)
- [Symantec Threat Hunter Team. (2023, July 18). FIN8 Uses Revamped Sardonic Backdoor to Deliver Noberus Ransomware. Retrieved August 9, 2023.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)
- [Schwarz, D. et al. (2019, October 16). TA505 Distributes New SDBbot Remote Access Trojan with Get2 Downloader. Retrieved May 29, 2020.](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
- [Frydrych, M. (2020, April 14). TA505 Continues to Infect Networks With SDBbot RAT. Retrieved May 29, 2020.](https://web.archive.org/web/20200420201624/https://securityintelligence.com/posts/ta505-continues-to-infect-networks-with-sdbbot-rat/)
- [Kaspersky Lab. (2017, August). ShadowPad: popular server management software hit in supply chain attack. Retrieved March 22, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
- [Falcone, R. (2018, December 13). Shamoon 3 Targets Oil and Gas Organization. Retrieved March 14, 2019.](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
- [Unit 42. (2025, July 31). Active Exploitation of Microsoft SharePoint Vulnerabilities: Threat Brief (Updated). Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/microsoft-sharepoint-cve-2025-49704-cve-2025-49706-cve-2025-53770/)
- [ClearSky Cyber Security . (2021, August). New Iranian Espionage Campaign By “Siamesekitten” - Lyceum. Retrieved June 6, 2022.](https://www.clearskysec.com/siamesekitten/)
- [Ilascu, I. (2020, December 14). Hacking group’s new malware abuses Google and Facebook services. Retrieved December 28, 2020.](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [Prizmant, D. (2021, June 7). Siloscape: First Known Malware Targeting Windows Containers to Compromise Cloud Environments. Retrieved June 9, 2021.](https://unit42.paloaltonetworks.com/siloscape/)
- [Remillano, A., Urbanec, J. (2019, September 19). Skidmap Linux Malware Uses Rootkit Capabilities to Hide Cryptocurrency-Mining Payload. Retrieved June 4, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
- [Perez, D. et al. (2021, April 20). Check Your Pulse: Suspected APT Actors Leverage Authentication Bypass Techniques and Pulse Secure Zero-Day. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
- [Baker, B., Unterbrink H. (2018, July 03). Smoking Guns - Smoke Loader learned new tricks. Retrieved July 5, 2018.](https://blog.talosintelligence.com/2018/07/smoking-guns-smoke-loader-learned-new.html#more)
- [Lorber, N. (2021, May 7). Revealing the Snip3 Crypter, a Highly Evasive RAT Loader. Retrieved September 13, 2023.](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
- [CISA. (2020, July 16). MAR-10296782-1.v1 – SOREFANG. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
- [Falcone, R., et al. (2020, March 3). Molerats Delivers Spark Backdoor to Government and Telecommunications Organizations. Retrieved December 14, 2020.](https://unit42.paloaltonetworks.com/molerats-delivers-spark-backdoor/)
- [Yuma Masubuchi. (2025, February 20). SPAWNCHIMERA Malware: The Chimera Spawning from Ivanti Connect Secure Vulnerability. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2025/02/spawnchimera.html)
- [Shields, W. (2024, January 18). Russian threat group COLDRIVER expands its targeting of Western officials to include the use of malware. Retrieved June 13, 2024.](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)
- [Platt, J. and Reeves, J.. (2019, March). FIN7 Revisited: Inside Astra Panel and SQLRat Malware. Retrieved June 18, 2019.](https://www.flashpoint-intel.com/blog/fin7-revisited-inside-astra-panel-and-sqlrat-malware/)
- [Kumar, A., Stone-Gross, Brett. (2021, September 28). Squirrelwaffle: New Loader Delivering Cobalt Strike. Retrieved August 9, 2022.](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
- [Palazolo, G. (2021, October 7). SquirrelWaffle: New Malware Loader Delivering Cobalt Strike and QakBot. Retrieved August 9, 2022.](https://www.netskope.com/blog/squirrelwaffle-new-malware-loader-delivering-cobalt-strike-and-qakbot)
- [Symantec Security Response. (2017, November 7). Sowbug: Cyber espionage group targets South American and Southeast Asian governments. Retrieved November 16, 2017.](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: ToneShell and StarProxy | P1. Retrieved July 21, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
- [Cybereason Global SOC Team. (n.d.). THREAT ANALYSIS REPORT: Inside the LockBit Arsenal - The StealBit Exfiltration Tool. Retrieved January 29, 2025.](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
- [Tyler McGraw, Thomas Elkins, and Evan McCann. (2024, May 10). Ongoing Social Engineering Campaign Linked to Black Basta Ransomware Operators. Retrieved January 31, 2025.](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)
- [DCSO CyTec Blog. (2022, November 8). #ShortAndMalicious: StrelaStealer aims for mail credentials. Retrieved December 31, 2024.](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)
- [Benjamin Chang, Goutam Tripathy, Pranay Kumar Chhaparwal, Anmol Maurya & Vishwa Thothathri, Palo Alto Networks. (2024, March 22). Large-Scale StrelaStealer Campaign in Early 2024. Retrieved December 31, 2024.](https://unit42.paloaltonetworks.com/strelastealer-campaign/)
- [Fortgale. (2023, September 18). StrelaStealer Malware Analysis. Retrieved December 31, 2024.](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [CrowdStrike Intelligence Team. (2021, January 11). SUNSPOT: An Implant in the Build Process. Retrieved January 11, 2021.](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
- [AhnLab. (2022, April 4). SystemBC Being Used by Various Attackers . Retrieved June 18, 2025.](https://asec.ahnlab.com/en/33600/)
- [Black Lotus Labs . (2025, September 18). SystemBC: Bringing the noise. Retrieved December 15, 2025.](https://blog.lumen.com/systembc-bringing-the-noise/)
- [Terefos, A. (2020, November 18). TA505: A Brief History of Their Time. Retrieved July 14, 2022.](https://research.nccgroup.com/2020/11/18/ta505-a-brief-history-of-their-time/)
- [CISA, FBI, DOD. (2021, August). MAR-10292089-1.v2 – Chinese Remote Access Trojan: TAIDOOR. Retrieved August 24, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [Check Point Research. (2020, December 22). SUNBURST, TEARDROP and the NetSec New Normal. Retrieved January 6, 2021.](https://research.checkpoint.com/2020/sunburst-teardrop-and-the-netsec-new-normal/)
- [Legezo, D. (2018, June 13). LuckyMouse hits national data center to organize country-level waterholing campaign. Retrieved August 18, 2018.](https://securelist.com/luckymouse-hits-national-data-center/86083/)
- [Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle. Retrieved October 27, 2021.](https://securelist.com/lazarus-threatneedle/100803/)
- [Nathaniel Morales, Nick Dai. (2025, February 18). Earth Preta Mixes Legitimate and Malicious Components to Sidestep Detection. Retrieved September 10, 2025.](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
- [Tom Fakterman. (2024, September 6). Chinese APT Abuses VSCode to Target Government in Asia. Retrieved March 24, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage/)
- [Beek, C. (2020, November 5). Operation North Star: Behind The Scenes. Retrieved December 20, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
- [Reaves, J. (2016, October 15). TrickBot: We Missed you, Dyre. Retrieved August 2, 2018.](https://www.fidelissecurity.com/threatgeek/2016/10/trickbot-we-missed-you-dyre)
- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [Joe Security. (2020, July 13). TrickBot's new API-Hammering explained. Retrieved September 30, 2021.](https://www.joesecurity.org/blog/498839998833561473)
- [Ray, V. (2016, November 22). Tropic Trooper Targets Taiwanese Government and Fossil Fuel Provider With Poison Ivy. Retrieved November 9, 2018.](https://researchcenter.paloaltonetworks.com/2016/11/unit42-tropic-trooper-targets-taiwanese-government-and-fossil-fuel-provider-with-poison-ivy/)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Tomonaga, S. (2018, March 6). Malware “TSCookie”. Retrieved May 6, 2020.](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
- [Ubiedo, L. (2025, November 20). Blockchain and Node.js abused by Tsundere: an emerging botnet. Retrieved April 6, 2026.](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)
- [Ctrl-Alt-Intel. (2026, March 4). MuddyWater Exposed: Inside an Iranian APT operation . Retrieved April 6, 2026.](https://ctrlaltintel.com/research/MuddyWater/)
- [Adam Burgher. (2021, June 10). BackdoorDiplomacy: Upgrading from Quarian to Turian. Retrieved September 1, 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [US-CERT. (2018, June 14). MAR-10135536-12 – North Korean Trojan: TYPEFRAME. Retrieved July 13, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
- [Volexity Threat Research. (2024, April 12). Zero-Day Exploitation of Unauthenticated Remote Code Execution Vulnerability in GlobalProtect (CVE-2024-3400). Retrieved November 20, 2024.](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)
- [Unit 42. (2024, April 12). Threat Brief: Operation MidnightEclipse, Post-Exploitation Activity Related to CVE-2024-3400 . Retrieved January 15, 2025.](https://unit42.paloaltonetworks.com/cve-2024-3400/)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Proofpoint Staff. (2016, August 25). Nightmare on Tor Street: Ursnif variant Dreambot adds Tor functionality. Retrieved June 5, 2019.](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)
- [Salem, E. et al. (2020, May 28). VALAK: MORE THAN MEETS THE EYE . Retrieved June 19, 2020.](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
- [Duncan, B. (2020, July 24). Evolution of Valak, from Its Beginnings to Mass Distribution. Retrieved August 31, 2020.](https://unit42.paloaltonetworks.com/valak-evolution/)
- [Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
- [US-CERT. (2017, November 01). Malware Analysis Report (MAR) - 10135536-D. Retrieved July 16, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)
- [Counter Threat Unit Research Team. (2023, May 24). Chinese Cyberespionage Group BRONZE SILHOUETTE Targets U.S. Government and Defense Organizations. Retrieved July 27, 2023.](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [Antenucci, S., Pantazopoulos, N., Sandee, M. (2020, June 23). WastedLocker: A New Ransomware Variant Developed By The Evil Corp Group. Retrieved September 14, 2021.](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
- [Shinji Robert Arasawa, Joshua Aquino, Charles Steven Derion, Juhn Emmanuel Atanque, Francisrey Joshua Castillo, John Carlo Marquez, Henry Salcedo, John Rainier Navato, Arianne Dela Cruz, Raymart Yambot & Ian Kenefick. (2024, January 9). Black Basta-Affiliated Water Curupira’s Pikabot Spam Campaign. Retrieved July 17, 2024.](https://www.trendmicro.com/en_us/research/24/a/a-look-into-pikabot-spam-wave-campaign.html)
- [Su, V. et al. (2019, December 11). Waterbear Returns, Uses API Hooking to Evade Security. Retrieved February 22, 2021.](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
- [CISA. (2020, July 16). MAR-10296782-3.v1 – WELLMAIL. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
- [PWC. (2020, July 16). How WellMess malware has been used to target COVID-19 vaccines. Retrieved September 24, 2020.](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)
- [PWC. (2020, August 17). WellMess malware: analysis of its Command and Control (C2) server. Retrieved September 29, 2020.](https://www.pwc.co.uk/issues/cyber-security-services/insights/wellmess-analysis-command-control.html)
- [CISA. (2020, July 16). MAR-10296782-2.v1 – WELLMESS. Retrieved September 24, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)
- [Biasini, N. et al.. (2022, January 21). Ukraine Campaign Delivers Defacement and Wipers, in Continued Escalation. Retrieved March 14, 2022.](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
- [S2W. (2022, January 18). Analysis of Destructive Malware (WhisperGate) targeting Ukraine. Retrieved March 14, 2022.](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)
- [Wardle, Patrick. (2018, December 20). Middle East Cyber-Espionage analyzing WindShift's implant: OSX.WindTail (part 1). Retrieved October 3, 2019.](https://objective-see.com/blog/blog_0x3B.html)
- [Chronicle Blog. (2019, May 15). Winnti: More than just Windows and Gates. Retrieved April 29, 2020.](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)
- [Novetta Threat Research Group. (2015, April 7). Winnti Analysis. Retrieved February 8, 2017.](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
- [Matthieu Faou. (2023, October 25). Winter Vivern exploits zero-day vulnerability in Roundcube Webmail servers. Retrieved July 29, 2024.](https://www.welivesecurity.com/en/eset-research/winter-vivern-exploits-zero-day-vulnerability-roundcube-webmail-servers/)
- [McLellan, T. et al. (2024, January 12). Cutting Edge: Suspected APT Targets Ivanti Connect Secure VPN in New Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
- [S2 Grupo. (2019, April 2). WIRTE Group attacking the Middle East. Retrieved May 24, 2019.](https://lab52.io/blog/wirte-group-attacking-the-middle-east/)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [CheckPoint Research. (2021, July 1). IndigoZebra APT continues to attack Central Asia with evolving tools. Retrieved September 24, 2021.](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
- [Zscaler Threatlabz. (2025, January 27). Technical Analysis of Xloader Versions 6 and 7 | Part 1. Retrieved March 11, 2025.](https://www.zscaler.com/blogs/security-research/technical-analysis-xloader-versions-6-and-7-part-1)
- [Nart Villeneuve, Randi Eitzman, Sandor Nemes & Tyler Dean, Google Cloud. (2017, October 5). Significant FormBook Distribution Campaigns Impacting the U.S. and South Korea. Retrieved March 11, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)
- [Alintanahin, K. (2015). Operation Tropic Trooper: Relying on Tried-and-Tested Flaws to Infiltrate Secret Keepers. Retrieved June 14, 2019.](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)
- [Falcone, R., Lee, B. (2018, November 20). Sofacy Continues Global Attacks and Wheels Out New ‘Cannon’ Trojan. Retrieved November 26, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
- [ESET. (2018, November 20). Sednit: What’s going on with Zebrocy?. Retrieved February 12, 2019.](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
- [Huss, D., et al. (2017, February 2). Oops, they did it again: APT Targets Russia and Belarus with ZeroT and PlugX. Retrieved April 5, 2018.](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)
- [Brumaghin, E., et al. (2017, November 02). Poisoning the Well: Banking Trojan Targets Google Search Results. Retrieved November 5, 2018.](https://blog.talosintelligence.com/2017/11/zeus-panda-campaign.html#More)
- [Itkin, E. and Cohen, I. (2021, February 22). The Story of Jian – How APT31 Stole and Used an Unknown Equation Group 0-Day. Retrieved March 24, 2021.](https://research.checkpoint.com/2021/the-story-of-jian/)
- [Raghuprasad, C . (2022, May 11). Bitter APT adds Bangladesh to their targets. Retrieved June 1, 2022.](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Lazarus Group]] [related_actor:: [[Lazarus Group]]]
- 🦠 **Tooling Capability Integration:** Executed via malware family [[DragonForce]] [related_malware:: [[DragonForce]]]
- 🦠 **Tooling Capability Integration:** Executed via malware family [[Lumma Stealer]] [related_malware:: [[Lumma Stealer]]]

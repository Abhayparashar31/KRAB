# Obfuscated Files or Information

## Description

Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the system or in transit. This is common behavior that can be used across different platforms and the network to evade defenses.

Payloads may be compressed, archived, or encrypted in order to avoid detection. These payloads may be used during Initial Access or later to mitigate detection. Sometimes a user's action may be required to open and Deobfuscate/Decode Files or Information for User Execution . The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary. [1] Adversaries may also use compressed or archived scripts, such as JavaScript.

Portions of files can also be encoded to hide the plain-text strings that would otherwise help defenders with discovery. [2] Payloads may also be split into separate, seemingly benign files that only reveal malicious functionality when reassembled. [3]

Adversaries may also abuse Command Obfuscation to obscure commands executed from payloads or directly via Command and Scripting Interpreter . Environment variables, aliases, characters, and other platform/language specific semantics can be used to evade signature based detections and application control mechanisms. [4] [5] [6]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0025 | 2016 Ukraine Electric Power Attack | During the 2016 Ukraine Electric Power Attack , Sandworm Team used heavily obfuscated code with Industroyer in its Windows Notepad backdoor. [7] |
| C0057 | 3CX Supply Chain Attack | During the 3CX Supply Chain Attack , AppleJeus payloads use AES-256 GCM cipher to encrypt data to include ICONICSTEALER and VEILEDSIGNAL. [8] [9] |
| S1028 | Action RAT | Action RAT 's commands, strings, and domains can be Base64 encoded within the payload. [10] |
| S0045 | ADVSTORESHELL | Most of the strings in ADVSTORESHELL are encrypted with an XOR-based algorithm; some strings are also encrypted with 3DES and reversed. API function names are also reversed, presumably to avoid detection in memory. [11] [12] |
| S0331 | Agent Tesla | Agent Tesla has had its code obfuscated in an apparent attempt to make analysis difficult. [13] Agent Tesla has used the Rijndael symmetric encryption algorithm to encrypt strings. [14] |
| S1025 | Amadey | Amadey has obfuscated strings such as antivirus vendor names, domains, files, and others. [15] |
| S0504 | Anchor | Anchor has obfuscated code with stack strings and string encryption. [16] |
| S9027 | ANELLDR | ANELLDR code implements anti-analysis techniques including control flow flattening and Mixed Boolean Arithmetic (MBA). [17] |
| S0584 | AppleJeus | AppleJeus has XOR-encrypted collected system information prior to sending to a C2. AppleJeus has also used the open source ADVObfuscation library for its components. [18] |
| S0622 | AppleSeed | AppleSeed has the ability to Base64 encode its payload and custom encrypt API calls. [19] |
| G0099 | APT-C-36 | APT-C-36 has used ConfuserEx to obfuscate its variant of Imminent Monitor , compressed payloads and RAT packages, and password protected encrypted email attachments to avoid detection. [20] APT-C-36 has also compressed initial droppers into ZIP, LHA and UUE formats. [21] |
| G0022 | APT3 | APT3 obfuscates files or information to help evade defensive measures. [22] |
| G0067 | APT37 | APT37 obfuscates strings and payloads. [23] [24] [25] |
| G0096 | APT41 | APT41 used VMProtected binaries in multiple intrusions. [26] |
| S0640 | Avaddon | Avaddon has used encrypted strings. [27] |
| S1053 | AvosLocker | AvosLocker has used XOR-encoded strings. [28] |
| G0135 | BackdoorDiplomacy | BackdoorDiplomacy has obfuscated tools and malware it uses with VMProtect. [29] |
| G0063 | BlackOasis | BlackOasis 's first stage shellcode contains a NOP sled with alternative instructions that was likely designed to bypass antivirus tools. [30] |
| S1226 | BOOKWORM | BOOKWORM has been delivered using self-extracting RAR archives. [31] |
| S0635 | BoomBox | BoomBox can encrypt data using AES prior to exfiltration. [32] |
| S0651 | BoxCaon | BoxCaon used the "StackStrings" obfuscation technique to hide malicious functionalities. [33] |
| S1161 | BPFDoor | BPFDoor can require a password to activate the backdoor and uses RC4 encryption or static library encryption libtomcrypt . [34] |
| S9015 | BRICKSTORM | BRICKSTORM has utilized Go libraries to include Garble to obfuscate code. [35] [36] |
| S1063 | Brute Ratel C4 | Brute Ratel C4 has used encrypted payload files and maintains an encrypted configuration structure in memory. [37] [38] |
| S1039 | Bumblebee | Bumblebee has been delivered as password-protected zipped ISO files and used control-flow-flattening to obfuscate the flow of functions. [39] [40] [41] |
| S0482 | Bundlore | Bundlore has obfuscated data with base64, AES, RC4, and bz2. [42] |
| S1118 | BUSHWALK | BUSHWALK can encrypt the resulting data generated from C2 commands with RC4. [43] |
| C0015 | C0015 | During C0015 , the threat actors used Base64-encoded strings. [44] |
| C0017 | C0017 | During C0017 , APT41 broke malicious binaries, including DEADEYE and KEYPLUG , into multiple sections on disk to evade detection. [45] |
| S0030 | Carbanak | Carbanak encrypts strings to make analysis more difficult. [46] |
| S0335 | Carbon | Carbon encrypts configuration files and tasks for the malware to complete using CAST-128 algorithm. [47] [48] |
| S0465 | CARROTBALL | CARROTBALL has used a custom base64 alphabet to decode files. [49] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP can use a custom Base64 alphabet to encode an API decryption key. [50] |
| S0660 | Clambling | The Clambling executable has been obfuscated when dropped on a compromised host. [51] |
| S1105 | COATHANGER | COATHANGER can store obfuscated configuration information in the last 56 bytes of the file /date/.bd.key/preload.so . [52] |
| S0154 | Cobalt Strike | Cobalt Strike can hash functions to obfuscate calls to the Windows API and use a public/private key pair to encrypt Beacon session metadata. [53] [54] |
| S0369 | CoinTicker | CoinTicker initially downloads a hidden encoded file. [55] |
| S0244 | Comnie | Comnie uses RC4 and Base64 to obfuscate strings. [56] |
| S0126 | ComRAT | ComRAT has encrypted its virtual file system using AES-256 in XTS mode. [57] [58] |
| S0608 | Conficker | Conficker has obfuscated its code to prevent its removal from host machines. [59] |
| S0575 | Conti | Conti can use compiler-based obfuscation for its code, encrypt DLLs, and hide Windows API calls. [60] [61] [62] |
| S0137 | CORESHELL | CORESHELL obfuscates strings using a custom stream cipher. [63] |
| S0625 | Cuba | Cuba has used multiple layers of obfuscation to avoid analysis, including its Base64 encoded payload. [64] |
| S1111 | DarkGate | DarkGate uses a hard-coded string as a seed, along with the victim machine hardware identifier and input text, to generate a unique string used as an internal mutex value to evade static detection based on mutexes. [65] |
| S1066 | DarkTortilla | DarkTortilla has been obfuscated with the DeepSea .NET and ConfuserEx code obfuscators. [66] |
| S0187 | Daserf | Daserf uses encrypted Windows APIs and also encrypts data using the alternative base64+RC4 or the Caesar cipher. [67] |
| S0354 | Denis | Denis obfuscates its code and encrypts the API names. [68] |
| S0659 | Diavol | Diavol has Base64 encoded the RSA public key used for encrypting files. [69] |
| S0694 | DRATzarus | DRATzarus can be partly encrypted with XOR. [70] |
| S0384 | Dridex | Dridex 's strings are obfuscated using RC4. [71] |
| S0502 | Drovorub | Drovorub has used XOR encrypted payloads in WebSocket client to server messages. [72] |
| S0062 | DustySky | The DustySky dropper uses a function to obfuscate the name of functions and other parts of the malware. [73] |
| G1006 | Earth Lusca | Earth Lusca used Base64 to encode strings. [74] |
| S0377 | Ebury | Ebury has obfuscated its strings with a simple XOR encryption with a static key. [75] |
| S0593 | ECCENTRICBANDWAGON | ECCENTRICBANDWAGON has encrypted strings with RC4. [76] |
| S0624 | Ecipekac | Ecipekac can use XOR, AES, and DES to encrypt loader shellcode. [77] |
| S0605 | EKANS | EKANS uses encoded strings in its process kill list. [78] |
| S0091 | Epic | Epic heavily obfuscates its code to make analysis more difficult. [79] |
| S0512 | FatDuke | FatDuke can use base64 encoding, string stacking, and opaque predicates for obfuscation. [80] |
| S0355 | Final1stspy | Final1stspy obfuscates strings with base64 encoding. [81] |
| S0182 | FinFisher | FinFisher is heavily obfuscated in many ways, including through the use of spaghetti code in its functions in an effort to confuse disassembly programs. It also uses a custom XOR algorithm to obfuscate code. [82] [83] |
| S0696 | Flagpro | Flagpro has been delivered within ZIP or RAR password-protected archived files. [84] |
| S9033 | Fooder | Fooder has stored its embedded payload in encrypted form within the binary, using a hardcoded key modified at runtime to produce the AES decryption key. [85] |
| G0093 | GALLIUM | GALLIUM used a modified version of HTRAN in which they obfuscated strings such as debug messages in an apparent attempt to evade detection. [86] |
| G0084 | Gallmaker | Gallmaker obfuscated shellcode used during execution. [87] |
| G0047 | Gamaredon Group | Gamaredon Group has delivered self-extracting 7z archive files within malicious document attachments. [88] Additionally, Gamaredon Group has used an obfuscated .drv file. [89] |
| S1138 | Gootloader | The Gootloader first stage script is obfuscated using random alpha numeric strings. [90] [91] |
| S0690 | Green Lambert | Green Lambert has encrypted strings. [92] [93] |
| S0632 | GrimAgent | GrimAgent has used Rotate on Right (RoR) and Rotate on Left (RoL) functionality to encrypt strings. [94] |
| S0132 | H1N1 | H1N1 uses multiple techniques to obfuscate strings, including XOR. [95] |
| S0499 | Hancitor | Hancitor has used Base64 to encode malicious links. [96] |
| S0070 | HTTPBrowser | HTTPBrowser 's code may be obfuscated through structured exception handling and return-oriented programming. [97] |
| S9007 | HTTPTroy | HTTPTroy has obfuscated strings using Single Instruction Multiple Data (SIMD) instructions to hinder analysis and detection. [98] |
| S0203 | Hydraq | Hydraq uses basic obfuscation in the form of spaghetti code. [99] [100] |
| S0434 | Imminent Monitor | Imminent Monitor has encrypted the spearphish attachments to avoid detection from email gateways; the debugger also encrypts information before sending to the C2. [20] |
| S0604 | Industroyer | Industroyer uses heavily obfuscated code in its Windows Notepad backdoor. [7] |
| S0259 | InnaputRAT | InnaputRAT uses an 8-byte XOR key to obfuscate API names and other strings contained in the payload. [101] |
| S0260 | InvisiMole | InvisiMole avoids analysis by encrypting all strings, internal files, configuration data and by using a custom executable format. [102] [103] |
| S0189 | ISMInjector | ISMInjector is obfuscated with the off-the-shelf SmartAssembly .NET obfuscator created by red-gate.com. [104] |
| S0201 | JPIN | A JPIN uses a encrypted and compressed payload that is disguised as a bitmap within the resource section of the installer. [105] |
| S0283 | jRAT | jRAT ’s Java payload is encrypted with AES. [106] Additionally, backdoor files are encrypted using DES as a stream cipher. Later variants of jRAT also incorporated AV evasion methods such as Java bytecode obfuscation via the commercial Allatori obfuscation tool. [107] |
| S0265 | Kazuar | Kazuar is obfuscated using the open source ConfuserEx protector. Kazuar also obfuscates the name of created files/folders/mutexes and encrypts debug messages written to log files using the Rijndael cipher. [108] |
| G0004 | Ke3chang | Ke3chang has used Base64-encoded shellcode strings. [109] |
| S0607 | KillDisk | KillDisk uses VMProtect to make reverse engineering the malware more difficult. [110] |
| G0094 | Kimsuky | Kimsuky has obfuscated binary strings including the use of XOR encryption and Base64 encoding. [111] [112] Kimsuky has also modified the first byte of DLL implants targeting victims to prevent recognition of the executable file format. [113] Kimsuky has obfuscated strings using Single Instruction Multiple Data (SIMD) instructions that complicate static analysis. [98] |
| S0641 | Kobalos | Kobalos encrypts all strings using RC4 and bundles all functionality into a single function call. [114] |
| S0681 | Lizar | Lizar has obfuscated the fingerprint of the victim system, the local IP address, and the Fowler-Noll-V 1 (FNV-1) hash of the local IP address using an XOR operation. The data is then sent to the C2 server. [115] |
| S9020 | LODEINFO | LODEINFO has used control flow flattening to obfuscate code. [116] |
| S0447 | Lokibot | Lokibot has obfuscated strings with base64 encoding. [117] |
| S1213 | Lumma Stealer | Lumma Stealer has used SmartAssembly to obfuscate .NET payloads. [118] |
| S0167 | Matryoshka | Matryoshka obfuscates API function names using a substitute cipher combined with Base64 encoding. [119] |
| S0449 | Maze | Maze has decrypted strings and other important information during the encryption process. Maze also calls certain functions dynamically to hinder analysis. [120] |
| S0500 | MCMD | MCMD can Base64 encode output strings prior to sending to C2. [121] |
| S0051 | MiniDuke | MiniDuke can use control flow flattening to obscure code. [80] |
| G1036 | Moonstone Sleet | Moonstone Sleet delivers encrypted payloads in pieces that are then combined together to form a new portable executable (PE) file during installation. [122] |
| G0129 | Mustang Panda | Mustang Panda has delivered initial payloads hidden using archives and encoding measures. [123] [124] [125] [126] [127] [128] [129] [130] [31] [131] [132] [133] Mustang Panda has also utilized opaque predicates in payloads to hinder analysis. [134] |
| S0336 | NanoCore | NanoCore ’s plugins were obfuscated with Eazfuscater.NET 3.3. [135] |
| S0198 | NETWIRE | NETWIRE has used a custom obfuscation algorithm to hide strings including Registry keys, APIs, and DLL names. [136] |
| S1090 | NightClub | NightClub can obfuscate strings using the congruential generator (LCG): staten+1 = (690069 × staten + 1) mod 232 . [137] |
| S0353 | NOKKI | NOKKI uses Base64 encoding for strings. [138] |
| S9025 | NOOPLDR | NOOPLDR can use control flow flattening to help hide malicious code. [139] [140] |
| S0138 | OLDBAIT | OLDBAIT obfuscates internal strings and unpacks them at startup. [63] |
| S0264 | OopsIE | OopsIE uses the Confuser protector to obfuscate an embedded .Net Framework assembly used for C2. OopsIE also encodes collected data in hexadecimal format before writing to files on disk and obfuscates strings. [141] [142] |
| S0229 | Orz | Some Orz strings are base64 encoded, such as the embedded DLL known as MockDll. [143] |
| S0594 | Out1 | Out1 has the ability to encode data. [144] |
| S0598 | P.A.S. Webshell | P.A.S. Webshell can use encryption and base64 encoding to hide strings and to enforce access control once deployed. [145] |
| S0517 | Pillowmint | Pillowmint has obfuscated the AES key used for encryption. [146] |
| S0124 | Pisloader | Pisloader obfuscates files by splitting strings into smaller sub-strings and including "garbage" strings that are never used. The malware also uses return-oriented programming (ROP) technique and single-byte XOR to obfuscate data. [147] |
| S0013 | PlugX | PlugX can use API hashing and modify the names of strings to evade detection. [51] [130] |
| S0428 | PoetRAT | PoetRAT has used a custom encryption scheme for communication between scripts. [148] |
| S0012 | PoisonIvy | PoisonIvy hides any strings related to its own indicators of compromise. [149] |
| S0518 | PolyglotDuke | PolyglotDuke can custom encrypt strings. [80] |
| S0150 | POSHSPY | POSHSPY appends a file signature header (randomly selected from six file types) to encrypted data prior to upload or download. [150] |
| S0393 | PowerStallion | PowerStallion uses a XOR cipher to encrypt command output written to its OneDrive C2 server. [151] |
| S1228 | PUBLOAD | PUBLOAD has obfuscated DLL names using the ror13AddHash32 algorithm. [124] |
| S0196 | PUNCHBUGGY | PUNCHBUGGY has hashed most its code's functions and encrypted payloads with base64 and XOR. [152] |
| S0197 | PUNCHTRACK | PUNCHTRACK is loaded and executed by a highly obfuscated launcher. [153] |
| S0650 | QakBot | QakBot has hidden code within Excel spreadsheets by turning the font color to white and splitting it across multiple cells. [154] |
| S0458 | Ramsay | Ramsay has base64-encoded its portable executable and hidden itself under a JPG header. Ramsay can also embed information within document footers. [155] |
| S1130 | Raspberry Robin | Raspberry Robin uses mixed-case letters for filenames and commands to evade detection. [156] |
| G1039 | RedCurl | RedCurl has used malware with string encryption. [157] RedCurl has also encrypted data and has encoded PowerShell commands using Base64. [158] [159] RedCurl has used PyArmor to obfuscate code execution of LaZagne . [158] Additionally, RedCurl has obfuscated downloaded files by renaming them as commonly used tools and has used echo , instead of file names themselves, to execute files. [160] |
| S0511 | RegDuke | RegDuke can use control-flow flattening or the commercially available .NET Reactor for obfuscation. [80] |
| S0332 | Remcos | Remcos uses RC4 and base64 to obfuscate data, including Registry entries and file paths. [161] Remcos can also employ control flow flattening to hinder analysis. [162] |
| G0106 | Rocke | Rocke has modified UPX headers after packing files to break unpackers. [163] |
| S0240 | ROKRAT | ROKRAT can encrypt data prior to exfiltration by using an RSA public key. [25] [164] |
| S0148 | RTM | RTM strings, network data, configuration, and modules are encrypted with a modified RC4 algorithm. [165] [166] |
| S9037 | RustyWater | RustyWater has an obfuscated function (i.e. love_me__()) that dynamically reconstructs the string WScript.Shell using hard-coded ASCII values and the Chr() function. [167] |
| S0446 | Ryuk | Ryuk can use anti-disassembly and code transformation obfuscation techniques. [62] |
| S1018 | Saint Bot | Saint Bot has been obfuscated to help avoid detection. [168] |
| S1099 | Samurai | Samurai can encrypt the names of requested APIs. [169] |
| G0034 | Sandworm Team | Sandworm Team has used Base64 encoding within malware variants. [170] |
| S1085 | Sardonic | Sardonic can use certain ConfuserEx features for obfuscation and can be encoded in a base64 string. [171] |
| S0461 | SDBbot | SDBbot has the ability to XOR the strings for its installer component with a hardcoded 128 byte key. [172] |
| S0596 | ShadowPad | ShadowPad has encrypted its payload, a virtual file system, and various files. [173] [74] |
| S9008 | Shai-Hulud | Shai-Hulud has utilized double-base64 encoding to store stolen secrets within the Github Action Logs within the victim account. [174] [175] [176] [177] Shai-Hulud has also leveraged three layers of base64 encoding of exfiltrated data for anti-forensic purposes. [178] |
| S0140 | Shamoon | Shamoon contains base64-encoded strings. [179] |
| S0445 | ShimRatReporter | ShimRatReporter encrypted gathered information with a combination of shifting and XOR using a static key. [180] |
| S0063 | SHOTPUT | SHOTPUT is obscured using XOR encoding and appended to a valid GIF file. [181] [182] |
| S0623 | Siloscape | Siloscape itself is obfuscated and uses obfuscated API calls. [183] |
| S0633 | Sliver | Sliver obfuscates configuration and other static files using native Go libraries such as garble and gobfuscate to inhibit configuration analysis and static detection. [184] |
| S1104 | SLOWPULSE | SLOWPULSE can hide malicious code in the padding regions between legitimate functions in the Pulse Secure libdsplibs.so file. [185] |
| S1035 | Small Sieve | Small Sieve has the ability to use a custom hex byte swapping encoding scheme combined with an obfuscated Base64 function to protect program strings and Telegram credentials. [186] |
| S1086 | Snip3 | Snip3 has the ability to obfuscate strings using XOR encryption. [187] |
| S0627 | SodaMaster | SodaMaster can use "stackstrings" for obfuscation. [77] |
| S0615 | SombRAT | SombRAT can encrypt strings with XOR-based routines and use a custom AES storage format for plugins, configuration, C2 domains, and harvested data. [188] [189] [190] |
| S0516 | SoreFang | SoreFang has the ability to encode and RC6 encrypt data sent to C2. [191] |
| S0142 | StreamEx | StreamEx obfuscates some commands by using statically programmed fragments of strings when starting a DLL. It also uses a one-byte xor against 0x91 to encode configuration data. [192] |
| S1183 | StrelaStealer | StrelaStealer has been distributed in ISO archives. [193] StrelaStealer has been delivered in encrypted, password-protected ZIP archives. [194] |
| S0559 | SUNBURST | SUNBURST obfuscated collected system information using a FNV-1a + XOR algorithm. [195] |
| S0562 | SUNSPOT | SUNSPOT encrypted log entries it collected with the stream cipher RC4 using a hard-coded key. It also uses AES128-CBC encrypted blobs for SUNBURST source code and data extracted from the SolarWinds Orion <MsBuild.exe process. [196] |
| S1064 | SVCReady | SVCReady can encrypt victim data with an RC4 cipher. [197] |
| S0242 | SynAck | SynAck payloads are obfuscated prior to compilation to inhibit analysis and/or reverse engineering. [198] [199] |
| S0467 | TajMahal | TajMahal has used an encrypted Virtual File System to store plugins. [200] |
| S0560 | TEARDROP | TEARDROP created and read from a file with a fake JPG header, and its payload was encrypted with a simple rotating XOR cipher. [195] [201] [202] |
| S0266 | TrickBot | TrickBot uses non-descriptive names to hide functionality. [203] |
| S0094 | Trojan.Karagany | Trojan.Karagany can base64 encode and AES-128-CBC encrypt data prior to transmission. [204] |
| S0647 | Turian | Turian can use VMProtect for obfuscation. [29] |
| S0476 | Valak | Valak has the ability to base64 encode and XOR encrypt strings. [205] [206] [207] |
| G0112 | Windshift | Windshift has used string encoding with floating point calculations. [208] |
| S0117 | XTunnel | A version of XTunnel introduced in July 2015 obfuscated the binary using opaque predicates and other techniques in a likely attempt to obfuscate it and bypass security products. [209] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1049 | Antivirus/Antimalware | Anti-virus can be used to automatically detect and quarantine suspicious files. Consider utilizing the Antimalware Scan Interface (AMSI) on Windows 10+ to analyze commands after being processed/interpreted. [210] |
| M1047 | Audit | Consider periodic review of common fileless storage locations (such as the Registry or WMI repository) to potentially identify abnormal and malicious data. |
| M1040 | Behavior Prevention on Endpoint | On Windows 10+, enable Attack Surface Reduction (ASR) rules to prevent execution of potentially obfuscated payloads. [211] |
| M1017 | User Training | Ensure that a finite amount of ingress points to a software deployment system exist with restricted access for those required to allow and enable newly deployed software. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0378 | Behavioral Detection of Obfuscated Files or Information | AN1064 | Correlates script execution or suspicious parent processes with creation or modification of encoded, compressed, or encrypted file formats (e.g., .zip, .7z, .enc) and abnormal command-line syntax or PowerShell obfuscation. |
| AN1065 | Detects use of gzip, base64, tar, or openssl in scripts or commands that encode/encrypt files after file staging or system enumeration. |  |  |
| AN1066 | Monitors use of archive or encryption tools (zip, openssl) tied to user-scripted activity or binaries writing encoded payloads under /Users or /Volumes. |  |  |
| AN1067 | Identifies transfer of base64, uuencoded, or high-entropy files over HTTP, FTP, or custom protocols in lateral movement or exfiltration streams. |  |  |
| AN1068 | Detects encoded PowerCLI or Base64-encoded payloads staged via datastore uploads or shell access (e.g., ESXi Shell or backdoored VIBs). |  |  |

---

## References

- [Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
- [Pierre-Marc Bureau. (2013, April 26). Linux/Cdorked.A: New Apache backdoor being used in the wild to serve Blackhole. Retrieved September 10, 2017.](https://www.welivesecurity.com/2013/04/26/linuxcdorked-new-apache-backdoor-in-the-wild-serves-blackhole/)
- [Tedesco, B. (2016, September 23). Security Alert Summary. Retrieved February 12, 2018.](https://www.carbonblack.com/2016/09/23/security-advisory-variants-well-known-adware-families-discovered-include-sophisticated-obfuscation-techniques-previously-associated-nation-state-attacks/)
- [Bohannon, D. & Carr N. (2017, June 30). Obfuscation in the Wild: Targeted Attackers Lead the Way in Evasion Techniques. Retrieved February 12, 2018.](https://web.archive.org/web/20170923102302/https://www.fireeye.com/blog/threat-research/2017/06/obfuscation-in-the-wild.html)
- [Bohannon, D. & Holmes, L. (2017, July 27). Revoke-Obfuscation: PowerShell Obfuscation Detection Using Science. Retrieved November 17, 2024.](https://www.blackhat.com/docs/us-17/thursday/us-17-Bohannon-Revoke-Obfuscation-PowerShell-Obfuscation-Detection-And%20Evasion-Using-Science-wp.pdf)
- [White, J. (2017, March 10). Pulling Back the Curtains on EncodedCommand PowerShell Attacks. Retrieved February 12, 2018.](https://researchcenter.paloaltonetworks.com/2017/03/unit42-pulling-back-the-curtains-on-encodedcommand-powershell-attacks/)
- [Anton Cherepanov. (2017, June 12). Win32/Industroyer: A new threat for industrial controls systems. Retrieved December 18, 2020.](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
- [Ankur Saini, Callum Roxan, Charlie Gardner, Paul Rascagneres, Steven Adair, Tom Lancaster. (2023, March 30). 3CX Supply Chain Compromise Leads to ICONIC Incident. Retrieved October 21, 2025.](https://www.volexity.com/blog/2023/03/30/3cx-supply-chain-compromise-leads-to-iconic-incident/)
- [Jeff Johnson, Fred Plan, Adrian Sanchez, Renato Fontana, Jake Nicastro, Dimiter Andonov, Marius Fodoreanu, Daniel Scott. (2023, April 20). 3CX Software Supply Chain Compromise Initiated by a Prior Software Supply Chain Compromise; Suspected North Korean Actor Responsible. Retrieved August 25, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise/)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [Kaspersky Lab's Global Research and Analysis Team. (2015, December 4). Sofacy APT hits high profile targets with updated toolset. Retrieved December 10, 2015.](https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/)
- [Bitdefender. (2015, December). APT28 Under the Scope. Retrieved February 23, 2017.](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
- [Zhang, X. (2018, April 05). Analysis of New Agent Tesla Spyware Variant. Retrieved November 5, 2018.](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)
- [Jazi, H. (2020, April 16). New AgentTesla variant steals WiFi credentials. Retrieved May 19, 2020.](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)
- [Kasuya, M. (2020, January 8). Threat Spotlight: Amadey Bot Targets Non-Russian Users. Retrieved July 14, 2022.](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [Hiroaki, H. (2024, November 26). Guess Who’s Back - The Return of ANEL in the Recent Earth Kasha Spear-phishing Campaign in 2024. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
- [Cybersecurity and Infrastructure Security Agency. (2021, February 21). AppleJeus: Analysis of North Korea’s Cryptocurrency Malware. Retrieved March 1, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa21-048a)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [QiAnXin Threat Intelligence Center. (2019, February 18). APT-C-36: Continuous Attacks Targeting Colombian Government Institutions and Corporations. Retrieved May 5, 2020.](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
- [Global Research & Analysis Team, Kaspersky. (2024, August 19). BlindEagle flying high in Latin America. Retrieved April 16, 2026.](https://securelist.com/blindeagle-apt/113414/)
- [Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
- [Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)
- [GReAT. (2019, May 13). ScarCruft continues to evolve, introduces Bluetooth harvester. Retrieved June 4, 2019.](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)
- [Cash, D., Grunzweig, J., Adair, S., Lancaster, T. (2021, August 25). North Korean BLUELIGHT Special: InkySquid Deploys RokRAT. Retrieved October 1, 2021.](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
- [Glyer, C, et al. (2020, March). This Is Not a Test: APT41 Initiates Global Intrusion Campaign Using Multiple Exploits. Retrieved April 28, 2020.](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)
- [Yuste, J. Pastrana, S. (2021, February 9). Avaddon ransomware: an in-depth analysis and decryption of infected systems. Retrieved August 19, 2021.](https://arxiv.org/pdf/2102.04796.pdf)
- [Hasherezade. (2021, July 23). AvosLocker enters the ransomware scene, asks for partners. Retrieved January 11, 2023.](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
- [Adam Burgher. (2021, June 10). BackdoorDiplomacy: Upgrading from Quarian to Turian. Retrieved September 1, 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
- [Kaspersky Lab's Global Research & Analysis Team. (2017, October 16). BlackOasis APT and new targeted attacks leveraging zero-day exploit. Retrieved February 15, 2018.](https://securelist.com/blackoasis-apt-and-new-targeted-attacks-leveraging-zero-day-exploit/82732/)
- [Robert Falcone, Mike Scott, Juan Cortes. (2015, November 10). Bookworm Trojan: A Model of Modular Architecture. Retrieved July 21, 2025.](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)
- [MSTIC. (2021, May 28). Breaking down NOBELIUM’s latest early-stage toolset. Retrieved August 4, 2021.](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
- [CheckPoint Research. (2021, July 1). IndigoZebra APT continues to attack Central Asia with evolving tools. Retrieved September 24, 2021.](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
- [The Sandfly Security Team. (2022, May 11). BPFDoor - An Evasive Linux Backdoor Technical Analysis. Retrieved September 29, 2023.](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/)
- [Huseyin Can Yuceel. (2025, October 1). BRICKSTORM Malware: UNC5221 Targets Tech and Legal Sectors in the United States. Retrieved April 16, 2026.](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)
- [Sarah Yoder, John Wolfram, Ashley Pearson, Doug Bienstock, Josh Madeley, Josh Murchie, Brad Slaybaugh, Matt Lin, Geoff Carstairs, Austin Larsen. (2025, September 24). Another BRICKSTORM: Stealthy Backdoor Enabling Espionage into Tech and Legal Sectors. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
- [Harbison, M. and Renals, P. (2022, July 5). When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors. Retrieved February 1, 2023.](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
- [Chell, D. PART 3: How I Met Your Beacon – Brute Ratel. Retrieved February 6, 2023.](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)
- [Merriman, K. and Trouerbach, P. (2022, April 28). This isn't Optimus Prime's Bumblebee but it's Still Transforming. Retrieved August 22, 2022.](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
- [Cybereason. (2022, August 17). Bumblebee Loader – The High Road to Enterprise Domain Control. Retrieved August 29, 2022.](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
- [Salem, A. (2022, April 27). The chronicles of Bumblebee: The Hook, the Bee, and the Trickbot connection. Retrieved September 2, 2022.](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
- [Sushko, O. (2019, April 17). macOS Bundlore: Mac Virus Bypassing macOS Security Features. Retrieved June 30, 2020.](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
- [Lin, M. et al. (2024, January 31). Cutting Edge, Part 2: Investigating Ivanti Connect Secure VPN Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)
- [ESET. (2017, March 30). Carbon Paper: Peering into Turla’s second stage backdoor. Retrieved November 7, 2018.](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)
- [Accenture. (2020, October). Turla uses HyperStack, Carbon, and Kazuar to compromise government entity. Retrieved December 2, 2020.](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)
- [McCabe, A. (2020, January 23). The Fractured Statue Campaign: U.S. Government Agency Targeted in Spear-Phishing Attacks. Retrieved June 2, 2020.](https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Dutch Military Intelligence and Security Service (MIVD) & Dutch General Intelligence and Security Service (AIVD). (2024, February 6). Ministry of Defense of the Netherlands uncovers COATHANGER, a stealthy Chinese FortiGate RAT. Retrieved February 7, 2024.](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
- [Mavis, N. (2020, September 21). The Art and Science of Detecting Cobalt Strike. Retrieved September 12, 2024.](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Thomas Reed. (2018, October 29). Mac cryptocurrency ticker app installs backdoors. Retrieved April 23, 2019.](https://blog.malwarebytes.com/threat-analysis/2018/10/mac-cryptocurrency-ticker-app-installs-backdoors/)
- [Grunzweig, J. (2018, January 31). Comnie Continues to Target Organizations in East Asia. Retrieved June 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [CISA. (2020, October 29). Malware Analysis Report (AR20-303A). Retrieved December 9, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303a)
- [Trend Micro. (2014, March 18). Conficker. Retrieved February 18, 2021.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/conficker)
- [Baskin, B. (2020, July 8). TAU Threat Discovery: Conti Ransomware. Retrieved February 17, 2021.](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [Rochberger, L. (2021, January 12). Cybereason vs. Conti Ransomware. Retrieved February 17, 2021.](https://www.cybereason.com/blog/cybereason-vs.-conti-ransomware)
- [Podlosky, A., Hanel, A. et al. (2020, October 16). WIZARD SPIDER Update: Resilient, Reactive and Resolute. Retrieved June 15, 2021.](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)
- [FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [Ernesto Fernández Provecho, Pham Duy Phuc, Ciana Driscoll & Vinoo Thomas. (2023, November 21). The Continued Evolution of the DarkGate Malware-as-a-Service. Retrieved February 9, 2024.](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [Chen, J. and Hsieh, M. (2017, November 7). REDBALDKNIGHT/BRONZE BUTLER’s Daserf Backdoor Now Using Steganography. Retrieved December 27, 2017.](http://blog.trendmicro.com/trendlabs-security-intelligence/redbaldknight-bronze-butler-daserf-backdoor-now-using-steganography/)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [Check Point Research. (2021, January 4). Stopping Serial Killer: Catching the Next Strike. Retrieved September 7, 2021.](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)
- [NSA/FBI. (2020, August). Russian GRU 85th GTsSS Deploys Previously Undisclosed Drovorub Malware. Retrieved August 25, 2020.](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
- [ClearSky. (2016, January 7). Operation DustySky. Retrieved January 8, 2016.](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
- [Chen, J., et al. (2022). Delving Deep: An Analysis of Earth Lusca’s Operations. Retrieved July 1, 2022.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
- [M.Léveillé, M.. (2014, February 21). An In-depth Analysis of Linux/Ebury. Retrieved April 19, 2019.](https://www.welivesecurity.com/2014/02/21/an-in-depth-analysis-of-linuxebury/)
- [Cybersecurity and Infrastructure Security Agency. (2020, August 26). MAR-10301706-1.v1 - North Korean Remote Access Tool: ECCENTRICBANDWAGON. Retrieved March 18, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-239a)
- [GREAT. (2021, March 30). APT10: sophisticated multi-layered loader Ecipekac discovered in A41APT campaign. Retrieved June 17, 2021.](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
- [Zafra, D., et al. (2020, February 24). Ransomware Against the Machine: How Adversaries are Learning to Disrupt Industrial Production by Targeting IT and OT. Retrieved March 2, 2021.](https://www.fireeye.com/blog/threat-research/2020/02/ransomware-against-machine-learning-to-disrupt-industrial-production.html)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Grunzweig, J. (2018, October 01). NOKKI Almost Ties the Knot with DOGCALL: Reaper Group Uses New Malware to Deploy RAT. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
- [FinFisher. (n.d.). Retrieved September 12, 2024.](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
- [Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [ESET Research. (2025, December 2). MuddyWater: Snakes by the riverbank. Retrieved February 17, 2026.](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
- [Cybereason Nocturnus. (2019, June 25). Operation Soft Cell: A Worldwide Campaign Against Telecommunications Providers. Retrieved July 18, 2019.](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)
- [Symantec Security Response. (2018, October 10). Gallmaker: New Attack Group Eschews Malware to Live off the Land. Retrieved November 27, 2018.](https://www.symantec.com/blogs/threat-intelligence/gallmaker-attack-group)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Threat Hunter Team, Symantec and Carbon Black. (2025, April 10). Shuckworm Targets Foreign Military Mission Based in Ukraine. Retrieved July 23, 2025.](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)
- [Szappanos, G. & Brandt, A. (2021, March 1). “Gootloader” expands its payload delivery options. Retrieved September 30, 2022.](https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/)
- [Pirozzi, A. (2021, June 16). Gootloader: ‘Initial Access as a Service’ Platform Expands Its Search for High Value Targets. Retrieved May 28, 2024.](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)
- [Sandvik, Runa. (2021, October 1). Made In America: Green Lambert for OS X. Retrieved March 21, 2022.](https://objective-see.com/blog/blog_0x68.html)
- [Sandvik, Runa. (2021, October 18). Green Lambert and ATT&CK. Retrieved November 17, 2024.](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)
- [Priego, A. (2021, July). THE BROTHERS GRIM: THE REVERSING TALE OF GRIMAGENT MALWARE USED BY RYUK. Retrieved September 19, 2024.](https://www.group-ib.com/blog/grimagent/)
- [Reynolds, J.. (2016, September 13). H1N1: Technical analysis reveals new capabilities. Retrieved September 26, 2016.](http://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities)
- [Tom Spring. (2017, January 11). Spammers Revive Hancitor Downloader Campaigns. Retrieved August 13, 2020.](https://threatpost.com/spammers-revive-hancitor-downloader-campaigns/123011/)
- [Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)
- [Alexndru-Cristian Bardas. (2025, October 30). DPRK’s Playbook: Kimsuky’s HttpTroy and Lazarus’s New BLINDINGCAN Variant. Retrieved April 8, 2026.](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)
- [O'Gorman, G., and McDonald, G.. (2012, September 6). The Elderwood Project. Retrieved November 17, 2024.](https://web.archive.org/web/20190717233006/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf)
- [Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
- [ASERT Team. (2018, April 04). Innaput Actors Utilize Remote Access Trojan Since 2016, Presumably Targeting Victim Files. Retrieved July 9, 2018.](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Falcone, R. and Lee, B. (2017, October 9). OilRig Group Steps Up Attacks with New Delivery Documents and New Injector Trojan. Retrieved January 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/10/unit42-oilrig-group-steps-attacks-new-delivery-documents-new-injector-trojan/)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [Sharma, R. (2018, August 15). Revamped jRAT Uses New Anti-Parsing Techniques. Retrieved September 21, 2018.](https://www.symantec.com/blogs/threat-intelligence/jrat-new-anti-parsing-techniques)
- [Bingham, J. (2013, February 11). Cross-Platform Frutas RAT Builder and Back Door. Retrieved April 23, 2019.](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Fernando Merces, Byron Gelera, Martin Co. (2018, June 7). KillDisk Variant Hits Latin American Finance Industry. Retrieved January 12, 2021.](https://www.trendmicro.com/en_us/research/18/f/new-killdisk-variant-hits-latin-american-financial-organizations-again.html)
- [ThreatConnect. (2020, September 28). Kimsuky Phishing Operations Putting In Work. Retrieved October 30, 2020.](https://threatconnect.com/blog/kimsuky-phishing-operations-putting-in-work/)
- [Kim, J. et al. (2019, October). KIMSUKY GROUP: TRACKING THE KING OF THE SPEAR PHISHING. Retrieved November 2, 2020.](https://www.virusbulletin.com/virusbulletin/2020/03/vb2019-paper-kimsuky-group-tracking-king-spearphishing/)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [M.Leveille, M., Sanmillan, I. (2021, February 2). Kobalos – A complex Linux threat to high performance computing infrastructure. Retrieved August 24, 2021.](https://www.welivesecurity.com/2021/02/02/kobalos-complex-linux-threat-high-performance-computing-infrastructure/)
- [Bourhis, P., Sekoia TDR. (2024, February 1). Unveiling the intricacies of DiceLoader. Retrieved May 14, 2025.](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
- [ITOCHU. (2024, January 24). The Endless Struggle Against APT10: Insights from LODEINFO v0.6.6 - v0.7.3 Analysis. Retrieved April 17, 2026.](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
- [Hoang, M. (2019, January 31). Malicious Activity Report: Elements of Lokibot Infostealer. Retrieved May 15, 2020.](https://insights.infoblox.com/threat-intelligence-reports/threat-intelligence--22)
- [Cara Lin, Fortinet. (2024, January 8). Deceptive Cracked Software Spreads Lumma Variant on YouTube. Retrieved March 22, 2025.](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)
- [Minerva Labs LTD and ClearSky Cyber Security. (2015, November 23). CopyKittens Attack Group. Retrieved November 17, 2024.](https://cdn2.hubspot.net/hubfs/1903456/Whitepapers/CopyKittens.pdf)
- [Mundo, A. (2020, March 26). Ransomware Maze. Retrieved May 18, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
- [Secureworks. (2019, July 24). MCMD Malware Analysis. Retrieved August 13, 2020.](https://www.secureworks.com/research/mcmd-malware-analysis)
- [Microsoft Threat Intelligence. (2024, May 28). Moonstone Sleet emerges as new North Korean threat actor with new bag of tricks. Retrieved August 26, 2024.](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)
- [Anomali Threat Research. (2019, October 7). China-Based APT Mustang Panda Targets Minority Groups, Public and Private Sector Organizations. Retrieved April 12, 2021.](https://www.anomali.com/blog/china-based-apt-mustang-panda-targets-minority-groups-public-and-private-sector-organizations)
- [Asheer Malhotra, Jungsoo An, Kendall Mc. (2022, May 5). Mustang Panda deploys a new wave of malware targeting Europe. Retrieved August 4, 2025.](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
- [Counter Threat Unit Research Team. (2019, December 29). BRONZE PRESIDENT Targets NGOs. Retrieved April 13, 2021.](https://www.secureworks.com/research/bronze-president-targets-ngos)
- [Insikt Group. (2020, July 28). CHINESE STATE-SPONSORED GROUP ‘REDDELTA’ TARGETS THE VATICAN AND CATHOLIC ORGANIZATIONS. Retrieved April 13, 2021.](https://go.recordedfuture.com/hubfs/reports/cta-2020-0728.pdf)
- [Meyers, A. (2018, June 15). Meet CrowdStrike’s Adversary of the Month for June: MUSTANG PANDA. Retrieved April 12, 2021.](https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-june-mustang-panda/)
- [Nick Dai, Vickie Su, Sunny Lu. (2022, November 18). Earth Preta Spear-Phishing Governments Worldwide. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
- [Proofpoint Threat Research Team. (2020, November 23). TA416 Goes to Ground and Returns with a Golang PlugX Malware Loader. Retrieved April 13, 2021.](https://www.proofpoint.com/us/blog/threat-insight/ta416-goes-ground-and-returns-golang-plugx-malware-loader)
- [Raggi, M. et al. (2022, March 7). The Good, the Bad, and the Web Bug: TA416 Increases Operational Tempo Against European Governments as Conflict in Ukraine Escalates. Retrieved March 16, 2022.](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)
- [Secureworks Counter Threat Unit Research Team. (2022, April 27). BRONZE PRESIDENT Targets Russian Speakers with Updated PlugX. Retrieved September 9, 2025.](https://www.secureworks.com/blog/bronze-president-targets-russian-speakers-with-updated-plugx)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: PAKLOG, CorKLOG, and SplatCloak | P2. Retrieved September 12, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: ToneShell and StarProxy | P1. Retrieved July 21, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Kasza, A., Halfpop, T. (2016, February 09). NanoCoreRAT Behind an Increase in Tax-Themed Phishing E-mails. Retrieved November 9, 2018.](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
- [Maniath, S. and Kadam P. (2019, March 19). Dissecting a NETWIRE Phishing Campaign's Usage of Process Hollowing. Retrieved January 7, 2021.](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Grunzweig, J., Lee, B. (2018, September 27). New KONNI Malware attacking Eurasia and Southeast Asia. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [Lee, B., Falcone, R. (2018, February 23). OopsIE! OilRig Uses ThreeDollars to Deliver New Trojan. Retrieved July 16, 2018.](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)
- [Falcone, R., et al. (2018, September 04). OilRig Targets a Middle Eastern Government and Adds Evasion Techniques to OopsIE. Retrieved September 24, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-oilrig-targets-middle-eastern-government-adds-evasion-techniques-oopsie/)
- [Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
- [Peretz, A. and Theck, E. (2021, March 5). Earth Vetala – MuddyWater Continues to Target Organizations in the Middle East. Retrieved March 18, 2021.](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
- [ANSSI. (2021, January 27). SANDWORM INTRUSION SET CAMPAIGN TARGETING CENTREON SYSTEMS. Retrieved March 30, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
- [Trustwave SpiderLabs. (2020, June 22). Pillowmint: FIN7’s Monkey Thief . Retrieved July 27, 2020.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
- [Grunzweig, J., et al. (2016, May 24). New Wekby Attacks Use DNS Requests As Command and Control Mechanism. Retrieved August 17, 2016.](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
- [Mercer, W, et al. (2020, April 16). PoetRAT: Python RAT uses COVID-19 lures to target Azerbaijan public and private sectors. Retrieved April 27, 2020.](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
- [Hayashi, K. (2005, August 18). Backdoor.Darkmoon. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)
- [Dunwoody, M.. (2017, April 3). Dissecting One of APT29’s Fileless WMI and PowerShell Backdoors (POSHSPY). Retrieved April 5, 2017.](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [Gorelik, M.. (2019, June 10). SECURITY ALERT: FIN8 IS BACK IN BUSINESS, TARGETING THE HOSPITALITY INDUSTRY. Retrieved June 13, 2019.](http://blog.morphisec.com/security-alert-fin8-is-back)
- [Kizhakkinan, D., et al. (2016, May 11). Threat Actor Leverages Windows Zero-day Exploit in Payment Card Data Attacks. Retrieved February 12, 2018.](https://www.fireeye.com/blog/threat-research/2016/05/windows-zero-day-payment-cards.html)
- [Cyberint. (2021, May 25). Qakbot Banking Trojan. Retrieved September 27, 2021.](https://blog.cyberint.com/qakbot-banking-trojan)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Lauren Podber and Stef Rand. (2022, May 5). Raspberry Robin gets the worm early. Retrieved May 17, 2024.](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)
- [Antoniuk, D. (2023, July 17). RedCurl hackers return to spy on 'major Russian bank,' Australian company. Retrieved August 9, 2024.](https://therecord.media/redcurl-hackers-russian-bank-australian-company)
- [Group-IB. (2020, August). RedCurl: The Pentest You Didn’t Know About. Retrieved August 9, 2024.](https://www.group-ib.com/resources/research-hub/red-curl/)
- [Group-IB. (2021, November). RedCurl: The Awakening. Retrieved August 14, 2024.](https://www.group-ib.com/resources/research-hub/red-curl-2/)
- [Tancio et al. (2024, March 6). Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence. Retrieved August 9, 2024.](https://www.trendmicro.com/en_us/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
- [Brumaghin, E., Unterbrink, H. (2018, August 22). Picking Apart Remcos Botnet-In-A-Box. Retrieved November 6, 2018.](https://blog.talosintelligence.com/2018/08/picking-apart-remcos.html)
- [Check Point Research. (2025, March 10). Blind Eagle: …And Justice for All. Retrieved April 16, 2026.](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
- [Anomali Labs. (2019, March 15). Rocke Evolves Its Arsenal With a New Malware Family Written in Golang. Retrieved April 24, 2019.](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)
- [Jazi, Hossein. (2021, January 6). Retrohunting APT37: North Korean APT used VBA self decode technique to inject RokRat. Retrieved March 22, 2022.](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
- [Faou, M. and Boutin, J. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
- [Duncan, B., Harbison, M. (2019, January 23). Russian Language Malspam Pushing Redaman Banking Malware. Retrieved June 16, 2020.](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
- [Awasthi, P. (2026, January 8). Reborn in Rust: Muddy Water Evolves Tooling with RustyWater Implant. Retrieved March 19, 2026.](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Ward, S.. (2014, October 14). iSIGHT discovers zero-day vulnerability CVE-2014-4114 used in Russian cyber-espionage campaign. Retrieved November 17, 2024.](https://web.archive.org/web/20160503234007/https:/www.isightpartners.com/2014/10/cve-2014-4114/)
- [Symantec Threat Hunter Team. (2023, July 18). FIN8 Uses Revamped Sardonic Backdoor to Deliver Noberus Ransomware. Retrieved August 9, 2023.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)
- [Schwarz, D. et al. (2019, October 16). TA505 Distributes New SDBbot Remote Access Trojan with Get2 Downloader. Retrieved May 29, 2020.](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
- [GReAT. (2017, August 15). ShadowPad in corporate networks. Retrieved March 22, 2021.](https://securelist.com/shadowpad-in-corporate-networks/81432/)
- [Charlie Eriksen. (2025, September 16). S1ngularity/nx attackers strike again. Retrieved April 9, 2026.](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
- [Gianpietro Cutolo. (2025, November 26). Shai-Hulud 2.0: Aggressive, Automated, and Fast Spreading. Retrieved April 9, 2026.](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
- [Merav Bar, Rami McCarthy, Barak Sharoni. (2025, September 16). Shai-Hulud: Ongoing Package Supply Chain Worm Delivering Data-Stealing Malware. Retrieved April 9, 2026.](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)
- [Socket Research Team. (2025, September 15). Popular Tinycolor npm Package Compromised in Supply Chain Attack Affecting 40+ Packages. Retrieved April 9, 2026.](https://socket.dev/blog/tinycolor-supply-chain-attack-affects-40-packages)
- [Socket Research Team. (2025, November 24). Shai Hulud Strikes Again (v2). Retrieved April 9, 2026.](https://socket.dev/blog/shai-hulud-strikes-again-v2)
- [Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Eng, E., Caselden, D.. (2015, June 23). Operation Clandestine Wolf – Adobe Flash Zero-Day in APT3 Phishing Campaign. Retrieved January 14, 2016.](https://www.fireeye.com/blog/threat-research/2015/06/operation-clandestine-wolf-adobe-flash-zero-day.html)
- [Falcone, R. and Wartell, R.. (2015, July 27). Observations on CVE-2015-3113, Prior Zero-Days and the Pirpi Payload. Retrieved January 22, 2016.](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
- [Prizmant, D. (2021, June 7). Siloscape: First Known Malware Targeting Windows Containers to Compromise Cloud Environments. Retrieved June 9, 2021.](https://unit42.paloaltonetworks.com/siloscape/)
- [Microsoft Security Experts. (2022, August 24). Looking for the ‘Sliver’ lining: Hunting for emerging command-and-control frameworks. Retrieved March 24, 2025.](https://www.microsoft.com/en-us/security/blog/2022/08/24/looking-for-the-sliver-lining-hunting-for-emerging-command-and-control-frameworks/)
- [Perez, D. et al. (2021, April 20). Check Your Pulse: Suspected APT Actors Leverage Authentication Bypass Techniques and Pulse Secure Zero-Day. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
- [NCSC GCHQ. (2022, January 27). Small Sieve Malware Analysis Report. Retrieved August 22, 2022.](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)
- [Lorber, N. (2021, May 7). Revealing the Snip3 Crypter, a Highly Evasive RAT Loader. Retrieved September 13, 2023.](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [McLellan, T. and Moore, J. et al. (2021, April 29). UNC2447 SOMBRAT and FIVEHANDS Ransomware: A Sophisticated Financial Threat. Retrieved June 2, 2021.](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [CISA. (2020, July 16). MAR-10296782-1.v1 – SOREFANG. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
- [Cylance SPEAR Team. (2017, February 9). Shell Crew Variants Continue to Fly Under Big AV’s Radar. Retrieved February 15, 2017.](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)
- [DCSO CyTec Blog. (2022, November 8). #ShortAndMalicious: StrelaStealer aims for mail credentials. Retrieved December 31, 2024.](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)
- [Golo Mühr, Joe Fasulo & Charlotte Hammond, IBM X-Force. (2024, November 12). Strela Stealer: Today’s invoice is tomorrow’s phish. Retrieved December 31, 2024.](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [CrowdStrike Intelligence Team. (2021, January 11). SUNSPOT: An Implant in the Build Process. Retrieved January 11, 2021.](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [Ivanov, A. et al. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
- [Bettencourt, J. (2018, May 7). Kaspersky Lab finds new variant of SynAck ransomware using sophisticated Doppelgänging technique. Retrieved May 24, 2018.](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Check Point Research. (2020, December 22). SUNBURST, TEARDROP and the NetSec New Normal. Retrieved January 6, 2021.](https://research.checkpoint.com/2020/sunburst-teardrop-and-the-netsec-new-normal/)
- [MSTIC, CDOC, 365 Defender Research Team. (2021, January 20). Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop . Retrieved January 22, 2021.](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
- [Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
- [Secureworks. (2019, July 24). Updated Karagany Malware Targets Energy Sector. Retrieved August 12, 2020.](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
- [Salem, E. et al. (2020, May 28). VALAK: MORE THAN MEETS THE EYE . Retrieved June 19, 2020.](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
- [Duncan, B. (2020, July 24). Evolution of Valak, from Its Beginnings to Mass Distribution. Retrieved August 31, 2020.](https://unit42.paloaltonetworks.com/valak-evolution/)
- [Reaves, J. and Platt, J. (2020, June). Valak Malware and the Connection to Gozi Loader ConfCrew. Retrieved August 31, 2020.](https://assets.sentinelone.com/labs/sentinel-one-valak-i)
- [The BlackBerry Research & Intelligence Team. (2020, October). BAHAMUT: Hack-for-Hire Masters of Phishing, Fake News, and Fake Apps. Retrieved February 8, 2021.](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)
- [ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
- [Microsoft. (2015, June 9). Windows 10 to offer application developers new malware defenses. Retrieved February 12, 2018.](https://cloudblogs.microsoft.com/microsoftsecure/2015/06/09/windows-10-to-offer-application-developers-new-malware-defenses/?source=mmpc)
- [Microsoft. (2021, July 2). Use attack surface reduction rules to prevent malware infection. Retrieved June 24, 2021.](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)

---

# File and Directory Discovery

## Description

Adversaries may enumerate files and directories or may search in specific locations of a host or network share for certain information within a file system. Adversaries may use the information from File and Directory Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Many command shell utilities can be used to obtain this information. Examples include dir , tree , ls , find , and locate . [1] Custom tools may also be used to gather file and directory information and interact with the Native API . Adversaries may also leverage a Network Device CLI on network devices to gather file and directory information (e.g. dir , show flash , and/or nvram ). [2]

Some files and directories may require elevated or specific user permissions to access.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries obtained the contents of users’ directories using dir /s /b C:\Users command. [3] |
| S0066 | 3PARA RAT | 3PARA RAT has a command to retrieve metadata for files on disk as well as a command to list the current working directory. [4] |
| S0065 | 4H RAT | 4H RAT has the capability to obtain file and directory listings. [4] |
| S1167 | AcidPour | AcidPour can identify specific files and directories within the Linux operating system corresponding with storage devices for follow-on wiping activity, similar to AcidRain . [5] |
| S1125 | AcidRain | AcidRain identifies specific files and directories in the Linux operating system associated with storage devices. [6] |
| S1028 | Action RAT | Action RAT has the ability to collect drive and file information on an infected machine. [7] |
| G0018 | admin@338 | admin@338 actors used the following commands after exploiting a machine with LOWBALL malware to obtain information about files and directories: dir c:\ >> %temp%\download dir "c:\Documents and Settings" >> %temp%\download dir "c:\Program Files\" >> %temp%\download dir d:\ >> %temp%\download [8] |
| S0045 | ADVSTORESHELL | ADVSTORESHELL can list files and directories. [9] [10] |
| S1129 | Akira | Akira examines files prior to encryption to determine if they meet requirements for encryption and can be encrypted by the ransomware. These checks are performed through native Windows functions such as GetFileAttributesW . [11] [12] |
| S1194 | Akira _v2 | Akira _v2 can target specific files and folders for encryption. [13] [12] [14] |
| S1025 | Amadey | Amadey has searched for folders associated with antivirus software. [15] |
| S9027 | ANELLDR | ANELLDR can enumerate files in the current directory to search for encrypted payload files. [16] |
| C0062 | Anthropic AI-orchestrated Campaign | During the Anthropic AI-orchestrated Campaign , the adversary leveraged Claude Code to identify sensitive data within the victim environment for extraction. [17] |
| G1007 | Aoqin Dragon | Aoqin Dragon has run scripts to identify file formats including Microsoft Word. [18] |
| S0622 | AppleSeed | AppleSeed has the ability to search for .txt, .ppt, .hwp, .pdf, and .doc files in specified directories. [19] |
| G0026 | APT18 | APT18 can list files information for specific directories. [20] |
| G0007 | APT28 | APT28 has used Forfiles to locate PDF, Excel, and Word documents during collection. The group also searched a compromised DCCC computer for specific terms. [21] [22] |
| G0022 | APT3 | APT3 has a tool that looks for files and directories on the local file system. [23] [24] |
| G0050 | APT32 | APT32 's backdoor possesses the capability to list files and directories on a machine. [25] |
| G0082 | APT38 | APT38 have enumerated files and directories, or searched in specific locations within a compromised host. [26] |
| G0087 | APT39 | APT39 has used tools with the ability to search for files on a compromised host. [27] |
| G0096 | APT41 | APT41 has executed file /bin/pwd on exploited victims, perhaps to return architecture related information. [28] |
| G1023 | APT5 | APT5 has used the BLOODMINE utility to discover files with .css, .jpg, .png, .gif, .ico, .js, and .jsp extensions in Pulse Secure Connect logs. [29] |
| S0456 | Aria-body | Aria-body has the ability to gather metadata from a file and to search for file and directory names. [30] |
| S9031 | AshTag | The AshTag AshenOrchestrator component can enumerate files on victim hosts. [31] |
| S0438 | Attor | Attor has a plugin that enumerates files with specific extensions on all hard disk drives and stores file information in encrypted log files. [32] |
| S0347 | AuditCred | AuditCred can search through folders and files on the system. [33] |
| S0129 | AutoIt backdoor | AutoIt backdoor is capable of identifying documents on the victim with the following extensions: .doc; .pdf, .csv, .ppt, .docx, .pst, .xls, .xlsx, .pptx, and .jpeg. [34] |
| S0640 | Avaddon | Avaddon has searched for specific files prior to encryption. [35] |
| S0473 | Avenger | Avenger has the ability to browse files in directories such as Program Files and the Desktop. [36] |
| S1053 | AvosLocker | AvosLocker has searched for files and directories on a compromised network. [37] [38] |
| S0344 | Azorult | Azorult can recursively search for files in folders and collects files from the desktop with certain extensions. [39] |
| S0638 | Babuk | Babuk has the ability to enumerate files on a targeted system. [40] [41] |
| S0414 | BabyShark | BabyShark has used dir to search for "programfiles" and "appdata". [42] |
| S0475 | BackConfig | BackConfig has the ability to identify folders and files related to previous infections. [43] |
| S0093 | Backdoor.Oldrea | Backdoor.Oldrea collects information about available drives, default browser, desktop file list, My Documents, Internet history, program files, and root of available drives. It also searches for ICS-related software files. [44] |
| S0031 | BACKSPACE | BACKSPACE allows adversaries to search for files. [45] |
| S0642 | BADFLICK | BADFLICK has searched for files on the infected host. [46] |
| S0128 | BADNEWS | BADNEWS identifies files with certain extensions from USB devices, then copies them to a predefined directory. [47] |
| S0337 | BadPatch | BadPatch searches for files with specific file extensions. [48] |
| S0234 | Bandook | Bandook has a command to list files on a system. [49] |
| S0239 | Bankshot | Bankshot searches for files on the victim's machine. [50] |
| S0534 | Bazar | Bazar can enumerate the victim's desktop. [51] [52] |
| S0127 | BBSRAT | BBSRAT can list file and directory information. [53] |
| S1246 | BeaverTail | BeaverTail has searched for .ldb and .log files stored in browser extension directories for collection and exfiltration. [54] [55] [56] |
| S0268 | Bisonal | Bisonal can retrieve a file listing from the system. [57] [58] |
| S1070 | Black Basta | Black Basta can enumerate specific files for encryption. [59] [60] [61] [62] [63] [64] [65] [66] |
| S1068 | BlackCat | BlackCat can enumerate files for encryption. [67] |
| S0069 | BLACKCOFFEE | BLACKCOFFEE has the capability to enumerate files. [68] |
| S0089 | BlackEnergy | BlackEnergy gathers a list of installed apps from the uninstall program Registry. It also gathers registered mail, browser, and instant messaging clients from the Registry. BlackEnergy has searched for given file types. [69] [70] |
| S0564 | BlackMould | BlackMould has the ability to find files on the targeted system. [71] |
| S0520 | BLINDINGCAN | BLINDINGCAN can search, read, write, move, and execute files. [72] [73] |
| S0657 | BLUELIGHT | BLUELIGHT can enumerate files and collect associated metadata. [74] |
| S1184 | BOLDMOVE | BOLDMOVE can list information of all files in the system recursively from the root directory or from a specified directory. [75] |
| S0635 | BoomBox | BoomBox can search for specific files and directories on a machine. [76] |
| S0651 | BoxCaon | BoxCaon has searched for files on the system, such as documents located in the desktop folder. [77] |
| S0252 | Brave Prince | Brave Prince gathers file and directory information from the victim’s machine. [78] |
| S9015 | BRICKSTORM | BRICKSTORM has identified specific files and directories within targeted hosts and systems for modification, execution, collection and exfiltration. [79] [80] [81] [82] [83] [84] |
| G0060 | BRONZE BUTLER | BRONZE BUTLER has collected a list of files from the victim and uploaded it to its C2 server, and then created a new list of specific files to steal. [85] |
| C0015 | C0015 | During C0015 , the threat actors conducted a file listing discovery against multiple hosts to ensure locker encryption was successful. [86] |
| S0693 | CaddyWiper | CaddyWiper can enumerate all files and directories on a compromised host. [87] |
| S0351 | Cannon | Cannon can obtain victim drive information as well as a list of folders in C:\Program Files. [88] |
| S0348 | Cardinal RAT | Cardinal RAT checks its current working directory upon execution and also contains watchdog functionality that ensures its executable is located in the correct path (else it will rewrite the payload). [89] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell can search for files in directories. [90] |
| S1043 | ccf32 | ccf32 can parse collected files to identify specific file extensions. [91] |
| S0674 | CharmPower | CharmPower can enumerate drives and list the contents of the C: drive on a victim's computer. [92] |
| S0144 | ChChes | ChChes collects the victim's %TEMP% directory path and version of Internet Explorer. [93] |
| S1096 | Cheerscrypt | Cheerscrypt can search for log and VMware-related files with .log, .vmdk, .vmem, .vswp, and .vmsn extensions. [94] |
| G0114 | Chimera | Chimera has utilized multiple commands to identify data of interest in file and directory listings. [95] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP has the ability to enumerate directories for files that match a set list. [96] |
| S0020 | China Chopper | China Chopper 's server component can list directory contents. [97] [98] |
| S0023 | CHOPSTICK | An older version of CHOPSTICK has a module that monitors all mounted volumes for files with the extensions .doc, .docx, .pgp, .gpg, .m2f, or .m2o. [9] |
| S0660 | Clambling | Clambling can browse directories on a compromised host. [99] [100] |
| S0611 | Clop | Clop has searched folders and subfolders for files to encrypt. [101] |
| S0106 | cmd | cmd can be used to find files and directories with native functionality such as dir commands. [102] |
| S1105 | COATHANGER | COATHANGER will survey the contents of system files during installation. [103] |
| S0154 | Cobalt Strike | Cobalt Strike can explore files on a compromised system. [104] |
| G0142 | Confucius | Confucius has used a file stealer that checks the Document, Downloads, Desktop, and Picture folders for documents and images with specific extensions. [105] |
| G1052 | Contagious Interview | Contagious Interview has conducted key word searches within files and directories on a compromised hosts to identify files for exfiltration. [56] [106] |
| S0575 | Conti | Conti can discover files on a local system. [107] |
| S0492 | CookieMiner | CookieMiner has looked for files in the user's home directory with "wallet" in their name using find . [108] |
| S0212 | CORALDECK | CORALDECK searches for specified files. [109] |
| S0050 | CosmicDuke | CosmicDuke searches attached and mounted drives for file extensions and keywords that match a predefined list. [110] |
| S0488 | CrackMapExec | CrackMapExec can discover specified filetypes and log files on a targeted system. [111] |
| S1023 | CreepyDrive | CreepyDrive can specify the local file path to upload files from. [112] |
| S0115 | Crimson | Crimson contains commands to list files and directories, as well as search for files matching certain extensions from a defined list. [113] [114] [115] |
| S0235 | CrossRAT | CrossRAT can list all files on a system. [116] |
| S0498 | Cryptoistic | Cryptoistic can scan a directory to identify files for deletion. [117] |
| S0625 | Cuba | Cuba can enumerate files by using a variety of functions. [118] |
| S1153 | Cuckoo Stealer | Cuckoo Stealer can search for files associated with specific applications. [119] [120] |
| S0687 | Cyclops Blink | Cyclops Blink can use the Linux API statvfs to enumerate the current working directory. [121] [122] |
| S0497 | Dacls | Dacls can scan directories on a compromised host. [123] |
| G0070 | Dark Caracal | Dark Caracal collected file listings of all default Windows directories. [116] |
| S1111 | DarkGate | Some versions of DarkGate search for the hard-coded folder C:\Program Files\e Carte Bleue . [124] |
| G0012 | Darkhotel | Darkhotel has used malware that searched for files with specific patterns. [125] |
| S0673 | DarkWatchman | DarkWatchman has the ability to enumerate file and folder names. [126] |
| S0255 | DDKONG | DDKONG lists files on the victim’s machine. [127] |
| S0616 | DEATHRANSOM | DEATHRANSOM can use loop operations to enumerate directories on a compromised host. [128] |
| S0354 | Denis | Denis has several commands to search directories for files. [129] [130] |
| S0021 | Derusbi | Derusbi is capable of obtaining directory, file, and drive listings. [131] [97] |
| S0659 | Diavol | Diavol has a command to traverse the files and directories in a given path. [132] |
| S9002 | Diskpart | If executed with elevated privileges, Diskpart can list all volumes, including virtual disks. [133] |
| S0600 | Doki | Doki has resolved the path of a process PID to use as a script argument. [134] |
| S0472 | down_new | down_new has the ability to list the directories on a compromised host. [36] |
| G0035 | Dragonfly | Dragonfly has used a batch script to gather folder and file names from victim hosts. [135] [136] [137] |
| S0547 | DropBook | DropBook can collect the names of all files and folders in the Program Files directories. [138] [139] |
| S0567 | Dtrack | Dtrack can list files on available disk volumes. [140] [141] |
| S1159 | DUSTTRAP | DUSTTRAP can enumerate files and directories. [142] |
| S0062 | DustySky | DustySky scans the victim for files that contain certain keywords and document types including PDF, DOC, DOCX, XLS, and XLSX, from a list that is obtained from the C2 as a text file. It can also identify logical drives for the infected machine. [143] [144] |
| S9038 | DynoWiper | DynoWiper has used the Microsoft Windows native FindFirstFile() and FindNextFile() to recursively enumerate directories and files on the system. [3] |
| S0081 | Elise | A variant of Elise executes dir C:\progra~1 when initially run. [145] [146] |
| S0064 | ELMER | ELMER is capable of performing directory listings. [147] |
| S1247 | Embargo | Embargo has searched for folders, subfolders and other networked or mounted drives for follow on encryption actions. [148] Embargo has also iterated device volumes using FindFirstVolumeW() and FindNextVolumeW() functions and then calls the GetVolumePathNamesForVolumeNameW() function to retrieve a list of drive letters and mounted folder paths for each specified volume. [148] |
| S0363 | Empire | Empire includes various modules for finding files of interest on hosts and network shares. [149] |
| S0091 | Epic | Epic recursively searches for all .doc files on the system and collects a directory listing of the Desktop, %TEMP%, and %WINDOWS%\Temp directories. [150] [151] |
| S1179 | Exbyte | Exbyte enumerates all document files on an infected machine, then creates a summary of these items including filename and directory location prior to exfiltration to cloud hosting services. [152] |
| S0181 | FALLCHILL | FALLCHILL can search files on a victim. [153] |
| S0512 | FatDuke | FatDuke can enumerate directories on target machines. [154] |
| G1016 | FIN13 | FIN13 has used the Windows dir command to enumerate files and directories in a victim's network. [155] |
| S0182 | FinFisher | FinFisher enumerates directories and scans for certain files. [156] [157] |
| S0618 | FIVEHANDS | FIVEHANDS has the ability to enumerate files on a compromised host in order to encrypt files with specific extensions. [158] [159] |
| S0036 | FLASHFLOOD | FLASHFLOOD searches for interesting files (either a default or customized set of file extensions) on the local system and removable media. [45] |
| S0661 | FoggyWeb | FoggyWeb 's loader can check for the FoggyWeb backdoor .pri file on a compromised AD FS server. [160] |
| S0193 | Forfiles | Forfiles can be used to locate certain types of files/directories in a system.(ex: locate all files with a specific extension, name, and/or age) [21] |
| G0117 | Fox Kitten | Fox Kitten has used WizTree to obtain network files and directory listings. [161] |
| S0277 | FruitFly | FruitFly looks for specific files and file types. [162] |
| S1044 | FunnyDream | FunnyDream can identify files with .doc, .docx, .ppt, .pptx, .xls, .xlsx, and .pdf extensions and specific timestamps for collection. [91] |
| S0628 | FYAnti | FYAnti can search the C:\Windows\Microsoft.NET\ directory for files of a specified size. [163] |
| S0410 | Fysbis | Fysbis has the ability to search for files. [164] |
| G0047 | Gamaredon Group | Gamaredon Group macros can scan for Microsoft Word and Excel files to inject with additional malicious macros. Gamaredon Group has also used its backdoors to automatically list interesting files (such as Office documents) found on a system. [165] [166] [167] Gamaredon Group has also identified directory trees, folders and files on the compromised host. [168] |
| S0666 | Gelsemium | Gelsemium can retrieve data from specific Windows directories, as well as open random files as part of Virtualization/Sandbox Evasion . [169] |
| S0049 | GeminiDuke | GeminiDuke collects information from the victim, including installed drivers, programs previously executed by users, programs and services configured to automatically run at startup, files and folders present in any user's home folder, files and folders present in any user's My Documents, programs installed to the Program Files folder, and recently accessed files, folders, and programs. [170] |
| S0249 | Gold Dragon | Gold Dragon lists the directories for Desktop, program files, and the user’s recently accessed files. [78] |
| S0493 | GoldenSpy | GoldenSpy has included a program "ExeProtector", which monitors for the existence of GoldenSpy on the infected system and redownloads if necessary. [171] |
| S1198 | Gomir | Gomir collects information about directory and file structures, including total number of subdirectories, total number of files, and total size of files on infected systems. [172] |
| S0237 | GravityRAT | GravityRAT collects the volumes mapped on the system, and also steals files with the following extensions: .docx, .doc, .pptx, .ppt, .xlsx, .xls, .rtf, and .pdf. [173] |
| S0632 | GrimAgent | GrimAgent has the ability to enumerate files and directories on a compromised host. [174] |
| G0125 | HAFNIUM | HAFNIUM has searched file contents on a compromised host. [98] |
| S1229 | Havoc | The Havoc interface can display a file explorer view of the compromised host. [175] |
| S0697 | HermeticWiper | HermeticWiper can enumerate common folders such as My Documents, Desktop, and AppData. [176] [177] |
| S1027 | Heyoka Backdoor | Heyoka Backdoor has the ability to search the compromised host for files. [18] |
| S0376 | HOPLIGHT | HOPLIGHT has been observed enumerating system drives and partitions. [178] |
| S0431 | HotCroissant | HotCroissant has the ability to retrieve a list of files in a given directory as well as drives and drive types. [179] |
| S0070 | HTTPBrowser | HTTPBrowser is capable of listing files, folders, and drives on a victim. [180] [181] |
| S0203 | Hydraq | Hydraq creates a backdoor through which remote attackers can check for the existence of files, including its own components, as well as retrieve a list of logical drives. [182] [183] |
| S1022 | IceApple | The IceApple Directory Lister module can list information about files and directories including creation time, last write time, name, and size. [184] |
| S0434 | Imminent Monitor | Imminent Monitor has a dynamic debugging feature to check whether it is located in the %TEMP% directory, otherwise it copies itself there. [185] |
| S1139 | INC Ransomware | INC Ransomware can receive command line arguments to encrypt specific files and directories. [186] [187] |
| G0100 | Inception | Inception used a file listing plugin to collect information about file and directories both on local and remote drives. [188] |
| S0604 | Industroyer | Industroyer ’s data wiper component enumerates specific files on all the Windows drives. [189] |
| S0259 | InnaputRAT | InnaputRAT enumerates directories and obtains file attributes on a system. [190] |
| S1245 | InvisibleFerret | InvisibleFerret has identified specific directories and files for exfiltration using the ssh_upload command which contains subcommands of .sdira , sdir , sfile , sfinda , sfindr , sfind . [56] [191] InvisibleFerret also has the capability to scan and upload files of interest from multiple OS systems through the use of scripts that check file names, file extensions, and avoids certain path names. [192] [106] InvisibleFerret has utilized the findstr on Windows or the macOS find commands to search for files of interest. [193] |
| S0260 | InvisiMole | InvisiMole can list information about files in a directory and recently opened or used documents. InvisiMole can also search for specific files by supplied file mask. [194] |
| S0015 | Ixeshe | Ixeshe can list file and directory information. [195] |
| S0201 | JPIN | JPIN can enumerate drives and their types. It can also change file permissions using cacls.exe. [196] |
| S0283 | jRAT | jRAT can browse file systems. [197] [198] |
| S0088 | Kasidet | Kasidet has the ability to search for a given filename on a victim. [199] |
| S0265 | Kazuar | Kazuar finds a specified directory, lists the files and metadata about those files. [200] |
| G0004 | Ke3chang | Ke3chang uses command-line interaction to search files and directories. [201] [202] |
| S0387 | KeyBoy | KeyBoy has a command to launch a file browser or explorer on the system. [203] |
| S0271 | KEYMARBLE | KEYMARBLE has a command to search for files on the victim’s machine. [204] |
| S0526 | KGH_SPY | KGH_SPY can enumerate files and directories on a compromised host. [205] |
| S0607 | KillDisk | KillDisk has used the FindNextFile command as part of its file deletion process. [206] |
| G0094 | Kimsuky | Kimsuky has the ability to enumerate all files and directories on an infected system. [207] [208] [209] Kimsuky has used a custom script with a function called CreateFileList() that can scan all filesystem drives, prioritizing C:\Users, to locate files and file extensions of interest that ultimately generates a file called FileList.txt saved within the victims %TEMP% Directory that contains the findings and the respective pathways. [210] |
| S0599 | Kinsing | Kinsing has used the find command to search for specific files. [211] |
| S0437 | Kivars | Kivars has the ability to list drives on the infected host. [212] |
| S0250 | Koadic | Koadic can obtain a list of directories. [213] |
| S0356 | KONNI | A version of KONNI searches for filenames created with a previous version of the malware, suggesting different versions targeted the same victims and the versions may work together. [214] |
| C0035 | KV Botnet Activity | KV Botnet Activity gathers a list of filenames from the following locations during execution of the final botnet stage: \/usr\/sbin\/ , \/usr\/bin\/ , \/sbin\/ , \/pfrm2.0\/bin\/ , \/usr\/local\/bin\/ . [215] |
| S0236 | Kwampirs | Kwampirs collects a list of files and directories in C:\ with the command dir /s /a c:\ >> "C:\windows\TEMP[RANDOM].tmp" . [216] |
| S9035 | LAMEHUG | LAMEHUG can target directories on victim machines for file collection. [217] [218] |
| S1160 | Latrodectus | Latrodectus can collect desktop filenames. [219] [220] [221] |
| G0032 | Lazarus Group | Lazarus Group malware can use a common function to identify target files by their extension, and some also enumerate files and directories, including a Destover-like variant that lists files and gathers information for all drives. [222] [223] [224] [225] |
| S9039 | LazyWiper | LazyWiper can specifically target multiple files by extension including: .rar, .tar.gz, .zip, .7z, .json, .bcp, .bak, .gho, .erf, .edb, .onepkg, .pst, and .ldiff. [3] |
| G0077 | Leafminer | Leafminer used a tool called MailSniper to search for files on the desktop and another utility called Sobolsoft to extract attachments from EML files. [226] |
| S1185 | LightSpy | LightSpy uses the NSFileManager to move, create and delete files. LightSpy can also use the assembly bt instruction to determine a file's executable permissions. [227] |
| S0211 | Linfo | Linfo creates a backdoor through which remote attackers can list contents of drives and search for files. [228] |
| S1121 | LITTLELAMB.WOOLTEA | LITTLELAMB.WOOLTEA can monitor for system upgrade events by checking for the presence of /tmp/data/root/dev . [229] |
| S1199 | LockBit 2.0 | LockBit 2.0 can exclude files associated with core system functions from encryption. [230] |
| S1202 | LockBit 3.0 | LockBit 3.0 can exclude files associated with core system functions from encryption. [231] |
| S9020 | LODEINFO | LODEINFO has the ability to designate specific files and folders to encryption. [232] [233] |
| S1101 | LoFiSe | LoFiSe can monitor the file system to identify files less than 6.4 MB in size with file extensions including .doc, .docx, .xls, .xlsx, .ppt, .pptx, .pdf, .rtf, .tif, .odt, .ods, .odp, .eml, and .msg. [234] |
| S0447 | Lokibot | Lokibot can search for specific files on an infected host. [235] |
| S0582 | LookBack | LookBack can retrieve file listings from the victim machine. [236] |
| G0030 | Lotus Blossom | Lotus Blossom has used commands such as dir to examine the local filesystem of victim machines. [237] |
| G1014 | LuminousMoth | LuminousMoth has used malware that scans for files in the Documents, Desktop, and Download folders and in other drives. [238] [239] |
| S1142 | LunarMail | LunarMail can search its staging directory for output files it has produced. [240] |
| S1141 | LunarWeb | LunarWeb has the ability to retrieve directory listings. [240] |
| S0409 | Machete | Machete produces file listings in order to search for files to be exfiltrated. [241] [242] [243] |
| S1016 | MacMa | MacMa can search for a specific file on the compromised computer and can enumerate files in Desktop, Downloads, and Documents folders. [244] |
| S1060 | Mafalda | Mafalda can search for files and directories. [245] |
| G0059 | Magic Hound | Magic Hound malware can list a victim's logical drives and the type, as well the total/free space of the fixed devices. Other malware can list a directory's contents. [246] |
| S1169 | Mango | Mango can enumerate the contents of current working or other specified directories. [247] |
| S1156 | Manjusaka | Manjusaka can gather information about specific files on the victim system. [248] |
| S0652 | MarkiRAT | MarkiRAT can look for files carrying specific extensions such as: .rtf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .pps, .ppsx, .txt, .gpg, .pkr, .kdbx, .key, and .jpb. [249] |
| G1051 | Medusa Group | Medusa Group has searched for files within the victim environment for encryption and exfiltration. [250] [251] [252] Medusa Group has also identified files associated with remote management services. [250] [251] |
| S1244 | Medusa Ransomware | Medusa Ransomware has searched for files within the victim environment for encryption and exfiltration. [250] [251] [252] Medusa Ransomware has also identified files associated with remote management services. [250] [251] |
| S0576 | MegaCortex | MegaCortex can parse the available drives and directories to determine which files to encrypt. [253] |
| S1191 | Megazord | Megazord can ignore specified directories for encryption. [14] |
| G0045 | menuPass | menuPass has searched compromised systems for folders of interest including those related to HR, audit and expense, and meeting memos. [254] |
| S0443 | MESSAGETAP | MESSAGETAP checks for the existence of two configuration files (keyword_parm.txt and parm.txt) and attempts to read the files every 30 seconds. [255] |
| S1059 | metaMain | metaMain can recursively enumerate files in an operator-provided directory. [245] [256] |
| S0455 | Metamorfo | Metamorfo has searched the Program Files directories for specific folders and has searched for strings related to its mutexes. [257] [258] [259] |
| S0339 | Micropsia | Micropsia can perform a recursive directory listing for all volume drives available on the victim's machine and can also fetch specific files by their paths. [260] |
| S0051 | MiniDuke | MiniDuke can enumerate local drives. [154] |
| G1054 | MirrorFace | MirrorFace has run commands to check the content of folders on compromised hosts and has specifically targeted files with .doc, .ppt, .xls, .jtd, .eml, .xps, and .pdf extensions. [232] [261] [262] |
| S0083 | Misdat | Misdat is capable of running commands to obtain a list of files and directories, as well as enumerating logical drives. [263] |
| S1122 | Mispadu | Mispadu searches for various filesystem paths to determine what banking applications are installed on the victim’s machine. [264] |
| S0079 | MobileOrder | MobileOrder has a command to upload to its C2 server information about files on the victim mobile device, including SD card size, installed app list, SMS content, contacts, and calling history. [265] |
| S0149 | MoonWind | MoonWind has a command to return a directory listing for a specified directory. [266] |
| G0069 | MuddyWater | MuddyWater has used malware that checked if the ProgramData folder had folders or files with the keywords "Kasper," "Panda," or "ESET." [267] |
| S1135 | MultiLayer Wiper | MultiLayer Wiper generates a list of all files and paths on the fixed drives of an infected system, enumerating all files on the system except specific folders defined in a hardcoded list. [268] |
| G0129 | Mustang Panda | Mustang Panda has searched the entire target system for DOC, DOCX, PPT, PPTX, XLS, XLSX, and PDF files. [269] [270] |
| S0272 | NDiskMonitor | NDiskMonitor can obtain a list of all files and directories as well as logical drives. [47] |
| S0630 | Nebulae | Nebulae can list files and directories on a compromised host. [271] |
| S0034 | NETEAGLE | NETEAGLE allows adversaries to enumerate and modify the infected host's file system. It supports searching for directories, creating directories, listing directory contents, reading and writing to files, retrieving file attributes, and retrieving volume information. [45] |
| S0198 | NETWIRE | NETWIRE has the ability to search for files on the compromised host. [272] |
| C0002 | Night Dragon | During Night Dragon , threat actors used zwShell to establish full remote control of the connected machine and browse the victim file system. [273] |
| S1090 | NightClub | NightClub can use a file monitor to identify .lnk, .doc, .docx, .xls, .xslx, and .pdf files. [274] |
| S1100 | Ninja | Ninja has the ability to enumerate directory content. [275] [234] |
| S0385 | njRAT | njRAT can browse file systems using a file manager module. [276] |
| S0368 | NotPetya | NotPetya searches for files ending with dozens of different file extensions prior to encryption. [277] |
| S0644 | ObliqueRAT | ObliqueRAT has the ability to recursively enumerate files on an infected endpoint. [278] |
| S0346 | OceanSalt | OceanSalt can extract drive information from the endpoint and search files on the system. [279] |
| S0340 | Octopus | Octopus can collect information on the Windows directory and searches for compressed RAR files on the host. [280] [281] [282] |
| S1170 | ODAgent | ODAgent can identify the current working directory. [283] |
| S0439 | Okrum | Okrum has used DriveLetterView to enumerate drive information. [284] |
| C0060 | Operation AkaiRyū | During Operation AkaiRyū , MirrorFace enumerated file system details in compromised environments. [16] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors used dir c:\\ to search for files. [285] |
| C0022 | Operation Dream Job | During Operation Dream Job , Lazarus Group conducted word searches within documents on a compromised host in search of security and financial matters. [286] |
| C0006 | Operation Honeybee | During Operation Honeybee , the threat actors used a malicious DLL to search for files with specific keywords. [287] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors gathered a recursive directory listing to find files and directories of interest. [288] |
| S0229 | Orz | Orz can gather victim drive information. [289] |
| S0402 | OSX/Shlayer | OSX/Shlayer has used the command appDir="$(dirname $(dirname "$currentDir"))" and $(dirname "$(pwd -P)") to construct installation paths. [290] [291] |
| S1017 | OutSteel | OutSteel can search for specific file extensions, including zipped files. [292] |
| S0072 | OwaAuth | OwaAuth has a command to list its directory and logical drives. [180] |
| S0598 | P.A.S. Webshell | P.A.S. Webshell has the ability to list files and file characteristics including extension, size, ownership, and permissions. [293] |
| S1109 | PACEMAKER | PACEMAKER can parse /proc/"process_name"/cmdline to look for the string dswsd within the command line. [294] |
| S0208 | Pasam | Pasam creates a backdoor through which remote attackers can retrieve lists of files. [295] |
| G0040 | Patchwork | A Patchwork payload has searched all fixed drives on the victim for files matching a specified list of extensions. [296] [47] |
| S1102 | Pcexter | Pcexter has the ability to search for files in specified directories. [234] |
| S0587 | Penquin | Penquin can use the command code do_vslist to send file names, size, and status to C2. [297] |
| S0643 | Peppy | Peppy can identify specific files for exfiltration. [113] |
| S0048 | PinchDuke | PinchDuke searches for files created within a certain timeframe and whose file extension matches a predefined list. [170] |
| S1031 | PingPull | PingPull can enumerate storage volumes and folder contents of a compromised host. [298] |
| S0124 | Pisloader | Pisloader has commands to list drives on the victim machine and to list file information for a given directory. [299] |
| G1040 | Play | Play has used the Grixba information stealer to list security files and processes. [300] |
| S1162 | Playcrypt | Playcrypt can avoid encrypting files with a .PLAY, .exe, .msi, .dll, .lnk, or .sys file extension. [300] |
| S0435 | PLEAD | PLEAD has the ability to list drives and files on the compromised host. [212] [301] |
| S0013 | PlugX | PlugX has a module to enumerate drives and find files recursively. [302] [303] [304] [305] PlugX has also checked the path from which it is running for specific parameters prior to execution. [302] [306] [307] |
| S0428 | PoetRAT | PoetRAT has the ability to list files upon receiving the ls command from C2. [308] |
| S0216 | POORAIM | POORAIM can conduct file browsing. [109] |
| S0378 | PoshC2 | PoshC2 can enumerate files on the local file system and includes a module for enumerating recently accessed files. [309] |
| S0139 | PowerDuke | PowerDuke has commands to get the current directory name as well as the size of a file. It also has commands to obtain information about logical drives, drive type, and free space. [310] |
| S0184 | POWRUNER | POWRUNER may enumerate user directories on a victim. [311] |
| S1058 | Prestige | Prestige can traverse the file system to discover files to encrypt by identifying specific extensions defined in a hardcoded list. [312] |
| S0113 | Prikormka | A module in Prikormka collects information about the paths, size, and creation time of files with specific file extensions, but not the actual content of the file. [313] |
| S0238 | Proxysvc | Proxysvc lists files in directories. [223] |
| S0078 | Psylo | Psylo has commands to enumerate all storage devices and to find all files that start with a particular string. [265] |
| S0147 | Pteranodon | Pteranodon identifies files matching certain file extension and copies them to subdirectories it created. [314] |
| S0192 | Pupy | Pupy can walk through directories and recursively search for strings in files. [315] |
| S0650 | QakBot | QakBot can identify whether it has been run previously on a host by checking for a specified folder. [316] |
| S1242 | Qilin | Qilin can exclude specific directories and files from encryption. [317] [318] |
| S0686 | QuietSieve | QuietSieve can search files on the target host by extension, including doc, docx, xls, rtf, odt, txt, jpg, pdf, rar, zip, and 7z. [319] |
| S1148 | Raccoon Stealer | Raccoon Stealer identifies target files and directories for collection based on a configuration file. [320] [321] |
| S0629 | RainyDay | RainyDay can use a file exfiltration tool to collect recently changed files with specific extensions. [271] |
| S0458 | Ramsay | Ramsay can collect directory and file lists. [322] [323] |
| S1212 | RansomHub | RansomHub has the ability to only encrypt specific files. [324] |
| S0055 | RARSTONE | RARSTONE obtains installer properties from Uninstall Registry Key entries to obtain information about installed applications and how to uninstall certain applications. [325] |
| S1130 | Raspberry Robin | Raspberry Robin will check to see if the initial executing script is located on the user's Desktop as an anti-analysis check. [326] |
| S1040 | Rclone | Rclone can list files and directories with the ls , lsd , and lsl commands. [327] |
| G1039 | RedCurl | RedCurl has searched for and collected files on local and network drives. [328] [329] [330] |
| S0153 | RedLeaves | RedLeaves can enumerate and search for files and directories. [331] [93] |
| S0332 | Remcos | Remcos can search for files on the infected machine. [332] [333] |
| S0375 | Remexi | Remexi searches for files on the system. [334] |
| S0592 | RemoteUtilities | RemoteUtilities can enumerate files and directories on a target machine. [335] |
| S0125 | Remsec | Remsec is capable of listing contents of folders on the victim. Remsec also searches for custom network encryption software on victims. [336] [337] [338] |
| S0496 | REvil | REvil has the ability to identify specific files and directories that are not to be encrypted. [339] [340] [341] [342] [343] [344] |
| S0448 | Rising Sun | Rising Sun can enumerate information about files from the infected system, including file size, attributes, creation time, last access time, and write time. Rising Sun can enumerate the compilation timestamp of Windows executable files. [345] |
| S1150 | ROADSWEEP | ROADSWEEP can enumerate files on infected devices and avoid encrypting files with .exe, .dll, .sys, .lnk, or . lck extensions. [96] [346] [347] |
| S0240 | ROKRAT | ROKRAT has the ability to gather a list of files and directories on the infected system. [348] [349] [350] |
| S0090 | Rover | Rover automatically searches for files on local drives based on a predefined list of file extensions. [351] |
| S1073 | Royal | Royal can identify specific files and directories to exclude from the encryption process. [352] [353] [354] |
| S0148 | RTM | RTM can check for specific files and directories associated with virtualization and malware analysis. [355] |
| S0446 | Ryuk | Ryuk has enumerated files and folders on all mounted drives. [356] |
| S1018 | Saint Bot | Saint Bot can search a compromised host for specific files. [292] |
| C0059 | Salesforce Data Exfiltration | During Salesforce Data Exfiltration , threat actors queried customers' Salesforce environments to identify sensitive information for exfiltration. [357] |
| S9030 | SameCoin | SameCoin can list all system files and can avoid wiping specific directories such as Program Files, Windows, and Users. [358] |
| S1099 | Samurai | Samurai can use a specific module for file enumeration. [275] |
| G0034 | Sandworm Team | Sandworm Team has enumerated files on a compromised host. [277] [359] |
| G1015 | Scattered Spider | Scattered Spider Spider enumerates a target organization for files and directories of interest, including source code, user provisioning, MFA device registration, network diagrams, and shared credentials in documents or spreadsheets. [360] [361] [362] [363] [364] |
| S0461 | SDBbot | SDBbot has the ability to get directory listings or drive information on a compromised host. [365] |
| S0345 | Seasalt | Seasalt has the capability to identify the drive type on a victim. [279] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors leveraged commands to locate accessible file shares, backup paths, or SharePoint content. [366] |
| S1089 | SharpDisco | SharpDisco can identify recently opened files by using an LNK format parser to extract the original file path from LNK files found in either %USERPROFILE%\Recent (Windows XP) or %APPDATA%\Microsoft\Windows\Recent (newer Windows versions) . [274] |
| S0444 | ShimRat | ShimRat can list directories. [367] |
| S0063 | SHOTPUT | SHOTPUT has a command to obtain a directory listing. [368] |
| S0610 | SideTwist | SideTwist has the ability to search for specific files. [369] |
| G0121 | Sidewinder | Sidewinder has used malware to collect information on files and directories. [370] |
| S0692 | SILENTTRINITY | SILENTTRINITY has several modules, such as ls.py , pwd.py , and recentFiles.py , to enumerate directories and files. [371] |
| S0623 | Siloscape | Siloscape searches for the Kubernetes config file and other related files using a regular expression. [372] |
| S0468 | Skidmap | Skidmap has checked for the existence of specific files including /usr/sbin/setenforce and /etc/selinux/config . It also has the ability to monitor the cryptocurrency miner file and process. [373] |
| S0633 | Sliver | Sliver can enumerate files on a target system. [374] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA can enumerate files and directories. [375] |
| S0226 | Smoke Loader | Smoke Loader recursively searches through directories for files. [376] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 obtained information about the configured Exchange virtual directory using Get-WebServicesVirtualDirectory . [377] |
| S0615 | SombRAT | SombRAT can execute enum to enumerate files in storage on a compromised system. [378] |
| S0516 | SoreFang | SoreFang has the ability to list directories. [379] |
| S0157 | SOUNDBITE | SOUNDBITE is capable of enumerating and manipulating files and directories. [380] |
| G0054 | Sowbug | Sowbug identified and extracted all Word documents on a server by using a command containing * .doc and *.docx. The actors also searched for documents based on a specific date range and attempted to identify all installed software on a victim. [381] |
| S0035 | SPACESHIP | SPACESHIP identifies files and directories for collection by searching for specific file extensions or file modification time. [45] |
| S1140 | Spica | Spica can list filesystem contents on targeted systems. [382] |
| S1234 | SplatCloak | SplatCloak has used Windows API to identify files associated with Windows Defender and Kaspersky. [383] |
| S1200 | StealBit | StealBit can be configured to exfiltrate specific file types. [230] [384] |
| S0142 | StreamEx | StreamEx has the ability to enumerate drive types. [385] |
| S1034 | StrifeWater | StrifeWater can enumerate files on a compromised host. [386] |
| S0491 | StrongPity | StrongPity can parse the hard drive on a compromised host to identify specific file extensions. [387] |
| S0603 | Stuxnet | Stuxnet uses a driver to scan for specific filesystem driver objects. [388] |
| S1042 | SUGARDUMP | SUGARDUMP can search for and collect data from specific Chrome, Opera, Microsoft Edge, and Firefox files, including any folders that have the string Profile in its name. [389] |
| S0559 | SUNBURST | SUNBURST had commands to enumerate files and directories. [390] [391] |
| S0562 | SUNSPOT | SUNSPOT enumerated the Orion software Visual Studio solution directory path. [392] |
| S0242 | SynAck | SynAck checks its directory location in an attempt to avoid launching in a sandbox. [393] [394] |
| S0663 | SysUpdate | SysUpdate can search files on a compromised host. [395] [396] |
| S0011 | Taidoor | Taidoor can search for specific files. [397] |
| S0586 | TAINTEDSCRIBE | TAINTEDSCRIBE can use DirectoryList to enumerate files in a specified directory. [398] |
| S0467 | TajMahal | TajMahal has the ability to index files from drives, user profiles, and removable drives. [399] |
| G0139 | TeamTNT | TeamTNT has used a script that checks /proc/*/environ for environment variables related to AWS. [400] |
| S0665 | ThreatNeedle | ThreatNeedle can obtain file and directory information. [401] |
| S0131 | TINYTYPHON | TINYTYPHON searches through the drive containing the OS, then all drive letters C through to Z, for documents matching certain extensions. [34] |
| G1022 | ToddyCat | ToddyCat has run scripts to enumerate recently modified documents having either a .pdf, .doc, .docx, .xls or .xlsx extension. [234] |
| S0266 | TrickBot | TrickBot searches the system for all of the following file extensions: .avi, .mov, .mkv, .mpeg, .mpeg4, .mp4, .mp3, .wav, .ogg, .jpeg, .jpg, .png, .bmp, .gif, .tiff, .ico, .xlsx, and .zip. It can also obtain browsing history, cookies, and plug-in information. [402] [403] |
| S0094 | Trojan.Karagany | Trojan.Karagany can enumerate files and directories on a compromised host. [404] |
| S1196 | Troll Stealer | Troll Stealer can enumerate and collect items from local drives and folders. [405] |
| G0081 | Tropic Trooper | Tropic Trooper has monitored files' modified time. [406] |
| S9009 | TruffleHog | TruffleHog has can browse and scan individual files and directories. [407] [408] [409] |
| S0436 | TSCookie | TSCookie has the ability to discover drive information on the infected host. [410] |
| S0647 | Turian | Turian can search for specific files and list directories. [411] |
| G0010 | Turla | Turla surveys a system upon check-in to discover files in specific locations on the hard disk %TEMP% directory, the current user's desktop, the Program Files directory, and Recent. [150] [412] Turla RPC backdoors have also searched for files matching the lPH*.dll pattern. [413] |
| S0263 | TYPEFRAME | TYPEFRAME can search directories for files on the victim’s machine. [414] |
| G1048 | UNC3886 | UNC3886 has used vmtoolsd.exe to enumerate files on guest machines. [415] [416] |
| S0275 | UPPERCUT | UPPERCUT has the capability to gather the victim's current directory. [417] |
| S0022 | Uroburos | Uroburos can search for specific files on a compromised system. [418] |
| S0452 | USBferry | USBferry can detect the victim's file or folder list. [406] |
| S0136 | USBStealer | USBStealer searches victim drives for files matching certain extensions (".skr",".pkr" or ".key") or names. [419] [420] |
| G1047 | Velvet Ant | Velvet Ant has enumerated local files and folders on victim devices. [421] |
| S0180 | Volgmer | Volgmer can list directories on a victim. [422] |
| G1017 | Volt Typhoon | Volt Typhoon has enumerated directories containing vulnerability testing and cyber related content and facilities data such as construction drawings. [423] |
| S0366 | WannaCry | WannaCry searches for variety of user files by file extension before encrypting them using RSA and AES, including Office, PDF, image, audio, video, source code, archive/compression format, and key and certificate files. [424] [425] |
| S0670 | WarzoneRAT | WarzoneRAT can enumerate directories on a compromise host. [426] |
| S0612 | WastedLocker | WastedLocker can enumerate files and directories just prior to encryption. [427] |
| S0689 | WhisperGate | WhisperGate can locate files based on hardcoded file extensions. [428] [429] [430] [431] |
| G0124 | Windigo | Windigo has used a script to check for the presence of files created by OpenSSH backdoors. [432] |
| S0466 | WindTail | WindTail has the ability to enumerate the users home directory and the path to its own application bundle. [433] [434] |
| S0219 | WINERACK | WINERACK can enumerate files and directories. [109] |
| S0059 | WinMM | WinMM sets a WH_CBT Windows hook to search for and capture files on the victim. [435] |
| S0141 | Winnti for Windows | Winnti for Windows can check for the presence of specific files prior to moving to the next phase of execution. [436] |
| G0044 | Winnti Group | Winnti Group has used a program named ff.exe to search for specific documents on compromised hosts. [437] |
| G1035 | Winter Vivern | Winter Vivern delivered malicious JavaScript payloads capable of listing folders and emails in exploited email servers. [438] |
| S1065 | Woody RAT | Woody RAT can list all files and their associated attributes, including filename, type, owner, creation time, last access time, last write time, size, and permissions. [439] |
| S0161 | XAgentOSX | XAgentOSX contains the readFiles function to return a detailed listing (sometimes recursive) of a specified directory. [440] XAgentOSX contains the showBackupIosFolder function to check for IOS device backups by running ls -la ~/Library/Application\ Support/MobileSync/Backup/ . [440] |
| S0658 | XCSSET | XCSSET has used mdfind to enumerate a list of apps known to grant screen sharing permissions and leverages a module to run the command ls -la ~/Desktop . [441] [442] |
| S0248 | yty | yty gathers information on victim’s drives and has a plugin for document listing. [443] |
| S0251 | Zebrocy | Zebrocy searches for files that are 60mb and less and contain the following extensions: .doc, .docx, .xls, .xlsx, .ppt, .pptx, .exe, .zip, and .rar. Zebrocy also runs the echo %APPDATA% command to list the contents of the directory. [444] [445] [446] Zebrocy can obtain the current execution path as well as perform drive enumeration. [447] [448] |
| S0330 | Zeus Panda | Zeus Panda searches for specific directories on the victim’s machine. [449] |
| S1114 | ZIPLINE | ZIPLINE can find and append specific files on Ivanti Connect Secure VPNs based upon received commands. [450] |
| S0086 | ZLib | ZLib has the ability to enumerate files and drives. [263] |
| S0672 | Zox | Zox can enumerate files on a compromised host. [451] |
| S0350 | zwShell | zwShell can browse the file system. [273] |
| S0412 | ZxShell | ZxShell has a command to open a file manager and explorer on the system. [452] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0370 | Recursive Enumeration of Files and Directories Across Privilege Contexts | AN1040 | Execution of file enumeration commands (e.g., 'dir', 'tree') from non-standard processes or unusual user contexts, followed by recursive directory traversal or access to sensitive locations. |
| AN1041 | Use of file enumeration commands (e.g., 'ls', 'find', 'locate') executed by suspicious users or scripts accessing broad file hierarchies or restricted directories. |  |  |
| AN1042 | Execution of file or directory discovery commands (e.g., 'ls', 'find') from terminal or script-based tooling, especially outside normal user workflows. |  |  |
| AN1043 | Execution of esxcli commands to enumerate datastore, configuration files, or directory structures by unauthorized or remote users. |  |  |
| AN1044 | Execution of file discovery commands (e.g., 'dir', 'show flash', 'nvram:') from CLI interfaces, especially by unauthorized users or from abnormal source IPs. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0370 | Recursive Enumeration of Files and Directories Across Privilege Contexts | AN1040 | Execution of file enumeration commands (e.g., 'dir', 'tree') from non-standard processes or unusual user contexts, followed by recursive directory traversal or access to sensitive locations. |
| AN1041 | Use of file enumeration commands (e.g., 'ls', 'find', 'locate') executed by suspicious users or scripts accessing broad file hierarchies or restricted directories. |  |  |
| AN1042 | Execution of file or directory discovery commands (e.g., 'ls', 'find') from terminal or script-based tooling, especially outside normal user workflows. |  |  |
| AN1043 | Execution of esxcli commands to enumerate datastore, configuration files, or directory structures by unauthorized or remote users. |  |  |
| AN1044 | Execution of file discovery commands (e.g., 'dir', 'show flash', 'nvram:') from CLI interfaces, especially by unauthorized users or from abnormal source IPs. |  |  |

---

## References

- [Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)
- [US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved October 19, 2020.](https://www.us-cert.gov/ncas/alerts/TA18-106A)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Crowdstrike Global Intelligence Team. (2014, June 9). CrowdStrike Intelligence Report: Putter Panda. Retrieved January 22, 2016.](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)
- [Juan Andrés Guerrero-Saade & Tom Hegel. (2024, March 21). AcidPour | New Embedded Wiper Variant of AcidRain Appears in Ukraine. Retrieved November 25, 2024.](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)
- [Juan Andres Guerrero-Saade and Max van Amerongen, SentinelOne. (2022, March 31). AcidRain | A Modem Wiper Rains Down on Europe. Retrieved March 25, 2024.](https://www.sentinelone.com/labs/acidrain-a-modem-wiper-rains-down-on-europe/)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [FireEye Threat Intelligence. (2015, December 1). China-based Cyber Threat Group Uses Dropbox for Malware Communications and Targets Hong Kong Media Outlets. Retrieved December 4, 2015.](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)
- [ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
- [Bitdefender. (2015, December). APT28 Under the Scope. Retrieved February 23, 2017.](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
- [Max Kersten & Alexandre Mundo. (2023, November 29). Akira Ransomware. Retrieved April 4, 2024.](https://www.trellix.com/blogs/research/akira-ransomware/)
- [Nutland, J. and Szeliga, M. (2024, October 21). Akira ransomware continues to evolve. Retrieved December 10, 2024.](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
- [CISA et al. (2024, April 18). #StopRansomware: Akira Ransomware. Retrieved December 10, 2024.](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)
- [Zemah, Y. (2024, December 2). Threat Assessment: Howling Scorpius (Akira Ransomware). Retrieved January 8, 2025.](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [Hiroaki, H. (2024, November 26). Guess Who’s Back - The Return of ANEL in the Recent Earth Kasha Spear-phishing Campaign in 2024. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
- [Anthropic. (2025, November). Disrupting the first reported AI-orchestrated cyber espionage campaign. Retrieved April 20, 2026.](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [Grunzweig, J., et al. (2016, May 24). New Wekby Attacks Use DNS Requests As Command and Control Mechanism. Retrieved November 15, 2018.](https://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
- [Guarnieri, C. (2015, June 19). Digital Attack on German Parliament: Investigative Report on the Hack of the Left Party Infrastructure in Bundestag. Retrieved January 22, 2018.](https://netzpolitik.org/2015/digital-attack-on-german-parliament-investigative-report-on-the-hack-of-the-left-party-infrastructure-in-bundestag/)
- [Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved November 17, 2024.](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)
- [Chen, X., Scott, M., Caselden, D.. (2014, April 26). New Zero-Day Exploit targeting Internet Explorer Versions 9 through 11 Identified in Targeted Attacks. Retrieved January 14, 2016.](https://www.fireeye.com/blog/threat-research/2014/04/new-zero-day-exploit-targeting-internet-explorer-versions-9-through-11-identified-in-targeted-attacks.html)
- [Yates, M. (2017, June 18). APT3 Uncovered: The code evolution of Pirpi. Retrieved September 28, 2017.](https://recon.cx/2017/montreal/resources/slides/RECON-MTL-2017-evolution_of_pirpi.pdf)
- [Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)
- [DHS/CISA. (2020, August 26). FASTCash 2.0: North Korea's BeagleBoyz Robbing Banks. Retrieved September 29, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)
- [FBI. (2020, September 17). Indicators of Compromise Associated with Rana Intelligence Computing, also known as Advanced Persistent Threat 39, Chafer, Cadelspy, Remexi, and ITG07. Retrieved December 10, 2020.](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)
- [Glyer, C, et al. (2020, March). This Is Not a Test: APT41 Initiates Global Intrusion Campaign Using Multiple Exploits. Retrieved April 28, 2020.](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)
- [Perez, D. et al. (2021, May 27). Re-Checking Your Pulse: Updates on Chinese APT Actors Compromising Pulse Secure VPN Devices. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Unit 42. (2025, December 11). Hamas-Affiliated Ashen Lepus Targets Middle Eastern Diplomatic Entities With New AshTag Malware Suite. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [Trend Micro. (2018, November 20). Lazarus Continues Heists, Mounts Attacks on Financial Organizations in Latin America. Retrieved December 3, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Yuste, J. Pastrana, S. (2021, February 9). Avaddon ransomware: an in-depth analysis and decryption of infected systems. Retrieved August 19, 2021.](https://arxiv.org/pdf/2102.04796.pdf)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [Hasherezade. (2021, July 23). AvosLocker enters the ransomware scene, asks for partners. Retrieved January 11, 2023.](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
- [Trend Micro Research. (2022, April 4). Ransomware Spotlight AvosLocker. Retrieved January 11, 2023.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-avoslocker)
- [Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
- [Mundo, A. et al. (2021, February). Technical Analysis of Babuk Ransomware. Retrieved August 11, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
- [Centero, R. et al. (2021, February 5). New in Ransomware: Seth-Locker, Babuk Locker, Maoloa, TeslaCrypt, and CobraLocker. Retrieved August 11, 2021.](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)
- [Unit 42. (2019, February 22). New BabyShark Malware Targets U.S. National Security Think Tanks. Retrieved October 7, 2019.](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
- [Hinchliffe, A. and Falcone, R. (2020, May 11). Updated BackConfig Malware Targeting Government and Military Organizations in South Asia. Retrieved June 17, 2020.](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)
- [Symantec Security Response. (2014, June 30). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
- [FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved November 17, 2024.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
- [Accenture iDefense Unit. (2019, March 5). Mudcarp's Focus on Submarine Technologies. Retrieved August 24, 2021.](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
- [Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
- [Bar, T., Conant, S. (2017, October 20). BadPatch. Retrieved November 13, 2018.](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)
- [Check Point. (2020, November 26). Bandook: Signed & Delivered. Retrieved May 31, 2021.](https://research.checkpoint.com/2020/bandook-signed-delivered/)
- [US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1, 2020.](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
- [Lee, B. Grunzweig, J. (2015, December 22). BBSRAT Attacks Targeting Russian Organizations Linked to Roaming Tiger. Retrieved August 19, 2016.](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)
- [Kirill Boychenko. (2025, July 14). Contagious Interview Campaign Escalates With 67 Malicious npm Packages and New Malware Loader. Retrieved October 19, 2025.](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Zykov, K. (2020, August 13). CactusPete APT group’s updated Bisonal backdoor. Retrieved May 5, 2021.](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [Cyble. (2022, May 6). New ransomware variant targeting high-value organizations. Retrieved November 17, 2024.](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
- [Avertium. (2022, June 1). AN IN-DEPTH LOOK AT BLACK BASTA RANSOMWARE. Retrieved March 7, 2023.](https://www.avertium.com/resources/threat-reports/in-depth-look-at-black-basta-ransomware)
- [Inman, R. and Gurney, P. (2022, June 6). Shining the Light on Black Basta. Retrieved March 8, 2023.](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)
- [Sharma, S. and Hegde, N. (2022, June 7). Black basta Ransomware Goes Cross-Platform, Now Targets ESXi Systems. Retrieved March 8, 2023.](https://www.uptycs.com/blog/black-basta-ransomware-goes-cross-platform-now-targets-esxi-systems)
- [Vilkomir-Preisman, S. (2022, August 18). Beating Black Basta Ransomware. Retrieved March 8, 2023.](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)
- [Elsad, A. (2022, August 25). Threat Assessment: Black Basta Ransomware. Retrieved March 8, 2023.](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)
- [Trend Micro. (2022, September 1). Ransomware Spotlight Black Basta. Retrieved March 8, 2023.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-blackbasta)
- [Check Point. (2022, October 20). BLACK BASTA AND THE UNNOTICED DELIVERY. Retrieved March 8, 2023.](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [FireEye Labs/FireEye Threat Intelligence. (2015, May 14). Hiding in Plain Sight: FireEye and Microsoft Expose Obfuscation Tactic. Retrieved November 17, 2024.](https://web.archive.org/web/20240119213200/https://www2.fireeye.com/rs/fireye/images/APT17_Report.pdf)
- [F-Secure Labs. (2014). BlackEnergy & Quedagh: The convergence of crimeware and APT attacks. Retrieved March 24, 2016.](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
- [Baumgartner, K. and Garnaeva, M.. (2014, November 3). BE2 custom plugins, router abuse, and target profiles. Retrieved March 24, 2016.](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
- [MSTIC. (2019, December 12). GALLIUM: Targeting global telecom. Retrieved January 13, 2021.](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)
- [US-CERT. (2020, August 19). MAR-10295134-1.v1 – North Korean Remote Access Trojan: BLINDINGCAN. Retrieved August 19, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
- [NHS Digital . (2020, August 20). BLINDINGCAN Remote Access Trojan. Retrieved August 20, 2020.](https://digital.nhs.uk/cyber-alerts/2020/cc-3603)
- [Cash, D., Grunzweig, J., Meltzer, M., Adair, S., Lancaster, T. (2021, August 17). North Korean APT InkySquid Infects Victims Using Browser Exploits. Retrieved September 30, 2021.](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
- [Scott Henderson, Cristiana Kittner, Sarah Hawley & Mark Lechtik, Google Cloud. (2023, January 19). Suspected Chinese Threat Actors Exploiting FortiOS Vulnerability (CVE-2022-42475). Retrieved December 31, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
- [MSTIC. (2021, May 28). Breaking down NOBELIUM’s latest early-stage toolset. Retrieved August 4, 2021.](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
- [CheckPoint Research. (2021, July 1). IndigoZebra APT continues to attack Central Asia with evolving tools. Retrieved September 24, 2021.](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
- [Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
- [CrowdStrike. (2025, December 4). Unveiling WARP PANDA: A New Sophisticated China-Nexus Adversary. Retrieved April 16, 2026.](https://www.crowdstrike.com/en-us/blog/warp-panda-cloud-threats/)
- [DHS/CISA. (2026, February 11). AR25-338A: BRICKSTORM Backdoor. Retrieved April 16, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
- [Huseyin Can Yuceel. (2025, October 1). BRICKSTORM Malware: UNC5221 Targets Tech and Legal Sectors in the United States. Retrieved April 16, 2026.](https://www.picussecurity.com/resource/blog/brickstorm-malware-unc5221-targets-tech-and-legal-sectors-in-the-united-states)
- [Matt Lin, Austin Larsen, John Wolfram, Ashley Pearson, Josh Murchie, Lukasz Lamparski, Joseph Pisano, Ryan Hall, Ron Craft, Shawn Crew, Billy Wong, Tyler McLellan. (2024, April 4). Cutting Edge, Part 4: Ivanti Connect Secure VPN Post-Exploitation Lateral Movement Case Studies. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
- [NVISO Incident Response. (2025, April 1). BRICKSTORM Backdoor Analysis: A Persistent Espionage Threat to European Industries. Retrieved April 16, 2026.](https://blog.nviso.eu/wp-content/uploads/2025/04/NVISO-BRICKSTORM-Report.pdf)
- [Sarah Yoder, John Wolfram, Ashley Pearson, Doug Bienstock, Josh Madeley, Josh Murchie, Brad Slaybaugh, Matt Lin, Geoff Carstairs, Austin Larsen. (2025, September 24). Another BRICKSTORM: Stealthy Backdoor Enabling Espionage into Tech and Legal Sectors. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
- [Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Threat Intelligence Team. (2022, March 18). Double header: IsaacWiper and CaddyWiper . Retrieved April 11, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/03/double-header-isaacwiper-and-caddywiper/)
- [Falcone, R., Lee, B. (2018, November 20). Sofacy Continues Global Attacks and Wheels Out New ‘Cannon’ Trojan. Retrieved November 26, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
- [Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [FireEye iSIGHT Intelligence. (2017, April 6). APT10 (MenuPass Group): New Tools, Global Campaign Latest Manifestation of Longstanding Threat. Retrieved June 29, 2017.](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)
- [Dela Cruz, A. et al. (2022, May 25). New Linux-Based Ransomware Cheerscrypt Targeting ESXi Devices Linked to Leaked Babuk Source Code. Retrieved December 19, 2023.](https://www.trendmicro.com/en_se/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [Eoin Miller. (2021, March 23). Defending Against the Zero Day: Analyzing Attacker Behavior Post-Exploitation of Microsoft Exchange. Retrieved October 27, 2022.](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Chen, T. and Chen, Z. (2020, February 17). CLAMBLING - A New Backdoor Base On Dropbox. Retrieved November 12, 2021.](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
- [Mundo, A. (2019, August 1). Clop Ransomware. Retrieved May 10, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
- [Microsoft. (n.d.). Dir. Retrieved April 18, 2016.](https://technet.microsoft.com/en-us/library/cc755121.aspx)
- [Dutch Military Intelligence and Security Service (MIVD) & Dutch General Intelligence and Security Service (AIVD). (2024, February 6). Ministry of Defense of the Netherlands uncovers COATHANGER, a stealthy Chinese FortiGate RAT. Retrieved February 7, 2024.](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Lunghi, D. (2021, August 17). Confucius Uses Pegasus Spyware-related Lures to Target Pakistani Military. Retrieved December 26, 2021.](https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Baskin, B. (2020, July 8). TAU Threat Discovery: Conti Ransomware. Retrieved February 17, 2021.](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [Chen, y., et al. (2019, January 31). Mac Malware Steals Cryptocurrency Exchanges’ Cookies. Retrieved July 22, 2020.](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
- [FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
- [F-Secure Labs. (2014, July). COSMICDUKE Cosmu with a twist of MiniDuke. Retrieved July 3, 2014.](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)
- [byt3bl33d3r. (2018, September 8). SMB: Command Reference. Retrieved July 17, 2020.](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
- [Microsoft. (2022, June 2). Exposing POLONIUM activity and infrastructure targeting Israeli organizations. Retrieved July 1, 2022.](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [N. Baisini. (2022, July 13). Transparent Tribe begins targeting education sector in latest campaign. Retrieved September 22, 2022.](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
- [Blaich, A., et al. (2018, January 18). Dark Caracal: Cyber-espionage at a Global Scale. Retrieved April 11, 2018.](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)
- [Stokes, P. (2020, July 27). Four Distinct Families of Lazarus Malware Target Apple’s macOS Platform. Retrieved August 7, 2020.](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [Kohler, A. and Lopez, C. (2024, April 30). Malware: Cuckoo Behaves Like Cross Between Infostealer and Spyware. Retrieved August 20, 2024.](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
- [Stokes, P. (2024, May 9). macOS Cuckoo Stealer | Ensuring Detection and Defense as New Samples Rapidly Emerge. Retrieved August 20, 2024.](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)
- [NCSC. (2022, February 23). Cyclops Blink Malware Analysis Report. Retrieved March 3, 2022.](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
- [Haquebord, F. et al. (2022, March 17). Cyclops Blink Sets Sights on Asus Routers. Retrieved March 17, 2022.](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)
- [Mabutas, G. (2020, May 11). New MacOS Dacls RAT Backdoor Shows Lazarus’ Multi-Platform Attack Capability. Retrieved August 10, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-dacls-rat-backdoor-show-lazarus-multi-platform-attack-capability/)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Microsoft. (2016, July 14). Reverse engineering DUBNIUM – Stage 2 payload analysis . Retrieved March 31, 2021.](https://www.microsoft.com/security/blog/2016/07/14/reverse-engineering-dubnium-stage-2-payload-analysis/)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [Ash, B., et al. (2018, June 26). RANCOR: Targeted Attacks in South East Asia Using PLAINTEE and DDKONG Malware Families. Retrieved July 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
- [McLellan, T. and Moore, J. et al. (2021, April 29). UNC2447 SOMBRAT and FIVEHANDS Ransomware: A Sophisticated Financial Threat. Retrieved June 2, 2021.](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
- [Dahan, A. (2017, May 24). OPERATION COBALT KITTY: A LARGE-SCALE APT IN ASIA CARRIED OUT BY THE OCEANLOTUS GROUP. Retrieved November 5, 2018.](https://www.cybereason.com/blog/operation-cobalt-kitty-apt)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Fidelis Cybersecurity. (2016, February 29). The Turbo Campaign, Featuring Derusbi for 64-bit Linux. Retrieved March 2, 2016.](https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2016/2016.02.29.Turbo_Campaign_Derusbi/TA_Fidelis_Turbo_1602_0.pdf)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [Halcyon RISE Team. (2024, December 12). Cloak Ransomware Variant Exhibits Advanced Persistence, Evasion and VHD Extraction Capabilities. Retrieved December 23, 2025.](https://www.halcyon.ai/blog/cloak-ransomware-variant-exhibits-advanced-persistence-evasion-and-vhd-extraction-capabilities)
- [Fishbein, N., Kajiloti, M.. (2020, July 28). Watch Your Containers: Doki Infecting Docker Servers in the Cloud. Retrieved March 30, 2021.](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [Slowik, J. (2021, October). THE BAFFLING BERSERK BEAR: A DECADE’S ACTIVITY TARGETING CRITICAL INFRASTRUCTURE. Retrieved December 6, 2021.](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
- [CISA. (2020, December 1). Russian State-Sponsored Advanced Persistent Threat Actor Compromises U.S. Government Targets. Retrieved December 9, 2021.](https://www.cisa.gov/uscert/ncas/alerts/aa20-296a#revisions)
- [Cybereason Nocturnus Team. (2020, December 9). MOLERATS IN THE CLOUD: New Malware Arsenal Abuses Cloud Platforms in Middle East Espionage Campaign. Retrieved December 22, 2020.](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
- [Ilascu, I. (2020, December 14). Hacking group’s new malware abuses Google and Facebook services. Retrieved December 28, 2020.](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
- [Konstantin Zykov. (2019, September 23). Hello! My name is Dtrack. Retrieved January 20, 2021.](https://securelist.com/my-name-is-dtrack/93338/)
- [Hod Gavriel. (2019, November 21). Dtrack: In-depth analysis of APT on a nuclear power plant. Retrieved January 20, 2021.](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [ClearSky. (2016, January 7). Operation DustySky. Retrieved January 8, 2016.](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
- [GReAT. (2019, April 10). Gaza Cybergang Group1, operation SneakyPastes. Retrieved May 13, 2020.](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
- [Falcone, R., et al.. (2015, June 16). Operation Lotus Blossom. Retrieved February 15, 2016.](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)
- [Accenture Security. (2018, January 27). DRAGONFISH DELIVERS NEW FORM OF ELISE MALWARE TARGETING ASEAN DEFENCE MINISTERS’ MEETING AND ASSOCIATES. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)
- [Winters, R. (2015, December 20). The EPS Awakens - Part 2. Retrieved January 22, 2016.](https://web.archive.org/web/20151226205946/https://www.fireeye.com/blog/threat-research/2015/12/the-eps-awakens-part-two.html)
- [Cyble. (2024, May 24). The Rust Revolution: New Embargo Ransomware Steps In. Retrieved October 19, 2025.](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [Kaspersky Lab's Global Research & Analysis Team. (2014, August 06). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroboros. Retrieved November 7, 2018.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
- [Symantec Threat Hunter Team. (2022, October 21). Exbyte: BlackByte Ransomware Attackers Deploy New Exfiltration Tool. Retrieved December 16, 2024.](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)
- [US-CERT. (2017, November 22). Alert (TA17-318A): HIDDEN COBRA – North Korean Remote Administration Tool: FALLCHILL. Retrieved December 7, 2017.](https://www.us-cert.gov/ncas/alerts/TA17-318A)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [FinFisher. (n.d.). Retrieved September 12, 2024.](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
- [Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [Matthews, M. and Backhouse, W. (2021, June 15). Handy guide to a new Fivehands ransomware variant. Retrieved June 24, 2021.](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)
- [Ramin Nafisi. (2021, September 27). FoggyWeb: Targeted NOBELIUM malware leads to persistent backdoor. Retrieved October 4, 2021.](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
- [CISA. (2020, September 15). Iran-Based Threat Actor Exploits VPN Vulnerabilities. Retrieved December 21, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)
- [Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.](https://objective-see.com/blog/blog_0x25.html)
- [GREAT. (2021, March 30). APT10: sophisticated multi-layered loader Ecipekac discovered in A41APT campaign. Retrieved June 17, 2021.](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
- [Doctor Web. (2014, November 21). Linux.BackDoor.Fysbis.1. Retrieved December 7, 2017.](https://vms.drweb.com/virus/?i=4276269)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Unit 42. (2022, February 3). Russia’s Gamaredon aka Primitive Bear APT Group Actively Targeting Ukraine. Retrieved February 21, 2022.](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Threat Hunter Team, Symantec and Carbon Black. (2025, April 10). Shuckworm Targets Foreign Military Mission Based in Ukraine. Retrieved July 23, 2025.](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [F-Secure Labs. (2015, September 17). The Dukes: 7 years of Russian cyberespionage. Retrieved December 10, 2015.](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
- [Trustwave SpiderLabs. (2020, June 25). The Golden Tax Department and Emergence of GoldenSpy Malware. Retrieved July 23, 2020.](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)
- [Symantec Threat Hunter Team. (2024, May 16). Springtail: New Linux Backdoor Added to Toolkit. Retrieved January 17, 2025.](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
- [Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
- [Priego, A. (2021, July). THE BROTHERS GRIM: THE REVERSING TALE OF GRIMAGENT MALWARE USED BY RYUK. Retrieved September 19, 2024.](https://www.group-ib.com/blog/grimagent/)
- [Ungur, P. (n.d.). HAVOC. Retrieved August 4, 2025.](https://havocframework.com/docs/welcome)
- [Guerrero-Saade, J. (2022, February 23). HermeticWiper | New Destructive Malware Used In Cyber Attacks on Ukraine. Retrieved March 25, 2022.](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
- [Dani, M. (2022, March 1). Ukrainian Targets Hit by HermeticWiper, New Datawiper Malware. Retrieved March 25, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [Knight, S.. (2020, April 16). VMware Carbon Black TAU Threat Analysis: The Evolution of Lazarus. Retrieved May 1, 2020.](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
- [Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)
- [Desai, D.. (2015, August 14). Chinese cyber espionage APT group leveraging recently leaked Hacking Team exploits to target a Financial Services Firm. Retrieved January 26, 2016.](http://research.zscaler.com/2015/08/chinese-cyber-espionage-apt-group.html)
- [Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
- [Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
- [CrowdStrike. (2022, May). ICEAPPLE: A NOVEL INTERNET INFORMATION SERVICES (IIS) POST-EXPLOITATION FRAMEWORK. Retrieved June 27, 2022.](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
- [QiAnXin Threat Intelligence Center. (2019, February 18). APT-C-36: Continuous Attacks Targeting Colombian Government Institutions and Corporations. Retrieved May 5, 2020.](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [SentinelOne. (n.d.). What Is Inc. Ransomware?. Retrieved June 5, 2024.](https://www.sentinelone.com/anthology/inc-ransom/)
- [Symantec. (2018, March 14). Inception Framework: Alive and Well, and Hiding Behind Proxies. Retrieved May 8, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/inception-framework-hiding-behind-proxies)
- [Anton Cherepanov. (2017, June 12). Win32/Industroyer: A new threat for industrial controls systems. Retrieved December 18, 2020.](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
- [ASERT Team. (2018, April 04). Innaput Actors Utilize Remote Access Trojan Since 2016, Presumably Targeting Victim Files. Retrieved July 9, 2018.](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)
- [Seongsu Park. (2024, November 4). From Pyongyang to Your Payroll: The Rise of North Korean Remote Workers in the West. Retrieved October 17, 2025.](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
- [eSentire Threat Response Unit (TRU). (2024, November 14). Bored BeaverTail & InvisibleFerret Yacht Club – A Lazarus Lure Pt.2. Retrieved October 17, 2025.](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
- [Unit42. (2024, October 9). Contagious Interview: DPRK Threat Actors Lure Tech Industry Job Seekers to Install New Variants of BeaverTail and InvisibleFerret Malware. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Sancho, D., et al. (2012, May 22). IXESHE An APT Campaign. Retrieved June 7, 2019.](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
- [Bingham, J. (2013, February 11). Cross-Platform Frutas RAT Builder and Back Door. Retrieved April 23, 2019.](https://www.symantec.com/connect/blogs/cross-platform-frutas-rat-builder-and-back-door)
- [Yadav, A., et al. (2016, January 29). Malicious Office files dropping Kasidet and Dridex. Retrieved March 24, 2016.](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Parys, B. (2017, February 11). The KeyBoys are back in town. Retrieved June 13, 2019.](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)
- [US-CERT. (2018, August 09). MAR-10135536-17 – North Korean Trojan: KEYMARBLE. Retrieved August 16, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
- [Dahan, A. et al. (2020, November 2). Back to the Future: Inside the Kimsuky KGH Spyware Suite. Retrieved November 6, 2020.](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
- [Gilbert Sison, Rheniel Ramos, Jay Yaneza, Alfredo Oliveira. (2018, January 15). KillDisk Variant Hits Latin American Financial Groups. Retrieved January 12, 2021.](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)
- [Tarakanov , D.. (2013, September 11). The “Kimsuky” Operation: A North Korean APT?. Retrieved August 13, 2019.](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [KISA. (2021). Phishing Target Reconnaissance and Attack Resource Analysis Operation Muzabi. Retrieved March 8, 2024.](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Singer, G. (2020, April 3). Threat Alert: Kinsing Malware Attacks Targeting Container Environments. Retrieved April 1, 2021.](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
- [Bermejo, L., et al. (2017, June 22). Following the Trail of BlackTech’s Cyber Espionage Campaigns. Retrieved May 5, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
- [Jazi, H. (2021, February). LazyScripter: From Empire to double RAT. Retrieved November 17, 2024.](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
- [Rascagneres, P. (2017, May 03). KONNI: A Malware Under The Radar For Years. Retrieved November 5, 2018.](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
- [Black Lotus Labs. (2023, December 13). Routers Roasting On An Open Firewall: The KV-Botnet Investigation. Retrieved June 10, 2024.](https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/)
- [Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
- [Conteras, T., Splunk Research Team. (2025, September 25). From Prompt to Payload: LAMEHUG’s LLM-Driven Cyber Intrusion. Retrieved April 21, 2026.](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
- [Google Threat Intelligence Group. (2025, November 5). GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools. Retrieved March 31, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
- [Proofpoint Threat Research and Team Cymru S2 Threat Research. (2024, April 4). Latrodectus: This Spider Bytes Like Ice . Retrieved May 31, 2024.](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
- [Batista, J. (2024, June 17). Latrodectus, are you coming back?. Retrieved September 13, 2024.](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
- [Stepanic, D. and Bousseaden, S. (2024, May 15). Spring Cleaning with LATRODECTUS: A Potential Replacement for ICEDID. Retrieved September 13, 2024.](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
- [Saini, A. and Hossein, J. (2022, January 27). North Korea’s Lazarus APT leverages Windows Update client, GitHub in latest campaign. Retrieved January 27, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)
- [Pradhan, A. (2022, February 8). LolZarus: Lazarus Group Incorporating Lolbins into Campaigns. Retrieved March 22, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)
- [Symantec Security Response. (2018, July 25). Leafminer: New Espionage Campaigns Targeting Middle Eastern Regions. Retrieved August 28, 2018.](https://www.symantec.com/blogs/threat-intelligence/leafminer-espionage-middle-east)
- [Stuart Ashenbrenner, Alden Schmidt. (2024, April 25). LightSpy Malware Variant Targeting macOS. Retrieved January 3, 2025.](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
- [Zhou, R. (2012, May 15). Backdoor.Linfo. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
- [Lin, M. et al. (2024, February 27). Cutting Edge, Part 3: Investigating Ivanti Connect Secure VPN Exploitation and Persistence Attempts. Retrieved March 1, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
- [FBI. (2022, February 4). Indicators of Compromise Associated with LockBit 2.0 Ransomware. Retrieved January 24, 2025.](https://www.ic3.gov/CSA/2022/220204.pdf)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [Breitenbacher, D. (2022, December 14). Unmasking MirrorFace: Operation LiberalFace targeting Japanese political entities. Retrieved April 17, 2026.](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
- [ITOCHU. (2024, January 24). The Endless Struggle Against APT10: Insights from LODEINFO v0.6.6 - v0.7.3 Analysis. Retrieved April 17, 2026.](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [Muhammad, I., Unterbrink, H.. (2021, January 6). A Deep Dive into Lokibot Infection Chain. Retrieved August 31, 2021.](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
- [Raggi, M. Schwarz, D.. (2019, August 1). LookBack Malware Targets the United States Utilities Sector with Phishing Attacks Impersonating Engineering Licensing Boards. Retrieved February 25, 2021.](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [Lechtik, M, and etl. (2021, July 14). LuminousMoth APT: Sweeping attacks for the chosen few. Retrieved October 20, 2022.](https://securelist.com/apt-luminousmoth/103332/)
- [Botezatu, B and etl. (2021, July 21). LuminousMoth - PlugX, File Exfiltration and Persistence Revisited. Retrieved October 20, 2022.](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [The Cylance Threat Research Team. (2017, March 22). El Machete's Malware Attacks Cut Through LATAM. Retrieved September 13, 2019.](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)
- [kate. (2020, September 25). APT-C-43 steals Venezuelan military secrets to provide intelligence support for the reactionaries — HpReact campaign. Retrieved November 20, 2020.](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [Lee, B. and Falcone, R. (2017, February 15). Magic Hound Campaign Attacks Saudi Targets. Retrieved December 27, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)
- [Hromcova, Z. and Burgher, A. (2023, September 21). OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes. Retrieved November 21, 2024.](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
- [Asheer Malhotra & Vitor Ventura. (2022, August 2). Manjusaka: A Chinese sibling of Sliver and Cobalt Strike. Retrieved September 4, 2024.](https://blog.talosintelligence.com/manjusaka-offensive-framework/)
- [GReAT. (2021, June 16). Ferocious Kitten: 6 Years of Covert Surveillance in Iran. Retrieved September 22, 2021.](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
- [Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Del Fierro, C. Kessem, L.. (2020, January 8). From Mega to Giga: Cross-Version Comparison of Top MegaCortex Modifications. Retrieved February 15, 2021.](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
- [Symantec. (2020, November 17). Japan-Linked Organizations Targeted in Long-Running and Sophisticated Attack Campaign. Retrieved December 17, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)
- [Leong, R., Perez, D., Dean, T. (2019, October 31). MESSAGETAP: Who’s Reading Your Text Messages?. Retrieved May 11, 2020.](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [Erlich, C. (2020, April 3). The Avast Abuser: Metamorfo Banking Malware Hides By Abusing Avast Executable. Retrieved May 26, 2020.](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
- [Zhang, X. (2020, February 4). Another Metamorfo Variant Targeting Customers of Financial Institutions in More Countries. Retrieved July 30, 2020.](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
- [Sierra, E., Iglesias, G.. (2018, April 24). Metamorfo Campaigns Targeting Brazilian Users. Retrieved July 30, 2020.](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
- [Tsarfaty, Y. (2018, July 25). Micropsia Malware. Retrieved November 13, 2018.](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [ESET Security. (2019, November 19). Mispadu: Advertisement for a discounted Unhappy Meal. Retrieved March 13, 2024.](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
- [Falcone, R. and Miller-Osborn, J.. (2016, January 24). Scarlet Mimic: Years-Long Espionage Campaign Targets Minority Activists. Retrieved February 10, 2016.](http://researchcenter.paloaltonetworks.com/2016/01/scarlet-mimic-years-long-espionage-targets-minority-activists/)
- [Miller-Osborn, J. and Grunzweig, J.. (2017, March 30). Trochilus and New MoonWind RATs Used In Attack Against Thai Organizations. Retrieved March 30, 2017.](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 10). MuddyWater expands operations. Retrieved November 2, 2018.](https://securelist.com/muddywater/88059/)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [Hamzeloofard, S. (2020, January 31). New wave of PlugX targets Hong Kong | Avira Blog. Retrieved April 13, 2021.](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)
- [Lior Rochberger, Tom Fakterman, Robert Falcone. (2023, September 22). Cyberespionage Attacks Against Southeast Asian Government Linked to Stately Taurus, Aka Mustang Panda. Retrieved September 9, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)
- [Vrabie, V. (2021, April 23). NAIKON – Traces from a Military Cyber-Espionage Operation. Retrieved June 29, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
- [Proofpoint. (2020, December 2). Geofenced NetWire Campaigns. Retrieved January 7, 2021.](https://www.proofpoint.com/us/blog/threat-insight/geofenced-netwire-campaigns)
- [McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Fidelis Cybersecurity. (2013, June 28). Fidelis Threat Advisory #1009: "njRAT" Uncovered. Retrieved June 4, 2019.](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
- [Scott W. Brady. (2020, October 15). United States vs. Yuriy Sergeyevich Andrienko et al.. Retrieved November 25, 2020.](https://www.justice.gov/opa/press-release/file/1328521/download)
- [Malhotra, A. (2021, March 2). ObliqueRAT returns with new campaign using hijacked websites. Retrieved September 2, 2021.](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
- [Sherstobitoff, R., Malhotra, A. (2018, October 18). ‘Operation Oceansalt’ Attacks South Korea, U.S., and Canada With Source Code From Chinese Hacker Group. Retrieved November 30, 2018.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 15). Octopus-infested seas of Central Asia. Retrieved November 14, 2018.](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
- [Paganini, P. (2018, October 16). Russia-linked APT group DustSquad targets diplomatic entities in Central Asia. Retrieved August 24, 2021.](https://securityaffairs.co/wordpress/77165/apt/russia-linked-apt-dustsquad.html)
- [Cherepanov, A. (2018, October 4). Nomadic Octopus Cyber espionage in Central Asia. Retrieved October 13, 2021.](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)
- [Hromcova, Z. and Burgher, A. (2023, December 14). OilRig’s persistent attacks using cloud service-powered downloaders. Retrieved November 26, 2024.](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
- [Hromcova, Z. (2019, July). OKRUM AND KETRICAN: AN OVERVIEW OF RECENT KE3CHANG GROUP ACTIVITY. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-uncovers-operation-honeybee-malicious-document-campaign-targeting-humanitarian-aid-groups/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
- [Phil Stokes. (2020, September 8). Coming Out of Your Shell: From Shlayer to ZShlayer. Retrieved September 13, 2021.](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)
- [Phil Stokes. (2021, February 16). 20 Common Tools & Techniques Used by macOS Threat Actors & Malware. Retrieved August 23, 2021.](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [ANSSI. (2021, January 27). SANDWORM INTRUSION SET CAMPAIGN TARGETING CENTREON SYSTEMS. Retrieved March 30, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
- [Perez, D. et al. (2021, April 20). Check Your Pulse: Suspected APT Actors Leverage Authentication Bypass Techniques and Pulse Secure Zero-Day. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
- [Mullaney, C. & Honda, H. (2012, May 4). Trojan.Pasam. Retrieved February 22, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)
- [Cymmetria. (2016). Unveiling Patchwork - The Copy-Paste APT. Retrieved November 17, 2024.](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)
- [Leonardo. (2020, May 29). MALWARE TECHNICAL INSIGHT TURLA “Penquin_x64”. Retrieved March 11, 2021.](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
- [Unit 42. (2022, June 13). GALLIUM Expands Targeting Across Telecommunications, Government and Finance Sectors With New PingPull Tool. Retrieved August 7, 2022.](https://unit42.paloaltonetworks.com/pingpull-gallium/)
- [Grunzweig, J., et al. (2016, May 24). New Wekby Attacks Use DNS Requests As Command and Control Mechanism. Retrieved August 17, 2016.](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
- [Trend Micro Research. (2023, July 21). Ransomware Spotlight: Play. Retrieved September 24, 2024.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
- [Tomonaga, S. (2018, June 8). PLEAD Downloader Used by BlackTech. Retrieved May 6, 2020.](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Asheer Malhotra, Jungsoo An, Kendall Mc. (2022, May 5). Mustang Panda deploys a new wave of malware targeting Europe. Retrieved August 4, 2025.](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
- [Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
- [Raggi, M. et al. (2022, March 7). The Good, the Bad, and the Web Bug: TA416 Increases Operational Tempo Against European Governments as Conflict in Ukraine Escalates. Retrieved March 16, 2022.](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)
- [DOJ. (2024, December 20). Mag. No. 24-mj-1387 AFFIDAVIT IN SUPPORT OF AN APPLICATION FOR A NINTH SEARCH AND SEIZURE WARRANT- IN THE MATTER OF THE SEARCH AND SEIZURE OF COMPUTERS IN THE UNITED STATES INFECTED WITH PLUGX MALWARE . Retrieved September 9, 2025.](https://www.justice.gov/archives/opa/media/1384136/dl)
- [Secureworks Counter Threat Unit Research Team. (2022, September 8). BRONZE PRESIDENT Targets Government Officials. Retrieved September 9, 2025.](https://www.secureworks.com/blog/bronze-president-targets-government-officials)
- [Mercer, W, et al. (2020, April 16). PoetRAT: Python RAT uses COVID-19 lures to target Azerbaijan public and private sectors. Retrieved April 27, 2020.](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
- [Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
- [MSTIC. (2022, October 14). New “Prestige” ransomware impacts organizations in Ukraine and Poland. Retrieved January 19, 2023.](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
- [Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
- [Kasza, A. and Reichel, D. (2017, February 27). The Gamaredon Group Toolset Evolution. Retrieved March 1, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)
- [Nicolas Verdier. (n.d.). Retrieved January 29, 2018.](https://github.com/n1nj4sec/pupy)
- [Morrow, D. (2021, April 15). The rise of QakBot. Retrieved September 27, 2021.](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)
- [Magdy, S. et al. (2022, August 25). New Golang Ransomware Agenda Customizes Attacks. Retrieved September 26, 2025.](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
- [Trend Micro. (2025, October 23). Agenda Ransomware Deploys Linux Variant on Windows Systems Through Remote Management Tools and BYOVD Techniques. Retrieved March 26, 2026.](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)
- [Microsoft Threat Intelligence Center. (2022, February 4). ACTINIUM targets Ukrainian organizations. Retrieved February 18, 2022.](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
- [S2W TALON. (2022, June 16). Raccoon Stealer is Back with a New Version. Retrieved August 1, 2024.](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Antiy CERT. (2020, April 20). Analysis of Ramsay components of Darkhotel's infiltration and isolation network. Retrieved March 24, 2021.](https://www.programmersought.com/article/62493896999/)
- [Alfano, V. et al. (2025, February 12). RansomHub Never Sleeps Episode 1: The evolution of modern ransomware. Retrieved March 17, 2025.](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
- [Camba, A. (2013, February 27). BKDR_RARSTONE: New RAT to Watch Out For. Retrieved January 8, 2016.](http://blog.trendmicro.com/trendlabs-security-intelligence/bkdr_rarstone-new-rat-to-watch-out-for/)
- [Patrick Schläpfer . (2024, April 10). Raspberry Robin Now Spreading Through Windows Script Files. Retrieved May 17, 2024.](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
- [Nick Craig-Wood. (n.d.). Rclone syncs your files to cloud storage. Retrieved August 30, 2022.](https://rclone.org)
- [Antoniuk, D. (2023, July 17). RedCurl hackers return to spy on 'major Russian bank,' Australian company. Retrieved August 9, 2024.](https://therecord.media/redcurl-hackers-russian-bank-australian-company)
- [Group-IB. (2020, August). RedCurl: The Pentest You Didn’t Know About. Retrieved August 9, 2024.](https://www.group-ib.com/resources/research-hub/red-curl/)
- [Group-IB. (2021, November). RedCurl: The Awakening. Retrieved August 14, 2024.](https://www.group-ib.com/resources/research-hub/red-curl-2/)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [Klijnsma, Y. (2018, January 23). Espionage Campaign Leverages Spear Phishing, RATs Against Turkish Defense Contractors. Retrieved November 6, 2018.](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Legezo, D. (2019, January 30). Chafer used Remexi malware to spy on Iran-based foreign diplomatic entities. Retrieved April 17, 2019.](https://securelist.com/chafer-used-remexi-malware/89538/)
- [Peretz, A. and Theck, E. (2021, March 5). Earth Vetala – MuddyWater Continues to Target Organizations in the Middle East. Retrieved March 18, 2021.](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
- [Symantec Security Response. (2016, August 8). Backdoor.Remsec indicators of compromise. Retrieved August 17, 2016.](http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/Symantec_Remsec_IOCs.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Retrieved August 17, 2016.](https://securelist.com/files/2016/07/The-ProjectSauron-APT_research_KL.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
- [Mamedov, O, et al. (2019, July 3). Sodin ransomware exploits Windows vulnerability and processor architecture. Retrieved August 4, 2020.](https://securelist.com/sodin-ransomware/91473/)
- [Cylance. (2019, July 3). hreat Spotlight: Sodinokibi Ransomware. Retrieved August 4, 2020.](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
- [Secureworks . (2019, September 24). REvil: The GandCrab Connection. Retrieved August 4, 2020.](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
- [McAfee. (2019, October 2). McAfee ATR Analyzes Sodinokibi aka REvil Ransomware-as-a-Service – What The Code Tells Us. Retrieved August 4, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
- [Intel 471 Malware Intelligence team. (2020, March 31). REvil Ransomware-as-a-Service – An analysis of a ransomware affiliate operation. Retrieved August 4, 2020.](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [CISA. (2022, September 23). AA22-264A Iranian State Actors Conduct Cyber Operations Against the Government of Albania. Retrieved August 6, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
- [MSTIC. (2022, September 8). Microsoft investigates Iranian attacks against the Albanian government. Retrieved August 6, 2024.](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)
- [GReAT. (2019, May 13). ScarCruft continues to evolve, introduces Bluetooth harvester. Retrieved June 4, 2019.](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)
- [Pantazopoulos, N.. (2018, November 8). RokRat Analysis. Retrieved May 21, 2020.](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
- [Cash, D., Grunzweig, J., Adair, S., Lancaster, T. (2021, August 25). North Korean BLUELIGHT Special: InkySquid Deploys RokRAT. Retrieved October 1, 2021.](https://www.volexity.com/blog/2021/08/24/north-korean-bluelight-special-inkysquid-deploys-rokrat/)
- [Ray, V., Hayashi, K. (2016, February 29). New Malware ‘Rover’ Targets Indian Ambassador to Afghanistan. Retrieved February 29, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
- [Cybereason Global SOC and Cybereason Security Research Teams. (2022, December 14). Royal Rumble: Analysis of Royal Ransomware. Retrieved March 30, 2023.](https://www.cybereason.com/blog/royal-ransomware-analysis)
- [Iacono, L. and Green, S. (2023, February 13). Royal Ransomware Deep Dive. Retrieved March 30, 2023.](https://www.kroll.com/en/insights/publications/cyber/royal-ransomware-deep-dive)
- [Morales, N. et al. (2023, February 20). Royal Ransomware Expands Attacks by Targeting Linux ESXi Servers. Retrieved March 30, 2023.](https://www.trendmicro.com/en_us/research/23/b/royal-ransomware-expands-attacks-by-targeting-linux-esxi-servers.html)
- [Duncan, B., Harbison, M. (2019, January 23). Russian Language Malspam Pushing Redaman Banking Malware. Retrieved June 16, 2020.](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
- [Hanel, A. (2019, January 10). Big Game Hunting with Ryuk: Another Lucrative Targeted Ransomware. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
- [FBI Cyber Division. (2025, September 12). Cyber Criminal Groups UNC6040 and UNC6395 Compromising Salesforce Instances for Data Theft and Extortion. Retrieved October 22, 2025.](https://www.ic3.gov/CSA/2025/250912.pdf)
- [Check Point. (2024, November 12). Hamas-affiliated Threat Actor WIRTE Continues its Middle East Operations and Moves to Disruptive Activity. Retrieved April 20, 2026.](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
- [Joe Slowik. (2018, October 12). Anatomy of an Attack: Detecting and Defeating CRASHOVERRIDE. Retrieved December 18, 2020.](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)
- [CISA. (2023, November 16). Cybersecurity Advisory: Scattered Spider (AA23-320A). Retrieved March 18, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)
- [Microsoft. (2023, October 25). Octo Tempest crosses boundaries to facilitate extortion, encryption, and destruction. Retrieved March 18, 2024.](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/)
- [Mandiant Incident Response. (2025, May 6). Defending Against UNC3944: Cybercrime Hardening Guidance from the Frontlines. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)
- [Counter Adversary Operations. (2025, July 2). CrowdStrike Services Observes SCATTERED SPIDER Escalate Attacks Across Industries. Retrieved October 13, 2025.](https://www.crowdstrike.com/en-us/blog/crowdstrike-services-observes-scattered-spider-escalate-attacks/)
- [Mandiant Incident Response. (2025, July 23). From Help Desk to Hypervisor: Defending Your VMware vSphere Estate from UNC3944. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)
- [Schwarz, D. et al. (2019, October 16). TA505 Distributes New SDBbot Remote Access Trojan with Get2 Downloader. Retrieved May 29, 2020.](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
- [Microsoft Threat Intelligence. (2025, July 22). Disrupting active exploitation of on-premises SharePoint vulnerabilities. Retrieved October 15, 2025.](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/#storm-2603)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Falcone, R. and Wartell, R.. (2015, July 27). Observations on CVE-2015-3113, Prior Zero-Days and the Pirpi Payload. Retrieved January 22, 2016.](http://researchcenter.paloaltonetworks.com/2015/07/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [Hegel, T. (2021, January 13). A Global Perspective of the SideWinder APT. Retrieved January 27, 2021.](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [Prizmant, D. (2021, June 7). Siloscape: First Known Malware Targeting Windows Containers to Compromise Cloud Environments. Retrieved June 9, 2021.](https://unit42.paloaltonetworks.com/siloscape/)
- [Remillano, A., Urbanec, J. (2019, September 19). Skidmap Linux Malware Uses Rootkit Capabilities to Hide Cryptocurrency-Mining Payload. Retrieved June 4, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
- [BishopFox. (2021, August 18). Sliver Filesystem. Retrieved September 22, 2021.](https://github.com/BishopFox/sliver/tree/master/client/command/filesystem)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [Baker, B., Unterbrink H. (2018, July 03). Smoking Guns - Smoke Loader learned new tricks. Retrieved July 5, 2018.](https://blog.talosintelligence.com/2018/07/smoking-guns-smoke-loader-learned-new.html#more)
- [Cash, D. et al. (2020, December 14). Dark Halo Leverages SolarWinds Compromise to Breach Organizations. Retrieved December 29, 2020.](https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [CISA. (2020, July 16). MAR-10296782-1.v1 – SOREFANG. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
- [Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
- [Symantec Security Response. (2017, November 7). Sowbug: Cyber espionage group targets South American and Southeast Asian governments. Retrieved November 16, 2017.](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)
- [Shields, W. (2024, January 18). Russian threat group COLDRIVER expands its targeting of Western officials to include the use of malware. Retrieved June 13, 2024.](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: PAKLOG, CorKLOG, and SplatCloak | P2. Retrieved September 12, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
- [Cybereason Global SOC Team. (n.d.). THREAT ANALYSIS REPORT: Inside the LockBit Arsenal - The StealBit Exfiltration Tool. Retrieved January 29, 2025.](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
- [Cylance SPEAR Team. (2017, February 9). Shell Crew Variants Continue to Fly Under Big AV’s Radar. Retrieved February 15, 2017.](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)
- [Cybereason Nocturnus. (2022, February 1). StrifeWater RAT: Iranian APT Moses Staff Adds New Trojan to Ransomware Operations. Retrieved August 15, 2022.](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
- [Mercer, W. et al. (2020, June 29). PROMETHIUM extends global reach with StrongPity3 APT. Retrieved July 20, 2020.](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [Mandiant Israel Research Team. (2022, August 17). Suspected Iranian Actor Targeting Israeli Shipping, Healthcare, Government and Energy Sectors. Retrieved September 21, 2022.](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [MSTIC. (2020, December 18). Analyzing Solorigate, the compromised DLL file that started a sophisticated cyberattack, and how Microsoft Defender helps protect customers . Retrieved January 5, 2021.](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)
- [CrowdStrike Intelligence Team. (2021, January 11). SUNSPOT: An Implant in the Build Process. Retrieved January 11, 2021.](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
- [Ivanov, A. et al. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
- [Bettencourt, J. (2018, May 7). Kaspersky Lab finds new variant of SynAck ransomware using sophisticated Doppelgänging technique. Retrieved May 24, 2018.](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)
- [Lunghi, D. and Lu, K. (2021, April 9). Iron Tiger APT Updates Toolkit With Evolved SysUpdate Malware. Retrieved November 12, 2021.](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
- [Daniel Lunghi. (2023, March 1). Iron Tiger’s SysUpdate Reappears, Adds Linux Targeting. Retrieved March 20, 2023.](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
- [CISA, FBI, DOD. (2021, August). MAR-10292089-1.v2 – Chinese Remote Access Trojan: TAIDOOR. Retrieved August 24, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
- [USG. (2020, May 12). MAR-10288834-2.v1 – North Korean Trojan: TAINTEDSCRIBE. Retrieved March 5, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle. Retrieved October 27, 2021.](https://securelist.com/lazarus-threatneedle/100803/)
- [Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
- [Anthony, N., Pascual, C.. (2018, November 1). Trickbot Shows Off New Trick: Password Grabber Module. Retrieved November 16, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)
- [Secureworks. (2019, July 24). Updated Karagany Malware Targets Energy Sector. Retrieved August 12, 2020.](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
- [Jiho Kim & Sebin Lee, S2W. (2024, February 7). Kimsuky disguised as a Korean company signed with a valid certificate to distribute Troll Stealer (English ver.). Retrieved January 17, 2025.](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Chris Traynor. (2024, January 18). Rooting For Secrets with TruffleHog. Retrieved April 15, 2026.](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)
- [Gianpietro Cutolo. (2025, November 26). Shai-Hulud 2.0: Aggressive, Automated, and Fast Spreading. Retrieved April 9, 2026.](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
- [Trufflesecurity. (2026, April 8). TruffleHog Enterprise. Retrieved April 15, 2026.](https://github.com/trufflesecurity/trufflehog)
- [Tomonaga, S. (2018, March 6). Malware “TSCookie”. Retrieved May 6, 2020.](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
- [Adam Burgher. (2021, June 10). BackdoorDiplomacy: Upgrading from Quarian to Turian. Retrieved September 1, 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [US-CERT. (2018, June 14). MAR-10135536-12 – North Korean Trojan: TYPEFRAME. Retrieved July 13, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
- [Alexander Marvi, Jeremy Koppen, Tufail Ahmed, and Jonathan Lepore. (2022, September 29). Bad VIB(E)s Part One: Investigating Novel Malware Persistence Within ESXi Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
- [Alexander Marvi, Brad Slaybaugh, Ron Craft, and Rufus Brown. (2023, June 13). VMware ESXi Zero-Day Used by Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)
- [Matsuda, A., Muhammad I. (2018, September 13). APT10 Targeting Japanese Corporations Using Updated TTPs. Retrieved September 17, 2018.](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Calvet, J. (2014, November 11). Sednit Espionage Group Attacking Air-Gapped Networks. Retrieved January 4, 2017.](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
- [Kaspersky Lab's Global Research and Analysis Team. (2015, December 4). Sofacy APT hits high profile targets with updated toolset. Retrieved December 10, 2015.](https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/)
- [Sygnia Team. (2024, June 3). China-Nexus Threat Group ‘Velvet Ant’ Abuses F5 Load Balancers for Persistence. Retrieved March 14, 2025.](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
- [US-CERT. (2017, November 22). Alert (TA17-318B): HIDDEN COBRA – North Korean Trojan: Volgmer. Retrieved December 7, 2017.](https://www.us-cert.gov/ncas/alerts/TA17-318B)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Noerenberg, E., Costis, A., and Quist, N. (2017, May 16). A Technical Analysis of WannaCry Ransomware. Retrieved December 8, 2024.](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)
- [Berry, A., Homan, J., and Eitzman, R. (2017, May 23). WannaCry Malware Profile. Retrieved March 15, 2019.](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [Antenucci, S., Pantazopoulos, N., Sandee, M. (2020, June 23). WastedLocker: A New Ransomware Variant Developed By The Evil Corp Group. Retrieved September 14, 2021.](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
- [MSTIC. (2022, January 15). Destructive malware targeting Ukrainian organizations. Retrieved March 10, 2022.](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)
- [Falcone, R. et al.. (2022, January 20). Threat Brief: Ongoing Russia and Ukraine Cyber Conflict. Retrieved March 10, 2022.](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)
- [Biasini, N. et al.. (2022, January 21). Ukraine Campaign Delivers Defacement and Wipers, in Continued Escalation. Retrieved March 14, 2022.](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
- [S2W. (2022, January 18). Analysis of Destructive Malware (WhisperGate) targeting Ukraine. Retrieved March 14, 2022.](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [Wardle, Patrick. (2018, December 20). Middle East Cyber-Espionage analyzing WindShift's implant: OSX.WindTail (part 1). Retrieved October 3, 2019.](https://objective-see.com/blog/blog_0x3B.html)
- [Wardle, Patrick. (2019, January 15). Middle East Cyber-Espionage analyzing WindShift's implant: OSX.WindTail (part 2). Retrieved October 3, 2019.](https://objective-see.com/blog/blog_0x3D.html)
- [Baumgartner, K., Golovkin, M.. (2015, May). The MsnMM Campaigns: The Earliest Naikon APT Campaigns. Retrieved April 10, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
- [Novetta Threat Research Group. (2015, April 7). Winnti Analysis. Retrieved February 8, 2017.](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
- [Kaspersky Lab's Global Research and Analysis Team. (2013, April 11). Winnti. More than just a game. Retrieved February 8, 2017.](https://securelist.com/winnti-more-than-just-a-game/37029/)
- [Matthieu Faou. (2023, October 25). Winter Vivern exploits zero-day vulnerability in Roundcube Webmail servers. Retrieved July 29, 2024.](https://www.welivesecurity.com/en/eset-research/winter-vivern-exploits-zero-day-vulnerability-roundcube-webmail-servers/)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Robert Falcone. (2017, February 14). XAgentOSX: Sofacy's Xagent macOS Tool. Retrieved July 12, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)
- [Brandon Dalton. (2022, August 9). A bundle of nerves: Tweaking macOS security controls to thwart application bundle manipulation. Retrieved September 27, 2022.](https://redcanary.com/blog/mac-application-bundles/)
- [Microsoft Threat Intelligence. (2025, March 11). New XCSSET malware adds new obfuscation, persistence techniques to infect Xcode projects. Retrieved April 2, 2025.](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)
- [Schwarz, D., Sopko J. (2018, March 08). Donot Team Leverages New Modular Malware Framework in South Asia. Retrieved June 11, 2018.](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, February 20). A Slice of 2017 Sofacy Activity. Retrieved November 27, 2018.](https://securelist.com/a-slice-of-2017-sofacy-activity/83930/)
- [ESET. (2018, November 20). Sednit: What’s going on with Zebrocy?. Retrieved February 12, 2019.](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
- [ESET Research. (2019, May 22). A journey to Zebrocy land. Retrieved June 20, 2019.](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
- [Accenture Security. (2018, November 29). SNAKEMACKEREL. Retrieved April 15, 2019.](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
- [CISA. (2020, October 29). Malware Analysis Report (AR20-303B). Retrieved December 9, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
- [Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
- [McLellan, T. et al. (2024, January 12). Cutting Edge: Suspected APT Targets Ivanti Connect Secure VPN in New Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
- [Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)

---

# Native API

## Description

Adversaries may interact with the native OS application programming interface (API) to execute behaviors. Native APIs provide a controlled means of calling low-level OS services within the kernel, such as those involving hardware/devices, memory, and processes. [1] [2] These native APIs are leveraged by the OS during system boot (when other system components are not yet initialized) as well as carrying out tasks and requests during routine operations.

Adversaries may abuse these OS API functions as a means of executing behaviors. Similar to Command and Scripting Interpreter , the native API and its hierarchy of interfaces provide mechanisms to interact with and utilize various components of a victimized system.

Native API functions (such as NtCreateProcess ) may be directed invoked via system calls / syscalls, but these features are also often exposed to user-mode applications via interfaces and libraries. [3] [4] [5] For example, functions such as the Windows API CreateProcess() or GNU fork() will allow programs and scripts to start other processes. [6] [7] This may allow API callers to execute a binary, run a CLI command, load modules, etc. as thousands of similar API functions exist for various system operations. [8] [9] [10]

Higher level software frameworks, such as Microsoft .NET and macOS Cocoa, are also available to interact with native APIs. These frameworks typically provide language wrappers/abstractions to API functionalities and are designed for ease-of-use/portability of code. [11] [12] [13] [14]

Adversaries may use assembly to directly or in-directly invoke syscalls in an attempt to subvert defensive sensors and detection signatures such as user mode API-hooks. [15] Adversaries may also attempt to tamper with sensors and defensive tools associated with API monitoring, such as unhooking monitored functions via Disable or Modify Tools .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0045 | ADVSTORESHELL | ADVSTORESHELL is capable of starting a process using CreateProcess. [16] |
| S1129 | Akira | Akira executes native Windows functions such as GetFileAttributesW and GetSystemInfo . [17] |
| S1025 | Amadey | Amadey has used a variety of Windows API calls, including GetComputerNameA , GetUserNameA , and CreateProcessA . [18] |
| S9027 | ANELLDR | ANELLDR can use the ZwSetInformationThread to enable debugger evasion. [19] |
| S0622 | AppleSeed | AppleSeed has the ability to use multiple dynamically resolved API calls. [20] |
| G0067 | APT37 | APT37 leverages the Windows API calls: VirtualAlloc(), WriteProcessMemory(), and CreateRemoteThread() for process injection. [21] |
| G0082 | APT38 | APT38 has used the Windows API to execute code within a victim's system. [22] |
| S0456 | Aria-body | Aria-body has the ability to launch files using ShellExecute . [23] |
| S1087 | AsyncRAT | AsyncRAT has the ability to use OS APIs including CheckRemoteDebuggerPresent . [24] |
| S0438 | Attor | Attor 's dispatcher has used CreateProcessW API for execution. [25] |
| S0640 | Avaddon | Avaddon has used the Windows Crypto API to generate an AES key. [26] |
| S1053 | AvosLocker | AvosLocker has used a variety of Windows API calls, including NtCurrentPeb and GetLogicalDrives . [27] |
| S0638 | Babuk | Babuk can use multiple Windows API calls for actions on compromised hosts including discovery and execution. [28] [29] [30] |
| S0475 | BackConfig | BackConfig can leverage API functions such as ShellExecuteA and HttpOpenRequestA in the process of downloading and executing files. [31] |
| S0606 | Bad Rabbit | Bad Rabbit has used various Windows API calls. [32] |
| S1081 | BADHATCH | BADHATCH can utilize Native API functions such as, ToolHelp32 and Rt1AdjustPrivilege to enable SeDebugPrivilege on a compromised machine. [33] |
| S0128 | BADNEWS | BADNEWS has a command to download an .exe and execute it via CreateProcess API. It can also run with ShellExecute. [34] [35] |
| S0234 | Bandook | Bandook has used the ShellExecuteW() function call. [36] |
| S0239 | Bankshot | Bankshot creates processes using the Windows API calls: CreateProcessA() and CreateProcessAsUserA(). [37] |
| S0534 | Bazar | Bazar can use various APIs to allocate memory and facilitate code execution/injection. [38] |
| S0470 | BBK | BBK has the ability to use the CreatePipe API to add a sub-process for execution via cmd . [39] |
| S0574 | BendyBear | BendyBear can load and execute modules and Windows Application Programming (API) calls using standard shellcode API hashing. [40] |
| S0268 | Bisonal | Bisonal has used the Windows API to communicate with the Service Control Manager to execute a thread. [41] |
| S0570 | BitPaymer | BitPaymer has used dynamic API resolution to avoid identifiable strings within the binary, including RegEnumKeyW . [42] |
| S1070 | Black Basta | Black Basta has the ability to use native APIs for numerous functions including discovery and defense evasion. [43] [44] [45] [46] [47] |
| S1180 | BlackByte Ransomware | BlackByte Ransomware uses the SetThreadExecutionState API to prevent the victim system from entering sleep. [48] |
| G0098 | BlackTech | BlackTech has used built-in API functions. [49] |
| S0521 | BloodHound | BloodHound can use .NET API calls in the SharpHound ingestor component to pull Active Directory data. [50] |
| S1226 | BOOKWORM | BOOKWORM has used various Windows API calls during execution and defense evasion. [51] [52] BOOKWORM has created a buffer on the heap using HeapCreate and HeapAlloc which allows for copying of shell code and then execution on the heap is initiated through callback function of legitimate API functions such as EnumChildWindows or EnumSystemLanguageGroupsA . [52] |
| S0651 | BoxCaon | BoxCaon has used Windows API calls to obtain information about the compromised host. [53] |
| S1063 | Brute Ratel C4 | Brute Ratel C4 can call multiple Windows APIs for execution, to share memory, and defense evasion. [54] [55] |
| S0471 | build_downer | build_downer has the ability to use the WinExec API to execute malware on a compromised host. [39] |
| S1039 | Bumblebee | Bumblebee can use multiple Native APIs. [56] [57] |
| S0693 | CaddyWiper | CaddyWiper has the ability to dynamically resolve and use APIs, including SeTakeOwnershipPrivilege . [58] |
| S9016 | Caminho | Caminho can use System.Net.WebClient.downloadString() for file download. [59] |
| S1237 | CANONSTAGER | CANONSTAGER has leveraged Native API calls to execute code within the victim’s system including GetCurrentDirectoryW , RegisterClassW and CreateWindowExW . [60] CANONSTAGER also created a new overlapped window that initiates callback functions to a windows procedure that processes Windows messages until a designated message type of 0x0018 WM_SHOWWINDOW is observed which then initiates the deployment of a subsequent malicious payload. [60] |
| S0484 | Carberp | Carberp has used the NtQueryDirectoryFile and ZwQueryDirectoryFile functions to hide files and directories. [61] |
| S0631 | Chaes | Chaes used the CreateFileW() API function with read permissions to access downloaded payloads. [62] |
| G0114 | Chimera | Chimera has used direct Windows system calls by leveraging Dumpert. [63] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP can use Windows APIs including LoadLibrary and GetProcAddress . [64] |
| S0667 | Chrommme | Chrommme can use Windows API including WinExec for execution. [65] |
| S1236 | CLAIMLOADER | CLAIMLOADER has used various Windows API calls during execution, when establishing persistence and defense evasion. [66] [67] CLAIMLOADER has also leveraged the legitimate API functions to run its shellcode through the callback function, including GetDC() and EnumFontsW() . [66] CLAIMLOADER established persistence by utilizing the API SHSetValue() . [66] CLAIMLOADER has utilized APIs with callback functions such as EnumpropsExW , EnumSystemLanguageGroupsA , and EnumCalendarInfoExW . [67] |
| S0611 | Clop | Clop has used built-in API functions such as WNetOpenEnumW(), WNetEnumResourceW(), WNetCloseEnum(), GetProcAddress(), and VirtualAlloc(). [68] [69] |
| S0154 | Cobalt Strike | Cobalt Strike 's Beacon payload is capable of running shell commands without cmd.exe and PowerShell commands without powershell.exe [70] [71] [72] Cobalt Strike can also use CreateThreadpoolWait , SetThreadpoolWait , and MessageBoxA for sandbox evasion and execution of embedded payloads in memory. [73] |
| S0126 | ComRAT | ComRAT can load a PE file from memory or the file system and execute it with CreateProcessW . [74] |
| S0575 | Conti | Conti has used API calls during execution. [75] [76] |
| S0614 | CostaBricks | CostaBricks has used a number of API calls, including VirtualAlloc , VirtualFree , LoadLibraryA , GetProcAddress , and ExitProcess . [77] |
| S0625 | Cuba | Cuba has used several built-in API functions for discovery like GetIpNetTable and NetShareEnum. [78] |
| S0687 | Cyclops Blink | Cyclops Blink can use various Linux API functions including those for execution and discovery. [79] |
| S1111 | DarkGate | DarkGate uses the native Windows API CallWindowProc() to decode and launch encoded shellcode payloads during execution. [80] DarkGate can call kernel mode functions directly to hide the use of process hollowing methods during execution. [81] DarkGate has also used the CreateToolhelp32Snapshot , GetFileAttributesA and CreateProcessA functions to obtain a list of running processes, to check for security products and to execute its malware. [82] |
| S1066 | DarkTortilla | DarkTortilla can use a variety of API calls for persistence and defense evasion. [83] |
| S1033 | DCSrv | DCSrv has used various Windows API functions, including DeviceIoControl , as part of its encryption process. [84] |
| S1052 | DEADEYE | DEADEYE can execute the GetComputerNameA and GetComputerNameExA WinAPI functions. [85] |
| S0354 | Denis | Denis used the IsDebuggerPresent , OutputDebugString , and SetLastError APIs to avoid debugging. Denis used GetProcAddress and LoadLibrary to dynamically resolve APIs. Denis also used the Wow64SetThreadContext API as part of a process hollowing process. [86] |
| S0659 | Diavol | Diavol has used several API calls like GetLogicalDriveStrings , SleepEx , SystemParametersInfoAPI , CryptEncrypt , and others to execute parts of its attack. [87] |
| S0695 | Donut | Donut code modules use various API functions to load and inject code. [88] |
| S9021 | DOWNIISSA | DOWNIISSA can use the URLDownloadToFileA() API to download from remote resources. [89] |
| S0694 | DRATzarus | DRATzarus can use various API calls to see if it is running in a sandbox. [90] |
| S0384 | Dridex | Dridex has used the OutputDebugStringW function to avoid malware analysis as part of its anti-debugging technique. [91] |
| S9038 | DynoWiper | DynoWiper has used multiple native Windows functions, such as GetLogicalDrives and FindNextFile for discovery and file deletion. [92] [93] |
| S0554 | Egregor | Egregor has used the Windows API to make detection more difficult. [94] |
| S1247 | Embargo | Embargo has leveraged Windows Native API functions to execute its operations. [95] |
| S0367 | Emotet | Emotet has used CreateProcess to create a new process to run its executable and WNetEnumResourceW to enumerate non-hidden shares. [96] |
| S0363 | Empire | Empire contains a variety of enumeration modules that have an option to use API calls to carry out tasks. [97] |
| S0396 | EvilBunny | EvilBunny has used various API calls as part of its checks to see if the malware is running in a sandbox. [98] |
| S1179 | Exbyte | Exbyte calls ShellExecuteW with the IpOperation parameter RunAs to launch explorer.exe with elevated privileges. [99] |
| S0569 | Explosive | Explosive has a function to call the OpenClipboard wrapper. [100] |
| S0512 | FatDuke | FatDuke can call ShellExecuteW to open the default browser on the URL localhost. [101] |
| S0696 | Flagpro | Flagpro can use Native API to enable obfuscation including GetLastError and GetTickCount . [102] |
| S0661 | FoggyWeb | FoggyWeb 's loader can use API functions to load the FoggyWeb backdoor into the same Application Domain within which the legitimate AD FS managed code is executed. [103] |
| S9033 | Fooder | Fooder has used the WinCrypt API for payload decryption, DuplicateTokenEx to duplicate the token of a specified process, and CreateProcessAsUserA for payload execution. [104] |
| S1044 | FunnyDream | FunnyDream can use Native API for defense evasion, discovery, and collection. [105] |
| G0047 | Gamaredon Group | Gamaredon Group malware has used CreateProcess to launch additional malicious components. [106] [107] |
| S0666 | Gelsemium | Gelsemium has the ability to use various Windows API functions to perform tasks. [65] |
| S0032 | gh0st RAT | gh0st RAT has used the InterlockedExchange , SeShutdownPrivilege , and ExitWindowsEx Windows API functions. [108] |
| S0493 | GoldenSpy | GoldenSpy can execute remote commands in the Windows command shell using the WinExec() API. [109] |
| S0477 | Goopy | Goopy has the ability to enumerate the infected system's user name via GetUserNameW . [86] |
| G0078 | Gorgon Group | Gorgon Group malware can leverage the Windows API call, CreateProcessA(), for execution. [110] |
| S0531 | Grandoreiro | Grandoreiro can execute through the WinExec API. [111] |
| S0632 | GrimAgent | GrimAgent can use Native API including GetProcAddress and ShellExecuteW . [112] |
| S0561 | GuLoader | GuLoader can use a number of different APIs for discovery and execution. [113] |
| S0499 | Hancitor | Hancitor has used CallWindowProc and EnumResourceTypesA to interpret and execute shellcode. [114] |
| S1229 | Havoc | Havoc can use NtAllocateVirtualMemory and NtCreateThreadEx to aid process injection. [115] |
| S0391 | HAWKBALL | HAWKBALL has leveraged several Windows API calls to create processes, gather disk information, and detect debugger activity. [116] |
| S9018 | HeartCrypt | HeartCrypt can use Windows API functions to modify the Registry and FindResourceW , LoadResource , and LockResource to acquire a pointer to corresponding code resources. [117] |
| S0697 | HermeticWiper | HermeticWiper can call multiple Windows API functions used for privilege escalation, service execution, and to overwrite random bites of data. [118] [119] [120] [121] |
| S0698 | HermeticWizard | HermeticWizard can connect to remote shares using WNetAddConnection2W . [120] |
| G0126 | Higaisa | Higaisa has called various native OS APIs. [122] |
| S0431 | HotCroissant | HotCroissant can perform dynamic DLL importing and API lookups using LoadLibrary and GetProcAddress on obfuscated strings. [123] |
| S9007 | HTTPTroy | HTTPTroy has leveraged Windows Native API calls, including GetProcAddress to execute functions in memory. [124] |
| S0398 | HyperBro | HyperBro has the ability to run an application ( CreateProcessW ) or script/file ( ShellExecuteW ) via API. [125] |
| S0537 | HyperStack | HyperStack can use Windows API's ConnectNamedPipe and WNetAddConnection2 to detect incoming connections and connect to remote shares. [126] |
| S0483 | IcedID | IcedID has called ZwWriteVirtualMemory , ZwProtectVirtualMemory , ZwQueueApcThread , and NtResumeThread to inject itself into a remote process. [127] |
| S1152 | IMAPLoader | IMAPLoader imports native Windows APIs such as GetConsoleWindow and ShowWindow . [128] |
| S0434 | Imminent Monitor | Imminent Monitor has leveraged CreateProcessW() call to execute the debugger. [129] |
| S1139 | INC Ransomware | INC Ransomware can use the API DeviceIoControl to resize the allocated space for and cause the deletion of volume shadow copy snapshots. [130] |
| S0259 | InnaputRAT | InnaputRAT uses the API call ShellExecuteW for execution. [131] |
| S0260 | InvisiMole | InvisiMole can use winapiexec tool for indirect execution of ShellExecuteW and CreateProcessA . [132] |
| S1190 | Kapeka | Kapeka utilizes WinAPI calls to gather victim system information. [133] |
| S1020 | Kevin | Kevin can use the ShowWindow API to avoid detection. [134] |
| S0607 | KillDisk | KillDisk has called the Windows API to retrieve the hard disk handle and shut down the machine. [135] |
| G0094 | Kimsuky | Kimsuky has utilized Native APIs to collect data from victim hosts and facilitate execution of malicious scripts. [124] [136] |
| S0669 | KOCTOPUS | KOCTOPUS can use the LoadResource and CreateProcessW APIs for execution. [137] |
| S0356 | KONNI | KONNI has hardcoded API calls within its functions to use on the victim's machine. [138] |
| S1160 | Latrodectus | Latrodectus has used multiple Windows API post exploitation including GetAdaptersInfo , CreateToolhelp32Snapshot , and CreateProcessW . [139] [140] |
| G0032 | Lazarus Group | Lazarus Group has used the Windows API ObtainUserAgentString to obtain the User-Agent from a compromised host to connect to a C2 server. [141] Lazarus Group has also used various, often lesser known, functions to perform various types of Discovery and Process Injection . [142] [143] |
| S0395 | LightNeuron | LightNeuron is capable of starting a process using CreateProcess. [144] |
| S0680 | LitePower | LitePower can use various API calls. [145] |
| S0681 | Lizar | Lizar has used various Windows API functions on a victim's machine. [146] |
| S1202 | LockBit 3.0 | LockBit 3.0 has the ability to directly call native Windows API items during execution. [147] [148] |
| S9020 | LODEINFO | LODEINFO can use Windows APIs such as VirtualAllocEx() , WriteProcessMemory() , CreateRemoteThread() , NtAllocateVirtualMemory() , NtWriteVirtualMemory() , and RtlCreateUserThread() to enable memory injection of shellcode. [149] |
| S0447 | Lokibot | Lokibot has used LoadLibrary(), GetProcAddress() and CreateRemoteThread() API functions to execute its shellcode. [150] |
| S9036 | LP-Notes | LP-Notes has used the ImpersonateLoggedOnUser API to impersonate the security context of the taskhostw.exe process. [104] Additionally, LP-Notes has also used the CredUIPromptForWindowsCredentialsW API to obtain Windows credentials. [104] |
| S1016 | MacMa | MacMa has used macOS API functions to perform tasks. [151] [152] |
| S1060 | Mafalda | Mafalda can use a variety of API calls. [153] |
| S1169 | Mango | Mango has the ability to use Native APIs. [154] |
| S0652 | MarkiRAT | MarkiRAT can run the ShellExecuteW API via the Windows Command Shell. [155] |
| S0449 | Maze | Maze has used several Windows API functions throughout the encryption process including IsDebuggerPresent, TerminateProcess, Process32FirstW, among others. [156] |
| G1051 | Medusa Group | Medusa Group has leveraged Windows Native API functions to execute payloads. [157] |
| S1244 | Medusa Ransomware | Medusa Ransomware has leveraged Windows Native API functions to execute payloads. [157] |
| S0576 | MegaCortex | After escalating privileges, MegaCortex calls TerminateProcess() , CreateRemoteThread , and other Win32 APIs. [158] |
| G0045 | menuPass | menuPass has used native APIs including GetModuleFileName , lstrcat , CreateFile , and ReadFile . [159] |
| S1059 | metaMain | metaMain can execute an operator-provided Windows command by leveraging functions such as WinExec , WriteFile , and ReadFile . [153] [160] |
| S0455 | Metamorfo | Metamorfo has used native WINAPI calls. [161] [162] |
| S0688 | Meteor | Meteor can use WinAPI to remove a victim machine from an Active Directory domain. [163] |
| S1015 | Milan | Milan can use the API DnsQuery_A for DNS resolution. [134] |
| S0084 | Mis-Type | Mis-Type has used Windows API calls, including NetUserAdd and NetUserDel . [164] |
| S0083 | Misdat | Misdat has used Windows APIs, including ExitWindowsEx and GetKeyboardType . [164] |
| S1122 | Mispadu | Mispadu has used a variety of Windows API calls, including ShellExecute and WriteProcessMemory. [165] [166] |
| S0256 | Mosquito | Mosquito leverages the CreateProcess() and LoadLibrary() calls to execute files with the .dll and .exe extensions. [167] |
| S9032 | MuddyViper | MuddyViper has the ability to relaunch itself using the CreateProcessW API. [104] |
| G0129 | Mustang Panda | Mustang Panda has used various Windows API calls during execution and defense evasion. [168] [51] [169] [66] [67] [170] [171] [60] [52] [172] [173] [174] |
| S0630 | Nebulae | Nebulae has the ability to use CreateProcess to execute a process. [175] |
| S0457 | Netwalker | Netwalker can use Windows API functions to inject the ransomware DLL. [176] |
| S0198 | NETWIRE | NETWIRE can use Native API including CreateProcess GetProcessById , and WriteProcessMemory . [177] |
| S1090 | NightClub | NightClub can use multiple native APIs including GetKeyState , GetForegroundWindow , GetWindowThreadProcessId , and GetKeyboardLayout . [178] |
| S1100 | Ninja | The Ninja loader can call Windows APIs for discovery, process injection, and payload decryption. [179] [180] |
| S0385 | njRAT | njRAT has used the ShellExecute() function within a script. [181] |
| S9025 | NOOPLDR | NOOPLDR can use native APIs NtProtectVirtualMemory , NtWriteVirtualMemory , and NtCreateThreadEx to aid process injection. [182] |
| S1170 | ODAgent | ODAgent can pass commands using native APIs. [183] |
| S1172 | OilBooster | OilBooster has used the ShowWindow and CreateProcessW APIs. [183] |
| C0061 | Operation Digital Eye | During Operation Digital Eye , threat actors used native API such as GetUserInfo . [184] |
| C0022 | Operation Dream Job | During Operation Dream Job , Lazarus Group used Windows API ObtainUserAgentString to obtain the victim's User-Agent and used the value to connect to their C2 server. [141] |
| C0006 | Operation Honeybee | During Operation Honeybee , the threat actors deployed malware that used API calls, including CreateProcessAsUser . [185] |
| C0013 | Operation Sharpshooter | During Operation Sharpshooter , the first stage downloader resolved various Windows libraries and APIs, including LoadLibraryA() , GetProcAddress() , and CreateProcessA() . [186] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors used the CreateProcessA and ShellExecute API functions to launch commands after being injected into a selected process. [187] |
| S1233 | PAKLOG | PAKLOG has used Windows API SetWindowsHookExW with idHook set to WH_KEYBOARD_LL and a custom hook procedure to support its keylogging functions. [173] |
| S1050 | PcShare | PcShare has used a variety of Windows API functions. [105] |
| S1145 | Pikabot | Pikabot uses native Windows APIs to determine if the process is being debugged and analyzed, such as CheckRemoteDebuggerPresent , NtQueryInformationProcess , ProcessDebugPort , and ProcessDebugFlags . [188] Other Pikabot variants populate a global list of Windows API addresses from the NTDLL and KERNEL32 libraries, and references these items instead of calling the API items to obfuscate execution. [189] |
| S0517 | Pillowmint | Pillowmint has used multiple native Windows APIs to execute and conduct process injections. [190] |
| S0501 | PipeMon | PipeMon 's first stage has been executed by a call to CreateProcess with the decryption password in an argument. PipeMon has used a call to LoadLibrary to load its installer. [191] |
| S0435 | PLEAD | PLEAD can use ShellExecute to execute applications. [192] |
| S0013 | PlugX | PlugX can use the Windows API functions GetProcAddress , LoadLibrary , and CreateProcess to execute another process. [168] [193] [194] |
| S0518 | PolyglotDuke | PolyglotDuke can use LoadLibraryW and CreateProcess to load and execute code. [101] |
| S0453 | Pony | Pony has used several Windows functions for various purposes. [195] |
| S1058 | Prestige | Prestige has used the Wow64DisableWow64FsRedirection() and Wow64RevertWow64FsRedirection() functions to disable and restore file system redirection. [196] |
| S0147 | Pteranodon | Pteranodon has used various API calls. [197] |
| S1228 | PUBLOAD | PUBLOAD has used various Windows API calls during execution, when establishing persistence and defense evasion. [169] [67] PUBLOAD stager leveraged Windows API functions with callback including GrayStringW , EnumDateFormatsA , and LineDDA to bypass anti-virus monitoring. [171] PUBLOAD has also utilized other native windows API functions with callback functions such as EnumChildWindows and EnumSystemLanguageGroupsA . [52] |
| S0650 | QakBot | QakBot can use GetProcAddress to help delete malicious strings from memory. [198] |
| S1242 | Qilin | Qilin can attempt to log on to the local computer via LogonUserW and use GetLogicalDrives() and EnumResourceW() for discovery. [199] [200] |
| S1076 | QUIETCANARY | QUIETCANARY can call System.Net.HttpWebRequest to identify the default proxy configured on the victim computer. [201] |
| S0629 | RainyDay | The file collection tool used by RainyDay can utilize native API including ReadDirectoryChangeW for folder monitoring. [175] |
| S0458 | Ramsay | Ramsay can use Windows API functions such as WriteFile , CloseHandle , and GetCurrentHwProfile during its collection and file storage operations. Ramsay can execute its embedded components via CreateProcessA and ShellExecute . [202] |
| S0662 | RCSession | RCSession can use WinSock API for communication including WSASend and WSARecv . [203] |
| S0416 | RDFSNIFFER | RDFSNIFFER has used several Win32 API functions to interact with the victim machine. [204] |
| S0496 | REvil | REvil can use Native API for execution and to retrieve active services. [205] [206] |
| S0448 | Rising Sun | Rising Sun used dynamic API resolutions to various Windows APIs by leveraging LoadLibrary() and GetProcAddress() . [186] |
| S0240 | ROKRAT | ROKRAT can use a variety of API calls to execute shellcode. [207] |
| S1078 | RotaJakiro | When executing with non-root permissions, RotaJakiro uses the the shmget API to create shared memory between other known RotaJakiro processes. RotaJakiro also uses the execvp API to help its dead process "resurrect". [208] |
| S1073 | Royal | Royal can use multiple APIs for discovery, communication, and execution. [209] |
| S0148 | RTM | RTM can use the FindNextUrlCacheEntryA and FindFirstUrlCacheEntryA functions to search for specific strings within browser history. [210] |
| S9037 | RustyWater | RustyWater has used CreateObject to instantiate a WScript.Shell Component Object Model (COM) object. [211] Additionally, RustyWater has used VirtualAllocEx and WriteProcessMemory to inject shellcode into explorer.exe. [211] |
| S0446 | Ryuk | Ryuk has used multiple native APIs including ShellExecuteW to run executables, GetWindowsDirectoryW to create folders, and VirtualAlloc , WriteProcessMemory , and CreateRemoteThread for process injection. [212] |
| S0085 | S-Type | S-Type has used Windows APIs, including GetKeyboardType , NetUserAdd , and NetUserDel . [164] |
| S1210 | Sagerunex | Sagerunex calls the WaitForSingleObject API function as part of time-check logic. [213] |
| S1018 | Saint Bot | Saint Bot has used different API calls, including GetProcAddress , VirtualAllocEx , WriteProcessMemory , CreateProcessA , and SetThreadContext . [214] [215] |
| S1099 | Samurai | Samurai has the ability to call Windows APIs. [179] |
| G0034 | Sandworm Team | Sandworm Team uses Prestige to disable and restore file system redirection by using the following functions: Wow64DisableWow64FsRedirection() and Wow64RevertWow64FsRedirection() . [196] |
| S1085 | Sardonic | Sardonic has the ability to call Win32 API functions to determine if powershell.exe is running. [216] |
| S1089 | SharpDisco | SharpDisco can leverage Native APIs through plugins including GetLogicalDrives . [178] |
| S0444 | ShimRat | ShimRat has used Windows API functions to install the service and shim. [217] |
| S0445 | ShimRatReporter | ShimRatReporter used several Windows API functions to gather information from the infected system. [217] |
| G1008 | SideCopy | SideCopy has executed malware by calling the API function CreateProcessW . [218] |
| S0610 | SideTwist | SideTwist can use GetUserNameW , GetComputerNameW , and GetComputerNameExW to gather information. [219] |
| G0091 | Silence | Silence has leveraged the Windows API, including using CreateProcess() or ShellExecute(), to perform a variety of tasks. [220] [221] |
| S0692 | SILENTTRINITY | SILENTTRINITY has the ability to leverage API including GetProcAddress and LoadLibrary . [222] |
| S0623 | Siloscape | Siloscape makes various native API calls. [223] |
| S0627 | SodaMaster | SodaMaster can use RegOpenKeyW to access the Registry. [224] |
| S0615 | SombRAT | SombRAT has the ability to respawn itself using ShellExecuteW and CreateProcessW . [77] |
| S1234 | SplatCloak | SplatCloak has utilized Native Windows API calls dynamically through ZwQuerySystemInformation . [173] |
| S1232 | SplatDropper | SplatDropper has utilized hashed Native Windows API calls. [173] |
| S1227 | StarProxy | StarProxy has used native windows API calls such as GetLocalTime() to retrieve system data. [174] |
| S1200 | StealBit | StealBit can use native APIs including LoadLibraryExA for execution and NtSetInformationProcess for defense evasion purposes. [225] |
| S1034 | StrifeWater | StrifeWater can use a variety of APIs for execution. [226] |
| S0603 | Stuxnet | Stuxnet uses the SetSecurityDescriptorDacl API to reduce object integrity levels. [227] |
| S0562 | SUNSPOT | SUNSPOT used Windows API functions such as MoveFileEx and NtQueryInformationProcess as part of the SUNBURST injection process. [228] |
| S1064 | SVCReady | SVCReady can use Windows API calls to gather information from an infected host. [229] |
| S0242 | SynAck | SynAck parses the export tables of system DLLs to locate and call various Windows API functions. [230] [231] |
| S9001 | SystemBC | SystemBC has utilized native Windows API functions such as EnumWindows and GetVolumeInformationA during discovery activities. [232] |
| S0663 | SysUpdate | SysUpdate can call the GetNetworkParams API as part of its C2 establishment process. [233] |
| G0092 | TA505 | TA505 has deployed payloads that use Windows API calls on a compromised host. [234] |
| S0011 | Taidoor | Taidoor has the ability to use native APIs for execution including GetProcessHeap , GetProcAddress , and LoadLibrary . [235] [236] |
| S0595 | ThiefQuest | ThiefQuest uses various API to perform behaviors such as executing payloads and performing local enumeration. [237] |
| S0668 | TinyTurla | TinyTurla has used WinHTTP , CreateProcess , and other APIs for C2 communications and other functions. [238] |
| G1022 | ToddyCat | ToddyCat has used WinExec to execute commands received from C2 on compromised hosts. [180] |
| S1239 | TONESHELL | TONESHELL has utilized Native Windows API functions such as WriteProcessMemory and CreateRemoteThreadEx . [170] TONESHELL has also utilized Windows API functions for creating seed values including CoCreateGuid and GetTickCount . [67] [174] TONESHELL has leveraged the legitimate API function EnumSystemLocalesA to run its shellcode through the callback function. [52] |
| S0678 | Torisma | Torisma has used various Windows API calls. [239] |
| S9012 | TRAILBLAZE | TRAILBLAZE has leveraged raw syscalls to execute commands. [240] [241] |
| S0266 | TrickBot | TrickBot uses the Windows API call, CreateProcessW(), to manage execution flow. [242] TrickBot has also used Nt* API functions to perform Process Injection . [243] |
| G0081 | Tropic Trooper | Tropic Trooper has used multiple Windows APIs including HttpInitialize, HttpCreateHttpHandle, and HttpAddUrl. [244] |
| G0010 | Turla | Turla and its RPC backdoors have used APIs calls for various tasks related to subverting AMSI and accessing then executing commands through RPC and/or named pipes. [245] |
| S0022 | Uroburos | Uroburos can use native Windows APIs including GetHostByName . [246] |
| S0386 | Ursnif | Ursnif has used CreateProcessW to create child processes. [247] |
| S0180 | Volgmer | Volgmer executes payloads using the Windows API call CreateProcessW(). [248] |
| S0670 | WarzoneRAT | WarzoneRAT can use a variety of API calls on a compromised host. [249] |
| S0612 | WastedLocker | WastedLocker 's custom crypter, CryptOne, leveraged the VirtualAlloc() API function to help execute the payload. [250] |
| S0579 | Waterbear | Waterbear can leverage API functions for execution. [251] |
| S0689 | WhisperGate | WhisperGate has used the ExitWindowsEx to flush file buffers to disk and stop running processes and other API calls. [252] [253] |
| S0466 | WindTail | WindTail can invoke Apple APIs contentsOfDirectoryAtPath , pathExtension , and (string) compare . [254] |
| S0141 | Winnti for Windows | Winnti for Windows can use Native API to create a new process and to start services. [255] |
| G0090 | WIRTE | WIRTE has used the RtlIpv4StringToAddressA to convert IP-formatted string to a byte array. [256] |
| S1065 | Woody RAT | Woody RAT can use multiple native APIs, including WriteProcessMemory , CreateProcess , and CreateRemoteThread for process injection. [257] |
| S0161 | XAgentOSX | XAgentOSX contains the execFile function to execute a specified file on the system using the NSTask:launch method. [258] |
| S0653 | xCaon | xCaon has leveraged native OS function calls to retrieve victim's network adapter's information using GetAdapterInfo() API. [53] |
| S1207 | XLoader | XLoader uses the native Windows API for functionality, including defense evasion. [259] |
| S1151 | ZeroCleare | ZeroCleare can call the GetSystemDirectoryW API to locate the system directory. [64] |
| S0412 | ZxShell | ZxShell can leverage native API including RegisterServiceCtrlHandler to register a service.RegisterServiceCtrlHandler |
| S1013 | ZxxZ | ZxxZ has used API functions such as Process32First , Process32Next , and ShellExecuteA . [260] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1040 | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent Office VBA macros from calling Win32 APIs. [261] |
| M1038 | Execution Prevention | Identify and block potentially malicious software executed that may be executed through this technique by using application control [262] tools, like Windows Defender Application Control [263] , AppLocker, [264] [265] or Software Restriction Policies [266] where appropriate. [267] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0529 | Behavioral Detection of Native API Invocation via Unusual DLL Loads and Direct Syscalls | AN1465 | Unusual or suspicious processes loading critical native API DLLs (e.g., ntdll.dll, kernel32.dll) followed by direct syscall behavior, memory manipulation, or hollowing. |
| AN1466 | Userland processes invoking syscall-heavy libraries (libc, glibc) followed by fork, mmap, or ptrace behavior commonly associated with code injection or memory manipulation. |  |  |
| AN1467 | Execution of processes that link to CoreServices or Foundation APIs followed by creation of memory regions, code execution, or abnormal library injection. |  |  |

---

## References

- [The NTinterlnals.net team. (n.d.). Nowak, T. Retrieved June 25, 2020.](https://undocumented.ntinternals.net/)
- [Linux Kernel Organization, Inc. (n.d.). The Linux Kernel API. Retrieved June 25, 2020.](https://www.kernel.org/doc/html/v4.12/core-api/kernel-api.html)
- [de Plaa, C. (2019, June 19). Red Team Tactics: Combining Direct System Calls and sRDI to bypass AV/EDR. Retrieved September 29, 2021.](https://outflank.nl/blog/2019/06/19/red-team-tactics-combining-direct-system-calls-and-srdi-to-bypass-av-edr/)
- [Gavriel, H. (2018, November 27). Malware Mitigation when Direct System Calls are Used. Retrieved September 29, 2021.](https://www.cyberbit.com/blog/endpoint-security/malware-mitigation-when-direct-system-calls-are-used/)
- [MDSec Research. (2020, December). Bypassing User-Mode Hooks and Direct Invocation of System Calls for Red Teams. Retrieved September 29, 2021.](https://www.mdsec.co.uk/2020/12/bypassing-user-mode-hooks-and-direct-invocation-of-system-calls-for-red-teams/)
- [Microsoft. (n.d.). CreateProcess function. Retrieved September 12, 2024.](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)
- [Free Software Foundation, Inc.. (2020, June 18). Creating a Process. Retrieved June 25, 2020.](https://www.gnu.org/software/libc/manual/html_node/Creating-a-Process.html)
- [Microsoft. (n.d.). Programming reference for the Win32 API. Retrieved March 15, 2020.](https://docs.microsoft.com/en-us/windows/win32/api/)
- [Kerrisk, M. (2016, December 12). libc(7) — Linux manual page. Retrieved June 25, 2020.](https://man7.org/linux/man-pages//man7/libc.7.html)
- [glibc developer community. (2020, February 1). The GNU C Library (glibc). Retrieved June 25, 2020.](https://www.gnu.org/software/libc/)
- [Microsoft. (n.d.). What is .NET Framework?. Retrieved March 15, 2020.](https://dotnet.microsoft.com/learn/dotnet/what-is-dotnet-framework)
- [Apple. (n.d.). Core Services. Retrieved June 25, 2020.](https://developer.apple.com/documentation/coreservices)
- [Apple. (2015, September 16). Cocoa Application Layer. Retrieved June 25, 2020.](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/CocoaApplicationLayer/CocoaApplicationLayer.html#//apple_ref/doc/uid/TP40001067-CH274-SW1)
- [Apple. (n.d.). Foundation. Retrieved July 1, 2020.](https://developer.apple.com/documentation/foundation)
- [Feichter, D. (2023, June 30). Direct Syscalls vs Indirect Syscalls. Retrieved September 27, 2023.](https://redops.at/en/blog/direct-syscalls-vs-indirect-syscalls)
- [Bitdefender. (2015, December). APT28 Under the Scope. Retrieved February 23, 2017.](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
- [Max Kersten & Alexandre Mundo. (2023, November 29). Akira Ransomware. Retrieved April 4, 2024.](https://www.trellix.com/blogs/research/akira-ransomware/)
- [Kasuya, M. (2020, January 8). Threat Spotlight: Amadey Bot Targets Non-Russian Users. Retrieved July 14, 2022.](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
- [Hiroaki, H. (2024, November 26). Guess Who’s Back - The Return of ANEL in the Recent Earth Kasha Spear-phishing Campaign in 2024. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)
- [DHS/CISA. (2020, August 26). FASTCash 2.0: North Korea's BeagleBoyz Robbing Banks. Retrieved September 29, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Jornet, A. (2021, December 23). Snip3, an investigation into malware. Retrieved September 19, 2023.](https://telefonicatech.com/blog/snip3-investigacion-malware)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [Security Lab. (2020, June 5). Avaddon: From seeking affiliates to in-the-wild in 2 days. Retrieved August 19, 2021.](https://www.hornetsecurity.com/en/security-information/avaddon-from-seeking-affiliates-to-in-the-wild-in-2-days/)
- [Hasherezade. (2021, July 23). AvosLocker enters the ransomware scene, asks for partners. Retrieved January 11, 2023.](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
- [Sogeti. (2021, March). Babuk Ransomware. Retrieved August 11, 2021.](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
- [Mundo, A. et al. (2021, February). Technical Analysis of Babuk Ransomware. Retrieved August 11, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
- [Sebdraven. (2021, February 8). Babuk is distributed packed. Retrieved August 11, 2021.](https://sebdraven.medium.com/babuk-is-distributed-packed-78e2f5dd2e62)
- [Hinchliffe, A. and Falcone, R. (2020, May 11). Updated BackConfig Malware Targeting Government and Military Organizations in South Asia. Retrieved June 17, 2020.](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)
- [M.Léveille, M-E.. (2017, October 24). Bad Rabbit: Not‑Petya is back with improved ransomware. Retrieved January 28, 2021.](https://www.welivesecurity.com/2017/10/24/bad-rabbit-not-petya-back/)
- [Savelesky, K., et al. (2019, July 23). ABADBABE 8BADFOOD: Discovering BADHATCH and a Detailed Look at FIN8's Tooling. Retrieved September 8, 2021.](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
- [Check Point. (2020, November 26). Bandook: Signed & Delivered. Retrieved May 31, 2021.](https://research.checkpoint.com/2020/bandook-signed-delivered/)
- [Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [Harbison, M. (2021, February 9). BendyBear: Novel Chinese Shellcode Linked With Cyber Espionage Group BlackTech. Retrieved February 16, 2021.](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [Frankoff, S., Hartley, B. (2018, November 14). Big Game Hunting: The Evolution of INDRIK SPIDER From Dridex Wire Fraud to BitPaymer Targeted Ransomware. Retrieved January 6, 2021.](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
- [Zargarov, N. (2022, May 2). New Black Basta Ransomware Hijacks Windows Fax Service. Retrieved March 7, 2023.](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
- [Cyble. (2022, May 6). New ransomware variant targeting high-value organizations. Retrieved November 17, 2024.](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
- [Avertium. (2022, June 1). AN IN-DEPTH LOOK AT BLACK BASTA RANSOMWARE. Retrieved March 7, 2023.](https://www.avertium.com/resources/threat-reports/in-depth-look-at-black-basta-ransomware)
- [Check Point. (2022, October 20). BLACK BASTA AND THE UNNOTICED DELIVERY. Retrieved March 8, 2023.](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
- [Gonzalez, I., Chavez I., et al. (2022, May 9). Examining the Black Basta Ransomware’s Infection Routine. Retrieved March 7, 2023.](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [Demboski, M., et al. (2021, October 26). China cyber attacks: the current threat landscape. Retrieved March 25, 2022.](https://www.ironnet.com/blog/china-cyber-attacks-the-current-threat-landscape)
- [Robbins, A., Vazarkar, R., and Schroeder, W. (2016, April 17). Bloodhound: Six Degrees of Domain Admin. Retrieved March 5, 2019.](https://github.com/BloodHoundAD/BloodHound)
- [Broadcom Protection Bulletins. (2025, February 20). Bookworm malware linked to Fireant (aka Stately Tarurus) activity observed in Southeast Asia. Retrieved July 21, 2025.](https://www.broadcom.com/support/security-center/protection-bulletin/bookworm-malware-linked-to-fireant-aka-stately-tarurus-activity-observed-in-southeast-asia)
- [Robert Falcone. (2025, February 20). Stately Taurus Activity in Southeast Asia Links to Bookworm Malware. Retrieved July 21, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-uses-bookworm-malware/)
- [CheckPoint Research. (2021, July 1). IndigoZebra APT continues to attack Central Asia with evolving tools. Retrieved September 24, 2021.](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
- [Harbison, M. and Renals, P. (2022, July 5). When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors. Retrieved February 1, 2023.](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
- [Chell, D. PART 3: How I Met Your Beacon – Brute Ratel. Retrieved February 6, 2023.](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)
- [Merriman, K. and Trouerbach, P. (2022, April 28). This isn't Optimus Prime's Bumblebee but it's Still Transforming. Retrieved August 22, 2022.](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
- [Salem, A. (2022, April 27). The chronicles of Bumblebee: The Hook, the Bee, and the Trickbot connection. Retrieved September 2, 2022.](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
- [Malhotra, A. (2022, March 15). Threat Advisory: CaddyWiper. Retrieved March 23, 2022.](https://blog.talosintelligence.com/2022/03/threat-advisory-caddywiper.html)
- [Pellegrino, G. (2025, December 16). BlindEagle Targets Colombian Government Agency with Caminho and DCRAT. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)
- [Patrick Whitsell. (2025, August 25). Deception in Depth: PRC-Nexus Espionage Campaign Hijacks Web Traffic to Target Diplomats. Retrieved September 9, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)
- [Trusteer Fraud Prevention Center. (2010, October 7). Carberp Under the Hood of Carberp: Malware & Configuration Analysis. Retrieved July 15, 2020.](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)
- [Salem, E. (2020, November 17). CHAES: Novel Malware Targeting Latin American E-Commerce. Retrieved June 30, 2021.](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
- [Cycraft. (2020, April 15). APT Group Chimera - APT Operation Skeleton key Targets Taiwan Semiconductor Vendors. Retrieved August 24, 2020..](https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Golo Muhr, Joshua Chung. (2025, June 23). Hive0154 aka Mustang Panda shifts focus on Tibetan community to deploy Pubload backdoor. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [Mundo, A. (2019, August 1). Clop Ransomware. Retrieved May 10, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
- [Cybereason Nocturnus. (2020, December 23). Cybereason vs. Clop Ransomware. Retrieved May 11, 2021.](https://www.cybereason.com/blog/cybereason-vs.-clop-ransomware)
- [Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
- [Mavis, N. (2020, September 21). The Art and Science of Detecting Cobalt Strike. Retrieved September 12, 2024.](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [Rochberger, L. (2021, January 12). Cybereason vs. Conti Ransomware. Retrieved February 17, 2021.](https://www.cybereason.com/blog/cybereason-vs.-conti-ransomware)
- [Baskin, B. (2020, July 8). TAU Threat Discovery: Conti Ransomware. Retrieved February 17, 2021.](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [NCSC. (2022, February 23). Cyclops Blink Malware Analysis Report. Retrieved March 3, 2022.](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
- [Ernesto Fernández Provecho, Pham Duy Phuc, Ciana Driscoll & Vinoo Thomas. (2023, November 21). The Continued Evolution of the DarkGate Malware-as-a-Service. Retrieved February 9, 2024.](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [McGraw, T. (2024, December 4). Black Basta Ransomware Campaign Drops Zbot, DarkGate, and Custom Malware. Retrieved December 9, 2024.](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [Checkpoint Research. (2021, November 15). Uncovering MosesStaff techniques: Ideology over Money. Retrieved August 11, 2022.](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [TheWover. (2019, May 9). donut. Retrieved March 25, 2022.](https://github.com/TheWover/donut)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part I. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [Check Point Research. (2021, January 4). Stopping Serial Killer: Catching the Next Strike. Retrieved September 7, 2021.](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [ESET. (2026, January 30). DynoWiper update: Technical analysis and attribution. Retrieved April 22, 2026.](https://www.welivesecurity.com/en/eset-research/dynowiper-update-technical-analysis-attribution/)
- [Cybleinc. (2020, October 31). Egregor Ransomware – A Deep Dive Into Its Activities and Techniques. Retrieved December 29, 2020.](https://cybleinc.com/2020/10/31/egregor-ransomware-a-deep-dive-into-its-activities-and-techniques/)
- [Cyble. (2024, May 24). The Rust Revolution: New Embargo Ransomware Steps In. Retrieved October 19, 2025.](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
- [Binary Defense. (n.d.). Emotet Evolves With new Wi-Fi Spreader. Retrieved September 8, 2023.](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Marschalek, M.. (2014, December 16). EvilBunny: Malware Instrumented By Lua. Retrieved June 28, 2019.](https://web.archive.org/web/20150311013500/http://www.cyphort.com/evilbunny-malware-instrumented-lua/)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [Threat Intelligence and Research. (2015, March 30). VOLATILE CEDAR. Retrieved February 8, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [Ramin Nafisi. (2021, September 27). FoggyWeb: Targeted NOBELIUM malware leads to persistent backdoor. Retrieved October 4, 2021.](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
- [ESET Research. (2025, December 2). MuddyWater: Snakes by the riverbank. Retrieved February 17, 2026.](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Quinn, J. (2019, March 25). The odd case of a Gh0stRAT variant. Retrieved July 15, 2020.](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
- [Trustwave SpiderLabs. (2020, June 25). The Golden Tax Department and Emergence of GoldenSpy Malware. Retrieved July 23, 2020.](https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/)
- [Falcone, R., et al. (2018, August 02). The Gorgon Group: Slithering Between Nation State and Cybercrime. Retrieved August 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [Priego, A. (2021, July). THE BROTHERS GRIM: THE REVERSING TALE OF GRIMAGENT MALWARE USED BY RYUK. Retrieved September 19, 2024.](https://www.group-ib.com/blog/grimagent/)
- [Salem, E. (2021, April 19). Dancing With Shellcodes: Cracking the latest version of Guloader. Retrieved July 7, 2021.](https://elis531989.medium.com/dancing-with-shellcodes-cracking-the-latest-version-of-guloader-75083fb15cb4)
- [Anubhav, A., Jallepalli, D. (2016, September 23). Hancitor (AKA Chanitor) observed using multiple attack approaches. Retrieved August 13, 2020.](https://www.fireeye.com/blog/threat-research/2016/09/hancitor_aka_chanit.html)
- [Ungur, P. (n.d.). HAVOC. Retrieved August 4, 2025.](https://havocframework.com/docs/welcome)
- [Patil, S. and Williams, M.. (2019, June 5). Government Sector in Central Asia Targeted With New HAWKBALL Backdoor Delivered via Microsoft Office Vulnerabilities. Retrieved June 20, 2019.](https://www.fireeye.com/blog/threat-research/2019/06/government-in-central-asia-targeted-with-hawkball-backdoor.html)
- [Tujague, J., Bunce, D. (n.d.). Crypted Hearts: Exposing the HeartCrypt Packer-as-a-Service Operation. Retrieved April 16, 2026.](https://unit42.paloaltonetworks.com/packer-as-a-service-heartcrypt-malware/)
- [Guerrero-Saade, J. (2022, February 23). HermeticWiper | New Destructive Malware Used In Cyber Attacks on Ukraine. Retrieved March 25, 2022.](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
- [Thomas, W. et al. (2022, February 25). CrowdStrike Falcon Protects from New Wiper Malware Used in Ukraine Cyberattacks. Retrieved March 25, 2022.](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
- [ESET. (2022, March 1). IsaacWiper and HermeticWizard: New wiper and worm targetingUkraine. Retrieved April 10, 2022.](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
- [Dani, M. (2022, March 1). Ukrainian Targets Hit by HermeticWiper, New Datawiper Malware. Retrieved March 25, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
- [Singh, S. Singh, A. (2020, June 11). The Return on the Higaisa APT. Retrieved March 2, 2021.](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)
- [US-CERT. (2020, February 20). MAR-10271944-1.v1 – North Korean Trojan: HOTCROISSANT. Retrieved May 1, 2020.](https://www.us-cert.gov/ncas/analysis-reports/ar20-045d)
- [Alexndru-Cristian Bardas. (2025, October 30). DPRK’s Playbook: Kimsuky’s HttpTroy and Lazarus’s New BLINDINGCAN Variant. Retrieved April 8, 2026.](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)
- [Falcone, R. and Lancaster, T. (2019, May 28). Emissary Panda Attacks Middle East Government Sharepoint Servers. Retrieved July 9, 2019.](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)
- [Accenture. (2020, October). Turla uses HyperStack, Carbon, and Kazuar to compromise government entity. Retrieved December 2, 2020.](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)
- [Kimayong, P. (2020, June 18). COVID-19 and FMLA Campaigns used to install new IcedID banking malware. Retrieved July 14, 2020.](https://blogs.juniper.net/en-us/threat-research/covid-19-and-fmla-campaigns-used-to-install-new-icedid-banking-malware)
- [PwC Threat Intelligence. (2023, October 25). Yellow Liderc ships its scripts and delivers IMAPLoader malware. Retrieved August 14, 2024.](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
- [QiAnXin Threat Intelligence Center. (2019, February 18). APT-C-36: Continuous Attacks Targeting Colombian Government Institutions and Corporations. Retrieved May 5, 2020.](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [ASERT Team. (2018, April 04). Innaput Actors Utilize Remote Access Trojan Since 2016, Presumably Targeting Victim Files. Retrieved July 9, 2018.](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Mohammad Kazem Hassan Nejad, WithSecure. (2024, April 17). KAPEKA A novel backdoor spotted in Eastern Europe. Retrieved January 6, 2025.](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Fernando Merces, Byron Gelera, Martin Co. (2018, June 7). KillDisk Variant Hits Latin American Finance Industry. Retrieved January 12, 2021.](https://www.trendmicro.com/en_us/research/18/f/new-killdisk-variant-hits-latin-american-financial-organizations-again.html)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Jazi, H. (2021, February). LazyScripter: From Empire to double RAT. Retrieved November 17, 2024.](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
- [Threat Intelligence Team. (2021, August 23). New variant of Konni malware used in campaign targetting Russia. Retrieved January 5, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
- [Stepanic, D. and Bousseaden, S. (2024, May 15). Spring Cleaning with LATRODECTUS: A Potential Replacement for ICEDID. Retrieved September 13, 2024.](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
- [Batista, J. (2024, June 17). Latrodectus, are you coming back?. Retrieved September 13, 2024.](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
- [Cashman, M. (2020, July 29). Operation North Star Campaign. Retrieved December 20, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-a-job-offer-thats-too-good-to-be-true/?hilite=%27Operation%27%2C%27North%27%2C%27Star%27)
- [Saini, A. and Hossein, J. (2022, January 27). North Korea’s Lazarus APT leverages Windows Update client, GitHub in latest campaign. Retrieved January 27, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)
- [Pradhan, A. (2022, February 8). LolZarus: Lazarus Group Incorporating Lolbins into Campaigns. Retrieved March 22, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)
- [Faou, M. (2019, May). Turla LightNeuron: One email away from remote code execution. Retrieved June 24, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
- [Yamout, M. (2021, November 29). WIRTE’s campaign in the Middle East ‘living off the land’ since at least 2019. Retrieved February 1, 2022.](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [Walter, J. (2022, July 21). LockBit 3.0 Update | Unpicking the Ransomware’s Latest Anti-Analysis and Evasion Techniques. Retrieved February 5, 2025.](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
- [INCIBE-CERT. (2024, March 14). LockBit: response and recovery actions. Retrieved February 5, 2025.](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part II. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
- [Muhammad, I., Unterbrink, H.. (2021, January 6). A Deep Dive into Lokibot Infection Chain. Retrieved August 31, 2021.](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Wardle, P. (2021, November 11). OSX.CDDS (OSX.MacMa). Retrieved June 30, 2022.](https://objective-see.org/blog/blog_0x69.html)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [Hromcova, Z. and Burgher, A. (2023, September 21). OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes. Retrieved November 21, 2024.](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
- [GReAT. (2021, June 16). Ferocious Kitten: 6 Years of Covert Surveillance in Iran. Retrieved September 22, 2021.](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
- [Mundo, A. (2020, March 26). Ransomware Maze. Retrieved May 18, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Del Fierro, C. Kessem, L.. (2020, January 8). From Mega to Giga: Cross-Version Comparison of Top MegaCortex Modifications. Retrieved February 15, 2021.](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
- [Symantec. (2020, November 17). Japan-Linked Organizations Targeted in Long-Running and Sophisticated Attack Campaign. Retrieved December 17, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [Erlich, C. (2020, April 3). The Avast Abuser: Metamorfo Banking Malware Hides By Abusing Avast Executable. Retrieved May 26, 2020.](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
- [Zhang, X. (2020, February 4). Another Metamorfo Variant Targeting Customers of Financial Institutions in More Countries. Retrieved July 30, 2020.](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
- [Check Point Research Team. (2021, August 14). Indra - Hackers Behind Recent Attacks on Iran. Retrieved February 17, 2022.](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Pedro Tavares (Segurança Informática). (2020, September 15). Threat analysis: The emergent URSA trojan impacts many countries using a sophisticated loader. Retrieved March 13, 2024.](https://seguranca-informatica.pt/threat-analysis-the-emergent-ursa-trojan-impacts-many-countries-using-a-sophisticated-loader/)
- [SCILabs. (2021, December 23). Cyber Threat Profile Malteiro. Retrieved March 13, 2024.](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
- [ESET, et al. (2018, January). Diplomats in Eastern Europe bitten by a Turla mosquito. Retrieved July 3, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Dex. (n.d.). New Mustang Panda’s campaing against Australia. Retrieved August 4, 2025.](https://lab52.io/blog/new-mustang-pandas-campaing-against-australia/)
- [Nathaniel Morales, Nick Dai. (2025, February 18). Earth Preta Mixes Legitimate and Malicious Components to Sidestep Detection. Retrieved September 10, 2025.](https://www.trendmicro.com/en_us/research/25/b/earth-preta-mixes-legitimate-and-malicious-components-to-sidestep-detection.html)
- [Nick Dai, Vickie Su, Sunny Lu. (2022, November 18). Earth Preta Spear-Phishing Governments Worldwide. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
- [Secureworks Counter Threat Unit Research Team. (2022, September 8). BRONZE PRESIDENT Targets Government Officials. Retrieved September 9, 2025.](https://www.secureworks.com/blog/bronze-president-targets-government-officials)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: PAKLOG, CorKLOG, and SplatCloak | P2. Retrieved September 12, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: ToneShell and StarProxy | P1. Retrieved July 21, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-toneshell-and-starproxy-p1)
- [Vrabie, V. (2021, April 23). NAIKON – Traces from a Military Cyber-Espionage Operation. Retrieved June 29, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
- [Victor, K.. (2020, May 18). Netwalker Fileless Ransomware Injected via Reflective Loading . Retrieved May 26, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
- [Maniath, S. and Kadam P. (2019, March 19). Dissecting a NETWIRE Phishing Campaign's Usage of Process Hollowing. Retrieved January 7, 2021.](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [Pascual, C. (2018, November 27). AutoIt-Compiled Worm Affecting Removable Media Delivers Fileless Version of BLADABINDI/njRAT Backdoor. Retrieved June 4, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [Hromcova, Z. and Burgher, A. (2023, December 14). OilRig’s persistent attacks using cloud service-powered downloaders. Retrieved November 26, 2024.](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
- [Aleksandar Milenkoski, Luigi Martire. (2024, December 10). Operation Digital Eye | Chinese APT Compromises Critical Digital Infrastructure via Visual Studio Code Tunnels. Retrieved February 27, 2025.](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels/)
- [Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-uncovers-operation-honeybee-malicious-document-campaign-targeting-humanitarian-aid-groups/)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Brett Stone-Gross & Nikolaos Pantazopoulos. (2023, May 24). Technical Analysis of Pikabot. Retrieved July 12, 2024.](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)
- [Daniel Stepanic & Salim Bitam. (2024, February 23). PIKABOT, I choose you!. Retrieved July 12, 2024.](https://www.elastic.co/security-labs/pikabot-i-choose-you)
- [Trustwave SpiderLabs. (2020, June 22). Pillowmint: FIN7’s Monkey Thief . Retrieved July 27, 2020.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
- [Tartare, M. et al. (2020, May 21). No “Game over” for the Winnti Group. Retrieved August 24, 2020.](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
- [Bermejo, L., et al. (2017, June 22). Following the Trail of BlackTech’s Cyber Espionage Campaigns. Retrieved May 5, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
- [Raggi, M. et al. (2022, March 7). The Good, the Bad, and the Web Bug: TA416 Increases Operational Tempo Against European Governments as Conflict in Ukraine Escalates. Retrieved March 16, 2022.](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)
- [Vasilenko, R. (2013, December 17). An Analysis of PlugX Malware. Retrieved November 24, 2015.](https://lastline3.rssing.com/chan-29044929/all_p1.html#c29044929a2)
- [hasherezade. (2016, April 11). No money, but Pony! From a mail to a trojan horse. Retrieved May 21, 2020.](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)
- [MSTIC. (2022, October 14). New “Prestige” ransomware impacts organizations in Ukraine and Poland. Retrieved January 19, 2023.](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
- [Microsoft Threat Intelligence Center. (2022, February 4). ACTINIUM targets Ukrainian organizations. Retrieved February 18, 2022.](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
- [Morrow, D. (2021, April 15). The rise of QakBot. Retrieved September 27, 2021.](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)
- [Magdy, S. et al. (2022, August 25). New Golang Ransomware Agenda Customizes Attacks. Retrieved September 26, 2025.](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
- [Halcyon RISE Team. (2024, October 24). New Qilin.B Ransomware Variant Boasts Enhanced Encryption and Defense Evasion. Retrieved September 26, 2025.](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Global Threat Center, Intelligence Team. (2020, December). APT27 Turns to Ransomware. Retrieved November 12, 2021.](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
- [Carr, N, et all. (2019, October 10). Mahalo FIN7: Responding to the Criminal Operators’ New Tools and Techniques. Retrieved October 11, 2019.](https://www.fireeye.com/blog/threat-research/2019/10/mahalo-fin7-responding-to-new-tools-and-techniques.html)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [Intel 471 Malware Intelligence team. (2020, March 31). REvil Ransomware-as-a-Service – An analysis of a ransomware affiliate operation. Retrieved August 4, 2020.](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
- [Jazi, Hossein. (2021, January 6). Retrohunting APT37: North Korean APT used VBA self decode technique to inject RokRat. Retrieved March 22, 2022.](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
- [Alex Turing, Hui Wang. (2021, April 28). RotaJakiro: A long live secret backdoor with 0 VT detection. Retrieved June 14, 2023.](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
- [Cybereason Global SOC and Cybereason Security Research Teams. (2022, December 14). Royal Rumble: Analysis of Royal Ransomware. Retrieved March 30, 2023.](https://www.cybereason.com/blog/royal-ransomware-analysis)
- [Faou, M. and Boutin, J. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
- [Awasthi, P. (2026, January 8). Reborn in Rust: Muddy Water Evolves Tooling with RustyWater Implant. Retrieved March 19, 2026.](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
- [Hanel, A. (2019, January 10). Big Game Hunting with Ryuk: Another Lucrative Targeted Ransomware. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [Hasherezade. (2021, April 6). A deep dive into Saint Bot, a new downloader. Retrieved June 9, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Budaca, E., et al. (2021, August 25). FIN8 Threat Actor Goes Agile with New Sardonic Backdoor. Retrieved August 9, 2023.](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [GReAT. (2017, November 1). Silence – a new Trojan attacking financial organizations. Retrieved May 24, 2019.](https://securelist.com/the-silence/83009/)
- [Group-IB. (2018, September). Silence: Moving Into the Darkside. Retrieved May 5, 2020.](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [Prizmant, D. (2021, June 7). Siloscape: First Known Malware Targeting Windows Containers to Compromise Cloud Environments. Retrieved June 9, 2021.](https://unit42.paloaltonetworks.com/siloscape/)
- [GREAT. (2021, March 30). APT10: sophisticated multi-layered loader Ecipekac discovered in A41APT campaign. Retrieved June 17, 2021.](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
- [Cybereason Global SOC Team. (n.d.). THREAT ANALYSIS REPORT: Inside the LockBit Arsenal - The StealBit Exfiltration Tool. Retrieved January 29, 2025.](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
- [Cybereason Nocturnus. (2022, February 1). StrifeWater RAT: Iranian APT Moses Staff Adds New Trojan to Ransomware Operations. Retrieved August 15, 2022.](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [CrowdStrike Intelligence Team. (2021, January 11). SUNSPOT: An Implant in the Build Process. Retrieved January 11, 2021.](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [Ivanov, A. et al. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
- [Bettencourt, J. (2018, May 7). Kaspersky Lab finds new variant of SynAck ransomware using sophisticated Doppelgänging technique. Retrieved May 24, 2018.](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)
- [Gallagher, S., Gn, S. (2020, December 16). Ransomware operators use SystemBC RAT as off-the-shelf Tor backdoor. Retrieved May 16, 2025.](https://news.sophos.com/en-us/2020/12/16/systembc/)
- [Daniel Lunghi. (2023, March 1). Iron Tiger’s SysUpdate Reappears, Adds Linux Targeting. Retrieved March 20, 2023.](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [Trend Micro. (2012). The Taidoor Campaign. Retrieved November 12, 2014.](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)
- [CISA, FBI, DOD. (2021, August). MAR-10292089-1.v2 – Chinese Remote Access Trojan: TAIDOOR. Retrieved August 24, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
- [Patrick Wardle. (2020, July 3). OSX.EvilQuest Uncovered part ii: insidious capabilities. Retrieved March 21, 2021.](https://objective-see.com/blog/blog_0x60.html)
- [Cisco Talos. (2021, September 21). TinyTurla - Turla deploys new malware to keep a secret backdoor on victim machines. Retrieved December 2, 2021.](https://blog.talosintelligence.com/2021/09/tinyturla.html)
- [Beek, C. (2020, November 5). Operation North Star: Behind The Scenes. Retrieved December 20, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
- [John Wolfram, Michael Edie, Jacob Thompson, Matt Lin, Josh Murchie. (2025, April 3). Suspected China-Nexus Threat Actor Actively Exploiting Critical Ivanti Connect Secure Vulnerability (CVE-2025-22457). Retrieved April 13, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)
- [Sila Ozeren Hacioglu. (2025, May 5). UNC5221’s Latest Exploit: Weaponizing CVE-2025-22457 in Ivanti Connect Secure. Retrieved April 13, 2026.](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
- [Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
- [Joe Security. (2020, July 13). TrickBot's new API-Hammering explained. Retrieved September 30, 2021.](https://www.joesecurity.org/blog/498839998833561473)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Vaish, A. & Nemes, S. (2017, November 28). Newly Observed Ursnif Variant Employs Malicious TLS Callback Technique to Achieve Process Injection. Retrieved June 5, 2019.](https://www.fireeye.com/blog/threat-research/2017/11/ursnif-variant-malicious-tls-callback-technique.html)
- [US-CERT. (2017, November 01). Malware Analysis Report (MAR) - 10135536-D. Retrieved July 16, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)
- [Mohanta, A. (2020, November 25). Warzone RAT comes with UAC bypass technique. Retrieved April 7, 2022.](https://www.uptycs.com/blog/warzone-rat-comes-with-uac-bypass-technique)
- [Antenucci, S., Pantazopoulos, N., Sandee, M. (2020, June 23). WastedLocker: A New Ransomware Variant Developed By The Evil Corp Group. Retrieved September 14, 2021.](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
- [Su, V. et al. (2019, December 11). Waterbear Returns, Uses API Hooking to Evade Security. Retrieved February 22, 2021.](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
- [Biasini, N. et al.. (2022, January 21). Ukraine Campaign Delivers Defacement and Wipers, in Continued Escalation. Retrieved March 14, 2022.](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
- [Insikt Group. (2020, January 28). WhisperGate Malware Corrupts Computers in Ukraine. Retrieved September 16, 2024.](https://www.recordedfuture.com/research/whispergate-malware-corrupts-computers-ukraine)
- [Wardle, Patrick. (2019, January 15). Middle East Cyber-Espionage analyzing WindShift's implant: OSX.WindTail (part 2). Retrieved October 3, 2019.](https://objective-see.com/blog/blog_0x3D.html)
- [Novetta Threat Research Group. (2015, April 7). Winnti Analysis. Retrieved February 8, 2017.](https://web.archive.org/web/20150412223949/http://www.novetta.com/wp-content/uploads/2015/04/novetta_winntianalysis.pdf)
- [Check Point. (2024, November 12). Hamas-affiliated Threat Actor WIRTE Continues its Middle East Operations and Moves to Disruptive Activity. Retrieved April 20, 2026.](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Robert Falcone. (2017, February 14). XAgentOSX: Sofacy's Xagent macOS Tool. Retrieved July 12, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)
- [Zscaler Threatlabz. (2025, January 27). Technical Analysis of Xloader Versions 6 and 7 | Part 1. Retrieved March 11, 2025.](https://www.zscaler.com/blogs/security-research/technical-analysis-xloader-versions-6-and-7-part-1)
- [Raghuprasad, C . (2022, May 11). Bitter APT adds Bangladesh to their targets. Retrieved June 1, 2022.](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)
- [Microsoft. (2021, July 2). Use attack surface reduction rules to prevent malware infection. Retrieved June 24, 2021.](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
- [Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)
- [Gorzelany, A., Hall, J., Poggemeyer, L.. (2019, January 7). Windows Defender Application Control. Retrieved July 16, 2019.](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
- [Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)
- [NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
- [Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved September 12, 2024.](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))
- [Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.](https://technet.microsoft.com/en-us/library/ee791851.aspx)

---

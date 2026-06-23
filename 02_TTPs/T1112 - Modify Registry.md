# Modify Registry

## Description

Adversaries may interact with the Windows Registry as part of a variety of other techniques to aid in defense evasion, persistence, and execution.

Access to specific areas of the Registry depends on account permissions, with some keys requiring administrator-level access. The built-in Windows command-line utility Reg may be used for local or remote Registry modification. [1] Other tools, such as remote access tools, may also contain functionality to interact with the Registry through the Windows API.

The Registry may be modified in order to hide configuration information or malicious payloads via Obfuscated Files or Information . [2] [3] [4] [5] The Registry may also be modified to impair defenses, such as by enabling macros for all Microsoft Office products, allowing privilege escalation without alerting the user, increasing the maximum number of allowed outbound requests, and/or modifying systems to store plaintext credentials in memory. [6] [2]

The Registry of a remote system may be modified to aid in execution of files as part of lateral movement. It requires the remote Registry service to be running on the target system. [7] Often Valid Accounts are required, along with access to the remote system's SMB/Windows Admin Shares for RPC communication.

Finally, Registry modifications may also include actions to hide keys, such as prepending key names with a null character, which will cause an error and/or be ignored when read via Reg or other utilities using the Win32 API. [8] Adversaries may abuse these pseudo-hidden keys to conceal payloads/commands used to maintain persistence. [9] [10]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0028 | 2015 Ukraine Electric Power Attack | During the 2015 Ukraine Electric Power Attack , Sandworm Team modified in-registry Internet settings to lower internet security before launching rundll32.exe , which in-turn launches the malware and communicates with C2 servers over the Internet. [11] . |
| S0677 | AADInternals | AADInternals can modify registry keys as part of setting a new pass-through authentication agent. [12] |
| S0045 | ADVSTORESHELL | ADVSTORESHELL is capable of setting and deleting Registry values. [13] |
| S0331 | Agent Tesla | Agent Tesla can achieve persistence by modifying Registry key entries. [14] |
| S1025 | Amadey | Amadey has overwritten registry keys for persistence. [15] |
| G0073 | APT19 | APT19 uses a Port 22 malware variant to modify several Registry keys. [16] |
| G0050 | APT32 | APT32 's backdoor has modified the Windows Registry to store the backdoor's configuration. [17] |
| G0082 | APT38 | APT38 uses a tool called CLEANTOAD that has the capability to modify Registry keys. [18] |
| G0096 | APT41 | APT41 used a malware variant called GOODLUCK to modify the registry in order to steal credentials. [19] [20] |
| G1044 | APT42 | APT42 has modified Registry keys to maintain persistence. [21] |
| G0143 | Aquatic Panda | Aquatic Panda modified the victim registry to enable the RestrictedAdmin mode feature, allowing for pass the hash behaviors to function via RDP. [22] |
| S0438 | Attor | Attor 's dispatcher can modify the Run registry key. [23] |
| S0640 | Avaddon | Avaddon modifies several registry keys for persistence and UAC bypass. [24] |
| S0031 | BACKSPACE | BACKSPACE is capable of deleting Registry keys, sub-keys, and values on a victim system. [25] |
| S0245 | BADCALL | BADCALL modifies the firewall Registry key SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfileGloballyOpenPorts\List . [26] |
| S0239 | Bankshot | Bankshot writes data into the Registry key HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Pniumj . [27] |
| S0268 | Bisonal | Bisonal has deleted Registry keys to clean up its prior activity. [28] |
| S0570 | BitPaymer | BitPaymer can set values in the Registry to help in execution. [29] |
| S1070 | Black Basta | Black Basta has modified the Registry to enable itself to run in safe mode, to change the icons and file extensions for encrypted files, and to add the malware path for persistence. [30] [31] [32] [33] [34] [35] |
| G1043 | BlackByte | BlackByte performed Registry modifications to escalate privileges and disable security tools. [36] [37] |
| S1181 | BlackByte 2.0 Ransomware | BlackByte 2.0 Ransomware modifies the victim Registry to allow for elevated execution. [38] |
| S1180 | BlackByte Ransomware | BlackByte Ransomware modifies the victim Registry to prevent system recovery. [39] |
| S1068 | BlackCat | BlackCat has the ability to add the following registry key on compromised networks to maintain persistence: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services \LanmanServer\Paramenters [4] |
| G0108 | Blue Mockingbird | Blue Mockingbird has used Windows Registry modifications to specify a DLL payload. [40] |
| S1226 | BOOKWORM | BOOKWORM has modified Registry key values as part of its created service DeviceSync . [41] |
| S0348 | Cardinal RAT | Cardinal RAT sets HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Load to point to its executable. [42] |
| S0261 | Catchamas | Catchamas creates three Registry keys to establish persistence by adding a Windows Service . [43] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell has a command to modify a Registry key. [44] |
| S0631 | Chaes | Chaes can modify Registry values to stored information and establish persistence. [45] |
| S0674 | CharmPower | CharmPower can remove persistence-related artifacts from the Registry. [46] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP can use the Windows Registry Environment key to change the %windir% variable to point to c:\Windows to enable payload execution. [47] |
| S0023 | CHOPSTICK | CHOPSTICK may modify Registry keys to store RC4 encrypted configuration information. [48] |
| S0660 | Clambling | Clambling can set and delete Registry keys. [49] |
| S0611 | Clop | Clop can make modifications to Registry keys. [50] |
| S0154 | Cobalt Strike | Cobalt Strike can modify Registry values within HKEY_CURRENT_USER\Software\Microsoft\Office\ \Excel\Security\AccessVBOM\ to enable the execution of additional code. [51] |
| S0126 | ComRAT | ComRAT has modified Registry values to store encrypted orchestrator code and payloads. [52] [53] |
| S0608 | Conficker | Conficker adds keys to the Registry at HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services and various other Registry locations. [54] [55] |
| S0488 | CrackMapExec | CrackMapExec can create a registry key using wdigest. [56] |
| S0115 | Crimson | Crimson can set a Registry key to determine how long it has been installed and possibly to indicate the version number. [57] |
| S0527 | CSPY Downloader | CSPY Downloader can write to the Registry under the %windir% variable to execute tasks. [58] |
| S0334 | DarkComet | DarkComet adds a Registry value for its installation routine to the Registry Key HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System Enable LUA="0" and HKEY_CURRENT_USER\Software\DC3_FEXEC . [59] [60] |
| S1066 | DarkTortilla | DarkTortilla has modified registry keys for persistence. [61] |
| S0673 | DarkWatchman | DarkWatchman can modify Registry values to store configuration strings, keylogger, and output of components. [62] |
| S1033 | DCSrv | DCSrv has created Registry keys for persistence. [63] |
| G0035 | Dragonfly | Dragonfly has modified the Registry to perform multiple techniques through the use of Reg . [64] |
| G1006 | Earth Lusca | Earth Lusca modified the registry using the command reg add "HKEY_CURRENT_USER\Environment" /v UserInitMprLogonScript /t REG_SZ /d "[file path]" for persistence. [65] |
| S1247 | Embargo | Embargo has modified and deleted Registry keys to add services, and to disable Security Solutions such as Windows Defender. [66] |
| G1003 | Ember Bear | Ember Bear modifies registry values for anti-forensics and defense evasion purposes. [67] |
| S0568 | EVILNUM | EVILNUM can make modifications to the Regsitry for persistence. [68] |
| S0343 | Exaramel for Windows | Exaramel for Windows adds the configuration to the Registry in XML format. [69] |
| S0569 | Explosive | Explosive has a function to write itself to Registry values. [70] |
| S0267 | FELIXROOT | FELIXROOT deletes the Registry key HKCU\Software\Classes\Applications\rundll32.exe\shell\open . [71] |
| S0679 | Ferocious | Ferocious has the ability to add a Class ID in the current user Registry hive to enable persistence mechanisms. [72] |
| G0061 | FIN8 | FIN8 has deleted Registry keys during post compromise cleanup activities. [73] |
| G0047 | Gamaredon Group | Gamaredon Group has removed security settings for VBA macro execution by changing registry values HKCU\Software\Microsoft\Office\<version>\<product>\Security\VBAWarnings and HKCU\Software\Microsoft\Office\<version>\<product>\Security\AccessVBOM . [74] [75] [76] Gamaredon Group has also modified Registry keys to hide folders and system files and to add the C2 address under HKEY_CURRENT_USER\Console\WindowsUpdate . [77] |
| S0666 | Gelsemium | Gelsemium can modify the Registry to store its components. [78] |
| S0032 | gh0st RAT | gh0st RAT has altered the InstallTime subkey. [79] |
| G0078 | Gorgon Group | Gorgon Group malware can deactivate security mechanisms in Microsoft Office by editing several keys and values under HKCU\Software\Microsoft\Office\ . [80] |
| S0531 | Grandoreiro | Grandoreiro can modify the Registry to store its configuration at HKCU\Software\ under frequently changing names including %USERNAME% and ToolTech-RM . [81] |
| S0342 | GreyEnergy | GreyEnergy modifies conditions in the Registry and adds keys. [82] |
| S0697 | HermeticWiper | HermeticWiper has the ability to modify Registry keys to disable crash dumps, colors for compressed files, and pop-up information about folders and desktop items. [83] [84] [85] |
| S9023 | HiddenFace | HiddenFace can store its configuration file in the Registry. [86] |
| S1230 | HIUPAN | HIUPAN has modified registry keys to ensure hidden files and extensions are not visible through the modification of HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced . [87] [88] |
| S0376 | HOPLIGHT | HOPLIGHT has modified Managed Object Format (MOF) files within the Registry to run specific commands and create persistence on the system. [89] |
| S0203 | Hydraq | Hydraq creates a Registry subkey to register its created service, and can also uninstall itself later by deleting this value. Hydraq 's backdoor also enables remote attackers to modify and delete subkeys. [90] [91] |
| S0537 | HyperStack | HyperStack can add the name of its communication pipe to HKLM\SYSTEM\CurrentControlSet\Services\lanmanserver\parameters\NullSessionPipes . [92] |
| G0119 | Indrik Spider | Indrik Spider has modified registry keys to prepare for ransomware execution and to disable common administrative utilities. [93] |
| S0260 | InvisiMole | InvisiMole has a command to create, set, copy, or delete a specified Registry key or value. [94] [95] |
| S1132 | IPsec Helper | IPsec Helper can make arbitrary changes to registry keys based on provided input. [96] |
| S1190 | Kapeka | Kapeka writes persistent configuration information to the victim host registry. [97] |
| S0271 | KEYMARBLE | KEYMARBLE has a command to create Registry entries for storing data under HKEY_CURRENT_USER\SOFTWARE\Microsoft\WABE\DataPath . [98] |
| G0094 | Kimsuky | Kimsuky has modified Registry settings for default file associations to enable all macros and for persistence. [99] [100] [101] [102] Kimsuky has also modified the registry entry for HKCU:\Software\Microsoft\Windows\CurrentVersion\Run registry key for persistence with the name WindowsSecurityCheck. [103] |
| S0669 | KOCTOPUS | KOCTOPUS has added and deleted keys from the Registry. [104] |
| S0356 | KONNI | KONNI has modified registry keys of ComSysApp, Svchost, and xmlProv on the machine to gain persistence. [105] [106] |
| S1199 | LockBit 2.0 | LockBit 2.0 can create Registry keys to bypass UAC and for persistence. [107] |
| S1202 | LockBit 3.0 | LockBit 3.0 can change the Registry values for Group Policy refresh time, to disable SmartScreen, and to disable Windows Defender. [108] [109] |
| S0397 | LoJax | LoJax has modified the Registry key ‘HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\BootExecute’ from ‘autocheck autochk ’ to ‘autocheck autoche ’ . [110] |
| S0447 | Lokibot | Lokibot has modified the Registry as part of its UAC bypass process. [111] |
| G0030 | Lotus Blossom | Lotus Blossom has installed tools such as Sagerunex by writing them to the Windows registry. [112] |
| G1014 | LuminousMoth | LuminousMoth has used malware that adds Registry keys for persistence. [113] [114] |
| S1060 | Mafalda | Mafalda can manipulate the system registry on a compromised host. [115] |
| G0059 | Magic Hound | Magic Hound has modified Registry settings for security tools. [116] |
| G1051 | Medusa Group | Medusa Group has modified Registry keys to elevate privileges, maintain persistence and allow remote access. [117] |
| S0576 | MegaCortex | MegaCortex has added entries to the Registry for ransom contact information. [118] |
| S1059 | metaMain | metaMain can write the process ID of a target process into the HKEY_LOCAL_MACHINE\SOFTWARE\DDE\tpid Registry value as part of its reflective loading activity. [115] |
| S0455 | Metamorfo | Metamorfo has written process names to the Registry, disabled IE browser features, deleted Registry keys, and changed the ExtendedUIHoverTime key. [119] [120] [121] [122] |
| S1047 | Mori | Mori can write data to HKLM\Software\NFC\IPA and HKLM\Software\NFC\ and delete Registry values. [123] [124] |
| S0256 | Mosquito | Mosquito can modify Registry keys under HKCU\Software\Microsoft[dllname] to store configuration values. Mosquito also modifies Registry keys under HKCR\CLSID...\InprocServer32 with a path to the launcher. [125] |
| S9032 | MuddyViper | MuddyViper has the ability to clear the Registry values in the Windows Startup folder that were previously set for persistence. [126] |
| S0205 | Naid | Naid creates Registry entries that store information about a created service and point to a malicious DLL dropped to disk. [127] |
| S0336 | NanoCore | NanoCore has the capability to edit the Registry. [128] [129] |
| S0691 | Neoichor | Neoichor has the ability to configure browser settings by modifying Registry entries under HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer . [130] |
| S0210 | Nerex | Nerex creates a Registry subkey that registers a new service. [131] |
| S0457 | Netwalker | Netwalker can add the following registry entry: HKEY_CURRENT_USER\SOFTWARE{8 random characters} . [132] |
| S0198 | NETWIRE | NETWIRE can modify the Registry to store its configuration information. [133] |
| C0002 | Night Dragon | During Night Dragon , threat actors used zwShell to establish full remote control of the connected machine and manipulate the Registry. [134] |
| S1090 | NightClub | NightClub can modify the Registry to set the ServiceDLL for a service created by the malware for persistence. [135] |
| S0385 | njRAT | njRAT can create, delete, or modify a specified Registry key or value. [136] [137] |
| S9025 | NOOPLDR | NOOPLDR can store its payload in the Registry using a random hex string in HKCU\SOFTWARE\Microsoft\COM3 . [138] |
| S1131 | NPPSPY | NPPSPY modifies the Registry to record the malicious listener for output from the Winlogon process. [139] |
| G0049 | OilRig | OilRig has used reg.exe to modify system configuration. [140] [141] |
| C0006 | Operation Honeybee | During Operation Honeybee , the threat actors used batch files that modified registry keys. [142] |
| C0014 | Operation Wocao | During Operation Wocao , the threat actors enabled Wdigest by changing the HKLM\SYSTEM\\ControlSet001\\Control\\SecurityProviders\\WDigest registry value from 0 (disabled) to 1 (enabled). [143] |
| S0229 | Orz | Orz can perform Registry operations. [144] |
| S0664 | Pandora | Pandora can write an encrypted token to the Registry to enable processing of remote commands. [145] |
| G0040 | Patchwork | A Patchwork payload deletes Resiliency Registry keys created by Microsoft Office applications in an apparent effort to trick users into thinking there were no issues during application runs. [146] |
| S1050 | PcShare | PcShare can delete its persistence mechanisms from the registry. [147] |
| S0158 | PHOREAL | PHOREAL is capable of manipulating the Registry. [148] |
| S0517 | Pillowmint | Pillowmint has modified the Registry key HKLM\SOFTWARE\Microsoft\DRM to store a malicious payload. [149] |
| S0501 | PipeMon | PipeMon has modified the Registry to store its encrypted payload. [150] |
| S0254 | PLAINTEE | PLAINTEE uses reg add to add a Registry Run key for persistence. [151] |
| S0013 | PlugX | PlugX has a module to create, delete, or modify Registry keys. [152] [153] [154] |
| S0428 | PoetRAT | PoetRAT has made registry modifications to alter its behavior upon execution. [155] |
| S0012 | PoisonIvy | PoisonIvy creates a Registry subkey that registers a new system device. [156] |
| S0518 | PolyglotDuke | PolyglotDuke can write encrypted JSON configuration files to the Registry. [157] |
| S0441 | PowerShower | PowerShower has added a registry key so future powershell.exe instances are spawned off-screen by default, and has removed all registry entries that are left behind during the dropper process. [158] |
| S1058 | Prestige | Prestige has the ability to register new registry keys for a new extension handler via HKCR\.enc and HKCR\enc\shell\open\command . [159] |
| S0583 | Pysa | Pysa has modified the registry key "SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" and added the ransom note. [160] |
| S0650 | QakBot | QakBot can modify the Registry to store its configuration information in a randomly named subkey under HKCU\Software\Microsoft . [161] [162] |
| S1242 | Qilin | Qilin can make Registry modifications to share networked drives between elevated and non-elevated processes and to increase the number of outstanding network requests per client. [163] [164] Qilin can also modify HKEY_CURRENT_USER\Control Panel\Desktop\Wallpaper to enable posting of ransom messages. [165] |
| S0269 | QUADAGENT | QUADAGENT modifies an HKCU Registry key to store a session identifier unique to the compromised system as well as a pre-shared key used for encrypting and decrypting C2 communications. [166] |
| S0262 | QuasarRAT | QuasarRAT has a command to edit the Registry on the victim’s machine. [167] [168] |
| S0662 | RCSession | RCSession can write its configuration file to the Registry. [49] [169] |
| S0075 | Reg | Reg may be used to interact with and modify the Windows Registry of a local or remote system at the command-line interface. [1] |
| S0511 | RegDuke | RegDuke can create seemingly legitimate Registry key to store its encryption key. [157] |
| S0019 | Regin | Regin appears to have functionality to modify remote Registry information. [170] |
| S0332 | Remcos | Remcos has full control of the Registry, including the ability to modify it. [171] [172] |
| S0496 | REvil | REvil can modify the Registry to save encryption parameters and system information. [173] [174] [175] [176] [177] |
| S0240 | ROKRAT | ROKRAT can modify the HKEY_CURRENT_USER\Software\Microsoft\Office\ registry key so it can bypass the VB object model (VBOM) on a compromised host. [178] |
| S0090 | Rover | Rover has functionality to remove Registry Run key persistence as a cleanup procedure. [179] |
| S0148 | RTM | RTM can delete all Registry entries created during its execution. [180] |
| G1031 | Saint Bear | Saint Bear will leverage malicious Windows batch scripts to modify registry values associated with Windows Defender functionality. [181] |
| S1099 | Samurai | The Samurai loader component can create multiple Registry keys to force the svchost.exe process to load the final backdoor. [182] |
| S0596 | ShadowPad | ShadowPad can modify the Registry to store and maintain a configuration block and virtual file system. [183] [65] |
| S0140 | Shamoon | Once Shamoon has access to a network share, it enables the RemoteRegistry service on the target system. It will then connect to the system with RegConnectRegistryW and modify the Registry to disable UAC remote restrictions by setting SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy to 1. [184] [185] [186] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors, including Storm-2603, disabled security services via Registry modifications. [187] |
| S0444 | ShimRat | ShimRat has registered two registry keys for shim databases. [188] |
| S1178 | ShrinkLocker | ShrinkLocker modifies various registry keys associated with system logon and BitLocker functionality to effectively lock-out users following disk encryption. [189] [190] |
| S0589 | Sibot | Sibot has modified the Registry to install a second-stage script in the HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\sibot . [191] |
| G0091 | Silence | Silence can create, delete, or modify a specified Registry key or value. [192] |
| S0692 | SILENTTRINITY | SILENTTRINITY can modify registry keys, including to enable or disable Remote Desktop Protocol (RDP). [193] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA can add, modify, and/or delete registry keys. It has changed the proxy configuration of a victim system by modifying the HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap registry. [194] |
| S0649 | SMOKEDHAM | SMOKEDHAM has modified registry keys for persistence, to enable credential caching for credential access, and to facilitate lateral movement via RDP. [195] |
| S0157 | SOUNDBITE | SOUNDBITE is capable of modifying the Registry. [148] |
| S0142 | StreamEx | StreamEx has the ability to modify the Registry. [196] |
| S0603 | Stuxnet | Stuxnet can create registry keys to load driver files. [197] |
| S0559 | SUNBURST | SUNBURST had commands that allow an attacker to write or delete registry keys, and was observed stopping services by setting their HKLM\SYSTEM\CurrentControlSet\services\[service_name]\Start registry entries to value 4. [198] [199] It also deleted previously-created Image File Execution Options (IFEO) Debugger registry values and registry keys related to HTTP proxy to clean up traces of its activity. [200] |
| S0242 | SynAck | SynAck can manipulate Registry keys. [201] |
| S0663 | SysUpdate | SysUpdate can write its configuration file to Software\Classes\scConfig in either HKEY_LOCAL_MACHINE or HKEY_CURRENT_USER . [145] |
| G0092 | TA505 | TA505 has used malware to disable Windows Defender through modification of the Registry. [202] |
| S0011 | Taidoor | Taidoor has the ability to modify the Registry on compromised hosts using RegDeleteValueA and RegCreateKeyExA . [203] |
| S0467 | TajMahal | TajMahal can set the KeepPrintedJobs attribute for configured printers in SOFTWARE\Microsoft\Windows NT\CurrentVersion\Print\Printers to enable document stealing. [204] |
| S1011 | Tarrask | Tarrask is able to delete the Security Descriptor ( SD ) registry subkey in order to "hide" scheduled tasks. [205] |
| S0560 | TEARDROP | TEARDROP modified the Registry to create a Windows service for itself on a compromised host. [206] |
| G0027 | Threat Group-3390 | A Threat Group-3390 tool has created new Registry keys under HKEY_CURRENT_USER\Software\Classes\ and HKLM\SYSTEM\CurrentControlSet\services . [207] [145] |
| S0665 | ThreatNeedle | ThreatNeedle can modify the Registry to save its configuration data as the following RC4-encrypted Registry key: HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\GameCon . [208] |
| S0668 | TinyTurla | TinyTurla can set its configuration parameters in the Registry. [209] |
| S1201 | TRANSLATEXT | TRANSLATEXT has modified the following registry key to install itself as the value, granting permission to install specified extensions: HKCU\Software\Policies\Google\Chrome\ExtensionInstallForcelist . [210] |
| S0266 | TrickBot | TrickBot can modify registry entries. [211] |
| G0010 | Turla | Turla has modified Registry values to store payloads. [212] [213] |
| S0263 | TYPEFRAME | TYPEFRAME can install encrypted configuration data under the Registry key HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\ShellCompatibility\Applications\laxhost.dll and HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\PrintConfigs . [214] |
| S0022 | Uroburos | Uroburos can store configuration information in the Registry including the initialization vector and AES key needed to find and decrypt other Uroburos components. [215] |
| S0386 | Ursnif | Ursnif has used Registry modifications as part of its installation routine. [216] [217] |
| S0476 | Valak | Valak has the ability to modify the Registry key HKCU\Software\ApplicationContainer\Appsw64 to store information regarding the C2 server and downloads. [218] [219] [220] |
| S0180 | Volgmer | Volgmer modifies the Registry to store an encoded configuration file in HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Security . [221] [222] |
| G1017 | Volt Typhoon | Volt Typhoon has used netsh to create a PortProxy Registry modification on a compromised server running the Paessler Router Traffic Grapher (PRTG). [223] |
| S0670 | WarzoneRAT | WarzoneRAT can create HKCU\Software\Classes\Folder\shell\open\command as a new registry key during privilege escalation. [224] [225] |
| S0612 | WastedLocker | WastedLocker can modify registry values within the Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap registry key. [226] |
| S0579 | Waterbear | Waterbear has deleted certain values from the Registry to load a malicious DLL. [227] |
| G0102 | Wizard Spider | Wizard Spider has modified the Registry key HKLM\System\CurrentControlSet\Control\SecurityProviders\WDigest by setting the UseLogonCredential registry value to 1 in order to force credentials to be stored in clear text in memory. Wizard Spider has also modified the WDigest registry key to allow plaintext credentials to be cached in memory. [228] [229] |
| S0330 | Zeus Panda | Zeus Panda modifies several Registry keys under HKCU\Software\Microsoft\Internet Explorer\ PhishingFilter\ to disable phishing filters. [230] |
| S0350 | zwShell | zwShell can modify the Registry. [134] |
| S0412 | ZxShell | ZxShell can create Registry entries to enable services to run. [231] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1024 | Restrict Registry Permissions | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0280 | Behavior-Based Registry Modification Detection on Windows | AN0781 | Behavior chain involving abnormal registry modifications via CLI, PowerShell, WMI, or direct API calls, especially targeting persistence, privilege escalation, or defense evasion keys, potentially followed by service restart or process execution. Such as editing Notify/Userinit/Startup keys, or disabling SafeDllSearchMode. |

---

## References

- [Microsoft. (2012, April 17). Reg. Retrieved May 1, 2015.](https://technet.microsoft.com/en-us/library/cc732643.aspx)
- [Unit 42. (2019, February 22). New BabyShark Malware Targets U.S. National Security Think Tanks. Retrieved October 7, 2019.](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
- [Javier Yuste and Sergio Pastrana. (2021). Avaddon ransomware: an in-depth analysis and decryption of infected systems. Retrieved March 24, 2025.](https://arxiv.org/pdf/2102.04796)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [CISA. (2018, March 16). Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved March 24, 2025.](https://www.cisa.gov/news-events/alerts/2018/03/15/russian-government-cyber-activity-targeting-energy-and-other-critical-infrastructure-sectors)
- [CISA. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved March 24, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-075a)
- [Microsoft. (n.d.). Enable the Remote Registry Service. Retrieved May 1, 2015.](https://technet.microsoft.com/en-us/library/cc754820.aspx)
- [Russinovich, M. & Sharkey, K. (2006, January 10). Reghide. Retrieved August 9, 2018.](https://docs.microsoft.com/sysinternals/downloads/reghide)
- [Santos, R. (2014, August 1). POWELIKS: Malware Hides In Windows Registry. Retrieved August 9, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/poweliks-malware-hides-in-windows-registry/)
- [Reitz, B. (2017, July 14). Hiding Registry keys with PSReflect. Retrieved August 9, 2018.](https://posts.specterops.io/hiding-registry-keys-with-psreflect-b18ec5ac8353)
- [Booz Allen Hamilton. (2016). When The Lights Went Out. Retrieved December 18, 2024.](https://www.boozallen.com/content/dam/boozallen/documents/2016/09/ukraine-report-when-the-lights-went-out.pdf)
- [Dr. Nestori Syynimaa. (2018, October 25). AADInternals. Retrieved February 18, 2022.](https://o365blog.com/aadinternals)
- [Bitdefender. (2015, December). APT28 Under the Scope. Retrieved February 23, 2017.](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
- [Walter, J. (2020, August 10). Agent Tesla | Old RAT Uses New Tricks to Stay on Top. Retrieved December 11, 2020.](https://labs.sentinelone.com/agent-tesla-old-rat-uses-new-tricks-to-stay-on-top/)
- [Kasuya, M. (2020, January 8). Threat Spotlight: Amadey Bot Targets Non-Russian Users. Retrieved July 14, 2022.](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
- [Grunzweig, J., Lee, B. (2016, January 22). New Attacks Linked to C0d0so0 Group. Retrieved August 2, 2018.](https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/)
- [Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)
- [FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [Rostovcev, N. (2021, June 10). Big airline heist APT41 likely behind a third-party attack on Air India. Retrieved August 26, 2021.](https://www.group-ib.com/blog/colunmtk-apt41/)
- [Mandiant. (n.d.). APT42: Crooked Charms, Cons and Compromises. Retrieved October 9, 2024.](https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf)
- [CrowdStrike. (2023). 2022 Falcon OverWatch Threat Hunting Report. Retrieved May 20, 2024.](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [Yuste, J. Pastrana, S. (2021, February 9). Avaddon ransomware: an in-depth analysis and decryption of infected systems. Retrieved August 19, 2021.](https://arxiv.org/pdf/2102.04796.pdf)
- [FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved November 17, 2024.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
- [US-CERT. (2018, February 06). Malware Analysis Report (MAR) - 10135536-G. Retrieved June 7, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)
- [US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [Frankoff, S., Hartley, B. (2018, November 14). Big Game Hunting: The Evolution of INDRIK SPIDER From Dridex Wire Fraud to BitPaymer Targeted Ransomware. Retrieved January 6, 2021.](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
- [Zargarov, N. (2022, May 2). New Black Basta Ransomware Hijacks Windows Fax Service. Retrieved March 7, 2023.](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
- [Cyble. (2022, May 6). New ransomware variant targeting high-value organizations. Retrieved November 17, 2024.](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
- [Gonzalez, I., Chavez I., et al. (2022, May 9). Examining the Black Basta Ransomware’s Infection Routine. Retrieved March 7, 2023.](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)
- [Inman, R. and Gurney, P. (2022, June 6). Shining the Light on Black Basta. Retrieved March 8, 2023.](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)
- [Vilkomir-Preisman, S. (2022, August 18). Beating Black Basta Ransomware. Retrieved March 8, 2023.](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)
- [Elsad, A. (2022, August 25). Threat Assessment: Black Basta Ransomware. Retrieved March 8, 2023.](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)
- [Huseyin Can Yuceel. (2022, February 21). TTPs used by BlackByte Ransomware Targeting Critical Infrastructure. Retrieved December 16, 2024.](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)
- [James Nutland, Craig Jackson, Terryn Valikodath, & Brennan Evans. (2024, August 28). BlackByte blends tried-and-true tradecraft with newly disclosed vulnerabilities to support ongoing attacks. Retrieved December 16, 2024.](https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [Lambert, T. (2020, May 7). Introducing Blue Mockingbird. Retrieved May 26, 2020.](https://redcanary.com/blog/blue-mockingbird-cryptominer/)
- [Robert Falcone, Mike Scott, Juan Cortes. (2015, November 10). Bookworm Trojan: A Model of Modular Architecture. Retrieved July 21, 2025.](https://unit42.paloaltonetworks.com/bookworm-trojan-a-model-of-modular-architecture/)
- [Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
- [Balanza, M. (2018, April 02). Infostealer.Catchamas. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165711/https://www-west.symantec.com/content/symantec/english/en/security-center/writeup.html/2018-040209-1742-99)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Salem, E. (2020, November 17). CHAES: Novel Malware Targeting Latin American E-Commerce. Retrieved June 30, 2021.](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Cybereason Nocturnus. (2020, December 23). Cybereason vs. Clop Ransomware. Retrieved May 11, 2021.](https://www.cybereason.com/blog/cybereason-vs.-clop-ransomware)
- [Mavis, N. (2020, September 21). The Art and Science of Detecting Cobalt Strike. Retrieved September 12, 2024.](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [CISA. (2020, October 29). Malware Analysis Report (AR20-303A). Retrieved December 9, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303a)
- [Burton, K. (n.d.). The Conficker Worm. Retrieved February 18, 2021.](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
- [Trend Micro. (2014, March 18). Conficker. Retrieved February 18, 2021.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/conficker)
- [byt3bl33d3r. (2018, September 8). SMB: Command Reference. Retrieved July 17, 2020.](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Dahan, A. et al. (2020, November 2). Back to the Future: Inside the Kimsuky KGH Spyware Suite. Retrieved November 6, 2020.](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
- [TrendMicro. (2014, September 03). DARKCOMET. Retrieved November 6, 2018.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
- [Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [Checkpoint Research. (2021, November 15). Uncovering MosesStaff techniques: Ideology over Money. Retrieved August 11, 2022.](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [Chen, J., et al. (2022). Delving Deep: An Analysis of Earth Lusca’s Operations. Retrieved July 1, 2022.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
- [Jan Holman, Tomas Zvara. (2024, October 23). Embargo ransomware: Rock’n’Rust. Retrieved October 19, 2025.](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
- [Microsoft Threat Intelligence. (2023, June 14). Cadet Blizzard emerges as a novel and distinct Russian threat actor. Retrieved July 10, 2023.](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)
- [Adamitis, D. (2020, May 6). Phantom in the Command Shell. Retrieved November 17, 2024.](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
- [Cherepanov, A., Lipovsky, R. (2018, October 11). New TeleBots backdoor: First evidence linking Industroyer to NotPetya. Retrieved November 27, 2018.](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)
- [Threat Intelligence and Research. (2015, March 30). VOLATILE CEDAR. Retrieved February 8, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
- [Patil, S. (2018, June 26). Microsoft Office Vulnerabilities Used to Distribute FELIXROOT Backdoor in Recent Campaign. Retrieved November 17, 2024.](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
- [Yamout, M. (2021, November 29). WIRTE’s campaign in the Middle East ‘living off the land’ since at least 2019. Retrieved February 1, 2022.](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
- [Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy: New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [CERT-EE. (2021, January 27). Gamaredon Infection: From Dropper to Entry. Retrieved February 17, 2022.](https://www.ria.ee/sites/default/files/content-editors/kuberturve/tale_of_gamaredon_infection.pdf)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Threat Hunter Team, Symantec and Carbon Black. (2025, April 10). Shuckworm Targets Foreign Military Mission Based in Ukraine. Retrieved July 23, 2025.](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Quinn, J. (2019, March 25). The odd case of a Gh0stRAT variant. Retrieved July 15, 2020.](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
- [Falcone, R., et al. (2018, August 02). The Gorgon Group: Slithering Between Nation State and Cybercrime. Retrieved August 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
- [Guerrero-Saade, J. (2022, February 23). HermeticWiper | New Destructive Malware Used In Cyber Attacks on Ukraine. Retrieved March 25, 2022.](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
- [Thomas, W. et al. (2022, February 25). CrowdStrike Falcon Protects from New Wiper Malware Used in Ukraine Cyberattacks. Retrieved March 25, 2022.](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
- [Dani, M. (2022, March 1). Ukrainian Targets Hit by HermeticWiper, New Datawiper Malware. Retrieved March 25, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
- [Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
- [Accenture. (2020, October). Turla uses HyperStack, Carbon, and Kazuar to compromise government entity. Retrieved December 2, 2020.](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)
- [Mandiant Intelligence. (2022, June 2). To HADES and Back: UNC2165 Shifts to LOCKBIT to Evade Sanctions. Retrieved July 29, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [Mohammad Kazem Hassan Nejad, WithSecure. (2024, April 17). KAPEKA A novel backdoor spotted in Eastern Europe. Retrieved January 6, 2025.](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)
- [US-CERT. (2018, August 09). MAR-10135536-17 – North Korean Trojan: KEYMARBLE. Retrieved August 16, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
- [CISA, FBI, CNMF. (2020, October 27). https://us-cert.cisa.gov/ncas/alerts/aa20-301a. Retrieved November 4, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-301a)
- [Crowdstrike. (2020, March 2). 2020 Global Threat Report. Retrieved December 11, 2020.](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [KISA. (2021). Phishing Target Reconnaissance and Attack Resource Analysis Operation Muzabi. Retrieved March 8, 2024.](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Jazi, H. (2021, February). LazyScripter: From Empire to double RAT. Retrieved November 17, 2024.](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
- [Karmi, D. (2020, January 4). A Look Into Konni 2019 Campaign. Retrieved April 28, 2020.](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)
- [Threat Intelligence Team. (2021, August 23). New variant of Konni malware used in campaign targetting Russia. Retrieved January 5, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
- [FBI. (2022, February 4). Indicators of Compromise Associated with LockBit 2.0 Ransomware. Retrieved January 24, 2025.](https://www.ic3.gov/CSA/2022/220204.pdf)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [INCIBE-CERT. (2024, March 14). LockBit: response and recovery actions. Retrieved February 5, 2025.](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
- [ESET. (2018, September). LOJAX First UEFI rootkit found in the wild, courtesy of the Sednit group. Retrieved July 2, 2019.](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)
- [Muhammad, I., Unterbrink, H.. (2021, January 6). A Deep Dive into Lokibot Infection Chain. Retrieved August 31, 2021.](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [Lechtik, M, and etl. (2021, July 14). LuminousMoth APT: Sweeping attacks for the chosen few. Retrieved October 20, 2022.](https://securelist.com/apt-luminousmoth/103332/)
- [Botezatu, B and etl. (2021, July 21). LuminousMoth - PlugX, File Exfiltration and Persistence Revisited. Retrieved October 20, 2022.](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [DFIR Report. (2022, March 21). APT35 Automates Initial Access Using ProxyShell. Retrieved May 25, 2022.](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Del Fierro, C. Kessem, L.. (2020, January 8). From Mega to Giga: Cross-Version Comparison of Top MegaCortex Modifications. Retrieved February 15, 2021.](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
- [Erlich, C. (2020, April 3). The Avast Abuser: Metamorfo Banking Malware Hides By Abusing Avast Executable. Retrieved May 26, 2020.](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
- [Zhang, X. (2020, February 4). Another Metamorfo Variant Targeting Customers of Financial Institutions in More Countries. Retrieved July 30, 2020.](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
- [Sierra, E., Iglesias, G.. (2018, April 24). Metamorfo Campaigns Targeting Brazilian Users. Retrieved July 30, 2020.](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
- [ESET Research. (2019, October 3). Casbaneiro: peculiarities of this banking Trojan that affects Brazil and Mexico. Retrieved September 23, 2021.](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
- [FBI, CISA, CNMF, NCSC-UK. (2022, February 24). Iranian Government-Sponsored Actors Conduct Cyber Operations Against Global Government and Commercial Networks. Retrieved September 27, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
- [Cyber National Mission Force. (2022, January 12). Iranian intel cyber suite of malware uses open source tools. Retrieved September 30, 2022.](https://www.cybercom.mil/Media/News/Article/2897570/iranian-intel-cyber-suite-of-malware-uses-open-source-tools/)
- [ESET, et al. (2018, January). Diplomats in Eastern Europe bitten by a Turla mosquito. Retrieved July 3, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
- [ESET Research. (2025, December 2). MuddyWater: Snakes by the riverbank. Retrieved February 17, 2026.](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
- [Neville, A. (2012, June 15). Trojan.Naid. Retrieved February 22, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-061518-4639-99)
- [The DigiTrust Group. (2017, January 01). NanoCore Is Not Your Average RAT. Retrieved November 9, 2018.](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
- [Kasza, A., Halfpop, T. (2016, February 09). NanoCoreRAT Behind an Increase in Tax-Themed Phishing E-mails. Retrieved November 9, 2018.](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Ladley, F. (2012, May 15). Backdoor.Nerex. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051515-3445-99)
- [Victor, K.. (2020, May 18). Netwalker Fileless Ransomware Injected via Reflective Loading . Retrieved May 26, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
- [Lambert, T. (2020, January 29). Intro to Netwire. Retrieved January 7, 2021.](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
- [McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Fidelis Cybersecurity. (2013, June 28). Fidelis Threat Advisory #1009: "njRAT" Uncovered. Retrieved June 4, 2019.](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
- [Pascual, C. (2018, November 27). AutoIt-Compiled Worm Affecting Removable Media Delivers Fileless Version of BLADABINDI/njRAT Backdoor. Retrieved June 4, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [Dray Agha. (2022, August 16). Cleartext Shenanigans: Gifting User Passwords to Adversaries With NPPSPY. Retrieved May 17, 2024.](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
- [Symantec Threat Hunter Team. (2023, October 19). Crambus: New Campaign Targets Middle Eastern Government. Retrieved November 27, 2024.](https://www.security.com/threat-intelligence/crambus-middle-east-government)
- [Fahmy, M. et al. (2024, October 11). Earth Simnavaz (aka APT34) Levies Advanced Cyberattacks Against Middle East. Retrieved November 27, 2024.](https://www.trendmicro.com/en_us/research/24/j/earth-simnavaz-cyberattacks.html)
- [Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-uncovers-operation-honeybee-malicious-document-campaign-targeting-humanitarian-aid-groups/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
- [Lunghi, D. and Lu, K. (2021, April 9). Iron Tiger APT Updates Toolkit With Evolved SysUpdate Malware. Retrieved November 12, 2021.](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
- [Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
- [Trustwave SpiderLabs. (2020, June 22). Pillowmint: FIN7’s Monkey Thief . Retrieved July 27, 2020.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
- [Tartare, M. et al. (2020, May 21). No “Game over” for the Winnti Group. Retrieved August 24, 2020.](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
- [Ash, B., et al. (2018, June 26). RANCOR: Targeted Attacks in South East Asia Using PLAINTEE and DDKONG Malware Families. Retrieved July 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
- [DOJ. (2024, December 20). Mag. No. 24-mj-1387 AFFIDAVIT IN SUPPORT OF AN APPLICATION FOR A NINTH SEARCH AND SEIZURE WARRANT- IN THE MATTER OF THE SEARCH AND SEIZURE OF COMPUTERS IN THE UNITED STATES INFECTED WITH PLUGX MALWARE . Retrieved September 9, 2025.](https://www.justice.gov/archives/opa/media/1384136/dl)
- [Mercer, W, et al. (2020, April 16). PoetRAT: Python RAT uses COVID-19 lures to target Azerbaijan public and private sectors. Retrieved April 27, 2020.](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
- [Hayashi, K. (2005, August 18). Backdoor.Darkmoon. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Lancaster, T. (2018, November 5). Inception Attackers Target Europe with Year-old Office Vulnerability. Retrieved May 8, 2020.](https://unit42.paloaltonetworks.com/unit42-inception-attackers-target-europe-year-old-office-vulnerability/)
- [MSTIC. (2022, October 14). New “Prestige” ransomware impacts organizations in Ukraine and Poland. Retrieved January 19, 2023.](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
- [CERT-FR. (2020, April 1). ATTACKS INVOLVING THE MESPINOZA/PYSA RANSOMWARE. Retrieved March 1, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
- [Rainey, K. (n.d.). Qbot. Retrieved September 27, 2021.](https://redcanary.com/threat-detection-report/threats/qbot/)
- [Group IB. (2020, September). LOCK LIKE A PRO. Retrieved November 17, 2024.](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
- [Halcyon RISE Team. (2024, October 24). New Qilin.B Ransomware Variant Boasts Enhanced Encryption and Defense Evasion. Retrieved September 26, 2025.](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
- [Hacioglu, S. (2025, March 10). Qilin Ransomware: Exposing the TTPs Behind One of the Most Active Ransomware Campaigns of 2024. Retrieved September 26, 2025.](https://www.picussecurity.com/resource/blog/qilin-ransomware)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [Lee, B., Falcone, R. (2018, July 25). OilRig Targets Technology Service Provider and Government Agency with QUADAGENT. Retrieved August 9, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)
- [MaxXor. (n.d.). QuasarRAT. Retrieved July 10, 2018.](https://github.com/quasar/QuasarRAT)
- [CISA. (2018, December 18). Analysis Report (AR18-352A) Quasar Open-Source Remote Administration Tool. Retrieved August 1, 2022.](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
- [Global Threat Center, Intelligence Team. (2020, December). APT27 Turns to Ransomware. Retrieved November 12, 2021.](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, November 24). THE REGIN PLATFORM NATION-STATE OWNAGE OF GSM NETWORKS. Retrieved December 1, 2014.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070305/Kaspersky_Lab_whitepaper_Regin_platform_eng.pdf)
- [Klijnsma, Y. (2018, January 23). Espionage Campaign Leverages Spear Phishing, RATs Against Turkish Defense Contractors. Retrieved November 6, 2018.](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Cylance. (2019, July 3). hreat Spotlight: Sodinokibi Ransomware. Retrieved August 4, 2020.](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
- [Secureworks . (2019, September 24). REvil: The GandCrab Connection. Retrieved August 4, 2020.](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
- [McAfee. (2019, October 2). McAfee ATR Analyzes Sodinokibi aka REvil Ransomware-as-a-Service – What The Code Tells Us. Retrieved August 4, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
- [Intel 471 Malware Intelligence team. (2020, March 31). REvil Ransomware-as-a-Service – An analysis of a ransomware affiliate operation. Retrieved August 4, 2020.](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [Jazi, Hossein. (2021, January 6). Retrohunting APT37: North Korean APT used VBA self decode technique to inject RokRat. Retrieved March 22, 2022.](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
- [Ray, V., Hayashi, K. (2016, February 29). New Malware ‘Rover’ Targets Indian Ambassador to Afghanistan. Retrieved February 29, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
- [Faou, M. and Boutin, J. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Kaspersky Lab. (2017, August). ShadowPad: popular server management software hit in supply chain attack. Retrieved March 22, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
- [FireEye. (2016, November 30). FireEye Responds to Wave of Destructive Cyber Attacks in Gulf Region. Retrieved November 17, 2024.](https://web.archive.org/web/20210126065851/https://www.fireeye.com/blog/threat-research/2016/11/fireeye_respondsto.html)
- [Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [Mundo, A., Roccia, T., Saavedra-Morales, J., Beek, C.. (2018, December 14). Shamoon Returns to Wipe Systems in Middle East, Europe . Retrieved May 29, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/)
- [Microsoft Threat Intelligence. (2025, July 22). Disrupting active exploitation of on-premises SharePoint vulnerabilities. Retrieved October 15, 2025.](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/#storm-2603)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Cristian Souza, Eduardo Ovalle, Ashley Muñoz, & Christopher Zachor. (2024, May 23). ShrinkLocker: Turning BitLocker into ransomware. Retrieved December 7, 2024.](https://securelist.com/ransomware-abuses-bitlocker/112643/)
- [Splunk Threat Research Team , Teoderick Contreras. (2024, September 5). ShrinkLocker Malware: Abusing BitLocker to Lock Your Data. Retrieved December 7, 2024.](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [Group-IB. (2018, September). Silence: Moving Into the Darkside. Retrieved May 5, 2020.](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [FireEye. (2021, June 16). Smoking Out a DARKSIDE Affiliate’s Supply Chain Software Compromise. Retrieved September 22, 2021.](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
- [Cylance SPEAR Team. (2017, February 9). Shell Crew Variants Continue to Fly Under Big AV’s Radar. Retrieved February 15, 2017.](https://www.cylance.com/shell-crew-variants-continue-to-fly-under-big-avs-radar)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [MSTIC. (2020, December 18). Analyzing Solorigate, the compromised DLL file that started a sophisticated cyberattack, and how Microsoft Defender helps protect customers . Retrieved January 5, 2021.](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)
- [MSTIC, CDOC, 365 Defender Research Team. (2021, January 20). Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop . Retrieved January 22, 2021.](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
- [Ivanov, A. et al. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [CISA, FBI, DOD. (2021, August). MAR-10292089-1.v2 – Chinese Remote Access Trojan: TAIDOOR. Retrieved August 24, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Microsoft Threat Intelligence Team & Detection and Response Team . (2022, April 12). Tarrask malware uses scheduled tasks for defense evasion. Retrieved June 1, 2022.](https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/)
- [Check Point Research. (2020, December 22). SUNBURST, TEARDROP and the NetSec New Normal. Retrieved January 6, 2021.](https://research.checkpoint.com/2020/sunburst-teardrop-and-the-netsec-new-normal/)
- [Pantazopoulos, N., Henry T. (2018, May 18). Emissary Panda – A potential new malicious tool. Retrieved June 25, 2018.](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)
- [Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle. Retrieved October 27, 2021.](https://securelist.com/lazarus-threatneedle/100803/)
- [Cisco Talos. (2021, September 21). TinyTurla - Turla deploys new malware to keep a secret backdoor on victim machines. Retrieved December 2, 2021.](https://blog.talosintelligence.com/2021/09/tinyturla.html)
- [Park, S. (2024, June 27). Kimsuky deploys TRANSLATEXT to target South Korean academia. Retrieved October 14, 2024.](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
- [Anthony, N., Pascual, C.. (2018, November 1). Trickbot Shows Off New Trick: Password Grabber Module. Retrieved November 16, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [Symantec DeepSight Adversary Intelligence Team. (2019, June 20). Waterbug: Espionage Group Rolls Out Brand-New Toolset in Attacks Against Governments. Retrieved July 8, 2019.](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)
- [US-CERT. (2018, June 14). MAR-10135536-12 – North Korean Trojan: TYPEFRAME. Retrieved July 13, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Sioting, S. (2013, June 15). BKDR_URSNIF.SM. Retrieved June 5, 2019.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
- [Proofpoint Staff. (2016, August 25). Nightmare on Tor Street: Ursnif variant Dreambot adds Tor functionality. Retrieved June 5, 2019.](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)
- [Salem, E. et al. (2020, May 28). VALAK: MORE THAN MEETS THE EYE . Retrieved June 19, 2020.](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
- [Duncan, B. (2020, July 24). Evolution of Valak, from Its Beginnings to Mass Distribution. Retrieved August 31, 2020.](https://unit42.paloaltonetworks.com/valak-evolution/)
- [Reaves, J. and Platt, J. (2020, June). Valak Malware and the Connection to Gozi Loader ConfCrew. Retrieved August 31, 2020.](https://assets.sentinelone.com/labs/sentinel-one-valak-i)
- [US-CERT. (2017, November 01). Malware Analysis Report (MAR) - 10135536-D. Retrieved July 16, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)
- [Yagi, J. (2014, August 24). Trojan.Volgmer. Retrieved July 16, 2018.](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Mohanta, A. (2020, November 25). Warzone RAT comes with UAC bypass technique. Retrieved April 7, 2022.](https://www.uptycs.com/blog/warzone-rat-comes-with-uac-bypass-technique)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [Antenucci, S., Pantazopoulos, N., Sandee, M. (2020, June 23). WastedLocker: A New Ransomware Variant Developed By The Evil Corp Group. Retrieved September 14, 2021.](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
- [Su, V. et al. (2019, December 11). Waterbear Returns, Uses API Hooking to Evade Security. Retrieved February 22, 2021.](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
- [John, E. and Carvey, H. (2019, May 30). Unraveling the Spiderweb: Timelining ATT&CK Artifacts Used by GRIM SPIDER. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)

---

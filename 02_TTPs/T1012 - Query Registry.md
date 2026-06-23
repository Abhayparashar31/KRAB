# Query Registry

## Description

Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.

The Registry contains a significant amount of information about the operating system, configuration, software, and security. [1] Information can easily be queried using the Reg utility, though other means to access the Registry exist. Some of the information may help adversaries to further their operation within a network. Adversaries may use the information from Query Registry during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0045 | ADVSTORESHELL | ADVSTORESHELL can enumerate registry keys. [2] [3] |
| G0050 | APT32 | APT32 's backdoor can query the Windows Registry to gather system information. [4] |
| G0087 | APT39 | APT39 has used various strains of malware to query the Registry. [5] |
| G0096 | APT41 | APT41 queried registry values to determine items such as configured RDP ports and network configurations. [6] |
| S0438 | Attor | Attor has opened the registry and performed query searches. [7] |
| S0344 | Azorult | Azorult can check for installed software on the system under the Registry key Software\Microsoft\Windows\CurrentVersion\Uninstall . [8] |
| S0414 | BabyShark | BabyShark has executed the reg query command for HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default . [9] |
| S0031 | BACKSPACE | BACKSPACE is capable of enumerating and making modifications to an infected system's Registry. [10] |
| S0239 | Bankshot | Bankshot searches for certain Registry keys to be configured before executing the payload. [11] |
| S0534 | Bazar | Bazar can query Windows\CurrentVersion\Uninstall for installed applications. [12] [13] |
| S0574 | BendyBear | BendyBear can query the host's Registry key at HKEY_CURRENT_USER\Console\QuickEdit to retrieve data. [14] |
| S0268 | Bisonal | Bisonal has used the RegQueryValueExA function to retrieve proxy information in the Registry. [15] |
| S0570 | BitPaymer | BitPaymer can use the RegEnumKeyW to iterate through Registry keys. [16] |
| G1043 | BlackByte | BlackByte queried registry values to determine system language settings. [17] |
| S1180 | BlackByte Ransomware | BlackByte Ransomware enumerates the Registry, specifically the HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options key. [18] |
| S0252 | Brave Prince | Brave Prince gathers information about the Registry. [19] |
| S1039 | Bumblebee | Bumblebee can check the Registry for specific keys. [20] |
| S0030 | Carbanak | Carbanak checks the Registry key HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings for proxy configurations information. [21] |
| S0484 | Carberp | Carberp has searched the Image File Execution Options registry key for "Debugger" within every subkey. [22] |
| S0335 | Carbon | Carbon enumerates values in the Registry. [23] |
| S0348 | Cardinal RAT | Cardinal RAT contains watchdog functionality that periodically ensures HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Load is set to point to its executable. [24] |
| S0674 | CharmPower | CharmPower has the ability to enumerate Uninstall registry values. [25] |
| G0114 | Chimera | Chimera has queried Registry keys using reg query \ \HKU\ \SOFTWARE\Microsoft\Terminal Server Client\Servers and reg query \ \HKU\ \Software\Microsoft\Windows\CurrentVersion\Internet Settings . [26] |
| S0023 | CHOPSTICK | CHOPSTICK provides access to the Windows Registry, which can be used to gather information. [27] |
| S0660 | Clambling | Clambling has the ability to enumerate Registry keys, including KEY_CURRENT_USER\Software\Bitcoin\Bitcoin-Qt\strDataDir to search for a bitcoin wallet. [28] [29] |
| S0154 | Cobalt Strike | Cobalt Strike can query HKEY_CURRENT_USER\Software\Microsoft\Office\ \Excel\Security\AccessVBOM\ to determine if the security setting for restricting default programmatic access is enabled. [30] [31] |
| S0126 | ComRAT | ComRAT can check the default browser by querying HKCR\http\shell\open\command . [32] |
| S0115 | Crimson | Crimson can check the Registry for the presence of HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\last_edate to determine how long it has been installed on a host. [33] |
| G1034 | Daggerfly | Daggerfly used Reg to dump the Security Account Manager (SAM), System, and Security Windows registry hives from victim machines. [34] |
| S0673 | DarkWatchman | DarkWatchman can query the Registry to determine if it has already been installed on the system. [35] |
| S0354 | Denis | Denis queries the Registry for keys and values. [36] |
| S0021 | Derusbi | Derusbi is capable of enumerating Registry keys and values. [37] |
| S0186 | DownPaper | DownPaper searches and reads the value of the Windows Update Registry Run key. [38] |
| G0035 | Dragonfly | Dragonfly has queried the Registry to identify victim information. [39] |
| S0567 | Dtrack | Dtrack can collect the RegisteredOwner, RegisteredOrganization, and InstallDate registry values. [40] |
| S1159 | DUSTTRAP | DUSTTRAP can enumerate Registry items. [41] |
| S0091 | Epic | Epic uses the rem reg query command to obtain values from Registry keys. [42] |
| S0512 | FatDuke | FatDuke can get user agent strings for the default browser from HKCU\Software\Classes\http\shell\open\command . [43] |
| S0267 | FELIXROOT | FELIXROOT queries the Registry for specific keys for potential privilege escalation and proxy information. FELIXROOT has also used WMI to query the Windows Registry. [44] [45] |
| S0182 | FinFisher | FinFisher queries Registry values as part of its anti-sandbox checks. [46] [47] |
| G0117 | Fox Kitten | Fox Kitten has accessed Registry hives ntuser.dat and UserClass.dat. [48] |
| S1044 | FunnyDream | FunnyDream can check Software\Microsoft\Windows\CurrentVersion\Internet Settings to extract the ProxyServer string. [49] |
| G0047 | Gamaredon Group | Gamaredon Group has queried HKEY_CURRENT_USER\\Console\\WindowsUpdates to obtain the C2 addresses. [50] Gamaredon Group has queried HKEY_CURRENT_USER\\Console\\WindowsUpdates to obtain the C2 addresses. [50] |
| S0666 | Gelsemium | Gelsemium can open random files and Registry keys to obscure malware behavior from sandbox analysis. [51] |
| S0032 | gh0st RAT | gh0st RAT has checked for the existence of a Service key to determine if it has already been installed on the system. [52] |
| S0249 | Gold Dragon | Gold Dragon enumerates registry keys with the command regkeyenum and obtains information for the Registry key HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run . [19] |
| S0376 | HOPLIGHT | A variant of HOPLIGHT hooks lsass.exe, and lsass.exe then checks the Registry for the data value 'rdpproto' under the key SYSTEM\CurrentControlSet\Control\Lsa Name . [53] |
| S0203 | Hydraq | Hydraq creates a backdoor through which remote attackers can retrieve system information, such as CPU speed, from Registry keys. [54] [55] |
| G0119 | Indrik Spider | Indrik Spider has used a service account to extract copies of the Security Registry hive. [56] |
| S0604 | Industroyer | Industroyer has a data wiper component that enumerates keys in the Registry HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services . [57] |
| S0260 | InvisiMole | InvisiMole can enumerate Registry values, keys, and data. [58] |
| S0201 | JPIN | JPIN can enumerate Registry keys. [59] |
| S1190 | Kapeka | Kapeka queries registry values for stored configuration information. [60] |
| G0094 | Kimsuky | Kimsuky has obtained specific Registry keys and values on a compromised host. [61] |
| G0032 | Lazarus Group | Lazarus Group malware IndiaIndia checks Registry keys within HKCU and HKLM to determine if certain applications are present, including SecureCRT, Terminal Services, RealVNC, TightVNC, UltraVNC, Radmin, mRemote, TeamViewer, FileZilla, pcAnyware, and Remote Desktop. Another Lazarus Group malware sample checks for the presence of the following Registry key: HKEY_CURRENT_USER\Software\Bitcoin\Bitcoin-Qt . [62] [63] [64] |
| S0513 | LiteDuke | LiteDuke can query the Registry to check for the presence of HKCU\Software\KasperskyLab . [43] |
| S0680 | LitePower | LitePower can query the Registry for keys added to execute COM hijacking. [65] |
| G0030 | Lotus Blossom | Lotus Blossom has run commands such as reg query HKLM\SYSTEM\CurrentControlSet\Services\[service name]\Parameters to verify if installed implants are running as a service. [66] |
| S0532 | Lucifer | Lucifer can check for existing stratum cryptomining information in HKLM\Software\Microsoft\Windows\CurrentVersion\spreadCpuXmr – %stratum info% . [67] |
| S1060 | Mafalda | Mafalda can enumerate Registry keys with all subkeys and values. [68] |
| S1015 | Milan | Milan can query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography MachineGuid to retrieve the machine GUID. [69] |
| S1047 | Mori | Mori can read data from the Registry including from HKLM\Software\NFC\IPA and HKLM\Software\NFC\ . [70] |
| S0385 | njRAT | njRAT can read specific registry values. [71] |
| G0049 | OilRig | OilRig has used reg query "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default" on a victim to query the Registry. [72] |
| C0014 | Operation Wocao | During Operation Wocao , the threat actors executed /c cd /d c:\windows\temp\ & reg query HKEY_CURRENT_USER\Software\<username>\PuTTY\Sessions\ to detect recent PuTTY sessions, likely to further lateral movement. [73] |
| S0165 | OSInfo | OSInfo queries the registry to look for information about Terminal Services. [74] |
| S1050 | PcShare | PcShare can search the registry files of a compromised host. [49] |
| S0517 | Pillowmint | Pillowmint has used shellcode which reads code stored in the registry keys \REGISTRY\SOFTWARE\Microsoft\DRM using the native Windows API as well as read HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\Interfaces as part of its C2. [75] |
| S0013 | PlugX | PlugX can enumerate and query for information contained within the Windows Registry. [76] [77] [78] |
| S0145 | POWERSOURCE | POWERSOURCE queries Registry keys in preparation for setting Run keys to achieve persistence. [79] |
| S0194 | PowerSploit | PowerSploit contains a collection of Privesc-PowerUp modules that can query Registry keys for potential opportunities. [80] [81] |
| S0184 | POWRUNER | POWRUNER may query the Registry by running reg query on a victim. [82] |
| S0238 | Proxysvc | Proxysvc gathers product names from the Registry key: HKLM\Software\Microsoft\Windows NT\CurrentVersion ProductName and the processor description from the Registry key HKLM\HARDWARE\DESCRIPTION\System\CentralProcessor\0 ProcessorNameString . [83] |
| S1228 | PUBLOAD | PUBLOAD has queried Registry values to identify software using reg query . [84] |
| S1242 | Qilin | Qilin can check HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control SystemStartOptions to determine if a machine is running in safe mode. [85] |
| S0269 | QUADAGENT | QUADAGENT checks if a value exists within a Registry key in the HKCU hive whose name is the same as the scheduled task it has created. [86] |
| S1076 | QUIETCANARY | QUIETCANARY has the ability to retrieve information from the Registry. [87] |
| S1148 | Raccoon Stealer | Raccoon Stealer queries the Windows Registry to fingerprint the infected host via the HKLM:\SOFTWARE\Microsoft\Cryptography\MachineGuid key. [88] [89] |
| S0241 | RATANKBA | RATANKBA uses the command reg query "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\InternetSettings" . [90] |
| S0172 | Reaver | Reaver queries the Registry to determine the correct Startup path to use for persistence. [91] |
| S1240 | RedLine Stealer | RedLine Stealer can query the Windows Registry. [92] |
| S0075 | Reg | Reg may be used to gather details from the Windows Registry of a local or remote system at the command-line interface. [93] |
| S0332 | Remcos | Remcos can obtain Registry data from targeted systems. [94] |
| S0496 | REvil | REvil can query the Registry to get random file extensions to append to encrypted files. [95] |
| S0448 | Rising Sun | Rising Sun has identified the OS product name from a compromised host by searching the registry for SOFTWARE\MICROSOFT\Windows NT\ CurrentVersion | ProductName . [96] |
| S0240 | ROKRAT | ROKRAT can access the HKLM\System\CurrentControlSet\Services\mssmbios\Data\SMBiosData Registry key to obtain the System manufacturer value to identify the machine type. [97] |
| S1018 | Saint Bot | Saint Bot has used check_registry_keys as part of its environmental checks. [98] |
| S1099 | Samurai | Samurai can query SOFTWARE\Microsoft\.NETFramework\policy\v2.0 for discovery. [99] |
| S0140 | Shamoon | Shamoon queries several Registry keys to identify hard disk partitions to overwrite. [100] |
| S1019 | Shark | Shark can query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography MachineGuid to retrieve the machine GUID. [69] |
| S0589 | Sibot | Sibot has queried the registry for proxy server information. [101] |
| S0692 | SILENTTRINITY | SILENTTRINITY can use the GetRegValue function to check Registry keys within HKCU\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated and HKLM\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated . It also contains additional modules that can check software AutoRun values and use the Win32 namespace to get values from HKCU, HKLM, HKCR, and HKCC hives. [102] |
| S0627 | SodaMaster | SodaMaster has the ability to query the Registry to detect a key specific to VMware. [103] |
| G0038 | Stealth Falcon | Stealth Falcon malware attempts to determine the installed version of .NET by querying the Registry. [104] |
| S0380 | StoneDrill | StoneDrill has looked in the registry to find the default browser path. [105] |
| S0603 | Stuxnet | Stuxnet searches the Registry for indicators of security programs. [106] |
| S0559 | SUNBURST | SUNBURST collected the registry value HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\MachineGuid from compromised hosts. [107] |
| S1064 | SVCReady | SVCReady can search for the HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System Registry key to gather system information. [108] |
| S0242 | SynAck | SynAck enumerates Registry keys associated with event logs. [109] |
| S0011 | Taidoor | Taidoor can query the Registry on compromised hosts using RegQueryValueExA . [110] |
| S0560 | TEARDROP | TEARDROP checked that HKU\SOFTWARE\Microsoft\CTF existed before decoding its embedded payload. [107] [111] |
| G0027 | Threat Group-3390 | A Threat Group-3390 tool can read and decrypt stored Registry values. [112] |
| S0668 | TinyTurla | TinyTurla can query the Registry for its configuration information. [113] |
| S1201 | TRANSLATEXT | TRANSLATEXT has queried the following registry key to check for installed Chrome extensions: HKCU\Software\Policies\Google\Chrome\ExtensionInstallForcelist . [114] |
| G0010 | Turla | Turla surveys a system upon check-in to discover information in the Windows Registry with the reg query command. [42] Turla has also retrieved PowerShell payloads hidden in Registry keys as well as checking keys associated with null session named pipes . [115] |
| S0022 | Uroburos | Uroburos can query the Registry, typically HKLM:\SOFTWARE\Classes\.wav\OpenWithProgIds , to find the key and path to decrypt and load its kernel driver and kernel driver loader. [116] |
| S0386 | Ursnif | Ursnif has used Reg to query the Registry for installed programs. [117] [118] |
| S0476 | Valak | Valak can use the Registry for code updates and to collect credentials. [119] |
| S0180 | Volgmer | Volgmer checks the system for certain Registry keys. [120] |
| G1017 | Volt Typhoon | Volt Typhoon has queried the Registry on compromised systems, reg query hklm\software\ , for information on installed software including PuTTY. [121] [122] |
| S0612 | WastedLocker | WastedLocker checks for specific registry keys related to the UCOMIEnumConnections and IActiveScriptParseProcedure32 interfaces. [123] |
| S0579 | Waterbear | Waterbear can query the Registry key "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSDTC\MTxOCI" to see if the value OracleOcilib exists. [124] |
| S0155 | WINDSHIELD | WINDSHIELD can gather Registry values. [125] |
| S1065 | Woody RAT | Woody RAT can search registry keys to identify antivirus programs on an compromised host. [126] |
| S0251 | Zebrocy | Zebrocy executes the reg query command to obtain information in the Registry. [127] |
| S0330 | Zeus Panda | Zeus Panda checks for the existence of a Registry key and if it contains certain values. [128] |
| G0128 | ZIRCONIUM | ZIRCONIUM has used a tool to query the Registry for proxy settings. [129] |
| S0412 | ZxShell | ZxShell can query the netsvc group value data located in the svchost group Registry key. [130] |
| S1013 | ZxxZ | ZxxZ can search the registry of a compromised host. [131] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0209 | Detection of Registry Query for Environmental Discovery | AN0589 | Registry read access associated with suspicious or non-interactive processes querying system config, installed software, or security settings. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0209 | Detection of Registry Query for Environmental Discovery | AN0589 | Registry read access associated with suspicious or non-interactive processes querying system config, installed software, or security settings. |

---

## References

- [Wikipedia. (n.d.). Windows Registry. Retrieved February 2, 2015.](https://en.wikipedia.org/wiki/Windows_Registry)
- [ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
- [Bitdefender. (2015, December). APT28 Under the Scope. Retrieved February 23, 2017.](https://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf)
- [Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)
- [FBI. (2020, September 17). Indicators of Compromise Associated with Rana Intelligence Computing, also known as Advanced Persistent Threat 39, Chafer, Cadelspy, Remexi, and ITG07. Retrieved December 10, 2020.](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)
- [Nikita Rostovcev. (2022, August 18). APT41 World Tour 2021 on a tight schedule. Retrieved February 22, 2024.](https://www.group-ib.com/blog/apt41-world-tour-2021/)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
- [Unit 42. (2019, February 22). New BabyShark Malware Targets U.S. National Security Think Tanks. Retrieved October 7, 2019.](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
- [FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved November 17, 2024.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
- [US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1, 2020.](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
- [Harbison, M. (2021, February 9). BendyBear: Novel Chinese Shellcode Linked With Cyber Espionage Group BlackTech. Retrieved February 16, 2021.](https://unit42.paloaltonetworks.com/bendybear-shellcode-blacktech/)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [Frankoff, S., Hartley, B. (2018, November 14). Big Game Hunting: The Evolution of INDRIK SPIDER From Dridex Wire Fraud to BitPaymer Targeted Ransomware. Retrieved January 6, 2021.](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
- [Huseyin Can Yuceel. (2022, February 21). TTPs used by BlackByte Ransomware Targeting Critical Infrastructure. Retrieved December 16, 2024.](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
- [Salem, A. (2022, April 27). The chronicles of Bumblebee: The Hook, the Bee, and the Trickbot connection. Retrieved September 2, 2022.](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
- [Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)
- [Giuliani, M., Allievi, A. (2011, February 28). Carberp - a modular information stealing trojan. Retrieved September 12, 2024.](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
- [ESET. (2017, March 30). Carbon Paper: Peering into Turla’s second stage backdoor. Retrieved November 7, 2018.](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)
- [Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Chen, T. and Chen, Z. (2020, February 17). CLAMBLING - A New Backdoor Base On Dropbox. Retrieved November 12, 2021.](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
- [Mavis, N. (2020, September 21). The Art and Science of Detecting Cobalt Strike. Retrieved September 12, 2024.](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Threat Hunter Team. (2023, April 20). Daggerfly: APT Actor Targets Telecoms Company in Africa. Retrieved July 25, 2024.](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [ClearSky Cyber Security. (2017, December). Charming Kitten. Retrieved December 27, 2017.](http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [Hod Gavriel. (2019, November 21). Dtrack: In-depth analysis of APT on a nuclear power plant. Retrieved January 20, 2021.](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Patil, S. (2018, June 26). Microsoft Office Vulnerabilities Used to Distribute FELIXROOT Backdoor in Recent Campaign. Retrieved November 17, 2024.](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
- [Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
- [FinFisher. (n.d.). Retrieved September 12, 2024.](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
- [Allievi, A.,Flori, E. (2018, March 01). FinFisher exposed: A researcher’s tale of defeating traps, tricks, and complex virtual machines. Retrieved July 9, 2018.](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
- [CISA. (2020, September 15). Iran-Based Threat Actor Exploits VPN Vulnerabilities. Retrieved December 21, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Threat Hunter Team, Symantec and Carbon Black. (2025, April 10). Shuckworm Targets Foreign Military Mission Based in Ukraine. Retrieved July 23, 2025.](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Quinn, J. (2019, March 25). The odd case of a Gh0stRAT variant. Retrieved July 15, 2020.](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
- [Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
- [Mandiant Intelligence. (2022, June 2). To HADES and Back: UNC2165 Shifts to LOCKBIT to Evade Sanctions. Retrieved July 29, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)
- [Anton Cherepanov. (2017, June 12). Win32/Industroyer: A new threat for industrial controls systems. Retrieved December 18, 2020.](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [Mohammad Kazem Hassan Nejad, WithSecure. (2024, April 17). KAPEKA A novel backdoor spotted in Eastern Europe. Retrieved January 6, 2025.](https://labs.withsecure.com/content/dam/labs/docs/WithSecure-Research-Kapeka.pdf)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)
- [Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)
- [Yamout, M. (2021, November 29). WIRTE’s campaign in the Middle East ‘living off the land’ since at least 2019. Retrieved February 1, 2022.](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [Hsu, K. et al. (2020, June 24). Lucifer: New Cryptojacking and DDoS Hybrid Malware Exploiting High and Critical Vulnerabilities to Infect Windows Devices. Retrieved November 16, 2020.](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [Accenture. (2021, November 9). Who are latest targets of cyber group Lyceum?. Retrieved June 16, 2022.](https://www.accenture.com/us-en/blogs/cyber-defense/iran-based-lyceum-campaigns)
- [FBI, CISA, CNMF, NCSC-UK. (2022, February 24). Iranian Government-Sponsored Actors Conduct Cyber Operations Against Global Government and Commercial Networks. Retrieved September 27, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
- [Pascual, C. (2018, November 27). AutoIt-Compiled Worm Affecting Removable Media Delivers Fileless Version of BLADABINDI/njRAT Backdoor. Retrieved June 4, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
- [Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
- [Trustwave SpiderLabs. (2020, June 22). Pillowmint: FIN7’s Monkey Thief . Retrieved July 27, 2020.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
- [Vasilenko, R. (2013, December 17). An Analysis of PlugX Malware. Retrieved November 24, 2015.](https://lastline3.rssing.com/chan-29044929/all_p1.html#c29044929a2)
- [Brumaghin, E. and Grady, C.. (2017, March 2). Covert Channels and Poor Decisions: The Tale of DNSMessenger. Retrieved March 8, 2017.](http://blog.talosintelligence.com/2017/03/dnsmessenger.html)
- [PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.](https://github.com/PowerShellMafia/PowerSploit)
- [PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.](http://powersploit.readthedocs.io)
- [Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
- [Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Magdy, S. et al. (2022, August 25). New Golang Ransomware Agenda Customizes Attacks. Retrieved September 26, 2025.](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
- [Lee, B., Falcone, R. (2018, July 25). OilRig Targets Technology Service Provider and Government Agency with QUADAGENT. Retrieved August 9, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Quentin Bourgue, Pierre le Bourhis, & Sekoia TDR. (2022, June 28). Raccoon Stealer v2 - Part 1: The return of the dead. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
- [Grunzweig, J. and Miller-Osborn, J. (2017, November 10). New Malware with Ties to SunOrcal Discovered. Retrieved November 16, 2017.](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)
- [Mohansundaram M, Neil Tyagi. (2024, April 17). Redline Stealer: A Novel Approach. Retrieved September 17, 2025.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/redline-stealer-a-novel-approach/)
- [Microsoft. (2012, April 17). Reg. Retrieved May 1, 2015.](https://technet.microsoft.com/en-us/library/cc732643.aspx)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)
- [Hasherezade. (2021, April 6). A deep dive into Saint Bot, a new downloader. Retrieved June 9, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [GREAT. (2021, March 30). APT10: sophisticated multi-layered loader Ecipekac discovered in A41APT campaign. Retrieved June 17, 2021.](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
- [Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.](https://citizenlab.org/2016/05/stealth-falcon/)
- [Kaspersky Lab. (2017, March 7). From Shamoon to StoneDrill: Wipers attacking Saudi organizations and beyond. Retrieved March 14, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [Ivanov, A. et al. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
- [CISA, FBI, DOD. (2021, August). MAR-10292089-1.v2 – Chinese Remote Access Trojan: TAIDOOR. Retrieved August 24, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
- [MSTIC, CDOC, 365 Defender Research Team. (2021, January 20). Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop . Retrieved January 22, 2021.](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
- [Pantazopoulos, N., Henry T. (2018, May 18). Emissary Panda – A potential new malicious tool. Retrieved June 25, 2018.](https://research.nccgroup.com/2018/05/18/emissary-panda-a-potential-new-malicious-tool/)
- [Cisco Talos. (2021, September 21). TinyTurla - Turla deploys new malware to keep a secret backdoor on victim machines. Retrieved December 2, 2021.](https://blog.talosintelligence.com/2021/09/tinyturla.html)
- [Park, S. (2024, June 27). Kimsuky deploys TRANSLATEXT to target South Korean academia. Retrieved October 14, 2024.](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Caragay, R. (2015, March 26). URSNIF: The Multifaceted Malware. Retrieved June 5, 2019.](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
- [Sioting, S. (2013, June 15). BKDR_URSNIF.SM. Retrieved June 5, 2019.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
- [Duncan, B. (2020, July 24). Evolution of Valak, from Its Beginnings to Mass Distribution. Retrieved August 31, 2020.](https://unit42.paloaltonetworks.com/valak-evolution/)
- [US-CERT. (2017, November 01). Malware Analysis Report (MAR) - 10135536-D. Retrieved July 16, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-D_WHITE_S508C.PDF)
- [NSA et al. (2023, May 24). People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection. Retrieved July 27, 2023.](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Antenucci, S., Pantazopoulos, N., Sandee, M. (2020, June 23). WastedLocker: A New Ransomware Variant Developed By The Evil Corp Group. Retrieved September 14, 2021.](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
- [Su, V. et al. (2019, December 11). Waterbear Returns, Uses API Hooking to Evade Security. Retrieved February 22, 2021.](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
- [Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [ESET Research. (2019, May 22). A journey to Zebrocy land. Retrieved June 20, 2019.](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
- [Ebach, L. (2017, June 22). Analysis Results of Zeus.Variant.Panda. Retrieved November 5, 2018.](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
- [Singh, S. and Antil, S. (2020, October 27). APT-31 Leverages COVID-19 Vaccine Theme and Abuses Legitimate Online Services. Retrieved March 24, 2021.](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)
- [Raghuprasad, C . (2022, May 11). Bitter APT adds Bangladesh to their targets. Retrieved June 1, 2022.](https://blog.talosintelligence.com/2022/05/bitter-apt-adds-bangladesh-to-their.html)

---

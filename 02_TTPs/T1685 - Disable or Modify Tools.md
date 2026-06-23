# Disable or Modify Tools

## Description

Adversaries may disable, degrade, or tamper with security tools or applications (e.g., endpoint detection and response (EDR) tools, intrusion detection systems (IDS), antivirus, logging agents, sensors, etc.) to impair or reduce visibility of defensive capabilities. This may include stopping specific services, killing processes, modifying or deleting tool configuration files and Registry keys, or preventing tools from updating. This may also include impairing defenses more broadly by disrupting preventative, detection, and response mechanisms across host, network, and cloud environments. [1]

In addition to directly targeting tools, adversaries may block or manipulate indicators and telemetry used for detection. This includes maliciously disabling or redirecting sensors such as Event Tracing for Windows (ETW), modifying event log configurations (e.g., redirecting Security logs), or interfering with logging pipelines and forwarding mechanisms (e.g., SIEM ingestion). [2] [3]

More advanced techniques include leveraging legitimate drivers or debugging mechanisms to render tools non-functional, bypassing anti-tampering protections, and targeting specific defenses such as Sysmon or cloud monitoring agents. Adversaries may also disrupt broader defensive operations, including update mechanisms, logging infrastructure (e.g., syslog), or event aggregation, further degrading an organization’s ability to detect and respond to malicious activity. [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0028 | 2015 Ukraine Electric Power Attack | During the 2015 Ukraine Electric Power Attack , Sandworm Team modified in-registry internet settings to lower internet security. [5] |
| S0331 | Agent Tesla | Agent Tesla has the capability to kill any running analysis processes and AV software. [6] |
| G1030 | Agrius | Agrius used several mechanisms to try to disable security tools. Agrius attempted to modify EDR-related services to disable auto-start on system reboot. Agrius used a publicly available driver, GMER64.sys typically used for anti-rootkit functionality, to selectively stop and remove security software processes. [7] |
| G1024 | Akira | Akira has disabled or modified security tools for defense evasion. [8] |
| G0082 | APT38 | APT38 has unhooked DLLs to disable endpoint detection and response (EDR) or anti-virus (AV) tools. [9] |
| G0096 | APT41 | APT41 developed a custom injector that enables an Event Tracing for Windows (ETW) bypass, making malicious processes invisible to Windows logging. [10] |
| G1023 | APT5 | APT5 has used the CLEANPULSE utility to insert command line strings into a targeted process to prevent certain log events from occurring. [11] |
| G0143 | Aquatic Panda | Aquatic Panda has attempted to stop endpoint detection and response (EDR) tools on compromised systems. [12] |
| C0046 | ArcaneDoor | ArcaneDoor modified the Authentication, Authorization, and Accounting (AAA) function of targeted Cisco ASA appliances to allow the threat actor to bypass normal AAA operations. [13] [14] |
| S0640 | Avaddon | Avaddon looks for and attempts to stop anti-malware solutions. [15] |
| S0638 | Babuk | Babuk can stop anti-virus services on a compromised host. [16] |
| S0534 | Bazar | Bazar has manually loaded ntdll from disk in order to identity and remove API hooks set by security products. [17] |
| G1043 | BlackByte | BlackByte disabled security tools such as Windows Defender and the Raccine anti-ransomware tool during operations. [18] [19] [20] |
| S1180 | BlackByte Ransomware | BlackByte Ransomware adds .JS and .EXE extensions to the Microsoft Defender exclusion list. BlackByte Ransomware terminates and removes the Raccine anti-ransomware utility. [21] |
| S1184 | BOLDMOVE | BOLDMOVE can disable the Fortinet daemons moglogd and syslogd to evade detection and logging. [22] |
| S0252 | Brave Prince | Brave Prince terminates antimalware processes. [23] |
| G0060 | BRONZE BUTLER | BRONZE BUTLER has incorporated code into several tools that attempts to terminate anti-virus processes. [24] |
| S1063 | Brute Ratel C4 | Brute Ratel C4 has the ability to hide memory artifacts and to patch Event Tracing for Windows (ETW) and the Anti Malware Scan Interface (AMSI). [25] [26] |
| S0482 | Bundlore | Bundlore can change browser security settings to enable extensions to be installed. Bundlore uses the pkill cfprefsd command to prevent users from inspecting processes. [27] [28] |
| S0484 | Carberp | Carberp has attempted to disable security software by creating a suspended process for the security software and injecting code to delete antivirus core files when the process is resumed. [29] |
| S0144 | ChChes | ChChes can alter the victim's proxy configuration. [30] |
| S0611 | Clop | Clop can uninstall or disable security products. [31] |
| S0154 | Cobalt Strike | Cobalt Strike has the ability to use Smart Applet attacks to disable the Java SecurityManager sandbox. [32] [33] |
| S0608 | Conficker | Conficker terminates various services related to system security and Windows. [34] |
| G1052 | Contagious Interview | Contagious Interview has convinced victims to disable Docker and other container environments and run code on their machine natively in attempts to bypass container isolation and ensure device infection. [35] |
| C0029 | Cutting Edge | During Cutting Edge , threat actors disabled logging and modified the compcheckresult.cgi component to edit the Ivanti Connect Secure built-in Integrity Checker exclusion list to evade detection. [36] [37] |
| S0334 | DarkComet | DarkComet can disable Security Center functions like anti-virus. [38] [39] |
| S1111 | DarkGate | DarkGate will terminate processes associated with several security software products if identified during execution. [40] |
| S9017 | DCRAT | DCRAT can patch Microsoft’s Antimalware Scan Interface (AMSI) to evade detection. [41] |
| S0659 | Diavol | Diavol can attempt to stop security software. [42] |
| S0695 | Donut | Donut can patch Antimalware Scan Interface (AMSI), Windows Lockdown Policy (WLDP), as well as exit-related Native API functions to avoid process termination. [43] |
| S9013 | DRYHOOK | DRYHOOK has killed all instances of the cgi-server process in order for the modified Perl module to be activated. [44] |
| S0377 | Ebury | Ebury can disable SELinux Role-Based Access Control and deactivate PAM modules. [45] |
| S0554 | Egregor | Egregor has disabled Windows Defender to evade protections. [46] |
| S0605 | EKANS | EKANS stops processes related to security and management software. [47] [48] |
| G0037 | FIN6 | FIN6 has deployed a utility script named kill.bat to disable anti-virus. [49] |
| G0047 | Gamaredon Group | Gamaredon Group has delivered macros which can tamper with Microsoft Office security settings. [50] [51] |
| S0249 | Gold Dragon | Gold Dragon terminates anti-malware processes if they’re found running on the system. [23] |
| S0477 | Goopy | Goopy has the ability to disable Microsoft Outlook's security policies to disable macro warnings. [52] |
| G0078 | Gorgon Group | Gorgon Group malware can attempt to disable security features in Microsoft Office and Windows Defender using the taskkill command. [53] |
| S0531 | Grandoreiro | Grandoreiro can hook APIs, kill processes, break file system paths, and change ACLs to prevent security tools from running. [54] |
| S0132 | H1N1 | H1N1 kills and disables services for Windows Security Center, and Windows Defender. [55] |
| S0061 | HDoor | HDoor kills anti-virus found on the victim. [56] |
| S0697 | HermeticWiper | HermeticWiper has the ability to set the HKLM:\SYSTEM\\CurrentControlSet\\Control\\CrashControl\CrashDumpEnabled Registry key to 0 in order to disable crash dumps. [57] [58] [59] |
| S0601 | Hildegard | Hildegard has modified DNS resolvers to evade DNS monitoring tools. [60] |
| C0038 | HomeLand Justice | During HomeLand Justice , threat actors modified and disabled components of endpoint detection and response (EDR) solutions including Microsoft Defender Antivirus. [61] |
| S1097 | HUI Loader | HUI Loader has the ability to disable Windows Event Tracing for Windows (ETW) and Antimalware Scan Interface (AMSI) functions. [62] |
| S0434 | Imminent Monitor | Imminent Monitor has a feature to disable Windows Task Manager. [63] |
| G1032 | INC Ransom | INC Ransom can use SystemSettingsAdminFlows.exe, a native Windows utility, to disable Windows Defender. [64] |
| G0119 | Indrik Spider | Indrik Spider used PsExec to leverage Windows Defender to disable scanning of all downloaded files and to restrict real-time monitoring. [65] Indrik Spider has used MpCmdRun to revert the definitions in Microsoft Defender. [66] Additionally, Indrik Spider has used WMI to stop or uninstall and reset anti-virus products and other defensive services. [66] |
| S0201 | JPIN | JPIN can lower security settings by changing Registry keys. [67] |
| S1206 | JumbledPath | JumbledPath can impair logging on all devices used along its connection path to compromised hosts. [68] |
| G0094 | Kimsuky | Kimsuky has been observed turning off Windows Security Center and can hide the AV software window from the view of the infected user. [69] [70] |
| S0669 | KOCTOPUS | KOCTOPUS will attempt to delete or disable all Registry keys and scheduled tasks related to Microsoft Security Defender and Security Essentials. [71] |
| C0035 | KV Botnet Activity | KV Botnet Activity used various scripts to remove or disable security tools, such as http_watchdog and firewallsd , as well as tools related to other botnet infections, such as mips_ff , on victim devices. [72] |
| G0032 | Lazarus Group | Lazarus Group malware TangoDelta attempts to terminate various processes associated with McAfee. Additionally, Lazarus Group malware SHARPKNOT disables the Microsoft Windows System Event Notification and Alerter services. [73] [74] [75] [76] . |
| S9039 | LazyWiper | LazyWiper can disable Microsoft Windows Defender Real-Time Monitoring with the Set-MpPreference cmdlet. [77] |
| S1199 | LockBit 2.0 | LockBit 2.0 can disable firewall rules and anti-malware and monitoring software including Windows Defender. [78] [79] |
| S1202 | LockBit 3.0 | LockBit 3.0 can disable security tools to evade detection including Windows Defender. [80] [81] [82] |
| S0372 | LockerGoga | LockerGoga installation has been immediately preceded by a "task kill" command in order to disable anti-virus. [83] |
| S1213 | Lumma Stealer | Lumma Stealer has attempted to bypass Windows Antimalware Scan Interface (AMSI) by removing the string "AmsiScanBuffer" from the "clr.dll" module in memory to prevent it from being called. [84] |
| S1048 | macOS.OSAMiner | macOS.OSAMiner has searched for the Activity Monitor process in the System Events process list and kills the process if running. macOS.OSAMiner also searches the operating system's install.log for apps matching its hardcoded list, killing all matching process names. [85] |
| G0059 | Magic Hound | Magic Hound has disabled antivirus services on targeted systems in order to upload malicious payloads. [86] |
| S1169 | Mango | Mango contains an unused capability to block endpoint security solutions from loading user-mode code hooks via a DLL in a specified process by using the UpdateProcThreadAttribute API to set the PROC_THREAD_ATTRIBUTE_MITIGATION_POLICY to PROCESS_CREATION_MITIGATION_POLICY_BLOCK_NON_MICROSOFT_BINARIES_ALWAYS_ON for an identified process. [87] |
| S0449 | Maze | Maze has disabled dynamic analysis and other security tools including IDA debugger, x32dbg, and OllyDbg. [88] It has also disabled Windows Defender's Real-Time Monitoring feature and attempted to disable endpoint protection services. [89] |
| G1051 | Medusa Group | Medusa Group has terminated antivirus services utilizing the gaze.exe executable and utilizing psexec.exe . [90] [91] [92] Medusa Group has also leveraged I/O control codes (IOCTLs) for terminating and deleting processes of identified security tools. [90] |
| S1244 | Medusa Ransomware | Medusa Ransomware has terminated antivirus services utilizing the gaze.exe executable. [90] Medusa Ransomware has also terminated antivirus services utilizing PowerShell scripts. [90] [93] |
| S0576 | MegaCortex | MegaCortex was used to kill endpoint security processes. [94] |
| S0455 | Metamorfo | Metamorfo has a function to kill processes associated with defenses and can prevent certain processes from launching. [95] [96] |
| S0688 | Meteor | Meteor can attempt to uninstall Kaspersky Antivirus or remove the Kaspersky license; it can also add all files and folders related to the attack to the Windows Defender exclusion list. [97] |
| G1054 | MirrorFace | MirrorFace has disabled Windows Defender in compromised environments. [98] |
| G0069 | MuddyWater | MuddyWater can disable the system's local proxy settings. [99] |
| S1135 | MultiLayer Wiper | MultiLayer Wiper removes the Volume Shadow Copy (VSS) service from infected devices along with all present shadow copies. [7] |
| S0228 | NanHaiShu | NanHaiShu can change Internet Explorer settings to reduce warnings about malware activity. [100] |
| S0336 | NanoCore | NanoCore can modify the victim's anti-virus. [101] [102] |
| S0457 | Netwalker | Netwalker can detect and terminate active security software-related processes on infected systems. [103] [104] |
| C0002 | Night Dragon | During Night Dragon , threat actors disabled anti-virus and anti-spyware tools in some instances on the victim’s machines. The actors also disabled proxy settings to allow direct communication from victims to the Internet. [105] |
| S9014 | PHASEJAM | PHASEJAM has modified Ivanti Connect Secure appliances and blocks the system upgrades by altering the DSUpgrade.pm file. [44] |
| G1040 | Play | Play has used tools including GMER, IOBit, and PowerTool to disable antivirus software. [106] [107] |
| S0223 | POWERSTATS | POWERSTATS can disable Microsoft Office Protected View by changing Registry keys. [108] |
| S0279 | Proton | Proton kills security tools like Wireshark that are running. [109] |
| S9019 | PureCrypter | PureCrypter has executed Set-MpPreference -ExclusionPath to exclude files or folders from Windows Defender scans. [110] |
| G0024 | Putter Panda | Malware used by Putter Panda attempts to terminate processes corresponding to two components of Sophos Anti-Virus (SAVAdminService.exe and SavService.exe). [111] |
| S0583 | Pysa | Pysa has the capability to stop antivirus services and disable Windows Defender. [112] |
| S0650 | QakBot | QakBot has the ability to modify the Registry to add its binaries to the Windows Defender exclusion list. [113] |
| S1242 | Qilin | Qilin can terminate antivirus-related processes and services. [114] [115] [116] [117] |
| C0055 | Quad7 Activity | Quad7 Activity has disabled the TP-Link management interface for TP-Link by killing the /usr/bin/httpd process. [118] [119] [120] |
| S0481 | Ragnar Locker | Ragnar Locker has attempted to terminate/stop processes and services associated with endpoint security products. [121] |
| S1130 | Raspberry Robin | Raspberry Robin can add an exception to Microsoft Defender that excludes the entire main drive from anti-malware scanning to evade detection. [122] |
| S1240 | RedLine Stealer | RedLine Stealer can disable security software and update services. [123] |
| S0496 | REvil | REvil can connect to and disable the Symantec server on the victim's network. [124] |
| S0400 | RobbinHood | RobbinHood will search for Windows services that are associated with antivirus software on the system and kill the process. [125] |
| G0106 | Rocke | Rocke used scripts which detected and uninstalled antivirus software. [126] [127] |
| S0253 | RunningRAT | RunningRAT kills antimalware running process. [23] |
| S0446 | Ryuk | Ryuk has stopped services related to anti-virus. [128] |
| G1031 | Saint Bear | Saint Bear will modify registry entries and scheduled task objects associated with Windows Defender to disable its functionality. [129] |
| G1015 | Scattered Spider | Scattered Spider has uninstalled and disabled security tools. [130] |
| S9008 | Shai-Hulud | Shai-Hulud has replaced DNS configuration from /tmp/resolved.conf in order to gain control of network-level control within CI environments and has flushed iptables rules using sudo iptables -F OUTPUT and sudo iptables -F DOCKER-USER . [131] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors disabled Microsoft Defender through Registry settings and real-time monitoring via PowerShell. [132] [133] |
| S1178 | ShrinkLocker | ShrinkLocker disables protectors used to secure the BitLocker encryption key on victim systems. [134] [135] |
| S0692 | SILENTTRINITY | SILENTTRINITY 's amsiPatch.py module can disable Antimalware Scan Interface (AMSI) functions. [136] |
| S0468 | Skidmap | Skidmap has the ability to set SELinux to permissive mode. [137] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 used the service control manager on a remote system to disable services associated with security monitoring products. [138] |
| S9024 | SPAWNCHIMERA | SPAWNCHIMERA has modified the Ivanti Integrity Checker Tool to evade detection. [139] [140] |
| S1234 | SplatCloak | SplatCloak has identified and disabled API callback features of Windows Defender and Kaspersky. [141] |
| S0058 | SslMM | SslMM identifies and kills anti-malware processes. [56] |
| S1200 | StealBit | StealBit can configure processes to not display certain Windows error messages by through use of the NtSetInformationProcess . [142] |
| S0491 | StrongPity | StrongPity can add directories used by the malware to the Windows Defender exclusions list to prevent detection. [143] |
| S0603 | Stuxnet | Stuxnet reduces the integrity level of objects to allow write actions. [144] |
| S0559 | SUNBURST | SUNBURST attempted to disable software security services following checks against a FNV-1a + XOR hashed hardcoded blocklist. [145] |
| G1018 | TA2541 | TA2541 has attempted to disable built-in security protections such as Windows AMSI. [146] |
| G0092 | TA505 | TA505 has used malware to disable Windows Defender. [147] |
| G0139 | TeamTNT | TeamTNT has disabled and uninstalled security tools such as Alibaba, Tencent, and BMC cloud monitoring agents on cloud-based infrastructure. [148] [149] |
| S0595 | ThiefQuest | ThiefQuest uses the function kill_unwanted to obtain a list of running processes and kills each process matching a list of security related processes. [150] |
| S0004 | TinyZBot | TinyZBot can disable Avira anti-virus. [151] |
| S0266 | TrickBot | TrickBot can disable Windows Defender. [152] |
| G0010 | Turla | Turla has used a AMSI bypass, which patches the in-memory amsi.dll, in PowerShell scripts to bypass Windows antimalware products. [153] |
| G1048 | UNC3886 | UNC3886 has disabled OpenSSL digital signature verification of system files through corruption of boot files. [154] |
| S0130 | Unknown Logger | Unknown Logger has functionality to disable security tools, including Kaspersky, BitDefender, and MalwareBytes. [155] |
| G1047 | Velvet Ant | Velvet Ant attempted to disable local security tools and endpoint detection and response (EDR) software during operations. [156] |
| S0670 | WarzoneRAT | WarzoneRAT can disarm Windows Defender during the UAC process to evade detection. [157] |
| S0579 | Waterbear | Waterbear can hook the ZwOpenProcess and GetExtendedTcpTable APIs called by the process of a security product to hide PIDs and TCP records from detection. [158] |
| S0689 | WhisperGate | WhisperGate can download and execute AdvancedRun.exe to disable the Windows Defender Theat Protection service and set an exclusion path for the C:\ drive. [159] [160] [161] |
| G0102 | Wizard Spider | Wizard Spider has shut down or uninstalled security applications on victim systems that might prevent ransomware from executing. [162] [163] [164] [165] |
| S1065 | Woody RAT | Woody RAT has suppressed all error reporting by calling SetErrorMode with 0x8007 as a parameter. [166] |
| S1207 | XLoader | XLoader loads a copy of NTDLL to evade hooks from security monitoring tools on this library. [167] XLoader can add the path of its executable to the Microsoft Defender exclusion list. [168] |
| S1114 | ZIPLINE | ZIPLINE can add itself to the exclusion list for the Ivanti Connect Secure Integrity Checker Tool if the --exclude parameter is passed by the tar process. [169] |
| S0412 | ZxShell | ZxShell can kill AV products' processes. [170] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Periodically verify that tools are functioning appropriately – for example, that all expected hosts with EDRs or monitoring agents are checking in to the central console. Check EDRs to ensure that no unexpected exclusion paths have been added. In Microsoft Defender for Endpoint, exclusions can be reviewed with the Get-MpPreference cmdlet. [171] |
| M1042 | Disable or Remove Feature or Program | Consider removing previous versions of tools that are unnecessary to the environment when possible. |
| M1038 | Execution Prevention | Use application control where appropriate, especially regarding the execution of tools outside of the organization's security policies (such as rootkit removal tools) that have been abused to impair system defenses. Ensure that only approved security applications are used and running on enterprise systems. |
| M1022 | Restrict File and Directory Permissions | Ensure proper process and file permissions are in place to prevent adversaries from disabling or interfering with security services. |
| M1024 | Restrict Registry Permissions | Ensure proper Registry permissions are in place to prevent adversaries from disabling or interfering with security services. |
| M1054 | Software Configuration | Consider automatically relaunching forwarding mechanisms at recurring intervals (ex: temporal, on-logon, etc.) as well as applying appropriate change management to firewall rules and other related system configurations. |
| M1018 | User Account Management | Ensure proper user permissions are in place to prevent adversaries from disabling or interfering with security services. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0497 | Detection of Defense Impairment through Disabled or Modified Tools across OS Platforms. | AN1369 | Detection of adversary behavior that disables or modifies security tools, including killing AV/EDR processes, stopping services, altering Sysmon registry keys, or tampering with exclusion lists. Defenders observe process/service termination, registry modification, and abnormal absence of expected telemetry. |
| AN1370 | Detects kill/systemctl/service commands against EDR, auditd, falco, osquery, rsyslog, journald, or agent processes; configuration edits disabling startup; module unload attempts; abrupt cessation of logs after privileged shell execution. |  |  |
| AN1371 | Detection of adversary disabling endpoint security tools by unloading launch agents/daemons, modifying configuration profiles, or disabling Gatekeeper/XProtect/logging settings, or removing endpoint agents followed by telemetry loss. |  |  |
| AN1372 | Correlates control-plane API actions disabling cloud-native monitoring or sensor agents (CloudTrail, GuardDuty, Security Hub, Defender, monitoring agents), role abuse preceding disablement, or instance agent uninstall events |  |  |
| AN1373 | Detects disabling container runtime security controls, removing sidecar sensors, modifying seccomp/AppArmor profiles, mounting host proc/sys paths to interfere with host logging, or killing in-container monitoring agents. |  |  |
| AN1374 | Detects disabling AAA, syslog, SNMP traps, ACL logging, or security features on routers/switches/firewalls; correlates privileged login followed by configuration commit reducing visibility. |  |  |
| AN2044 | Detects esxcli commands disabling syslog, firewall, lockdown mode, or stopping hostd/vpxa; correlates command execution with reduced forwarding activity. |  |  |

---

## References

- [Shaked, O. (2020, January 20). Anatomy of a Targeted Ransomware Attack. Retrieved June 18, 2022.](https://cdn.logic-control.com/docs/scadafence/Anatomy-Of-A-Targeted-Ransomware-Attack-WP.pdf)
- [Microsoft. (2009, May 17). Backdoor:Win32/Lamin.A. Retrieved September 6, 2018.](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?name=Backdoor:Win32/Lamin.A)
- [Palantir. (2018, December 24). Tampering with Windows Event Tracing: Background, Offense, and Defense. Retrieved April 15, 2026.](https://blog.palantir.com/tampering-with-windows-event-tracing-background-offense-and-defense-4be7ac62ac63)
- [Cocomazzi, Antonio. (2024, July 17). FIN7 Reboot | Cybercrime Gang Enhances Ops with New EDR Bypasses and Automated Attacks. Retrieved September 24, 2025.](https://www.sentinelone.com/labs/fin7-reboot-cybercrime-gang-enhances-ops-with-new-edr-bypasses-and-automated-attacks/)
- [Booz Allen Hamilton. (2016). When The Lights Went Out. Retrieved December 18, 2024.](https://www.boozallen.com/content/dam/boozallen/documents/2016/09/ukraine-report-when-the-lights-went-out.pdf)
- [Zhang, X. (2017, June 28). In-Depth Analysis of A New Variant of .NET Malware AgentTesla. Retrieved November 5, 2018.](https://www.fortinet.com/blog/threat-research/in-depth-analysis-of-net-malware-javaupdtr.html)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [Nutland, J. and Szeliga, M. (2024, October 21). Akira ransomware continues to evolve. Retrieved December 10, 2024.](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
- [SEONGSU PARK. (2022, December 27). BlueNoroff introduces new methods bypassing MoTW. Retrieved February 6, 2024.](https://securelist.com/bluenoroff-methods-bypass-motw/108383/)
- [Nikita Rostovcev. (2022, August 18). APT41 World Tour 2021 on a tight schedule. Retrieved February 22, 2024.](https://www.group-ib.com/blog/apt41-world-tour-2021/)
- [Perez, D. et al. (2021, May 27). Re-Checking Your Pulse: Updates on Chinese APT Actors Compromising Pulse Secure VPN Devices. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
- [Wiley, B. et al. (2021, December 29). OverWatch Exposes AQUATIC PANDA in Possession of Log4Shell Exploit Tools During Hands-on Intrusion Attempt. Retrieved January 18, 2022.](https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/)
- [Cisco Talos. (2024, April 24). ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices. Retrieved January 6, 2025.](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
- [Canadian Centre for Cyber Security. (2024, April 24). Cyber Activity Impacting CISCO ASA VPNs. Retrieved January 6, 2025.](https://www.cyber.gc.ca/en/news-events/cyber-activity-impacting-cisco-asa-vpns)
- [Yuste, J. Pastrana, S. (2021, February 9). Avaddon ransomware: an in-depth analysis and decryption of infected systems. Retrieved August 19, 2021.](https://arxiv.org/pdf/2102.04796.pdf)
- [Sogeti. (2021, March). Babuk Ransomware. Retrieved August 11, 2021.](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
- [Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1, 2020.](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
- [US Federal Bureau of Investigation & US Secret Service. (2022, February 11). Indicators of Compromise Associated with BlackByte Ransomware. Retrieved December 16, 2024.](https://www.ic3.gov/CSA/2022/220211.pdf)
- [Huseyin Can Yuceel. (2022, February 21). TTPs used by BlackByte Ransomware Targeting Critical Infrastructure. Retrieved December 16, 2024.](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)
- [James Nutland, Craig Jackson, Terryn Valikodath, & Brennan Evans. (2024, August 28). BlackByte blends tried-and-true tradecraft with newly disclosed vulnerabilities to support ongoing attacks. Retrieved December 16, 2024.](https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [Scott Henderson, Cristiana Kittner, Sarah Hawley & Mark Lechtik, Google Cloud. (2023, January 19). Suspected Chinese Threat Actors Exploiting FortiOS Vulnerability (CVE-2022-42475). Retrieved December 31, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
- [Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [Harbison, M. and Renals, P. (2022, July 5). When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors. Retrieved February 1, 2023.](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
- [Chell, D. PART 3: How I Met Your Beacon – Brute Ratel. Retrieved February 6, 2023.](https://www.mdsec.co.uk/2022/08/part-3-how-i-met-your-beacon-brute-ratel/)
- [Sushko, O. (2019, April 17). macOS Bundlore: Mac Virus Bypassing macOS Security Features. Retrieved June 30, 2020.](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
- [Phil Stokes. (2021, February 16). 20 Common Tools & Techniques Used by macOS Threat Actors & Malware. Retrieved August 23, 2021.](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
- [Giuliani, M., Allievi, A. (2011, February 28). Carberp - a modular information stealing trojan. Retrieved September 12, 2024.](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [Cybereason Nocturnus. (2020, December 23). Cybereason vs. Clop Ransomware. Retrieved May 11, 2021.](https://www.cybereason.com/blog/cybereason-vs.-clop-ransomware)
- [Mavis, N. (2020, September 21). The Art and Science of Detecting Cobalt Strike. Retrieved September 12, 2024.](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Burton, K. (n.d.). The Conficker Worm. Retrieved February 18, 2021.](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Lin, M. et al. (2024, January 31). Cutting Edge, Part 2: Investigating Ivanti Connect Secure VPN Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
- [Meltzer, M. et al. (2024, January 10). Active Exploitation of Two Zero-Day Vulnerabilities in Ivanti Connect Secure VPN. Retrieved February 27, 2024.](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/)
- [TrendMicro. (2014, September 03). DARKCOMET. Retrieved November 6, 2018.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
- [Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Pellegrino, G. (2025, December 16). BlindEagle Targets Colombian Government Agency with Caminho and DCRAT. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [TheWover. (2019, May 9). donut. Retrieved March 25, 2022.](https://github.com/TheWover/donut)
- [John Wolfram, Josh Murchie, Matt Lin, Daniel Ainsworth, Robert Wallace, Dimiter Andonov, Dhanesh Kizhakkinan, Jacob Thompson. (2025, January 8). Ivanti Connect Secure VPN Targeted in New Zero-Day Exploitation. Retrieved April 14, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
- [Vachon, F. (2017, October 30). Windigo Still not Windigone: An Ebury Update . Retrieved February 10, 2021.](https://www.welivesecurity.com/2017/10/30/windigo-ebury-update-2/)
- [Bichet, J. (2020, November 12). Egregor – Prolock: Fraternal Twins ?. Retrieved January 6, 2021.](https://www.intrinsec.com/egregor-prolock/?cn-reloaded=1)
- [Dragos. (2020, February 3). EKANS Ransomware and ICS Operations. Retrieved February 9, 2021.](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)
- [Zafra, D., et al. (2020, February 24). Ransomware Against the Machine: How Adversaries are Learning to Disrupt Industrial Production by Targeting IT and OT. Retrieved March 2, 2021.](https://www.fireeye.com/blog/threat-research/2020/02/ransomware-against-machine-learning-to-disrupt-industrial-production.html)
- [McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Falcone, R., et al. (2018, August 02). The Gorgon Group: Slithering Between Nation State and Cybercrime. Retrieved August 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/08/unit42-gorgon-group-slithering-nation-state-cybercrime/)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [Reynolds, J.. (2016, September 14). H1N1: Technical analysis reveals new capabilities – part 2. Retrieved November 17, 2024.](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)
- [Baumgartner, K., Golovkin, M.. (2015, May). The MsnMM Campaigns: The Earliest Naikon APT Campaigns. Retrieved April 10, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
- [Guerrero-Saade, J. (2022, February 23). HermeticWiper | New Destructive Malware Used In Cyber Attacks on Ukraine. Retrieved March 25, 2022.](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
- [Thomas, W. et al. (2022, February 25). CrowdStrike Falcon Protects from New Wiper Malware Used in Ukraine Cyberattacks. Retrieved March 25, 2022.](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
- [Dani, M. (2022, March 1). Ukrainian Targets Hit by HermeticWiper, New Datawiper Malware. Retrieved March 25, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
- [Chen, J. et al. (2021, February 3). Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes. Retrieved April 5, 2021.](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [MSTIC. (2022, September 8). Microsoft investigates Iranian attacks against the Albanian government. Retrieved August 6, 2024.](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)
- [Counter Threat Unit Research Team . (2022, June 23). BRONZE STARLIGHT RANSOMWARE OPERATIONS USE HUI LOADER. Retrieved December 7, 2023.](https://www.secureworks.com/research/bronze-starlight-ransomware-operations-use-hui-loader)
- [Unit 42. (2019, December 2). Imminent Monitor – a RAT Down Under. Retrieved May 5, 2020.](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)
- [Carvey, H. (2024, May 1). LOLBin to INC Ransomware. Retrieved June 5, 2024.](https://www.huntress.com/blog/lolbin-to-inc-ransomware)
- [Symantec Threat Intelligence. (2020, June 25). WastedLocker: Symantec Identifies Wave of Attacks Against U.S. Organizations. Retrieved May 20, 2021.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)
- [Mandiant Intelligence. (2022, June 2). To HADES and Back: UNC2165 Shifts to LOCKBIT to Evade Sanctions. Retrieved July 29, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [Cisco Talos. (2025, February 20). Weathering the storm: In the midst of a Typhoon. Retrieved February 24, 2025.](https://blog.talosintelligence.com/salt-typhoon-analysis/)
- [Tarakanov , D.. (2013, September 11). The “Kimsuky” Operation: A North Korean APT?. Retrieved August 13, 2019.](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [Jazi, H. (2021, February). LazyScripter: From Empire to double RAT. Retrieved November 17, 2024.](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
- [Black Lotus Labs. (2023, December 13). Routers Roasting On An Open Firewall: The KV-Botnet Investigation. Retrieved June 10, 2024.](https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Tools Report. Retrieved March 10, 2016.](https://web.archive.org/web/20220425194457/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Tools-Report.pdf)
- [US-CERT. (2018, March 09). Malware Analysis Report (MAR) - 10135536.11.WHITE. Retrieved June 13, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536.11.WHITE.pdf)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [FBI. (2022, February 4). Indicators of Compromise Associated with LockBit 2.0 Ransomware. Retrieved January 24, 2025.](https://www.ic3.gov/CSA/2022/220204.pdf)
- [Elsad, A. et al. (2022, June 9). LockBit 2.0: How This RaaS Operates and How to Protect Against It. Retrieved January 24, 2025.](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
- [CISA et al. (2023, June 14). UNDERSTANDING RANSOMWARE THREAT ACTORS: LOCKBIT. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [INCIBE-CERT. (2024, March 14). LockBit: response and recovery actions. Retrieved February 5, 2025.](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
- [Greenberg, A. (2019, March 25). A Guide to LockerGoga, the Ransomware Crippling Industrial Firms. Retrieved July 17, 2019.](https://www.wired.com/story/lockergoga-ransomware-crippling-industrial-firms/)
- [Leandro Fróes, Netskope. (2025, January 23). Lumma Stealer: Fake CAPTCHAs & New Techniques to Evade Detection. Retrieved March 22, 2025.](https://www.netskope.com/blog/lumma-stealer-fake-captchas-new-techniques-to-evade-detection)
- [Phil Stokes. (2021, January 11). FADE DEAD | Adventures in Reversing Malicious Run-Only AppleScripts. Retrieved September 29, 2022.](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/)
- [DFIR Report. (2022, March 21). APT35 Automates Initial Access Using ProxyShell. Retrieved May 25, 2022.](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)
- [Hromcova, Z. and Burgher, A. (2023, September 21). OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes. Retrieved November 21, 2024.](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
- [Mundo, A. (2020, March 26). Ransomware Maze. Retrieved May 18, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
- [Brandt, A., Mackenzie, P.. (2020, September 17). Maze Attackers Adopt Ragnar Locker Virtual Machine Technique. Retrieved October 9, 2020.](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)
- [Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Del Fierro, C. Kessem, L.. (2020, January 8). From Mega to Giga: Cross-Version Comparison of Top MegaCortex Modifications. Retrieved February 15, 2021.](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
- [Erlich, C. (2020, April 3). The Avast Abuser: Metamorfo Banking Malware Hides By Abusing Avast Executable. Retrieved May 26, 2020.](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
- [Sierra, E., Iglesias, G.. (2018, April 24). Metamorfo Campaigns Targeting Brazilian Users. Retrieved July 30, 2020.](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
- [Check Point Research Team. (2021, August 14). Indra - Hackers Behind Recent Attacks on Iran. Retrieved February 17, 2022.](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [Peretz, A. and Theck, E. (2021, March 5). Earth Vetala – MuddyWater Continues to Target Organizations in the Middle East. Retrieved March 18, 2021.](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
- [Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
- [The DigiTrust Group. (2017, January 01). NanoCore Is Not Your Average RAT. Retrieved November 9, 2018.](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
- [Kasza, A., Halfpop, T. (2016, February 09). NanoCoreRAT Behind an Increase in Tax-Themed Phishing E-mails. Retrieved November 9, 2018.](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
- [Victor, K.. (2020, May 18). Netwalker Fileless Ransomware Injected via Reflective Loading . Retrieved May 26, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
- [Szappanos, G., Brandt, A.. (2020, May 27). Netwalker ransomware tools give insight into threat actor. Retrieved May 27, 2020.](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)
- [McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
- [CISA. (2023, December 18). #StopRansomware: Play Ransomware AA23-352A. Retrieved September 24, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)
- [Trend Micro Research. (2023, July 21). Ransomware Spotlight: Play. Retrieved September 24, 2024.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
- [Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
- [Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.](https://objective-see.com/blog/blog_0x25.html)
- [Dumont, R. (2022, June 13). Technical Analysis of PureCrypter: A Fully-Functional Loader Distributing Remote Access Trojans and Information Stealers. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
- [Crowdstrike Global Intelligence Team. (2014, June 9). CrowdStrike Intelligence Report: Putter Panda. Retrieved January 22, 2016.](http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf)
- [CERT-FR. (2020, April 1). ATTACKS INVOLVING THE MESPINOZA/PYSA RANSOMWARE. Retrieved March 1, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
- [Group IB. (2020, September). LOCK LIKE A PRO. Retrieved November 17, 2024.](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
- [Magdy, S. et al. (2022, August 25). New Golang Ransomware Agenda Customizes Attacks. Retrieved September 26, 2025.](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
- [SentinelOne. (2022, November 30). Agenda (Qilin). Retrieved September 26, 2025.](https://www.sentinelone.com/anthology/agenda-qilin/)
- [Halcyon RISE Team. (2024, October 24). New Qilin.B Ransomware Variant Boasts Enhanced Encryption and Defense Evasion. Retrieved September 26, 2025.](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
- [Hacioglu, S. (2025, March 10). Qilin Ransomware: Exposing the TTPs Behind One of the Most Active Ransomware Campaigns of 2024. Retrieved September 26, 2025.](https://www.picussecurity.com/resource/blog/qilin-ransomware)
- [Aime, F. et al. (n.d.). Solving the 7777 Botnet enigma: A cybersecurity quest. Retrieved July 23, 2024.](https://blog.sekoia.io/solving-the-7777-botnet-enigma-a-cybersecurity-quest/)
- [Microsoft Threat Intelligence. (2024, October 31). Chinese threat actor Storm-0940 uses credentials from password spray attacks from a covert network. Retrieved June 4, 2025.](https://www.microsoft.com/en-us/security/blog/2024/10/31/chinese-threat-actor-storm-0940-uses-credentials-from-password-spray-attacks-from-a-covert-network/)
- [Batista, João. Gi7w0rm. (2024, August 27). Retrieved June 5, 2025.](https://www.bitsight.com/blog/7777-botnet-insights-multi-target-botnet)
- [SophosLabs. (2020, May 21). Ragnar Locker ransomware deploys virtual machine to dodge security. Retrieved June 29, 2020.](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
- [Patrick Schläpfer . (2024, April 10). Raspberry Robin Now Spreading Through Windows Script Files. Retrieved May 17, 2024.](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
- [Splunk Threat Research Team. (2023, June 1). Do Not Cross The 'RedLine' Stealer: Detections and Analysis. Retrieved September 17, 2025.](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
- [Cylance. (2019, July 3). hreat Spotlight: Sodinokibi Ransomware. Retrieved August 4, 2020.](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
- [Lee, S. (2019, May 17). CB TAU Threat Intelligence Notification: RobbinHood Ransomware Stops 181 Windows Services Before Encryption. Retrieved July 29, 2019.](https://www.carbonblack.com/2019/05/17/cb-tau-threat-intelligence-notification-robbinhood-ransomware-stops-181-windows-services-before-encryption/)
- [Liebenberg, D.. (2018, August 30). Rocke: The Champion of Monero Miners. Retrieved May 26, 2020.](https://blog.talosintelligence.com/2018/08/rocke-champion-of-monero-miners.html)
- [Xingyu, J.. (2019, January 17). Malware Used by Rocke Group Evolves to Evade Detection by Cloud Security Products. Retrieved May 26, 2020.](https://unit42.paloaltonetworks.com/malware-used-by-rocke-group-evolves-to-evade-detection-by-cloud-security-products/)
- [Goody, K., et al (2019, January 11). A Nasty Trick: From Credential Theft Malware to Business Disruption. Retrieved May 12, 2020.](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Mandiant Incident Response. (2025, May 6). Defending Against UNC3944: Cybercrime Hardening Guidance from the Frontlines. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)
- [Socket Research Team. (2025, November 24). Shai Hulud Strikes Again (v2). Retrieved April 9, 2026.](https://socket.dev/blog/shai-hulud-strikes-again-v2)
- [Microsoft Threat Intelligence. (2025, July 22). Disrupting active exploitation of on-premises SharePoint vulnerabilities. Retrieved October 15, 2025.](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/#storm-2603)
- [Unit 42. (2025, July 31). Active Exploitation of Microsoft SharePoint Vulnerabilities: Threat Brief (Updated). Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/microsoft-sharepoint-cve-2025-49704-cve-2025-49706-cve-2025-53770/)
- [Cristian Souza, Eduardo Ovalle, Ashley Muñoz, & Christopher Zachor. (2024, May 23). ShrinkLocker: Turning BitLocker into ransomware. Retrieved December 7, 2024.](https://securelist.com/ransomware-abuses-bitlocker/112643/)
- [Splunk Threat Research Team , Teoderick Contreras. (2024, September 5). ShrinkLocker Malware: Abusing BitLocker to Lock Your Data. Retrieved December 7, 2024.](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [Remillano, A., Urbanec, J. (2019, September 19). Skidmap Linux Malware Uses Rootkit Capabilities to Hide Cryptocurrency-Mining Payload. Retrieved June 4, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
- [MSTIC, CDOC, 365 Defender Research Team. (2021, January 20). Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop . Retrieved January 22, 2021.](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
- [DHS/CISA. (2026, February 26). MAR-25993211-r1.v2 Ivanti Connect Secure (RESURGE): AR25-087A. Retrieved April 17, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
- [Sila Ozeren Hacioglu. (2025, May 5). UNC5221’s Latest Exploit: Weaponizing CVE-2025-22457 in Ivanti Connect Secure. Retrieved April 13, 2026.](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: PAKLOG, CorKLOG, and SplatCloak | P2. Retrieved September 12, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
- [Cybereason Global SOC Team. (n.d.). THREAT ANALYSIS REPORT: Inside the LockBit Arsenal - The StealBit Exfiltration Tool. Retrieved January 29, 2025.](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
- [Mercer, W. et al. (2020, June 29). PROMETHIUM extends global reach with StrongPity3 APT. Retrieved July 20, 2020.](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [Stephen Eckels, Jay Smith, William Ballenthin. (2020, December 24). SUNBURST Additional Technical Details. Retrieved January 6, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/sunburst-additional-technical-details.html)
- [Larson, S. and Wise, J. (2022, February 15). Charting TA2541's Flight. Retrieved September 12, 2023.](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [AT&T Alien Labs. (2021, September 8). TeamTNT with new campaign aka Chimaera. Retrieved September 22, 2021.](https://cybersecurity.att.com/blogs/labs-research/teamtnt-with-new-campaign-aka-chimaera)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Patrick Wardle. (2020, June 29). OSX.EvilQuest Uncovered part i: infection, persistence, and more!. Retrieved March 18, 2021.](https://objective-see.com/blog/blog_0x59.html)
- [Cylance. (2014, December). Operation Cleaver. Retrieved September 14, 2017.](https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf)
- [Anthony, N., Pascual, C.. (2018, November 1). Trickbot Shows Off New Trick: Password Grabber Module. Retrieved November 16, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [Marvi, A. et al.. (2023, March 16). Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation. Retrieved March 22, 2023.](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Sygnia Team. (2024, June 3). China-Nexus Threat Group ‘Velvet Ant’ Abuses F5 Load Balancers for Persistence. Retrieved March 14, 2025.](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [Su, V. et al. (2019, December 11). Waterbear Returns, Uses API Hooking to Evade Security. Retrieved February 22, 2021.](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
- [Falcone, R. et al.. (2022, January 20). Threat Brief: Ongoing Russia and Ukraine Cyber Conflict. Retrieved March 10, 2022.](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)
- [Biasini, N. et al.. (2022, January 21). Ukraine Campaign Delivers Defacement and Wipers, in Continued Escalation. Retrieved March 14, 2022.](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
- [S2W. (2022, January 18). Analysis of Destructive Malware (WhisperGate) targeting Ukraine. Retrieved March 14, 2022.](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)
- [DHS/CISA. (2020, October 28). Ransomware Activity Targeting the Healthcare and Public Health Sector. Retrieved October 28, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-302a)
- [Kimberly Goody, Jeremy Kennelly, Joshua Shilko, Steve Elovitz, Douglas Bienstock. (2020, October 28). Unhappy Hour Special: KEGTAP and SINGLEMALT With a Ransomware Chaser. Retrieved October 28, 2020.](https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html)
- [The DFIR Report. (2020, October 8). Ryuk’s Return. Retrieved October 9, 2020.](https://thedfirreport.com/2020/10/08/ryuks-return/)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Zscaler Threatlabz. (2025, January 27). Technical Analysis of Xloader Versions 6 and 7 | Part 1. Retrieved March 11, 2025.](https://www.zscaler.com/blogs/security-research/technical-analysis-xloader-versions-6-and-7-part-1)
- [Gustavo Palazolo, Netskope. (2022, March 11). New Formbook Campaign Delivered Through Phishing Emails. Retrieved March 11, 2025.](https://www.netskope.com/blog/new-formbook-campaign-delivered-through-phishing-emails)
- [McLellan, T. et al. (2024, January 12). Cutting Edge: Suspected APT Targets Ivanti Connect Secure VPN in New Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)
- [Christopher Brumm. (2021, August 4). My learnings on Microsoft Defender for Endpoint and Exclusions. Retrieved March 18, 2025.](https://medium.com/codex/my-learnings-on-microsoft-defender-for-endpoint-and-exclusions-ddacf2fdd047)

---

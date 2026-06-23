# Process Injection

## Description

Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process.

There are many different ways to inject code into a process, many of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific.

More sophisticated samples may perform multiple process injections to segment modules and further evade detection, utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0028 | 2015 Ukraine Electric Power Attack | During the 2015 Ukraine Electric Power Attack , Sandworm Team loaded BlackEnergy into svchost.exe, which then launched iexplore.exe for their C2. [1] |
| C0057 | 3CX Supply Chain Attack | During the 3CX Supply Chain Attack , AppleJeus 's VEILEDSIGNAL uses process injection to inject the C2 communication module code in the first found process instance of Chrome, Firefox, or Edge web browsers. It also monitors the established named pipe and re-injects the C2 communication module if necessary. [2] |
| S0469 | ABK | ABK has the ability to inject shellcode into svchost.exe. [3] |
| S0331 | Agent Tesla | Agent Tesla can inject into known, vulnerable binaries on targeted hosts. [4] |
| S1074 | ANDROMEDA | ANDROMEDA can inject into the wuauclt.exe process to perform C2 actions. [5] |
| G0050 | APT32 | APT32 malware has injected a Cobalt Strike beacon into Rundll32.exe. [6] |
| G0067 | APT37 | APT37 injects its malware variant, ROKRAT , into the cmd.exe process. [7] |
| G0082 | APT38 | APT38 has injected malicious payloads into the explorer.exe process. [8] |
| G0096 | APT41 | APT41 malware TIDYELF loaded the main WINTERLOVE component by injecting it into the iexplore.exe process. [9] |
| G1023 | APT5 | APT5 has used the CLEANPULSE utility to insert command line strings into a targeted process to alter its functionality. [10] |
| C0046 | ArcaneDoor | ArcaneDoor included injecting code into the AAA and Crash Dump processes on infected Cisco ASA devices. [11] |
| S0438 | Attor | Attor 's dispatcher can inject itself into running processes to gain higher privileges and to evade detection. [12] |
| S0347 | AuditCred | AuditCred can inject code from files to other running processes. [13] |
| S0473 | Avenger | Avenger has the ability to inject shellcode into svchost.exe. [3] |
| S0093 | Backdoor.Oldrea | Backdoor.Oldrea injects itself into explorer.exe. [14] [15] |
| S1081 | BADHATCH | BADHATCH can inject itself into an existing explorer.exe process by using RtlCreateUserThread . [16] [17] |
| S0534 | Bazar | Bazar can inject code through calling VirtualAllocExNuma . [18] |
| S0470 | BBK | BBK has the ability to inject shellcode into svchost.exe. [3] |
| G1043 | BlackByte | BlackByte has injected Cobalt Strike into wuauclt.exe during intrusions. [19] BlackByte has injected ransomware into svchost.exe before encryption. [20] |
| S1181 | BlackByte 2.0 Ransomware | BlackByte 2.0 Ransomware injects into a newly-created svchost.exe process prior to device encryption. [21] |
| S1039 | Bumblebee | Bumblebee can inject code into multiple processes on infected endpoints. [22] |
| S0348 | Cardinal RAT | Cardinal RAT injects into a newly spawned process created from a native Windows executable. [23] |
| S0660 | Clambling | Clambling can inject into the svchost.exe process for execution. [24] |
| S1105 | COATHANGER | COATHANGER includes a binary labeled authd that can inject a library into a running process and then hook an existing function within that process with a new function from that library. [25] |
| G0080 | Cobalt Group | Cobalt Group has injected code into trusted processes. [26] |
| S0154 | Cobalt Strike | Cobalt Strike can inject a variety of payloads into processes dynamically chosen by the adversary. [27] [28] [29] |
| S0614 | CostaBricks | CostaBricks can inject a payload into the memory of a compromised host. [30] |
| C0029 | Cutting Edge | During Cutting Edge , threat actors used malicious SparkGateway plugins to inject shared objects into web process memory on compromised Ivanti Secure Connect VPNs to enable deployment of backdoors. [31] |
| S0695 | Donut | Donut includes a subproject DonutTest to inject shellcode into a target process. [32] |
| S9021 | DOWNIISSA | DOWNIISSA can inject shellcode directly into process memory including WINWORD.exe and msiexec.exe. [33] |
| S1159 | DUSTTRAP | DUSTTRAP compromises the .text section of a legitimate system DLL in %windir% to hold the contents of retrieved plug-ins. [34] |
| S0024 | Dyre | Dyre has the ability to directly inject its code into the web browser process. [35] |
| S0554 | Egregor | Egregor can inject its payload into iexplore.exe process. [36] |
| S0363 | Empire | Empire contains multiple modules for injecting into processes, such as Invoke-PSInject . [37] |
| G0047 | Gamaredon Group | Gamaredon Group has injected Remcos into explorer.exe. [38] |
| S0168 | Gazer | Gazer injects its communication module into an Internet accessible process through which it performs C2. [39] [40] |
| S0032 | gh0st RAT | gh0st RAT can inject malicious code into process created by the "Command_Create&Inject" function. [41] |
| S0561 | GuLoader | GuLoader has the ability to inject shellcode into a donor processes that is started in a suspended state. GuLoader has previously used RegAsm as a donor process. [42] |
| S9023 | HiddenFace | HiddenFace can inject code directly into legitimate applications. [43] |
| S0376 | HOPLIGHT | HOPLIGHT has injected into running processes. [44] |
| S0040 | HTRAN | HTRAN can inject into into running processes. [45] |
| S0398 | HyperBro | HyperBro can run shellcode it injects into a newly created process. [46] |
| S0260 | InvisiMole | InvisiMole can inject itself into another process to avoid detection including use of a technique called ListPlanting that customizes the sorting algorithm in a ListView structure. [47] |
| S0581 | IronNetInjector | IronNetInjector can use an IronPython scripts to load a .NET injector to inject a payload into its own or a remote process. [48] |
| S0044 | JHUHUGIT | JHUHUGIT performs code injection injecting its own functions to browser processes. [49] [50] |
| S0201 | JPIN | JPIN can inject content into lsass.exe to load a module. [51] |
| G0094 | Kimsuky | Kimsuky has used Win7Elevate to inject malicious code into explorer.exe. [52] |
| S0681 | Lizar | Lizar can migrate the loader into another process. [53] |
| S9020 | LODEINFO | LODEINFO can inject shellcode into the memory of compromised hosts. [54] [55] [56] |
| S1059 | metaMain | metaMain can inject the loader file, Speech02.db, into a process. [57] |
| S0084 | Mis-Type | Mis-Type has been injected directly into a running process, including explorer.exe . [58] |
| S1122 | Mispadu | Mispadu 's binary is injected into memory via WriteProcessMemory . [59] [60] |
| S0247 | NavRAT | NavRAT copies itself into a running Internet Explorer process to evade detection. [61] |
| S0198 | NETWIRE | NETWIRE can inject code into system processes including notepad.exe, svchost.exe, and vbc.exe. [62] |
| S1100 | Ninja | Ninja has the ability to inject an agent module into a new process and arbitrary shellcode into running processes. [63] [64] |
| S9025 | NOOPLDR | NOOPLDR can inject decrypted payloads into processes including wuauclt.exe., rdrleakdiag.exe, and tabcal.exe. [65] |
| C0013 | Operation Sharpshooter | During Operation Sharpshooter , threat actors leveraged embedded shellcode to inject a downloader into the memory of Word. [66] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors injected code into a selected process, which in turn launches a command as a child process of the original. [67] |
| S0664 | Pandora | Pandora can start and inject code into a new svchost process. [68] |
| S1050 | PcShare | The PcShare payload has been injected into the logagent.exe and rdpclip.exe processes. [69] |
| G0068 | PLATINUM | PLATINUM has used various methods of process injection including hot patching. [51] |
| S0378 | PoshC2 | PoshC2 contains multiple modules for injecting into processes, such as Invoke-PSInject . [70] |
| S9019 | PureCrypter | PureCrypter can inject its final stage into another process on the targeted system. [71] |
| S0650 | QakBot | QakBot can inject itself into processes including explore.exe, Iexplore.exe, Mobsync.exe., and wermgr.exe. [72] [73] [74] [75] [76] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 exploited CVE-2025-21590 to enable malicious code injection into the memory of legitimate processes. [77] [78] |
| S0332 | Remcos | Remcos has a command to hide itself by injecting into another process. [79] |
| S0496 | REvil | REvil can inject itself into running processes on a compromised host. [80] |
| S0240 | ROKRAT | ROKRAT can use VirtualAlloc , WriteProcessMemory , and then CreateRemoteThread to execute shellcode within the address space of Notepad.exe . [81] |
| S0446 | Ryuk | Ryuk has injected itself into remote processes to encrypt files using a combination of VirtualAlloc , WriteProcessMemory , and CreateRemoteThread . [82] |
| S0596 | ShadowPad | ShadowPad has injected an install module into a newly created process. [83] |
| G0091 | Silence | Silence has injected a DLL library containing a Trojan into the fwmain32.exe process. [84] |
| S0692 | SILENTTRINITY | SILENTTRINITY can inject shellcode directly into Excel.exe or a specific process. [85] |
| S0633 | Sliver | Sliver includes multiple methods to perform process injection to migrate the framework into other, potentially privileged processes on the victim machine. [86] [87] [88] [89] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA can inject into running processes on a compromised host. [90] |
| S0226 | Smoke Loader | Smoke Loader injects into the Internet Explorer process. [91] |
| S0380 | StoneDrill | StoneDrill has relied on injecting its payload directly into the process memory of the victim's preferred browser. [92] |
| G1018 | TA2541 | TA2541 has injected malicious code into legitimate .NET related processes including regsvcs.exe, msbuild.exe, and installutil.exe. [93] [94] |
| S0266 | TrickBot | TrickBot has used Nt* Native API functions to inject code into legitimate processes such as wermgr.exe . [95] |
| S0436 | TSCookie | TSCookie has the ability to inject code into the svchost.exe, iexplorer.exe, explorer.exe, and default browser processes. [96] |
| G0010 | Turla | Turla has also used PowerSploit 's Invoke-ReflectivePEInjection.ps1 to reflectively load a PowerShell payload into a random process on the victim system. [97] |
| G1047 | Velvet Ant | Velvet Ant initial execution included launching multiple svchost processes and injecting code into them. [98] |
| S0670 | WarzoneRAT | WarzoneRAT has the ability to inject malicious DLLs into a specific process for privilege escalation. [99] |
| S0579 | Waterbear | Waterbear can inject decrypted shellcode into the LanmanServer service. [100] |
| S0206 | Wiarp | Wiarp creates a backdoor through which remote attackers can inject files into running processes. [101] |
| S0176 | Wingbird | Wingbird performs multiple process injections to hijack system processes and execute malicious code. [102] |
| G0102 | Wizard Spider | Wizard Spider has used process injection to execute payloads to escalate privileges. [103] |
| S1065 | Woody RAT | Woody RAT can inject code into a targeted process by writing to the remote memory of an infected system and then create a remote thread. [104] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1040 | Behavior Prevention on Endpoint | Some endpoint security solutions can be configured to block some types of process injection based on common sequences of behavior that occur during the injection process. For example, on Windows 10, Attack Surface Reduction (ASR) rules may prevent Office applications from code injection. [105] |
| M1026 | Privileged Account Management | Utilize Yama (ex: /proc/sys/kernel/yama/ptrace_scope) to mitigate ptrace based process injection by restricting the use of ptrace to privileged users only. Other mitigation controls involve the deployment of security kernel modules that provide advanced access control and process restrictions such as SELinux, grsecurity, and AppArmor. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0508 | Behavioral Detection of Process Injection Across Platforms | AN1399 | Detects process injection by correlating memory manipulation API calls (e.g., VirtualAllocEx, WriteProcessMemory), suspicious thread creation (e.g., CreateRemoteThread), and unusual DLL loads within another process's context. |
| AN1400 | Detects ptrace- or memfd-based process injection through audit logs capturing system calls (e.g., ptrace, mmap) targeting running processes along with suspicious file descriptors or memory writes. |  |  |
| AN1401 | Detects memory-based injection by monitoring task_for_pid , mach_vm_write , and dylib injection patterns through DYLD_INSERT_LIBRARIES or manual memory mapping. |  |  |

---

## References

- [Booz Allen Hamilton. (2016). When The Lights Went Out. Retrieved December 18, 2024.](https://www.boozallen.com/content/dam/boozallen/documents/2016/09/ukraine-report-when-the-lights-went-out.pdf)
- [Jeff Johnson, Fred Plan, Adrian Sanchez, Renato Fontana, Jake Nicastro, Dimiter Andonov, Marius Fodoreanu, Daniel Scott. (2023, April 20). 3CX Software Supply Chain Compromise Initiated by a Prior Software Supply Chain Compromise; Suspected North Korean Actor Responsible. Retrieved August 25, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise/)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [Walter, J. (2020, August 10). Agent Tesla | Old RAT Uses New Tricks to Stay on Top. Retrieved December 11, 2020.](https://labs.sentinelone.com/agent-tesla-old-rat-uses-new-tricks-to-stay-on-top/)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)
- [SEONGSU PARK. (2022, December 27). BlueNoroff introduces new methods bypassing MoTW. Retrieved February 6, 2024.](https://securelist.com/bluenoroff-methods-bypass-motw/108383/)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [Perez, D. et al. (2021, May 27). Re-Checking Your Pulse: Updates on Chinese APT Actors Compromising Pulse Secure VPN Devices. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
- [Cisco Talos. (2024, April 24). ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices. Retrieved January 6, 2025.](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [Trend Micro. (2018, November 20). Lazarus Continues Heists, Mounts Attacks on Financial Organizations in Latin America. Retrieved December 3, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-continues-heists-mounts-attacks-on-financial-organizations-in-latin-america/)
- [Symantec Security Response. (2014, June 30). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
- [Slowik, J. (2021, October). THE BAFFLING BERSERK BEAR: A DECADE’S ACTIVITY TARGETING CRITICAL INFRASTRUCTURE. Retrieved December 6, 2021.](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
- [Savelesky, K., et al. (2019, July 23). ABADBABE 8BADFOOD: Discovering BADHATCH and a Detailed Look at FIN8's Tooling. Retrieved September 8, 2021.](https://blog.gigamon.com/2019/07/23/abadbabe-8badf00d-discovering-badhatch-and-a-detailed-look-at-fin8s-tooling/)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Huseyin Can Yuceel. (2022, February 21). TTPs used by BlackByte Ransomware Targeting Critical Infrastructure. Retrieved December 16, 2024.](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)
- [Symantec Threat Hunter Team. (2022, October 21). Exbyte: BlackByte Ransomware Attackers Deploy New Exfiltration Tool. Retrieved December 16, 2024.](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [Cybereason. (2022, August 17). Bumblebee Loader – The High Road to Enterprise Domain Control. Retrieved August 29, 2022.](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
- [Grunzweig, J.. (2017, April 20). Cardinal RAT Active for Over Two Years. Retrieved December 8, 2018.](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Dutch Military Intelligence and Security Service (MIVD) & Dutch General Intelligence and Security Service (AIVD). (2024, February 6). Ministry of Defense of the Netherlands uncovers COATHANGER, a stealthy Chinese FortiGate RAT. Retrieved February 7, 2024.](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
- [Matveeva, V. (2017, August 15). Secrets of Cobalt. Retrieved October 10, 2018.](https://www.group-ib.com/blog/cobalt)
- [Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [Lin, M. et al. (2024, February 27). Cutting Edge, Part 3: Investigating Ivanti Connect Secure VPN Exploitation and Persistence Attempts. Retrieved March 1, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
- [TheWover. (2019, May 9). donut. Retrieved March 25, 2022.](https://github.com/TheWover/donut)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part I. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [hasherezade. (2015, November 4). A Technical Look At Dyreza. Retrieved June 15, 2020.](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
- [Cybleinc. (2020, October 31). Egregor Ransomware – A Deep Dive Into Its Activities and Techniques. Retrieved December 29, 2020.](https://cybleinc.com/2020/10/31/egregor-ransomware-a-deep-dive-into-its-activities-and-techniques/)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Venere, G. (2025, March 28). Gamaredon campaign abuses LNK files to distribute Remcos backdoor. Retrieved July 23, 2025.](https://blog.talosintelligence.com/gamaredon-campaign-distribute-remcos/)
- [ESET. (2017, August). Gazing at Gazer: Turla’s new second stage backdoor. Retrieved September 14, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2017, August 30). Introducing WhiteBear. Retrieved September 21, 2017.](https://securelist.com/introducing-whitebear/81638/)
- [Quinn, J. (2019, March 25). The odd case of a Gh0stRAT variant. Retrieved July 15, 2020.](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
- [Salem, E. (2021, April 19). Dancing With Shellcodes: Cracking the latest version of Guloader. Retrieved July 7, 2021.](https://elis531989.medium.com/dancing-with-shellcodes-cracking-the-latest-version-of-guloader-75083fb15cb4)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [The Australian Cyber Security Centre (ACSC), the Canadian Centre for Cyber Security (CCCS), the New Zealand National Cyber Security Centre (NZ NCSC), CERT New Zealand, the UK National Cyber Security Centre (UK NCSC) and the US National Cybersecurity and Communications Integration Center (NCCIC). (2018, October 11). Joint report on publicly available hacking tools. Retrieved March 11, 2019.](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
- [Falcone, R. and Lancaster, T. (2019, May 28). Emissary Panda Attacks Middle East Government Sharepoint Servers. Retrieved July 9, 2019.](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Reichel, D. (2021, February 19). IronNetInjector: Turla’s New Malware Loading Tool. Retrieved February 24, 2021.](https://unit42.paloaltonetworks.com/ironnetinjector/)
- [F-Secure. (2015, September 8). Sofacy Recycles Carberp and Metasploit Code. Retrieved August 3, 2016.](https://labsblog.f-secure.com/2015/09/08/sofacy-recycles-carberp-and-metasploit-code/)
- [Lee, B, et al. (2018, February 28). Sofacy Attacks Multiple Government Entities. Retrieved March 15, 2018.](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [Tarakanov , D.. (2013, September 11). The “Kimsuky” Operation: A North Korean APT?. Retrieved August 13, 2019.](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part II. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
- [Breitenbacher, D. (2022, December 14). Unmasking MirrorFace: Operation LiberalFace targeting Japanese political entities. Retrieved April 17, 2026.](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
- [ITOCHU. (2024, January 24). The Endless Struggle Against APT10: Insights from LODEINFO v0.6.6 - v0.7.3 Analysis. Retrieved April 17, 2026.](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Pedro Tavares (Segurança Informática). (2020, September 15). Threat analysis: The emergent URSA trojan impacts many countries using a sophisticated loader. Retrieved March 13, 2024.](https://seguranca-informatica.pt/threat-analysis-the-emergent-ursa-trojan-impacts-many-countries-using-a-sophisticated-loader/)
- [SCILabs. (2021, December 23). Cyber Threat Profile Malteiro. Retrieved March 13, 2024.](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
- [Mercer, W., Rascagneres, P. (2018, May 31). NavRAT Uses US-North Korea Summit As Decoy For Attacks In South Korea. Retrieved June 11, 2018.](https://blog.talosintelligence.com/2018/05/navrat.html)
- [Lambert, T. (2020, January 29). Intro to Netwire. Retrieved January 7, 2021.](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [L. O'Donnell. (2019, March 3). RSAC 2019: New Operation Sharpshooter Data Reveals Higher Complexity, Scope. Retrieved September 26, 2022.](https://threatpost.com/sharpshooter-complexity-scope/142359/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Lunghi, D. and Lu, K. (2021, April 9). Iron Tiger APT Updates Toolkit With Evolved SysUpdate Malware. Retrieved November 12, 2021.](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [Dumont, R. (2022, June 13). Technical Analysis of PureCrypter: A Fully-Functional Loader Distributing Remote Access Trojans and Information Stealers. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
- [Mendoza, E. et al. (2020, May 25). Qakbot Resurges, Spreads through VBS Files. Retrieved September 27, 2021.](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)
- [Sette, N. et al. (2020, June 4). Qakbot Malware Now Exfiltrating Emails for Sophisticated Thread Hijacking Attacks. Retrieved September 27, 2021.](https://www.kroll.com/en/insights/publications/cyber/qakbot-malware-exfiltrating-emails-thread-hijacking-attacks)
- [Trend Micro. (2020, December 17). QAKBOT: A decade-old malware still with new tricks. Retrieved November 17, 2024.](https://success.trendmicro.com/en-US/solution/KA-0011282)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [Kenefick, I. et al. (2022, October 12). Black Basta Ransomware Gang Infiltrates Networks via QAKBOT, Brute Ratel, and Cobalt Strike. Retrieved February 6, 2023.](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
- [Lamparski, L. et al. (2025, March 11). Ghost in the Router: China-Nexus Espionage Actor UNC3886 Targets Juniper Routers. Retrieved June 24, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers)
- [Juniper Networks, Cybersecurity R&D. (2025, March 11). The RedPenguin Malware Incident. Retrieved June 24, 2025.](https://supportportal.juniper.net/sfc/servlet.shepherd/document/download/069Dp00000FzdmIIAR?operationContext=S1)
- [Bacurio, F., Salvio, J. (2017, February 14). REMCOS: A New RAT In The Wild. Retrieved November 6, 2018.](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)
- [Saavedra-Morales, J, et al. (2019, October 20). McAfee ATR Analyzes Sodinokibi aka REvil Ransomware-as-a-Service – Crescendo. Retrieved August 5, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-crescendo/)
- [Jazi, Hossein. (2021, January 6). Retrohunting APT37: North Korean APT used VBA self decode technique to inject RokRat. Retrieved March 22, 2022.](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
- [Hanel, A. (2019, January 10). Big Game Hunting with Ryuk: Another Lucrative Targeted Ransomware. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
- [Kaspersky Lab. (2017, August). ShadowPad: popular server management software hit in supply chain attack. Retrieved March 22, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
- [Group-IB. (2018, September). Silence: Moving Into the Darkside. Retrieved May 5, 2020.](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [Microsoft Security Experts. (2022, August 24). Looking for the ‘Sliver’ lining: Hunting for emerging command-and-control frameworks. Retrieved March 24, 2025.](https://www.microsoft.com/en-us/security/blog/2022/08/24/looking-for-the-sliver-lining-hunting-for-emerging-command-and-control-frameworks/)
- [Cybereason Global SOC and Incident Response Team. (n.d.). Sliver C2 Leveraged by Many Threat Actors. Retrieved March 24, 2025.](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)
- [Kervella, R. (2019, August 4). Cross-platform General Purpose Implant Framework Written in Golang. Retrieved July 30, 2021.](https://labs.bishopfox.com/tech-blog/sliver)
- [BishopFox. (n.d.). Sliver. Retrieved September 15, 2021.](https://github.com/BishopFox/sliver/)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [Baker, B., Unterbrink H. (2018, July 03). Smoking Guns - Smoke Loader learned new tricks. Retrieved July 5, 2018.](https://blog.talosintelligence.com/2018/07/smoking-guns-smoke-loader-learned-new.html#more)
- [Kaspersky Lab. (2017, March 7). From Shamoon to StoneDrill: Wipers attacking Saudi organizations and beyond. Retrieved March 14, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
- [Larson, S. and Wise, J. (2022, February 15). Charting TA2541's Flight. Retrieved September 12, 2023.](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)
- [Ventura, V. (2021, September 16). Operation Layover: How we tracked an attack on the aviation industry to five years of compromise. Retrieved September 15, 2023.](https://blog.talosintelligence.com/operation-layover-how-we-tracked-attack/)
- [Joe Security. (2020, July 13). TrickBot's new API-Hammering explained. Retrieved September 30, 2021.](https://www.joesecurity.org/blog/498839998833561473)
- [Tomonaga, S.. (2019, September 18). Malware Used by BlackTech after Network Intrusion. Retrieved May 6, 2020.](https://blogs.jpcert.or.jp/en/2019/09/tscookie-loader.html)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [Sygnia Team. (2024, June 3). China-Nexus Threat Group ‘Velvet Ant’ Abuses F5 Load Balancers for Persistence. Retrieved March 14, 2025.](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [Su, V. et al. (2019, December 11). Waterbear Returns, Uses API Hooking to Evade Security. Retrieved February 22, 2021.](https://www.trendmicro.com/en_us/research/19/l/waterbear-is-back-uses-api-hooking-to-evade-security-product-detection.html)
- [Zhou, R. (2012, May 15). Backdoor.Wiarp. Retrieved February 22, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051606-1005-99)
- [Anthe, C. et al. (2016, December 14). Microsoft Security Intelligence Report Volume 21. Retrieved November 27, 2017.](http://download.microsoft.com/download/E/B/0/EB0F50CC-989C-4B66-B7F6-68CD3DC90DE3/Microsoft_Security_Intelligence_Report_Volume_21_English.pdf)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Microsoft. (2021, July 2). Use attack surface reduction rules to prevent malware infection. Retrieved June 24, 2021.](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)

---

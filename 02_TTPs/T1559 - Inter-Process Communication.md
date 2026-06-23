# Inter-Process Communication

## Description

Adversaries may abuse inter-process communication (IPC) mechanisms for local code or command execution. IPC is typically used by processes to share data, communicate with each other, or synchronize execution. IPC is also commonly used to avoid situations such as deadlocks, which occurs when processes are stuck in a cyclic waiting pattern.

Adversaries may abuse IPC to execute arbitrary code or commands. IPC mechanisms may differ depending on OS, but typically exists in a form accessible through programming languages/libraries or native interfaces such as Windows Dynamic Data Exchange or Component Object Model . Linux environments support several different IPC mechanisms, two of which being sockets and pipes. [1] Higher level execution mediums, such as those of Command and Scripting Interpreter s, may also leverage underlying IPC mechanisms. Adversaries may also use Remote Services such as Distributed Component Object Model to facilitate remote IPC execution. [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0057 | 3CX Supply Chain Attack | During the 3CX Supply Chain Attack , AppleJeus 's VEILEDSIGNAL creates and listens on a Windows named pipe to exchange messages between modules. [3] |
| S0687 | Cyclops Blink | Cyclops Blink has the ability to create a pipe to enable inter-process communication. [4] |
| S1229 | Havoc | The Havoc SMB demon can use named pipes for communication through a parent demon. [5] |
| S0537 | HyperStack | HyperStack can connect to the IPC$ share on remote machines. [6] |
| S1141 | LunarWeb | LunarWeb can retrieve output from arbitrary processes and shell commands via a pipe. [7] |
| S1244 | Medusa Ransomware | Medusa Ransomware has leveraged the CreatePipe API to enable inter-process communication. [8] |
| S1100 | Ninja | Ninja can use pipes to redirect the standard input and the standard output. [9] |
| S1172 | OilBooster | OilBooster can read the results of command line execution via an unnamed pipe connected to the process. [10] |
| C0048 | Operation MidnightEclipse | During Operation MidnightEclipse , threat actors wrote output to stdout then piped it to bash for execution. [11] |
| S1123 | PITSTOP | PITSTOP can listen over the Unix domain socket located at /data/runtime/cockpit/wd.fd . [12] |
| S1130 | Raspberry Robin | Raspberry Robin contains an embedded custom Tor network client that communicates with the primary payload via shared process memory. [13] |
| S1150 | ROADSWEEP | ROADSWEEP can pipe command output to a targeted process. [14] |
| S1078 | RotaJakiro | When executing with non-root permissions, RotaJakiro uses the the shmget API to create shared memory between other known RotaJakiro processes. This allows processes to communicate with each other and share their PID. [15] |
| S9024 | SPAWNCHIMERA | SPAWNCHIMERA has leveraged IPC using a UNIX domain socket between the dsmdm process and the web process. [16] [17] |
| S1200 | StealBit | StealBit can use interprocess communication (IPC) to enable the designation of multiple files for exfiltration in a scalable manner. [18] |
| S1239 | TONESHELL | TONESHELL has facilitated inter-process communication between DLL components via the use of pipes. [19] TONESHELL has also created a reverse shell using two anonymous pipes to write data to stdin and read data from stdout and stderr. [20] |
| S0022 | Uroburos | Uroburos has the ability to move data between its kernel and user mode components, generally using named pipes. [21] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1013 | Application Developer Guidance | Enable the Hardened Runtime capability when developing applications. Do not include the com.apple.security.get-task-allow entitlement with the value set to any variation of true. |
| M1048 | Application Isolation and Sandboxing | Ensure all COM alerts and Protected View are enabled. [22] |
| M1040 | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent DDE attacks and spawning of child processes from Office programs. [23] [24] |
| M1042 | Disable or Remove Feature or Program | Registry keys specific to Microsoft Office feature control security can be set to disable automatic DDE/OLE execution. [25] [26] [27] Microsoft also created, and enabled by default, Registry keys to completely disable DDE execution in Word and Excel. [28] |
| M1026 | Privileged Account Management | Modify Registry settings (directly or using Dcomcnfg.exe) in HKEY_LOCAL_MACHINE\\SOFTWARE\\Classes\\AppID\\{AppID_GUID} associated with the process-wide security of individual COM applications. [29] Modify Registry settings (directly or using Dcomcnfg.exe) in HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Ole associated with system-wide security defaults for all COM applications that do no set their own process-wide security. [30] [31] |
| M1054 | Software Configuration | Consider disabling embedded files in Office programs, such as OneNote, that do not work with Protected View. [24] [27] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0493 | Detect Abuse of Inter-Process Communication (T1559) | AN1357 | Detects anomalous use of COM, DDE, or named pipes for execution. Correlates creation or access of IPC mechanisms (e.g., named pipes, COM objects) with unusual parent-child process relationships or code injection patterns (e.g., Office spawning cmd.exe via DDE). |
| AN1358 | Detects abuse of UNIX domain sockets, pipes, or message queues for unauthorized code execution. Correlates unexpected socket creation with suspicious binaries, abnormal shell pipelines, or injected processes establishing IPC channels. |  |  |
| AN1359 | Detects anomalous use of Mach ports, Apple Events, or XPC services for inter-process execution or code injection. Focuses on unexpected processes attempting to send privileged Apple Events (e.g., automation scripts injecting into security-sensitive apps). |  |  |

---

## References

- [N/A. (2021, April 1). Inter Process Communication (IPC). Retrieved March 11, 2022.](https://www.geeksforgeeks.org/inter-process-communication-ipc/#:~:text=Inter%2Dprocess%20communication%20(IPC),of%20co%2Doperation%20between%20them.)
- [Hamilton, C. (2019, June 4). Hunting COM Objects. Retrieved June 10, 2019.](https://www.fireeye.com/blog/threat-research/2019/06/hunting-com-objects.html)
- [Jeff Johnson, Fred Plan, Adrian Sanchez, Renato Fontana, Jake Nicastro, Dimiter Andonov, Marius Fodoreanu, Daniel Scott. (2023, April 20). 3CX Software Supply Chain Compromise Initiated by a Prior Software Supply Chain Compromise; Suspected North Korean Actor Responsible. Retrieved August 25, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise/)
- [Haquebord, F. et al. (2022, March 17). Cyclops Blink Sets Sights on Asus Routers. Retrieved March 17, 2022.](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)
- [Ungur, P. (n.d.). HAVOC. Retrieved August 4, 2025.](https://havocframework.com/docs/welcome)
- [Accenture. (2020, October). Turla uses HyperStack, Carbon, and Kazuar to compromise government entity. Retrieved December 2, 2020.](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Hromcova, Z. and Burgher, A. (2023, December 14). OilRig’s persistent attacks using cloud service-powered downloaders. Retrieved November 26, 2024.](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
- [Volexity Threat Research. (2024, April 12). Zero-Day Exploitation of Unauthenticated Remote Code Execution Vulnerability in GlobalProtect (CVE-2024-3400). Retrieved November 20, 2024.](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)
- [Lin, M. et al. (2024, February 27). Cutting Edge, Part 3: Investigating Ivanti Connect Secure VPN Exploitation and Persistence Attempts. Retrieved March 1, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
- [Christopher So. (2022, December 20). Raspberry Robin Malware Targets Telecom, Governments. Retrieved May 17, 2024.](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [Alex Turing, Hui Wang. (2021, April 28). RotaJakiro: A long live secret backdoor with 0 VT detection. Retrieved June 14, 2023.](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
- [Matt Lin, Austin Larsen, John Wolfram, Ashley Pearson, Josh Murchie, Lukasz Lamparski, Joseph Pisano, Ryan Hall, Ron Craft, Shawn Crew, Billy Wong, Tyler McLellan. (2024, April 4). Cutting Edge, Part 4: Ivanti Connect Secure VPN Post-Exploitation Lateral Movement Case Studies. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
- [Yuma Masubuchi. (2025, February 20). SPAWNCHIMERA Malware: The Chimera Spawning from Ivanti Connect Secure Vulnerability. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2025/02/spawnchimera.html)
- [Cybereason Global SOC Team. (n.d.). THREAT ANALYSIS REPORT: Inside the LockBit Arsenal - The StealBit Exfiltration Tool. Retrieved January 29, 2025.](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
- [Lior Rochberger, Tom Fakterman, Robert Falcone. (2023, September 22). Cyberespionage Attacks Against Southeast Asian Government Linked to Stately Taurus, Aka Mustang Panda. Retrieved September 9, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Microsoft. (n.d.). What is Protected View?. Retrieved November 22, 2017.](https://support.office.com/en-us/article/What-is-Protected-View-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653)
- [Brower, N. & D'Souza-Wiltshire, I. (2017, November 9). Enable Attack surface reduction. Retrieved February 3, 2018.](https://docs.microsoft.com/windows/threat-protection/windows-defender-exploit-guard/enable-attack-surface-reduction)
- [Nelson, M. (2018, January 29). Reviving DDE: Using OneNote and Excel for Code Execution. Retrieved February 3, 2018.](https://posts.specterops.io/reviving-dde-using-onenote-and-excel-for-code-execution-d7226864caee)
- [Microsoft. (2017, November 8). Microsoft Security Advisory 4053440 - Securely opening Microsoft Office documents that contain Dynamic Data Exchange (DDE) fields. Retrieved November 21, 2017.](https://technet.microsoft.com/library/security/4053440)
- [Cimpanu, C. (2017, December 15). Microsoft Disables DDE Feature in Word to Prevent Further Malware Attacks. Retrieved December 19, 2017.](https://www.bleepingcomputer.com/news/microsoft/microsoft-disables-dde-feature-in-word-to-prevent-further-malware-attacks/)
- [Dormann, W. (2017, October 20). Disable DDEAUTO for Outlook, Word, OneNote, and Excel versions 2010, 2013, 2016. Retrieved February 3, 2018.](https://gist.github.com/wdormann/732bb88d9b5dd5a66c9f1e1498f31a1b)
- [Microsoft. (2017, December 12). ADV170021 - Microsoft Office Defense in Depth Update. Retrieved February 3, 2018.](https://portal.msrc.microsoft.com/security-guidance/advisory/ADV170021)
- [Microsoft. (n.d.). Setting Process-Wide Security Through the Registry. Retrieved November 21, 2017.](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687317(v=vs.85).aspx)
- [Microsoft. (n.d.). Registry Values for System-Wide Security. Retrieved November 21, 2017.](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694331(v=vs.85).aspx)
- [Microsoft. (n.d.). DCOM Security Enhancements in Windows XP Service Pack 2 and Windows Server 2003 Service Pack 1. Retrieved November 22, 2017.](https://docs.microsoft.com/en-us/windows/desktop/com/dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1)

---

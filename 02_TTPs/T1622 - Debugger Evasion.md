# Debugger Evasion

## Description

Adversaries may employ various means to detect and avoid debuggers. Debuggers are typically used by defenders to trace and/or analyze the execution of potential malware payloads. [1]

Debugger evasion may include changing behaviors based on the results of the checks for the presence of artifacts indicative of a debugged environment. Similar to Virtualization/Sandbox Evasion , if the adversary detects a debugger, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for debugger artifacts before dropping secondary or additional payloads.

Specific checks will vary based on the target and/or adversary. On Windows, this may involve Native API function calls such as IsDebuggerPresent() and NtQueryInformationProcess() , or manually checking the BeingDebugged flag of the Process Environment Block (PEB). On Linux, this may involve querying /proc/self/status for the TracerPID field, which indicates whether or not the process is being traced by dynamic analysis tools. [2] [3] Other checks for debugging artifacts may also seek to enumerate hardware breakpoints, interrupt assembly opcodes, time checks, or measurements if exceptions are raised in the current process (assuming a present debugger would "swallow" or handle the potential error). [4] [5] [6]

Malware may also leverage Structured Exception Handling (SEH) to detect debuggers by throwing an exception and detecting whether the process is suspended. SEH handles both hardware and software expectations, providing control over the exceptions including support for debugging. If a debugger is present, the program’s control will be transferred to the debugger, and the execution of the code will be suspended. If the debugger is not present, control will be transferred to the SEH handler, which will automatically handle the exception and allow the program’s execution to continue. [7]

Adversaries may use the information learned from these debugger checks during automated discovery to shape follow-on behaviors. Debuggers can also be evaded by detaching the process or flooding debug logs with meaningless data via messages produced by looping Native API function calls such as OutputDebugStringW() . [8] [9]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S9027 | ANELLDR | ANELLDR can call ZwSetInformationThread with the second argument set to ThreadHideFromDebugger (0x11) to evade being debugged. [10] |
| S1087 | AsyncRAT | AsyncRAT can use the CheckRemoteDebuggerPresent function to detect the presence of a debugger. [11] |
| S1070 | Black Basta | The Black Basta dropper can check system flags, CPU registers, CPU instructions, process timing, system libraries, and APIs to determine if a debugger is present. [12] |
| S1039 | Bumblebee | Bumblebee can search for tools used in static analysis. [13] |
| S1111 | DarkGate | DarkGate checks the BeingDebugged flag in the PEB structure during execution to identify if the malware is being debugged. [14] |
| S1066 | DarkTortilla | DarkTortilla can detect debuggers by using functions such as DebuggerIsAttached and DebuggerIsLogging . DarkTortilla can also detect profilers by verifying the COR_ENABLE_PROFILING environment variable is present and active. [15] |
| S0694 | DRATzarus | DRATzarus can use IsDebuggerPresent to detect whether a debugger is present on a victim. [16] |
| S1160 | Latrodectus | Latrodectus has the ability to check for the presence of debuggers. [17] |
| S1202 | LockBit 3.0 | LockBit 3.0 can check heap memory parameters for indications of a debugger and stop the flow of events to the attached debugger in order to hinder dynamic analysis. [18] |
| S1213 | Lumma Stealer | Lumma Stealer has checked for debugger strings by invoking GetForegroundWindow and looks for strings containing "x32dbg", "x64dbg", "windbg", "ollydbg", "dnspy", "immunity debugger", "hyperdbg", "debug", "debugger", "cheat engine", "cheatengine" and "ida". [19] |
| S1060 | Mafalda | Mafalda can search for debugging tools on a compromised host. [20] |
| G0129 | Mustang Panda | Mustang Panda has embedded debug strings with messages to distract analysts. [21] Mustang Panda has also made calls to Windows API CheckRemoteDebuggerPresent and exits if it detects a debugger. [22] |
| C0022 | Operation Dream Job | During Operation Dream Job , Lazarus Group used tools that used the IsDebuggerPresent call to detect debuggers. [16] |
| S1145 | Pikabot | Pikabot features several methods to evade debugging by analysts, including checks for active debuggers, the use of breakpoints during execution, and checking various system information items such as system memory and the number of processors. [23] [24] [25] |
| S0013 | PlugX | PlugX has made calls to Windows API CheckRemoteDebuggerPresent and exits if it detects a debugger. [22] |
| S1228 | PUBLOAD | PUBLOAD has embedded debug strings with messages to distract analysts. [26] [21] PUBLOAD has leveraged OutputDebugStringW and OutputDebugStringA functions. [21] |
| S9019 | PureCrypter | PureCrypter has the ability to call CheckRemoteDebuggerPresent . [27] |
| S1130 | Raspberry Robin | Raspberry Robin leverages anti-debugging mechanisms through the use of ThreadHideFromDebugger . [28] |
| S0240 | ROKRAT | ROKRAT can check for debugging tools. [29] [30] [31] |
| S9037 | RustyWater | RustyWater has registered a Vectored Exception Handler (VEH) to catch debugging efforts. [32] |
| S1018 | Saint Bot | Saint Bot has used is_debugger_present as part of its environmental checks. [33] |
| S1200 | StealBit | StealBit can detect it is being run in the context of a debugger. [34] |
| S1183 | StrelaStealer | StrelaStealer variants include functionality to identify and evade debuggers. [35] |
| S0595 | ThiefQuest | ThiefQuest uses a function named is_debugging to perform anti-debugging logic. The function invokes sysctl checking the returned value of P_TRACED . ThiefQuest also calls ptrace with the PTRACE_DENY_ATTACH flag to prevent debugging. [8] |
| S1239 | TONESHELL | TONESHELL has leveraged custom exception handlers to hide code flow and stop execution of a debugger. [21] |
| S1207 | XLoader | XLoader uses anti-debugging mechanisms such as calling NtQueryInformationProcess with InfoClass=7 , referencing ProcessDebugPort , to determine if it is being analyzed. [36] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0371 | Detection Strategy for Debugger Evasion (T1622) | AN1045 | Monitor for suspicious use of Windows API calls such as IsDebuggerPresent() and NtQueryInformationProcess(), or processes manually checking the BeingDebugged flag in the Process Environment Block (PEB). Detect sequences of OutputDebugStringW() calls in short intervals that may indicate debugger flooding attempts. |
| AN1046 | Monitor access to /proc/self/status where TracerPID field is queried, as this is a common technique for debugger detection. Detect processes that attempt to trigger exceptions intentionally and monitor whether exception handling indicates presence of a debugger. |  |  |
| AN1047 | Detect suspicious calls to sysctl or ptrace API used to determine if a process is being debugged. Monitor for processes that flood OutputDebugString equivalents or generate abnormal exceptions to evade analysis. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0371 | Detection Strategy for Debugger Evasion (T1622) | AN1045 | Monitor for suspicious use of Windows API calls such as IsDebuggerPresent() and NtQueryInformationProcess(), or processes manually checking the BeingDebugged flag in the Process Environment Block (PEB). Detect sequences of OutputDebugStringW() calls in short intervals that may indicate debugger flooding attempts. |
| AN1046 | Monitor access to /proc/self/status where TracerPID field is queried, as this is a common technique for debugger detection. Detect processes that attempt to trigger exceptions intentionally and monitor whether exception handling indicates presence of a debugger. |  |  |
| AN1047 | Detect suspicious calls to sysctl or ptrace API used to determine if a process is being debugged. Monitor for processes that flood OutputDebugString equivalents or generate abnormal exceptions to evade analysis. |  |  |

---

## References

- [ProcessHacker. (2009, October 27). Process Hacker. Retrieved April 11, 2022.](https://github.com/processhacker/processhacker)
- [jbowen. (2023, December 4). P2Pinfect - New Variant Targets MIPS Devices. Retrieved March 18, 2025.](https://www.cadosecurity.com/blog/p2pinfect-new-variant-targets-mips-devices)
- [PT Expert Security Center. (2023, November 29). Hellhounds: operation Lahat. Retrieved March 18, 2025.](https://global.ptsecurity.com/analytics/pt-esc-threat-intelligence/hellhounds-operation-lahat)
- [hasherezade. (2021, June 30). Module 3 - Understanding and countering malware's evasion and self-defence. Retrieved April 1, 2022.](https://github.com/hasherezade/malware_training_vol1/blob/main/slides/module3/Module3_2_fingerprinting.pdf)
- [Noteworthy. (2019, January 6). Al-Khaser. Retrieved April 1, 2022.](https://github.com/LordNoteworthy/al-khaser/tree/master/al-khaser/AntiDebug)
- [vxunderground. (2021, June 30). VX-API. Retrieved April 1, 2022.](https://web.archive.org/web/20250904153443/https://github.com/vxunderground/VX-API/tree/main#anti-debug)
- [Apriorit. (2024, June 4). Anti Debugging Protection Techniques with Examples. Retrieved March 4, 2025.](https://www.apriorit.com/dev-blog/367-anti-reverse-engineering-protection-techniques-to-use-before-releasing-software)
- [Patrick Wardle. (2020, July 3). OSX.EvilQuest Uncovered part ii: insidious capabilities. Retrieved March 21, 2021.](https://objective-see.com/blog/blog_0x60.html)
- [Check Point Research. (2021, January 4). Stopping Serial Killer: Catching the Next Strike. Retrieved September 7, 2021.](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)
- [Hiroaki, H. (2024, November 26). Guess Who’s Back - The Return of ANEL in the Recent Earth Kasha Spear-phishing Campaign in 2024. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
- [Jornet, A. (2021, December 23). Snip3, an investigation into malware. Retrieved September 19, 2023.](https://telefonicatech.com/blog/snip3-investigacion-malware)
- [Check Point. (2022, October 20). BLACK BASTA AND THE UNNOTICED DELIVERY. Retrieved March 8, 2023.](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
- [Salem, A. (2022, April 27). The chronicles of Bumblebee: The Hook, the Bee, and the Trickbot connection. Retrieved September 2, 2022.](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
- [Ernesto Fernández Provecho, Pham Duy Phuc, Ciana Driscoll & Vinoo Thomas. (2023, November 21). The Continued Evolution of the DarkGate Malware-as-a-Service. Retrieved February 9, 2024.](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [Proofpoint Threat Research and Team Cymru S2 Threat Research. (2024, April 4). Latrodectus: This Spider Bytes Like Ice . Retrieved May 31, 2024.](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
- [Walter, J. (2022, July 21). LockBit 3.0 Update | Unpicking the Ransomware’s Latest Anti-Analysis and Evasion Techniques. Retrieved February 5, 2025.](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
- [Cara Lin, Fortinet. (2024, January 8). Deceptive Cracked Software Spreads Lumma Variant on YouTube. Retrieved March 22, 2025.](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [Nick Dai, Vickie Su, Sunny Lu. (2022, November 18). Earth Preta Spear-Phishing Governments Worldwide. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
- [Secureworks Counter Threat Unit Research Team. (2022, September 8). BRONZE PRESIDENT Targets Government Officials. Retrieved September 9, 2025.](https://www.secureworks.com/blog/bronze-president-targets-government-officials)
- [Brett Stone-Gross & Nikolaos Pantazopoulos. (2023, May 24). Technical Analysis of Pikabot. Retrieved July 12, 2024.](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)
- [Daniel Stepanic & Salim Bitam. (2024, February 23). PIKABOT, I choose you!. Retrieved July 12, 2024.](https://www.elastic.co/security-labs/pikabot-i-choose-you)
- [Swachchhanda Shrawan Poudel. (2024, February). Pikabot: A Sophisticated and Modular Backdoor Trojan with Advanced Evasion Techniques. Retrieved July 12, 2024.](https://www.logpoint.com/wp-content/uploads/2024/02/logpoint-etpr-pikabot.pdf)
- [Asheer Malhotra, Jungsoo An, Kendall Mc. (2022, May 5). Mustang Panda deploys a new wave of malware targeting Europe. Retrieved August 4, 2025.](https://blog.talosintelligence.com/mustang-panda-targets-europe/)
- [Dumont, R. (2022, June 13). Technical Analysis of PureCrypter: A Fully-Functional Loader Distributing Remote Access Trojans and Information Stealers. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
- [Christopher So. (2022, December 20). Raspberry Robin Malware Targets Telecom, Governments. Retrieved May 17, 2024.](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
- [Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)
- [Pantazopoulos, N.. (2018, November 8). RokRat Analysis. Retrieved May 21, 2020.](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
- [Jazi, Hossein. (2021, January 6). Retrohunting APT37: North Korean APT used VBA self decode technique to inject RokRat. Retrieved March 22, 2022.](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
- [Awasthi, P. (2026, January 8). Reborn in Rust: Muddy Water Evolves Tooling with RustyWater Implant. Retrieved March 19, 2026.](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
- [Hasherezade. (2021, April 6). A deep dive into Saint Bot, a new downloader. Retrieved June 9, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
- [Cybereason Global SOC Team. (n.d.). THREAT ANALYSIS REPORT: Inside the LockBit Arsenal - The StealBit Exfiltration Tool. Retrieved January 29, 2025.](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
- [Fortgale. (2023, September 18). StrelaStealer Malware Analysis. Retrieved December 31, 2024.](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)
- [Nart Villeneuve, Randi Eitzman, Sandor Nemes & Tyler Dean, Google Cloud. (2017, October 5). Significant FormBook Distribution Campaigns Impacting the U.S. and South Korea. Retrieved March 11, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)

---

# Virtualization/Sandbox Evasion

## Description

Adversaries may employ various means to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from Virtualization/Sandbox Evasion during automated discovery to shape follow-on behaviors. [1]

Adversaries may use several methods to accomplish Virtualization/Sandbox Evasion such as checking for security monitoring tools (e.g., Sysinternals, Wireshark, etc.) or other system artifacts associated with analysis or virtualization. Adversaries may also check for legitimate user activity to help determine if it is in an analysis environment. Additional methods include use of sleep timers or loops within malware code to avoid operating within a temporary sandbox. [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0331 | Agent Tesla | Agent Tesla has the ability to perform anti-sandboxing and anti-virtualization checks. [3] |
| S0534 | Bazar | Bazar can attempt to overload sandbox analysis by sending 1550 calls to printf . [4] |
| S0268 | Bisonal | Bisonal can check to determine if the compromised system is running on VMware. [5] |
| S1070 | Black Basta | Black Basta can make a random number of calls to the kernel32.beep function to hinder log analysis. [6] |
| S1039 | Bumblebee | Bumblebee has the ability to perform anti-virtualization checks. [7] |
| S0484 | Carberp | Carberp has removed various hooks before installing the trojan or bootkit to evade sandbox analysis or other analysis software. [8] |
| S0023 | CHOPSTICK | CHOPSTICK includes runtime checks to identify an analysis environment and prevent execution on it. [9] |
| G1052 | Contagious Interview | Contagious Interview has requested victims to disable Docker and other container environments in attempts to thwart container isolation and ensure device infection. [10] |
| S0046 | CozyCar | Some versions of CozyCar will check to ensure it is not being executed inside a virtual machine or a known malware analysis sandbox environment. If it detects that it is, it will exit. [11] |
| G0012 | Darkhotel | Darkhotel malware has employed just-in-time decryption of strings to evade sandbox detection. [12] |
| S0554 | Egregor | Egregor has used multiple anti-analysis and anti-sandbox techniques to prevent automated analysis by sandboxes. [13] [14] |
| S0666 | Gelsemium | Gelsemium can use junk code to generate random activity to obscure malware behavior. [15] |
| S0499 | Hancitor | Hancitor has used a macro to check that an ActiveDocument shape object in the lure message is present. If this object is not found, the macro will exit without downloading additional payloads. [16] |
| S0483 | IcedID | IcedID has manipulated Keitaro Traffic Direction System to filter researcher and sandbox traffic. [17] |
| S1020 | Kevin | Kevin can sleep for a time interval between C2 communication attempts. [18] |
| S0455 | Metamorfo | Metamorfo has embedded a "vmdetect.exe" executable to identify virtual machines at the beginning of execution. [19] |
| C0005 | Operation Spalax | During Operation Spalax , the threat actors used droppers that would run anti-analysis checks before executing malware on a compromised host. [20] |
| S0147 | Pteranodon | Pteranodon has the ability to use anti-detection functions to identify sandbox environments. [21] |
| S1130 | Raspberry Robin | Raspberry Robin contains real and fake second-stage payloads following initial execution, with the real payload only delivered if the malware determines it is not running in a virtualized environment. [22] |
| S1240 | RedLine Stealer | RedLine Stealer has an anti-sandbox technique that requires the malware to consistently check with the C2 server, if the communication fails RedLine Stealer will not continue execution. [23] |
| S0148 | RTM | RTM can detect if it is running within a sandbox or other virtualized analysis environment. [24] |
| G1031 | Saint Bear | Saint Bear contains several anti-analysis and anti-virtualization checks. [25] |
| S1030 | Squirrelwaffle | Squirrelwaffle has contained a hardcoded list of IP addresses to block that belong to sandboxes and analysis platforms. [26] [27] |
| S0380 | StoneDrill | StoneDrill has used several anti-emulation techniques to prevent automated analysis by emulators or sandboxes. [28] |
| S1183 | StrelaStealer | StrelaStealer payloads have used control flow obfuscation techniques such as excessively long code blocks of mathematical instructions to defeat sandboxing and related analysis methods. [29] [30] |
| S1207 | XLoader | XLoader can utilize decoy command and control domains within the malware configuration to circumvent sandbox analysis. [31] [32] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0046 | Detection Strategy for T1497 Virtualization/Sandbox Evasion | AN0127 | Execution of discovery commands or API calls for virtualization artifacts (e.g., registry keys, device drivers, services), sleep/skipped execution behavior, or sandbox evasion DLLs before payload deployment. |
| AN0128 | Execution of commands to enumerate virtualization-related files or processes (e.g., '/sys/class/dmi/id/product_name', dmesg, lscpu, lspci), or querying hypervisor interfaces prior to malware execution. |  |  |
| AN0129 | Execution of scripts or binaries that check for virtualization indicators (e.g., system_profiler, ioreg -l, kextstat), combined with delay functions or anomalous launchd activity. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0046 | Detection Strategy for T1497 Virtualization/Sandbox Evasion | AN0127 | Execution of discovery commands or API calls for virtualization artifacts (e.g., registry keys, device drivers, services), sleep/skipped execution behavior, or sandbox evasion DLLs before payload deployment. |
| AN0128 | Execution of commands to enumerate virtualization-related files or processes (e.g., '/sys/class/dmi/id/product_name', dmesg, lscpu, lspci), or querying hypervisor interfaces prior to malware execution. |  |  |
| AN0129 | Execution of scripts or binaries that check for virtualization indicators (e.g., system_profiler, ioreg -l, kextstat), combined with delay functions or anomalous launchd activity. |  |  |

---

## References

- [Torello, A. & Guibernau, F. (n.d.). Environment Awareness. Retrieved September 13, 2024.](https://drive.google.com/file/d/1t0jn3xr4ff2fR30oQAUn_RsWSnMpOAQc/edit)
- [Falcone, R., Wartell, R.. (2015, July 27). UPS: Observations on CVE-2015-3113, Prior Zero-Days and the Pirpi Payload. Retrieved April 23, 2019.](https://unit42.paloaltonetworks.com/ups-observations-on-cve-2015-3113-prior-zero-days-and-the-pirpi-payload/)
- [Jazi, H. (2020, April 16). New AgentTesla variant steals WiFi credentials. Retrieved May 19, 2020.](https://blog.malwarebytes.com/threat-analysis/2020/04/new-agenttesla-variant-steals-wifi-credentials/)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [Check Point. (2022, October 20). BLACK BASTA AND THE UNNOTICED DELIVERY. Retrieved March 8, 2023.](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
- [Merriman, K. and Trouerbach, P. (2022, April 28). This isn't Optimus Prime's Bumblebee but it's Still Transforming. Retrieved August 22, 2022.](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
- [Matrosov, A., Rodionov, E., Volkov, D., Harley, D. (2012, March 2). Win32/Carberp When You’re in a Black Hole, Stop Digging. Retrieved July 15, 2020.](https://www.eset.com/fileadmin/eset/US/resources/docs/white-papers/white-papers-win-32-carberp.pdf)
- [FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [F-Secure Labs. (2015, April 22). CozyDuke: Malware Analysis. Retrieved December 10, 2015.](https://www.f-secure.com/documents/996508/1030745/CozyDuke)
- [Arunpreet Singh, Clemens Kolbitsch. (2015, November 5). Defeating Darkhotel Just-In-Time Decryption. Retrieved April 15, 2021.](https://www.lastline.com/labsblog/defeating-darkhotel-just-in-time-decryption/)
- [Cybleinc. (2020, October 31). Egregor Ransomware – A Deep Dive Into Its Activities and Techniques. Retrieved December 29, 2020.](https://cybleinc.com/2020/10/31/egregor-ransomware-a-deep-dive-into-its-activities-and-techniques/)
- [NHS Digital. (2020, November 26). Egregor Ransomware The RaaS successor to Maze. Retrieved December 29, 2020.](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Anubhav, A., Jallepalli, D. (2016, September 23). Hancitor (AKA Chanitor) observed using multiple attack approaches. Retrieved August 13, 2020.](https://www.fireeye.com/blog/threat-research/2016/09/hancitor_aka_chanit.html)
- [Kenefick , I. (2022, December 23). IcedID Botnet Distributors Abuse Google PPC to Distribute Malware. Retrieved July 24, 2024.](https://www.trendmicro.com/en_us/research/22/l/icedid-botnet-distributors-abuse-google-ppc-to-distribute-malware.html)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Erlich, C. (2020, April 3). The Avast Abuser: Metamorfo Banking Malware Hides By Abusing Avast Executable. Retrieved May 26, 2020.](https://medium.com/@chenerlich/the-avast-abuser-metamorfo-banking-malware-hides-by-abusing-avast-executable-ac9b8b392767)
- [M. Porolli. (2021, January 21). Operation Spalax: Targeted malware attacks in Colombia. Retrieved September 16, 2022.](https://www.welivesecurity.com/2021/01/12/operation-spalax-targeted-malware-attacks-colombia/)
- [Unit 42. (2022, February 3). Russia’s Gamaredon aka Primitive Bear APT Group Actively Targeting Ukraine. Retrieved February 21, 2022.](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)
- [Christopher So. (2022, December 20). Raspberry Robin Malware Targets Telecom, Governments. Retrieved May 17, 2024.](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
- [Splunk Threat Research Team. (2023, June 1). Do Not Cross The 'RedLine' Stealer: Detections and Analysis. Retrieved September 17, 2025.](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
- [Duncan, B., Harbison, M. (2019, January 23). Russian Language Malspam Pushing Redaman Banking Malware. Retrieved June 16, 2020.](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Kumar, A., Stone-Gross, Brett. (2021, September 28). Squirrelwaffle: New Loader Delivering Cobalt Strike. Retrieved August 9, 2022.](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
- [Palazolo, G. (2021, October 7). SquirrelWaffle: New Malware Loader Delivering Cobalt Strike and QakBot. Retrieved August 9, 2022.](https://www.netskope.com/blog/squirrelwaffle-new-malware-loader-delivering-cobalt-strike-and-qakbot)
- [Kaspersky Lab. (2017, March 7). From Shamoon to StoneDrill: Wipers attacking Saudi organizations and beyond. Retrieved March 14, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
- [Benjamin Chang, Goutam Tripathy, Pranay Kumar Chhaparwal, Anmol Maurya & Vishwa Thothathri, Palo Alto Networks. (2024, March 22). Large-Scale StrelaStealer Campaign in Early 2024. Retrieved December 31, 2024.](https://unit42.paloaltonetworks.com/strelastealer-campaign/)
- [Fortgale. (2023, September 18). StrelaStealer Malware Analysis. Retrieved December 31, 2024.](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)
- [ANY.RUN. (2023, February 28). XLoader/FormBook: Encryption Analysis and Malware Decryption . Retrieved March 11, 2025.](https://any.run/cybersecurity-blog/xloader-formbook-encryption-analysis-and-malware-decryption/)
- [Alexey Bukhteyev & Raman Ladutska, Check Point Research. (2022, May 31). XLoader Botnet: Find Me If You Can. Retrieved March 11, 2025.](https://research.checkpoint.com/2022/xloader-botnet-find-me-if-you-can/)

---

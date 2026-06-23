# Event Triggered Execution

## Description

Adversaries may establish persistence and/or elevate privileges using system mechanisms that trigger execution based on specific events. Various operating systems have means to monitor and subscribe to events such as logons or other user activity such as running specific applications/binaries. Cloud environments may also support various functions and services that monitor and can be invoked in response to specific cloud events. [1] [2] [3]

Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via repeatedly executing malicious code. After gaining access to a victim system, adversaries may create/modify event triggers to point to malicious content that will be executed whenever the event trigger is invoked. [4] [5] [6]

Since the execution can be proxied by an account with higher permissions, such as SYSTEM or service accounts, an adversary may be able to abuse these triggered execution mechanisms to escalate their privileges.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0035 | KV Botnet Activity | KV Botnet Activity involves managing events on victim systems via libevent to execute a callback function when any running process contains the following references in their path without also having a reference to bioset : busybox, wget, curl, tftp, telnetd, or lua. If the bioset string is not found, the related process is terminated. [7] |
| S1091 | Pacu | Pacu can set up S3 bucket notifications to trigger a malicious Lambda function when a CloudFormation template is uploaded to the bucket. It can also create Lambda functions that trigger upon the creation of users, roles, and groups. [8] |
| S1164 | UPSTYLE | UPSTYLE creates a .pth file beginning with the text import so that any time another process or script attempts to reference the modified item the malicious code will also run. [9] |
| S0658 | XCSSET | XCSSET 's dfhsebxzod module searches for .xcodeproj directories within the user’s home folder and subdirectories. For each match, it locates the corresponding project.pbxproj file and embeds an encoded payload into a build rule, target configuration, or project setting. The payload is later executed during the build process. [10] [11] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1026 | Privileged Account Management | Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root. |
| M1051 | Update Software | Perform regular software updates to mitigate exploitation risk. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0010 | Behavioral Detection of Event Triggered Execution Across Platforms | AN0024 | Correlates unexpected modifications to WMI event filters, scheduled task triggers, or registry autorun keys with subsequent execution of non-standard binaries by SYSTEM-level processes. |
| AN0025 | Detects inotify or auditd configuration changes that monitor system files coupled with execution of script interpreters or binaries by cron or systemd timers. |  |  |
| AN0026 | Correlates launchd plist modifications with subsequent unauthorized script execution or anomalous parent-child process trees involving user agents. |  |  |
| AN0027 | Monitors cloud function creation triggered by specific audit log events (e.g., IAM changes, object creation), followed by anomalous behavior from new service accounts. |  |  |
| AN0028 | Correlates Power Automate or similar logic app workflows triggered by SaaS file uploads or email rules with data forwarding or anomalous access patterns. |  |  |
| AN0029 | Detects macros or VBA triggers set to execute on document open or close events, often correlating with embedded payloads or C2 traffic shortly after execution. |  |  |

---

## References

- [Daniel Grzelak. (2016, July 9). Backdooring an AWS account. Retrieved May 27, 2022.](https://medium.com/daniel-grzelak/backdooring-an-aws-account-da007d36f8f9)
- [Eric Saraga. (2022, February 2). Using Power Automate for Covert Data Exfiltration in Microsoft 365. Retrieved May 27, 2022.](https://www.varonis.com/blog/power-automate-data-exfiltration)
- [Berk Veral. (2020, March 9). Real-life cybercrime stories from DART, the Microsoft Detection and Response Team. Retrieved May 27, 2022.](https://www.microsoft.com/security/blog/2020/03/09/real-life-cybercrime-stories-dart-microsoft-detection-and-response-team)
- [Ballenthin, W., et al. (2015). Windows Management Instrumentation (WMI) Offense, Defense, and Forensics. Retrieved March 30, 2016.](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)
- [Patrick Wardle. (2015). Malware Persistence on OS X Yosemite. Retrieved July 10, 2017.](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
- [Claud Xiao, Cong Zheng, Yanhui Jia. (2017, April 6). New IoT/Linux Malware Targets DVRs, Forms Botnet. Retrieved February 19, 2018.](https://researchcenter.paloaltonetworks.com/2017/04/unit42-new-iotlinux-malware-targets-dvrs-forms-botnet/)
- [Black Lotus Labs. (2023, December 13). Routers Roasting On An Open Firewall: The KV-Botnet Investigation. Retrieved June 10, 2024.](https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/)
- [Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.](https://github.com/RhinoSecurityLabs/pacu)
- [Volexity Threat Research. (2024, April 12). Zero-Day Exploitation of Unauthenticated Remote Code Execution Vulnerability in GlobalProtect (CVE-2024-3400). Retrieved November 20, 2024.](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)
- [Microsoft Threat Intelligence. (2025, March 11). New XCSSET malware adds new obfuscation, persistence techniques to infect Xcode projects. Retrieved April 2, 2025.](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)
- [Steven Du, Dechao Zhao, Luis Magisa, Ariel Neimond Lazaro. (2021, April 16). XCSSET Quickly Adapts to macOS 11 and M1-based Macs. Retrieved February 18, 2025.](https://www.trendmicro.com/en_us/research/21/d/xcsset-quickly-adapts-to-macos-11-and-m1-based-macs.html)

---

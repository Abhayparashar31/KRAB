# Create or Modify System Process

## Description

Adversaries may create or modify system-level processes to repeatedly execute malicious payloads as part of persistence. When operating systems boot up, they can start processes that perform background system functions. On Windows and Linux, these system processes are referred to as services. [1] On macOS, launchd processes known as Launch Daemon and Launch Agent are run to finish system initialization and load user specific parameters. [2]

Adversaries may install new services, daemons, or agents that can be configured to execute at startup or a repeatable interval in order to establish persistence. Similarly, adversaries may modify existing services, daemons, or agents to achieve the same effect.

Services, daemons, or agents may be created with administrator privileges but executed under root/SYSTEM privileges. Adversaries may leverage this functionality to create or modify system processes in order to escalate privileges. [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1194 | Akira _v2 | Akira _v2 can create a child process for encryption. [4] |
| S1184 | BOLDMOVE | BOLDMOVE can free all resources and terminate itself on victim machines. [5] |
| S9015 | BRICKSTORM | BRICKSTORM has created a new background session and has spawned a child process of a parent process when it determines it is not running in its intended state. [6] |
| S0401 | Exaramel for Linux | Exaramel for Linux has a hardcoded location that it uses to achieve persistence if the startup system is Upstart or System V and it is running as root. [7] |
| S1152 | IMAPLoader | IMAPLoader modifies Windows tasks on the victim machine to reference a retrieved PE file through a path modification. [8] |
| S1121 | LITTLELAMB.WOOLTEA | LITTLELAMB.WOOLTEA can initialize itself as a daemon to run persistently in the background. [9] |
| S1142 | LunarMail | LunarMail can create an arbitrary process with a specified command line and redirect its output to a staging directory. [10] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Use auditing tools capable of detecting privilege and service abuse opportunities on systems within an enterprise and correct them. |
| M1040 | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent an application from writing a signed vulnerable driver to the system. [11] On Windows 10 and 11, enable Microsoft Vulnerable Driver Blocklist to assist in hardening against third party-developed drivers. [12] |
| M1045 | Code Signing | Enforce registration and execution of only legitimately signed service drivers where possible. |
| M1033 | Limit Software Installation | Restrict software installation to trusted repositories only and be cautious of orphaned software packages. |
| M1028 | Operating System Configuration | Ensure that Driver Signature Enforcement is enabled to restrict unsigned drivers from being installed. |
| M1026 | Privileged Account Management | Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root. |
| M1022 | Restrict File and Directory Permissions | Restrict read/write access to system-level process files to only select privileged users who have a legitimate need to manage system services. |
| M1054 | Software Configuration | Where possible, consider enforcing the use of container services in rootless mode to limit the possibility of privilege escalation or malicious effects on the host running the container. |
| M1018 | User Account Management | Limit privileges of user accounts and groups so that only authorized administrators can interact with system-level process changes and service configurations. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0571 | Detection of System Process Creation or Modification Across Platforms | AN1575 | Detects command-line or API-based creation/modification of Windows Services via sc.exe , powershell.exe , services.exe , or ChangeServiceConfig . Looks for creation/modification of autostart services via registry changes, file drops to System32\services , and anomalous parent-child process trees. |
| AN1576 | Detects creation or modification of systemd service units, addition of cron jobs that invoke binaries on boot, or suspicious writes to /etc/init.d/ . Monitors chmod +x and systemctl execution paths, especially from non-root parent processes. |  |  |
| AN1577 | Detects creation or modification of LaunchDaemon or LaunchAgent plist files under /Library/LaunchDaemons/ , ~/Library/LaunchAgents/ , or similar. Monitors execution of launchctl , property list edits, and file permission changes. |  |  |
| AN1578 | Detects creation of new container system processes via docker run --restart , kubectl exec to init containers, or modification of container init specs. Flags container images that override entrypoints to embed persistence behaviors. |  |  |

---

## References

- [Microsoft. (n.d.). Services. Retrieved June 7, 2016.](https://technet.microsoft.com/en-us/library/cc772408.aspx)
- [Apple. (n.d.). Creating Launch Daemons and Agents. Retrieved July 10, 2017.](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)
- [Patrick Wardle. (2016, February 29). Let's Play Doctor: Practical OS X Malware Detection & Analysis. Retrieved November 17, 2024.](https://papers.put.as/papers/macosx/2016/RSA_OSX_Malware.pdf)
- [CISA et al. (2024, April 18). #StopRansomware: Akira Ransomware. Retrieved December 10, 2024.](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)
- [Scott Henderson, Cristiana Kittner, Sarah Hawley & Mark Lechtik, Google Cloud. (2023, January 19). Suspected Chinese Threat Actors Exploiting FortiOS Vulnerability (CVE-2022-42475). Retrieved December 31, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
- [DHS/CISA. (2026, February 11). AR25-338A: BRICKSTORM Backdoor. Retrieved April 16, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
- [ANSSI. (2021, January 27). SANDWORM INTRUSION SET CAMPAIGN TARGETING CENTREON SYSTEMS. Retrieved March 30, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
- [PwC Threat Intelligence. (2023, October 25). Yellow Liderc ships its scripts and delivers IMAPLoader malware. Retrieved August 14, 2024.](https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/yellow-liderc-ships-its-scripts-delivers-imaploader-malware.html)
- [Lin, M. et al. (2024, February 27). Cutting Edge, Part 3: Investigating Ivanti Connect Secure VPN Exploitation and Persistence Attempts. Retrieved March 1, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [Azure Edge and Platform Security Team & Microsoft 365 Defender Research Team. (2021, December 8). Improve kernel security with the new Microsoft Vulnerable and Malicious Driver Reporting Center. Retrieved April 6, 2022.](https://www.microsoft.com/security/blog/2021/12/08/improve-kernel-security-with-the-new-microsoft-vulnerable-and-malicious-driver-reporting-center/)
- [Jordan Geurten et al. . (2022, March 29). Microsoft recommended driver block rules. Retrieved April 7, 2022.](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)

---

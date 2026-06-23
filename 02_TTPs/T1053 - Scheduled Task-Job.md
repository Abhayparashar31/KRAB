# Scheduled Task/Job

## Description

Adversaries may abuse task scheduling functionality to facilitate initial or recurring execution of malicious code. Utilities exist within all major operating systems to schedule programs or scripts to be executed at a specified date and time. A task can also be scheduled on a remote system, provided the proper authentication is met (ex: RPC and file and printer sharing in Windows environments). Scheduling a task on a remote system typically may require being a member of an admin or otherwise privileged group on the remote system. [1]

Adversaries may use task scheduling to execute programs at system startup or on a scheduled basis for persistence. These mechanisms can also be abused to run a process under the context of a specified account (such as one with elevated permissions/privileges). Similar to System Binary Proxy Execution , adversaries have also abused task scheduling to potentially mask one-time execution under a trusted system process. [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries set FortiGate scheduled tasks to run the adversary generated CLI scripts weekly. [3] |
| S0447 | Lokibot | Lokibot 's second stage DLL has set a timer using "timeSetEvent" to schedule its next execution. [4] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for permission weaknesses in scheduled tasks that could be used to escalate privileges. [5] |
| M1028 | Operating System Configuration | Configure settings for scheduled tasks to force tasks to run under the context of the authenticated account instead of allowing them to run as SYSTEM. The associated Registry key is located at HKLM\SYSTEM\CurrentControlSet\Control\Lsa\SubmitControl . The setting can be configured through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > Security Options: Domain Controller: Allow server operators to schedule tasks, set to disabled. [6] |
| M1026 | Privileged Account Management | Configure the Increase Scheduling Priority option to only allow the Administrators group the rights to schedule a priority process. This can be can be configured through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Increase scheduling priority. [7] |
| M1022 | Restrict File and Directory Permissions | Restrict access by setting directory and file permissions that are not specific to users or privileged accounts. |
| M1018 | User Account Management | Limit privileges of user accounts and remediate Privilege Escalation vectors so only authorized administrators can create scheduled tasks on remote systems. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0094 | Cross-Platform Behavioral Detection of Scheduled Task/Job Abuse | AN0258 | Detects creation or modification of scheduled tasks using schtasks.exe, at.exe, or COM objects followed by execution of outlier processes tied to the scheduled job. |
| AN0259 | Detects creation or modification of cron jobs via crontab, /etc/cron.* directories, or systemd timer units with execution by unusual users or non-standard intervals. |  |  |
| AN0260 | Detects creation or alteration of LaunchAgents or LaunchDaemons with corresponding plist modification followed by execution of associated binaries. |  |  |
| AN0261 | Detects unusual use of cron or sleep loops inside containers executing unfamiliar scripts or binaries repeatedly. |  |  |
| AN0262 | Detects modification of ESXi cron jobs, local.sh scripts, or scheduled API calls to persist custom binaries or shell scripts. |  |  |

---

## References

- [Microsoft. (2005, January 21). Task Scheduler and security. Retrieved June 8, 2016.](https://technet.microsoft.com/en-us/library/cc785125.aspx)
- [Campbell, B. et al. (2022, March 21). Serpent, No Swiping! New Backdoor Targets French Entities with Unique Attack Chain. Retrieved April 11, 2022.](https://www.proofpoint.com/us/blog/threat-insight/serpent-no-swiping-new-backdoor-targets-french-entities-unique-attack-chain)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Muhammad, I., Unterbrink, H.. (2021, January 6). A Deep Dive into Lokibot Infection Chain. Retrieved August 31, 2021.](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
- [PowerSploit. (n.d.). Retrieved December 4, 2014.](https://github.com/mattifestation/PowerSploit)
- [Microsoft. (2012, November 15). Domain controller: Allow server operators to schedule tasks. Retrieved December 18, 2017.](https://technet.microsoft.com/library/jj852168.aspx)
- [Microsoft. (2013, May 8). Increase scheduling priority. Retrieved December 18, 2017.](https://technet.microsoft.com/library/dn221960.aspx)

---

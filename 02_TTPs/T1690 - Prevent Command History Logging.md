# Prevent Command History Logging

## Description

Adversaries may impair command history logging to hide commands they run on a compromised system. Various command interpreters keep track of the commands users type in their terminal so that users can retrace what they have done.

On Linux and macOS, command history is tracked in a file pointed to by the environment variable HISTFILE . When a user logs off a system, this information is flushed to a file in the user's home directory called ~/.bash_history . The HISTCONTROL environment variable keeps track of what should be saved by the history command and eventually into the ~/.bash_history file when a user logs out. HISTCONTROL does not exist by default on macOS, but can be set by the user and will be respected. The HISTFILE environment variable is also used in some ESXi systems. [1]

Adversaries may clear the history environment variable ( unset HISTFILE ) or set the command history size to zero ( export HISTFILESIZE=0 ) to prevent logging of commands. Additionally, HISTCONTROL can be configured to ignore commands that start with a space by simply setting it to "ignorespace". HISTCONTROL can also be set to ignore duplicate commands by setting it to "ignoredups". In some Linux systems, this is set by default to "ignoreboth" which covers both of the previous examples. This means that " ls" will not be saved, but "ls" would be saved by history. Adversaries can abuse this to operate without leaving traces by simply prepending a space to all of their terminal commands.

On Windows systems, the PSReadLine module tracks commands used in all PowerShell sessions and writes them to a file ( $env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt by default). Adversaries may change where these logs are saved using Set-PSReadLineOption -HistorySavePath {File Path} . This will cause ConsoleHost_history.txt to stop receiving logs. Additionally, it is possible to turn off logging to this file using the PowerShell command Set-PSReadlineOption -HistorySaveStyle SaveNothing . [2] [3]

Adversaries may also leverage a Network Device CLI on network devices to disable historical command logging (e.g. no logging ).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0082 | APT38 | APT38 has prepended a space to all of their terminal commands to operate without leaving traces in the HISTCONTROL environment. [4] |
| C0046 | ArcaneDoor | ArcaneDoor included disabling logging on targeted Cisco ASA appliances. [5] [6] |
| S1161 | BPFDoor | BPFDoor sets the MYSQL_HISTFILE and HISTFILE to /dev/null preventing the shell and MySQL from logging history in /proc/<PID>/environ . [7] |
| S9015 | BRICKSTORM | BRICKSTORM has impaired command logging through the use of dev/null which prevents generating output from the command and does not wait for input. [8] |
| S1186 | Line Dancer | Line Dancer can disable syslog on compromised devices. [5] |
| G1051 | Medusa Group | Medusa Group has removed PowerShell command history through the use of the PSReadLine module by running the PowerShell command Remove-Item (Get-PSReadlineOption).HistorySavePath . [9] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 used malware to clear the HISTFILE environmental variable and to inject into Junos OS processes to inhibit logging. [10] [11] |
| G1041 | Sea Turtle | Sea Turtle unset the Bash and MySQL history files on victim systems. [12] |
| S0692 | SILENTTRINITY | SILENTTRINITY can bypass ScriptBlock logging to execute unmanaged PowerShell code from memory. [13] |
| S9024 | SPAWNCHIMERA | SPAWNCHIMERA has disabled logging and log forwarding on Ivanti devices targeting the dslogserver process. [14] [15] [16] [17] |
| G1048 | UNC3886 | UNC3886 has tampered with and disabled logging services on targeted systems. [18] |
| S1217 | VIRTUALPITA | VIRTUALPITA can impair logging by setting the HISTFILE environmental variable to 0 and stopping the vmsyslogd service. [1] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1039 | Environment Variable Permissions | Prevent users from changing the HISTCONTROL , HISTFILE , and HISTFILESIZE environment variables. [19] |
| M1028 | Operating System Configuration | Make sure that the HISTCONTROL environment variable is set to "ignoredups" instead of "ignoreboth" or "ignorespace". |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0563 | Detection Strategy for Defense Impairment via Prevent Command History Logging across OS platforms. | AN1555 | Detection of environment variable tampering (HISTFILE, HISTCONTROL, HISTFILESIZE) and absence of expected bash history writes. Correlation of unset or zeroed history variables with active shell sessions is indicative of adversarial evasion. |
| AN1556 | Detection of bash/zsh history suppression via HISTFILE/HISTCONTROL manipulation and absence of ~/.bash_history updates. Observing environment variable changes tied to terminal processes is a strong indicator. |  |  |
| AN1557 | Detection of PowerShell history suppression using Set-PSReadLineOption with SaveNothing or altered HistorySavePath. Correlating these options with PowerShell usage highlights adversarial evasion attempts. |  |  |
| AN1558 | Detection of unset HISTFILE or modified history variables in ESXi shell sessions. Correlation of suspicious shell sessions with no recorded commands despite active usage. |  |  |
| AN1559 | Detection of CLI commands that disable history logging such as 'no logging'. Anomalous lack of new commands in session logs while activity persists is a strong signal. |  |  |

---

## References

- [Alexander Marvi, Jeremy Koppen, Tufail Ahmed, and Jonathan Lepore. (2022, September 29). Bad VIB(E)s Part One: Investigating Novel Malware Persistence Within ESXi Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
- [Microsoft. (n.d.). Retrieved April 15, 2026.](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_history?view=powershell-7.6&viewFallbackFrom=powershell-7)
- [Vikas, S. (2020, August 26). PowerShell Command History Forensics. Retrieved November 17, 2024.](https://community.sophos.com/sophos-labs/b/blog/posts/powershell-command-history-forensics)
- [DHS/CISA. (2020, August 26). FASTCash 2.0: North Korea's BeagleBoyz Robbing Banks. Retrieved September 29, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)
- [Cisco Talos. (2024, April 24). ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices. Retrieved January 6, 2025.](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
- [Canadian Centre for Cyber Security. (2024, April 24). Cyber Activity Impacting CISCO ASA VPNs. Retrieved January 6, 2025.](https://www.cyber.gc.ca/en/news-events/cyber-activity-impacting-cisco-asa-vpns)
- [The Sandfly Security Team. (2022, May 11). BPFDoor - An Evasive Linux Backdoor Technical Analysis. Retrieved September 29, 2023.](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/)
- [DHS/CISA. (2026, February 11). AR25-338A: BRICKSTORM Backdoor. Retrieved April 16, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Lamparski, L. et al. (2025, March 11). Ghost in the Router: China-Nexus Espionage Actor UNC3886 Targets Juniper Routers. Retrieved June 24, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers)
- [Juniper Networks, Cybersecurity R&D. (2025, March 11). The RedPenguin Malware Incident. Retrieved June 24, 2025.](https://supportportal.juniper.net/sfc/servlet.shepherd/document/download/069Dp00000FzdmIIAR?operationContext=S1)
- [Hunt & Hackett Research Team. (2024, January 5). Turkish espionage campaigns in the Netherlands. Retrieved November 20, 2024.](https://www.huntandhackett.com/blog/turkish-espionage-campaigns)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [DHS/CISA. (2026, February 26). MAR-25993211-r1.v2 Ivanti Connect Secure (RESURGE): AR25-087A. Retrieved April 17, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
- [John Wolfram, Michael Edie, Jacob Thompson, Matt Lin, Josh Murchie. (2025, April 3). Suspected China-Nexus Threat Actor Actively Exploiting Critical Ivanti Connect Secure Vulnerability (CVE-2025-22457). Retrieved April 13, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-exploiting-critical-ivanti-vulnerability)
- [Matt Lin, Austin Larsen, John Wolfram, Ashley Pearson, Josh Murchie, Lukasz Lamparski, Joseph Pisano, Ryan Hall, Ron Craft, Shawn Crew, Billy Wong, Tyler McLellan. (2024, April 4). Cutting Edge, Part 4: Ivanti Connect Secure VPN Post-Exploitation Lateral Movement Case Studies. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
- [Sila Ozeren Hacioglu. (2025, May 5). UNC5221’s Latest Exploit: Weaponizing CVE-2025-22457 in Ivanti Connect Secure. Retrieved April 13, 2026.](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
- [Alexander Marvi, Brad Slaybaugh, Ron Craft, and Rufus Brown. (2023, June 13). VMware ESXi Zero-Day Used by Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)
- [Mathew Branwell. (2012, March 21). Securing .bash_history file. Retrieved July 8, 2017.](http://www.akyl.net/securing-bashhistory-file-make-sure-your-linux-system-users-won%E2%80%99t-hide-or-delete-their-bashhistory)

---

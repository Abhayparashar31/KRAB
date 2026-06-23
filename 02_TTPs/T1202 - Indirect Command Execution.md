# Indirect Command Execution

## Description

Adversaries may abuse utilities that allow for command execution to bypass security restrictions that limit the use of command-line interpreters. Various Windows utilities may be used to execute commands, possibly without invoking cmd . For example, Forfiles , the Program Compatibility Assistant ( pcalua.exe ), components of the Windows Subsystem for Linux (WSL), Scriptrunner.exe , as well as other utilities may invoke the execution of programs and commands from a Command and Scripting Interpreter , Run window, or via scripts. [1] [2] [3] [4] [5] Adversaries may also abuse the ssh.exe binary to execute malicious commands via the ProxyCommand and LocalCommand options, which can be invoked via the -o flag or by modifying the SSH config file. [6]

Adversaries may abuse these features for Stealth , specifically to perform arbitrary execution while subverting detections and/or mitigation controls (such as Group Policy) that limit/prevent the usage of cmd or file extensions more commonly associated with malicious payloads.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0193 | Forfiles | Forfiles can be used to subvert controls and possibly conceal command execution by not directly invoking cmd . [1] [2] |
| G0032 | Lazarus Group | Lazarus Group persistence mechanisms have used forfiles.exe to execute .htm files. [7] |
| G1039 | RedCurl | RedCurl has used pcalua.exe to obfuscate binary execution and remote connections. [8] |
| S0379 | Revenge RAT | Revenge RAT uses the Forfiles utility to execute commands on the system. [9] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0200 | Indirect Command Execution – Windows utility abuse behavior chain | AN0576 | Cause→effect chain: (1) A user or service launches an indirection utility (e.g., forfiles.exe, pcalua.exe, wsl.exe, scriptrunner.exe, ssh.exe with -o ProxyCommand/LocalCommand). (2) That utility spawns a secondary program/command (PowerShell, cmd, msiexec, regsvr32, curl, arbitrary EXE) and/or opens outbound network connections. (3) Optional precursor modification of SSH config to persist LocalCommand/ProxyCommand. Correlate process creation, command/script content, file access to %USERPROFILE%.ssh\config, and network connections from the utility or its child. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0200 | Indirect Command Execution – Windows utility abuse behavior chain | AN0576 | Cause→effect chain: (1) A user or service launches an indirection utility (e.g., forfiles.exe, pcalua.exe, wsl.exe, scriptrunner.exe, ssh.exe with -o ProxyCommand/LocalCommand). (2) That utility spawns a secondary program/command (PowerShell, cmd, msiexec, regsvr32, curl, arbitrary EXE) and/or opens outbound network connections. (3) Optional precursor modification of SSH config to persist LocalCommand/ProxyCommand. Correlate process creation, command/script content, file access to %USERPROFILE%.ssh\config, and network connections from the utility or its child. |

---

## References

- [vector_sec. (2017, August 11). Defenders watching launches of cmd? What about forfiles?. Retrieved September 12, 2024.](https://x.com/vector_sec/status/896049052642533376)
- [Evi1cg. (2017, November 26). block cmd.exe ? try this :. Retrieved September 12, 2024.](https://x.com/Evi1cg/status/935027922397573120)
- [Secure Team - Information Assurance. (2023, January 8). Windows Error Reporting Tool Abused to Load Malware. Retrieved July 8, 2024.](https://secureteam.co.uk/2023/01/08/windows-error-reporting-tool-abused-to-load-malware/)
- [SS64. (n.d.). ScriptRunner.exe. Retrieved July 8, 2024.](https://ss64.com/nt/scriptrunner.html)
- [Bill Toulas. (2023, January 4). Hackers abuse Windows error reporting tool to deploy malware. Retrieved July 8, 2024.](https://www.bleepingcomputer.com/news/security/hackers-abuse-windows-error-reporting-tool-to-deploy-malware/)
- [Cyble. (2024, December 5). Threat Actor Targets the Manufacturing industry with Lumma Stealer and Amadey Bot. Retrieved February 4, 2025.](https://cyble.com/blog/threat-actor-targets-manufacturing-industry-with-malware/)
- [Pradhan, A. (2022, February 8). LolZarus: Lazarus Group Incorporating Lolbins into Campaigns. Retrieved March 22, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)
- [Tancio et al. (2024, March 6). Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence. Retrieved August 9, 2024.](https://www.trendmicro.com/en_us/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
- [Gannon, M. (2019, February 11). With Upgrades in Delivery and Support Infrastructure, Revenge RAT Malware is a Bigger Threat. Retrieved November 17, 2024.](https://web.archive.org/web/20200428173819/https://cofense.com/upgrades-delivery-support-infrastructure-revenge-rat-malware-bigger-threat/)

---

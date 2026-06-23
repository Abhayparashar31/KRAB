# Trusted Developer Utilities Proxy Execution

## Description

Adversaries may take advantage of trusted developer utilities to proxy execution of malicious payloads. There are many utilities used for software development related tasks that can be used to execute code in various forms to assist in development, debugging, and reverse engineering. [1] [2] [3] [4] These utilities may often be signed with legitimate certificates that allow them to execute on a system and proxy execution of malicious code through a trusted process that effectively bypasses application control solutions.

Smart App Control is a feature of Windows that blocks applications it considers potentially malicious from running by verifying unsigned applications against a known safe list from a Microsoft cloud service before executing them. [5] However, adversaries may leverage "reputation hijacking" to abuse an operating system’s trust of safe, signed applications that support the execution of arbitrary code. By leveraging Trusted Developer Utilities Proxy Execution to run their malicious code, adversaries may bypass Smart App Control protections. [6]

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1042 | Disable or Remove Feature or Program | Specific developer utilities may not be necessary within a given environment and should be removed if not used. |
| M1038 | Execution Prevention | Certain developer utilities should be blocked or restricted if not required. |
| M1021 | Restrict Web-Based Content | Consider disabling software installation or execution from the internet via developer utilities. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0172 | Behavior-chain, platform-aware detection strategy for T1127 Trusted Developer Utilities Proxy Execution (Windows) | AN0488 | A trusted/signed developer utility (parent) is executed in a non-developer context and (a) spawns suspicious children (e.g., powershell.exe, cmd.exe, rundll32.exe, regsvr32.exe, wscript.exe), (b) loads unsigned/user-writable DLLs, (c) writes and then runs a new PE from user-writable paths, and/or (d) immediately makes outbound network connections. |

---

## References

- [Nelson, M. (2017, November 17). Bypassing Application Whitelisting By Using dnx.exe. Retrieved May 25, 2017.](https://enigma0x3.net/2016/11/17/bypassing-application-whitelisting-by-using-dnx-exe/)
- [Nelson, M. (2016, November 21). Bypassing Application Whitelisting By Using rcsi.exe. Retrieved May 26, 2017.](https://enigma0x3.net/2016/11/21/bypassing-application-whitelisting-by-using-rcsi-exe/)
- [Graeber, M. (2016, August 15). Bypassing Application Whitelisting by using WinDbg/CDB as a Shellcode Runner. Retrieved November 17, 2024.](https://web.archive.org/web/20160816135945/http://www.exploit-monday.com/2016/08/windbg-cdb-shellcode-runner.html)
- [LOLBAS. (n.d.). Tracker.exe. Retrieved July 31, 2019.](https://lolbas-project.github.io/lolbas/OtherMSBinaries/Tracker/)
- [Microsoft. (n.d.). Smart App Control Frequently Asked Questions. Retrieved April 4, 2025.](https://support.microsoft.com/en-us/windows/smart-app-control-frequently-asked-questions-285ea03d-fa88-4d56-882e-6698afdb7003)
- [Joe Desimone. (2024, August 5). Dismantling Smart App Control. Retrieved March 21, 2025.](https://www.elastic.co/security-labs/dismantling-smart-app-control)

---

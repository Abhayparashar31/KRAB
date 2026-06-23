# System Script Proxy Execution

## Description

Adversaries may use trusted scripts, often signed with certificates, to proxy the execution of malicious files. Several Microsoft signed scripts that have been downloaded from Microsoft or are default on Windows installations can be used to proxy execution of other files. [1] This behavior may be abused by adversaries to execute malicious files that could bypass application control and signature validation on systems. [2]

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1038 | Execution Prevention | Certain signed scripts that can be used to execute other programs may not be necessary within a given environment. Use application control configured to block execution of these scripts if they are not required for a given system or network to prevent potential misuse by adversaries. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0466 | Detection of Script-Based Proxy Execution via Signed Microsoft Utilities | AN1288 | Execution of Microsoft-signed scripts (e.g., pubprn.vbs, installutil.exe, wscript.exe, cscript.exe) used to proxy execution of untrusted or external binaries. Behavior is detected through command-line process lineage, child process spawning, and unsigned payload execution from signed parent. |

---

## References

- [Oddvar Moe et al. (2022, February). Living Off The Land Binaries, Scripts and Libraries. Retrieved March 7, 2022.](https://github.com/LOLBAS-Project/LOLBAS#criteria)
- [Moe, O. (2018, March 1). Ultimate AppLocker Bypass List. Retrieved April 10, 2018.](https://github.com/api0cradle/UltimateAppLockerByPassList)

---

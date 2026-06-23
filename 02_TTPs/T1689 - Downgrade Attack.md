# Downgrade Attack

## Description

Adversaries may downgrade or use a version of system features that may be outdated, vulnerable, and/or does not support updated security controls. Downgrade attacks typically take advantage of a system’s backward compatibility to force it into less secure modes of operation.

Adversaries may downgrade and use various less-secure versions of features of a system, such as Command and Scripting Interpreter or even network protocols that can be abused to enable Adversary-in-the-Middle or Network Sniffing . [1] For example, PowerShell versions 5+ includes Script Block Logging (SBL), which can record executed script content. However, adversaries may attempt to execute a previous version of PowerShell that does not support SBL with the intent to impair defenses while running malicious scripts that may have otherwise been detected. [2] [3] [4]

Adversaries may similarly target network traffic to downgrade from an encrypted HTTPS connection to an unsecured HTTP connection that exposes network data in clear text. [5] [6] On Windows systems, adversaries may downgrade the boot manager to a vulnerable version that bypasses Secure Boot, granting the ability to disable various operating system security mechanisms. [7]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1180 | BlackByte Ransomware | BlackByte Ransomware enables SMBv1 during execution. [8] |
| C0041 | FrostyGoop Incident | During FrostyGoop Incident , the adversary downgraded firmware on victim devices in order to impair visibility into the process environment. [9] |
| S0692 | SILENTTRINITY | SILENTTRINITY can downgrade NTLM to capture NTLM hashes. [10] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1042 | Disable or Remove Feature or Program | Consider removing previous versions of tools that are unnecessary to the environment when possible. |
| M1054 | Software Configuration | Consider implementing policies on internal web servers, such HTTP Strict Transport Security, that enforce the use of HTTPS/network traffic encryption to prevent insecure connections. [11] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0350 | Detecting Downgrade Attacks | AN0995 | Detection of processes launching downgraded PowerShell versions (e.g., v2) or other legacy binaries that lack logging or security features. Correlates command-line arguments, process metadata, and version fields. Monitors registry changes to Defender or HVCI keys that could indicate intentional downgrades. |
| AN0996 | Monitors execution of older or legacy interpreters (e.g., python2, bash with restricted history logging), downgrade of TLS/SSL configurations, or forced fallback to unencrypted protocols. Detects suspicious reconfiguration of kernel modules or boot loaders to reduce integrity controls. |  |  |
| AN0997 | Detection of execution of legacy scripting runtimes (e.g., older versions of Python, Bash, or PowerShell Core) lacking auditing. Monitoring for changes to EFI or system boot files indicative of downgrade-based persistence or bypass of integrity features. |  |  |

---

## References

- [Praetorian. (2014, August 19). Man-in-the-Middle TLS Protocol Downgrade Attack. Retrieved October 8, 2021.](https://www.praetorian.com/blog/man-in-the-middle-tls-ssl-protocol-downgrade-attack/)
- [Falcon Complete Team. (2021, May 11). Response When Minutes Matter: Rising Up Against Ransomware. Retrieved April 15, 2026.](https://www.crowdstrike.com/en-us/blog/how-falcon-complete-stopped-a-big-game-hunting-ransomware-attack/)
- [Nathan Kirk. (2018, June 18). Bring Your Own Land (BYOL) — A Novel Red Teaming Technique. Retrieved April 15, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/bring-your-own-land-novel-red-teaming-technique/)
- [Hao, M. (2019, February 27). Attack and Defense Around PowerShell Event Logging. Retrieved November 24, 2021.](https://nsfocusglobal.com/attack-and-defense-around-powershell-event-logging/)
- [Check Point. (n.d.). Targeted SSL Stripping Attacks Are Real. Retrieved May 24, 2023.](https://blog.checkpoint.com/research/targeted-ssl-stripping-attacks-are-real/amp/)
- [Bart Lenaerts-Bergmans. (2023, March 13). What are Downgrade Attacks?. Retrieved April 15, 2026.](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/downgrade-attack/)
- [Alon Leviev. (2024, August 7). Windows Downdate: Downgrade Attacks Using Windows Updates. Retrieved January 8, 2025.](https://www.safebreach.com/blog/downgrade-attacks-using-windows-updates/)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [Mark Graham, Carolyn Ahlers, Kyle O'Meara; Dragos. (2024, July). Impact of FrostyGoop ICS Malware on Connected OT Systems. Retrieved November 20, 2024.](https://hub.dragos.com/hubfs/Reports/Dragos-FrostyGoop-ICS-Malware-Intel-Brief-0724_r2.pdf)
- [byt3bl33d3r. (n.d.). SILENTTRINITY. Retrieved September 12, 2024.](https://github.com/byt3bl33d3r/SILENTTRINITY)
- [Chromium. (n.d.). HTTP Strict Transport Security. Retrieved May 24, 2023.](https://www.chromium.org/hsts/)

---

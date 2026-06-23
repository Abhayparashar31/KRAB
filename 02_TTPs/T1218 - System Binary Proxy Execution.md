# System Binary Proxy Execution

## Description

Adversaries may bypass process and/or signature-based defenses by proxying execution of malicious content with signed, or otherwise trusted, binaries. Binaries used in this technique are often Microsoft-signed files, indicating that they have been either downloaded from Microsoft or are already native in the operating system. [1] Binaries signed with trusted digital certificates can typically execute on Windows systems protected by digital signature validation. Several Microsoft signed binaries that are default on Windows installations can be used to proxy execution of other files or commands.

Similarly, on Linux systems adversaries may abuse trusted binaries such as split to proxy execution of malicious commands. [2] [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0032 | Lazarus Group | Lazarus Group lnk files used for persistence have abused the Windows Update Client ( wuauclt.exe ) to execute a malicious DLL. [4] [5] |
| G1017 | Volt Typhoon | Volt Typhoon has used native tools and processes including living off the land binaries or "LOLBins" to maintain and expand access to the victim networks. [6] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1042 | Disable or Remove Feature or Program | Many native binaries may not be necessary within a given environment. |
| M1038 | Execution Prevention | Consider using application control to prevent execution of binaries that are susceptible to abuse and not required for a given system or network. |
| M1050 | Exploit Protection | Microsoft's Enhanced Mitigation Experience Toolkit (EMET) Attack Surface Reduction (ASR) feature can be used to block methods of using using trusted binaries to bypass application control. |
| M1037 | Filter Network Traffic | Use network appliances to filter ingress or egress traffic and perform protocol-based filtering. Configure software on endpoints to filter network traffic. |
| M1026 | Privileged Account Management | Restrict execution of particularly vulnerable binaries to privileged accounts or groups that need to use it to lessen the opportunities for malicious usage. |
| M1021 | Restrict Web-Based Content | Restrict use of certain websites, block downloads/attachments, block Javascript, restrict browser extensions, etc. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0081 | Detection of Proxy Execution via Trusted Signed Binaries Across Platforms | AN0226 | Execution of trusted, Microsoft-signed binaries such as rundll32.exe , msiexec.exe , or regsvr32.exe used to execute externally hosted, unsigned, or suspicious payloads through command-line parameters or network retrieval. |
| AN0227 | Execution of trusted system binaries (e.g., split , tee , bash , env ) used in uncommon sequences or chained behaviors to execute malicious payloads or perform actions inconsistent with normal system or script behavior. |  |  |
| AN0228 | Use of system binaries such as osascript , bash , or curl to download or execute unsigned code or files in conjunction with application proxying. |  |  |

---

## References

- [Oddvar Moe et al. (2022, February). Living Off The Land Binaries, Scripts and Libraries. Retrieved March 7, 2022.](https://github.com/LOLBAS-Project/LOLBAS#criteria)
- [Torbjorn Granlund, Richard M. Stallman. (2020, March null). split(1) — Linux manual page. Retrieved March 25, 2022.](https://man7.org/linux/man-pages/man1/split.1.html)
- [GTFOBins. (2020, November 13). split. Retrieved April 18, 2022.](https://gtfobins.github.io/gtfobins/split/)
- [Saini, A. and Hossein, J. (2022, January 27). North Korea’s Lazarus APT leverages Windows Update client, GitHub in latest campaign. Retrieved January 27, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)
- [Pradhan, A. (2022, February 8). LolZarus: Lazarus Group Incorporating Lolbins into Campaigns. Retrieved March 22, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/02/08/lolzarus-lazarus-group-incorporating-lolbins-into-campaigns)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)

---

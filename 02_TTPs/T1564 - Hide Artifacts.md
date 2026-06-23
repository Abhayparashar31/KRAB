# Hide Artifacts

## Description

Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Operating systems may have features to hide various artifacts, such as important system files and administrative task execution, to avoid disrupting user work environments and prevent users from changing files or features on the system. Adversaries may abuse these features to hide artifacts such as files, directories, user accounts, or other system activity to evade detection. [1] [2] [3]

Adversaries may also attempt to hide artifacts associated with malicious behavior by creating computing regions that are isolated from common security instrumentation, such as through the use of virtualization technology. [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0482 | Bundlore | Bundlore uses the mktemp utility to make unique file and directory names for payloads, such as TMP_DIR=`mktemp -d -t x . [5] |
| S1066 | DarkTortilla | DarkTortilla has used %HiddenReg% and %HiddenKey% as part of its persistence via the Windows registry. [6] |
| S9025 | NOOPLDR | NOOPLDR can hide services used to aid execution. [7] |
| S0402 | OSX/Shlayer | OSX/Shlayer has used the mktemp utility to make random and unique filenames for payloads, such as export tmpDir="$(mktemp -d /tmp/XXXXXXXXXXXX)" or mktemp -t Installer . [8] [5] [9] |
| S0332 | Remcos | Remcos can modify file attributes to hide the file. [10] |
| S1011 | Tarrask | Tarrask is able to create "hidden" scheduled tasks by deleting the Security Descriptor ( SD ) registry value. [11] |
| S0670 | WarzoneRAT | WarzoneRAT can masquerade the Process Environment Block on a compromised host to hide its attempts to elevate privileges through IFileOperation . [12] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1049 | Antivirus/Antimalware | Review and audit file/folder exclusions, and limit scope of exclusions to only what is required where possible. [13] |
| M1013 | Application Developer Guidance | Application developers should consider limiting the requirements for custom or otherwise difficult to manage file/folder exclusions. Where possible, install applications to trusted system folder paths that are already protected by restricted file and directory permissions. |
| M1047 | Audit | Periodically audit virtual machines for abnormalities. |
| M1033 | Limit Software Installation | Restrict the installation of software that may be abused to create hidden desktops, such as hVNC, to user groups that require it. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0502 | Detection Strategy for Hidden Artifacts Across Platforms | AN1384 | Abuse of file/registry attributes to hide malicious files, directories, or services. Defender view: detection of attrib.exe setting hidden/system flags, creation of Alternate Data Streams, or registry keys altering file visibility. |
| AN1385 | Hidden file creation using leading '.' or file attribute changes with chattr (immutable/hidden flags). Defender view: detect execution of chattr, lsattr anomalies, and unusual hidden files appearing in system directories. |  |  |
| AN1386 | Hidden files via 'chflags hidden' or Apple-specific attributes, LaunchAgents/LaunchDaemons placed in non-standard hidden directories. Defender view: detect command execution modifying file flags and unusual plist creation in hidden paths. |  |  |
| AN1387 | Abuse of VMFS or ESXi shell to hide datastore files, renaming/moving VMDK or VMX files into hidden directories. Defender view: anomalous ESXi shell commands or file operations obscuring VM artifacts. |  |  |
| AN1388 | Malicious macros or embedded objects hidden within Office documents by renaming streams or using hidden OLE objects. Defender view: detection of hidden macro streams or objects in documents correlated with anomalous execution. |  |  |

---

## References

- [Dani Creus, Tyler Halfpop, Robert Falcone. (2016, September 26). Sofacy's 'Komplex' OS X Trojan. Retrieved July 8, 2017.](https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/)
- [Amit Serper. (2016). Cybereason Lab Analysis OSX.Pirrit. Retrieved December 10, 2021.](https://cdn2.hubspot.net/hubfs/3354902/Content%20PDFs/Cybereason-Lab-Analysis-OSX-Pirrit-4-6-16.pdf)
- [Arntz, P. (2015, July 22). Introduction to Alternate Data Streams. Retrieved March 21, 2018.](https://blog.malwarebytes.com/101/2015/07/introduction-to-alternate-data-streams/)
- [SophosLabs. (2020, May 21). Ragnar Locker ransomware deploys virtual machine to dodge security. Retrieved June 29, 2020.](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
- [Phil Stokes. (2021, February 16). 20 Common Tools & Techniques Used by macOS Threat Actors & Malware. Retrieved August 23, 2021.](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [Phil Stokes. (2020, September 8). Coming Out of Your Shell: From Shlayer to ZShlayer. Retrieved September 13, 2021.](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/)
- [Jaron Bradley. (2021, April 26). Shlayer malware abusing Gatekeeper bypass on macOS. Retrieved September 22, 2021.](https://www.jamf.com/blog/shlayer-malware-abusing-gatekeeper-bypass-on-macos/)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Microsoft Threat Intelligence Team & Detection and Response Team . (2022, April 12). Tarrask malware uses scheduled tasks for defense evasion. Retrieved June 1, 2022.](https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [Microsoft. (2024, February 27). Contextual file and folder exclusions. Retrieved March 29, 2024.](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-contextual-file-folder-exclusions-microsoft-defender-antivirus)

---

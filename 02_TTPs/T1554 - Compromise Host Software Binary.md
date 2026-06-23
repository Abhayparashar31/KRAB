# Compromise Host Software Binary

## Description

Adversaries may modify host software binaries to establish persistent access to systems. Software binaries/executables provide a wide range of system commands or services, programs, and libraries. Common software binaries are SSH clients, FTP clients, email clients, web browsers, and many other user or server applications.

Adversaries may establish persistence though modifications to host software binaries. For example, an adversary may replace or otherwise infect a legitimate application binary (or support files) with a backdoor. Since these binaries may be routinely executed by applications or the user, the adversary can leverage this for persistent access to the host. An adversary may also modify a software binary such as an SSH client in order to persistently collect credentials during logins (i.e., Modify Authentication Process ). [1]

An adversary may also modify an existing binary by patching in malicious functionality (e.g., IAT Hooking/Entry point patching) [2] prior to the binary’s legitimate execution. For example, an adversary may modify the entry point of a binary to point to malicious code patched in by the adversary before resuming normal execution flow. [3]

After modifying a binary, an adversary may attempt to impair defenses by preventing it from updating (e.g., via the yum-versionlock command or versionlock.list file in Linux systems that use the yum package manager). [1]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0025 | 2016 Ukraine Electric Power Attack | During the 2016 Ukraine Electric Power Attack , Sandworm Team used a trojanized version of Windows Notepad to add a layer of persistence for Industroyer . [4] |
| G1023 | APT5 | APT5 has modified legitimate binaries and scripts for Pulse Secure VPNs including the legitimate DSUpgrade.pm file to install the ATRIUM webshell for persistence. [5] [6] |
| S1136 | BFG Agonizer | BFG Agonizer uses DLL unhooking to remove user mode inline hooks that security solutions often implement. BFG Agonizer also uses IAT unhooking to remove user-mode IAT hooks that security solutions also use. [7] |
| S1184 | BOLDMOVE | BOLDMOVE contains a watchdog-like feature that monitors a particular file for modification. If modification is detected, the legitimate file is backed up and replaced with a trojanized file to allow for persistence through likely system upgrades. [8] |
| S0486 | Bonadan | Bonadan has maliciously altered the OpenSSH binary on targeted systems to create a backdoor. [9] |
| S1118 | BUSHWALK | BUSHWALK can embed into the legitimate querymanifest.cgi file on compromised Ivanti Connect Secure VPNs. [10] [11] |
| C0029 | Cutting Edge | During Cutting Edge , threat actors trojanized legitimate files in Ivanti Connect Secure appliances with malicious code. [12] [13] [10] |
| S0377 | Ebury | Ebury modifies the keyutils library to add malicious behavior to the OpenSSH client and the curl library. [14] [15] |
| S1120 | FRAMESTING | FRAMESTING can embed itself in the CAV Python package of an Ivanti Connect Secure VPN located in /home/venv3/lib/python3.6/site-packages/cav-0.1-py3.6.egg/cav/api/resources/category.py. [10] |
| S9010 | GlassWorm | GlassWorm can modify hardware wallet applications. [16] |
| S0604 | Industroyer | Industroyer has used a Trojanized version of the Windows Notepad application for an additional backdoor persistence mechanism. [4] |
| S0487 | Kessel | Kessel has maliciously altered the OpenSSH binary on targeted systems to create a backdoor. [9] |
| S0641 | Kobalos | Kobalos replaced the SSH client with a trojanized SSH client to steal credentials on compromised systems. [17] |
| S1119 | LIGHTWIRE | LIGHTWIRE can imbed itself into the legitimate compcheckresult.cgi component of Ivanti Connect Secure VPNs to enable command execution. [12] [10] |
| S1121 | LITTLELAMB.WOOLTEA | LITTLELAMB.WOOLTEA can append malicious components to the tmp/tmpmnt/bin/samba_upgrade.tar archive inside the factory reset partition in attempt to persist post reset. [11] |
| S9014 | PHASEJAM | PHASEJAM has modified legitimate components to enable persistence and execution, including inserting a web shell into getComponent.cgi and restAuth.cgi , modifying DSUpgrade.pm to block system upgrades, and overwriting remotedebug to execute arbitrary commands when specific parameters are provided. [18] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 peformed a local memory patching attack to modify the snmpd and mgd Junos OS daemons. [19] |
| S1104 | SLOWPULSE | SLOWPULSE is applied in compromised environments through modifications to legitimate Pulse Secure files. [6] |
| S0595 | ThiefQuest | ThiefQuest searches through the /Users/ folder looking for executable files. For each executable, ThiefQuest prepends a copy of itself to the beginning of the file. When the file is executed, the ThiefQuest code is executed first. ThiefQuest creates a hidden file, copies the original target executable to the file, then executes the new hidden file to maintain the appearance of normal behavior. [20] [21] |
| G1048 | UNC3886 | UNC3886 has trojanized Fortinet firmware and replaced the legitimate /usr/bin/tac_plus TACACS+ daemon for Linux with a malicious version containing credential logging functionality. [1] [22] |
| S1116 | WARPWIRE | WARPWIRE can embed itself into a legitimate file on compromised Ivanti Connect Secure VPNs. [12] |
| S1115 | WIREFIRE | WIREFIRE can modify the visits.py component of Ivanti Connect Secure VPNs for file download and arbitrary command execution. [12] [13] |
| S0658 | XCSSET | XCSSET uses a malicious browser application to replace the legitimate browser in order to continuously capture credentials, monitor web traffic, and download additional modules. [23] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1045 | Code Signing | Ensure all application component binaries are signed by the correct application developers. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0336 | Detect Compromise of Host Software Binaries | AN0949 | Monitors for unexpected modifications of system or application binaries, particularly signed executables. Correlates file write events with subsequent unsigned or anomalously signed process execution, and checks for tampered binaries outside normal patch cycles. |
| AN0950 | Detects modification of system or application binaries by monitoring /usr/bin, /bin, and other privileged directories. Correlates file integrity monitoring (FIM) events with unexpected process executions or service restarts. |  |  |
| AN0951 | Monitors binary modification in /Applications and system library paths. Detects unsigned or improperly signed binaries executed after modification. Tracks Gatekeeper or notarization bypass attempts tied to modified binaries. |  |  |
| AN0952 | Detects unauthorized modification of host binaries, modules, or services within ESXi. Correlates tampered files with subsequent unexpected service behavior or malicious module load attempts. |  |  |

---

## References

- [Punsaen Boonyakarn, Shawn Chew, Logeswaran Nadarajan, Mathew Potaczek, Jakub Jozwiak, and Alex Marvi. (2024, June 18). Cloaked and Covert: Uncovering UNC3886 Espionage Operations. Retrieved September 24, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [Or Chechik. (2022, October 31). Banking Trojan Techniques: How Financially Motivated Malware Became Infrastructure. Retrieved September 27, 2023.](https://unit42.paloaltonetworks.com/banking-trojan-techniques/#post-125550-_rm3d6xxbk52n)
- [Vladislav Hrčka. (2021, January 1). FontOnLake. Retrieved September 27, 2023.](https://web-assets.esetstatic.com/wls/2021/10/eset_fontonlake.pdf)
- [Anton Cherepanov. (2017, June 12). Win32/Industroyer: A new threat for industrial controls systems. Retrieved December 18, 2020.](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
- [Perez, D. et al. (2021, April 20). Check Your Pulse: Suspected APT Actors Leverage Authentication Bypass Techniques and Pulse Secure Zero-Day. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
- [Perez, D. et al. (2021, May 27). Re-Checking Your Pulse: Updates on Chinese APT Actors Compromising Pulse Secure VPN Devices. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [Scott Henderson, Cristiana Kittner, Sarah Hawley & Mark Lechtik, Google Cloud. (2023, January 19). Suspected Chinese Threat Actors Exploiting FortiOS Vulnerability (CVE-2022-42475). Retrieved December 31, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [Lin, M. et al. (2024, January 31). Cutting Edge, Part 2: Investigating Ivanti Connect Secure VPN Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
- [Lin, M. et al. (2024, February 27). Cutting Edge, Part 3: Investigating Ivanti Connect Secure VPN Exploitation and Persistence Attempts. Retrieved March 1, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-exploitation-persistence)
- [McLellan, T. et al. (2024, January 12). Cutting Edge: Suspected APT Targets Ivanti Connect Secure VPN in New Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-targets-ivanti-zero-day)
- [Meltzer, M. et al. (2024, January 10). Active Exploitation of Two Zero-Day Vulnerabilities in Ivanti Connect Secure VPN. Retrieved February 27, 2024.](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/)
- [M.Léveillé, M.. (2014, February 21). An In-depth Analysis of Linux/Ebury. Retrieved April 19, 2019.](https://www.welivesecurity.com/2014/02/21/an-in-depth-analysis-of-linuxebury/)
- [Marc-Etienne M.Léveillé. (2024, May 1). Ebury is alive but unseen. Retrieved May 21, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/ebury-is-alive-but-unseen.pdf)
- [Gal Hachamov. (2025, December 29). GlassWorm Goes Mac: Fresh Infrastructure, New Tricks. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
- [M.Leveille, M., Sanmillan, I. (2021, January). A WILD KOBALOS APPEARS Tricksy Linux malware goes after HPCs. Retrieved August 24, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
- [John Wolfram, Josh Murchie, Matt Lin, Daniel Ainsworth, Robert Wallace, Dimiter Andonov, Dhanesh Kizhakkinan, Jacob Thompson. (2025, January 8). Ivanti Connect Secure VPN Targeted in New Zero-Day Exploitation. Retrieved April 14, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
- [Juniper Networks, Cybersecurity R&D. (2025, March 11). The RedPenguin Malware Incident. Retrieved June 24, 2025.](https://supportportal.juniper.net/sfc/servlet.shepherd/document/download/069Dp00000FzdmIIAR?operationContext=S1)
- [Patrick Wardle. (2020, July 3). OSX.EvilQuest Uncovered part ii: insidious capabilities. Retrieved March 21, 2021.](https://objective-see.com/blog/blog_0x60.html)
- [Thomas Reed. (2020, July 7). Mac ThiefQuest malware may not be ransomware after all. Retrieved March 22, 2021.](https://blog.malwarebytes.com/mac/2020/07/mac-thiefquest-malware-may-not-be-ransomware-after-all/)
- [Marvi, A. et al.. (2023, March 16). Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation. Retrieved March 22, 2023.](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
- [Mac Threat Response, Mobile Research Team. (2020, August 13). The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSS Backdoor Planting in Safari, and Leverages Two Zero-day Exploits. Retrieved October 5, 2021.](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)

---

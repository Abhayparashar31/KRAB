# Rootkit

## Description

Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting/hooking and modifying operating system API calls that supply system information. [1]

Rootkits or rootkit enabling functionality may reside at the user or kernel level in the operating system or lower, to include a hypervisor or System Firmware . [2] Rootkits have been seen for Windows, Linux, and Mac OS X systems. [3] [4]

Rootkits that reside or modify boot sectors are known as Bootkit s and specifically target the boot process of the operating system.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0007 | APT28 | APT28 has used a UEFI (Unified Extensible Firmware Interface) rootkit known as LoJax . [5] [6] |
| G0096 | APT41 | APT41 deployed rootkits on Linux systems. [7] [8] |
| C0046 | ArcaneDoor | ArcaneDoor included hooking the processHostScanReply() function on victim Cisco ASA devices. [9] |
| S0484 | Carberp | Carberp has used user mode rootkit techniques to remain hidden on the system. [10] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell has a module to use a rootkit on a system. [11] |
| S1105 | COATHANGER | COATHANGER hooks or replaces multiple legitimate processes and other functions on victim devices. [12] |
| S0502 | Drovorub | Drovorub has used a kernel module rootkit to hide processes, files, executables, and network artifacts from user space view. [13] |
| S0377 | Ebury | Ebury acts as a user land rootkit using the SSH service. [14] [15] |
| S0047 | Hacking Team UEFI Rootkit | Hacking Team UEFI Rootkit is a UEFI BIOS rootkit developed by the company Hacking Team to persist remote access software on some targeted systems. [16] |
| S0394 | HiddenWasp | HiddenWasp uses a rootkit to hook and implement functions on the system. [17] |
| S0135 | HIDEDRV | HIDEDRV is a rootkit that hides certain operating system artifacts. [18] |
| S0009 | Hikit | Hikit is a Rootkit that has been used by Axiom . [19] [20] |
| S0601 | Hildegard | Hildegard has modified /etc/ld.so.preload to overwrite readdir() and readdir64(). [21] |
| S0040 | HTRAN | HTRAN can install a rootkit to hide network connections from the host OS. [22] |
| S1186 | Line Dancer | Line Dancer can hook both the crash dump process and the Autehntication, Authorization, and Accounting (AAA) functions on compromised machines to evade forensic analysis and authentication mechanisms. [9] |
| S0397 | LoJax | LoJax is a UEFI BIOS rootkit deployed to persist remote access software on some targeted systems. [6] |
| S1220 | MEDUSA | MEDUSA is a rootkit with command execution and credential logging capabilities. [23] |
| S0012 | PoisonIvy | PoisonIvy starts a rootkit from a malicious file dropped to disk. [24] |
| S0458 | Ramsay | Ramsay has included a rootkit to evade defenses. [25] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 used rootkits such as REPTILE and MEDUSA . [26] |
| S1219 | REPTILE | REPTILE has the ability to hook kernel functions and modify functions data to achieve rootkit functionality such as hiding processes and network connections. [23] |
| G0106 | Rocke | Rocke has modified /etc/ld.so.preload to hook libc functions in order to hide the installed dropper and mining software in process lists. [27] |
| S0468 | Skidmap | Skidmap is a kernel-mode rootkit that has the ability to hook system calls to hide specific files and fake network and CPU-related statistics to make the CPU load of the infected machine always appear low. [28] |
| S0603 | Stuxnet | Stuxnet uses a Windows rootkit to mask its binaries and other relevant files. [29] |
| G0139 | TeamTNT | TeamTNT has used rootkits such as the open-source Diamorphine rootkit and their custom bots to hide cryptocurrency mining activities on the machine. [30] [31] |
| S0221 | Umbreon | Umbreon hides from defenders by hooking libc function calls, hiding artifacts that would reveal its presence, such as the user account it creates to provide access and undermining strace, a tool often used to identify malware. [32] |
| G1048 | UNC3886 | UNC3886 has used the publicly available rootkits REPTILE and MEDUSA on targeted VMs. [23] |
| S0022 | Uroburos | Uroburos can use its kernel module to prevent its host components from being listed by the targeted system's OS and to mediate requests between user mode and concealed components. [33] [34] |
| S0670 | WarzoneRAT | WarzoneRAT can include a rootkit to hide processes, files, and startup. [35] |
| S0430 | Winnti for Linux | Winnti for Linux has used a modified copy of the open-source userland rootkit Azazel, named libxselinux.so, to hide the malware's operations and network activity. [36] |
| G0044 | Winnti Group | Winnti Group used a rootkit to modify typical server functionality. [37] |
| S0027 | Zeroaccess | Zeroaccess is a kernel-mode rootkit. [38] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0377 | Detection of Kernel/User-Level Rootkit Behavior Across Platforms | AN1061 | Unauthorized or anomalous loading of kernel-mode drivers or DLLs, concealed services, or abnormal modification of boot components indicative of rootkit activity. |
| AN1062 | Abnormal loading of kernel modules, direct tampering with /dev, /proc, or LD_PRELOAD behaviors hiding processes or files. |  |  |
| AN1063 | Execution of unsigned kernel extensions (KEXTs), tampering with LaunchDaemons, or userspace hooks into system libraries. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0377 | Detection of Kernel/User-Level Rootkit Behavior Across Platforms | AN1061 | Unauthorized or anomalous loading of kernel-mode drivers or DLLs, concealed services, or abnormal modification of boot components indicative of rootkit activity. |
| AN1062 | Abnormal loading of kernel modules, direct tampering with /dev, /proc, or LD_PRELOAD behaviors hiding processes or files. |  |  |
| AN1063 | Execution of unsigned kernel extensions (KEXTs), tampering with LaunchDaemons, or userspace hooks into system libraries. |  |  |

---

## References

- [Symantec. (n.d.). Windows Rootkit Overview. Retrieved December 21, 2017.](https://www.symantec.com/avcenter/reference/windows.rootkit.overview.pdf)
- [Wikipedia. (2016, June 1). Rootkit. Retrieved June 2, 2016.](https://en.wikipedia.org/wiki/Rootkit)
- [Kurtz, G. (2012, November 19). HTTP iframe Injecting Linux Rootkit. Retrieved December 21, 2017.](https://www.crowdstrike.com/blog/http-iframe-injecting-linux-rootkit/)
- [Pan, M., Tsai, S. (2014). You can’t see me: A Mac OS X Rootkit uses the tricks you haven't known yet. Retrieved December 21, 2017.](http://www.blackhat.com/docs/asia-14/materials/Tsai/WP-Asia-14-Tsai-You-Cant-See-Me-A-Mac-OS-X-Rootkit-Uses-The-Tricks-You-Havent-Known-Yet.pdf)
- [Symantec Security Response. (2018, October 04). APT28: New Espionage Operations Target Military and Government Organizations. Retrieved November 14, 2018.](https://www.symantec.com/blogs/election-security/apt28-espionage-military-government)
- [ESET. (2018, September). LOJAX First UEFI rootkit found in the wild, courtesy of the Sednit group. Retrieved July 2, 2019.](https://www.welivesecurity.com/wp-content/uploads/2018/09/ESET-LoJax.pdf)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [Crowdstrike. (2020, March 2). 2020 Global Threat Report. Retrieved December 11, 2020.](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)
- [Cisco Talos. (2024, April 24). ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices. Retrieved January 6, 2025.](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
- [Giuliani, M., Allievi, A. (2011, February 28). Carberp - a modular information stealing trojan. Retrieved September 12, 2024.](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Dutch Military Intelligence and Security Service (MIVD) & Dutch General Intelligence and Security Service (AIVD). (2024, February 6). Ministry of Defense of the Netherlands uncovers COATHANGER, a stealthy Chinese FortiGate RAT. Retrieved February 7, 2024.](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
- [NSA/FBI. (2020, August). Russian GRU 85th GTsSS Deploys Previously Undisclosed Drovorub Malware. Retrieved August 25, 2020.](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF)
- [Vachon, F. (2017, October 30). Windigo Still not Windigone: An Ebury Update . Retrieved February 10, 2021.](https://www.welivesecurity.com/2017/10/30/windigo-ebury-update-2/)
- [Marc-Etienne M.Léveillé. (2024, May 1). Ebury is alive but unseen. Retrieved May 21, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/ebury-is-alive-but-unseen.pdf)
- [Lin, P. (2015, July 13). Hacking Team Uses UEFI BIOS Rootkit to Keep RCS 9 Agent in Target Systems. Retrieved December 11, 2015.](http://blog.trendmicro.com/trendlabs-security-intelligence/hacking-team-uses-uefi-bios-rootkit-to-keep-rcs-9-agent-in-target-systems/)
- [Sanmillan, I. (2019, May 29). HiddenWasp Malware Stings Targeted Linux Systems. Retrieved June 24, 2019.](https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/)
- [ESET. (2016, October). En Route with Sednit - Part 3: A Mysterious Downloader. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part3.pdf)
- [Glyer, C., Kazanciyan, R. (2012, August 20). The “Hikit” Rootkit: Advanced and Persistent Attack Techniques (Part 1). Retrieved November 17, 2024.](https://web.archive.org/web/20190216180458/https://www.fireeye.com/blog/threat-research/2012/08/hikit-rootkit-advanced-persistent-attack-techniques-part-1.html)
- [Glyer, C., Kazanciyan, R. (2012, August 22). The “Hikit” Rootkit: Advanced and Persistent Attack Techniques (Part 2). Retrieved November 17, 2024.](https://web.archive.org/web/20210920172620/https://www.fireeye.com/blog/threat-research/2012/08/hikit-rootkit-advanced-persistent-attack-techniques-part-2.html)
- [Chen, J. et al. (2021, February 3). Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes. Retrieved April 5, 2021.](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [The Australian Cyber Security Centre (ACSC), the Canadian Centre for Cyber Security (CCCS), the New Zealand National Cyber Security Centre (NZ NCSC), CERT New Zealand, the UK National Cyber Security Centre (UK NCSC) and the US National Cybersecurity and Communications Integration Center (NCCIC). (2018, October 11). Joint report on publicly available hacking tools. Retrieved March 11, 2019.](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
- [Punsaen Boonyakarn, Shawn Chew, Logeswaran Nadarajan, Mathew Potaczek, Jakub Jozwiak, and Alex Marvi. (2024, June 18). Cloaked and Covert: Uncovering UNC3886 Espionage Operations. Retrieved September 24, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [Hayashi, K. (2005, August 18). Backdoor.Darkmoon. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Lamparski, L. et al. (2025, March 11). Ghost in the Router: China-Nexus Espionage Actor UNC3886 Targets Juniper Routers. Retrieved June 24, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers)
- [Anomali Labs. (2019, March 15). Rocke Evolves Its Arsenal With a New Malware Family Written in Golang. Retrieved April 24, 2019.](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)
- [Remillano, A., Urbanec, J. (2019, September 19). Skidmap Linux Malware Uses Rootkit Capabilities to Hide Cryptocurrency-Mining Payload. Retrieved June 4, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [Fiser, D. Oliveira, A. (n.d.). Tracking the Activities of TeamTNT A Closer Look at a Cloud-Focused Malicious Actor Group. Retrieved September 22, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-tracking-the-activities-of-teamTNT.pdf)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Fernando Mercês. (2016, September 5). Pokémon-themed Umbreon Linux Rootkit Hits x86, ARM Systems. Retrieved March 5, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/pokemon-themed-umbreon-linux-rootkit-hits-x86-arm-systems/?_ga=2.180041126.367598458.1505420282-1759340220.1502477046)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [FBI et al. (2023, May 9). Hunting Russian Intelligence “Snake” Malware. Retrieved June 8, 2023.](https://www.cisa.gov/sites/default/files/2023-05/aa23-129a_snake_malware_2.pdf)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [Chronicle Blog. (2019, May 15). Winnti: More than just Windows and Gates. Retrieved April 29, 2020.](https://medium.com/chronicle-blog/winnti-more-than-just-windows-and-gates-e4f03436031a)
- [Kaspersky Lab's Global Research and Analysis Team. (2013, April 11). Winnti. More than just a game. Retrieved February 8, 2017.](https://securelist.com/winnti-more-than-just-a-game/37029/)
- [Wyke, J. (2012, April). ZeroAccess. Retrieved July 18, 2016.](https://sophosnews.files.wordpress.com/2012/04/zeroaccess2.pdf)

---

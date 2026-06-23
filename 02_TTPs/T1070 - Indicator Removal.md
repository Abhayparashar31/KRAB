# Indicator Removal

## Description

Adversaries may selectively delete or modify artifacts generated to reduce indications of their presence and blend in with legitimate activity. Rather than broadly removing evidence, adversaries may target specific artifacts that appear anomalous or are likely to draw scrutiny, while leaving sufficient data intact to maintain the appearance of normal system behavior.

Artifacts such as command histories, log entries, or file metadata may be altered in ways that align with expected user or system activity. Location, format, and type of artifact (such as command or login history) are often platform-specific, allowing adversaries to tailor modifications that minimize suspicion.

These actions may not prevent detection entirely but can delay recognition of malicious activity or reduce the fidelity of alerts by making events appear benign or consistent with routine operations. Additionally, selectively removed or modified artifacts may still be recoverable through deeper forensic analysis, though their absence or alteration can complicate timeline reconstruction and attribution.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1044 | APT42 | APT42 has cleared Chrome browser history. [1] |
| G1023 | APT5 | APT5 has used the THINBLOOD utility to clear SSL VPN log files located at /home/runtime/logs . [2] [3] |
| S0239 | Bankshot | Bankshot deletes all artifacts associated with the malware from the infected machine. [4] |
| S0089 | BlackEnergy | BlackEnergy has removed the watermark associated with enabling the TESTSIGNING boot configuration option by removing the relevant strings in the user32.dll.mui of the system. [5] |
| S1161 | BPFDoor | BPFDoor clears the file location /proc/<PID>/environ removing all environment variables for the process. [6] |
| S0527 | CSPY Downloader | CSPY Downloader has the ability to remove values it writes to the Registry. [7] |
| C0029 | Cutting Edge | During Cutting Edge , threat actors cleared logs to remove traces of their activity and restored compromised systems to a clean state to bypass manufacturer mitigations for CVE-2023-46805 and CVE-2024-21887. [8] [9] |
| S0673 | DarkWatchman | DarkWatchman can uninstall malicious components from the Registry, stop processes, and clear the browser history. [10] |
| S0695 | Donut | Donut can erase file references to payloads in-memory after being reflectively loaded and executed. [11] |
| S1159 | DUSTTRAP | DUSTTRAP restores the .text section of compromised DLLs after malicious code is loaded into memory and before the file is closed. [12] |
| S0568 | EVILNUM | EVILNUM has a function called "DeleteLeftovers" to remove certain artifacts of the attack. [13] |
| S0696 | Flagpro | Flagpro can close specific Windows Security and Internet Explorer dialog boxes to mask external connections. [14] |
| S1044 | FunnyDream | FunnyDream has the ability to clean traces of malware deployment. [15] |
| S0697 | HermeticWiper | HermeticWiper can disable pop-up information about folders and desktop items and delete Registry keys to hide malicious services. [16] [17] |
| S1132 | IPsec Helper | IPsec Helper can delete various registry keys related to its execution and use. [18] |
| S9029 | IronWind | IronWind has used a .NET DLL named "exit-DN4-core.dll" to terminate malicious processes running on victim's systems. [19] |
| G0032 | Lazarus Group | Lazarus Group has restored malicious KernelCallbackTable code to its original state after the process execution flow has been hijacked. [20] |
| S0449 | Maze | Maze has used the "Wow64RevertWow64FsRedirection" function following attempts to delete the shadow volumes, in order to leave the system in the same state as it was prior to redirection. [21] |
| S0455 | Metamorfo | Metamorfo has a command to delete a Registry key it uses, \Software\Microsoft\Internet Explorer\notes . [22] |
| S1135 | MultiLayer Wiper | MultiLayer Wiper uses a batch script to clear file system cache memory via the ProcessIdleTasks export in advapi32.dll as an anti-analysis and anti-forensics technique. [23] |
| G0129 | Mustang Panda | Mustang Panda has deleted registry keys that store data and maintained persistence. [24] |
| S0691 | Neoichor | Neoichor can clear the browser history on a compromised host by changing the ClearBrowsingHistoryOnExit value to 1 in the HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Privacy Registry key. [25] |
| S0229 | Orz | Orz can overwrite Registry settings to reduce its visibility on the victim. [26] |
| S0332 | Remcos | Remcos can clean saved cookies and logins from the web browser. [27] |
| S0448 | Rising Sun | Rising Sun can clear a memory blog in the process by overwriting it with junk bytes. [28] |
| S1085 | Sardonic | Sardonic has the ability to delete created WMI objects to evade detections. [29] |
| S0461 | SDBbot | SDBbot has the ability to clean up and remove data structures from a compromised host. [30] |
| S0596 | ShadowPad | ShadowPad has deleted arbitrary Registry values. [31] |
| S0589 | Sibot | Sibot will delete an associated registry key if a certain server response is received. [32] |
| S0692 | SILENTTRINITY | SILENTTRINITY can remove artifacts from the compromised host, including created Registry keys. [33] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 temporarily replaced legitimate utilities with their own, executed their payload, and then restored the original file. [34] |
| S0603 | Stuxnet | Stuxnet can delete OLE Automation and SQL stored procedures used to store malicious payloads. [35] |
| S0559 | SUNBURST | SUNBURST removed HTTP proxy registry values to clean up traces of execution. [36] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1041 | Encrypt Sensitive Information | Obfuscate/encrypt event files locally and in transit to avoid giving feedback to an adversary. |
| M1029 | Remote Data Storage | Automatically forward events to a log server or data repository to prevent conditions in which the adversary can locate and manipulate data on the local system. When possible, minimize time delay on event reporting to avoid prolonged storage on the local system. |
| M1022 | Restrict File and Directory Permissions | Protect generated event files that are stored locally with proper permissions and authentication and limit opportunities for adversaries to increase privileges by preventing Privilege Escalation opportunities. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0184 | Behavioral Detection of Indicator Removal Across Platforms | AN0520 | Monitors sequences involving deletion/modification of logs, registry keys, scheduled tasks, or prefetch files following suspicious process activity or elevated access escalation. |
| AN0521 | Detects deletion or overwriting of bash history, syslog, audit logs, and .ssh metadata following privilege elevation or suspicious process spawning. |  |  |
| AN0522 | Detects clearing of unified logs, deletion of plist files tied to persistence, and manipulation of Terminal history after initial execution. |  |  |
| AN0523 | Monitors tampering with audit logs, volumes, or mounted storage often used for side-channel logging (e.g., /var/log inside containers) post-compromise. |  |  |
| AN0524 | Tracks suspicious use of ESXi shell commands or PowerCLI to delete logs, rotate system files, or tamper with hostd/vpxa history. |  |  |
| AN0525 | Detects deletion or hiding of security-related mail rules, audit mailboxes, or calendar/log sync artifacts indicative of tampering post-intrusion. |  |  |

---

## References

- [Rozmann, O., et al. (2024, May 1). Uncharmed: Untangling Iran's APT42 Operations. Retrieved October 9, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)
- [Perez, D. et al. (2021, April 20). Check Your Pulse: Suspected APT Actors Leverage Authentication Bypass Techniques and Pulse Secure Zero-Day. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
- [Perez, D. et al. (2021, May 27). Re-Checking Your Pulse: Updates on Chinese APT Actors Compromising Pulse Secure VPN Devices. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/updates-on-chinese-apt-compromising-pulse-secure-vpn-devices)
- [US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
- [F-Secure Labs. (2014). BlackEnergy & Quedagh: The convergence of crimeware and APT attacks. Retrieved March 24, 2016.](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
- [The Sandfly Security Team. (2022, May 11). BPFDoor - An Evasive Linux Backdoor Technical Analysis. Retrieved September 29, 2023.](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/)
- [Dahan, A. et al. (2020, November 2). Back to the Future: Inside the Kimsuky KGH Spyware Suite. Retrieved November 6, 2020.](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
- [Lin, M. et al. (2024, January 31). Cutting Edge, Part 2: Investigating Ivanti Connect Secure VPN Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
- [Meltzer, M. et al. (2024, January 10). Active Exploitation of Two Zero-Day Vulnerabilities in Ivanti Connect Secure VPN. Retrieved February 27, 2024.](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [TheWover. (2019, May 9). donut. Retrieved March 25, 2022.](https://github.com/TheWover/donut)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Adamitis, D. (2020, May 6). Phantom in the Command Shell. Retrieved November 17, 2024.](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Thomas, W. et al. (2022, February 25). CrowdStrike Falcon Protects from New Wiper Malware Used in Ukraine Cyberattacks. Retrieved March 25, 2022.](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
- [ESET. (2022, March 1). IsaacWiper and HermeticWizard: New wiper and worm targetingUkraine. Retrieved April 10, 2022.](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [Check Point. (2024, November 12). Hamas-affiliated Threat Actor WIRTE Continues its Middle East Operations and Moves to Disruptive Activity. Retrieved April 20, 2026.](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
- [Saini, A. and Hossein, J. (2022, January 27). North Korea’s Lazarus APT leverages Windows Update client, GitHub in latest campaign. Retrieved January 27, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)
- [Mundo, A. (2020, March 26). Ransomware Maze. Retrieved May 18, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
- [Sierra, E., Iglesias, G.. (2018, April 24). Metamorfo Campaigns Targeting Brazilian Users. Retrieved July 30, 2020.](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [Budaca, E., et al. (2021, August 25). FIN8 Threat Actor Goes Agile with New Sardonic Backdoor. Retrieved August 9, 2023.](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
- [Schwarz, D. et al. (2019, October 16). TA505 Distributes New SDBbot Remote Access Trojan with Get2 Downloader. Retrieved May 29, 2020.](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
- [Kaspersky Lab. (2017, August). ShadowPad: popular server management software hit in supply chain attack. Retrieved March 22, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [MSTIC, CDOC, 365 Defender Research Team. (2021, January 20). Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop . Retrieved January 22, 2021.](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)

---

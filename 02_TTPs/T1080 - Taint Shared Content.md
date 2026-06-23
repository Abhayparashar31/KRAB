# Taint Shared Content

## Description

Adversaries may deliver payloads to remote systems by adding content to shared storage locations, such as network drives or internal code repositories. Content stored on network drives or in other shared locations may be tainted by adding malicious programs, scripts, or exploit code to otherwise valid files. Once a user opens the shared tainted content, the malicious portion can be executed to run the adversary's code on a remote system. Adversaries may use tainted shared content to move laterally.

A directory share pivot is a variation on this technique that uses several other techniques to propagate malware when users access a shared network directory. It uses Shortcut Modification of directory .LNK files that use Masquerading to look like the real directories, which are hidden through Hidden Files and Directories . The malicious .LNK-based directories have an embedded command that executes the hidden malware file in the directory and then opens the real intended directory so that the user's expected action still occurs. When used with frequently used network directories, the technique may result in frequent reinfections and broad access to systems and potentially to new and higher privileged accounts. [1]

Adversaries may also compromise shared network directories through binary infections by appending or prepending its code to the healthy binary on the shared network directory. The malware may modify the original entry point (OEP) of the healthy binary to ensure that it is executed before the legitimate code. The infection could continue to spread via the newly infected file when it is executed by a remote system. These infections may target both binary and non-binary formats that end with extensions including, but not limited to, .EXE, .DLL, .SCR, .BAT, and/or .VBS.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0060 | BRONZE BUTLER | BRONZE BUTLER has placed malware on file shares and given it the same name as legitimate documents on the share. [2] |
| G1021 | Cinnamon Tempest | Cinnamon Tempest has deployed ransomware from a batch file in a network share. [3] |
| S0575 | Conti | Conti can spread itself by infecting other remote machines via network shared drives. [4] [5] |
| G0012 | Darkhotel | Darkhotel used a virus that propagates by infecting executables stored on shared drives. [6] |
| G0047 | Gamaredon Group | Gamaredon Group has injected malicious macros into all Word and Excel documents on mapped network drives. [7] |
| S0132 | H1N1 | H1N1 has functionality to copy itself to network shares. [8] |
| S0260 | InvisiMole | InvisiMole can replace legitimate software or documents in the compromised network with their trojanized versions, in an attempt to propagate itself within the network. [9] |
| S0133 | Miner-C | Miner-C copies itself into the public folder of Network Attached Storage (NAS) devices and infects new victims who open the file. [10] |
| S0458 | Ramsay | Ramsay can spread itself by infecting other portable executable files on networks shared drives. [11] |
| G1039 | RedCurl | RedCurl has placed modified LNK files on network drives for lateral movement. [12] [13] |
| S0603 | Stuxnet | Stuxnet infects remote servers via network shares and by infecting WinCC database views with malicious code. [14] |
| S0386 | Ursnif | Ursnif has copied itself to and infected files in network drives for propagation. [15] [16] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1049 | Antivirus/Antimalware | Anti-virus can be used to automatically quarantine suspicious files. [17] |
| M1038 | Execution Prevention | Identify potentially malicious software that may be used to taint content or may result from it and audit and/or block the unknown programs by using application control [18] tools, like AppLocker, [19] [20] or Software Restriction Policies [21] where appropriate. [22] |
| M1050 | Exploit Protection | Use utilities that detect or mitigate common features used in exploitation, such as the Microsoft Enhanced Mitigation Experience Toolkit (EMET). |
| M1022 | Restrict File and Directory Permissions | Protect shared folders by minimizing users who have write access. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0471 | Detection of Tainted Content Written to Shared Storage | AN1298 | Detects adversary tampering of shared directories via file drops (e.g., malicious LNK, EXE, VBS) followed by user execution or suspicious network activity. |
| AN1299 | Detects script or binary modification within shared NFS/SMB directories followed by process execution from those paths. |  |  |
| AN1300 | Detects modification of shared network folders via .app bundles or scripting files with hidden extensions (e.g., double extensions like docx.app). |  |  |
| AN1301 | Detects upload of malicious or unusual file types into cloud-shared folders, followed by user downloads or interactions. |  |  |
| AN1302 | Detects embedded macros or scripts added to shared documents or use of external references to execute code. |  |  |

---

## References

- [Routin, D. (2017, November 13). Abusing network shares for efficient lateral movements and privesc (DirSharePivot). Retrieved April 12, 2018.](https://rewtin.blogspot.ch/2017/11/abusing-user-shares-for-efficient.html)
- [Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)
- [Microsoft. (2022, May 9). Ransomware as a service: Understanding the cybercrime gig economy and how to protect yourself. Retrieved March 10, 2023.](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)
- [Rochberger, L. (2021, January 12). Cybereason vs. Conti Ransomware. Retrieved February 17, 2021.](https://www.cybereason.com/blog/cybereason-vs.-conti-ransomware)
- [Baskin, B. (2020, July 8). TAU Threat Discovery: Conti Ransomware. Retrieved February 17, 2021.](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, November). The Darkhotel APT A Story of Unusual Hospitality. Retrieved November 12, 2014.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070903/darkhotel_kl_07.11.pdf)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Reynolds, J.. (2016, September 14). H1N1: Technical analysis reveals new capabilities – part 2. Retrieved November 17, 2024.](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Cimpanu, C.. (2016, September 9). Cryptocurrency Mining Malware Discovered Targeting Seagate NAS Hard Drives. Retrieved September 12, 2024.](https://news.softpedia.com/news/cryptocurrency-mining-malware-discovered-targeting-seagate-nas-hard-drives-508119.shtml)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Group-IB. (2020, August). RedCurl: The Pentest You Didn’t Know About. Retrieved August 9, 2024.](https://www.group-ib.com/resources/research-hub/red-curl/)
- [Group-IB. (2021, November). RedCurl: The Awakening. Retrieved August 14, 2024.](https://www.group-ib.com/resources/research-hub/red-curl-2/)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [Caragay, R. (2015, March 26). URSNIF: The Multifaceted Malware. Retrieved June 5, 2019.](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
- [Caragay, R. (2014, December 11). Info-Stealing File Infector Hits US, UK. Retrieved June 5, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/info-stealing-file-infector-hits-us-uk/)
- [Pany, D. & Hanley, C. (2023, May 3). Cloudy with a Chance of Bad Logs: Cloud Platform Log Configurations to Consider in Investigations. Retrieved October 16, 2023.](https://www.mandiant.com/resources/blog/cloud-bad-log-configurations)
- [Beechey, J. (2010, December). Application Whitelisting: Panacea or Propaganda?. Retrieved November 18, 2014.](http://www.sans.org/reading-room/whitepapers/application/application-whitelisting-panacea-propaganda-33599)
- [Tomonaga, S. (2016, January 26). Windows Commands Abused by Attackers. Retrieved February 2, 2016.](https://blogs.jpcert.or.jp/en/2016/01/windows-commands-abused-by-attackers.html)
- [NSA Information Assurance Directorate. (2014, August). Application Whitelisting Using Microsoft AppLocker. Retrieved March 31, 2016.](https://apps.nsa.gov/iaarchive/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
- [Corio, C., & Sayana, D. P. (2008, June). Application Lockdown with Software Restriction Policies. Retrieved September 12, 2024.](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc510322(v=msdn.10))
- [Microsoft. (2012, June 27). Using Software Restriction Policies and AppLocker Policies. Retrieved April 7, 2016.](https://technet.microsoft.com/en-us/library/ee791851.aspx)

---

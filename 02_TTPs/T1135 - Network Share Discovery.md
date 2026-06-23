# Network Share Discovery

## Description

Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network.

File sharing over a Windows network occurs over the SMB protocol. [1] [2] Net can be used to query a remote system for available shared drives using the net view \\remotesystem command. It can also be used to query shared drives on the local system using net share . For macOS, the sharing -l command lists all shared points used for smb services.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1129 | Akira | Akira can identify remote file shares for encryption. [3] |
| G0006 | APT1 | APT1 listed connected network shares. [4] |
| G0050 | APT32 | APT32 used the net view command to show all shares available, including the administrative shares such as C$ and ADMIN$ . [5] |
| G0082 | APT38 | APT38 has enumerated network shares on a compromised host. [6] |
| G0087 | APT39 | APT39 has used the post exploitation tool CrackMapExec to enumerate network shares. [7] |
| G0096 | APT41 | APT41 used the net share command as part of network reconnaissance. [8] [9] |
| S0640 | Avaddon | Avaddon has enumerated shared folders and mapped volumes. [10] |
| S1053 | AvosLocker | AvosLocker has enumerated shared drives on a compromised network. [11] [12] |
| S0638 | Babuk | Babuk has the ability to enumerate network shares. [13] |
| S0606 | Bad Rabbit | Bad Rabbit enumerates open SMB shares on internal victim networks. [14] |
| S1081 | BADHATCH | BADHATCH can check a user's access to the C$ share on a compromised machine. [15] |
| S0534 | Bazar | Bazar can enumerate shared drives on the domain. [16] |
| S0570 | BitPaymer | BitPaymer can search for network shares on the domain or workgroup using net view . [17] |
| G1043 | BlackByte | BlackByte enumerated network shares on victim devices. [18] |
| S1181 | BlackByte 2.0 Ransomware | BlackByte 2.0 Ransomware can identify network shares connected to the victim machine. [19] |
| S1180 | BlackByte Ransomware | BlackByte Ransomware can identify network shares connected to the victim machine. [20] |
| S1068 | BlackCat | BlackCat has the ability to discover network shares on compromised networks. [21] [22] |
| C0015 | C0015 | During C0015 , the threat actors executed the PowerView ShareFinder module to identify open shares. [23] |
| G0114 | Chimera | Chimera has used net share and net view to identify network shares of interest. [24] |
| S0660 | Clambling | Clambling has the ability to enumerate network shares. [25] |
| S0611 | Clop | Clop can enumerate network shares. [26] |
| S0154 | Cobalt Strike | Cobalt Strike can query shared drives on the local system. [27] |
| S0575 | Conti | Conti can enumerate remote open SMB network shares using NetShareEnum() . [28] [29] |
| S0488 | CrackMapExec | CrackMapExec can enumerate the shared folders and associated permissions for a targeted network. [30] |
| S0625 | Cuba | Cuba can discover shared resources using the NetShareEnum API call. [31] |
| G0105 | DarkVishnya | DarkVishnya scanned the network for public shared folders. [32] |
| S0616 | DEATHRANSOM | DEATHRANSOM has the ability to use loop operations to enumerate network resources. [33] |
| S0659 | Diavol | Diavol has a ENMDSKS command to enumerates available network shares. [34] |
| G0035 | Dragonfly | Dragonfly has identified and browsed file servers in the victim network, sometimes , viewing files pertaining to ICS or Supervisory Control and Data Acquisition (SCADA) systems. [35] |
| S1159 | DUSTTRAP | DUSTTRAP can identify and enumerate victim system network shares. [36] |
| S1247 | Embargo | Embargo has searched for folders, subfolders and other networked or mounted drives for follow-on encryption actions. [37] |
| S0367 | Emotet | Emotet has enumerated non-hidden network shares using WNetEnumResourceW . [38] |
| S0363 | Empire | Empire can find shared drives on the local system. [39] |
| G1016 | FIN13 | FIN13 has executed net view commands for enumeration of open shares on compromised machines. [40] [41] |
| S0618 | FIVEHANDS | FIVEHANDS can enumerate network shares and mounted drives on a network. [42] |
| S0696 | Flagpro | Flagpro has been used to execute net view to discover mapped network shares. [43] |
| S0617 | HELLOKITTY | HELLOKITTY has the ability to enumerate network resources. [33] |
| S0483 | IcedID | IcedID has used the net view /all command to show available shares. [44] |
| G1032 | INC Ransom | INC Ransom has used Internet Explorer to view folders on other systems. [45] |
| S1139 | INC Ransomware | INC Ransomware has the ability to check for shared network drives to encrypt. [46] |
| S0260 | InvisiMole | InvisiMole can gather network share information. [47] |
| S0250 | Koadic | Koadic can scan local network for open SMB. [48] |
| S1075 | KOPILUWAK | KOPILUWAK can use netstat and Net to discover network shares. [49] |
| S0236 | Kwampirs | Kwampirs collects a list of network shares with the command net share . [50] |
| S1160 | Latrodectus | Latrodectus can run C:\Windows\System32\cmd.exe /c net view /all to discover network shares. [51] [52] |
| C0049 | Leviathan Australian Intrusions | Leviathan scanned and enumerated remote network shares in victim environments during Leviathan Australian Intrusions . [53] |
| S1199 | LockBit 2.0 | LockBit 2.0 can discover remote shares. [54] |
| S1202 | LockBit 3.0 | LockBit 3.0 can identify network shares on compromised systems. [55] |
| S1141 | LunarWeb | LunarWeb can identify shared resources in compromised environments. [56] |
| G1051 | Medusa Group | Medusa Group has identified network shares using cmd.exe /c net share . [57] |
| S1244 | Medusa Ransomware | Medusa Ransomware has identified networked drives. [58] [59] [60] |
| S0233 | MURKYTOP | MURKYTOP has the capability to retrieve information about shares on remote hosts. [61] |
| S0039 | Net | The net view \remotesystem and net share commands in Net can be used to find shared drives and directories on remote and local systems respectively. [62] |
| S0365 | Olympic Destroyer | Olympic Destroyer will attempt to enumerate mapped network shares to later attempt to wipe all files on those shares. [63] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors used the net share command as part of their advanced reconnaissance. [64] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors discovered network disks mounted to the system using netstat . [65] |
| S0165 | OSInfo | OSInfo discovers shares on the network [66] |
| S0013 | PlugX | PlugX has a module to enumerate network shares. [67] [68] |
| S0192 | Pupy | Pupy can list local and remote shared drives and folders over SMB. [69] |
| S0650 | QakBot | QakBot can use net share to identify network shares for use in lateral movement. [70] [71] |
| S1242 | Qilin | Qilin has the ability to list network drives. [72] [73] |
| S0686 | QuietSieve | QuietSieve can identify and search networked drives for specific file name extensions. [74] |
| S0458 | Ramsay | Ramsay can scan for network drives which may contain documents for collection. [75] [76] |
| S1212 | RansomHub | RansomHub has the ability to target specific network shares for encryption. [77] |
| S1073 | Royal | Royal can enumerate the shared resources of a given IP addresses using the API call NetShareEnum . [78] |
| S1085 | Sardonic | Sardonic has the ability to execute the net view command. [79] |
| S0444 | ShimRat | ShimRat can enumerate connected drives for infected host machines. [80] |
| S0692 | SILENTTRINITY | SILENTTRINITY can enumerate shares on a compromised host. [81] |
| G0054 | Sowbug | Sowbug listed remote shared drives that were accessible from a victim. [82] |
| S0603 | Stuxnet | Stuxnet enumerates the directories of a network resource. [83] |
| G0131 | Tonto Team | Tonto Team has used tools such as NBTscan to enumerate network shares. [84] |
| S0266 | TrickBot | TrickBot module shareDll/mshareDll discovers network shares via the WNetOpenEnumA API. [85] [86] |
| G0081 | Tropic Trooper | Tropic Trooper used netview to scan target systems for shared resources. [87] |
| S0612 | WastedLocker | WastedLocker can identify network adjacent and accessible drives. [88] |
| S0689 | WhisperGate | WhisperGate can enumerate connected remote logical drives. [89] |
| G0102 | Wizard Spider | Wizard Spider has used the "net view" command to locate mapped network shares. [90] |
| S0251 | Zebrocy | Zebrocy identifies network drives when they are added to victim systems. [91] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1028 | Operating System Configuration | Enable Windows Group Policy "Do Not Allow Anonymous Enumeration of SAM Accounts and Shares" security setting to limit users who can enumerate network shares. [92] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0182 | Behavior-chain detection for T1135 Network Share Discovery across Windows, Linux, and macOS | AN0513 | Process or script enumerates network shares via CLI (net view/net share, PowerShell Get-SmbShare/WMI) or OS APIs (NetShareEnum/ srvsvc.NetShareEnumAll RPC) → bursts of outbound SMB/RPC connections (445/139, \host\IPC$ / srvsvc) to many hosts inside a short window → optional follow-on file listing or copy operations. |
| AN0514 | CLI tools (smbclient -L, smbmap, rpcclient, nmblookup) or custom scripts enumerate SMB shares on many internal hosts → corresponding SMB connections (445/139) captured by Zeek/Netflow within a short window. |  |  |
| AN0515 | Use of native/mac tools (sharing -l, smbutil view, mount_smbfs) or scripts to enumerate SMB shares across many hosts, followed by outbound SMB connections observed in PF/Zeek logs. |  |  |

---

## References

- [Wikipedia. (2017, April 15). Shared resource. Retrieved June 30, 2017.](https://en.wikipedia.org/wiki/Shared_resource)
- [Microsoft. (n.d.). Share a Folder or Drive. Retrieved June 30, 2017.](https://technet.microsoft.com/library/cc770880.aspx)
- [Max Kersten & Alexandre Mundo. (2023, November 29). Akira Ransomware. Retrieved April 4, 2024.](https://www.trellix.com/blogs/research/akira-ransomware/)
- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [DHS/CISA. (2020, August 26). FASTCash 2.0: North Korea's BeagleBoyz Robbing Banks. Retrieved September 29, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)
- [Rusu, B. (2020, May 21). Iranian Chafer APT Targeted Air Transportation and Government in Kuwait and Saudi Arabia. Retrieved May 22, 2020.](https://www.bitdefender.com/blog/labs/iranian-chafer-apt-targeted-air-transportation-and-government-in-kuwait-and-saudi-arabia/)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [Rostovcev, N. (2021, June 10). Big airline heist APT41 likely behind a third-party attack on Air India. Retrieved August 26, 2021.](https://www.group-ib.com/blog/colunmtk-apt41/)
- [Yuste, J. Pastrana, S. (2021, February 9). Avaddon ransomware: an in-depth analysis and decryption of infected systems. Retrieved August 19, 2021.](https://arxiv.org/pdf/2102.04796.pdf)
- [Hasherezade. (2021, July 23). AvosLocker enters the ransomware scene, asks for partners. Retrieved January 11, 2023.](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
- [FBI, FinCEN, Treasury. (2022, March 17). Indicators of Compromise Associated with AvosLocker Ransomware. Retrieved January 11, 2023.](https://www.ic3.gov/Media/News/2022/220318.pdf)
- [Sogeti. (2021, March). Babuk Ransomware. Retrieved August 11, 2021.](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
- [M.Léveille, M-E.. (2017, October 24). Bad Rabbit: Not‑Petya is back with improved ransomware. Retrieved January 28, 2021.](https://www.welivesecurity.com/2017/10/24/bad-rabbit-not-petya-back/)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1, 2020.](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
- [Frankoff, S., Hartley, B. (2018, November 14). Big Game Hunting: The Evolution of INDRIK SPIDER From Dridex Wire Fraud to BitPaymer Targeted Ransomware. Retrieved January 6, 2021.](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
- [James Nutland, Craig Jackson, Terryn Valikodath, & Brennan Evans. (2024, August 28). BlackByte blends tried-and-true tradecraft with newly disclosed vulnerabilities to support ongoing attacks. Retrieved December 16, 2024.](https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [Brandt, Andrew. (2022, July 14). BlackCat ransomware attacks not merely a byproduct of bad luck. Retrieved December 20, 2022.](https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Mundo, A. (2019, August 1). Clop Ransomware. Retrieved May 10, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
- [Cobalt Strike. (2017, December 8). Tactics, Techniques, and Procedures. Retrieved November 17, 2024.](https://web.archive.org/web/20210924171429/https://www.cobaltstrike.com/downloads/reports/tacticstechniquesandprocedures.pdf)
- [Baskin, B. (2020, July 8). TAU Threat Discovery: Conti Ransomware. Retrieved February 17, 2021.](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [Podlosky, A., Hanel, A. et al. (2020, October 16). WIZARD SPIDER Update: Resilient, Reactive and Resolute. Retrieved June 15, 2021.](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)
- [byt3bl33d3r. (2018, September 8). SMB: Command Reference. Retrieved July 17, 2020.](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [Golovanov, S. (2018, December 6). DarkVishnya: Banks attacked through direct connection to local network. Retrieved May 15, 2020.](https://securelist.com/darkvishnya/89169/)
- [McLellan, T. and Moore, J. et al. (2021, April 29). UNC2447 SOMBRAT and FIVEHANDS Ransomware: A Sophisticated Financial Threat. Retrieved June 2, 2021.](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Cyble. (2024, May 24). The Rust Revolution: New Embargo Ransomware Steps In. Retrieved October 19, 2025.](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
- [Binary Defense. (n.d.). Emotet Evolves With new Wi-Fi Spreader. Retrieved September 8, 2023.](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [Sygnia Incident Response Team. (2022, January 5). TG2003: ELEPHANT BEETLE UNCOVERING AN ORGANIZED FINANCIAL-THEFT OPERATION. Retrieved February 9, 2023.](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)
- [Matthews, M. and Backhouse, W. (2021, June 15). Handy guide to a new Fivehands ransomware variant. Retrieved June 24, 2021.](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [DFIR. (2022, April 25). Quantum Ransomware. Retrieved July 26, 2024.](https://thedfirreport.com/2022/04/25/quantum-ransomware/)
- [Team Huntress. (2023, August 11). Investigating New INC Ransom Group Activity. Retrieved June 5, 2024.](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Magius, J., et al. (2017, July 19). Koadic. Retrieved September 27, 2024.](https://github.com/offsecginger/koadic)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
- [Stepanic, D. and Bousseaden, S. (2024, May 15). Spring Cleaning with LATRODECTUS: A Potential Replacement for ICEDID. Retrieved September 13, 2024.](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
- [Batista, J. (2024, June 17). Latrodectus, are you coming back?. Retrieved September 13, 2024.](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
- [CISA et al. (2024, July 8). People’s Republic of China (PRC) Ministry of State Security APT40 Tradecraft in Action. Retrieved February 3, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a)
- [FBI. (2022, February 4). Indicators of Compromise Associated with LockBit 2.0 Ransomware. Retrieved January 24, 2025.](https://www.ic3.gov/CSA/2022/220204.pdf)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)
- [Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Computer Incident Response Center Luxembourg. (2013, March 29). Analysis of a PlugX variant. Retrieved November 5, 2018.](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
- [Nicolas Verdier. (n.d.). Retrieved January 29, 2018.](https://github.com/n1nj4sec/pupy)
- [Mendoza, E. et al. (2020, May 25). Qakbot Resurges, Spreads through VBS Files. Retrieved September 27, 2021.](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [Magdy, S. et al. (2022, August 25). New Golang Ransomware Agenda Customizes Attacks. Retrieved September 26, 2025.](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
- [Halcyon RISE Team. (2024, October 24). New Qilin.B Ransomware Variant Boasts Enhanced Encryption and Defense Evasion. Retrieved September 26, 2025.](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
- [Microsoft Threat Intelligence Center. (2022, February 4). ACTINIUM targets Ukrainian organizations. Retrieved February 18, 2022.](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Antiy CERT. (2020, April 20). Analysis of Ramsay components of Darkhotel's infiltration and isolation network. Retrieved March 24, 2021.](https://www.programmersought.com/article/62493896999/)
- [Alfano, V. et al. (2025, February 12). RansomHub Never Sleeps Episode 1: The evolution of modern ransomware. Retrieved March 17, 2025.](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
- [Cybereason Global SOC and Cybereason Security Research Teams. (2022, December 14). Royal Rumble: Analysis of Royal Ransomware. Retrieved March 30, 2023.](https://www.cybereason.com/blog/royal-ransomware-analysis)
- [Budaca, E., et al. (2021, August 25). FIN8 Threat Actor Goes Agile with New Sardonic Backdoor. Retrieved August 9, 2023.](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [Symantec Security Response. (2017, November 7). Sowbug: Cyber espionage group targets South American and Southeast Asian governments. Retrieved November 16, 2017.](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [Daniel Lughi, Jaromir Horejsi. (2020, October 2). Tonto Team - Exploring the TTPs of an advanced threat actor operating a large infrastructure. Retrieved October 17, 2021.](https://vb2020.vblocalhost.com/uploads/VB2020-06.pdf)
- [Boutin, J. (2020, October 12). ESET takes part in global operation to disrupt Trickbot. Retrieved March 15, 2021.](https://www.welivesecurity.com/2020/10/12/eset-takes-part-global-operation-disrupt-trickbot/)
- [Tudorica, R., Maximciuc, A., Vatamanu, C. (2020, March 18). New TrickBot Module Bruteforces RDP Connections, Targets Select Telecommunication Services in US and Hong Kong. Retrieved March 15, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/316/Bitdefender-Whitepaper-TrickBot-en-EN-interactive.pdf)
- [Alintanahin, K. (2015). Operation Tropic Trooper: Relying on Tried-and-Tested Flaws to Infiltrate Secret Keepers. Retrieved June 14, 2019.](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)
- [Walter, J.. (2020, July 23). WastedLocker Ransomware: Abusing ADS and NTFS File Attributes. Retrieved September 14, 2021.](https://www.sentinelone.com/labs/wastedlocker-ransomware-abusing-ads-and-ntfs-file-attributes/)
- [Biasini, N. et al.. (2022, January 21). Ukraine Campaign Delivers Defacement and Wipers, in Continued Escalation. Retrieved March 14, 2022.](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
- [DHS/CISA. (2020, October 28). Ransomware Activity Targeting the Healthcare and Public Health Sector. Retrieved October 28, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-302a)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, February 20). A Slice of 2017 Sofacy Activity. Retrieved November 27, 2018.](https://securelist.com/a-slice-of-2017-sofacy-activity/83930/)
- [Microsoft. (2017, April 19). Network access: Do not allow anonymous enumeration of SAM accounts and shares. Retrieved May 20, 2020.](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-access-do-not-allow-anonymous-enumeration-of-sam-accounts-and-shares)

---

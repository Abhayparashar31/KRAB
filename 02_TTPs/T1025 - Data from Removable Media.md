# Data from Removable Media

## Description

Adversaries may search connected removable media on computers they have compromised to find files of interest. Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised system prior to Exfiltration. Interactive command shells may be in use, and common functionality within cmd may be used to gather information.

Some adversaries may also use Automated Collection on removable media.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0622 | AppleSeed | AppleSeed can find and collect data from removable media devices. [1] [2] |
| G0007 | APT28 | An APT28 backdoor may collect the entire contents of an inserted USB device. [3] |
| S0456 | Aria-body | Aria-body has the ability to collect data from USB devices. [4] |
| S0128 | BADNEWS | BADNEWS copies files with certain extensions from USB devices to a predefined directory. [5] |
| S0050 | CosmicDuke | CosmicDuke steals user files from removable media with file extensions and keywords that match a predefined list. [6] |
| S0115 | Crimson | Crimson contains a module to collect data from removable drives. [7] [8] |
| S0538 | Crutch | Crutch can monitor removable drives and exfiltrate files matching a given extension list. [9] |
| S0569 | Explosive | Explosive can scan all .exe files located in the USB drive. [10] |
| S0036 | FLASHFLOOD | FLASHFLOOD searches for interesting files (either a default or customized set of file extensions) on removable media and copies them to a staging area. The default file types copied would include data copied to the drive by SPACESHIP . [11] |
| S1044 | FunnyDream | The FunnyDream FilePakMonitor component has the ability to collect files from removable devices. [12] |
| G0047 | Gamaredon Group | A Gamaredon Group file stealer has the capability to steal data from newly connected logical volumes on a system, including USB drives. [13] [14] [15] |
| S0237 | GravityRAT | GravityRAT steals files based on an extension list if a USB drive is connected to the system. [16] |
| S0260 | InvisiMole | InvisiMole can collect jpeg files from connected MTP devices. [17] |
| S0409 | Machete | Machete can find, encrypt, and upload files from fixed and removable drives. [18] [19] |
| S1146 | MgBot | MgBot includes modules capable of gathering information from USB thumb drives and CD-ROMs on the victim machine given a list of provided criteria. [20] |
| S0644 | ObliqueRAT | ObliqueRAT has the ability to extract data from removable devices connected to the endpoint. [21] |
| G0049 | OilRig | OilRig has used Wireshark’s usbcapcmd utility to capture USB traffic. [22] |
| S0113 | Prikormka | Prikormka contains a module that collects documents with certain extensions from removable media or fixed drives connected via USB. [23] |
| S0458 | Ramsay | Ramsay can collect data from removable media and stage it for exfiltration. [24] |
| S0125 | Remsec | Remsec has a package that collects documents from any inserted USB sticks. [25] |
| S0090 | Rover | Rover searches for files on attached removable drives based on a predefined list of file extensions every five seconds. [26] |
| S0467 | TajMahal | TajMahal has the ability to steal written CD images and files of interest from previously connected removable drives when they become available again. [27] |
| G0010 | Turla | Turla RPC backdoors can collect files from USB thumb drives. [28] [29] |
| S0136 | USBStealer | Once a removable media device is inserted back into the first victim, USBStealer collects data from it that was exfiltrated from a second victim. [30] [31] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1057 | Data Loss Prevention | Data loss prevention can restrict access to sensitive data and detect sensitive data that is unencrypted. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0511 | Detection of Data Access and Collection from Removable Media | AN1410 | Adversary mounts a USB device and begins enumerating, copying, or compressing files using scripting engines, cmd, or remote access tools. |
| AN1411 | Adversary mounts external drive to /media or /mnt then accesses or copies targeted data via shell, cp, or tar. |  |  |
| AN1412 | Adversary attaches USB drive and accesses sensitive files using Finder, cp, or bash scripts. |  |  |

---

## References

- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [KISA. (2021). Phishing Target Reconnaissance and Attack Resource Analysis Operation Muzabi. Retrieved March 8, 2024.](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
- [Anthe, C. et al. (2015, October 19). Microsoft Security Intelligence Report Volume 19. Retrieved December 23, 2015.](http://download.microsoft.com/download/4/4/C/44CDEF0E-7924-4787-A56A-16261691ACE3/Microsoft_Security_Intelligence_Report_Volume_19_English.pdf)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
- [F-Secure Labs. (2014, July). COSMICDUKE Cosmu with a twist of MiniDuke. Retrieved July 3, 2014.](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [Faou, M. (2020, December 2). Turla Crutch: Keeping the “back door” open. Retrieved December 4, 2020.](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
- [Threat Intelligence and Research. (2015, March 30). VOLATILE CEDAR. Retrieved February 8, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
- [FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved November 17, 2024.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Kasza, A. and Reichel, D. (2017, February 27). The Gamaredon Group Toolset Evolution. Retrieved March 1, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [The Cylance Threat Research Team. (2017, March 22). El Machete's Malware Attacks Cut Through LATAM. Retrieved September 13, 2019.](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [Facundo Muñoz. (2023, April 26). Evasive Panda APT group delivers malware via updates for popular Chinese software. Retrieved July 25, 2024.](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)
- [Malhotra, A. (2021, March 2). ObliqueRAT returns with new campaign using hijacked websites. Retrieved September 2, 2021.](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
- [Symantec Threat Hunter Team. (2023, October 19). Crambus: New Campaign Targets Middle Eastern Government. Retrieved November 27, 2024.](https://www.security.com/threat-intelligence/crambus-middle-east-government)
- [Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
- [Ray, V., Hayashi, K. (2016, February 29). New Malware ‘Rover’ Targets Indian Ambassador to Afghanistan. Retrieved February 29, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [Symantec DeepSight Adversary Intelligence Team. (2019, June 20). Waterbug: Espionage Group Rolls Out Brand-New Toolset in Attacks Against Governments. Retrieved July 8, 2019.](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)
- [Calvet, J. (2014, November 11). Sednit Espionage Group Attacking Air-Gapped Networks. Retrieved January 4, 2017.](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
- [Kaspersky Lab's Global Research and Analysis Team. (2015, December 4). Sofacy APT hits high profile targets with updated toolset. Retrieved December 10, 2015.](https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/)

---

# Local Storage Discovery

## Description

Adversaries may enumerate local drives, disks, and/or volumes and their attributes like total or free space and volume serial number. This can be done to prepare for ransomware-related encryption, to perform Lateral Movement , or as a precursor to Direct Volume Access .

On ESXi systems, adversaries may use Hypervisor CLI commands such as esxcli to list storage connected to the host as well as .vmdk files. [1] [2]

On Windows systems, adversaries can use wmic logicaldisk get to find information about local network drives. They can also use Get-PSDrive in PowerShell to retrieve drives and may additionally use Windows API functions such as GetDriveType . [3] [4]

Linux has commands such as parted , lsblk , fdisk , lshw , and df that can list information about disk partitions such as size, type, file system types, and free space. The command diskutil on MacOS can be used to list disks while system_profiler SPStorageDataType can additionally show information such as a volume’s mount path, file system, and the type of drive in the system.

Infrastructure as a Service (IaaS) cloud providers also have commands for storage discovery such as describe volume in AWS, gcloud compute disks list in GCP, and az disk list in Azure. [5] [6] [7]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0456 | Aria-body | Aria-body has the ability to identify disk information on a compromised host. [8] |
| S9031 | AshTag | AshTag can use volumeserialnumber to enumerate volumes. [9] |
| S1087 | AsyncRAT | AsyncRAT can check the disk size through the values obtained with DeviceInfo. [10] |
| S0438 | Attor | Attor monitors the free disk space on the system. [11] |
| S0473 | Avenger | Avenger has the ability to identify the host volume ID. [12] |
| S0638 | Babuk | Babuk can enumerate disk volumes, get disk information, and query service status. [13] |
| S0234 | Bandook | Bandook can collect information about the drives available on the system. [14] |
| S0239 | Bankshot | Bankshot gathers disk type and disk free space. [15] [16] |
| S1070 | Black Basta | Black Basta can enumerate volumes. [17] [18] |
| S1068 | BlackCat | BlackCat can enumerate local drives. [19] |
| S0564 | BlackMould | BlackMould can enumerate local drives on a compromised host. [20] |
| S0520 | BLINDINGCAN | BLINDINGCAN has collected disk information, including type and free space available. [21] |
| S0471 | build_downer | build_downer has the ability to send system volume information to C2. [12] |
| C0017 | C0017 | During C0017 , APT41 issued ping -n 1 ((cmd /c dir c:\|findstr Number).split()[-1]+ commands to find the volume serial number of compromised systems. [22] |
| S0351 | Cannon | Cannon can gather drive information from the victim's machine. [23] [24] |
| G0114 | Chimera | Chimera has used fsutil fsinfo drives , systeminfo , and vssadmin list shadows for system information including shadow volumes and drive information. [25] |
| S0667 | Chrommme | Chrommme has the ability to list drives. [26] |
| G0142 | Confucius | Confucius has used a file stealer that can examine system drives, including those other than the C drive. [27] |
| S0137 | CORESHELL | CORESHELL collects the volume serial number from the victim and sends the information to its C2 server. [28] |
| S0488 | CrackMapExec | CrackMapExec can enumerate the system drives and associated system name. [29] |
| S0115 | Crimson | Crimson contains a command to collect disk drive information. [30] [31] [32] |
| S0625 | Cuba | Cuba can enumerate local drives, disk type, and disk free space. [33] |
| S1111 | DarkGate | DarkGate uses the Delphi methods Sysutils::DiskSize and GlobalMemoryStatusEx to collect disk size and physical memory as part of the malware's anti-analysis checks for running in a virtualized environment. [34] |
| S0616 | DEATHRANSOM | DEATHRANSOM can enumerate logical drives on a target system. [35] |
| S0472 | down_new | down_new has the ability to identify the system volume information of a compromised host. [12] |
| S9038 | DynoWiper | DynoWiper has used the Microsoft Windows native GetLogicalDrives() and GetDriveType() functions to enumerate all the drives visible to the system. [36] |
| S0091 | Epic | Epic collects disk space information. [37] |
| S0181 | FALLCHILL | FALLCHILL can collect information about installed disks from the victim. [38] |
| S0267 | FELIXROOT | FELIXROOT collects the victim’s volume serial number. [39] [40] |
| S1044 | FunnyDream | FunnyDream can enumerate all logical drives on a targeted machine. [41] |
| S0617 | HELLOKITTY | HELLOKITTY can enumerate logical drives on a target system. [35] |
| S0697 | HermeticWiper | HermeticWiper can enumerate physical drives on a targeted host. [42] [43] [44] [45] |
| S1027 | Heyoka Backdoor | Heyoka Backdoor can enumerate drives on a compromised host. [46] |
| G0126 | Higaisa | Higaisa collected the system volume serial number. [47] [48] |
| S0376 | HOPLIGHT | HOPLIGHT has been observed collecting victim machine volume information. [49] |
| S1139 | INC Ransomware | INC Ransomware can discover and mount hidden drives to encrypt them. [50] |
| S0259 | InnaputRAT | InnaputRAT gathers volume drive information. [51] |
| S0260 | InvisiMole | InvisiMole can gather information on the mapped drives and system volume serial number. [52] [53] |
| S0044 | JHUHUGIT | JHUHUGIT obtains a build identifier as well as victim hard drive information from Windows registry key HKLM\SYSTEM\CurrentControlSet\Services\Disk\Enum . Another JHUHUGIT variant gathers the victim storage volume serial number and the storage device name. [54] [55] |
| S0265 | Kazuar | Kazuar gathers information on local drives. [56] |
| S0271 | KEYMARBLE | KEYMARBLE has the capability to collect information on disk devices. [57] |
| S0526 | KGH_SPY | KGH_SPY can collect drive information from a compromised host. [58] |
| S0607 | KillDisk | KillDisk retrieves the hard disk name by calling the CreateFileA to \.\PHYSICALDRIVE0 API. [59] |
| G0094 | Kimsuky | Kimsuky has enumerated drives. [60] [61] [62] |
| S0356 | KONNI | KONNI can gather information on connected drives and disk space from the victim’s machine. [63] [64] [65] |
| S1075 | KOPILUWAK | KOPILUWAK can discover logical drive information on compromised hosts. [66] |
| G0032 | Lazarus Group | A Destover-like variant used by Lazarus Group collects disk space information and sends it to its C2 server. [67] [68] [69] [70] [71] [72] |
| S0680 | LitePower | LitePower has the ability to list local drives. [73] |
| S1199 | LockBit 2.0 | LockBit 2.0 can enumerate local drive configuration. [74] [75] |
| S1202 | LockBit 3.0 | LockBit 3.0 can enumerate local drive configuration. [76] |
| S1016 | MacMa | MacMa can collect information about a compromised computer's disk sizes. [77] |
| S1048 | macOS.OSAMiner | macOS.OSAMiner has checked to ensure there is enough disk space using the Unix utility df . [78] |
| S1060 | Mafalda | Mafalda can enumerate all drives on a compromised host. [79] [80] |
| S1244 | Medusa Ransomware | Medusa Ransomware has enumerated logical drives on infected hosts. [81] |
| S1026 | Mongall | Mongall can identify drives on compromised hosts. [46] |
| S0630 | Nebulae | Nebulae can discover logical drive information including the drive type, free space, and volume information. [82] |
| S1147 | Nightdoor | Nightdoor can collect information about disk drives, their total and free space, and file system type. [83] |
| S1100 | Ninja | Ninja can obtain information on physical drives from targeted hosts. [84] [85] |
| S0353 | NOKKI | NOKKI can gather information on drives on the victim’s machine. [86] |
| S0340 | Octopus | Octopus can collect system drive and disk size information. [87] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors discovered the local disks attached to the system and their hardware information including manufacturer and model. [88] |
| S0208 | Pasam | Pasam creates a backdoor through which remote attackers can retrieve information like free disk space. [89] |
| G0040 | Patchwork | Patchwork enumerated all available drives on the victim's machine. [90] [91] |
| S0587 | Penquin | Penquin can report the disk space of a compromised host to C2. [92] |
| S0013 | PlugX | PlugX has collected a list of all mapped drives on the infected host. [93] |
| S0238 | Proxysvc | Proxysvc collects volume information for all drives on the system. [71] |
| S1228 | PUBLOAD | PUBLOAD has leveraged wmic logicaldisk get to map local network drives. [3] |
| S1242 | Qilin | Qilin has used GetLogicalDrives() and EnumResourceW() to locate mounted drives and shares. [94] |
| S0458 | Ramsay | Ramsay can detect system information--including disk names, total space, and remaining space--to create a hardware profile GUID which acts as a system identifier for operators. [95] [96] |
| S0172 | Reaver | Reaver collects volume serial number from the victim. [97] |
| S0496 | REvil | REvil can identify system drive information on a compromised host. [98] [99] [100] [101] [101] [102] [103] [104] |
| S0448 | Rising Sun | Rising Sun can detect drive information, including drive type, total number of bytes on disk, total number of free bytes on disk, and name of a specified volume. [105] |
| S1150 | ROADSWEEP | ROADSWEEP can enumerate logical drives on targeted devices. [106] [107] |
| S1073 | Royal | Royal can use GetLogicalDrives to enumerate logical drives. [108] [109] |
| S0253 | RunningRAT | RunningRAT gathers logical drives information and volume information. [110] |
| S0446 | Ryuk | Ryuk has called GetLogicalDrives to emumerate all mounted drives, and GetDriveTypeW to determine the drive type. [111] |
| S1168 | SampleCheck5000 | SampleCheck5000 can create unique victim identifiers by using the compromised system’s volume ID. [112] |
| S1085 | Sardonic | Sardonic has the ability to collect the C:\ drive serial number from a compromised machine. [113] |
| S0596 | ShadowPad | ShadowPad has discovered system information including volume serial numbers. [114] |
| S1089 | SharpDisco | SharpDisco can use a plugin to enumerate system drives. [115] |
| S0692 | SILENTTRINITY | SILENTTRINITY can collect information related to a compromised host, including a list of drives. [116] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA has collected disk information from a victim machine. [117] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 used fsutil to check available free space before executing actions that might create large files on disk. [118] |
| S0516 | SoreFang | SoreFang can collect disk space information on victim machines by executing Systeminfo . [119] |
| S0491 | StrongPity | StrongPity can identify the hard disk volume serial number on a compromised host. [120] |
| S1049 | SUGARUSH | MoonWind can obtain the number of drives on the victim machine. [121] |
| S0663 | SysUpdate | SysUpdate can collect a system's drive information. [122] [123] |
| S0586 | TAINTEDSCRIBE | TAINTEDSCRIBE can use DriveList to retrieve drive information. [124] |
| G0139 | TeamTNT | TeamTNT has searched for disk partition and logical volume information. [125] [126] |
| G1022 | ToddyCat | ToddyCat has collected information on bootable drives including model, vendor, and serial numbers. [85] |
| S1239 | TONESHELL | TONESHELL has retrieved the disk serial number of the device using WMI query SELECT volumeserialnumber FROM win32_logicaldisk where Name =’C: to identify the victim machine. [127] |
| S0678 | Torisma | Torisma can use GetlogicalDrives to get a bitmask of all drives available on a compromised system. It can also use GetDriveType to determine if a new drive is a CD-ROM drive. [128] |
| G0081 | Tropic Trooper | Tropic Trooper has detected a target system’s system volume information. [129] [130] |
| S0263 | TYPEFRAME | TYPEFRAME can gather the disk volume information. [131] |
| G1017 | Volt Typhoon | Volt Typhoon has discovered file system types, drive names, size, and free space on compromised systems. [132] [133] [134] [135] |
| S0689 | WhisperGate | WhisperGate has the ability to enumerate fixed logical drives on a targeted system. [136] |
| S1065 | Woody RAT | Woody RAT can retrieve information about storage drives from an infected machine. [137] |
| S0248 | yty | yty gathers the the serial number of the main disk volume. [138] |
| S0251 | Zebrocy | Zebrocy collects the serial number for the storage volume C:. [139] [23] [140] [24] [141] [142] [143] |
| S1151 | ZeroCleare | ZeroCleare can use the IOCTL_DISK_GET_DRIVE_GEOMETRY_EX , IOCTL_DISK_GET_DRIVE_GEOMETRY , and IOCTL_DISK_GET_LENGTH_INFO system calls to compute disk size. [106] |
| S0672 | Zox | Zox can enumerate attached drives. [144] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0188 | Local Storage Discovery via Drive Enumeration and Filesystem Probing | AN0536 | Drive enumeration using PowerShell ( Get-PSDrive ), wmic logicaldisk , or Win32 API indicative of local volume enumeration by non-admin users or executed outside of baseline system inventory scripts. |
| AN0537 | Abnormal use of lsblk , fdisk -l , lshw -class disk , or parted by non-admin users or within non-interactive shells suggests suspicious disk enumeration activity. |  |  |
| AN0538 | Disk enumeration via diskutil list or system_profiler SPStorageDataType run outside of user login or not associated with system inventory tools |  |  |
| AN0539 | Use of esxcli storage or vim-cmd vmsvc/getallvms by unusual sessions or through interactive shells unrelated to administrative maintenance tasks. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0188 | Local Storage Discovery via Drive Enumeration and Filesystem Probing | AN0536 | Drive enumeration using PowerShell ( Get-PSDrive ), wmic logicaldisk , or Win32 API indicative of local volume enumeration by non-admin users or executed outside of baseline system inventory scripts. |
| AN0537 | Abnormal use of lsblk , fdisk -l , lshw -class disk , or parted by non-admin users or within non-interactive shells suggests suspicious disk enumeration activity. |  |  |
| AN0538 | Disk enumeration via diskutil list or system_profiler SPStorageDataType run outside of user login or not associated with system inventory tools |  |  |
| AN0539 | Use of esxcli storage or vim-cmd vmsvc/getallvms by unusual sessions or through interactive shells unrelated to administrative maintenance tasks. |  |  |

---

## References

- [Mina Naiim. (2021, May 28). DarkSide on Linux: Virtual Machines Targeted. Retrieved March 26, 2025.](https://www.trendmicro.com/en_us/research/21/e/darkside-linux-vms-targeted.html)
- [Junestherry Dela Cruz. (2022, January 24). Analysis and Impact of LockBit Ransomware’s First Linux and VMware ESXi Variant. Retrieved March 26, 2025.](https://www.trendmicro.com/en_us/research/22/a/analysis-and-Impact-of-lockbit-ransomwares-first-linux-and-vmware-esxi-variant.html)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Ankur Saini, Charlie Gardner. (2023, June 28). Charming Kitten Updates POWERSTAR with an InterPlanetary Twist. Retrieved September 25, 2025.](https://www.volexity.com/blog/2023/06/28/charming-kitten-updates-powerstar-with-an-interplanetary-twist/)
- [AWS. (n.d.). describe-volumes. Retrieved October 20, 2025.](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volumes.html)
- [Google Cloud. (n.d.). gcloud compute disks list. Retrieved October 20, 2025.](https://cloud.google.com/sdk/gcloud/reference/compute/disks/list)
- [Azure. (n.d.). az disk. Retrieved October 20, 2025.](https://learn.microsoft.com/en-us/cli/azure/disk?view=azure-cli-latest)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Unit 42. (2025, December 11). Hamas-Affiliated Ashen Lepus Targets Middle Eastern Diplomatic Entities With New AshTag Malware Suite. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
- [Jornet, A. (2021, December 23). Snip3, an investigation into malware. Retrieved September 19, 2023.](https://telefonicatech.com/blog/snip3-investigacion-malware)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [Mundo, A. et al. (2021, February). Technical Analysis of Babuk Ransomware. Retrieved August 11, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
- [Check Point. (2020, November 26). Bandook: Signed & Delivered. Retrieved May 31, 2021.](https://research.checkpoint.com/2020/bandook-signed-delivered/)
- [Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
- [US-CERT. (2017, December 13). Malware Analysis Report (MAR) - 10135536-B. Retrieved July 17, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-B_WHITE.PDF)
- [Zargarov, N. (2022, May 2). New Black Basta Ransomware Hijacks Windows Fax Service. Retrieved March 7, 2023.](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
- [Cyble. (2022, May 6). New ransomware variant targeting high-value organizations. Retrieved November 17, 2024.](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [MSTIC. (2019, December 12). GALLIUM: Targeting global telecom. Retrieved January 13, 2021.](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)
- [US-CERT. (2020, August 19). MAR-10295134-1.v1 – North Korean Remote Access Trojan: BLINDINGCAN. Retrieved August 19, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Falcone, R., Lee, B. (2018, November 20). Sofacy Continues Global Attacks and Wheels Out New ‘Cannon’ Trojan. Retrieved November 26, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
- [Lee, B., Falcone, R. (2018, December 12). Dear Joohn: The Sofacy Group’s Global Campaign. Retrieved April 19, 2019.](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Lunghi, D. (2021, August 17). Confucius Uses Pegasus Spyware-related Lures to Target Pakistani Military. Retrieved December 26, 2021.](https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html)
- [FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
- [byt3bl33d3r. (2018, September 8). SMB: Command Reference. Retrieved July 17, 2020.](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [N. Baisini. (2022, July 13). Transparent Tribe begins targeting education sector in latest campaign. Retrieved September 22, 2022.](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [McLellan, T. and Moore, J. et al. (2021, April 29). UNC2447 SOMBRAT and FIVEHANDS Ransomware: A Sophisticated Financial Threat. Retrieved June 2, 2021.](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2014, August 06). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroboros. Retrieved November 7, 2018.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
- [US-CERT. (2017, November 22). Alert (TA17-318A): HIDDEN COBRA – North Korean Remote Administration Tool: FALLCHILL. Retrieved December 7, 2017.](https://www.us-cert.gov/ncas/alerts/TA17-318A)
- [Patil, S. (2018, June 26). Microsoft Office Vulnerabilities Used to Distribute FELIXROOT Backdoor in Recent Campaign. Retrieved November 17, 2024.](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
- [Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Guerrero-Saade, J. (2022, February 23). HermeticWiper | New Destructive Malware Used In Cyber Attacks on Ukraine. Retrieved March 25, 2022.](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
- [Thomas, W. et al. (2022, February 25). CrowdStrike Falcon Protects from New Wiper Malware Used in Ukraine Cyberattacks. Retrieved March 25, 2022.](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
- [ESET. (2022, March 1). IsaacWiper and HermeticWizard: New wiper and worm targetingUkraine. Retrieved April 10, 2022.](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
- [Dani, M. (2022, March 1). Ukrainian Targets Hit by HermeticWiper, New Datawiper Malware. Retrieved March 25, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [PT ESC Threat Intelligence. (2020, June 4). COVID-19 and New Year greetings: an investigation into the tools and methods used by the Higaisa group. Retrieved March 2, 2021.](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/covid-19-and-new-year-greetings-the-higaisa-group/)
- [Malwarebytes Threat Intelligence Team. (2020, June 4). New LNK attack tied to Higaisa APT discovered. Retrieved March 2, 2021.](https://blog.malwarebytes.com/threat-analysis/2020/06/higaisa/)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [ASERT Team. (2018, April 04). Innaput Actors Utilize Remote Access Trojan Since 2016, Presumably Targeting Victim Files. Retrieved July 9, 2018.](https://asert.arbornetworks.com/innaput-actors-utilize-remote-access-trojan-since-2016-presumably-targeting-victim-files/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [ESET. (2016, October). En Route with Sednit - Part 1: Approaching the Target. Retrieved November 8, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part1.pdf)
- [Lee, B, et al. (2018, February 28). Sofacy Attacks Multiple Government Entities. Retrieved March 15, 2018.](https://researchcenter.paloaltonetworks.com/2018/02/unit42-sofacy-attacks-multiple-government-entities/)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [US-CERT. (2018, August 09). MAR-10135536-17 – North Korean Trojan: KEYMARBLE. Retrieved August 16, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
- [Dahan, A. et al. (2020, November 2). Back to the Future: Inside the Kimsuky KGH Spyware Suite. Retrieved November 6, 2020.](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
- [Fernando Merces, Byron Gelera, Martin Co. (2018, June 7). KillDisk Variant Hits Latin American Finance Industry. Retrieved January 12, 2021.](https://www.trendmicro.com/en_us/research/18/f/new-killdisk-variant-hits-latin-american-financial-organizations-again.html)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [Tarakanov , D.. (2013, September 11). The “Kimsuky” Operation: A North Korean APT?. Retrieved August 13, 2019.](https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Rascagneres, P. (2017, May 03). KONNI: A Malware Under The Radar For Years. Retrieved November 5, 2018.](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
- [Karmi, D. (2020, January 4). A Look Into Konni 2019 Campaign. Retrieved April 28, 2020.](https://medium.com/d-hunter/a-look-into-konni-2019-campaign-b45a0f321e9b)
- [Threat Intelligence Team. (2021, August 23). New variant of Konni malware used in campaign targetting Russia. Retrieved January 5, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved November 17, 2024.](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)
- [Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)
- [Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
- [Saini, A. and Hossein, J. (2022, January 27). North Korea’s Lazarus APT leverages Windows Update client, GitHub in latest campaign. Retrieved January 27, 2022.](https://blog.malwarebytes.com/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign/)
- [Yamout, M. (2021, November 29). WIRTE’s campaign in the Middle East ‘living off the land’ since at least 2019. Retrieved February 1, 2022.](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
- [FBI. (2022, February 4). Indicators of Compromise Associated with LockBit 2.0 Ransomware. Retrieved January 24, 2025.](https://www.ic3.gov/CSA/2022/220204.pdf)
- [Elsad, A. et al. (2022, June 9). LockBit 2.0: How This RaaS Operates and How to Protect Against It. Retrieved January 24, 2025.](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Phil Stokes. (2021, January 11). FADE DEAD | Adventures in Reversing Malicious Run-Only AppleScripts. Retrieved September 29, 2022.](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Vrabie, V. (2021, April 23). NAIKON – Traces from a Military Cyber-Espionage Operation. Retrieved June 29, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
- [Ahn Ho, Facundo Muñoz, & Marc-Etienne M.Léveillé. (2024, March 7). Evasive Panda leverages Monlam Festival to target Tibetans. Retrieved July 25, 2024.](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [Grunzweig, J., Lee, B. (2018, September 27). New KONNI Malware attacking Eurasia and Southeast Asia. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 15). Octopus-infested seas of Central Asia. Retrieved November 14, 2018.](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Mullaney, C. & Honda, H. (2012, May 4). Trojan.Pasam. Retrieved February 22, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-050412-4128-99)
- [Cymmetria. (2016). Unveiling Patchwork - The Copy-Paste APT. Retrieved November 17, 2024.](https://web.archive.org/web/20180825085952/https:/s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf)
- [Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
- [Leonardo. (2020, May 29). MALWARE TECHNICAL INSIGHT TURLA “Penquin_x64”. Retrieved March 11, 2021.](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Halcyon RISE Team. (2024, October 24). New Qilin.B Ransomware Variant Boasts Enhanced Encryption and Defense Evasion. Retrieved September 26, 2025.](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Antiy CERT. (2020, April 20). Analysis of Ramsay components of Darkhotel's infiltration and isolation network. Retrieved March 24, 2021.](https://www.programmersought.com/article/62493896999/)
- [Grunzweig, J. and Miller-Osborn, J. (2017, November 10). New Malware with Ties to SunOrcal Discovered. Retrieved November 16, 2017.](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)
- [Mamedov, O, et al. (2019, July 3). Sodin ransomware exploits Windows vulnerability and processor architecture. Retrieved August 4, 2020.](https://securelist.com/sodin-ransomware/91473/)
- [Cylance. (2019, July 3). hreat Spotlight: Sodinokibi Ransomware. Retrieved August 4, 2020.](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
- [Secureworks . (2019, September 24). REvil: The GandCrab Connection. Retrieved August 4, 2020.](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
- [McAfee. (2019, October 2). McAfee ATR Analyzes Sodinokibi aka REvil Ransomware-as-a-Service – What The Code Tells Us. Retrieved August 4, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
- [Intel 471 Malware Intelligence team. (2020, March 31). REvil Ransomware-as-a-Service – An analysis of a ransomware affiliate operation. Retrieved August 4, 2020.](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
- [Group IB. (2020, May). Ransomware Uncovered: Attackers’ Latest Methods. Retrieved August 5, 2020.](https://www.group-ib.com/whitepapers/ransomware-uncovered.html)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [MSTIC. (2022, September 8). Microsoft investigates Iranian attacks against the Albanian government. Retrieved August 6, 2024.](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)
- [Cybereason Global SOC and Cybereason Security Research Teams. (2022, December 14). Royal Rumble: Analysis of Royal Ransomware. Retrieved March 30, 2023.](https://www.cybereason.com/blog/royal-ransomware-analysis)
- [Morales, N. et al. (2023, February 20). Royal Ransomware Expands Attacks by Targeting Linux ESXi Servers. Retrieved March 30, 2023.](https://www.trendmicro.com/en_us/research/23/b/royal-ransomware-expands-attacks-by-targeting-linux-esxi-servers.html)
- [Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
- [Hanel, A. (2019, January 10). Big Game Hunting with Ryuk: Another Lucrative Targeted Ransomware. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
- [Hromcova, Z. and Burgher, A. (2023, December 14). OilRig’s persistent attacks using cloud service-powered downloaders. Retrieved November 26, 2024.](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
- [Budaca, E., et al. (2021, August 25). FIN8 Threat Actor Goes Agile with New Sardonic Backdoor. Retrieved August 9, 2023.](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
- [Kaspersky Lab. (2017, August). ShadowPad: popular server management software hit in supply chain attack. Retrieved March 22, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [MSTIC, CDOC, 365 Defender Research Team. (2021, January 20). Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop . Retrieved January 22, 2021.](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
- [CISA. (2020, July 16). MAR-10296782-1.v1 – SOREFANG. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
- [Mercer, W. et al. (2020, June 29). PROMETHIUM extends global reach with StrongPity3 APT. Retrieved July 20, 2020.](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
- [Miller-Osborn, J. and Grunzweig, J.. (2017, March 30). Trochilus and New MoonWind RATs Used In Attack Against Thai Organizations. Retrieved March 30, 2017.](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
- [Lunghi, D. and Lu, K. (2021, April 9). Iron Tiger APT Updates Toolkit With Evolved SysUpdate Malware. Retrieved November 12, 2021.](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
- [Daniel Lunghi. (2023, March 1). Iron Tiger’s SysUpdate Reappears, Adds Linux Targeting. Retrieved March 20, 2023.](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
- [USG. (2020, May 12). MAR-10288834-2.v1 – North Korean Trojan: TAINTEDSCRIBE. Retrieved March 5, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
- [AT&T Alien Labs. (2021, September 8). TeamTNT with new campaign aka Chimaera. Retrieved September 22, 2021.](https://cybersecurity.att.com/blogs/labs-research/teamtnt-with-new-campaign-aka-chimaera)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Ken Towne, Francis Guibernau. (2023, March 23). Emulating the Politically Motivated Chinese APT Mustang Panda. Retrieved September 10, 2025.](https://www.attackiq.com/2023/03/23/emulating-the-politically-motivated-chinese-apt-mustang-panda/)
- [Beek, C. (2020, November 5). Operation North Star: Behind The Scenes. Retrieved December 20, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
- [Alintanahin, K. (2015). Operation Tropic Trooper: Relying on Tried-and-Tested Flaws to Infiltrate Secret Keepers. Retrieved June 14, 2019.](https://documents.trendmicro.com/assets/wp/wp-operation-tropic-trooper.pdf)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [US-CERT. (2018, June 14). MAR-10135536-12 – North Korean Trojan: TYPEFRAME. Retrieved July 13, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-165A)
- [Microsoft Threat Intelligence. (2023, May 24). Volt Typhoon targets US critical infrastructure with living-off-the-land techniques. Retrieved July 27, 2023.](https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/)
- [NSA et al. (2023, May 24). People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection. Retrieved July 27, 2023.](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)
- [Counter Threat Unit Research Team. (2023, May 24). Chinese Cyberespionage Group BRONZE SILHOUETTE Targets U.S. Government and Defense Organizations. Retrieved July 27, 2023.](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Biasini, N. et al.. (2022, January 21). Ukraine Campaign Delivers Defacement and Wipers, in Continued Escalation. Retrieved March 14, 2022.](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Schwarz, D., Sopko J. (2018, March 08). Donot Team Leverages New Modular Malware Framework in South Asia. Retrieved June 11, 2018.](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
- [Lee, B., Falcone, R. (2018, June 06). Sofacy Group’s Parallel Attacks. Retrieved June 18, 2018.](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)
- [ESET. (2018, November 20). Sednit: What’s going on with Zebrocy?. Retrieved February 12, 2019.](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
- [ESET Research. (2019, May 22). A journey to Zebrocy land. Retrieved June 20, 2019.](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
- [Accenture Security. (2018, November 29). SNAKEMACKEREL. Retrieved April 15, 2019.](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
- [CISA. (2020, October 29). Malware Analysis Report (AR20-303B). Retrieved December 9, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
- [Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)

---

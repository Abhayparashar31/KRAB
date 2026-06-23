# Inhibit System Recovery

## Description

Adversaries may delete or remove built-in data and turn off services designed to aid in the recovery of a corrupted system to prevent recovery. [1] [2] This may deny access to available backups and recovery options.

Operating systems may contain features that can help fix corrupted systems, such as a backup catalog, volume shadow copies, and automatic repair features. Adversaries may disable or delete system recovery features to augment the effects of Data Destruction and Data Encrypted for Impact . [1] [2] Furthermore, adversaries may disable recovery notifications, then corrupt backups. [3]

A number of native Windows utilities have been used by adversaries to disable or delete system recovery features:

On network devices, adversaries may leverage Disk Wipe to delete backup firmware images and reformat the file system, then System Shutdown/Reboot to reload the device. Together this activity may leave network devices completely inoperable and inhibit recovery operations.

On ESXi servers, adversaries may delete or encrypt snapshots of virtual machines to support Data Encrypted for Impact , preventing them from being leveraged as backups (e.g., via vim-cmd vmsvc/snapshot.removeall ). [6]

Adversaries may also delete "online" backups that are connected to their network – whether via network storage media or through folders that sync to cloud services. [7] In cloud environments, adversaries may disable versioning and backup policies and delete snapshots, database backups, machine images, and prior versions of objects designed to be used in disaster recovery scenarios. [8] [9]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries deleted Windows Volume Shadow Copies using vssadmin delete shadows . [10] |
| S1129 | Akira | Akira will delete system volume shadow copies via PowerShell commands. [11] [12] |
| S0640 | Avaddon | Avaddon deletes backups and shadow copies using native system tools. [13] [14] |
| S0638 | Babuk | Babuk has the ability to delete shadow volumes using vssadmin.exe delete shadows /all /quiet . [15] [16] |
| S1136 | BFG Agonizer | BFG Agonizer wipes the boot sector of infected machines to inhibit system recovery. [17] |
| S0570 | BitPaymer | BitPaymer attempts to remove the backup shadow files from the host using vssadmin.exe Delete Shadows /All /Quiet . [18] |
| S1070 | Black Basta | Black Basta can delete shadow copies using vssadmin.exe. [19] [20] [21] [22] [23] [24] [25] [26] [26] [27] |
| G1043 | BlackByte | BlackByte resized and deleted volume shadow copy files to prevent system recovery after encryption. [28] [29] |
| S1181 | BlackByte 2.0 Ransomware | BlackByte 2.0 Ransomware modifies volume shadow copies during execution in a way that destroys them on the victim machine. [30] |
| S1180 | BlackByte Ransomware | BlackByte Ransomware deletes all volume shadow copies and restore points among other actions to inhibit system recovery following ransomware deployment. [31] |
| S1068 | BlackCat | BlackCat can delete shadow copies using vssadmin.exe delete shadows /all /quiet and wmic.exe Shadowcopy Delete ; it can also modify the boot loader using bcdedit /set {default} recoveryenabled No . [32] |
| S0611 | Clop | Clop can delete the shadow volumes with vssadmin Delete Shadows /all /quiet and can use bcdedit to disable recovery options. [33] |
| S0608 | Conficker | Conficker resets system restore points and deletes backup files. [34] |
| S0575 | Conti | Conti can delete Windows Volume Shadow Copies using vssadmin . [35] |
| S1111 | DarkGate | DarkGate can delete system restore points through the command cmd.exe /c vssadmin delete shadows /for=c: /all /quiet" . [36] |
| S0673 | DarkWatchman | DarkWatchman can delete shadow volumes using vssadmin.exe . [37] |
| S0616 | DEATHRANSOM | DEATHRANSOM can delete volume shadow copies on compromised hosts. [38] |
| S0659 | Diavol | Diavol can delete shadow copies using the IVssBackupComponents COM object to call the DeleteSnapshots method. [39] |
| S0605 | EKANS | EKANS removes backups of Volume Shadow Copies to disable any restoration capabilities. [40] [41] |
| S1247 | Embargo | Embargo has cleared files from the recycle bin by invoking SHEmptyRecycleBinW() and disabled Windows recovery through C:\Windows\System32\cmd.exe /q /c bcdedit /set {default} recoveryenabled no . [42] |
| S0618 | FIVEHANDS | FIVEHANDS has the ability to delete volume shadow copies on compromised hosts. [38] [43] |
| S0132 | H1N1 | H1N1 disable recovery options and deletes shadow copies from the victim. [44] |
| S0617 | HELLOKITTY | HELLOKITTY can delete volume shadow copies on compromised hosts. [38] |
| S0697 | HermeticWiper | HermeticWiper can disable the VSS service on a compromised host using the service control manager. [45] [46] [47] |
| S1139 | INC Ransomware | INC Ransomware can delete volume shadow copy backups from victim machines. [48] |
| S0260 | InvisiMole | InvisiMole can can remove all system restore points. [49] |
| S0389 | JCry | JCry has been observed deleting shadow copies to ensure that data cannot be restored easily. [50] |
| S1199 | LockBit 2.0 | LockBit 2.0 has the ability to delete volume shadow copies on targeted hosts. [51] [52] |
| S1202 | LockBit 3.0 | LockBit 3.0 can delete volume shadow copies. [53] [54] [55] |
| S0449 | Maze | Maze has attempted to delete the shadow volumes of infected machines, once before and once after the encryption process. [56] [57] |
| G1051 | Medusa Group | Medusa Group has deleted recovery files such as shadow copies using vssadmin.exe . [58] [59] [60] [61] |
| S1244 | Medusa Ransomware | Medusa Ransomware has deleted recovery files such as shadow copies using vssadmin.exe . [58] [59] [60] [61] |
| S0576 | MegaCortex | MegaCortex has deleted volume shadow copies using vssadmin.exe . [62] |
| S0688 | Meteor | Meteor can use bcdedit to delete different boot identifiers on a compromised host; it can also use vssadmin.exe delete shadows /all /quiet and C:\\Windows\\system32\\wbem\\wmic.exe shadowcopy delete . [63] |
| S1135 | MultiLayer Wiper | MultiLayer Wiper wipes the boot sector of infected systems to inhibit system recovery. [17] |
| S0457 | Netwalker | Netwalker can delete the infected system's Shadow Volumes to prevent recovery. [64] [65] |
| S0365 | Olympic Destroyer | Olympic Destroyer uses the native Windows utilities vssadmin , wbadmin , and bcdedit to delete and disable operating system recovery features such as the Windows backup catalog and Windows Automatic Repair. [1] |
| S1162 | Playcrypt | Playcrypt can use AlphaVSS to delete shadow copies. [66] |
| S1058 | Prestige | Prestige can delete the backup catalog from the target system using: c:\Windows\System32\wbadmin.exe delete catalog -quiet and can also delete volume shadow copies using: \Windows\System32\vssadmin.exe delete shadows /all /quiet . [67] |
| S0654 | ProLock | ProLock can use vssadmin.exe to remove volume shadow copies. [68] |
| S0583 | Pysa | Pysa has the functionality to delete shadow copies. [69] |
| S1242 | Qilin | Qilin can execute vssadmin.exe delete shadows /all /quiet to remove volume shadow copies and can disable High Availability (HA) and Distributed Resource Scheduler (DRS) in vCenter clusters. [70] [71] [72] [73] |
| S0481 | Ragnar Locker | Ragnar Locker can delete volume shadow copies using vssadmin delete shadows /all /quiet . [74] |
| S1212 | RansomHub | RansomHub has used vssadmin.exe to delete volume shadow copies. [75] [76] |
| S0496 | REvil | REvil can use vssadmin to delete volume shadow copies and bcdedit to disable recovery features. [77] [78] [79] [80] [81] [82] [83] [84] [85] |
| S1150 | ROADSWEEP | ROADSWEEP has the ability to disable SystemRestore and Volume Shadow Copies. [86] [87] |
| S0400 | RobbinHood | RobbinHood deletes shadow copies to ensure that all the data cannot be restored easily. [88] |
| S1073 | Royal | Royal can delete shadow copy backups with vssadmin.exe using the command delete shadows /all /quiet . [89] [90] [91] |
| S0446 | Ryuk | Ryuk has used vssadmin Delete Shadows /all /quiet to to delete volume shadow copies and vssadmin resize shadowstorage to force deletion of shadow copies created by third-party applications. [92] |
| G0034 | Sandworm Team | Sandworm Team uses Prestige to delete the backup catalog from the target system using: C:\Windows\System32\wbadmin.exe delete catalog -quiet and to delete volume shadow copies using: C:\Windows\System32\vssadmin.exe delete shadows /all /quiet . [67] |
| G1015 | Scattered Spider | Scattered Spider has stopped the Volume Shadow Copy service on compromised hosts. [93] |
| G1053 | Storm-0501 | Storm-0501 has deleted snapshots, restore points, storage accounts, and backup services to prevent remediation and restoration. [94] Storm-0501 has also impacted Azure resources through the targeting of Microsoft.Compute/snapshots/delete , Microsoft.Compute/restorePointCollections/delete , Microsoft.Storage/storageAccounts/delete , and Microsoft.RecoveryServices/Vaults/backupFabrics/protectionContainers/delete . [94] |
| G1055 | VOID MANTICORE | VOID MANTICORE has deleted virtual machines directly from the virtualization platform. [95] |
| S0366 | WannaCry | WannaCry uses vssadmin , wbadmin , bcdedit , and wmic to delete and disable operating system recovery features. [96] [2] [97] |
| S0612 | WastedLocker | WastedLocker can delete shadow volumes. [98] [99] [100] |
| G0102 | Wizard Spider | Wizard Spider has used WMIC and vssadmin to manually delete volume shadow copies. Wizard Spider has also used Conti ransomware to delete volume shadow copies automatically with the use of vssadmin. [101] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1053 | Data Backup | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data. [102] Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. In cloud environments, enable versioning on storage objects where possible, and copy backups to other accounts or regions to isolate them from the original copies. [103] On ESXi servers, ensure that disk images and snapshots of virtual machines are regularly taken, with copies stored off system. [104] |
| M1038 | Execution Prevention | Consider using application control configured to block execution of utilities such as diskshadow.exe that may not be required for a given system or network to prevent potential misuse by adversaries. |
| M1028 | Operating System Configuration | Consider technical controls to prevent the disabling of services or deletion of files involved in system recovery. Additionally, ensure that WinRE is enabled using the following command: reagentc /enable . [105] |
| M1018 | User Account Management | Limit the user accounts that have access to backups to only those required. In AWS environments, consider using Service Control Policies to restrict API calls to delete backups, snapshots, and images. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0329 | Behavioral Detection for T1490 - Inhibit System Recovery | AN0933 | Process chains that use native utilities (vssadmin, wbadmin, diskshadow, bcdedit, REAgentC, wmic) with arguments to delete shadow copies, disable recovery, or remove backup catalogs |
| AN0934 | Shell utilities or scripts deleting /etc/systemd/system/rescue.target , /etc/fstab backups, or /boot/efi partitions; chattr used to block snapshot auto-recovery |  |  |
| AN0935 | ESXi shell or vim-cmd execution that deletes all VM snapshots using vmsvc/snapshot.removeall or rm on snapshot paths |  |  |
| AN0936 | Execution of erase , format , and reload in immediate sequence from a privileged AAA session |  |  |
| AN0937 | Cloud API calls disabling snapshot scheduling, backup policies, versioning, followed by DeleteSnapshot/DeleteVolume operations |  |  |

---

## References

- [Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [Berry, A., Homan, J., and Eitzman, R. (2017, May 23). WannaCry Malware Profile. Retrieved March 15, 2019.](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
- [TheDFIRReport. (2022, March 1). Disabling notifications on Synology servers before ransom. Retrieved September 12, 2024.](https://x.com/TheDFIRReport/status/1498657590259109894)
- [Microsoft Windows Server. (2023, February 3). Diskshadow. Retrieved November 21, 2023.](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/diskshadow)
- [Romain Dumont . (2022, September 21). Technical Analysis of Crytox Ransomware. Retrieved November 22, 2023.](https://www.zscaler.com/blogs/security-research/technical-analysis-crytox-ransomware)
- [Cybereason Nocturnus. (n.d.). Cybereason vs. BlackCat Ransomware. Retrieved March 26, 2025.](https://www.cybereason.com/blog/cybereason-vs.-blackcat-ransomware)
- [Steve Ranger. (2020, February 27). Ransomware victims thought their backups were safe. They were wrong. Retrieved March 21, 2023.](https://www.zdnet.com/article/ransomware-victims-thought-their-backups-were-safe-they-were-wrong/)
- [Brian Prince. (2014, June 20). Code Hosting Service Shuts Down After Cyber Attack. Retrieved March 21, 2023.](https://www.darkreading.com/attacks-breaches/code-hosting-service-shuts-down-after-cyber-attack)
- [Spencer Gietzen. (n.d.). AWS Simple Storage Service S3 Ransomware Part 2: Prevention and Defense. Retrieved March 21, 2023.](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Max Kersten & Alexandre Mundo. (2023, November 29). Akira Ransomware. Retrieved April 4, 2024.](https://www.trellix.com/blogs/research/akira-ransomware/)
- [CISA et al. (2024, April 18). #StopRansomware: Akira Ransomware. Retrieved December 10, 2024.](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)
- [Security Lab. (2020, June 5). Avaddon: From seeking affiliates to in-the-wild in 2 days. Retrieved August 19, 2021.](https://www.hornetsecurity.com/en/security-information/avaddon-from-seeking-affiliates-to-in-the-wild-in-2-days/)
- [Yuste, J. Pastrana, S. (2021, February 9). Avaddon ransomware: an in-depth analysis and decryption of infected systems. Retrieved August 19, 2021.](https://arxiv.org/pdf/2102.04796.pdf)
- [Sogeti. (2021, March). Babuk Ransomware. Retrieved August 11, 2021.](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
- [Mundo, A. et al. (2021, February). Technical Analysis of Babuk Ransomware. Retrieved August 11, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [Frankoff, S., Hartley, B. (2018, November 14). Big Game Hunting: The Evolution of INDRIK SPIDER From Dridex Wire Fraud to BitPaymer Targeted Ransomware. Retrieved January 6, 2021.](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
- [Zargarov, N. (2022, May 2). New Black Basta Ransomware Hijacks Windows Fax Service. Retrieved March 7, 2023.](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
- [Cyble. (2022, May 6). New ransomware variant targeting high-value organizations. Retrieved November 17, 2024.](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
- [Gonzalez, I., Chavez I., et al. (2022, May 9). Examining the Black Basta Ransomware’s Infection Routine. Retrieved March 7, 2023.](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)
- [Avertium. (2022, June 1). AN IN-DEPTH LOOK AT BLACK BASTA RANSOMWARE. Retrieved March 7, 2023.](https://www.avertium.com/resources/threat-reports/in-depth-look-at-black-basta-ransomware)
- [Inman, R. and Gurney, P. (2022, June 6). Shining the Light on Black Basta. Retrieved March 8, 2023.](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)
- [Vilkomir-Preisman, S. (2022, August 18). Beating Black Basta Ransomware. Retrieved March 8, 2023.](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)
- [Elsad, A. (2022, August 25). Threat Assessment: Black Basta Ransomware. Retrieved March 8, 2023.](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)
- [Trend Micro. (2022, September 1). Ransomware Spotlight Black Basta. Retrieved March 8, 2023.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-blackbasta)
- [Check Point. (2022, October 20). BLACK BASTA AND THE UNNOTICED DELIVERY. Retrieved March 8, 2023.](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
- [Huseyin Can Yuceel. (2022, February 21). TTPs used by BlackByte Ransomware Targeting Critical Infrastructure. Retrieved December 16, 2024.](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)
- [Symantec Threat Hunter Team. (2022, October 21). Exbyte: BlackByte Ransomware Attackers Deploy New Exfiltration Tool. Retrieved December 16, 2024.](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [Mundo, A. (2019, August 1). Clop Ransomware. Retrieved May 10, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
- [Burton, K. (n.d.). The Conficker Worm. Retrieved February 18, 2021.](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
- [Baskin, B. (2020, July 8). TAU Threat Discovery: Conti Ransomware. Retrieved February 17, 2021.](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [McLellan, T. and Moore, J. et al. (2021, April 29). UNC2447 SOMBRAT and FIVEHANDS Ransomware: A Sophisticated Financial Threat. Retrieved June 2, 2021.](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [Dragos. (2020, February 3). EKANS Ransomware and ICS Operations. Retrieved February 9, 2021.](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)
- [Hinchliffe, A. Santos, D. (2020, June 26). Threat Assessment: EKANS Ransomware. Retrieved February 9, 2021.](https://unit42.paloaltonetworks.com/threat-assessment-ekans-ransomware/)
- [Cyble. (2024, May 24). The Rust Revolution: New Embargo Ransomware Steps In. Retrieved October 19, 2025.](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [Reynolds, J.. (2016, September 14). H1N1: Technical analysis reveals new capabilities – part 2. Retrieved November 17, 2024.](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)
- [Thomas, W. et al. (2022, February 25). CrowdStrike Falcon Protects from New Wiper Malware Used in Ukraine Cyberattacks. Retrieved March 25, 2022.](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
- [ESET. (2022, March 1). IsaacWiper and HermeticWizard: New wiper and worm targetingUkraine. Retrieved April 10, 2022.](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
- [Dani, M. (2022, March 1). Ukrainian Targets Hit by HermeticWiper, New Datawiper Malware. Retrieved March 25, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Lee, S.. (2019, May 14). JCry Ransomware. Retrieved June 18, 2019.](https://www.carbonblack.com/2019/05/14/cb-tau-threat-intelligence-notification-jcry-ransomware-pretends-to-be-adobe-flash-player-update-installer/)
- [FBI. (2022, February 4). Indicators of Compromise Associated with LockBit 2.0 Ransomware. Retrieved January 24, 2025.](https://www.ic3.gov/CSA/2022/220204.pdf)
- [Cybereason Global SOC Team. (n.d.). THREAT ANALYSIS REPORT: LockBit 2.0 - All Paths Lead to Ransom. Retrieved January 24, 2025.](https://www.cybereason.com/blog/threat-analysis-report-lockbit-2.0-all-paths-lead-to-ransom)
- [CISA et al. (2023, June 14). UNDERSTANDING RANSOMWARE THREAT ACTORS: LOCKBIT. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [INCIBE-CERT. (2024, March 14). LockBit: response and recovery actions. Retrieved February 5, 2025.](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
- [Mundo, A. (2020, March 26). Ransomware Maze. Retrieved May 18, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
- [Brandt, A., Mackenzie, P.. (2020, September 17). Maze Attackers Adopt Ragnar Locker Virtual Machine Technique. Retrieved October 9, 2020.](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)
- [Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Del Fierro, C. Kessem, L.. (2020, January 8). From Mega to Giga: Cross-Version Comparison of Top MegaCortex Modifications. Retrieved February 15, 2021.](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
- [Check Point Research Team. (2021, August 14). Indra - Hackers Behind Recent Attacks on Iran. Retrieved February 17, 2022.](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
- [Victor, K.. (2020, May 18). Netwalker Fileless Ransomware Injected via Reflective Loading . Retrieved May 26, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
- [Szappanos, G., Brandt, A.. (2020, May 27). Netwalker ransomware tools give insight into threat actor. Retrieved May 27, 2020.](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)
- [Trend Micro Research. (2023, July 21). Ransomware Spotlight: Play. Retrieved September 24, 2024.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
- [MSTIC. (2022, October 14). New “Prestige” ransomware impacts organizations in Ukraine and Poland. Retrieved January 19, 2023.](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
- [Group IB. (2020, September). LOCK LIKE A PRO. Retrieved November 17, 2024.](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
- [CERT-FR. (2020, April 1). ATTACKS INVOLVING THE MESPINOZA/PYSA RANSOMWARE. Retrieved March 1, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
- [Magdy, S. et al. (2022, August 25). New Golang Ransomware Agenda Customizes Attacks. Retrieved September 26, 2025.](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
- [Halcyon RISE Team. (2024, October 24). New Qilin.B Ransomware Variant Boasts Enhanced Encryption and Defense Evasion. Retrieved September 26, 2025.](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
- [Bradshaw, A. et al. (2025, April 1). Qilin affiliates spear-phish MSP ScreenConnect admin, targeting customers downstream. Retrieved September 26, 2025.](https://news.sophos.com/en-us/2025/04/01/sophos-mdr-tracks-ongoing-campaign-by-qilin-affiliates-targeting-screenconnect/)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [SophosLabs. (2020, May 21). Ragnar Locker ransomware deploys virtual machine to dodge security. Retrieved June 29, 2020.](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
- [CISA et al. (2024, August 29). #StopRansomware: RansomHub Ransomware. Retrieved March 17, 2025.](https://www.cisa.gov/sites/default/files/2024-09/aa24-242a-stopransomware-ransomhub-ransomware_1.pdf)
- [Alfano, V. et al. (2025, February 12). RansomHub Never Sleeps Episode 1: The evolution of modern ransomware. Retrieved March 17, 2025.](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
- [Mamedov, O, et al. (2019, July 3). Sodin ransomware exploits Windows vulnerability and processor architecture. Retrieved August 4, 2020.](https://securelist.com/sodin-ransomware/91473/)
- [Cylance. (2019, July 3). hreat Spotlight: Sodinokibi Ransomware. Retrieved August 4, 2020.](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
- [Secureworks . (2019, September 24). REvil: The GandCrab Connection. Retrieved August 4, 2020.](https://www.secureworks.com/blog/revil-the-gandcrab-connection)
- [Cadieux, P, et al (2019, April 30). Sodinokibi ransomware exploits WebLogic Server vulnerability. Retrieved August 4, 2020.](https://blog.talosintelligence.com/2019/04/sodinokibi-ransomware-exploits-weblogic.html)
- [McAfee. (2019, October 2). McAfee ATR Analyzes Sodinokibi aka REvil Ransomware-as-a-Service – What The Code Tells Us. Retrieved August 4, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-what-the-code-tells-us/)
- [Intel 471 Malware Intelligence team. (2020, March 31). REvil Ransomware-as-a-Service – An analysis of a ransomware affiliate operation. Retrieved August 4, 2020.](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
- [Ozarslan, S. (2020, January 15). A Brief History of Sodinokibi. Retrieved August 5, 2020.](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [Tetra Defense. (2020, March). CAUSE AND EFFECT: SODINOKIBI RANSOMWARE ANALYSIS. Retrieved November 17, 2024.](https://web.archive.org/web/20210414101816/https://tetradefense.com/incident-response-services/cause-and-effect-sodinokibi-ransomware-analysis/)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [CISA. (2022, September 23). AA22-264A Iranian State Actors Conduct Cyber Operations Against the Government of Albania. Retrieved August 6, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
- [Lee, S. (2019, May 17). CB TAU Threat Intelligence Notification: RobbinHood Ransomware Stops 181 Windows Services Before Encryption. Retrieved July 29, 2019.](https://www.carbonblack.com/2019/05/17/cb-tau-threat-intelligence-notification-robbinhood-ransomware-stops-181-windows-services-before-encryption/)
- [Cybereason Global SOC and Cybereason Security Research Teams. (2022, December 14). Royal Rumble: Analysis of Royal Ransomware. Retrieved March 30, 2023.](https://www.cybereason.com/blog/royal-ransomware-analysis)
- [Iacono, L. and Green, S. (2023, February 13). Royal Ransomware Deep Dive. Retrieved March 30, 2023.](https://www.kroll.com/en/insights/publications/cyber/royal-ransomware-deep-dive)
- [CISA. (2023, March 2). #StopRansomware: Royal Ransomware. Retrieved March 31, 2023.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-061a)
- [Hanel, A. (2019, January 10). Big Game Hunting with Ryuk: Another Lucrative Targeted Ransomware. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
- [Mandiant Incident Response. (2025, May 6). Defending Against UNC3944: Cybercrime Hardening Guidance from the Frontlines. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)
- [Microsoft Threat Intelligence. (2025, August 27). Storm-0501’s evolving techniques lead to cloud-based ransomware. Retrieved October 19, 2025.](https://www.microsoft.com/en-us/security/blog/2025/08/27/storm-0501s-evolving-techniques-lead-to-cloud-based-ransomware/)
- [Check Point Research. (2026, March 12). “Handala Hack” – Unveiling Group’s Modus Operandi. Retrieved April 20, 2026.](https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/)
- [Noerenberg, E., Costis, A., and Quist, N. (2017, May 16). A Technical Analysis of WannaCry Ransomware. Retrieved December 8, 2024.](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)
- [Counter Threat Unit Research Team. (2017, May 18). WCry Ransomware Analysis. Retrieved March 26, 2019.](https://www.secureworks.com/research/wcry-ransomware-analysis)
- [Symantec Threat Intelligence. (2020, June 25). WastedLocker: Symantec Identifies Wave of Attacks Against U.S. Organizations. Retrieved May 20, 2021.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)
- [Antenucci, S., Pantazopoulos, N., Sandee, M. (2020, June 23). WastedLocker: A New Ransomware Variant Developed By The Evil Corp Group. Retrieved September 14, 2021.](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
- [Walter, J.. (2020, July 23). WastedLocker Ransomware: Abusing ADS and NTFS File Attributes. Retrieved September 14, 2021.](https://www.sentinelone.com/labs/wastedlocker-ransomware-abusing-ads-and-ntfs-file-attributes/)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [Ready.gov. (n.d.). IT Disaster Recovery Plan. Retrieved March 15, 2019.](https://www.ready.gov/business/implementation/IT)
- [Jay Chen. (2022, May 16). A Look Into Public Clouds From the Ransomware Actor's Perspective. Retrieved March 21, 2023.](https://unit42.paloaltonetworks.com/ransomware-in-public-clouds/)
- [Michael Dawson. (2021, August 30). Hypervisor Jackpotting, Part 2: eCrime Actors Increase Targeting of ESXi Servers with Ransomware. Retrieved March 26, 2025.](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
- [Microsoft, EliotSeattle, et al. (2022, August 18). REAgentC command-line options. Retrieved October 19, 2022.](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11)

---


### 🔗 KRAB Intelligence Correlation
- 🦠 **Tooling Capability Integration:** Executed via malware family [[DragonForce]] [related_malware:: [[DragonForce]]]
- 🦠 **Tooling Capability Integration:** Executed via malware family [[Mamona]] [related_malware:: [[Mamona]]]

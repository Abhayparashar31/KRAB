# Peripheral Device Discovery

## Description

Adversaries may attempt to gather information about attached peripheral devices and components connected to a computer system. [1] [2] Peripheral devices could include auxiliary resources that support a variety of functionalities such as keyboards, printers, cameras, smart card readers, or removable storage. The information may be used to enhance their awareness of the system and network environment or may be used for further actions.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1167 | AcidPour | AcidPour includes functionality to identify MMC and SD cards connected to the victim device. [3] |
| S0045 | ADVSTORESHELL | ADVSTORESHELL can list connected devices. [4] |
| G0007 | APT28 | APT28 uses a module to receive a notification every time a USB mass storage device is inserted into a victim. [5] |
| G0067 | APT37 | APT37 has a Bluetooth device harvester, which uses Windows Bluetooth APIs to find information on connected Bluetooth devices. [6] |
| S0438 | Attor | Attor has a plugin that collects information about inserted storage devices, modems, and phone devices. [7] |
| G0135 | BackdoorDiplomacy | BackdoorDiplomacy has used an executable to detect removable media, such as USB flash drives. [8] |
| S0128 | BADNEWS | BADNEWS checks for new hard drives on the victim, such as USB devices, by listening for the WM_DEVICECHANGE window message. [9] [10] |
| S0234 | Bandook | Bandook can detect USB devices. [11] |
| S0089 | BlackEnergy | BlackEnergy can gather very specific information about attached USB devices, to include device instance ID and drive geometry. [12] |
| S0454 | Cadelspy | Cadelspy has the ability to steal information about printers and the documents sent to printers. [13] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP can monitor for removable drives. [14] |
| S0115 | Crimson | Crimson has the ability to discover pluggable/removable drives to extract files from. [15] [16] |
| S0538 | Crutch | Crutch can monitor for removable drives being plugged into the compromised machine. [17] |
| S0673 | DarkWatchman | DarkWatchman can list signed PnP drivers for smartcard readers. [18] |
| S0062 | DustySky | DustySky can detect connected USB devices. [19] |
| S9038 | DynoWiper | DynoWiper has enumerated and overwritten files on all removeable and fixed drives. [20] |
| G0020 | Equation | Equation has used tools with the functionality to search for specific information about the attached hard drive that could be used to identify and overwrite the firmware. [21] |
| S0679 | Ferocious | Ferocious can run GET.WORKSPACE in Microsoft Excel to check if a mouse is present. [22] |
| S0381 | FlawedAmmyy | FlawedAmmyy will attempt to detect if a usable smart card is current inserted into a card reader. [23] |
| S1044 | FunnyDream | The FunnyDream FilepakMonitor component can detect removable drive insertion. [24] |
| G0047 | Gamaredon Group | Gamaredon Group tools have contained an application to check performance of USB flash drives. Gamaredon Group has also used malware to scan for removable drives. [25] [26] [27] |
| S1027 | Heyoka Backdoor | Heyoka Backdoor can identify removable media attached to victim's machines. [28] |
| S1230 | HIUPAN | HIUPAN has checked periodically for removable drives and installs itself when a drive is detected. [29] [30] |
| S1139 | INC Ransomware | INC Ransomware can identify external USB and hard drives for encryption and printers to print ransom notes. [31] |
| S0283 | jRAT | jRAT can map UPnP ports. [32] |
| S1199 | LockBit 2.0 | LockBit 2.0 has the ability to identify mounted external storage devices. [33] |
| S1202 | LockBit 3.0 | LockBit 3.0 has the ability to discover external storage devices. [34] |
| S0409 | Machete | Machete detects the insertion of new devices by listening for the WM_DEVICECHANGE window message. [35] |
| S1026 | Mongall | Mongall can identify removable media attached to compromised hosts. [28] |
| S0149 | MoonWind | MoonWind obtains the number of removable drives from the victim. [36] |
| S1090 | NightClub | NightClub has the ability to monitor removable drives. [37] |
| S0385 | njRAT | njRAT will attempt to detect if the victim system has a camera during the initial infection. njRAT can also detect any removable drives connected to the system. [38] [39] |
| S0644 | ObliqueRAT | ObliqueRAT can discover pluggable/removable drives to extract files from. [40] |
| G0049 | OilRig | OilRig has used tools to identify if a mouse is connected to a targeted system. [41] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors used the fsutil fsinfo drives command as part of their advanced reconnaissance. [42] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors discovered removable disks attached to a system. [43] |
| S0013 | PlugX | PlugX can identify removable media attached to compromised hosts. [44] |
| S0113 | Prikormka | A module in Prikormka collects information on available printers and disk drives. [45] |
| S0650 | QakBot | QakBot can identify peripheral devices on targeted systems. [46] |
| S0686 | QuietSieve | QuietSieve can identify and search removable drives for specific file name extensions. [47] |
| S0481 | Ragnar Locker | Ragnar Locker may attempt to connect to removable drives and mapped network drives. [48] |
| S0458 | Ramsay | Ramsay can scan for removable media which may contain documents for collection. [49] [50] |
| S1150 | ROADSWEEP | ROADSWEEP can identify removable drives attached to the victim's machine. [14] |
| S0148 | RTM | RTM can obtain a list of smart card readers attached to the victim. [51] [52] |
| S1089 | SharpDisco | SharpDisco has dropped a plugin to monitor external drives to C:\Users\Public\It3.exe . [37] |
| S0603 | Stuxnet | Stuxnet enumerates removable drives for infection. [53] |
| S1064 | SVCReady | SVCReady can check for the number of devices plugged into an infected host. [54] |
| S0098 | T9000 | T9000 searches through connected drives for removable storage devices. [55] |
| S0467 | TajMahal | TajMahal has the ability to identify connected Apple devices. [56] |
| G0139 | TeamTNT | TeamTNT has searched for attached VGA devices using lspci. [57] |
| S0647 | Turian | Turian can scan for removable media to collect data. [8] |
| G0010 | Turla | Turla has used fsutil fsinfo drives to list connected drives. [58] |
| S0452 | USBferry | USBferry can check for connected USB devices. [59] |
| S0136 | USBStealer | USBStealer monitors victims for insertion of removable drives. When dropped onto a second victim, it also enumerates drives connected to the system. [60] |
| G1017 | Volt Typhoon | Volt Typhoon has obtained victim's screen dimension and display device information. [61] |
| S0366 | WannaCry | WannaCry contains a thread that will attempt to scan for new attached drives every few seconds. If one is identified, it will encrypt the files on the attached device. [62] |
| S0612 | WastedLocker | WastedLocker can enumerate removable drives prior to the encryption process. [63] |
| S0251 | Zebrocy | Zebrocy enumerates information about connected storage devices. [64] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0491 | Peripheral Device Enumeration via System Utilities and API Calls | AN1353 | Suspicious enumeration of attached peripherals via WMI, PowerShell, or low-level API calls potentially chained with removable device interactions. |
| AN1354 | Enumeration of USB and other peripheral hardware via udevadm, lshw, or /sys or /proc interfaces in proximity to collection or mounting behavior. |  |  |
| AN1355 | Execution of system utilities like 'system_profiler' and 'ioreg' to enumerate hardware components or USB devices, particularly if followed by clipboard, file, or network activity. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0491 | Peripheral Device Enumeration via System Utilities and API Calls | AN1353 | Suspicious enumeration of attached peripherals via WMI, PowerShell, or low-level API calls potentially chained with removable device interactions. |
| AN1354 | Enumeration of USB and other peripheral hardware via udevadm, lshw, or /sys or /proc interfaces in proximity to collection or mounting behavior. |  |  |
| AN1355 | Execution of system utilities like 'system_profiler' and 'ioreg' to enumerate hardware components or USB devices, particularly if followed by clipboard, file, or network activity. |  |  |

---

## References

- [Shahriar Shovon. (2018, March). List USB Devices Linux. Retrieved March 11, 2022.](https://linuxhint.com/list-usb-devices-linux/)
- [SS64. (n.d.). system_profiler. Retrieved March 11, 2022.](https://ss64.com/osx/system_profiler.html)
- [Juan Andrés Guerrero-Saade & Tom Hegel. (2024, March 21). AcidPour | New Embedded Wiper Variant of AcidRain Appears in Ukraine. Retrieved November 25, 2024.](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)
- [ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
- [Anthe, C. et al. (2015, October 19). Microsoft Security Intelligence Report Volume 19. Retrieved December 23, 2015.](http://download.microsoft.com/download/4/4/C/44CDEF0E-7924-4787-A56A-16261691ACE3/Microsoft_Security_Intelligence_Report_Volume_19_English.pdf)
- [GReAT. (2019, May 13). ScarCruft continues to evolve, introduces Bluetooth harvester. Retrieved June 4, 2019.](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [Adam Burgher. (2021, June 10). BackdoorDiplomacy: Upgrading from Quarian to Turian. Retrieved September 1, 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
- [Galperin, E., Et al.. (2016, August). I Got a Letter From the Government the Other Day.... Retrieved April 25, 2018.](https://www.eff.org/files/2016/08/03/i-got-a-letter-from-the-government.pdf)
- [Baumgartner, K. and Garnaeva, M.. (2014, November 3). BE2 custom plugins, router abuse, and target profiles. Retrieved March 24, 2016.](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
- [Symantec Security Response. (2015, December 7). Iran-based attackers use back door threats to spy on Middle Eastern targets. Retrieved April 17, 2019.](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [Faou, M. (2020, December 2). Turla Crutch: Keeping the “back door” open. Retrieved December 4, 2020.](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [GReAT. (2019, April 10). Gaza Cybergang Group1, operation SneakyPastes. Retrieved May 13, 2020.](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
- [ESET. (2026, January 30). Russian Sandworm group attacks energy company in Poland with DynoWiper, ESET Research discovers. Retrieved April 22, 2026.](https://www.eset.com/us/about/newsroom/research/eset-research-russian-sandwormapt-attacks-energy-company-poland-with-dynowiper/)
- [Kaspersky Lab's Global Research and Analysis Team. (2015, February). Equation Group: Questions and Answers. Retrieved December 21, 2015.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064459/Equation_group_questions_and_answers.pdf)
- [Yamout, M. (2021, November 29). WIRTE’s campaign in the Middle East ‘living off the land’ since at least 2019. Retrieved February 1, 2022.](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
- [Proofpoint Staff. (2018, March 7). Leaked Ammyy Admin Source Code Turned into Malware. Retrieved May 28, 2019.](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Kasza, A. and Reichel, D. (2017, February 27). The Gamaredon Group Toolset Evolution. Retrieved March 1, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
- [FBI. (2022, February 4). Indicators of Compromise Associated with LockBit 2.0 Ransomware. Retrieved January 24, 2025.](https://www.ic3.gov/CSA/2022/220204.pdf)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [Miller-Osborn, J. and Grunzweig, J.. (2017, March 30). Trochilus and New MoonWind RATs Used In Attack Against Thai Organizations. Retrieved March 30, 2017.](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Fidelis Cybersecurity. (2013, June 28). Fidelis Threat Advisory #1009: "njRAT" Uncovered. Retrieved June 4, 2019.](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
- [Pascual, C. (2018, November 27). AutoIt-Compiled Worm Affecting Removable Media Delivers Fileless Version of BLADABINDI/njRAT Backdoor. Retrieved June 4, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
- [Malhotra, A. (2021, March 2). ObliqueRAT returns with new campaign using hijacked websites. Retrieved September 2, 2021.](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [DOJ. (2024, December 20). Mag. No. 24-mj-1387 AFFIDAVIT IN SUPPORT OF AN APPLICATION FOR A NINTH SEARCH AND SEIZURE WARRANT- IN THE MATTER OF THE SEARCH AND SEIZURE OF COMPUTERS IN THE UNITED STATES INFECTED WITH PLUGX MALWARE . Retrieved September 9, 2025.](https://www.justice.gov/archives/opa/media/1384136/dl)
- [Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
- [Mendoza, E. et al. (2020, May 25). Qakbot Resurges, Spreads through VBS Files. Retrieved September 27, 2021.](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)
- [Microsoft Threat Intelligence Center. (2022, February 4). ACTINIUM targets Ukrainian organizations. Retrieved February 18, 2022.](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
- [SophosLabs. (2020, May 21). Ragnar Locker ransomware deploys virtual machine to dodge security. Retrieved June 29, 2020.](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Antiy CERT. (2020, April 20). Analysis of Ramsay components of Darkhotel's infiltration and isolation network. Retrieved March 24, 2021.](https://www.programmersought.com/article/62493896999/)
- [Faou, M. and Boutin, J. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
- [Duncan, B., Harbison, M. (2019, January 23). Russian Language Malspam Pushing Redaman Banking Malware. Retrieved June 16, 2020.](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [Grunzweig, J. and Miller-Osborn, J.. (2016, February 4). T9000: Advanced Modular Backdoor Uses Complex Anti-Analysis Techniques. Retrieved April 15, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Calvet, J. (2014, November 11). Sednit Espionage Group Attacking Air-Gapped Networks. Retrieved January 4, 2017.](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Berry, A., Homan, J., and Eitzman, R. (2017, May 23). WannaCry Malware Profile. Retrieved March 15, 2019.](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
- [Walter, J.. (2020, July 23). WastedLocker Ransomware: Abusing ADS and NTFS File Attributes. Retrieved September 14, 2021.](https://www.sentinelone.com/labs/wastedlocker-ransomware-abusing-ads-and-ntfs-file-attributes/)
- [Falcone, R., Lee, B. (2018, November 20). Sofacy Continues Global Attacks and Wheels Out New ‘Cannon’ Trojan. Retrieved November 26, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)

---

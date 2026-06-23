# Replication Through Removable Media

## Description

Adversaries may move onto systems, possibly those on disconnected or air-gapped networks, by copying malware to removable media and taking advantage of Autorun features when the media is inserted into a system and executes. In the case of Lateral Movement, this may occur through modification of executable files stored on removable media or by copying malware and renaming it to look like a legitimate file to trick users into executing it on a separate system. In the case of Initial Access, this may occur through manual manipulation of the media, modification of systems used to initially format the media, or modification to the media's firmware itself.

Mobile devices may also be used to infect PCs with malware if connected via USB. [1] This infection may be achieved using devices (Android, iOS, etc.) and, in some instances, USB charging cables. [2] [3] For example, when a smartphone is connected to a system, it may appear to be mounted similar to a USB-connected disk drive. If malware that is compatible with the connected system is on the mobile device, the malware could infect the machine (especially if Autorun features are enabled).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0092 | Agent.btz | Agent.btz drops itself onto removable media devices and creates an autorun.inf file with an instruction to run that file. When the device is inserted into another system, it opens autorun.inf and loads the malware. [4] |
| S1074 | ANDROMEDA | ANDROMEDA has been spread via infected USB keys. [5] |
| G1007 | Aoqin Dragon | Aoqin Dragon has used a dropper that employs a worm infection strategy using a removable device to breach a secure network environment. [6] |
| G0007 | APT28 | APT28 uses a tool to infect connected USB devices and transmit itself to air-gapped computers when the infected USB device is inserted. [7] |
| S0023 | CHOPSTICK | Part of APT28 's operation involved using CHOPSTICK modules to copy itself to air-gapped machines and using files written to USB sticks to transfer data and command traffic. [8] [7] [9] |
| S0608 | Conficker | Conficker variants used the Windows AUTORUN feature to spread through USB propagation. [10] [11] |
| S0115 | Crimson | Crimson can spread across systems by infecting removable media. [12] |
| G0012 | Darkhotel | Darkhotel 's selective infector modifies executables stored on removable media as a method of spreading across computers. [13] |
| S0062 | DustySky | DustySky searches for removable media and duplicates itself onto it. [14] |
| G0046 | FIN7 | FIN7 actors have mailed USB drives to potential victims containing malware that downloads and installs various backdoors, including in some cases for ransomware operations. [15] Additionally, FIN7 has used malicious USBs that acted as virtual keyboards to install malware and txt files that decode to PowerShell commands. [16] |
| S0143 | Flame | Flame contains modules to infect USB sticks and spread laterally to other Windows systems the stick is plugged into using Autorun functionality. [17] |
| G0047 | Gamaredon Group | Gamaredon Group has replicated to removable media by leveraging the User Assist Reg Key and creating LNKs on all network and removable drives available on the infected host. [18] |
| S0132 | H1N1 | H1N1 has functionality to copy itself to removable media. [19] |
| S1230 | HIUPAN | HIUPAN has periodically checked for removable and hot-plugged drives connected to the infected machine, should one be found HIUPAN will propagate to the removeable drives by copying itself and accompanying malware components to a directory to the new drive in a hidden subdirectory <Drive_Letter>:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\ and hides any other existing files to ensure UsbConfig.exe is the only visible file on the device. [20] [21] |
| G1014 | LuminousMoth | LuminousMoth has used malicious DLLs to spread malware to connected removable USB drives on infected machines. [22] [23] |
| G0129 | Mustang Panda | Mustang Panda has used a customized PlugX variant which could spread through USB connections. [24] |
| S0385 | njRAT | njRAT can be configured to spread via removable drives. [25] [26] |
| S0013 | PlugX | PlugX has copied itself to infected removable drives for propagation to other victim devices. [27] |
| S0650 | QakBot | QakBot has the ability to use removable drives to spread through compromised networks. [28] |
| S0458 | Ramsay | Ramsay can spread itself by infecting other portable executable files on removable drives. [29] |
| S1130 | Raspberry Robin | Raspberry Robin has historically used infected USB media to spread to new victims. [30] [31] |
| S0028 | SHIPSHAPE | APT30 may have used the SHIPSHAPE malware to move onto air-gapped networks. SHIPSHAPE targets removable drives to spread to other systems by modifying the drive to use Autorun to execute or by hiding legitimate document files and copying an executable to the folder with the same name as the legitimate document. [32] |
| S0603 | Stuxnet | Stuxnet can propagate via removable media using an autorun.inf file or the CVE-2010-2568 LNK vulnerability. [33] |
| G0081 | Tropic Trooper | Tropic Trooper has attempted to transfer USBferry from an infected USB device by copying an Autorun function to the target machine. [34] |
| S0130 | Unknown Logger | Unknown Logger is capable of spreading to USB devices. [35] |
| S0386 | Ursnif | Ursnif has copied itself to and infected removable drives for propagation. [36] [37] |
| S0452 | USBferry | USBferry can copy its installer to attached USB storage devices. [34] |
| S0136 | USBStealer | USBStealer drops itself onto removable media and relies on Autorun to execute the malicious file when a user opens the removable media on another system. [38] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1040 | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to block unsigned/untrusted executable files (such as .exe, .dll, or .scr) from running from USB removable drives. [39] |
| M1042 | Disable or Remove Feature or Program | Disable Autorun if it is unnecessary. [40] Disallow or restrict removable media at an organizational policy level if it is not required for business operations. [41] |
| M1034 | Limit Hardware Installation | Limit the use of USB devices and removable media within a network. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0301 | Removable Media Execution Chain Detection via File and Process Activity | AN0841 | Execution of files originating from removable media after drive mount, with correlation to file write activity, autorun usage, or lateral spread via staged tools. |

---

## References

- [Zhaohui Wang & Angelos Stavrou. (n.d.). Exploiting Smart-Phone USB Connectivity For Fun And Profit. Retrieved May 25, 2022.](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.226.3427&rep=rep1&type=pdf)
- [Lucian Constantin. (2014, January 23). Windows malware tries to infect Android devices connected to PCs. Retrieved May 25, 2022.](https://www.computerworld.com/article/2486903/windows-malware-tries-to-infect-android-devices-connected-to-pcs.html)
- [Zack Whittaker. (2019, August 12). This hacker’s iPhone charging cable can hijack your computer. Retrieved May 25, 2022.](https://techcrunch.com/2019/08/12/iphone-charging-cable-hack-computer-def-con/)
- [Shevchenko, S.. (2008, November 30). Agent.btz - A Threat That Hit Pentagon. Retrieved April 8, 2016.](http://blog.threatexpert.com/2008/11/agentbtz-threat-that-hit-pentagon.html)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [Anthe, C. et al. (2015, October 19). Microsoft Security Intelligence Report Volume 19. Retrieved December 23, 2015.](http://download.microsoft.com/download/4/4/C/44CDEF0E-7924-4787-A56A-16261691ACE3/Microsoft_Security_Intelligence_Report_Volume_19_English.pdf)
- [FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
- [Secureworks CTU. (2017, March 30). IRON TWILIGHT Supports Active Measures. Retrieved February 28, 2022.](https://www.secureworks.com/research/iron-twilight-supports-active-measures)
- [Burton, K. (n.d.). The Conficker Worm. Retrieved February 18, 2021.](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
- [Trend Micro. (2014, March 18). Conficker. Retrieved February 18, 2021.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/conficker)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, November). The Darkhotel APT A Story of Unusual Hospitality. Retrieved November 12, 2014.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08070903/darkhotel_kl_07.11.pdf)
- [ClearSky. (2016, January 7). Operation DustySky. Retrieved January 8, 2016.](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
- [The Record. (2022, January 7). FBI: FIN7 hackers target US companies with BadUSB devices to install ransomware. Retrieved January 14, 2022.](https://therecord.media/fbi-fin7-hackers-target-us-companies-with-badusb-devices-to-install-ransomware/)
- [Gemini Advisory. (2022, January 13). FIN7 Uses Flash Drives to Spread Remote Access Trojan. Retrieved May 14, 2025.](https://geminiadvisory.io/fin7-flash-drives-spread-remote-access-trojan/)
- [Gostev, A. (2012, May 28). The Flame: Questions and Answers. Retrieved March 1, 2017.](https://securelist.com/the-flame-questions-and-answers-51/34344/)
- [Threat Hunter Team, Symantec and Carbon Black. (2025, April 10). Shuckworm Targets Foreign Military Mission Based in Ukraine. Retrieved July 23, 2025.](https://www.security.com/threat-intelligence/shuckworm-ukraine-gammasteel)
- [Reynolds, J.. (2016, September 14). H1N1: Technical analysis reveals new capabilities – part 2. Retrieved November 17, 2024.](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Lechtik, M, and etl. (2021, July 14). LuminousMoth APT: Sweeping attacks for the chosen few. Retrieved October 20, 2022.](https://securelist.com/apt-luminousmoth/103332/)
- [Botezatu, B and etl. (2021, July 21). LuminousMoth - PlugX, File Exfiltration and Persistence Revisited. Retrieved October 20, 2022.](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)
- [Hamzeloofard, S. (2020, January 31). New wave of PlugX targets Hong Kong | Avira Blog. Retrieved April 13, 2021.](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)
- [Fidelis Cybersecurity. (2013, June 28). Fidelis Threat Advisory #1009: "njRAT" Uncovered. Retrieved June 4, 2019.](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
- [Pascual, C. (2018, November 27). AutoIt-Compiled Worm Affecting Removable Media Delivers Fileless Version of BLADABINDI/njRAT Backdoor. Retrieved June 4, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
- [DOJ. (2024, December 20). Mag. No. 24-mj-1387 AFFIDAVIT IN SUPPORT OF AN APPLICATION FOR A NINTH SEARCH AND SEIZURE WARRANT- IN THE MATTER OF THE SEARCH AND SEIZURE OF COMPUTERS IN THE UNITED STATES INFECTED WITH PLUGX MALWARE . Retrieved September 9, 2025.](https://www.justice.gov/archives/opa/media/1384136/dl)
- [Mendoza, E. et al. (2020, May 25). Qakbot Resurges, Spreads through VBS Files. Retrieved September 27, 2021.](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Christopher So. (2022, December 20). Raspberry Robin Malware Targets Telecom, Governments. Retrieved May 17, 2024.](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
- [Lauren Podber and Stef Rand. (2022, May 5). Raspberry Robin gets the worm early. Retrieved May 17, 2024.](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)
- [FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved November 17, 2024.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Caragay, R. (2015, March 26). URSNIF: The Multifaceted Malware. Retrieved June 5, 2019.](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
- [Caragay, R. (2014, December 11). Info-Stealing File Infector Hits US, UK. Retrieved June 5, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/info-stealing-file-infector-hits-us-uk/)
- [Calvet, J. (2014, November 11). Sednit Espionage Group Attacking Air-Gapped Networks. Retrieved January 4, 2017.](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
- [Microsoft. (2021, July 2). Use attack surface reduction rules to prevent malware infection. Retrieved June 24, 2021.](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
- [Microsoft. (n.d.). How to disable the Autorun functionality in Windows. Retrieved April 20, 2016.](https://support.microsoft.com/en-us/kb/967715)
- [Microsoft. (2007, August 31). https://technet.microsoft.com/en-us/library/cc771759(v=ws.10).aspx. Retrieved April 20, 2016.](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)

---

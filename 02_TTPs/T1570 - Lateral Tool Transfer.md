# Lateral Tool Transfer

## Description

Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e., Ingress Tool Transfer ) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation.

Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over SMB/Windows Admin Shares to connected network shares or with authenticated connections via Remote Desktop Protocol . [1]

Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and ftp . In some cases, adversaries may be able to leverage Web Service s such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders. [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0028 | 2015 Ukraine Electric Power Attack | During the 2015 Ukraine Electric Power Attack , Sandworm Team moved their tools laterally within the corporate network and between the ICS and corporate network. [3] |
| C0025 | 2016 Ukraine Electric Power Attack | During the 2016 Ukraine Electric Power Attack , Sandworm Team used move to transfer files to a network share. [4] |
| C0034 | 2022 Ukraine Electric Power Attack | During the 2022 Ukraine Electric Power Attack , Sandworm Team used a Group Policy Object (GPO) to copy CaddyWiper 's executable msserver.exe from a staging server to a local hard drive before deployment. [5] |
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries had placed the malicious payload on an accessible network share to facilitate propagation. [6] [7] [8] |
| G1030 | Agrius | Agrius downloaded some payloads for follow-on execution from legitimate filesharing services such as ufile.io and easyupload.io . [9] |
| G1007 | Aoqin Dragon | Aoqin Dragon has spread malware in target networks by copying modules to folders masquerading as removable devices. [10] |
| G0050 | APT32 | APT32 has deployed tools after moving laterally using administrative accounts. [11] |
| G0096 | APT41 | APT41 uses remote shares to move and remotely execute payloads during lateral movemement. [12] |
| S0190 | BITSAdmin | BITSAdmin can be used to create BITS Jobs to upload and/or download files from SMB file servers. [13] |
| G1043 | BlackByte | BlackByte transfered tools such as Cobalt Strike and the AnyDesk remote access tool during operations using SMB shares. [14] |
| S1180 | BlackByte Ransomware | BlackByte Ransomware spreads itself laterally by writing the JavaScript launcher file to mapped shared folders. [15] |
| S1068 | BlackCat | BlackCat can replicate itself across connected servers via psexec . [16] |
| C0015 | C0015 | During C0015 , the threat actors used WMI to load Cobalt Strike onto additional hosts within a compromised network. [17] |
| C0018 | C0018 | During C0018 , the threat actors transferred the SoftPerfect Network Scanner and other tools to machines in the network using AnyDesk and PDQ Deploy. [18] [19] |
| G0114 | Chimera | Chimera has copied tools between compromised hosts using SMB. [20] |
| S0106 | cmd | cmd can be used to copy files to/from a remotely connected internal system. [21] |
| S0062 | DustySky | DustySky searches for network drives and removable media and duplicates itself onto them. [22] |
| G1003 | Ember Bear | Ember Bear retrieves follow-on payloads direct from adversary-owned infrastructure for deployment on compromised hosts. [23] |
| S0367 | Emotet | Emotet has copied itself to remote systems using the service.exe filename. [24] |
| S0404 | esentutl | esentutl can be used to copy files to/from a remote share. [25] |
| S0361 | Expand | Expand can be used to download or upload a file over a network share. [26] |
| G0051 | FIN10 | FIN10 has deployed Meterpreter stagers and SplinterRAT instances in the victim network after moving laterally. [27] |
| S0095 | ftp | ftp may be abused by adversaries to transfer tools or files between systems within a compromised environment. [28] [29] |
| G0093 | GALLIUM | GALLIUM has used PsExec to move laterally between hosts in the target network. [30] |
| S1229 | Havoc | Havoc has the ability to copy files from one location to another. [31] |
| S0698 | HermeticWizard | HermeticWizard can copy files to other machines on a compromised network. [32] |
| C0038 | HomeLand Justice | During HomeLand Justice , threat actors initiated a process named Mellona.exe to spread the ROADSWEEP file encryptor and a persistence script to a list of internal machines. [33] |
| S0357 | Impacket | Impacket has used its wmiexec command, leveraging Windows Management Instrumentation, to remotely stage and execute payloads in victim networks. [34] |
| G1032 | INC Ransom | INC Ransom has used a rapid succession of copy commands to install a file encryption executable across multiple endpoints within compromised infrastructure. [35] [36] |
| S1139 | INC Ransomware | INC Ransomware can push its encryption executable to multiple endpoints within compromised infrastructure. [35] |
| S1132 | IPsec Helper | IPsec Helper can download additional payloads from command and control nodes and execute them. [37] |
| S0372 | LockerGoga | LockerGoga has been observed moving around the victim network via SMB, indicating the actors behind this ransomware are manually copying files form computer to computer instead of self-propagating. [1] |
| S0532 | Lucifer | Lucifer can use certutil for propagation on Windows hosts within intranets. [38] |
| G0059 | Magic Hound | Magic Hound has copied tools within a compromised network using RDP. [39] |
| G1051 | Medusa Group | Medusa Group has utilized legitimate software services such as PDQ Deploy to transfer malicious binaries and tools to other victimized hosts within the target environment. [40] |
| S0457 | Netwalker | Operators deploying Netwalker have used psexec to copy the Netwalker payload across accessible systems. [41] |
| S0365 | Olympic Destroyer | Olympic Destroyer attempts to copy itself to remote machines on the network. [42] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors used SMB to copy files to and from target systems. [43] |
| S1017 | OutSteel | OutSteel can download the Saint Bot malware for follow-on execution. [44] |
| S0029 | PsExec | PsExec can be used to download or upload a file over a network share. [45] |
| S1242 | Qilin | Qilin has used PsExec to distribute a second encryptor, named encryptor_1.exe, across the targeted environment. [46] |
| S9030 | SameCoin | SameCoin can copy its wiper executable to remote machines within the same Active Directory. [47] |
| G0034 | Sandworm Team | Sandworm Team has used move to transfer files to a network share and has copied payloads--such as Prestige ransomware--to an Active Directory Domain Controller and distributed via the Default Domain Group Policy Object. [4] [48] Additionally, Sandworm Team has transferred an ISO file into the OT network to gain initial access. [5] |
| S0140 | Shamoon | Shamoon attempts to copy itself to remote machines on the network. [49] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors used Impacket to remotely stage and execute payloads via WMI. [50] |
| G1046 | Storm-1811 | Storm-1811 has used the Impacket toolset to move and remotely execute payloads to other hosts in victim networks. [51] |
| S0603 | Stuxnet | Stuxnet uses an RPC server that contains a file dropping routine and support for payload version updates for P2P communications within a victim network. [52] |
| G0010 | Turla | Turla RPC backdoors can be used to transfer files to/from victim machines on the local network. [53] [54] |
| G1048 | UNC3886 | UNC3886 has utilzed Python scripts to transfer files between ESXi hosts and guest VMs. [55] |
| G1047 | Velvet Ant | Velvet Ant transferred files laterally within victim networks through the Impacket toolkit. [34] |
| S1218 | VIRTUALPIE | VIRTUALPIE has file transfer capabilities. [56] |
| S1217 | VIRTUALPITA | VIRTUALPITA is capable of file transfer and arbitrary command execution. [56] |
| G1017 | Volt Typhoon | Volt Typhoon has copied web shells between servers in targeted environments. [57] |
| S0366 | WannaCry | WannaCry attempts to copy itself to remote computers after gaining access via an SMB exploit. [58] |
| G0102 | Wizard Spider | Wizard Spider has used stolen credentials to copy tools into the %TEMP% directory of domain controllers. [59] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1037 | Filter Network Traffic | Consider using the host firewall to restrict file sharing communications such as SMB. [60] |
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware or unusual data transfer over known tools and protocols like FTP can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. [61] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0183 | Detection Strategy for Lateral Tool Transfer across OS platforms | AN0516 | Correlate suspicious file transfers over SMB or Admin$ shares with process creation events (e.g., cmd.exe, powershell.exe, certutil.exe) that do not align with normal administrative behavior. Detect remote file writes followed by execution of transferred binaries. |
| AN0517 | Monitor scp, rsync, curl, sftp, or ftp processes initiating transfers to internal systems combined with file creation events in unusual directories. Correlate transfer activity with subsequent execution of those binaries. |  |  |
| AN0518 | Detect anomalous use of scp, rsync, curl, or third-party sync apps transferring executables into user directories. Correlate new file creation with immediate execution events. |  |  |
| AN0519 | Identify lateral transfer via datastore file uploads or internal scp/ssh sessions that result in new VMX/VMDK or script files. Correlate transfer with VM execution or datastore modification. |  |  |

---

## References

- [Harbison, M. (2019, March 26). Born This Way? Origins of LockerGoga. Retrieved April 16, 2019.](https://unit42.paloaltonetworks.com/born-this-way-origins-of-lockergoga/)
- [David Talbot. (2013, August 21). Dropbox and Similar Services Can Sync Malware. Retrieved May 31, 2023.](https://www.technologyreview.com/2013/08/21/83143/dropbox-and-similar-services-can-sync-malware/)
- [Booz Allen Hamilton. (2016). When The Lights Went Out. Retrieved December 18, 2024.](https://www.boozallen.com/content/dam/boozallen/documents/2016/09/ukraine-report-when-the-lights-went-out.pdf)
- [Joe Slowik. (2018, October 12). Anatomy of an Attack: Detecting and Defeating CRASHOVERRIDE. Retrieved December 18, 2020.](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)
- [Ken Proska, John Wolfram, Jared Wilson, Dan Black, Keith Lunden, Daniel Kapellmann Zafra, Nathan Brubaker, Tyler Mclellan, Chris Sistrunk. (2023, November 9). Sandworm Disrupts Power in Ukraine Using a Novel Attack Against Operational Technology. Retrieved March 28, 2024.](https://www.mandiant.com/resources/blog/sandworm-disrupts-power-ukraine-operational-technology)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [ESET. (2026, January 30). Russian Sandworm group attacks energy company in Poland with DynoWiper, ESET Research discovers. Retrieved April 22, 2026.](https://www.eset.com/us/about/newsroom/research/eset-research-russian-sandwormapt-attacks-energy-company-poland-with-dynowiper/)
- [ESET. (2026, January 30). DynoWiper update: Technical analysis and attribution. Retrieved April 22, 2026.](https://www.welivesecurity.com/en/eset-research/dynowiper-update-technical-analysis-attribution/)
- [Marc Salinas Fernandez & Jiri Vinopal. (2023, May 23). AGRIUS DEPLOYS MONEYBIRD IN TARGETED ATTACKS AGAINST ISRAELI ORGANIZATIONS. Retrieved May 21, 2024.](https://research.checkpoint.com/2023/agrius-deploys-moneybird-in-targeted-attacks-against-israeli-organizations/)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Nikita Rostovcev. (2022, August 18). APT41 World Tour 2021 on a tight schedule. Retrieved February 22, 2024.](https://www.group-ib.com/blog/apt41-world-tour-2021/)
- [Microsoft. (2019, July 12). About BITS. Retrieved March 16, 2020.](https://docs.microsoft.com/en-us/windows/win32/bits/about-bits)
- [Huseyin Can Yuceel. (2022, February 21). TTPs used by BlackByte Ransomware Targeting Critical Infrastructure. Retrieved December 16, 2024.](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Venere, G. Neal, C. (2022, June 21). Avos ransomware group expands with new attack arsenal. Retrieved January 11, 2023.](https://blog.talosintelligence.com/avoslocker-new-arsenal/)
- [Costa, F. (2022, May 1). RaaS AvosLocker Incident Response Analysis. Retrieved January 11, 2023.](https://www.linkedin.com/pulse/raas-avoslocker-incident-response-analysis-fl%C3%A1vio-costa?trk=articles_directory)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Microsoft. (n.d.). Copy. Retrieved April 26, 2016.](https://technet.microsoft.com/en-us/library/bb490886.aspx)
- [ClearSky. (2016, January 7). Operation DustySky. Retrieved January 8, 2016.](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
- [Microsoft Threat Intelligence. (2023, June 14). Cadet Blizzard emerges as a novel and distinct Russian threat actor. Retrieved July 10, 2023.](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)
- [Binary Defense. (n.d.). Emotet Evolves With new Wi-Fi Spreader. Retrieved September 8, 2023.](https://www.binarydefense.com/resources/blog/emotet-evolves-with-new-wi-fi-spreader/)
- [LOLBAS. (n.d.). Esentutl.exe. Retrieved September 3, 2019.](https://lolbas-project.github.io/lolbas/Binaries/Esentutl/)
- [LOLBAS. (n.d.). Expand.exe. Retrieved February 19, 2019.](https://lolbas-project.github.io/lolbas/Binaries/Expand/)
- [FireEye iSIGHT Intelligence. (2017, June 16). FIN10: Anatomy of a Cyber Extortion Operation. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/rpt-fin-10-anatomy-of-a-cyber-en.pdf)
- [Microsoft. (2021, July 21). ftp. Retrieved February 25, 2022.](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ftp)
- [N/A. (n.d.). ftp(1) - Linux man page. Retrieved February 25, 2022.](https://linux.die.net/man/1/ftp)
- [MSTIC. (2019, December 12). GALLIUM: Targeting global telecom. Retrieved January 13, 2021.](https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/)
- [Ungur, P. (n.d.). HAVOC. Retrieved August 4, 2025.](https://havocframework.com/docs/welcome)
- [ESET. (2022, March 1). IsaacWiper and HermeticWizard: New wiper and worm targetingUkraine. Retrieved April 10, 2022.](https://www.welivesecurity.com/2022/03/01/isaacwiper-hermeticwizard-wiper-worm-targeting-ukraine)
- [CISA. (2022, September 23). AA22-264A Iranian State Actors Conduct Cyber Operations Against the Government of Albania. Retrieved August 6, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
- [Sygnia Team. (2024, June 3). China-Nexus Threat Group ‘Velvet Ant’ Abuses F5 Load Balancers for Persistence. Retrieved March 14, 2025.](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
- [Team Huntress. (2023, August 11). Investigating New INC Ransom Group Activity. Retrieved June 5, 2024.](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)
- [Counter Threat Unit Research Team. (2024, April 15). GOLD IONIC DEPLOYS INC RANSOMWARE. Retrieved June 5, 2024.](https://www.secureworks.com/blog/gold-ionic-deploys-inc-ransomware)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [Hsu, K. et al. (2020, June 24). Lucifer: New Cryptojacking and DDoS Hybrid Malware Exploiting High and Critical Vulnerabilities to Infect Windows Devices. Retrieved November 16, 2020.](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [Szappanos, G., Brandt, A.. (2020, May 27). Netwalker ransomware tools give insight into threat actor. Retrieved May 27, 2020.](https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/)
- [Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Russinovich, M. (2004, June 28). PsExec. Retrieved December 17, 2015.](http://windowsitpro.com/systems-management/psexec)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [Check Point. (2024, November 12). Hamas-affiliated Threat Actor WIRTE Continues its Middle East Operations and Moves to Disruptive Activity. Retrieved April 20, 2026.](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
- [MSTIC. (2022, October 14). New “Prestige” ransomware impacts organizations in Ukraine and Poland. Retrieved January 19, 2023.](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
- [Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [Microsoft Threat Intelligence. (2025, July 22). Disrupting active exploitation of on-premises SharePoint vulnerabilities. Retrieved October 15, 2025.](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/#storm-2603)
- [Tyler McGraw, Thomas Elkins, and Evan McCann. (2024, May 10). Ongoing Social Engineering Campaign Linked to Black Basta Ransomware Operators. Retrieved January 31, 2025.](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [Symantec DeepSight Adversary Intelligence Team. (2019, June 20). Waterbug: Espionage Group Rolls Out Brand-New Toolset in Attacks Against Governments. Retrieved July 8, 2019.](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)
- [Alexander Marvi, Brad Slaybaugh, Ron Craft, and Rufus Brown. (2023, June 13). VMware ESXi Zero-Day Used by Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)
- [Alexander Marvi, Jeremy Koppen, Tufail Ahmed, and Jonathan Lepore. (2022, September 29). Bad VIB(E)s Part One: Investigating Novel Malware Persistence Within ESXi Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
- [Counter Threat Unit Research Team. (2023, May 24). Chinese Cyberespionage Group BRONZE SILHOUETTE Targets U.S. Government and Defense Organizations. Retrieved July 27, 2023.](https://web.archive.org/web/20230601025540/https://www.secureworks.com/blog/chinese-cyberespionage-group-bronze-silhouette-targets-us-government-and-defense-organizations)
- [Noerenberg, E., Costis, A., and Quist, N. (2017, May 16). A Technical Analysis of WannaCry Ransomware. Retrieved December 8, 2024.](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)
- [John, E. and Carvey, H. (2019, May 30). Unraveling the Spiderweb: Timelining ATT&CK Artifacts Used by GRIM SPIDER. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)
- [Microsoft. (2020, March 10). Preventing SMB traffic from lateral connections and entering or leaving the network. Retrieved June 1, 2020.](https://support.microsoft.com/en-us/help/3185535/preventing-smb-traffic-from-lateral-connections)
- [Gardiner, J., Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

---

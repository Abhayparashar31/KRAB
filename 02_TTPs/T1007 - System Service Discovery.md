# System Service Discovery

## Description

Adversaries may try to gather information about registered local system services. Adversaries may obtain information about services using tools as well as OS utility commands such as sc query , tasklist /svc , systemctl --type=service , and net start . Adversaries may also gather information about schedule tasks via commands such as schtasks on Windows or crontab -l on Linux and macOS. [1] [2] [3] [4]

Adversaries may use the information from System Service Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0018 | admin@338 | admin@338 actors used the following command following exploitation of a machine with LOWBALL malware to obtain information about services: net start >> %temp%\download [5] |
| G0006 | APT1 | APT1 used the commands net start and tasklist to get a listing of the services on the system. [6] |
| G0143 | Aquatic Panda | Aquatic Panda has attempted to discover services for third party EDR products. [7] |
| S0638 | Babuk | Babuk can enumerate all services running on a compromised host. [8] |
| S0127 | BBSRAT | BBSRAT can query service configuration information. [9] |
| S0570 | BitPaymer | BitPaymer can enumerate existing Windows services on the host that are configured to run as LocalSystem. [10] |
| S1070 | Black Basta | Black Basta can check whether the service name FAX is present. [11] |
| G0060 | BRONZE BUTLER | BRONZE BUTLER has used TROJ_GETVERSION to discover system services. [12] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell can obtain a list of the services from a system. [13] |
| G0114 | Chimera | Chimera has used net start and net use for system service discovery. [14] |
| S0154 | Cobalt Strike | Cobalt Strike can enumerate services on compromised hosts. [15] |
| S0244 | Comnie | Comnie runs the command: net start >> %TEMP%\info.dat on a victim. [16] |
| S0625 | Cuba | Cuba can query service status using QueryServiceStatusEx function. [17] |
| S1066 | DarkTortilla | DarkTortilla can retrieve information about a compromised system's running services. [18] |
| S0024 | Dyre | Dyre has the ability to identify running services on a compromised host. [19] |
| G1006 | Earth Lusca | Earth Lusca has used Tasklist to obtain information from a compromised host. [20] |
| S0081 | Elise | Elise executes net start after initial communication is made to the remote server. [21] |
| S1247 | Embargo | Embargo has obtained active services running on the victim’s system through the functions OpenSCManagerW() and EnumServicesStatusExW() . [22] |
| S0082 | Emissary | Emissary has the capability to execute the command net start to interact with services. [23] |
| S0091 | Epic | Epic uses the tasklist /svc command to list the services on the system. [24] |
| S0049 | GeminiDuke | GeminiDuke collects information on programs and services on the victim that are configured to automatically run at startup. [25] |
| S0237 | GravityRAT | GravityRAT has a feature to list the available services on the system. [26] |
| S0342 | GreyEnergy | GreyEnergy enumerates all Windows services. [27] |
| S1027 | Heyoka Backdoor | Heyoka Backdoor can check if it is running as a service on a compromised host. [28] |
| S0431 | HotCroissant | HotCroissant has the ability to retrieve a list of services on the infected host. [29] |
| S0203 | Hydraq | Hydraq creates a backdoor through which remote attackers can monitor services. [30] [31] |
| S0398 | HyperBro | HyperBro can list all services and their configurations. [32] |
| G0119 | Indrik Spider | Indrik Spider has used the win32_service WMI class to retrieve a list of services from the system. [33] |
| S0260 | InvisiMole | InvisiMole can obtain running services on the victim. [34] |
| S0015 | Ixeshe | Ixeshe can list running services. [35] |
| S0201 | JPIN | JPIN can list running services. [36] |
| S0283 | jRAT | jRAT can list local services. [37] |
| G0004 | Ke3chang | Ke3chang performs service discovery using net start commands. [38] |
| G0094 | Kimsuky | Kimsuky has used an instrumentor script to gather the names of all services running on a victim's system. [39] |
| S0236 | Kwampirs | Kwampirs collects a list of running services with the command tasklist /svc . [40] |
| S9035 | LAMEHUG | LAMEHUG can gather service information on targeted systems. [41] [42] |
| S0582 | LookBack | LookBack can enumerate services on the victim machine. [43] |
| S1244 | Medusa Ransomware | Medusa Ransomware has leveraged an encoded list of services that it designates for termination. [44] [45] [46] |
| G1054 | MirrorFace | MirrorFace has used Tasklist for discovery post compromise. [47] |
| S0039 | Net | The net start command can be used in Net to find information about Windows services. [48] |
| G0049 | OilRig | OilRig has used sc query on a victim to gather information about services. [49] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors used the net start command as part of their initial reconnaissance. [50] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors used the tasklist command to search for one of its backdoors. [51] |
| G0033 | Poseidon Group | After compromising a victim, Poseidon Group discovers all running services. [52] |
| S0378 | PoshC2 | PoshC2 can enumerate service and service permission information. [53] |
| S1228 | PUBLOAD | PUBLOAD has leveraged tasklist to gather running services on victim host. [54] |
| S1242 | Qilin | Qilin can identify specific services for termination or to be left running at execution. [55] [56] [57] [58] |
| S0629 | RainyDay | RainyDay can create and register a service for execution. [59] |
| S0241 | RATANKBA | RATANKBA uses tasklist /svc to display running tasks. [60] |
| S0496 | REvil | REvil can enumerate active services. [61] |
| S0085 | S-Type | S-Type runs the command net start on a victim. [62] |
| S1085 | Sardonic | Sardonic has the ability to execute the net start command. [63] |
| S0692 | SILENTTRINITY | SILENTTRINITY can search for modifiable services that could be used for privilege escalation. [64] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA has the capability to enumerate services. [65] |
| S0615 | SombRAT | SombRAT can enumerate services on a victim machine. [66] |
| S0559 | SUNBURST | SUNBURST collected a list of service names that were hashed using a FNV-1a + XOR algorithm to check against similarly-hashed hardcoded blocklists. [67] |
| S0018 | Sykipot | Sykipot may use net start to display running services. [68] |
| S0242 | SynAck | SynAck enumerates all running services. [69] [70] |
| S0663 | SysUpdate | SysUpdate can collect a list of services on a victim machine. [71] |
| S0057 | Tasklist | Tasklist can be used to discover services running on a system. [72] |
| G0139 | TeamTNT | TeamTNT has searched for services such as Alibaba Cloud Security's aliyun service and BMC Helix Cloud Security's bmc-agent service in order to disable them. [73] |
| S0266 | TrickBot | TrickBot collects a list of install programs and services on the system’s machine. [74] |
| G0010 | Turla | Turla surveys a system upon check-in to discover running services and associated processes using the tasklist /svc command. [24] |
| S0386 | Ursnif | Ursnif has gathered information about running services. [75] |
| S0180 | Volgmer | Volgmer queries the system to identify existing services. [76] |
| G1017 | Volt Typhoon | Volt Typhoon has used net start to list running services. [77] |
| S0219 | WINERACK | WINERACK can enumerate services. [78] |
| S0086 | ZLib | ZLib has the ability to discover and manipulate Windows services. [62] |
| S0412 | ZxShell | ZxShell can check the services on the system. [79] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0483 | Detection of System Service Discovery Commands Across OS Platforms | AN1325 | Enumeration of services via native CLI tools (e.g., sc query , tasklist /svc , net start ) or API calls via PowerShell and WMI. |
| AN1326 | Execution of service management commands like systemctl list-units , service --status-all , or direct reading of /etc/init.d . |  |  |
| AN1327 | Discovery via launchctl commands, or process enumeration using ps aux | grep com.apple. to identify daemons and services. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0483 | Detection of System Service Discovery Commands Across OS Platforms | AN1325 | Enumeration of services via native CLI tools (e.g., sc query , tasklist /svc , net start ) or API calls via PowerShell and WMI. |
| AN1326 | Execution of service management commands like systemctl list-units , service --status-all , or direct reading of /etc/init.d . |  |  |
| AN1327 | Discovery via launchctl commands, or process enumeration using ps aux | grep com.apple. to identify daemons and services. |  |  |

---

## References

- [Jia Yu Chan, Salim Bitam, Daniel Stepanic, and Seth Goodwin. (2024, December 12). Under the SADBRIDGE with GOSAR: QUASAR Gets a Golang Rewrite. Retrieved May 22, 2025.](https://www.elastic.co/security-labs/under-the-sadbridge-with-gosar)
- [Phil Stokes. (2021, February 16). 20 Common Tools & Techniques Used by macOS Threat Actors & Malware. Retrieved May 22, 2025.](https://www.sentinelone.com/labs/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
- [Splunk Threat Research Team , Teoderick Contreras. (2024, July 15). Breaking Down Linux.Gomir: Understanding this Backdoor’s TTPs. Retrieved May 22, 2025.](https://www.splunk.com/en_us/blog/security/breaking-down-linux-gomir-understanding-this-backdoors-ttps.html)
- [Gal Singer. (2020, April 3). Threat Alert: Kinsing Malware Attacks Targeting Container Environments. Retrieved May 22, 2025.](https://www.aquasec.com/blog/threat-alert-kinsing-malware-container-vulnerability/)
- [FireEye Threat Intelligence. (2015, December 1). China-based Cyber Threat Group Uses Dropbox for Malware Communications and Targets Hong Kong Media Outlets. Retrieved December 4, 2015.](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)
- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Wiley, B. et al. (2021, December 29). OverWatch Exposes AQUATIC PANDA in Possession of Log4Shell Exploit Tools During Hands-on Intrusion Attempt. Retrieved January 18, 2022.](https://www.crowdstrike.com/blog/overwatch-exposes-aquatic-panda-in-possession-of-log-4-shell-exploit-tools/)
- [Mundo, A. et al. (2021, February). Technical Analysis of Babuk Ransomware. Retrieved August 11, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
- [Lee, B. Grunzweig, J. (2015, December 22). BBSRAT Attacks Targeting Russian Organizations Linked to Roaming Tiger. Retrieved August 19, 2016.](http://researchcenter.paloaltonetworks.com/2015/12/bbsrat-attacks-targeting-russian-organizations-linked-to-roaming-tiger/)
- [Frankoff, S., Hartley, B. (2018, November 14). Big Game Hunting: The Evolution of INDRIK SPIDER From Dridex Wire Fraud to BitPaymer Targeted Ransomware. Retrieved January 6, 2021.](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
- [Cyble. (2022, May 6). New ransomware variant targeting high-value organizations. Retrieved November 17, 2024.](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Grunzweig, J. (2018, January 31). Comnie Continues to Target Organizations in East Asia. Retrieved June 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [hasherezade. (2015, November 4). A Technical Look At Dyreza. Retrieved June 15, 2020.](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
- [Chen, J., et al. (2022). Delving Deep: An Analysis of Earth Lusca’s Operations. Retrieved July 1, 2022.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
- [Falcone, R., et al.. (2015, June 16). Operation Lotus Blossom. Retrieved February 15, 2016.](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)
- [Cyble. (2024, May 24). The Rust Revolution: New Embargo Ransomware Steps In. Retrieved October 19, 2025.](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
- [Falcone, R. and Miller-Osborn, J. (2016, February 3). Emissary Trojan Changelog: Did Operation Lotus Blossom Cause It to Evolve?. Retrieved February 15, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [F-Secure Labs. (2015, September 17). The Dukes: 7 years of Russian cyberespionage. Retrieved December 10, 2015.](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
- [Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
- [Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [Knight, S.. (2020, April 16). VMware Carbon Black TAU Threat Analysis: The Evolution of Lazarus. Retrieved May 1, 2020.](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
- [Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
- [Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
- [Falcone, R. and Lancaster, T. (2019, May 28). Emissary Panda Attacks Middle East Government Sharepoint Servers. Retrieved July 9, 2019.](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)
- [Symantec Threat Intelligence. (2020, June 25). WastedLocker: Symantec Identifies Wave of Attacks Against U.S. Organizations. Retrieved May 20, 2021.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Sancho, D., et al. (2012, May 22). IXESHE An APT Campaign. Retrieved June 7, 2019.](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
- [Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
- [Google Threat Intelligence Group. (2025, November 5). GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools. Retrieved March 31, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
- [Simonovich, V. (2025, July 23). Cato CTRL™ Threat Research: Analyzing LAMEHUG – First Known LLM-Powered Malware with Links to APT28 (Fancy Bear) . Retrieved April 21, 2026.](https://www.catonetworks.com/blog/cato-ctrl-threat-research-analyzing-lamehug/)
- [Raggi, M. Schwarz, D.. (2019, August 1). LookBack Malware Targets the United States Utilities Sector with Phishing Attacks Impersonating Engineering Licensing Boards. Retrieved February 25, 2021.](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
- [Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)
- [Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Kaspersky Lab's Global Research and Analysis Team. (2016, February 9). Poseidon Group: a Targeted Attack Boutique specializing in global cyber-espionage. Retrieved March 16, 2016.](https://securelist.com/poseidon-group-a-targeted-attack-boutique-specializing-in-global-cyber-espionage/73673/)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Magdy, S. et al. (2022, August 25). New Golang Ransomware Agenda Customizes Attacks. Retrieved September 26, 2025.](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
- [SentinelOne. (2022, November 30). Agenda (Qilin). Retrieved September 26, 2025.](https://www.sentinelone.com/anthology/agenda-qilin/)
- [Health Sector Cybersecurity Coordination Center. (2024, June 18). Qilin, aka Agenda Ransomware. Retrieved September 26, 2025.](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [Vrabie, V. (2021, April 23). NAIKON – Traces from a Military Cyber-Espionage Operation. Retrieved June 29, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
- [Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
- [Intel 471 Malware Intelligence team. (2020, March 31). REvil Ransomware-as-a-Service – An analysis of a ransomware affiliate operation. Retrieved August 4, 2020.](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Budaca, E., et al. (2021, August 25). FIN8 Threat Actor Goes Agile with New Sardonic Backdoor. Retrieved August 9, 2023.](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [The BlackBerry Research and Intelligence Team. (2020, November 12). The CostaRicto Campaign: Cyber-Espionage Outsourced. Retrieved May 24, 2021.](https://blogs.blackberry.com/en/2020/11/the-costaricto-campaign-cyber-espionage-outsourced)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [Blasco, J. (2011, December 12). Another Sykipot sample likely targeting US federal agencies. Retrieved March 28, 2016.](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)
- [Ivanov, A. et al. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
- [Bettencourt, J. (2018, May 7). Kaspersky Lab finds new variant of SynAck ransomware using sophisticated Doppelgänging technique. Retrieved May 24, 2018.](https://usa.kaspersky.com/about/press-releases/2018_synack-doppelganging)
- [Daniel Lunghi. (2023, March 1). Iron Tiger’s SysUpdate Reappears, Adds Linux Targeting. Retrieved March 20, 2023.](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
- [Microsoft. (n.d.). Tasklist. Retrieved December 23, 2015.](https://technet.microsoft.com/en-us/library/bb491010.aspx)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
- [Caragay, R. (2015, March 26). URSNIF: The Multifaceted Malware. Retrieved June 5, 2019.](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
- [US-CERT. (2017, November 22). Alert (TA17-318B): HIDDEN COBRA – North Korean Trojan: Volgmer. Retrieved December 7, 2017.](https://www.us-cert.gov/ncas/alerts/TA17-318B)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)

---

# Software Discovery

## Description

Adversaries may attempt to get a listing of software and software versions that are installed on a system or in a cloud environment. Adversaries may use the information from Software Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Such software may be deployed widely across the environment for configuration management or security reasons, such as Software Deployment Tools , and may allow adversaries broad access to infect devices or move laterally.

Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are present or if the compromised system has a version of software that is vulnerable to Exploitation for Privilege Escalation .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0534 | Bazar | Bazar can query the Registry for installed applications. [1] |
| G0060 | BRONZE BUTLER | BRONZE BUTLER has used tools to enumerate software installed on an infected host. [2] |
| S0482 | Bundlore | Bundlore has the ability to enumerate what browser is being used as well as version information for Safari. [3] |
| S0674 | CharmPower | CharmPower can list the installed applications on a compromised host. [4] |
| S0154 | Cobalt Strike | The Cobalt Strike System Profiler can discover applications through the browser and identify the version of Java the target has. [5] |
| S0126 | ComRAT | ComRAT can check the victim's default browser to determine which process to inject its communications module into. [6] |
| S1153 | Cuckoo Stealer | Cuckoo Stealer has the ability to search systems for installed applications. [7] |
| S0472 | down_new | down_new has the ability to gather information on installed applications. [2] |
| S0384 | Dridex | Dridex has collected a list of installed software on the system. [8] |
| S0062 | DustySky | DustySky lists all installed software for the infected machine. [9] |
| S0024 | Dyre | Dyre has the ability to identify installed programs on a compromised host. [10] |
| S9010 | GlassWorm | GlassWorm has searched for existing wallet applications to include Ledger Live and Trezor Suite. [11] |
| G1001 | HEXANE | HEXANE has enumerated programs installed on an infected machine. [12] |
| S0431 | HotCroissant | HotCroissant can retrieve a list of applications from the SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths registry key. [13] |
| G0100 | Inception | Inception has enumerated installed software on compromised systems. [14] |
| S1245 | InvisibleFerret | InvisibleFerret has gathered installed programs and running processes. [15] |
| S0260 | InvisiMole | InvisiMole can collect information about installed software used by specific users, software executed on user login, and software executed by each system. [16] [17] |
| S9029 | IronWind | IronWind can list installed software on targeted hosts. [18] |
| C0044 | Juicy Mix | During Juicy Mix , OilRig used browser data dumper tools to create a list of users with Google Chrome installed. [19] |
| S0526 | KGH_SPY | KGH_SPY can collect information on installed applications. [20] |
| S1185 | LightSpy | If sent the command 16001 , LightSpy uses the NSFileManger contentsOfDirectoryAtPath() to enumerate the Applications folder to collect the bundle name, bundle identifier, and version information from each application's info.plist file. The results are then converted into a JSON blob for exfiltration. [21] |
| S1141 | LunarWeb | LunarWeb can list installed software on compromised systems. [22] |
| S0652 | MarkiRAT | MarkiRAT can check for the Telegram installation directory by enumerating the files on disk. [23] |
| S0455 | Metamorfo | Metamorfo has searched the compromised system for banking applications. [24] [25] |
| G0069 | MuddyWater | MuddyWater has used a PowerShell backdoor to check for Skype connectivity on the target machine. [26] |
| G0129 | Mustang Panda | Mustang Panda has searched the victim system for the InstallUtil.exe program and its version. [27] |
| C0016 | Operation Dust Storm | During Operation Dust Storm , the threat actors deployed a file called DeployJava.js to fingerprint installed software on a victim system prior to exploit delivery. [28] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors collected a list of installed software on the infected system. [29] |
| S0229 | Orz | Orz can gather the victim's Internet Explorer version. [30] |
| S0598 | P.A.S. Webshell | P.A.S. Webshell can list PHP server configuration details. [31] |
| S1228 | PUBLOAD | PUBLOAD has used several commands executed in sequence via cmd in a short interval to gather software versions including querying Registry keys. [32] |
| S0650 | QakBot | QakBot can enumerate a list of installed programs. [33] |
| S1148 | Raccoon Stealer | Raccoon Stealer is capable of identifying running software on victim machines. [34] [35] |
| S1240 | RedLine Stealer | RedLine Stealer can get a list of programs on the victim device. [36] |
| S0148 | RTM | RTM can scan victim drives to look for specific banking software on the machine to determine next actions. [37] |
| S1099 | Samurai | Samurai can check for the presence and version of the .NET framework. [38] |
| S0445 | ShimRatReporter | ShimRatReporter gathered a list of installed software on the infected host. [39] |
| G1008 | SideCopy | SideCopy has collected browser information from a compromised host. [40] |
| G0121 | Sidewinder | Sidewinder has used tools to enumerate software installed on an infected host. [41] [42] |
| S0623 | Siloscape | Siloscape searches for the kubectl binary. [43] |
| S1124 | SocGholish | SocGholish can identify the victim's browser in order to serve the correct fake update page. [44] |
| S0646 | SpicyOmelette | SpicyOmelette can enumerate running software on a targeted system. [45] |
| S1183 | StrelaStealer | StrelaStealer variants use COM objects to enumerate installed applications from the "AppsFolder" on victim machines. [46] |
| S1042 | SUGARDUMP | SUGARDUMP can identify Chrome, Opera, Edge Chromium, and Firefox browsers, including version number, on a compromised host. [47] |
| S1064 | SVCReady | SVCReady can collect a list of installed software from an infected host. [48] |
| S0467 | TajMahal | TajMahal has the ability to identify the Internet Explorer (IE) version on an infected host. [49] |
| G0081 | Tropic Trooper | Tropic Trooper 's backdoor could list the infected system's installed software. [50] |
| G1017 | Volt Typhoon | Volt Typhoon has queried the Registry on compromised systems for information on installed software. [51] [52] |
| G0124 | Windigo | Windigo has used a script to detect installed software on targeted systems. [53] |
| G0112 | Windshift | Windshift has used malware to identify installed software. [54] |
| S1065 | Woody RAT | Woody RAT can collect .NET, PowerShell, and Python information from an infected host. [55] |
| S0658 | XCSSET | XCSSET uses ps aux with the grep command to enumerate common browsers and system processes potentially impacting XCSSET 's exfiltration capabilities. [56] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0392 | Multi-Platform Software Discovery Behavior Chain | AN1100 | Adversary spawns a process or script to enumerate installed software using WMI, registry, or PowerShell, potentially followed by additional discovery or evasion behavior. |
| AN1101 | Adversary invokes 'dpkg -l', 'rpm -qa', or other package managers via shell or script to enumerate installed software. |  |  |
| AN1102 | Adversary runs 'system_profiler SPApplicationsDataType' or queries plist files to enumerate software via Terminal or scripts. |  |  |
| AN1103 | Adversary uses cloud-native APIs or CLI (e.g., AWS Systems Manager, Azure Resource Graph) to list installed software on cloud workloads. |  |  |
| AN1104 | Adversary uses 'esxcli software vib list' to enumerate installed VIBs, drivers, and modules. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0392 | Multi-Platform Software Discovery Behavior Chain | AN1100 | Adversary spawns a process or script to enumerate installed software using WMI, registry, or PowerShell, potentially followed by additional discovery or evasion behavior. |
| AN1101 | Adversary invokes 'dpkg -l', 'rpm -qa', or other package managers via shell or script to enumerate installed software. |  |  |
| AN1102 | Adversary runs 'system_profiler SPApplicationsDataType' or queries plist files to enumerate software via Terminal or scripts. |  |  |
| AN1103 | Adversary uses cloud-native APIs or CLI (e.g., AWS Systems Manager, Azure Resource Graph) to list installed software on cloud workloads. |  |  |
| AN1104 | Adversary uses 'esxcli software vib list' to enumerate installed VIBs, drivers, and modules. |  |  |

---

## References

- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [Sushko, O. (2019, April 17). macOS Bundlore: Mac Virus Bypassing macOS Security Features. Retrieved June 30, 2020.](https://mackeeper.com/blog/post/610-macos-bundlore-adware-analysis/)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [Kohler, A. and Lopez, C. (2024, April 30). Malware: Cuckoo Behaves Like Cross Between Infostealer and Spyware. Retrieved August 20, 2024.](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
- [Check Point Research. (2021, January 4). Stopping Serial Killer: Catching the Next Strike. Retrieved September 7, 2021.](https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/)
- [GReAT. (2019, April 10). Gaza Cybergang Group1, operation SneakyPastes. Retrieved May 13, 2020.](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
- [hasherezade. (2015, November 4). A Technical Look At Dyreza. Retrieved June 15, 2020.](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
- [Gal Hachamov. (2025, December 29). GlassWorm Goes Mac: Fresh Infrastructure, New Tricks. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Knight, S.. (2020, April 16). VMware Carbon Black TAU Threat Analysis: The Evolution of Lazarus. Retrieved May 1, 2020.](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
- [Symantec. (2018, March 14). Inception Framework: Alive and Well, and Hiding Behind Proxies. Retrieved May 8, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/inception-framework-hiding-behind-proxies)
- [Seongsu Park. (2024, November 4). From Pyongyang to Your Payroll: The Rise of North Korean Remote Workers in the West. Retrieved October 17, 2025.](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Check Point. (2024, November 12). Hamas-affiliated Threat Actor WIRTE Continues its Middle East Operations and Moves to Disruptive Activity. Retrieved April 20, 2026.](https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/)
- [Hromcova, Z. and Burgher, A. (2023, September 21). OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes. Retrieved November 21, 2024.](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
- [Dahan, A. et al. (2020, November 2). Back to the Future: Inside the Kimsuky KGH Spyware Suite. Retrieved November 6, 2020.](https://www.cybereason.com/blog/back-to-the-future-inside-the-kimsuky-kgh-spyware-suite)
- [Stuart Ashenbrenner, Alden Schmidt. (2024, April 25). LightSpy Malware Variant Targeting macOS. Retrieved January 3, 2025.](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [GReAT. (2021, June 16). Ferocious Kitten: 6 Years of Covert Surveillance in Iran. Retrieved September 22, 2021.](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
- [Sierra, E., Iglesias, G.. (2018, April 24). Metamorfo Campaigns Targeting Brazilian Users. Retrieved July 30, 2020.](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
- [ESET Research. (2019, October 3). Casbaneiro: peculiarities of this banking Trojan that affects Brazil and Mexico. Retrieved September 23, 2021.](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
- [Peretz, A. and Theck, E. (2021, March 5). Earth Vetala – MuddyWater Continues to Target Organizations in the Middle East. Retrieved March 18, 2021.](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
- [Anomali Threat Research. (2019, October 7). China-Based APT Mustang Panda Targets Minority Groups, Public and Private Sector Organizations. Retrieved April 12, 2021.](https://www.anomali.com/blog/china-based-apt-mustang-panda-targets-minority-groups-public-and-private-sector-organizations)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
- [ANSSI. (2021, January 27). SANDWORM INTRUSION SET CAMPAIGN TARGETING CENTREON SYSTEMS. Retrieved March 30, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-005.pdf)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Group IB. (2020, September). LOCK LIKE A PRO. Retrieved November 17, 2024.](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
- [Quentin Bourgue, Pierre le Bourhis, & Sekoia TDR. (2022, June 28). Raccoon Stealer v2 - Part 1: The return of the dead. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Splunk Threat Research Team. (2023, June 1). Do Not Cross The 'RedLine' Stealer: Detections and Analysis. Retrieved September 17, 2025.](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
- [Faou, M. and Boutin, J. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [Hegel, T. (2021, January 13). A Global Perspective of the SideWinder APT. Retrieved January 27, 2021.](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)
- [Rewterz. (2020, April 20). Sidewinder APT Group Campaign Analysis. Retrieved January 29, 2021.](https://www.rewterz.com/threats/sidewinder-apt-group-campaign-analysis)
- [Prizmant, D. (2021, June 7). Siloscape: First Known Malware Targeting Windows Containers to Compromise Cloud Environments. Retrieved June 9, 2021.](https://unit42.paloaltonetworks.com/siloscape/)
- [Secureworks. (n.d.). GOLD PRELUDE . Retrieved March 22, 2024.](https://www.secureworks.com/research/threat-profiles/gold-prelude)
- [CTU. (2018, September 27). Cybercriminals Increasingly Trying to Ensnare the Big Financial Fish. Retrieved September 20, 2021.](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)
- [Golo Mühr, Joe Fasulo & Charlotte Hammond, IBM X-Force. (2024, November 12). Strela Stealer: Today’s invoice is tomorrow’s phish. Retrieved December 31, 2024.](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
- [Mandiant Israel Research Team. (2022, August 17). Suspected Iranian Actor Targeting Israeli Shipping, Healthcare, Government and Energy Sectors. Retrieved September 21, 2022.](https://www.mandiant.com/resources/blog/suspected-iranian-actor-targeting-israeli-shipping)
- [Schlapfer, Patrick. (2022, June 6). A New Loader Gets Ready. Retrieved December 13, 2022.](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [NSA et al. (2023, May 24). People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection. Retrieved July 27, 2023.](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [The BlackBerry Research & Intelligence Team. (2020, October). BAHAMUT: Hack-for-Hire Masters of Phishing, Fake News, and Fake Apps. Retrieved February 8, 2021.](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Mac Threat Response, Mobile Research Team. (2020, August 13). The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSS Backdoor Planting in Safari, and Leverages Two Zero-day Exploits. Retrieved October 5, 2021.](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)

---

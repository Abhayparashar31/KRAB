# Application Window Discovery

## Description

Adversaries may attempt to get a listing of open application windows. Window listings could convey information about how the system is used. [1] For example, information about application windows could be used identify potential data to collect as well as identifying security tooling ( Security Software Discovery ) to evade. [2]

Adversaries typically abuse system features for this type of enumeration. For example, they may gather information through native system features such as Command and Scripting Interpreter commands and Native API functions.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0456 | Aria-body | Aria-body has the ability to identify the titles of running windows on a compromised host. [3] |
| S0438 | Attor | Attor can obtain application window titles and then determines which windows to perform Screen Capture on. [4] |
| S0454 | Cadelspy | Cadelspy has the ability to identify open windows on the compromised host. [5] |
| S0261 | Catchamas | Catchamas obtains application windows titles and then determines which windows to perform Screen Capture on. [6] |
| S1111 | DarkGate | DarkGate will search for cryptocurrency wallets by examining application window names for specific strings. [7] DarkGate extracts information collected via NirSoft tools from the hosting process's memory by first identifying the window through the FindWindow API function. [7] |
| S0673 | DarkWatchman | DarkWatchman reports window names along with keylogger information to provide application context. [1] |
| S0038 | Duqu | The discovery modules used with Duqu can collect information on open windows. [8] |
| S1159 | DUSTTRAP | DUSTTRAP can enumerate running application windows. [9] |
| S0696 | Flagpro | Flagpro can check the name of the window displayed on the system. [10] |
| S1044 | FunnyDream | FunnyDream has the ability to discover application windows via execution of EnumWindows . [11] |
| S0531 | Grandoreiro | Grandoreiro can identify installed security tools based on window names. [2] |
| G1001 | HEXANE | HEXANE has used a PowerShell-based keylogging tool to capture the window title. [12] |
| S0431 | HotCroissant | HotCroissant has the ability to list the names of all open windows on the infected host. [13] |
| S0260 | InvisiMole | InvisiMole can enumerate windows and child windows on a compromised host. [14] [15] |
| S0265 | Kazuar | Kazuar gathers information about opened windows. [16] |
| G0032 | Lazarus Group | Lazarus Group malware IndiaIndia obtains and sends to its C2 server the title of the window for each running process. The KilaAlfa keylogger also reports the title of the window in the foreground. [17] [18] [19] |
| S0409 | Machete | Machete saves the window names. [20] |
| S0455 | Metamorfo | Metamorfo can enumerate all windows on the victim’s machine. [21] [22] |
| S0033 | NetTraveler | NetTraveler reports window names along with keylogger information to provide application context. [23] |
| S0198 | NETWIRE | NETWIRE can discover and close windows on controlled systems. [24] |
| S1090 | NightClub | NightClub can use GetForegroundWindow to enumerate the active window. [25] |
| S0385 | njRAT | njRAT gathers information about opened windows during the initial infection. [26] |
| S1233 | PAKLOG | PAKLOG has used GetForegroundWindow to access the foreground window. [27] PAKLOG has also captured text from the foreground windows. [27] |
| S0435 | PLEAD | PLEAD has the ability to list open windows on the compromised host. [28] [28] |
| S0012 | PoisonIvy | PoisonIvy captures window titles. [29] |
| S0139 | PowerDuke | PowerDuke has a command to get text of the current foreground window. [30] |
| S0650 | QakBot | QakBot has the ability to enumerate windows on a compromised host. [31] |
| S0262 | QuasarRAT | APT-C-36 used a customized version of QuasarRAT to monitor browser windows for strings relating to specific Colombian financial institutions. [32] |
| S0332 | Remcos | Remcos can list all windows on victim systems. [33] |
| S0375 | Remexi | Remexi has a command to capture active windows on the machine and retrieve window titles. [34] |
| S0240 | ROKRAT | ROKRAT can use the GetForegroundWindow and GetWindowText APIs to discover where the user is typing. [35] |
| S0692 | SILENTTRINITY | SILENTTRINITY can enumerate the active Window during keylogging through execution of GetActiveWindowTitle . [36] |
| S0157 | SOUNDBITE | SOUNDBITE is capable of enumerating application windows. [37] |
| S1239 | TONESHELL | TONESHELL has used GetForegroundWindow to detect virtualization or sandboxes by calling the API twice and comparing each window handle. [38] |
| S0094 | Trojan.Karagany | Trojan.Karagany can monitor the titles of open windows to identify specific keywords. [39] |
| G1017 | Volt Typhoon | Volt Typhoon has collected window title information from compromised systems. [40] |
| S0219 | WINERACK | WINERACK can enumerate active windows. [41] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0097 | Detection of Application Window Enumeration via API or Scripting | AN0271 | Processes using Win32 API calls (e.g., EnumWindows, GetForegroundWindow) or scripting tools (e.g., PowerShell, VBScript) to enumerate open windows. These often appear with reconnaissance or data collection TTPs. |
| AN0272 | Scripted or binary usage of X11 utilities (e.g., xdotool, wmctrl) or direct /proc/*/window mappings to discover open GUI windows and active desktops. |  |  |
| AN0273 | Processes that utilize AppleScript, CGWindowListCopyWindowInfo , or NSRunningApplication APIs to list active application windows and foreground processes. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0097 | Detection of Application Window Enumeration via API or Scripting | AN0271 | Processes using Win32 API calls (e.g., EnumWindows, GetForegroundWindow) or scripting tools (e.g., PowerShell, VBScript) to enumerate open windows. These often appear with reconnaissance or data collection TTPs. |
| AN0272 | Scripted or binary usage of X11 utilities (e.g., xdotool, wmctrl) or direct /proc/*/window mappings to discover open GUI windows and active desktops. |  |  |
| AN0273 | Processes that utilize AppleScript, CGWindowListCopyWindowInfo , or NSRunningApplication APIs to list active application windows and foreground processes. |  |  |

---

## References

- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [Symantec Security Response. (2015, December 7). Iran-based attackers use back door threats to spy on Middle Eastern targets. Retrieved April 17, 2019.](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
- [Balanza, M. (2018, April 02). Infostealer.Catchamas. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165711/https://www-west.symantec.com/content/symantec/english/en/security-center/writeup.html/2018-040209-1742-99)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Symantec Security Response. (2011, November). W32.Duqu: The precursor to the next Stuxnet. Retrieved September 17, 2015.](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [SecureWorks 2019, August 27 LYCEUM Takes Center Stage in Middle East Campaign Retrieved. 2019/11/19](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)
- [Knight, S.. (2020, April 16). VMware Carbon Black TAU Threat Analysis: The Evolution of Lazarus. Retrieved May 1, 2020.](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Tools Report. Retrieved March 10, 2016.](https://web.archive.org/web/20220425194457/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Tools-Report.pdf)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [Sierra, E., Iglesias, G.. (2018, April 24). Metamorfo Campaigns Targeting Brazilian Users. Retrieved July 30, 2020.](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
- [Zhang, X. (2020, February 4). Another Metamorfo Variant Targeting Customers of Financial Institutions in More Countries. Retrieved July 30, 2020.](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
- [Kaspersky Lab's Global Research and Analysis Team. (n.d.). The NetTraveler (aka ‘Travnet’). Retrieved November 17, 2024.](https://web.archive.org/web/20160326004042/http://kasperskycontenthub.com/wp-content/uploads/sites/43/vlpdfs/kaspersky-the-net-traveler-part1-final.pdf)
- [Lambert, T. (2020, January 29). Intro to Netwire. Retrieved January 7, 2021.](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Fidelis Cybersecurity. (2013, June 28). Fidelis Threat Advisory #1009: "njRAT" Uncovered. Retrieved June 4, 2019.](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
- [Sudeep Singh. (2025, April 16). Latest Mustang Panda Arsenal: PAKLOG, CorKLOG, and SplatCloak | P2. Retrieved September 12, 2025.](https://www.zscaler.com/blogs/security-research/latest-mustang-panda-arsenal-paklog-corklog-and-splatcloak-p2)
- [Bermejo, L., et al. (2017, June 22). Following the Trail of BlackTech’s Cyber Espionage Campaigns. Retrieved May 5, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
- [Hayashi, K. (2005, August 18). Backdoor.Darkmoon. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2005-081910-3934-99)
- [Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
- [Morrow, D. (2021, April 15). The rise of QakBot. Retrieved September 27, 2021.](https://cybersecurity.att.com/blogs/labs-research/the-rise-of-qakbot)
- [Global Research & Analysis Team, Kaspersky. (2024, August 19). BlindEagle flying high in Latin America. Retrieved April 16, 2026.](https://securelist.com/blindeagle-apt/113414/)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Legezo, D. (2019, January 30). Chafer used Remexi malware to spy on Iran-based foreign diplomatic entities. Retrieved April 17, 2019.](https://securelist.com/chafer-used-remexi-malware/89538/)
- [Mercer, W., Rascagneres, P. (2017, April 03). Introducing ROKRAT. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)
- [Salvati, M. (2019, August 6). SILENTTRINITY Modules. Retrieved March 24, 2022.](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
- [Carr, N.. (2017, May 14). Cyber Espionage is Alive and Well: APT32 and the Threat to Global Corporations. Retrieved June 18, 2017.](https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html)
- [Nick Dai, Vickie Su, Sunny Lu. (2022, November 18). Earth Preta Spear-Phishing Governments Worldwide. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/22/k/earth-preta-spear-phishing-governments-worldwide.html)
- [Secureworks. (2019, July 24). Updated Karagany Malware Targets Energy Sector. Retrieved August 12, 2020.](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)

---

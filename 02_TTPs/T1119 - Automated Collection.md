# Automated Collection

## Description

Once established within a system or network, an adversary may use automated techniques for collecting internal data. Methods for performing this technique could include use of a Command and Scripting Interpreter to search for and copy information fitting set criteria such as file type, location, or name at specific time intervals.

In cloud-based environments, adversaries may also use cloud APIs, data pipelines, command line interfaces, or extract, transform, and load (ETL) services to automatically collect data. [1]

This functionality could also be built into remote access tools.

This technique may incorporate use of other techniques such as File and Directory Discovery and Lateral Tool Transfer to identify and move files, as well as Cloud Service Dashboard and Cloud Storage Object Discovery to identify resources in cloud environments.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1030 | Agrius | Agrius used a custom tool, sql.net4.exe , to query SQL databases and then identify and extract personally identifiable information. [2] |
| C0062 | Anthropic AI-orchestrated Campaign | During the Anthropic AI-orchestrated Campaign , the adversary used Claude Code to automatically collect and process large volumes of data from without human direction. [3] |
| S0622 | AppleSeed | AppleSeed has automatically collected data from USB drives, keystrokes, and screen images before exfiltration. [4] |
| G0006 | APT1 | APT1 used a batch script to perform a series of discovery techniques and saves it to a text file. [5] |
| G0007 | APT28 | APT28 used a publicly available tool to gather and compress multiple documents on the DCCC and DNC networks. [6] |
| C0040 | APT41 DUST | APT41 DUST used tools such as SQLULDR2 and PINEGROVE to gather local system and database information. [7] |
| C0046 | ArcaneDoor | ArcaneDoor included collection of packet capture and system configuration information. [8] |
| S0438 | Attor | Attor has automatically collected data about the compromised system. [9] |
| S0128 | BADNEWS | BADNEWS monitors USB devices and copies files with certain extensions to a predefined directory. [10] |
| S0239 | Bankshot | Bankshot recursively generates a list of files within a directory and sends them back to the control server. [11] |
| S1043 | ccf32 | ccf32 can be used to automatically collect files from a compromised host. [12] |
| G0114 | Chimera | Chimera has used custom DLLs for continuous retrieval of data from memory. [13] |
| S0244 | Comnie | Comnie executes a batch script to store discovery information in %TEMP%\info.dat and then uploads the temporarily file to the remote C2 server. [14] |
| G0142 | Confucius | Confucius has used a file stealer to steal documents and images with the following extensions: txt, pdf, png, jpg, doc, xls, xlm, odp, ods, odt, rtf, ppt, xlsx, xlsm, docx, pptx, and jpeg. [15] |
| S0538 | Crutch | Crutch can automatically monitor removable drives in a loop and copy interesting files. [16] |
| S1111 | DarkGate | DarkGate searches for stored credentials associated with cryptocurrency wallets and notifies the command and control server when identified. [17] |
| G1003 | Ember Bear | Ember Bear engages in mass collection from compromised systems during intrusions. [18] |
| S0363 | Empire | Empire can automatically gather the username, domain name, machine name, and other information from a compromised system. [19] |
| G0053 | FIN5 | FIN5 scans processes on all victim systems in the environment and uses automated scripts to pull back the results. [20] |
| G0037 | FIN6 | FIN6 has used a script to iterate through a list of compromised PoS systems, copy and remove data to a log file, and to bind to events from the submit payment button. [21] [22] |
| C0001 | Frankenstein | During Frankenstein , the threat actors used Empire to automatically gather the username, domain name, machine name, and other system information. [19] |
| S1044 | FunnyDream | FunnyDream can monitor files for changes and automatically collect them. [12] |
| G0047 | Gamaredon Group | Gamaredon Group has deployed scripts on compromised systems that automatically scan for interesting documents. [23] |
| S0597 | GoldFinder | GoldFinder logged and stored information related to the route or hops a packet took from a compromised machine to a hardcoded C2 server, including the target C2 URL, HTTP response/status code, HTTP response headers and values, and data received from the C2 node. [24] |
| G0125 | HAFNIUM | HAFNIUM has used MSGraph to exfiltrate data from email, OneDrive, and SharePoint. [25] |
| S0170 | Helminth | A Helminth VBScript receives a batch script to execute a set of commands in a command prompt. [26] |
| S0260 | InvisiMole | InvisiMole can sort and collect specific documents as well as generate a list of all files on a newly inserted drive and store them in an encrypted file. [27] [28] |
| G0004 | Ke3chang | Ke3chang has performed frequent and scheduled data collection from victim networks. [29] |
| S9035 | LAMEHUG | LAMEHUG can recursively copy files from targeted directories on victim hosts. [30] [31] |
| S0395 | LightNeuron | LightNeuron can be configured to automatically collect files under a specified directory. [32] |
| S1101 | LoFiSe | LoFiSe can collect all the files from the working directory every three hours and place them into a password-protected archive for further exfiltration. [33] |
| S1213 | Lumma Stealer | Lumma Stealer has automated collection of various information including cryptocurrency wallet details. [34] |
| G0045 | menuPass | menuPass has used the Csvde tool to collect Active Directory files and data. [35] |
| S0443 | MESSAGETAP | MESSAGETAP checks two files, keyword_parm.txt and parm.txt, for instructions on how to target and save data parsed and extracted from SMS message data from the network traffic. If an SMS message contained either a phone number, IMSI number, or keyword that matched the predefined list, it is saved to a CSV file for later theft by the threat actor. [36] |
| S0455 | Metamorfo | Metamorfo has automatically collected mouse clicks, continuous screenshots on the machine, and set timers to collect the contents of the clipboard and website browsing. [37] |
| S0339 | Micropsia | Micropsia executes an RAR tool to recursively archive files based on a predefined list of file extensions ( .xls, .xlsx, .csv, .odt, .doc, .docx, .ppt, .pptx, .pdf, .mdb, .accdb, .accde, *.txt). [38] |
| G0129 | Mustang Panda | Mustang Panda used custom batch scripts to collect files automatically from a targeted system. [39] |
| S0699 | Mythic | Mythic supports scripting of file downloads from agents. [40] |
| S0198 | NETWIRE | NETWIRE can automatically archive collected data. [41] |
| S1131 | NPPSPY | NPPSPY collection is automatically recorded to a specified file on the victim machine. [42] |
| G0049 | OilRig | OilRig has used automated collection. [43] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors used a script to collect information about the infected system. [44] |
| S1017 | OutSteel | OutSteel can automatically scan for and collect files with specific extensions. [45] |
| S1109 | PACEMAKER | PACEMAKER can enter a loop to read /proc/ entries every 2 seconds in order to read a target application's memory. [46] |
| S1091 | Pacu | Pacu can automatically collect data, such as CloudFormation templates, EC2 user data, AWS Inspector reports, and IAM credential reports. [47] |
| G0040 | Patchwork | Patchwork developed a file stealer to search C:\ and collect files with certain extensions. Patchwork also executed a script to enumerate all drives, store them as a list, and upload generated files to the C2 server. [10] |
| S0428 | PoetRAT | PoetRAT used file system monitoring to track modification and enable automatic exfiltration. [48] |
| S0378 | PoshC2 | PoshC2 contains a module for recursively parsing through files and directories to gather valid credit card numbers. [49] |
| S0238 | Proxysvc | Proxysvc automatically collects data about the victim and sends it to the control server. [50] |
| S1148 | Raccoon Stealer | Raccoon Stealer collects files and directories from victim systems based on configuration data downloaded from command and control servers. [51] [52] [53] |
| S0458 | Ramsay | Ramsay can conduct an initial scan for Microsoft Word documents on the local system, removable media, and connected network drives, before tagging and collecting them. It can continue tagging documents to collect with follow up scans. [54] |
| G1039 | RedCurl | RedCurl has used batch scripts to collect data. [55] [56] |
| S0684 | ROADTools | ROADTools automatically gathers data from Azure AD environments using the Azure Graph API. [57] |
| S1078 | RotaJakiro | Depending on the Linux distribution, RotaJakiro executes a set of commands to collect device information and sends the collected information to the C2 server. [58] |
| S0090 | Rover | Rover automatically collects files from the local system and removable drives based on a predefined list of file extensions on a regular timeframe. [59] |
| S0148 | RTM | RTM monitors browsing activity and automatically captures screenshots if a victim browses to a URL matching one of a list of strings. [60] [61] |
| S9008 | Shai-Hulud | Shai-Hulud has the ability to automatically collect host data, secrets, system information, and endpoints. [62] [63] [64] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors used a command shell to automatically iterate through web.config files to expose and collect machineKey settings. [65] [66] |
| S0445 | ShimRatReporter | ShimRatReporter gathered information automatically, without instruction from a C2, related to the user and host machine that is compiled into a report and sent to the operators. [67] |
| G0121 | Sidewinder | Sidewinder has used tools to automatically collect system and network configuration information. [68] |
| S1183 | StrelaStealer | StrelaStealer attempts to identify and collect mail login data from Thunderbird and Outlook following execution. [69] [70] [71] [72] |
| S0491 | StrongPity | StrongPity has a file searcher component that can automatically collect and archive files based on a predefined list of file extensions. [73] |
| S0098 | T9000 | T9000 searches removable storage devices for files with a pre-defined list of file extensions (e.g. * .doc, .ppt, .xls, .docx, .pptx, *.xlsx). Any matching files are encrypted and written to a local user directory. [74] |
| S0467 | TajMahal | TajMahal has the ability to index and compress files into a send queue for exfiltration. [75] |
| G0027 | Threat Group-3390 | Threat Group-3390 ran a command to compile an archive of file types of interest from the victim user's directories. [76] |
| G0081 | Tropic Trooper | Tropic Trooper has collected information automatically using the adversary's USBferry attack. [77] |
| S0136 | USBStealer | For all non-removable drives on a victim, USBStealer executes automated collection of certain files for later exfiltration. [78] |
| S0476 | Valak | Valak can download a module to search for and build a report of harvested credential data. [79] |
| S0257 | VERMIN | VERMIN saves each collected file with the automatically generated format {0:dd-MM-yyyy}.txt . [80] |
| G1055 | VOID MANTICORE | VOID MANTICORE conducted large-scale data exfiltration in the Stryker operation, consistent with automated or scripted collection against enterprise systems. [81] |
| S0466 | WindTail | WindTail can identify and add files that possess specific file extensions to an array for archiving. [82] |
| G1035 | Winter Vivern | Winter Vivern delivered a PowerShell script capable of recursively scanning victim machines looking for various file types before exfiltrating identified files via HTTP. [83] |
| S0251 | Zebrocy | Zebrocy scans the system and automatically collects files with the following extensions: .doc, .docx, ,.xls, .xlsx, .pdf, .pptx, .rar, .zip, .jpg, .jpeg, .bmp, .tiff, .kum, .tlg, .sbx, .cr, .hse, .hsf, and .lhz. [84] [85] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1041 | Encrypt Sensitive Information | Encryption and off-system storage of sensitive information may be one way to mitigate collection of files, but may not stop an adversary from acquiring the information if an intrusion persists over a long period of time and the adversary is able to discover and access the data through other means. Strong passwords should be used on certain encrypted documents that use them to prevent offline cracking through Brute Force techniques. |
| M1029 | Remote Data Storage | Encryption and off-system storage of sensitive information may be one way to mitigate collection of files, but may not stop an adversary from acquiring the information if an intrusion persists over a long period of time and the adversary is able to discover and access the data through other means. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0186 | Automated File and API Collection Detection Across Platforms | AN0531 | Automated execution of native utilities and scripts to discover, enumerate, and exfiltrate files and clipboard content. Focus is on detecting repeated file access, scripting engine use, and use of command-line utilities commonly leveraged by collection scripts. |
| AN0532 | Repeated or automated access to user document directories or clipboard using shell scripts or utilities like xclip/pbpaste. Detectable via auditd syscall logs or osquery file events. |  |  |
| AN0533 | Use of pbpaste, AppleScript, or third-party automation frameworks (e.g., Automator) to collect clipboard or file content in bursts. Observable via unified logs. |  |  |
| AN0534 | Suspicious sign-ins to Graph API or sensitive resources using non-browser scripting agents (e.g., Python, PowerShell), often for programmatic access to mailbox or OneDrive content. |  |  |

---

## References

- [Mandiant Intelligence. (2023, September 14). Why Are You Texting Me? UNC3944 Leverages SMS Phishing Campaigns for SIM Swapping, Ransomware, Extortion, and Notoriety. Retrieved January 2, 2024.](https://www.mandiant.com/resources/blog/unc3944-sms-phishing-sim-swapping-ransomware)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [Anthropic. (2025, November). Disrupting the first reported AI-orchestrated cyber espionage campaign. Retrieved April 20, 2026.](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
- [KISA. (2021). Phishing Target Reconnaissance and Attack Resource Analysis Operation Muzabi. Retrieved March 8, 2024.](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved November 17, 2024.](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Canadian Centre for Cyber Security. (2024, April 24). Cyber Activity Impacting CISCO ASA VPNs. Retrieved January 6, 2025.](https://www.cyber.gc.ca/en/news-events/cyber-activity-impacting-cisco-asa-vpns)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
- [Sherstobitoff, R. (2018, March 08). Hidden Cobra Targets Turkish Financial Sector With New Bankshot Implant. Retrieved May 18, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Grunzweig, J. (2018, January 31). Comnie Continues to Target Organizations in East Asia. Retrieved June 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
- [Lunghi, D. (2021, August 17). Confucius Uses Pegasus Spyware-related Lures to Target Pakistani Military. Retrieved December 26, 2021.](https://www.trendmicro.com/en_us/research/21/h/confucius-uses-pegasus-spyware-related-lures-to-target-pakistani.html)
- [Faou, M. (2020, December 2). Turla Crutch: Keeping the “back door” open. Retrieved December 4, 2020.](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Microsoft Threat Intelligence. (2023, June 14). Cadet Blizzard emerges as a novel and distinct Russian threat actor. Retrieved July 10, 2023.](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)
- [Adamitis, D. et al. (2019, June 4). It's alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign. Retrieved May 11, 2020.](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
- [Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.](https://www.youtube.com/watch?v=fevGZs0EQu8)
- [FireEye Threat Intelligence. (2016, April). Follow the Money: Dissecting the Operations of the Cyber Crime Group FIN6. Retrieved November 17, 2024.](https://web.archive.org/web/20190807112824/https://www2.fireeye.com/rs/848-DID-242/images/rpt-fin6.pdf)
- [Chen, J. (2019, October 10). Magecart Card Skimmers Injected Into Online Shops. Retrieved September 9, 2020.](https://www.trendmicro.com/en_us/research/19/j/fin6-compromised-e-commerce-platform-via-magecart-to-inject-credit-card-skimmers-into-thousands-of-online-shops.html)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [Microsoft Threat Intelligence . (2025, March 5). Silk Typhoon targeting IT supply chain. Retrieved March 20, 2025.](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/)
- [Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Conteras, T., Splunk Research Team. (2025, September 25). From Prompt to Payload: LAMEHUG’s LLM-Driven Cyber Intrusion. Retrieved April 21, 2026.](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
- [Google Threat Intelligence Group. (2025, November 5). GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools. Retrieved March 31, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
- [Faou, M. (2019, May). Turla LightNeuron: One email away from remote code execution. Retrieved June 24, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [Cybereaon Security Services Team. (n.d.). Your Data Is Under New Lummanagement: The Rise of LummaStealer. Retrieved March 22, 2025.](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)
- [Symantec. (2020, November 17). Japan-Linked Organizations Targeted in Long-Running and Sophisticated Attack Campaign. Retrieved December 17, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)
- [Leong, R., Perez, D., Dean, T. (2019, October 31). MESSAGETAP: Who’s Reading Your Text Messages?. Retrieved May 11, 2020.](https://www.fireeye.com/blog/threat-research/2019/10/messagetap-who-is-reading-your-text-messages.html)
- [Sierra, E., Iglesias, G.. (2018, April 24). Metamorfo Campaigns Targeting Brazilian Users. Retrieved July 30, 2020.](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
- [Tsarfaty, Y. (2018, July 25). Micropsia Malware. Retrieved November 13, 2018.](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
- [Counter Threat Unit Research Team. (2019, December 29). BRONZE PRESIDENT Targets NGOs. Retrieved April 13, 2021.](https://www.secureworks.com/research/bronze-president-targets-ngos)
- [Thomas, C. (n.d.). Mythc Documentation. Retrieved March 25, 2022.](https://docs.mythic-c2.net/)
- [Lambert, T. (2020, January 29). Intro to Netwire. Retrieved January 7, 2021.](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
- [Dray Agha. (2022, August 16). Cleartext Shenanigans: Gifting User Passwords to Adversaries With NPPSPY. Retrieved May 17, 2024.](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
- [Unit42. (2016, May 1). Evasive Serpens Unit 42 Playbook Viewer. Retrieved February 6, 2023.](https://pan-unit42.github.io/playbook_viewer/?pb=evasive-serpens)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Perez, D. et al. (2021, April 20). Check Your Pulse: Suspected APT Actors Leverage Authentication Bypass Techniques and Pulse Secure Zero-Day. Retrieved February 5, 2024.](https://www.mandiant.com/resources/blog/suspected-apt-actors-leverage-bypass-techniques-pulse-secure-zero-day)
- [Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.](https://github.com/RhinoSecurityLabs/pacu)
- [Mercer, W, et al. (2020, April 16). PoetRAT: Python RAT uses COVID-19 lures to target Azerbaijan public and private sectors. Retrieved April 27, 2020.](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
- [S2W TALON. (2022, June 16). Raccoon Stealer is Back with a New Version. Retrieved August 1, 2024.](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
- [Quentin Bourgue, Pierre le Bourhis, & Sekoia TDR. (2022, June 28). Raccoon Stealer v2 - Part 1: The return of the dead. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Group-IB. (2020, August). RedCurl: The Pentest You Didn’t Know About. Retrieved August 9, 2024.](https://www.group-ib.com/resources/research-hub/red-curl/)
- [Group-IB. (2021, November). RedCurl: The Awakening. Retrieved August 14, 2024.](https://www.group-ib.com/resources/research-hub/red-curl-2/)
- [Dirk-jan Mollema. (2020, April 16). Introducing ROADtools - The Azure AD exploration framework. Retrieved January 31, 2022.](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)
- [Alex Turing, Hui Wang. (2021, April 28). RotaJakiro: A long live secret backdoor with 0 VT detection. Retrieved June 14, 2023.](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
- [Ray, V., Hayashi, K. (2016, February 29). New Malware ‘Rover’ Targets Indian Ambassador to Afghanistan. Retrieved February 29, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
- [Faou, M. and Boutin, J. (2017, February). Read The Manual: A Guide to the RTM Banking Trojan. Retrieved March 9, 2017.](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
- [Duncan, B., Harbison, M. (2019, January 23). Russian Language Malspam Pushing Redaman Banking Malware. Retrieved June 16, 2020.](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
- [Charlie Eriksen. (2025, September 16). S1ngularity/nx attackers strike again. Retrieved April 9, 2026.](https://www.aikido.dev/blog/s1ngularity-nx-attackers-strike-again)
- [Gianpietro Cutolo. (2025, November 26). Shai-Hulud 2.0: Aggressive, Automated, and Fast Spreading. Retrieved April 9, 2026.](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
- [Microsoft Defender Security Team. (n.d.). Shai-Hulud 2.0: Guidance for detecting, investigating, and defending against the supply chain attack. Retrieved April 9, 2026.](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/)
- [Trend Micro Research. (2022, July 22). Proactive Security Insights for SharePoint Attacks (CVE-2025-53770 and CVE-2025-53771). Retrieved October 15, 2025.](https://www.trendmicro.com/en_us/research/25/g/cve-2025-53770-and-cve-2025-53771-sharepoint-attacks.html)
- [Unit 42. (2025, July 31). Active Exploitation of Microsoft SharePoint Vulnerabilities: Threat Brief (Updated). Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/microsoft-sharepoint-cve-2025-49704-cve-2025-49706-cve-2025-53770/)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Hegel, T. (2021, January 13). A Global Perspective of the SideWinder APT. Retrieved January 27, 2021.](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)
- [DCSO CyTec Blog. (2022, November 8). #ShortAndMalicious: StrelaStealer aims for mail credentials. Retrieved December 31, 2024.](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)
- [Benjamin Chang, Goutam Tripathy, Pranay Kumar Chhaparwal, Anmol Maurya & Vishwa Thothathri, Palo Alto Networks. (2024, March 22). Large-Scale StrelaStealer Campaign in Early 2024. Retrieved December 31, 2024.](https://unit42.paloaltonetworks.com/strelastealer-campaign/)
- [Fortgale. (2023, September 18). StrelaStealer Malware Analysis. Retrieved December 31, 2024.](https://fortgale.com/blog/malware-analysis/strelastealer-malware-analysis-2/)
- [Golo Mühr, Joe Fasulo & Charlotte Hammond, IBM X-Force. (2024, November 12). Strela Stealer: Today’s invoice is tomorrow’s phish. Retrieved December 31, 2024.](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
- [Tudorica, R. et al. (2020, June 30). StrongPity APT - Revealing Trojanized Tools, Working Hours and Infrastructure. Retrieved July 20, 2020.](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)
- [Grunzweig, J. and Miller-Osborn, J.. (2016, February 4). T9000: Advanced Modular Backdoor Uses Complex Anti-Analysis Techniques. Retrieved April 15, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Counter Threat Unit Research Team. (2017, June 27). BRONZE UNION Cyberespionage Persists Despite Disclosures. Retrieved July 13, 2017.](https://www.secureworks.com/research/bronze-union)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Calvet, J. (2014, November 11). Sednit Espionage Group Attacking Air-Gapped Networks. Retrieved January 4, 2017.](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
- [Reaves, J. and Platt, J. (2020, June). Valak Malware and the Connection to Gozi Loader ConfCrew. Retrieved August 31, 2020.](https://assets.sentinelone.com/labs/sentinel-one-valak-i)
- [Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
- [DomainTools Investigations. (2026, April 6). Handala: MOIS Linked Cyber Influence Ecosystem Threat Intelligence Assessment. Retrieved April 20, 2026.](https://dti.domaintools.com/research/handala-mois-linked-cyber-influence-ecosystem-threat-intelligence-assessment)
- [Wardle, Patrick. (2019, January 15). Middle East Cyber-Espionage analyzing WindShift's implant: OSX.WindTail (part 2). Retrieved October 3, 2019.](https://objective-see.com/blog/blog_0x3D.html)
- [CERT-UA. (2023, February 1). UAC-0114 aka Winter Vivern to target Ukrainian and Polish GOV entities (CERT-UA#5909). Retrieved July 29, 2024.](https://cert.gov.ua/article/3761104)
- [ESET. (2018, November 20). Sednit: What’s going on with Zebrocy?. Retrieved February 12, 2019.](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
- [ESET Research. (2019, May 22). A journey to Zebrocy land. Retrieved June 20, 2019.](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)

---


### 🔗 KRAB Intelligence Correlation
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025 Multi-Industry Hypervisor and Retail Extortion Campaign]] [related_campaign:: [[2025 Multi-Industry Hypervisor and Retail Extortion Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025-2026 SaaS Identity Crisis and Help Desk Exploitation Wave]] [related_campaign:: [[2025-2026 SaaS Identity Crisis and Help Desk Exploitation Wave]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2026 Enterprise LMS and Canvas Data Extortion Campaign]] [related_campaign:: [[2026 Enterprise LMS and Canvas Data Extortion Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2026 Oracle PeopleSoft Mass Data Theft Campaign]] [related_campaign:: [[2026 Oracle PeopleSoft Mass Data Theft Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[Salesforce Massive Corporate Extortion Wave]] [related_campaign:: [[Salesforce Massive Corporate Extortion Wave]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[Zendesk Typosquatting and Phishing Campaign]] [related_campaign:: [[Zendesk Typosquatting and Phishing Campaign]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Scattered Lapsus$ Hunters]] [related_actor:: [[Scattered Lapsus$ Hunters]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[RansomHub]] [related_actor:: [[RansomHub]]]

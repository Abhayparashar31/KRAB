# Masquerading

## Description

Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.

Renaming abusable system utilities to evade security monitoring is also a form of Masquerading . [1]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1030 | Agrius | Agrius used the Plink tool for tunneling and connections to remote machines, renaming it systems.exe in some instances. [2] |
| G1007 | Aoqin Dragon | Aoqin Dragon has used fake icons including antivirus and external drives to disguise malicious payloads. [3] |
| S0622 | AppleSeed | AppleSeed can disguise JavaScript files as PDFs. [4] |
| G0007 | APT28 | APT28 has renamed the WinRAR utility to avoid detection. [5] |
| G0050 | APT32 | APT32 has disguised a Cobalt Strike beacon as a Flash Installer. [6] |
| C0046 | ArcaneDoor | ArcaneDoor involved the use of digital certificates on adversary-controlled network infrastructure that mimicked the formatting used by legitimate Cisco ASA appliances. [7] |
| S1246 | BeaverTail | BeaverTail has masqueraded as MiroTalk installation packages: "MiroTalk.dmg" for macOS and "MiroTalk.msi" for Windows, and has included login GUIs with MiroTalk themes. [8] |
| S0268 | Bisonal | Bisonal dropped a decoy payload with a .jpg extension that contained a malicious Visual Basic script. [9] |
| S0635 | BoomBox | BoomBox has the ability to mask malicious data strings as PDF files. [10] |
| G0060 | BRONZE BUTLER | BRONZE BUTLER has masked executables with document file icons including Word and Adobe PDF. [11] |
| C0015 | C0015 | During C0015 , the threat actors named a binary file compareForfor.jpg to disguise it as a JPG file. [12] |
| C0018 | C0018 | During C0018 , AvosLocker was disguised using the victim company name as the filename. [13] |
| G1052 | Contagious Interview | Contagious Interview has delivered BeaverTail malware masquerading as legitimate software or applications. [14] [15] [16] [17] [8] Contagious Interview has also delivered malicious payloads masquerading as legitimate software drivers. [18] |
| S0497 | Dacls | The Dacls Mach-O binary has been disguised as a .nib file. [19] |
| S1111 | DarkGate | DarkGate can masquerade as pirated media content for initial delivery to victims. [20] |
| S1066 | DarkTortilla | DarkTortilla 's payload has been renamed PowerShellInfo.exe . [21] |
| S0673 | DarkWatchman | DarkWatchman has used an icon mimicking a text file to mask a malicious executable. [22] |
| S9038 | DynoWiper | DynoWiper has been named after well-known files schtask.exe, schtask2.exe, and _update.exe. [23] [24] |
| G1003 | Ember Bear | Ember Bear has renamed the legitimate Sysinternals tool procdump to alternative names such as dump64.exe to evade detection. [25] |
| S0634 | EnvyScout | EnvyScout has used folder icons for malicious files to lure victims into opening them. [10] |
| G1016 | FIN13 | FIN13 has masqueraded staged data by using the Windows certutil utility to generate fake Base64 encoded certificates with the input file. [26] [27] |
| S0696 | Flagpro | Flagpro can download malicious files with a .tmp extension and append them with .exe prior to execution. [28] |
| S0661 | FoggyWeb | FoggyWeb can masquerade the output of C2 commands as a fake, but legitimately formatted WebP file. [29] |
| S9010 | GlassWorm | GlassWorm has masqueraded as legitimate VSCode extensions. [30] [31] GlassWorm has also impersonated Github projects. [30] |
| C0035 | KV Botnet Activity | KV Botnet Activity involves changing process filename to pr_set_mm_exe_file and process name to pr_set_name during later infection stages. [32] |
| G0140 | LazyScripter | LazyScripter has used several different security software icons to disguise executables. [33] |
| G0045 | menuPass | menuPass has used esentutl to change file extensions to their true type that were masquerading as .txt files. [34] |
| S1015 | Milan | Milan has used an executable named companycatalogue to appear benign. [35] |
| S0637 | NativeZone | NativeZone has, upon execution, displayed a message box that appears to be related to a Ukrainian electronic document management system. [36] |
| G0133 | Nomadic Octopus | Nomadic Octopus attempted to make Octopus appear as a Telegram Messenger with a Russian interface. [37] |
| S0368 | NotPetya | NotPetya drops PsExec with the filename dllhost.dat. [38] |
| G0049 | OilRig | OilRig has used .doc file extensions to mask malicious executables. [39] |
| C0016 | Operation Dust Storm | For Operation Dust Storm , the threat actors disguised some executables as JPG files. [40] |
| C0006 | Operation Honeybee | During Operation Honeybee , the threat actors modified the MaoCheng dropper so its icon appeared as a Word document. [41] |
| G0068 | PLATINUM | PLATINUM has renamed rar.exe to avoid detection. [42] |
| S0453 | Pony | Pony has used the Adobe Reader icon for the downloaded file to look more trustworthy. [43] |
| S1046 | PowGoop | PowGoop has disguised a PowerShell script as a .dat file (goopdate.dat). [44] |
| S0565 | Raindrop | Raindrop was built to include a modified version of 7-Zip source code (including associated export names) and Far Manager source code. [45] [46] |
| S0458 | Ramsay | Ramsay has masqueraded as a JPG image file. [47] |
| S0662 | RCSession | RCSession has used a file named English.rtf to appear benign on victim hosts. [48] [49] |
| S1240 | RedLine Stealer | RedLine Stealer malware has masqueraded as legitimate software such as "PDF Converter Software" which has been distributed through poisoned search engine results often resembling legitimate software lures with the combination of typo squatted domains. [50] |
| S0148 | RTM | RTM has been delivered as archived Windows executable files masquerading as PDF documents. [51] |
| S0446 | Ryuk | Ryuk can create .dll files that actually contain a Rich Text File format document. [52] |
| S1018 | Saint Bot | Saint Bot has renamed malicious binaries as wallpaper.mp4 and slideshow.mp4 to avoid detection. [53] [54] |
| C0059 | Salesforce Data Exfiltration | During Salesforce Data Exfiltration , threat actors used voice calls to socially engineer victims into authorizing a modified version of the Salesforce Data Loader app. [55] |
| G0034 | Sandworm Team | Sandworm Team masqueraded malicious installers as Windows update packages to evade defense and entice users to execute binaries. [56] |
| S0615 | SombRAT | SombRAT can use a legitimate process name to hide itself. [57] |
| G1046 | Storm-1811 | Storm-1811 has prompted users to download and execute batch scripts that masquerade as legitimate update files during initial access and social engineering operations. [58] |
| S1183 | StrelaStealer | StrelaStealer PE executable payloads have used uncommon but legitimate extensions such as .com instead of .exe . [59] |
| G0127 | TA551 | TA551 has masked malware DLLs as dat and jpg files. [60] |
| G0139 | TeamTNT | TeamTNT has disguised their scripts with docker-related file names. [61] |
| S0682 | TrailBlazer | TrailBlazer has used filenames that match the name of the compromised system in attempt to avoid detection. [62] |
| S0266 | TrickBot | The TrickBot downloader has used an icon to appear as a Microsoft Word document. [63] |
| S1164 | UPSTYLE | UPSTYLE has masqueraded filenames using examples such as update.py . [64] |
| S0689 | WhisperGate | WhisperGate has been disguised as a JPG extension to avoid detection as a malicious PE file. [65] |
| G0112 | Windshift | Windshift has used icons mimicking MS Office files to mask malicious executables. [66] Windshift has also attempted to hide executables by changing the file extension to ".scr" to mimic Windows screensavers. [67] |
| S0466 | WindTail | WindTail has used icons mimicking MS Office files to mask payloads. [66] |
| G1035 | Winter Vivern | Winter Vivern created specially-crafted documents mimicking legitimate government or similar documents during phishing campaigns. [68] |
| S0658 | XCSSET | XCSSET installs malicious application bundles that mimic native macOS apps, such as Safari, by using the legitimate app’s icon and customizing the Info.plist to match expected metadata. [69] [70] |
| G0128 | ZIRCONIUM | ZIRCONIUM has spoofed legitimate applications in phishing lures and changed file extensions to conceal installation of malware. [71] [72] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1049 | Antivirus/Antimalware | Anti-virus can be used to automatically quarantine suspicious files. |
| M1047 | Audit | Audit user accounts to ensure that each one has a defined purpose. |
| M1040 | Behavior Prevention on Endpoint | Implement security controls on the endpoint, such as a Host Intrusion Prevention System (HIPS), to identify and prevent execution of potentially malicious files (such as those with mismatching file signatures). |
| M1045 | Code Signing | Require signed binaries. |
| M1038 | Execution Prevention | Use tools that restrict program execution via application control by attributes other than file name for common operating system utilities that are needed. |
| M1022 | Restrict File and Directory Permissions | Use file system access controls to protect folders such as C:\Windows\System32. |
| M1018 | User Account Management | Consider defining and enforcing a naming convention for user accounts to more easily spot generic account names that do not fit the typical schema. |
| M1017 | User Training | Train users not to open email attachments or click unknown links (URLs). Such training fosters more secure habits within your organization and will limit many of the risks. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0127 | Behavioral Detection of Masquerading Across Platforms via Metadata and Execution Discrepancy | AN0355 | Adversary renames LOLBINs or deploys binaries with spoofed file names, internal PE metadata, or misleading icons to appear legitimate. File creation is followed by execution or service registration inconsistent with known usage. |
| AN0356 | Adversary drops renamed binaries in uncommon directories (e.g., /tmp, /dev/shm) or uses special characters in names (e.g., trailing space, Unicode RLO). Execution or cronjob registration follows shortly after file drop. |  |  |
| AN0357 | Adversary creates disguised launch daemons or apps with misleading names and bundle metadata (e.g., Info.plist values inconsistent with binary path or icon). Launch is correlated with user logon or persistence setup. |  |  |
| AN0358 | Adversary uses renamed container images, injects files into containers with misleading names or metadata (e.g., renamed system binaries), and executes them during startup or scheduled jobs. |  |  |
| AN0359 | Adversary places scripts or binaries with misleading names in /etc/rc.local.d or /var/spool/cron, or registers services with legitimate-sounding names not present in default ESXi builds. |  |  |

---

## References

- [LOLBAS. (n.d.). Living Off The Land Binaries and Scripts (and also Libraries). Retrieved February 10, 2020.](https://lolbas-project.github.io/)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [Chen, Joey. (2022, June 9). Aoqin Dragon | Newly-Discovered Chinese-linked APT Has Been Quietly Spying On Organizations For 10 Years. Retrieved July 14, 2022.](https://www.sentinelone.com/labs/aoqin-dragon-newly-discovered-chinese-linked-apt-has-been-quietly-spying-on-organizations-for-10-years/)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [NSA, CISA, FBI, NCSC. (2021, July). Russian GRU Conducting Global Brute Force Campaign to Compromise Enterprise and Cloud Environments. Retrieved July 26, 2021.](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Cisco Talos. (2024, April 24). ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices. Retrieved January 6, 2025.](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
- [Unit42. (2024, October 9). Contagious Interview: DPRK Threat Actors Lure Tech Industry Job Seekers to Install New Variants of BeaverTail and InvisibleFerret Malware. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/north-korean-threat-actors-lure-tech-job-seekers-as-fake-recruiters/)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [MSTIC. (2021, May 28). Breaking down NOBELIUM’s latest early-stage toolset. Retrieved August 4, 2021.](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Venere, G. Neal, C. (2022, June 21). Avos ransomware group expands with new attack arsenal. Retrieved January 11, 2023.](https://blog.talosintelligence.com/avoslocker-new-arsenal/)
- [eSentire Threat Response Unit (TRU). (2024, November 14). Bored BeaverTail & InvisibleFerret Yacht Club – A Lazarus Lure Pt.2. Retrieved October 17, 2025.](https://www.esentire.com/blog/bored-beavertail-invisibleferret-yacht-club-a-lazarus-lure-pt-2)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Seongsu Park. (2024, November 4). From Pyongyang to Your Payroll: The Rise of North Korean Remote Workers in the West. Retrieved October 17, 2025.](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Amaury G., Coline Chavane, Felix Aimé and Sekoia TDR. (2025, March 31). From Contagious to ClickFake Interview: Lazarus leveraging the ClickFix tactic. Retrieved April 1, 2025.](https://blog.sekoia.io/clickfake-interview-campaign-by-lazarus/)
- [Stokes, P. (2020, July 27). Four Distinct Families of Lazarus Malware Target Apple’s macOS Platform. Retrieved August 7, 2020.](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [ESET. (2026, January 30). DynoWiper update: Technical analysis and attribution. Retrieved April 22, 2026.](https://www.welivesecurity.com/en/eset-research/dynowiper-update-technical-analysis-attribution/)
- [Microsoft Threat Intelligence. (2023, June 14). Cadet Blizzard emerges as a novel and distinct Russian threat actor. Retrieved July 10, 2023.](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [Sygnia Incident Response Team. (2022, January 5). TG2003: ELEPHANT BEETLE UNCOVERING AN ORGANIZED FINANCIAL-THEFT OPERATION. Retrieved February 9, 2023.](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [Ramin Nafisi. (2021, September 27). FoggyWeb: Targeted NOBELIUM malware leads to persistent backdoor. Retrieved October 4, 2021.](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
- [Ilyas Makari. (2025, October 31). The Return of the Invisible Threat: Hidden PUA Unicode Hits GitHub repositorties. Retrieved April 10, 2026.](https://www.aikido.dev/blog/the-return-of-the-invisible-threat-hidden-pua-unicode-hits-github-repositorties)
- [Lotan Sery. (2025, December 10). GlassWorm Goes Native: Same Infrastructure, Hardened Delivery. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)
- [Black Lotus Labs. (2023, December 13). Routers Roasting On An Open Firewall: The KV-Botnet Investigation. Retrieved June 10, 2024.](https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/)
- [Jazi, H. (2021, February). LazyScripter: From Empire to double RAT. Retrieved November 17, 2024.](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
- [Matsuda, A., Muhammad I. (2018, September 13). APT10 Targeting Japanese Corporations Using Updated TTPs. Retrieved September 17, 2018.](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
- [ClearSky Cyber Security . (2021, August). New Iranian Espionage Campaign By “Siamesekitten” - Lyceum. Retrieved June 6, 2022.](https://www.clearskysec.com/siamesekitten/)
- [Guerrero-Saade, J. (2021, June 1). NobleBaron | New Poisoned Installers Could Be Used In Supply Chain Attacks. Retrieved August 4, 2021.](https://labs.sentinelone.com/noblebaron-new-poisoned-installers-could-be-used-in-supply-chain-attacks/)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 15). Octopus-infested seas of Central Asia. Retrieved November 14, 2018.](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
- [Chiu, A. (2016, June 27). New Ransomware Variant "Nyetya" Compromises Systems Worldwide. Retrieved March 26, 2019.](https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Sherstobitoff, R. (2018, March 02). McAfee Uncovers Operation Honeybee, a Malicious Document Campaign Targeting Humanitarian Aid Groups. Retrieved May 16, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-uncovers-operation-honeybee-malicious-document-campaign-targeting-humanitarian-aid-groups/)
- [Carr, N.. (2018, October 25). Nick Carr Status Update. Retrieved September 12, 2024.](https://x.com/ItsReallyNick/status/1055321868641689600)
- [hasherezade. (2016, April 11). No money, but Pony! From a mail to a trojan horse. Retrieved May 21, 2020.](https://blog.malwarebytes.com/threat-analysis/2015/11/no-money-but-pony-from-a-mail-to-a-trojan-horse/)
- [FBI, CISA, CNMF, NCSC-UK. (2022, February 24). Iranian Government-Sponsored Actors Conduct Cyber Operations Against Global Government and Commercial Networks. Retrieved September 27, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
- [Symantec Threat Hunter Team. (2021, January 18). Raindrop: New Malware Discovered in SolarWinds Investigation. Retrieved January 19, 2021.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/solarwinds-raindrop-malware)
- [MSTIC, CDOC, 365 Defender Research Team. (2021, January 20). Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop . Retrieved January 22, 2021.](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Counter Threat Unit Research Team. (2019, December 29). BRONZE PRESIDENT Targets NGOs. Retrieved April 13, 2021.](https://www.secureworks.com/research/bronze-president-targets-ngos)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [George Glass. (2024, August 14). REDLINESTEALER Malware Driving the Initial Access Broker Market. Retrieved September 17, 2025.](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
- [Duncan, B., Harbison, M. (2019, January 23). Russian Language Malspam Pushing Redaman Banking Malware. Retrieved June 16, 2020.](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
- [ANSSI. (2021, February 25). RYUK RANSOMWARE. Retrieved March 29, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2021-CTI-006.pdf)
- [Hasherezade. (2021, April 6). A deep dive into Saint Bot, a new downloader. Retrieved June 9, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Google Threat Intelligence Group. (2025, June 4). The Cost of a Call: From Voice Phishing to Data Extortion. Retrieved October 22, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion)
- [Billy Leonard. (2023, April 19). Ukraine remains Russia’s biggest cyber focus in 2023. Retrieved March 1, 2024.](https://blog.google/threat-analysis-group/ukraine-remains-russias-biggest-cyber-focus-in-2023/)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [Tyler McGraw, Thomas Elkins, and Evan McCann. (2024, May 10). Ongoing Social Engineering Campaign Linked to Black Basta Ransomware Operators. Retrieved January 31, 2025.](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)
- [Golo Mühr, Joe Fasulo & Charlotte Hammond, IBM X-Force. (2024, November 12). Strela Stealer: Today’s invoice is tomorrow’s phish. Retrieved December 31, 2024.](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
- [Duncan, B. (2021, January 7). TA551: Email Attack Campaign Switches from Valak to IcedID. Retrieved March 17, 2021.](https://unit42.paloaltonetworks.com/ta551-shathak-icedid/)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [CrowdStrike. (2022, January 27). Early Bird Catches the Wormhole: Observations from the StellarParticle Campaign. Retrieved February 7, 2022.](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)
- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [Volexity Threat Research. (2024, April 12). Zero-Day Exploitation of Unauthenticated Remote Code Execution Vulnerability in GlobalProtect (CVE-2024-3400). Retrieved November 20, 2024.](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)
- [S2W. (2022, January 18). Analysis of Destructive Malware (WhisperGate) targeting Ukraine. Retrieved March 14, 2022.](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)
- [Wardle, Patrick. (2018, December 20). Middle East Cyber-Espionage analyzing WindShift's implant: OSX.WindTail (part 1). Retrieved October 3, 2019.](https://objective-see.com/blog/blog_0x3B.html)
- [The BlackBerry Research & Intelligence Team. (2020, October). BAHAMUT: Hack-for-Hire Masters of Phishing, Fake News, and Fake Apps. Retrieved February 8, 2021.](https://www.blackberry.com/us/en/pdfviewer?file=/content/dam/blackberry-com/asset/enterprise/pdf/direct/report-spark-bahamut.pdf)
- [Tom Hegel. (2023, March 16). Winter Vivern | Uncovering a Wave of Global Espionage. Retrieved July 29, 2024.](https://www.sentinelone.com/labs/winter-vivern-uncovering-a-wave-of-global-espionage/)
- [Mac Threat Response, Mobile Research Team. (2020, August 13). The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSS Backdoor Planting in Safari, and Leverages Two Zero-day Exploits. Retrieved October 5, 2021.](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
- [Microsoft Threat Intelligence. (2025, March 11). New XCSSET malware adds new obfuscation, persistence techniques to infect Xcode projects. Retrieved April 2, 2025.](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)
- [Huntley, S. (2020, October 16). How We're Tackling Evolving Online Threats. Retrieved March 24, 2021.](https://blog.google/threat-analysis-group/how-were-tackling-evolving-online-threats/)
- [Singh, S. and Antil, S. (2020, October 27). APT-31 Leverages COVID-19 Vaccine Theme and Abuses Legitimate Online Services. Retrieved March 24, 2021.](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)

---

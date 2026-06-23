# Archive Collected Data

## Description

An adversary may compress and/or encrypt data that is collected prior to exfiltration. Compressing the data can help to obfuscate the collected data and minimize the amount of data sent over the network. [1] Encryption can be used to hide information that is being exfiltrated from detection or make exfiltration less conspicuous upon inspection by a defender.

Both compression and encryption are done prior to exfiltration, and can be performed using a utility, 3rd party library, or custom method.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0045 | ADVSTORESHELL | ADVSTORESHELL encrypts with the 3DES algorithm and a hardcoded key prior to exfiltration. [2] |
| S0331 | Agent Tesla | Agent Tesla can encrypt data with 3DES before sending it over to a C2 server. [3] |
| S0622 | AppleSeed | AppleSeed has compressed collected data before exfiltration. [4] |
| G0007 | APT28 | APT28 used a publicly available tool to gather and compress multiple documents on the DCCC and DNC networks. [1] |
| G0050 | APT32 | APT32 's backdoor has used LZMA compression and RC4 encryption before exfiltration. [5] |
| S0456 | Aria-body | Aria-body has used ZIP to compress data gathered on a compromised host. [6] |
| G0001 | Axiom | Axiom has compressed and encrypted data prior to exfiltration. [7] |
| S0093 | Backdoor.Oldrea | Backdoor.Oldrea writes collected data to a temporary file in an encrypted form before exfiltration to a C2 server. [8] |
| G1043 | BlackByte | BlackByte compressed data collected from victim environments prior to exfiltration. [9] |
| S0521 | BloodHound | BloodHound can compress data collected by its SharpHound ingestor into a ZIP file to be written to disk. [10] [11] |
| S0657 | BLUELIGHT | BLUELIGHT can zip files before exfiltration. [12] |
| S1039 | Bumblebee | Bumblebee can compress data stolen from the Registry and volume shadow copies prior to exfiltration. [13] |
| S0454 | Cadelspy | Cadelspy has the ability to compress stolen data into a .cab file. [14] |
| S0667 | Chrommme | Chrommme can encrypt and store on disk collected data before exfiltration. [15] |
| S0187 | Daserf | Daserf hides collected data in password-protected .rar archives. [16] |
| G0035 | Dragonfly | Dragonfly has compressed data into .zip files prior to exfiltration. [17] |
| S0567 | Dtrack | Dtrack packs collected data into a password protected archive. [18] |
| G1003 | Ember Bear | Ember Bear has compressed collected data prior to exfiltration. [19] |
| S0363 | Empire | Empire can ZIP directories on the target system. [20] |
| S0091 | Epic | Epic encrypts collected data using a public key framework before sending it over the C2 channel. [21] Some variants encrypt the collected data with AES and encode it with base64 before transmitting it to the C2 server. [22] |
| S0343 | Exaramel for Windows | Exaramel for Windows automatically encrypts files before sending them to the C2 server. [23] |
| S0267 | FELIXROOT | FELIXROOT encrypts collected data with AES and Base64 and then sends it to the C2 server. [24] |
| G0037 | FIN6 | Following data collection, FIN6 has compressed log files into a ZIP archive prior to staging and exfiltration. [25] |
| S0249 | Gold Dragon | Gold Dragon encrypts data using Base64 before being sent to the command and control server. [26] |
| S1206 | JumbledPath | JumbledPath can compress and encrypt exfiltrated packet captures from targeted devices. [27] |
| G0004 | Ke3chang | The Ke3chang group has been known to compress data before exfiltration. [28] |
| S0487 | Kessel | Kessel can RC4-encrypt credentials before sending to the C2. [29] |
| S0356 | KONNI | KONNI has encrypted data and files prior to exfiltration. [30] |
| G0032 | Lazarus Group | Lazarus Group has compressed exfiltrated data with RAR and used RomeoDelta malware to archive specified directories in .zip format, encrypt the .zip file, and upload it to C2. [31] [32] [33] |
| G0065 | Leviathan | Leviathan has archived victim's data prior to exfiltration. [34] |
| S0395 | LightNeuron | LightNeuron contains a function to encrypt and store emails that it collects. [35] |
| S0681 | Lizar | Lizar has encrypted data before sending it to the server. [36] |
| S1101 | LoFiSe | LoFiSe can collect files into password-protected ZIP-archives for exfiltration. [37] |
| S9036 | LP-Notes | LP-Notes has encrypted collected credentials using AES-CBC from the CNG API and the key ED15C8344B45DAED1E0578F8BC1A32411812C61F4CB45D89B107287DE0E09FFC and the initialization vector 91A4E6F6D51DAEE773A8F00279792578. [38] |
| G1014 | LuminousMoth | LuminousMoth has manually archived stolen files from victim machines before exfiltration. [39] |
| S0010 | Lurid | Lurid can compress data before sending it. [40] |
| S0409 | Machete | Machete stores zipped files with profile data from installed web browsers. [41] |
| G0045 | menuPass | menuPass has encrypted files and information before exfiltration. [42] [43] |
| S9032 | MuddyViper | MuddyViper has archived collected web browser data into a file named CacheDump.zip. [38] |
| S0198 | NETWIRE | NETWIRE has the ability to compress archived screenshots. [44] |
| G0040 | Patchwork | Patchwork encrypted the collected files' path with AES and then encoded them with base64. [45] |
| S0517 | Pillowmint | Pillowmint has encrypted stolen credit card information with AES and further encoded it with Base64. [46] |
| S1012 | PowerLess | PowerLess can encrypt browser database files prior to exfiltration. [47] |
| S0113 | Prikormka | After collecting documents from removable media, Prikormka compresses the collected files, and encrypts it with Blowfish. [48] |
| S0279 | Proton | Proton zips up files before exfiltrating them. [49] |
| S1148 | Raccoon Stealer | Raccoon Stealer archives collected system information in a text f ile, System info.txt , prior to exfiltration. [50] |
| S0375 | Remexi | Remexi encrypts and adds all gathered browser data into files for upload to C2. [51] |
| S0253 | RunningRAT | RunningRAT contains code to compress files. [26] |
| S0445 | ShimRatReporter | ShimRatReporter used LZ compression to compress initial reconnaissance reports before sending to the C2. [52] |
| S1140 | Spica | Spica can archive collected documents for exfiltration. [53] |
| S0586 | TAINTEDSCRIBE | TAINTEDSCRIBE has used FileReadZipSend to compress a file and send to C2. [54] |
| S1196 | Troll Stealer | Troll Stealer compresses stolen data prior to exfiltration. [55] |
| S0257 | VERMIN | VERMIN encrypts the collected files using 3-DES. [56] |
| S0515 | WellMail | WellMail can archive files on the compromised host. [57] |
| S0658 | XCSSET | XCSSET will compress entire ~/Desktop folders excluding all .git folders, but only if the total data size is under 200MB. [58] |
| S0251 | Zebrocy | Zebrocy has used a method similar to RC4 as well as AES for encryption and hexadecimal for encoding data before exfiltration. [59] [60] [61] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | System scans can be performed to identify unauthorized archival utilities. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0526 | Detect Archiving and Encryption of Collected Data (T1560) | AN1458 | Detects adversarial archiving of files prior to exfiltration by correlating execution of compression/encryption utilities (e.g., makecab.exe, rar.exe, 7z.exe, powershell Compress-Archive) with subsequent creation of large compressed or encrypted files. Identifies abnormal process lineage involving crypt32.dll usage, command-line arguments invoking compression switches, and file write operations to temporary or staging directories. |
| AN1459 | Detects adversarial archiving activity through invocation of utilities like tar, gzip, bzip2, or openssl used in non-administrative or unusual contexts. Correlates command execution patterns with file creation of compressed/encrypted outputs in staging directories (e.g., /tmp, /var/tmp). |  |  |
| AN1460 | Detects use of macOS-native archiving or encryption tools (zip, ditto, hdiutil) for staging collected data. Identifies unexpected invocation of archive utilities by Office apps, browsers, or background daemons. Correlates file creation of .zip/.dmg containers with process lineage anomalies. |  |  |

---

## References

- [Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved November 17, 2024.](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)
- [ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
- [Brumaghin, E., et al. (2018, October 15). Old dog, new tricks - Analysing new RTF-based campaign distributing Agent Tesla, Loki with PyREbox. Retrieved November 5, 2018.](https://blog.talosintelligence.com/2018/10/old-dog-new-tricks-analysing-new-rtf_15.html)
- [KISA. (2021). Phishing Target Reconnaissance and Attack Resource Analysis Operation Muzabi. Retrieved March 8, 2024.](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
- [Dumont, R. (2019, March 20). Fake or Fake: Keeping up with OceanLotus decoys. Retrieved April 1, 2019.](https://www.welivesecurity.com/2019/03/20/fake-or-fake-keeping-up-with-oceanlotus-decoys/)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
- [Symantec Security Response. (2014, June 30). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
- [Huseyin Can Yuceel. (2022, February 21). TTPs used by BlackByte Ransomware Targeting Critical Infrastructure. Retrieved December 16, 2024.](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)
- [Robbins, A., Vazarkar, R., and Schroeder, W. (2016, April 17). Bloodhound: Six Degrees of Domain Admin. Retrieved March 5, 2019.](https://github.com/BloodHoundAD/BloodHound)
- [Kenefick, I. et al. (2022, October 12). Black Basta Ransomware Gang Infiltrates Networks via QAKBOT, Brute Ratel, and Cobalt Strike. Retrieved February 6, 2023.](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
- [Cash, D., Grunzweig, J., Meltzer, M., Adair, S., Lancaster, T. (2021, August 17). North Korean APT InkySquid Infects Victims Using Browser Exploits. Retrieved September 30, 2021.](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
- [Cybereason. (2022, August 17). Bumblebee Loader – The High Road to Enterprise Domain Control. Retrieved August 29, 2022.](https://www.cybereason.com/blog/threat-analysis-report-bumblebee-loader-the-high-road-to-enterprise-domain-control)
- [Symantec Security Response. (2015, December 7). Iran-based attackers use back door threats to spy on Middle Eastern targets. Retrieved April 17, 2019.](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [DiMaggio, J. (2016, April 28). Tick cyberespionage group zeros in on Japan. Retrieved July 16, 2018.](https://www.symantec.com/connect/blogs/tick-cyberespionage-group-zeros-japan)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [Konstantin Zykov. (2019, September 23). Hello! My name is Dtrack. Retrieved January 20, 2021.](https://securelist.com/my-name-is-dtrack/93338/)
- [US Cybersecurity & Infrastructure Security Agency et al. (2024, September 5). Russian Military Cyber Actors Target U.S. and Global Critical Infrastructure. Retrieved September 6, 2024.](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [Kaspersky Lab's Global Research & Analysis Team. (2014, August 06). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroboros. Retrieved November 7, 2018.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08080105/KL_Epic_Turla_Technical_Appendix_20140806.pdf)
- [Cherepanov, A., Lipovsky, R. (2018, October 11). New TeleBots backdoor: First evidence linking Industroyer to NotPetya. Retrieved November 27, 2018.](https://www.welivesecurity.com/2018/10/11/new-telebots-backdoor-linking-industroyer-notpetya/)
- [Patil, S. (2018, June 26). Microsoft Office Vulnerabilities Used to Distribute FELIXROOT Backdoor in Recent Campaign. Retrieved November 17, 2024.](https://web.archive.org/web/20200607025424/https://www.fireeye.com/blog/threat-research/2018/07/microsoft-office-vulnerabilities-used-to-distribute-felixroot-backdoor.html)
- [FireEye Threat Intelligence. (2016, April). Follow the Money: Dissecting the Operations of the Cyber Crime Group FIN6. Retrieved November 17, 2024.](https://web.archive.org/web/20190807112824/https://www2.fireeye.com/rs/848-DID-242/images/rpt-fin6.pdf)
- [Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
- [Cisco Talos. (2025, February 20). Weathering the storm: In the midst of a Typhoon. Retrieved February 24, 2025.](https://blog.talosintelligence.com/salt-typhoon-analysis/)
- [Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [Threat Intelligence Team. (2021, August 23). New variant of Konni malware used in campaign targetting Russia. Retrieved January 5, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Remote Administration Tools & Content Staging Malware Report. Retrieved March 16, 2016.](https://web.archive.org/web/20220608001455/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-RAT-and-Staging-Report.pdf)
- [Sherstobitoff, R. (2018, February 12). Lazarus Resurfaces, Targets Global Banks and Bitcoin Users. Retrieved February 19, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/lazarus-resurfaces-targets-global-banks-bitcoin-users/)
- [CISA. (2021, July 19). (AA21-200A) Joint Cybersecurity Advisory – Tactics, Techniques, and Procedures of Indicted APT40 Actors Associated with China’s MSS Hainan State Security Department. Retrieved August 12, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)
- [Faou, M. (2019, May). Turla LightNeuron: One email away from remote code execution. Retrieved June 24, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [Dedola, G. et al. (2023, October 12). ToddyCat: Keep calm and check logs. Retrieved January 3, 2024.](https://securelist.com/toddycat-keep-calm-and-check-logs/110696/)
- [ESET Research. (2025, December 2). MuddyWater: Snakes by the riverbank. Retrieved February 17, 2026.](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
- [Botezatu, B and etl. (2021, July 21). LuminousMoth - PlugX, File Exfiltration and Persistence Revisited. Retrieved October 20, 2022.](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)
- [Villeneuve, N., Sancho, D. (2011). THE “LURID” DOWNLOADER. Retrieved November 12, 2014.](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_dissecting-lurid-apt.pdf)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [United States District Court Southern District of New York (USDC SDNY) . (2018, December 17). United States of America v. Zhu Hua and Zhang Shilong. Retrieved April 17, 2019.](https://www.justice.gov/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion)
- [US District Court Southern District of New York. (2018, December 17). United States v. Zhu Hua Indictment. Retrieved December 17, 2020.](https://www.justice.gov/opa/page/file/1122671/download)
- [Lambert, T. (2020, January 29). Intro to Netwire. Retrieved January 7, 2021.](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
- [Lunghi, D., et al. (2017, December). Untangling the Patchwork Cyberespionage Group. Retrieved July 10, 2018.](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
- [Trustwave SpiderLabs. (2020, June 22). Pillowmint: FIN7’s Monkey Thief . Retrieved July 27, 2020.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/pillowmint-fin7s-monkey-thief/)
- [Cybereason Nocturnus. (2022, February 1). PowerLess Trojan: Iranian APT Phosphorus Adds New PowerShell Backdoor for Espionage. Retrieved June 1, 2022.](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)
- [Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
- [Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.](https://objective-see.com/blog/blog_0x25.html)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Legezo, D. (2019, January 30). Chafer used Remexi malware to spy on Iran-based foreign diplomatic entities. Retrieved April 17, 2019.](https://securelist.com/chafer-used-remexi-malware/89538/)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Shields, W. (2024, January 18). Russian threat group COLDRIVER expands its targeting of Western officials to include the use of malware. Retrieved June 13, 2024.](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)
- [USG. (2020, May 12). MAR-10288834-2.v1 – North Korean Trojan: TAINTEDSCRIBE. Retrieved March 5, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-133b)
- [Jiho Kim & Sebin Lee, S2W. (2024, February 7). Kimsuky disguised as a Korean company signed with a valid certificate to distribute Troll Stealer (English ver.). Retrieved January 17, 2025.](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
- [Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
- [CISA. (2020, July 16). MAR-10296782-3.v1 – WELLMAIL. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
- [Mac Threat Response, Mobile Research Team. (2020, August 13). The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSS Backdoor Planting in Safari, and Leverages Two Zero-day Exploits. Retrieved October 5, 2021.](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, February 20). A Slice of 2017 Sofacy Activity. Retrieved November 27, 2018.](https://securelist.com/a-slice-of-2017-sofacy-activity/83930/)
- [ESET. (2018, November 20). Sednit: What’s going on with Zebrocy?. Retrieved February 12, 2019.](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
- [CISA. (2020, October 29). Malware Analysis Report (AR20-303B). Retrieved December 9, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)

---

# Web Service

## Description

Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compromised system. Popular websites, cloud services, and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google, Microsoft, or Twitter, makes it easier for adversaries to hide in expected noise. [1] Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

Use of Web services may also protect back-end C2 infrastructure from discovery through malware binary analysis while also enabling operational resiliency (since this infrastructure may be dynamically changed).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0050 | APT32 | APT32 has used Dropbox, Amazon S3, and Google Drive to host malicious downloads. [2] |
| C0040 | APT41 DUST | APT41 DUST used compromised Google Workspace accounts for command and control. [3] |
| G1044 | APT42 | APT42 has used various links, such as links with typo-squatted domains, links to Dropbox files and links to fake Google sites, in spearphishing operations. [4] [5] [6] |
| S9031 | AshTag | AshTag can download malicious payloads from file sharing services. [7] |
| S1081 | BADHATCH | BADHATCH can be utilized to abuse sslip.io , a free IP to domain mapping service, as part of actor-controlled C2 channels. [8] |
| S0534 | Bazar | Bazar downloads have been hosted on Google Docs. [9] [10] |
| S0635 | BoomBox | BoomBox can download files from Dropbox using a hardcoded access token. [11] |
| S9015 | BRICKSTORM | BRICKSTORM has leveraged DNS web services to resolve C2 IP addresses including sslip.io and nip.io. [12] BRICKSTORM has also utilized Cloudflare Workers for C2 communications. [12] |
| S1063 | Brute Ratel C4 | Brute Ratel C4 can use legitimate websites for external C2 channels including Slack, Discord, and MS Teams. [13] |
| S1039 | Bumblebee | Bumblebee has been downloaded to victim's machines from OneDrive. [14] |
| C0017 | C0017 | During C0017 , APT41 used the Cloudflare services for C2 communications. [15] |
| C0027 | C0027 | During C0027 , Scattered Spider downloaded tools from sites including file.io, GitHub, and paste.ee. [16] |
| S0335 | Carbon | Carbon can use Pastebin to receive C2 commands. [17] |
| S0674 | CharmPower | CharmPower can download additional modules from actor-controlled Amazon S3 buckets. [18] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP has the ability to use use Telegram channels to return a list of commands to be executed, to download additional payloads, or to create a reverse shell. [19] |
| S1066 | DarkTortilla | DarkTortilla can retrieve its primary payload from public sites such as Pastebin and Textbin. [20] |
| S0600 | Doki | Doki has used the dogechain.info API to generate a C2 address. [21] |
| S0547 | DropBook | DropBook can communicate with its operators by exploiting the Simplenote, DropBox, and the social media platform, Facebook, where it can create fake accounts to control the backdoor and receive instructions. [22] [23] |
| G1011 | EXOTIC LILY | EXOTIC LILY has used file-sharing services including WeTransfer, TransferNow, and OneDrive to deliver payloads. [24] |
| G0037 | FIN6 | FIN6 has used Pastebin and Google Storage to host content for their operations. [25] |
| G0061 | FIN8 | FIN8 has used sslip.io , a free IP to domain mapping service that also makes SSL certificate generation easier for traffic encryption, as part of their command and control. [26] |
| G0117 | Fox Kitten | Fox Kitten has used Amazon Web Services to host C2. [27] |
| G0047 | Gamaredon Group | Gamaredon Group has used GitHub repositories for downloaders which will be obtained by the group's .NET executable on the compromised system. [28] |
| S0561 | GuLoader | GuLoader has the ability to download malware from Google Drive. [29] |
| S0601 | Hildegard | Hildegard has downloaded scripts from GitHub. [30] |
| G0100 | Inception | Inception has incorporated at least five different cloud service providers into their C2 infrastructure including CloudMe. [31] [32] |
| S1160 | Latrodectus | Latrodectus has used Google Firebase to download malicious installation scripts. [33] |
| G0140 | LazyScripter | LazyScripter has used GitHub to host its payloads to operate spam campaigns. [34] |
| S1221 | MOPSLED | MOPSLED can use third-party web services such as GitHub and Google Drive for C2. [35] |
| G0129 | Mustang Panda | Mustang Panda has used DropBox URLs to deliver variants of PlugX . [36] Mustang Panda has also used Google Drive to host malicious downloads. [37] |
| S0198 | NETWIRE | NETWIRE has used web services including Paste.ee to host payloads. [38] |
| S0508 | ngrok | ngrok has been used by threat actors to proxy C2 connections to ngrok service subdomains. [39] |
| S1147 | Nightdoor | Nightdoor can utilize Microsoft OneDrive or Google Drive for command and control purposes. [40] [41] |
| C0005 | Operation Spalax | During Operation Spalax , the threat actors used OneDrive and MediaFire to host payloads. [42] |
| S9019 | PureCrypter | PureCrypter can use Telegram or Discord to send infection status messages. [43] |
| S1130 | Raspberry Robin | Raspberry Robin second stage payloads can be hosted as RAR files, containing a malicious EXE and DLL, on Discord servers. [44] |
| G1039 | RedCurl | RedCurl has used web services to download malicious files. [45] [46] |
| S1240 | RedLine Stealer | RedLine Stealer has leveraged legitimate file sharing web services to host malicious payloads. [47] [48] |
| G0106 | Rocke | Rocke has used Pastebin, Gitee, and GitLab for Command and Control. [49] [50] |
| S0546 | SharpStage | SharpStage has used a legitimate web service for evading detection. [22] |
| S1178 | ShrinkLocker | ShrinkLocker uses a subdomain on the legitimate Cloudflare resource "trycloudflare[.]com" to obfuscate the threat actor's actual address and to tunnel information sent from victim systems. [51] |
| S0589 | Sibot | Sibot has used a legitimate compromised website to download DLLs to the victim's machine. [52] |
| S0649 | SMOKEDHAM | SMOKEDHAM has used Google Drive and Dropbox to host files downloaded by victims via malicious links. [53] |
| S1086 | Snip3 | Snip3 can download additional payloads from web services including Pastebin and top4top. [54] |
| S1124 | SocGholish | SocGholish has used Amazon Web Services to host second-stage servers. [55] |
| G0139 | TeamTNT | TeamTNT has leveraged iplogger.org to send collected data back to C2. [56] [57] |
| G0010 | Turla | Turla has used legitimate web services including Pastebin, Dropbox, and GitHub for C2 communications. [17] [58] |
| G1055 | VOID MANTICORE | VOID MANTICORE has utilized Telegram API for C2. [59] [60] |
| S0689 | WhisperGate | WhisperGate can download additional payloads hosted on a Discord channel. [61] [62] [63] [64] [65] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |
| M1021 | Restrict Web-Based Content | Web proxies can be used to enforce external network communication policy that prevents use of unauthorized external services. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0425 | Suspicious Use of Web Services for C2 | AN1189 | Detects unusual outbound connections to web services from uncommon processes using SSL/TLS, particularly those exhibiting high outbound data volume or persistence. |
| AN1190 | Detects command-line tools, agents, or scripts making outbound HTTPS connections to popular web services like Discord, Slack, Dropbox, or Graph API in an unusual context. |  |  |
| AN1191 | Detects user agents or background services making unauthorized or unscheduled web API calls to cloud/web services over HTTPS. |  |  |
| AN1192 | Detects guest VMs or management agents issuing HTTP(S) traffic to external services without a valid patch management or backup justification. |  |  |

---

## References

- [Broadcom. (2024, May 2). BirdyClient malware leverages Microsoft Graph API for C&C communication. Retrieved July 1, 2024.](https://www.broadcom.com/support/security-center/protection-bulletin/birdyclient-malware-leverages-microsoft-graph-api-for-c-c-communication)
- [Adair, S. and Lancaster, T. (2020, November 6). OceanLotus: Extending Cyber Espionage Operations Through Fake Websites. Retrieved November 20, 2020.](https://www.volexity.com/blog/2020/11/06/oceanlotus-extending-cyber-espionage-operations-through-fake-websites/)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Rozmann, O., et al. (2024, May 1). Uncharmed: Untangling Iran's APT42 Operations. Retrieved October 9, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)
- [Mandiant. (n.d.). APT42: Crooked Charms, Cons and Compromises. Retrieved October 9, 2024.](https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf)
- [Google Threat Analysis Group. (2024, August 14). Iranian backed group steps up phishing campaigns against Israel, U.S.. Retrieved October 9, 2024.](https://blog.google/threat-analysis-group/iranian-backed-group-steps-up-phishing-campaigns-against-israel-us/)
- [Unit 42. (2025, December 11). Hamas-Affiliated Ashen Lepus Targets Middle Eastern Diplomatic Entities With New AshTag Malware Suite. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Sadique, M. and Singh, A. (2020, September 29). Spear Phishing Campaign Delivers Buer and Bazar Malware. Retrieved November 19, 2020.](https://www.zscaler.com/blogs/research/spear-phishing-campaign-delivers-buer-and-bazar-malware)
- [MSTIC. (2021, May 28). Breaking down NOBELIUM’s latest early-stage toolset. Retrieved August 4, 2021.](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
- [Sarah Yoder, John Wolfram, Ashley Pearson, Doug Bienstock, Josh Madeley, Josh Murchie, Brad Slaybaugh, Matt Lin, Geoff Carstairs, Austin Larsen. (2025, September 24). Another BRICKSTORM: Stealthy Backdoor Enabling Espionage into Tech and Legal Sectors. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
- [Harbison, M. and Renals, P. (2022, July 5). When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors. Retrieved February 1, 2023.](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
- [Merriman, K. and Trouerbach, P. (2022, April 28). This isn't Optimus Prime's Bumblebee but it's Still Transforming. Retrieved August 22, 2022.](https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Parisi, T. (2022, December 2). Not a SIMulation: CrowdStrike Investigations Reveal Intrusion Campaign Targeting Telco and BPO Companies. Retrieved June 30, 2023.](https://www.crowdstrike.com/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/)
- [Accenture. (2020, October). Turla uses HyperStack, Carbon, and Kazuar to compromise government entity. Retrieved December 2, 2020.](https://web.archive.org/web/20201101015247/https://www.accenture.com/us-en/blogs/cyber-defense/turla-belugasturgeon-compromises-government-entity)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [Secureworks Counter Threat Unit Research Team. (2022, August 17). DarkTortilla Malware Analysis. Retrieved November 3, 2022.](https://www.secureworks.com/research/darktortilla-malware-analysis)
- [Fishbein, N., Kajiloti, M.. (2020, July 28). Watch Your Containers: Doki Infecting Docker Servers in the Cloud. Retrieved March 30, 2021.](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
- [Cybereason Nocturnus Team. (2020, December 9). MOLERATS IN THE CLOUD: New Malware Arsenal Abuses Cloud Platforms in Middle East Espionage Campaign. Retrieved December 22, 2020.](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
- [Ilascu, I. (2020, December 14). Hacking group’s new malware abuses Google and Facebook services. Retrieved December 28, 2020.](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
- [Stolyarov, V. (2022, March 17). Exposing initial access broker with ties to Conti. Retrieved August 18, 2022.](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)
- [McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)
- [Martin Zugec. (2021, July 27). Deep Dive Into a FIN8 Attack - A Forensic Investigation. Retrieved September 1, 2021.](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation)
- [ClearSky. (2020, December 17). Pay2Key Ransomware – A New Campaign by Fox Kitten. Retrieved December 21, 2020.](https://www.clearskysec.com/wp-content/uploads/2020/12/Pay2Kitten.pdf)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Salem, E. (2021, April 19). Dancing With Shellcodes: Cracking the latest version of Guloader. Retrieved July 7, 2021.](https://elis531989.medium.com/dancing-with-shellcodes-cracking-the-latest-version-of-guloader-75083fb15cb4)
- [Chen, J. et al. (2021, February 3). Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes. Retrieved April 5, 2021.](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [GReAT. (2014, December 10). Cloud Atlas: RedOctober APT is back in style. Retrieved May 8, 2020.](https://securelist.com/cloud-atlas-redoctober-apt-is-back-in-style/68083/)
- [Symantec. (2018, March 14). Inception Framework: Alive and Well, and Hiding Behind Proxies. Retrieved May 8, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/inception-framework-hiding-behind-proxies)
- [Unit 42. (2024, June 25). 2024-06-25-IOCs-from-Latrodectus-activity. Retrieved September 13, 2024.](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2024-06-25-IOCs-from-Latrodectus-activity.txt)
- [Jazi, H. (2021, February). LazyScripter: From Empire to double RAT. Retrieved November 17, 2024.](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
- [Punsaen Boonyakarn, Shawn Chew, Logeswaran Nadarajan, Mathew Potaczek, Jakub Jozwiak, and Alex Marvi. (2024, June 18). Cloaked and Covert: Uncovering UNC3886 Espionage Operations. Retrieved September 24, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [Raggi, M. et al. (2022, March 7). The Good, the Bad, and the Web Bug: TA416 Increases Operational Tempo Against European Governments as Conflict in Ukraine Escalates. Retrieved March 16, 2022.](https://www.proofpoint.com/us/blog/threat-insight/good-bad-and-web-bug-ta416-increases-operational-tempo-against-european)
- [Golo Muhr, Joshua Chung. (2025, June 23). Hive0154 aka Mustang Panda shifts focus on Tibetan community to deploy Pubload backdoor. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)
- [Maniath, S. and Kadam P. (2019, March 19). Dissecting a NETWIRE Phishing Campaign's Usage of Process Hollowing. Retrieved January 7, 2021.](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
- [Cimpanu, C. (2018, September 13). Sly malware author hides cryptomining botnet behind ever-shifting proxy service. Retrieved September 15, 2020.](https://www.zdnet.com/article/sly-malware-author-hides-cryptomining-botnet-behind-ever-shifting-proxy-service/)
- [Ahn Ho, Facundo Muñoz, & Marc-Etienne M.Léveillé. (2024, March 7). Evasive Panda leverages Monlam Festival to target Tibetans. Retrieved July 25, 2024.](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
- [Threat Hunter Team. (2024, July 23). Daggerfly: Espionage Group Makes Major Update to Toolset. Retrieved July 25, 2024.](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)
- [M. Porolli. (2021, January 21). Operation Spalax: Targeted malware attacks in Colombia. Retrieved September 16, 2022.](https://www.welivesecurity.com/2021/01/12/operation-spalax-targeted-malware-attacks-colombia/)
- [Dumont, R. (2022, June 13). Technical Analysis of PureCrypter: A Fully-Functional Loader Distributing Remote Access Trojans and Information Stealers. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
- [Patrick Schläpfer . (2024, April 10). Raspberry Robin Now Spreading Through Windows Script Files. Retrieved May 17, 2024.](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
- [Group-IB. (2020, August). RedCurl: The Pentest You Didn’t Know About. Retrieved August 9, 2024.](https://www.group-ib.com/resources/research-hub/red-curl/)
- [Group-IB. (2021, November). RedCurl: The Awakening. Retrieved August 14, 2024.](https://www.group-ib.com/resources/research-hub/red-curl-2/)
- [Proofpoint Threat Insight Team, Jeremy H, Axel F. (2020, March 16). New Redline Password Stealer Malware. Retrieved September 17, 2025.](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
- [Splunk Threat Research Team. (2023, June 1). Do Not Cross The 'RedLine' Stealer: Detections and Analysis. Retrieved September 17, 2025.](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
- [Anomali Labs. (2019, March 15). Rocke Evolves Its Arsenal With a New Malware Family Written in Golang. Retrieved April 24, 2019.](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)
- [Liebenberg, D.. (2018, August 30). Rocke: The Champion of Monero Miners. Retrieved May 26, 2020.](https://blog.talosintelligence.com/2018/08/rocke-champion-of-monero-miners.html)
- [Cristian Souza, Eduardo Ovalle, Ashley Muñoz, & Christopher Zachor. (2024, May 23). ShrinkLocker: Turning BitLocker into ransomware. Retrieved December 7, 2024.](https://securelist.com/ransomware-abuses-bitlocker/112643/)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [FireEye. (2021, May 11). Shining a Light on DARKSIDE Ransomware Operations. Retrieved September 22, 2021.](https://www.fireeye.com/blog/threat-research/2021/05/shining-a-light-on-darkside-ransomware-operations.html)
- [Lorber, N. (2021, May 7). Revealing the Snip3 Crypter, a Highly Evasive RAT Loader. Retrieved September 13, 2023.](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
- [Milenkoski, A. (2022, November 7). SocGholish Diversifies and Expands Its Malware Staging Infrastructure to Counter Defenders. Retrieved March 22, 2024.](https://www.sentinelone.com/labs/socgholish-diversifies-and-expands-its-malware-staging-infrastructure-to-counter-defenders/)
- [Kol, Roi. Morag, A. (2020, August 25). Deep Analysis of TeamTNT Techniques Using Container Images to Attack. Retrieved September 22, 2021.](https://blog.aquasec.com/container-security-tnt-container-attack)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Faou, M. (2020, December 2). Turla Crutch: Keeping the “back door” open. Retrieved December 4, 2020.](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
- [DOJ/FBI. (2026, March 19). Case 1:26-mj-00683-CDA: Affidavit in Support of Seizure Warrant: In the Matter of the Seizure of Domain Names Justicehomeland[.]org; karmabelow80[.]org; handala-hack[.]to; and handala-redwatned[.]to. Retrieved April 20, 2026.](https://www.justice.gov/opa/media/1431956/dl?inline)
- [FBI. (2026, March 20). FBI Flash: FLASH-20260320-001:Government of Iran Cyber Actors Deploy Telegram C2 to Push Malware to Identified Targets. Retrieved April 20, 2026.](https://www.ic3.gov/CSA/2026/260320.pdf)
- [Crowdstrike. (2022, January 19). Technical Analysis of the WhisperGate Malicious Bootloader. Retrieved March 10, 2022.](https://www.crowdstrike.com/blog/technical-analysis-of-whispergate-malware)
- [Falcone, R. et al.. (2022, January 20). Threat Brief: Ongoing Russia and Ukraine Cyber Conflict. Retrieved March 10, 2022.](https://unit42.paloaltonetworks.com/ukraine-cyber-conflict-cve-2021-32648-whispergate/#whispergate-malware-family)
- [MSTIC. (2022, January 15). Destructive malware targeting Ukrainian organizations. Retrieved March 10, 2022.](https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)
- [Biasini, N. et al.. (2022, January 21). Ukraine Campaign Delivers Defacement and Wipers, in Continued Escalation. Retrieved March 14, 2022.](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
- [S2W. (2022, January 18). Analysis of Destructive Malware (WhisperGate) targeting Ukraine. Retrieved March 14, 2022.](https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3)

---

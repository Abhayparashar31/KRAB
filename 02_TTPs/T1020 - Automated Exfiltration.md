# Automated Exfiltration

## Description

Adversaries may exfiltrate data, such as sensitive documents, through the use of automated processing after being gathered during Collection. [1]

When automated exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as Exfiltration Over C2 Channel and Exfiltration Over Alternative Protocol .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0046 | ArcaneDoor | ArcaneDoor included scripted exfiltration of collected data. [2] |
| S0438 | Attor | Attor has a file uploader plugin that automatically exfiltrates the collected data and log files to the C2 server. [3] |
| S0050 | CosmicDuke | CosmicDuke exfiltrates collected files automatically over FTP to remote servers. [4] |
| S0538 | Crutch | Crutch has automatically exfiltrated stolen files to Dropbox. [5] |
| S0600 | Doki | Doki has used a script that gathers information from a hardcoded list of IP addresses and uploads to an Ngrok URL. [6] |
| S0377 | Ebury | If credentials are not collected for two weeks, Ebury encrypts the credentials using a public key and sends them via UDP to an IP address located in the DNS TXT record. [7] [8] |
| S0363 | Empire | Empire has the ability to automatically send collected data back to the threat actors' C2. [9] |
| C0001 | Frankenstein | During Frankenstein , the threat actors collected information via Empire , which was automatically sent back to the adversary's C2. [9] |
| G0047 | Gamaredon Group | Gamaredon Group has used modules that automatically upload gathered documents to the C2 server. [1] |
| S1211 | Hannotog | Hannotog can upload encyrpted data for exfiltration. [10] |
| G0004 | Ke3chang | Ke3chang has performed frequent and scheduled data exfiltration from compromised networks. [11] |
| G0094 | Kimsuky | Kimsuky has exfiltrated data to C2 servers using an automated script that executes every 10 minutes and after successful checks for the presence of pre-designated staged filenames. [12] |
| S0395 | LightNeuron | LightNeuron can be configured to automatically exfiltrate files under a specified directory. [13] |
| S0409 | Machete | Machete ’s collected files are exfiltrated automatically to remote servers. [14] |
| S1017 | OutSteel | OutSteel can automatically upload collected files to its C2 server. [15] |
| S0643 | Peppy | Peppy has the ability to automatically exfiltrate files and keylogs. [16] |
| S1148 | Raccoon Stealer | Raccoon Stealer will automatically collect and exfiltrate data identified in received configuration files from command and control nodes. [17] [18] [19] |
| G1039 | RedCurl | RedCurl has used batch scripts to exfiltrate data. [20] [21] |
| S0090 | Rover | Rover automatically searches for files on local drives based on a predefined list of file extensions and sends them to the command and control server every 60 minutes. Rover also automatically sends keylogger files and screenshots to the C2 server on a regular timeframe. [22] |
| C0059 | Salesforce Data Exfiltration | During Salesforce Data Exfiltration , threat actors used API queries to automatically exfiltrate large volumes of data. [23] |
| S0445 | ShimRatReporter | ShimRatReporter sent collected system and network information compiled into a report to an adversary-controlled C2. [24] |
| G0121 | Sidewinder | Sidewinder has configured tools to automatically send collected files to attacker controlled servers. [25] |
| S1166 | Solar | Solar can automatically exfitrate files from compromised systems. [26] |
| S1183 | StrelaStealer | StrelaStealer automatically sends gathered email credentials following collection to command and control servers via HTTP POST. [27] [28] |
| S0491 | StrongPity | StrongPity can automatically exfiltrate collected documents to the C2 server. [29] [30] |
| S0467 | TajMahal | TajMahal has the ability to manage an automated queue of egress files and commands sent to its C2. [31] |
| S0131 | TINYTYPHON | When a document is found matching one of the extensions in the configuration, TINYTYPHON uploads it to the C2 server. [32] |
| G0081 | Tropic Trooper | Tropic Trooper has used a copy function to automatically exfiltrate sensitive data from air-gapped systems using USB storage. [33] |
| S0136 | USBStealer | USBStealer automatically exfiltrates collected files via removable media when an infected device connects to an air-gapped victim machine after initially being connected to an internet-enabled victim machine. [34] |
| G1035 | Winter Vivern | Winter Vivern delivered a PowerShell script capable of recursively scanning victim machines looking for various file types before exfiltrating identified files via HTTP. [35] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0397 | Automated Exfiltration Detection Strategy | AN1113 | Detection of automated tools or scripts periodically transmitting data to external destinations using scheduled tasks or background processes. |
| AN1114 | Background scripts (e.g., via cron) or daemons transmitting data repeatedly to remote IPs or URLs. |  |  |
| AN1115 | Observation of LaunchAgents or LaunchDaemons establishing periodic external connections indicative of automated data transfer. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0397 | Automated Exfiltration Detection Strategy | AN1113 | Detection of automated tools or scripts periodically transmitting data to external destinations using scheduled tasks or background processes. |
| AN1114 | Background scripts (e.g., via cron) or daemons transmitting data repeatedly to remote IPs or URLs. |  |  |
| AN1115 | Observation of LaunchAgents or LaunchDaemons establishing periodic external connections indicative of automated data transfer. |  |  |

---

## References

- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Canadian Centre for Cyber Security. (2024, April 24). Cyber Activity Impacting CISCO ASA VPNs. Retrieved January 6, 2025.](https://www.cyber.gc.ca/en/news-events/cyber-activity-impacting-cisco-asa-vpns)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [F-Secure Labs. (2014, July). COSMICDUKE Cosmu with a twist of MiniDuke. Retrieved July 3, 2014.](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)
- [Faou, M. (2020, December 2). Turla Crutch: Keeping the “back door” open. Retrieved December 4, 2020.](https://www.welivesecurity.com/2020/12/02/turla-crutch-keeping-back-door-open/)
- [Fishbein, N., Kajiloti, M.. (2020, July 28). Watch Your Containers: Doki Infecting Docker Servers in the Cloud. Retrieved March 30, 2021.](https://www.intezer.com/blog/cloud-security/watch-your-containers-doki-infecting-docker-servers-in-the-cloud/)
- [Bilodeau, O., Bureau, M., Calvet, J., Dorais-Joncas, A., Léveillé, M., Vanheuverzwijn, B. (2014, March 18). Operation Windigo – the vivisection of a large Linux server‑side credential‑stealing malware campaign. Retrieved February 10, 2021.](https://www.welivesecurity.com/2014/03/18/operation-windigo-the-vivisection-of-a-large-linux-server-side-credential-stealing-malware-campaign/)
- [Marc-Etienne M.Léveillé. (2024, May 1). Ebury is alive but unseen. Retrieved May 21, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/ebury-is-alive-but-unseen.pdf)
- [Adamitis, D. et al. (2019, June 4). It's alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign. Retrieved May 11, 2020.](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
- [Symntec Threat Hunter Team. (2022, November 12). Billbug: State-sponsored Actor Targets Cert Authority, Government Agencies in Multiple Asian Countries. Retrieved March 15, 2025.](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Faou, M. (2019, May). Turla LightNeuron: One email away from remote code execution. Retrieved June 24, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [S2W TALON. (2022, June 16). Raccoon Stealer is Back with a New Version. Retrieved August 1, 2024.](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
- [Quentin Bourgue, Pierre le Bourhis, & Sekoia TDR. (2022, June 28). Raccoon Stealer v2 - Part 1: The return of the dead. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Group-IB. (2020, August). RedCurl: The Pentest You Didn’t Know About. Retrieved August 9, 2024.](https://www.group-ib.com/resources/research-hub/red-curl/)
- [Group-IB. (2021, November). RedCurl: The Awakening. Retrieved August 14, 2024.](https://www.group-ib.com/resources/research-hub/red-curl-2/)
- [Ray, V., Hayashi, K. (2016, February 29). New Malware ‘Rover’ Targets Indian Ambassador to Afghanistan. Retrieved February 29, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
- [FBI Cyber Division. (2025, September 12). Cyber Criminal Groups UNC6040 and UNC6395 Compromising Salesforce Instances for Data Theft and Extortion. Retrieved October 22, 2025.](https://www.ic3.gov/CSA/2025/250912.pdf)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Hegel, T. (2021, January 13). A Global Perspective of the SideWinder APT. Retrieved January 27, 2021.](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)
- [Hromcova, Z. and Burgher, A. (2023, September 21). OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes. Retrieved November 21, 2024.](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)
- [DCSO CyTec Blog. (2022, November 8). #ShortAndMalicious: StrelaStealer aims for mail credentials. Retrieved December 31, 2024.](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)
- [Golo Mühr, Joe Fasulo & Charlotte Hammond, IBM X-Force. (2024, November 12). Strela Stealer: Today’s invoice is tomorrow’s phish. Retrieved December 31, 2024.](https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/)
- [Mercer, W. et al. (2020, June 29). PROMETHIUM extends global reach with StrongPity3 APT. Retrieved July 20, 2020.](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
- [Tudorica, R. et al. (2020, June 30). StrongPity APT - Revealing Trojanized Tools, Working Hours and Infrastructure. Retrieved July 20, 2020.](https://www.bitdefender.com/files/News/CaseStudies/study/353/Bitdefender-Whitepaper-StrongPity-APT.pdf)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Calvet, J. (2014, November 11). Sednit Espionage Group Attacking Air-Gapped Networks. Retrieved January 4, 2017.](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
- [CERT-UA. (2023, February 1). UAC-0114 aka Winter Vivern to target Ukrainian and Polish GOV entities (CERT-UA#5909). Retrieved July 29, 2024.](https://cert.gov.ua/article/3761104)

---


### 🔗 KRAB Intelligence Correlation
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025 Multi-Industry Hypervisor and Retail Extortion Campaign]] [related_campaign:: [[2025 Multi-Industry Hypervisor and Retail Extortion Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025-2026 SaaS Identity Crisis and Help Desk Exploitation Wave]] [related_campaign:: [[2025-2026 SaaS Identity Crisis and Help Desk Exploitation Wave]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2026 Enterprise LMS and Canvas Data Extortion Campaign]] [related_campaign:: [[2026 Enterprise LMS and Canvas Data Extortion Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2026 Oracle PeopleSoft Mass Data Theft Campaign]] [related_campaign:: [[2026 Oracle PeopleSoft Mass Data Theft Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[Salesforce Massive Corporate Extortion Wave]] [related_campaign:: [[Salesforce Massive Corporate Extortion Wave]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Scattered Lapsus$ Hunters]] [related_actor:: [[Scattered Lapsus$ Hunters]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[RansomHub]] [related_actor:: [[RansomHub]]]

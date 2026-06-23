# Dynamic Resolution

## Description

Adversaries may dynamically establish connections to command and control infrastructure to evade common detections and remediations. This may be achieved by using malware that shares a common algorithm with the infrastructure the adversary uses to receive the malware's communications. These calculations can be used to dynamically adjust parameters such as the domain name, IP address, or port number the malware uses for command and control.

Adversaries may use dynamic resolution for the purpose of Fallback Channels . When contact is lost with the primary command and control server malware may employ dynamic resolution as a means to reestablishing command and control. [1] [2] [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0099 | APT-C-36 | APT-C-36 has used DDNS services such as DuckDNS, noip[.]com, and con-ip[.]com to redirect victims to sites or repositories hosting malware implants. [4] [5] [6] [7] [8] |
| G0016 | APT29 | APT29 has used Dynamic DNS providers for their malware C2 infrastructure. [9] |
| S1087 | AsyncRAT | AsyncRAT can be configured to use dynamic DNS. [10] |
| S0268 | Bisonal | Bisonal has used a dynamic DNS service for C2. [11] |
| G1002 | BITTER | BITTER has used DDNS for C2 communications. [12] |
| S9015 | BRICKSTORM | BRICKSTORM has utilized DNS services sslip.io and nip.io to resolve C2 IP addresses. [13] |
| C0026 | C0026 | During C0026 , the threat actors re-registered a ClouDNS dynamic DNS subdomain which was previously used by ANDROMEDA . [14] |
| G0047 | Gamaredon Group | Gamaredon Group has incorporated dynamic DNS domains in its infrastructure. [15] |
| S0666 | Gelsemium | Gelsemium can use dynamic DNS domain names in C2. [16] |
| C0043 | Indian Critical Infrastructure Intrusions | During Indian Critical Infrastructure Intrusions , RedEcho used dynamic DNS domains associated with malicious infrastructure. [17] |
| G0094 | Kimsuky | Kimsuky has used Dynamic DNS (DDNS) services, such as FreeDNS or No-IP DDNS, to include servers located in South Korea. [18] |
| S0449 | Maze | Maze has forged POST strings with a random choice from a list of possibilities including "forum", "php", "view", etc. while making connection with the C2, hindering detection efforts. [19] |
| S0034 | NETEAGLE | NETEAGLE can use HTTP to download resources that contain an IP address and port number pair to connect to for C2. [20] |
| C0002 | Night Dragon | During Night Dragon , threat actors used dynamic DNS services for C2. [21] |
| C0016 | Operation Dust Storm | For Operation Dust Storm , the threat actors used dynamic DNS domains from a variety of free providers, including No-IP, Oray, and 3322. [22] |
| C0005 | Operation Spalax | For Operation Spalax , the threat actors used dynamic DNS services, including Duck DNS and DNS Exit, as part of their C2 infrastructure. [23] |
| G1042 | RedEcho | RedEcho used dynamic DNS domains associated with malicious infrastructure. [17] |
| S0332 | Remcos | Remcos has used dynamic DNS domains in C2 communications. [5] |
| S0148 | RTM | RTM has resolved Pony C2 server IP addresses by either converting Bitcoin blockchain transaction data to specific octets, or accessing IP addresses directly within the Namecoin blockchain. [24] [25] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 used dynamic DNS resolution to construct and resolve to randomly-generated subdomains for C2. [26] |
| S0559 | SUNBURST | SUNBURST dynamically resolved C2 infrastructure for randomly-generated subdomains within a parent domain. [27] |
| G1018 | TA2541 | TA2541 has used dynamic DNS services for C2 infrastructure. [28] |
| S0671 | Tomiris | Tomiris has connected to a signalization server that provides a URL and port, and then Tomiris sends a GET request to that URL to establish C2. [29] |
| G0134 | Transparent Tribe | Transparent Tribe has used dynamic DNS services to set up C2. [30] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Malware researchers can reverse engineer malware variants that use dynamic resolution and determine future C2 infrastructure that the malware will attempt to contact, but this is a time and resource intensive effort. [31] [32] |
| M1021 | Restrict Web-Based Content | In some cases a local DNS sinkhole may be used to help prevent behaviors associated with dynamic resolution. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0039 | Detection Strategy for Dynamic Resolution across OS Platforms | AN0109 | Correlate high-frequency or anomalous DNS query activity with processes that do not normally generate network requests (e.g., Office apps, system utilities). Detect pseudo-random or high-entropy domain lookups indicative of domain generation algorithms (DGAs). |
| AN0110 | Monitor /var/log/audit/audit.log and DNS resolver logs for repeated failed lookups or connections to high-entropy domain names. Correlate suspicious DNS queries with process lineage (e.g., Python, bash, or unusual system daemons). |  |  |
| AN0111 | Inspect unified logs for anomalous DNS resolutions triggered by non-network applications. Flag repeated connections to newly registered or algorithmically generated domains. Correlate with endpoint process telemetry. |  |  |
| AN0112 | Monitor esxcli and syslog records for DNS resolver changes or repeated queries to unusual external domains by management agents. Detect unauthorized changes to VM or host network settings that redirect DNS lookups. |  |  |

---

## References

- [Brumaghin, E. et al. (2017, September 18). CCleanup: A Vast Number of Machines at Risk. Retrieved March 9, 2018.](http://blog.talosintelligence.com/2017/09/avast-distributes-malware.html)
- [Dunwoody, M.. (2017, April 3). Dissecting One of APT29’s Fileless WMI and PowerShell Backdoors (POSHSPY). Retrieved April 5, 2017.](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)
- [ESET. (2017, December 21). Sednit update: How Fancy Bear Spent the Year. Retrieved February 18, 2019.](https://www.welivesecurity.com/2017/12/21/sednit-update-fancy-bear-spent-year/)
- [Global Research & Analysis Team, Kaspersky. (2024, August 19). BlindEagle flying high in Latin America. Retrieved April 16, 2026.](https://securelist.com/blindeagle-apt/113414/)
- [Check Point Research. (2025, March 10). Blind Eagle: …And Justice for All. Retrieved April 16, 2026.](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
- [Melnyk, S. (2025, June 27). Tracing Blind Eagle to Proton66. Retrieved April 16, 2026.](https://www.levelblue.com/blogs/spiderlabs-blog/tracing-blind-eagle-to-proton66/)
- [Insikt Group. (2025, August 26). TAG-144’s Persistent Grip on South American Organizations. Retrieved April 16, 2026.](https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0826.pdf)
- [Pellegrino, G. (2025, December 16). BlindEagle Targets Colombian Government Agency with Caminho and DCRAT. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/blindeagle-targets-colombian-government-agency-caminho-and-dcrat)
- [Mandiant. (2022, May 2). UNC3524: Eye Spy on Your Email. Retrieved August 17, 2023.](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
- [Nyan-x-Cat. (n.d.). NYAN-x-CAT / AsyncRAT-C-Sharp. Retrieved October 3, 2023.](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [Dela Paz, R. (2016, October 21). BITTER: a targeted attack against Pakistan. Retrieved June 1, 2022.](https://www.forcepoint.com/blog/x-labs/bitter-targeted-attack-against-pakistan)
- [Sarah Yoder, John Wolfram, Ashley Pearson, Doug Bienstock, Josh Madeley, Josh Murchie, Brad Slaybaugh, Matt Lin, Geoff Carstairs, Austin Larsen. (2025, September 24). Another BRICKSTORM: Stealthy Backdoor Enabling Espionage into Tech and Legal Sectors. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Unit 42. (2022, February 3). Russia’s Gamaredon aka Primitive Bear APT Group Actively Targeting Ukraine. Retrieved February 21, 2022.](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Recorded Future Insikt Group. (2021, February). China-Linked Group RedEcho Targets the Indian Power Sector Amid Heightened Border Tensions. Retrieved November 21, 2024.](https://go.recordedfuture.com/hubfs/reports/cta-2021-0228.pdf)
- [Naumaan, S., et al. (2025, April 17). Around the World in 90 Days: State-Sponsored Actors Try ClickFix . Retrieved January 21, 2026.](https://www.proofpoint.com/us/blog/threat-insight/around-world-90-days-state-sponsored-actors-try-clickfix)
- [Mundo, A. (2020, March 26). Ransomware Maze. Retrieved May 18, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/ransomware-maze/)
- [FireEye Labs. (2015, April). APT30 AND THE MECHANICS OF A LONG-RUNNING CYBER ESPIONAGE OPERATION. Retrieved November 17, 2024.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
- [McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [M. Porolli. (2021, January 21). Operation Spalax: Targeted malware attacks in Colombia. Retrieved September 16, 2022.](https://www.welivesecurity.com/2021/01/12/operation-spalax-targeted-malware-attacks-colombia/)
- [Eisenkraft, K., Olshtein, A. (2019, October 17). Pony’s C&C servers hidden inside the Bitcoin blockchain. Retrieved June 15, 2020.](https://research.checkpoint.com/2019/ponys-cc-servers-hidden-inside-the-bitcoin-blockchain/)
- [Duncan, B., Harbison, M. (2019, January 23). Russian Language Malspam Pushing Redaman Banking Malware. Retrieved June 16, 2020.](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
- [Cash, D. et al. (2020, December 14). Dark Halo Leverages SolarWinds Compromise to Breach Organizations. Retrieved December 29, 2020.](https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [Larson, S. and Wise, J. (2022, February 15). Charting TA2541's Flight. Retrieved September 12, 2023.](https://www.proofpoint.com/us/blog/threat-insight/charting-ta2541s-flight)
- [Kwiatkoswki, I. and Delcher, P. (2021, September 29). DarkHalo After SolarWinds: the Tomiris connection. Retrieved December 27, 2021.](https://securelist.com/darkhalo-after-solarwinds-the-tomiris-connection/104311/)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Sternfeld, U. (2016). Dissecting Domain Generation Algorithms: Eight Real World DGA Variants. Retrieved February 18, 2019.](http://go.cybereason.com/rs/996-YZT-709/images/Cybereason-Lab-Analysis-Dissecting-DGAs-Eight-Real-World-DGA-Variants.pdf)
- [Kasza, A. (2015, February 18). Using Algorithms to Brute Force Algorithms. Retrieved February 18, 2019.](https://umbrella.cisco.com/blog/2015/02/18/at-high-noon-algorithms-do-battle/)

---

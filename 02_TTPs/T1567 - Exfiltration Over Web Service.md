# Exfiltration Over Web Service

## Description

Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules may also already exist to permit traffic to these services.

Web service providers also commonly use SSL/TLS encryption, giving adversaries an added level of protection.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0062 | Anthropic AI-orchestrated Campaign | During the Anthropic AI-orchestrated Campaign , the adversary utilized Claude Code to generate a detailed summary report of collected data, which is then reviewed and approved by the adversary prior to exfiltration of data over Claude. [1] |
| S0622 | AppleSeed | AppleSeed has exfiltrated files using web services. [2] |
| G0007 | APT28 | APT28 can exfiltrate data over Google Drive. [3] |
| C0051 | APT28 Nearest Neighbor Campaign | During APT28 Nearest Neighbor Campaign , APT28 exfiltrated data over public-facing webservers – such as Google Drive. [4] |
| G1043 | BlackByte | BlackByte has used services such as anonymfiles.com and file.io to exfiltrate victim data. [5] |
| C0017 | C0017 | During C0017 , APT41 used Cloudflare services for data exfiltration. [6] |
| G1052 | Contagious Interview | Contagious Interview has leveraged Telegram API to exfiltrate stolen data. [7] |
| S0547 | DropBook | DropBook has used legitimate web services to exfiltrate data. [8] |
| S1179 | Exbyte | Exbyte exfiltrates collected data to online file hosting sites such as Mega.co.nz . [9] [10] |
| S1245 | InvisibleFerret | InvisibleFerret has leveraged Telegram chat to upload stolen data using the Telegram API with a bot token. [7] [11] |
| G0059 | Magic Hound | Magic Hound has used the Telegram API sendMessage to relay data on compromised devices. [12] |
| S0508 | ngrok | ngrok has been used by threat actors to configure servers for data exfiltration. [13] |
| S1171 | OilCheck | OilCheck can upload documents from compromised hosts to a shared Microsoft Office 365 Outlook email account for exfiltration. [14] |
| C0059 | Salesforce Data Exfiltration | During Salesforce Data Exfiltration , threat actors exfiltrated data via legitimate Salesforce API communication channels including the Salesforce Data Loader application. [15] [16] |
| S1168 | SampleCheck5000 | SampleCheck5000 can use the Microsoft Office Exchange Web Services API to access an actor-controlled account and retrieve files for exfiltration. [17] [14] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1057 | Data Loss Prevention | Data loss prevention can be detect and block sensitive data being uploaded to web services via web browsers. |
| M1021 | Restrict Web-Based Content | Web proxies can be used to enforce an external network communication policy that prevents use of unauthorized external services. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0548 | Detection Strategy for Exfiltration Over Web Service | AN1511 | Processes that normally do not initiate network communications suddenly making outbound HTTPS connections with high outbound-to-inbound data ratios. Defender view: correlation between process creation logs (e.g., Word, Excel, PowerShell) and subsequent anomalous network traffic volumes toward common web services (Dropbox, Google Drive, OneDrive). |
| AN1512 | Processes (tar, curl, python scripts) accessing large file sets and initiating outbound HTTPS POST requests with payload sizes inconsistent with baseline activity. Defender perspective: detect abnormal sequence of file archival followed by encrypted uploads to external web services. |  |  |
| AN1513 | Office apps or scripts writing files followed by xattr manipulation (to evade quarantine) and subsequent HTTPS uploads. Defender perspective: anomalous file modification + outbound TLS traffic originating from non-networking apps (Word, Excel, Preview). |  |  |
| AN1514 | Abnormal API calls from user accounts invoking file upload endpoints outside normal baselines (M365, Google Drive, Box). Defender perspective: monitor unified audit logs for elevated frequency of Upload, Create, or Copy operations from compromised accounts. |  |  |
| AN1515 | ESXi guest OS or management interface processes establishing unexpected external HTTPS connections. Defender perspective: monitor vmx or hostd processes making outbound web requests with significant data transfer. |  |  |

---

## References

- [Anthropic. (2025, November). Disrupting the first reported AI-orchestrated cyber espionage campaign. Retrieved April 20, 2026.](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
- [KISA. (2021). Phishing Target Reconnaissance and Attack Resource Analysis Operation Muzabi. Retrieved March 8, 2024.](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
- [Hacquebord, F., Remorin, L. (2020, December 17). Pawn Storm’s Lack of Sophistication as a Strategy. Retrieved January 13, 2021.](https://www.trendmicro.com/en_us/research/20/l/pawn-storm-lack-of-sophistication-as-a-strategy.html)
- [Koessel, Sean. Adair, Steven. Lancaster, Tom. (2024, November 22). The Nearest Neighbor Attack: How A Russian APT Weaponized Nearby Wi-Fi Networks for Covert Access. Retrieved February 25, 2025.](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)
- [Huseyin Can Yuceel. (2022, February 21). TTPs used by BlackByte Ransomware Targeting Critical Infrastructure. Retrieved December 16, 2024.](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Ilascu, I. (2020, December 14). Hacking group’s new malware abuses Google and Facebook services. Retrieved December 28, 2020.](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
- [Symantec Threat Hunter Team. (2022, October 21). Exbyte: BlackByte Ransomware Attackers Deploy New Exfiltration Tool. Retrieved December 16, 2024.](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [Seongsu Park. (2024, November 4). From Pyongyang to Your Payroll: The Rise of North Korean Remote Workers in the West. Retrieved October 17, 2025.](https://www.zscaler.com/blogs/security-research/pyongyang-your-payroll-rise-north-korean-remote-workers-west)
- [Bash, A. (2021, October 14). Countering threats from Iran. Retrieved January 4, 2023.](https://blog.google/threat-analysis-group/countering-threats-iran/)
- [Segura, J. (2020, February 26). Fraudsters cloak credit card skimmer with fake content delivery network, ngrok server. Retrieved September 15, 2020.](https://blog.malwarebytes.com/threat-analysis/2020/02/fraudsters-cloak-credit-card-skimmer-with-fake-content-delivery-network-ngrok-server/)
- [Hromcova, Z. and Burgher, A. (2023, December 14). OilRig’s persistent attacks using cloud service-powered downloaders. Retrieved November 26, 2024.](https://www.welivesecurity.com/en/eset-research/oilrig-persistent-attacks-cloud-service-powered-downloaders/)
- [Google Threat Intelligence Group. (2025, June 4). The Cost of a Call: From Voice Phishing to Data Extortion. Retrieved October 22, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion)
- [FBI Cyber Division. (2025, September 12). Cyber Criminal Groups UNC6040 and UNC6395 Compromising Salesforce Instances for Data Theft and Extortion. Retrieved October 22, 2025.](https://www.ic3.gov/CSA/2025/250912.pdf)
- [Hromcova, Z. and Burgher, A. (2023, September 21). OilRig’s Outer Space and Juicy Mix: Same ol’ rig, new drill pipes. Retrieved November 21, 2024.](https://www.welivesecurity.com/en/eset-research/oilrigs-outer-space-juicy-mix-same-ol-rig-new-drill-pipes/)

---

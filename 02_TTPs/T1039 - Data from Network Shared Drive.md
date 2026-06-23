# Data from Network Shared Drive

## Description

Adversaries may search network shares on computers they have compromised to find files of interest. Sensitive data can be collected from remote systems via shared network drives (host shared directory, network file server, etc.) that are accessible from the current system prior to Exfiltration. Interactive command shells may be in use, and common functionality within cmd may be used to gather information.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0007 | APT28 | APT28 has collected files from network shared drives. [1] |
| S0128 | BADNEWS | When it first starts, BADNEWS crawls the victim's mapped drives and collects documents with the following extensions: .doc, .docx, .pdf, .ppt, .pptx, and .txt. [2] |
| G0060 | BRONZE BUTLER | BRONZE BUTLER has exfiltrated files stolen from file shares. [3] |
| C0015 | C0015 | During C0015 , the threat actors collected files from network shared drives prior to network encryption. [4] |
| G0114 | Chimera | Chimera has collected data of interest from network shares. [5] |
| S0050 | CosmicDuke | CosmicDuke steals user files from network shared drives with file extensions and keywords that match a predefined list. [6] |
| S0554 | Egregor | Egregor can collect any files found in the enumerated drivers before sending it to its C2 channel. [7] |
| G0117 | Fox Kitten | Fox Kitten has searched network shares to access sensitive documents. [8] |
| G0047 | Gamaredon Group | Gamaredon Group malware has collected Microsoft Office documents from mapped network drives. [9] [10] |
| G0045 | menuPass | menuPass has collected data from remote systems by mounting network shares with net use and using Robocopy to transfer data. [11] |
| S0458 | Ramsay | Ramsay can collect data from network drives and stage it for exfiltration. [12] |
| G1039 | RedCurl | RedCurl has collected data about network drives. [13] [14] |
| G0054 | Sowbug | Sowbug extracted Word documents from a file server on a victim network. [15] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0410 | Detection Strategy for Data from Network Shared Drive | AN1145 | Monitoring of file access to network shares (e.g., C$, Admin$) followed by unusual read or copy operations by processes not typically associated with such activity (e.g., PowerShell, certutil). |
| AN1146 | Unusual access or copying of files from mounted network drives (e.g., NFS, CIFS/SMB) by user shells or scripts followed by large data transfer. |  |  |
| AN1147 | Detection of file access from mounted SMB shares followed by copy or exfil commands from Terminal or script interpreter processes. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0410 | Detection Strategy for Data from Network Shared Drive | AN1145 | Monitoring of file access to network shares (e.g., C$, Admin$) followed by unusual read or copy operations by processes not typically associated with such activity (e.g., PowerShell, certutil). |
| AN1146 | Unusual access or copying of files from mounted network drives (e.g., NFS, CIFS/SMB) by user shells or scripts followed by large data transfer. |  |  |
| AN1147 | Detection of file access from mounted SMB shares followed by copy or exfil commands from Terminal or script interpreter processes. |  |  |

---

## References

- [NSA, CISA, FBI, NCSC. (2021, July). Russian GRU Conducting Global Brute Force Campaign to Compromise Enterprise and Cloud Environments. Retrieved July 26, 2021.](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Counter Threat Unit Research Team. (2017, October 12). BRONZE BUTLER Targets Japanese Enterprises. Retrieved January 4, 2018.](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [F-Secure Labs. (2014, July). COSMICDUKE Cosmu with a twist of MiniDuke. Retrieved July 3, 2014.](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)
- [NHS Digital. (2020, November 26). Egregor Ransomware The RaaS successor to Maze. Retrieved December 29, 2020.](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
- [CISA. (2020, September 15). Iran-Based Threat Actor Exploits VPN Vulnerabilities. Retrieved December 21, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper. Retrieved April 5, 2017.](https://web.archive.org/web/20220224041316/https:/www.pwc.co.uk/cyber-security/pdf/cloud-hopper-report-final-v4.pdf)
- [Sanmillan, I.. (2020, May 13). Ramsay: A cyber‑espionage toolkit tailored for air‑gapped networks. Retrieved May 27, 2020.](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
- [Group-IB. (2020, August). RedCurl: The Pentest You Didn’t Know About. Retrieved August 9, 2024.](https://www.group-ib.com/resources/research-hub/red-curl/)
- [Group-IB. (2021, November). RedCurl: The Awakening. Retrieved August 14, 2024.](https://www.group-ib.com/resources/research-hub/red-curl-2/)
- [Symantec Security Response. (2017, November 7). Sowbug: Cyber espionage group targets South American and Southeast Asian governments. Retrieved November 16, 2017.](https://www.symantec.com/connect/blogs/sowbug-cyber-espionage-group-targets-south-american-and-southeast-asian-governments)

---

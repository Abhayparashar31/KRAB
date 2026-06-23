# Data Transfer Size Limits

## Description

An adversary may exfiltrate data in fixed size chunks instead of whole files or limit packet sizes below certain thresholds. This approach may be used to avoid triggering network data transfer threshold alerts.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0622 | AppleSeed | AppleSeed has divided files if the size is 0x1000000 bytes or more. [1] |
| G0007 | APT28 | APT28 has split archived exfiltration files into chunks smaller than 1MB. [2] |
| G0096 | APT41 | APT41 transfers post-exploitation files dividing the payload into fixed-size chunks to evade detection. [3] |
| C0015 | C0015 | During C0015 , the threat actors limited Rclone 's bandwidth setting during exfiltration. [4] |
| C0026 | C0026 | During C0026 , the threat actors split encrypted archives containing stolen files and information into 3MB parts prior to exfiltration. [5] |
| S0030 | Carbanak | Carbanak exfiltrates data in compressed chunks if a message is larger than 4096 bytes . [6] |
| S0154 | Cobalt Strike | Cobalt Strike will break large data sets into smaller chunks for exfiltration. [7] |
| S0170 | Helminth | Helminth splits data into chunks up to 23 bytes and sends the data in DNS queries to its C2 server. [8] |
| S0487 | Kessel | Kessel can split the data to be exilftrated into chunks that will fit in subdomains of DNS queries. [9] |
| S1020 | Kevin | Kevin can exfiltrate data to the C2 server in 27-character chunks. [10] |
| G1014 | LuminousMoth | LuminousMoth has split archived files into multiple parts to bypass a 5MB limit. [11] |
| S1141 | LunarWeb | LunarWeb can split exfiltrated data that exceeds 1.33 MB in size into multiple random sized parts between 384 and 512 KB. [12] |
| S0699 | Mythic | Mythic supports custom chunk sizes used to upload/download files. [13] |
| S0644 | ObliqueRAT | ObliqueRAT can break large files of interest into smaller chunks to prepare them for exfiltration. [14] |
| S0264 | OopsIE | OopsIE exfiltrates command output and collected files to its C2 server in 1500-byte blocks. [15] |
| G1040 | Play | Play has split victims' files into chunks for exfiltration. [16] [17] |
| S0150 | POSHSPY | POSHSPY uploads data in 2048-byte chunks. [18] |
| S1040 | Rclone | The Rclone "chunker" overlay supports splitting large files in smaller chunks during upload to circumvent size limits. [19] [4] |
| S0495 | RDAT | RDAT can upload a file via HTTP POST response to the C2 split into 102,400-byte portions. RDAT can also download data from the C2 which is split into 81,920-byte portions. [20] |
| S1200 | StealBit | StealBit can be configured to exfiltrate files at a specified rate to evade network detection mechanisms. [21] |
| G0027 | Threat Group-3390 | Threat Group-3390 actors have split RAR files for exfiltration into parts. [22] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0213 | Detection Strategy for Data Transfer Size Limits and Chunked Exfiltration | AN0596 | Adversary uses a process to establish outbound connections that transmit uniform packet sizes at a consistent interval, avoiding threshold-based network alerts. |
| AN0597 | Outbound connections from non-network-facing processes repeatedly send similarly sized payloads within uniform time intervals. |  |  |
| AN0598 | Processes on macOS initiate external connections that consistently transmit data in fixed sizes using LaunchAgents or unexpected users. |  |  |

---

## References

- [KISA. (2021). Phishing Target Reconnaissance and Attack Resource Analysis Operation Muzabi. Retrieved March 8, 2024.](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
- [NSA, CISA, FBI, NCSC. (2021, July). Russian GRU Conducting Global Brute Force Campaign to Compromise Enterprise and Cloud Environments. Retrieved July 26, 2021.](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)
- [Nikita Rostovcev. (2022, August 18). APT41 World Tour 2021 on a tight schedule. Retrieved February 22, 2024.](https://www.group-ib.com/blog/apt41-world-tour-2021/)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Bennett, J., Vengerik, B. (2017, June 12). Behind the CARBANAK Backdoor. Retrieved June 11, 2018.](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)
- [Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
- [Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Botezatu, B and etl. (2021, July 21). LuminousMoth - PlugX, File Exfiltration and Persistence Revisited. Retrieved October 20, 2022.](https://www.bitdefender.com/blog/labs/luminousmoth-plugx-file-exfiltration-and-persistence-revisited)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [Thomas, C. (n.d.). Mythc Documentation. Retrieved March 25, 2022.](https://docs.mythic-c2.net/)
- [Malhotra, A. (2021, March 2). ObliqueRAT returns with new campaign using hijacked websites. Retrieved September 2, 2021.](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
- [Lee, B., Falcone, R. (2018, February 23). OopsIE! OilRig Uses ThreeDollars to Deliver New Trojan. Retrieved July 16, 2018.](https://researchcenter.paloaltonetworks.com/2018/02/unit42-oopsie-oilrig-uses-threedollars-deliver-new-trojan/)
- [CISA. (2023, December 18). #StopRansomware: Play Ransomware AA23-352A. Retrieved September 24, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)
- [Trend Micro Research. (2023, July 21). Ransomware Spotlight: Play. Retrieved September 24, 2024.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
- [Dunwoody, M.. (2017, April 3). Dissecting One of APT29’s Fileless WMI and PowerShell Backdoors (POSHSPY). Retrieved April 5, 2017.](https://www.fireeye.com/blog/threat-research/2017/03/dissecting_one_ofap.html)
- [Nick Craig-Wood. (n.d.). Rclone syncs your files to cloud storage. Retrieved August 30, 2022.](https://rclone.org)
- [Falcone, R. (2020, July 22). OilRig Targets Middle Eastern Telecommunications Organization and Adds Novel C2 Channel with Steganography to Its Inventory. Retrieved July 28, 2020.](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
- [Cybereason Global SOC Team. (n.d.). THREAT ANALYSIS REPORT: Inside the LockBit Arsenal - The StealBit Exfiltration Tool. Retrieved January 29, 2025.](https://www.cybereason.com/blog/research/threat-analysis-report-inside-the-lockbit-arsenal-the-stealbit-exfiltration-tool)
- [Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)

---

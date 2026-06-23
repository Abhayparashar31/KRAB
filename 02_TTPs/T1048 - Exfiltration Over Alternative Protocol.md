# Exfiltration Over Alternative Protocol

## Description

Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.

Alternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel. Adversaries may also opt to encrypt and/or obfuscate these alternate channels.

Exfiltration Over Alternative Protocol can be done using various common operating system utilities such as Net /SMB or FTP. [1] On macOS and Linux curl may be used to invoke protocols such as HTTP/S or FTP/S to exfiltrate data from a system. [2]

Many IaaS and SaaS platforms (such as Microsoft Exchange, Microsoft SharePoint, GitHub, and AWS S3) support the direct download of files, emails, source code, and other sensitive information via the web console or Cloud API .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0677 | AADInternals | AADInternals can directly download cloud user data such as OneDrive files. [3] |
| S0482 | Bundlore | Bundlore uses the curl -s -L -o command to exfiltrate archived data to a URL. [2] |
| S0631 | Chaes | Chaes has exfiltrated its collected data from the infected machine to the C2, sometimes using the MIME protocol. [4] |
| S0503 | FrameworkPOS | FrameworkPOS can use DNS tunneling for exfiltration of credit card data. [5] |
| S0203 | Hydraq | Hydraq connects to a predefined domain on port 443 to exfil gathered information. [6] |
| S0641 | Kobalos | Kobalos can exfiltrate credentials over the network via UDP. [7] |
| G1040 | Play | Play has used WinSCP to exfiltrate data to actor-controlled accounts. [8] [9] |
| S0428 | PoetRAT | PoetRAT has used a .NET tool named dog.exe to exiltrate information over an e-mail account. [10] |
| G0139 | TeamTNT | TeamTNT has sent locally staged files with collected credentials to C2 servers using cURL. [11] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1057 | Data Loss Prevention | Data loss prevention can detect and block sensitive data being uploaded via web browsers. |
| M1037 | Filter Network Traffic | Enforce proxies and use dedicated servers for services such as DNS and only allow those systems to communicate over respective ports/protocols, instead of all systems within a network. Cloud service providers support IP-based restrictions when accessing cloud resources. Consider using IP allowlisting along with user account management to ensure that data access is restricted not only to valid users but only from expected IP ranges to mitigate the use of stolen credentials to access data. |
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. |
| M1030 | Network Segmentation | Follow best practices for network firewall configurations to allow only necessary ports and traffic to enter and exit the network. [12] |
| M1022 | Restrict File and Directory Permissions | Use access control lists on cloud storage systems and objects. |
| M1018 | User Account Management | Configure user permissions groups and roles for access to cloud storage. [13] Implement strict Identity and Access Management (IAM) controls to prevent access to storage solutions except for the applications, users, and services that require access. [14] Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary. [15] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0131 | Behavioral Detection Strategy for Exfiltration Over Alternative Protocol | AN0367 | Detects unusual outbound file transfer behavior using protocols like FTP, SMB, SMTP, or DNS, involving non-standard processes, off-hour activity, or uncommonly high volume. |
| AN0368 | Detects file exfiltration using tools like curl, scp, or custom binaries over protocols such as FTP, HTTP/S, or DNS tunneling, especially outside baseline user behavior. |  |  |
| AN0369 | Detects non-native file transfer via curl, Python scripts, or AppleScript using uncommon protocols like FTP, SMTP, or DNS exfiltration through mDNSResponder abuse. |  |  |
| AN0370 | Detects access to cloud APIs or CLI tools to move or sync files from sensitive buckets to external endpoints using protocols like HTTPS or S3 APIs. |  |  |
| AN0371 | Detects outbound traffic from hostd/vpxa or guest VM interfaces using unauthorized protocols such as FTP, HTTP POST bursts, or long-lived DNS tunnels. |  |  |

---

## References

- [Grunzweig, J. and Falcone, R.. (2016, October 4). OilRig Malware Campaign Updates Toolset and Expands Targets. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/)
- [Phil Stokes. (2021, February 16). 20 Common Tools & Techniques Used by macOS Threat Actors & Malware. Retrieved August 23, 2021.](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
- [Dr. Nestori Syynimaa. (2018, October 25). AADInternals. Retrieved February 18, 2022.](https://o365blog.com/aadinternals)
- [Salem, E. (2020, November 17). CHAES: Novel Malware Targeting Latin American E-Commerce. Retrieved June 30, 2021.](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
- [Kremez, V. (2019, September 19). FIN6 “FrameworkPOS”: Point-of-Sale Malware Analysis & Internals. Retrieved September 8, 2020.](https://labs.sentinelone.com/fin6-frameworkpos-point-of-sale-malware-analysis-internals-2/)
- [Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
- [M.Leveille, M., Sanmillan, I. (2021, January). A WILD KOBALOS APPEARS Tricksy Linux malware goes after HPCs. Retrieved August 24, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
- [CISA. (2023, December 18). #StopRansomware: Play Ransomware AA23-352A. Retrieved September 24, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)
- [Trend Micro Research. (2023, July 21). Ransomware Spotlight: Play. Retrieved September 24, 2024.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
- [Mercer, W, et al. (2020, April 16). PoetRAT: Python RAT uses COVID-19 lures to target Azerbaijan public and private sectors. Retrieved April 27, 2020.](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
- [Darin Smith. (2022, April 21). TeamTNT targeting AWS, Alibaba. Retrieved August 4, 2022.](https://blog.talosintelligence.com/teamtnt-targeting-aws-alibaba-2/)
- [Microsoft. (2004, February 6). Perimeter Firewall Design. Retrieved April 25, 2016.](https://technet.microsoft.com/en-us/library/cc700828.aspx)
- [Amlekar, M., Brooks, C., Claman, L., et. al.. (2019, March 20). Azure Storage security guide. Retrieved October 4, 2019.](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)
- [Amazon. (2019, May 17). How can I secure the files in my Amazon S3 bucket?. Retrieved October 4, 2019.](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)
- [Amazon. (n.d.). Temporary Security Credentials. Retrieved October 18, 2019.](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

---

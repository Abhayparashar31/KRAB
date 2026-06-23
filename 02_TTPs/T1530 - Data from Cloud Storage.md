# Data from Cloud Storage

## Description

Adversaries may access data from cloud storage.

Many IaaS providers offer solutions for online data object storage such as Amazon S3, Azure Storage, and Google Cloud Storage. Similarly, SaaS enterprise platforms such as Office 365 and Google Workspace provide cloud-based document storage to users through services such as OneDrive and Google Drive, while SaaS application providers such as Slack, Confluence, Salesforce, and Dropbox may provide cloud storage solutions as a peripheral or primary use case of their platform.

In some cases, as with IaaS-based cloud storage, there exists no overarching application (such as SQL or Elasticsearch) with which to interact with the stored objects: instead, data from these solutions is retrieved directly though the Cloud API . In SaaS applications, adversaries may be able to collect this data directly from APIs or backend cloud storage objects, rather than through their front-end application or interface (i.e., Data from Information Repositories ).

Adversaries may collect sensitive data from these cloud storage solutions. Providers typically offer security guides to help end users configure systems, though misconfigurations are a common problem. [1] [2] [3] There have been numerous incidents where cloud storage has been improperly secured, typically by unintentionally allowing public access to unauthenticated users, overly-broad access by all users, or even access for any anonymous person outside the control of the Identity Access Management system without even needing basic user permissions.

This open access may expose various types of sensitive data, such as credit cards, personally identifiable information, or medical records. [4] [5] [6] [7]

Adversaries may also obtain then abuse leaked credentials from source repositories, logs, or other means as a way to gain access to cloud storage objects.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries leveraged stolen credentials within cloud services to download targeted data from SharePoint, and Teams. [8] |
| S0677 | AADInternals | AADInternals can collect files from a user’s OneDrive. [9] |
| G1044 | APT42 | APT42 has collected data from Microsoft 365 environments. [10] [11] |
| C0027 | C0027 | During C0027 , Scattered Spider accessed victim OneDrive environments to search for VPN and MFA enrollment information, help desk instructions, and new hire guides. [12] |
| G0117 | Fox Kitten | Fox Kitten has obtained files from the victim's cloud storage instances. [13] |
| G0125 | HAFNIUM | HAFNIUM has exfitrated data from OneDrive. [14] |
| S1091 | Pacu | Pacu can enumerate and download files stored in AWS storage services, such as S3 buckets. [15] |
| S0683 | Peirates | Peirates can dump the contents of AWS S3 buckets. It can also retrieve service account tokens from kOps buckets in Google Cloud Storage or S3. [16] |
| G1015 | Scattered Spider | Scattered Spider enumerates data stored in cloud resources for collection and exfiltration purposes. [17] |
| G1053 | Storm-0501 | Storm-0501 had modified Azure Storage account resources through the Microsoft.Storage/storageAccounts/write operation to expose non-remotely accessible accounts for data exfiltration. [18] |
| S9009 | TruffleHog | TruffleHog has the ability to scan cloud storage services for credentials to include Amazon (AWS) S3 and Google Cloud Storage. [19] [20] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Frequently check permissions on cloud storage to ensure proper permissions are set to deny open or unprivileged access to resources. [1] |
| M1041 | Encrypt Sensitive Information | Encrypt data stored at rest in cloud storage. [1] [2] Managed encryption keys can be rotated by most providers. At a minimum, ensure an incident response plan to storage breach includes rotating the keys and test for impact on client applications. [21] |
| M1037 | Filter Network Traffic | Cloud service providers support IP-based restrictions when accessing cloud resources. Consider using IP allowlisting along with user account management to ensure that data access is restricted not only to valid users but only from expected IP ranges to mitigate the use of stolen credentials to access data. |
| M1032 | Multi-factor Authentication | Consider using multi-factor authentication to restrict access to resources and cloud storage APIs. [1] |
| M1022 | Restrict File and Directory Permissions | Use access control lists on storage systems and objects. |
| M1018 | User Account Management | Configure user permissions groups and roles for access to cloud storage. [2] Implement strict Identity and Access Management (IAM) controls to prevent access to storage solutions except for the applications, users, and services that require access. [1] Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary. [22] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0484 | Multi-Platform Cloud Storage Exfiltration Behavior Chain | AN1328 | Spike in object access from new IAM user or role followed by data exfiltration to external IPs |
| AN1329 | OAuth token granted to external app followed by download of high-volume files in OneDrive/Google Drive |  |  |
| AN1330 | Internal user account accesses shared links outside org followed by mass file download |  |  |

---

## References

- [Amazon. (2019, May 17). How can I secure the files in my Amazon S3 bucket?. Retrieved October 4, 2019.](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)
- [Amlekar, M., Brooks, C., Claman, L., et. al.. (2019, March 20). Azure Storage security guide. Retrieved October 4, 2019.](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)
- [Google. (2019, September 16). Best practices for Cloud Storage. Retrieved October 4, 2019.](https://cloud.google.com/storage/docs/best-practices)
- [Trend Micro. (2017, November 6). A Misconfigured Amazon S3 Exposed Almost 50 Thousand PII in Australia. Retrieved October 4, 2019.](https://www.trendmicro.com/vinfo/us/security/news/virtualization-and-cloud/a-misconfigured-amazon-s3-exposed-almost-50-thousand-pii-in-australia)
- [Barrett, B.. (2019, July 11). Hack Brief: A Card-Skimming Hacker Group Hit 17K Domains—and Counting. Retrieved October 4, 2019.](https://www.wired.com/story/magecart-amazon-cloud-hacks/)
- [HIPAA Journal. (2017, October 11). 47GB of Medical Records and Test Results Found in Unsecured Amazon S3 Bucket. Retrieved October 4, 2019.](https://www.hipaajournal.com/47gb-medical-records-unsecured-amazon-s3-bucket/)
- [Justin Schoenfeld, Aaron Didier. (2021, May 4). Transferring leverage in a ransomware attack. Retrieved July 14, 2022.](https://redcanary.com/blog/rclone-mega-extortion/)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Dr. Nestori Syynimaa. (2018, October 25). AADInternals. Retrieved February 1, 2022.](https://o365blog.com/aadinternals/)
- [Rozmann, O., et al. (2024, May 1). Uncharmed: Untangling Iran's APT42 Operations. Retrieved October 9, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)
- [Mandiant. (n.d.). APT42: Crooked Charms, Cons and Compromises. Retrieved October 9, 2024.](https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf)
- [Parisi, T. (2022, December 2). Not a SIMulation: CrowdStrike Investigations Reveal Intrusion Campaign Targeting Telco and BPO Companies. Retrieved June 30, 2023.](https://www.crowdstrike.com/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/)
- [CISA. (2020, September 15). Iran-Based Threat Actor Exploits VPN Vulnerabilities. Retrieved December 21, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)
- [Microsoft Threat Intelligence . (2025, March 5). Silk Typhoon targeting IT supply chain. Retrieved March 20, 2025.](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/)
- [Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.](https://github.com/RhinoSecurityLabs/pacu)
- [InGuardians. (2022, January 5). Peirates GitHub. Retrieved February 8, 2022.](https://github.com/inguardians/peirates)
- [CISA. (2023, November 16). Cybersecurity Advisory: Scattered Spider (AA23-320A). Retrieved March 18, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)
- [Microsoft Threat Intelligence. (2025, August 27). Storm-0501’s evolving techniques lead to cloud-based ransomware. Retrieved October 19, 2025.](https://www.microsoft.com/en-us/security/blog/2025/08/27/storm-0501s-evolving-techniques-lead-to-cloud-based-ransomware/)
- [Chris Traynor. (2024, January 18). Rooting For Secrets with TruffleHog. Retrieved April 15, 2026.](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)
- [Trufflesecurity. (2026, April 8). TruffleHog Enterprise. Retrieved April 15, 2026.](https://github.com/trufflesecurity/trufflehog)
- [Google. (n.d.). Key rotation. Retrieved October 18, 2019.](https://cloud.google.com/kms/docs/key-rotation)
- [Amazon. (n.d.). Temporary Security Credentials. Retrieved October 18, 2019.](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

---

# Transfer Data to Cloud Account

## Description

Adversaries may exfiltrate data by transferring the data, including through sharing/syncing and creating backups of cloud environments, to another cloud account they control on the same service.

A defender who is monitoring for large transfers to outside the cloud environment through normal file transfers or over command and control channels may not be watching for data transfers to another account within the same cloud provider. Such transfers may utilize existing cloud provider APIs and the internal address space of the cloud provider to blend into normal traffic or avoid data transfers over external network interfaces. [1]

Adversaries may also use cloud-native mechanisms to share victim data with adversary-controlled cloud accounts, such as creating anonymous file sharing links or, in Azure, a shared access signature (SAS) URI. [2]

Incidents have been observed where adversaries have created backups of cloud instances and transferred them to separate accounts. [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1032 | INC Ransom | INC Ransom has used Megasync to exfiltrate data to the cloud. [4] |
| G1039 | RedCurl | RedCurl has used cloud storage to exfiltrate data, in particular the megatools utilities were used to exfiltrate data to Mega, a file storage service. [5] [6] |
| G1053 | Storm-0501 | Storm-0501 has copied data from the victims environment to their own infrastructure leveraging AzCopy CLI. [7] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1057 | Data Loss Prevention | Data loss prevention can prevent and block sensitive data from being shared with individuals outside an organization. [8] [9] |
| M1037 | Filter Network Traffic | Implement network-based filtering restrictions to prohibit data transfers to untrusted VPCs. |
| M1054 | Software Configuration | Configure appropriate data sharing restrictions in cloud services. For example, external sharing in Microsoft SharePoint and Google Drive can be turned off altogether, blocked for certain domains, or restricted to certain users. [10] [11] |
| M1018 | User Account Management | Limit user account and IAM policies to the least privileges required. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0573 | Cross-Platform Detection of Data Transfer to Cloud Account | AN1580 | Detects snapshot sharing, backup exports, or data object transfers from victim-owned cloud accounts to other cloud identities within the same provider (e.g., AWS, Azure) using snapshot sharing, S3 bucket policy updates, or SAS URI generation. |
| AN1581 | Detects user activity that shares or syncs files with external domains via link generation, OneDrive external sharing, or file transfer actions involving non-whitelisted partner tenants. |  |  |
| AN1582 | Detects use of built-in SaaS sharing mechanisms to transfer ownership or share access of critical data to external tenants or untrusted users through API calls or link generation features. |  |  |

---

## References

- [Clint Gibler and Scott Piper. (2021, January 4). Lesser Known Techniques for Attacking AWS Environments. Retrieved March 4, 2024.](https://tldrsec.com/p/blog-lesser-known-aws-attacks)
- [Microsoft. (2023, June 7). Grant limited access to Azure Storage resources using shared access signatures (SAS). Retrieved March 4, 2024.](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)
- [Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved November 17, 2024.](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)
- [Counter Threat Unit Research Team. (2024, April 15). GOLD IONIC DEPLOYS INC RANSOMWARE. Retrieved June 5, 2024.](https://www.secureworks.com/blog/gold-ionic-deploys-inc-ransomware)
- [Group-IB. (2020, August). RedCurl: The Pentest You Didn’t Know About. Retrieved August 9, 2024.](https://www.group-ib.com/resources/research-hub/red-curl/)
- [Group-IB. (2021, November). RedCurl: The Awakening. Retrieved August 14, 2024.](https://www.group-ib.com/resources/research-hub/red-curl-2/)
- [Microsoft Threat Intelligence. (2025, August 27). Storm-0501’s evolving techniques lead to cloud-based ransomware. Retrieved October 19, 2025.](https://www.microsoft.com/en-us/security/blog/2025/08/27/storm-0501s-evolving-techniques-lead-to-cloud-based-ransomware/)
- [Microsoft. (2024, January 9). Learn about data loss prevention. Retrieved March 4, 2024.](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)
- [Google. (n.d.). Use Workspace DLP to prevent data loss. Retrieved March 4, 2024.](https://support.google.com/a/answer/9646351)
- [Google. (n.d.). Manage external sharing for your organization. Retrieved March 4, 2024.](https://support.google.com/a/answer/60781)
- [Microsoft. (2023, October 11). Manage sharing settings for SharePoint and OneDrive in Microsoft 365. Retrieved March 4, 2024.](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off)

---

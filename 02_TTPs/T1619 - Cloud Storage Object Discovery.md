# Cloud Storage Object Discovery

## Description

Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage. Similar to File and Directory Discovery on a local host, after identifying available storage services (i.e. Cloud Infrastructure Discovery ) adversaries may access the contents/objects stored in cloud infrastructure.

Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2 in AWS [1] and List Blobs in Azure [2] .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1091 | Pacu | Pacu can enumerate AWS storage services, such as S3 buckets and Elastic Block Store volumes. [3] |
| S0683 | Peirates | Peirates can list AWS S3 buckets. [4] |
| S9009 | TruffleHog | TruffleHog can enumerate cloud storage environments including Amazon Web Service (AWS) S3 buckets and Google Cloud Storage buckets. [5] [6] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1018 | User Account Management | Restrict granting of permissions related to listing objects in cloud storage to necessary accounts. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0578 | Detection Strategy for Cloud Storage Object Discovery | AN1594 | Detection of suspicious enumeration of cloud storage objects via API calls such as AWS S3 ListObjectsV2, Azure List Blobs, or GCP ListObjects. Correlate access with account role, user context, and prior authentication activity to identify anomalous usage patterns (e.g., unusual account, unexpected regions, or large-scale enumeration in short time windows). |

---

## References

- [Amazon - ListObjectsV2. Retrieved October 4, 2021.](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)
- [Microsoft - List Blobs. (n.d.). Retrieved October 4, 2021.](https://docs.microsoft.com/en-us/rest/api/storageservices/list-blobs)
- [Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.](https://github.com/RhinoSecurityLabs/pacu)
- [InGuardians. (2022, January 5). Peirates GitHub. Retrieved February 8, 2022.](https://github.com/inguardians/peirates)
- [Chris Traynor. (2024, January 18). Rooting For Secrets with TruffleHog. Retrieved April 15, 2026.](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)
- [Trufflesecurity. (2026, April 8). TruffleHog Enterprise. Retrieved April 15, 2026.](https://github.com/trufflesecurity/trufflehog)

---

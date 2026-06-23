# Defacement

## Description

Adversaries may modify visual content available internally or externally to an enterprise network, thus affecting the integrity of the original content. Reasons for Defacement include delivering messaging, intimidation, or claiming (possibly false) credit for an intrusion. Disturbing or offensive images may be used as a part of Defacement in order to cause user discomfort, or to pressure compliance with accompanying messages.

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1053 | Data Backup | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data. [1] Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0238 | Defacement via File and Web Content Modification Across Platforms | AN0662 | Adversary modifies website or application-hosted content via unauthorized file changes or script injections, often by exploiting web servers or CMS access. |
| AN0663 | Adversary gains shell access or uploads a malicious script to deface hosted web content in Nginx, Apache, or other services. |  |  |
| AN0664 | Adversary modifies internal or external site content through manipulated application bundles, hosted content, or web server configs. |  |  |
| AN0665 | Adversary defaces internal VM-hosted portals or web UIs by modifying static content on datastore-mounted paths. |  |  |
| AN0666 | Adversary uses compromised instance credentials or web application access to deface content hosted in S3 buckets, Azure Blob Storage, or GCP Buckets. |  |  |

---

## References

- [Ready.gov. (n.d.). IT Disaster Recovery Plan. Retrieved March 15, 2019.](https://www.ready.gov/business/implementation/IT)

---

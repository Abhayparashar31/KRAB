# Cloud Infrastructure Discovery

## Description

An adversary may attempt to discover infrastructure and resources that are available within an infrastructure-as-a-service (IaaS) environment. This includes compute service resources such as instances, virtual machines, and snapshots as well as resources of other services including the storage and database services.

Cloud providers offer methods such as APIs and commands issued through CLIs to serve information about infrastructure. For example, AWS provides a DescribeInstances API within the Amazon EC2 API that can return information about one or more instances within an account, the ListBuckets API that returns a list of all buckets owned by the authenticated sender of the request, the HeadBucket API to determine a bucket’s existence along with access permissions of the request sender, or the GetPublicAccessBlock API to retrieve access block configuration for a bucket. [1] [2] [3] [4] Similarly, GCP's Cloud SDK CLI provides the gcloud compute instances list command to list all Google Compute Engine instances in a project [5] , and Azure's CLI command az vm list lists details of virtual machines. [6] In addition to API commands, adversaries can utilize open source tools to discover cloud storage infrastructure through Wordlist Scanning . [7]

An adversary may enumerate resources using a compromised user's access keys to determine which are available to that user. [8] The discovery of these available resources may help adversaries determine their next steps in the Cloud environment, such as establishing Persistence. [9] An adversary may also use this information to change the configuration to make the bucket publicly accessible, allowing data to be accessed without authentication. Adversaries have also may use infrastructure discovery APIs such as DescribeDBInstances to determine size, owner, permissions, and network ACLs of database resources. [10] Adversaries can use this information to determine the potential value of databases and discover the requirements to access them. Unlike in Cloud Service Discovery , this technique focuses on the discovery of components of the provided services rather than the services themselves.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1091 | Pacu | Pacu can enumerate AWS infrastructure, such as EC2 instances. [11] |
| G1015 | Scattered Spider | Scattered Spider enumerates cloud environments including Amazon Web Services (AWS) S3 buckets to identify server and backup management infrastructure, resource access, databases and storage containers . [12] [13] [14] |
| G1053 | Storm-0501 | Storm-0501 has enumerated compromised cloud environments to identify critical assets, data stores, and back resources. [15] |
| S9009 | TruffleHog | TruffleHog can enumerate AWS Infrastructure to include EC2 instances. [16] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1018 | User Account Management | Limit permissions to discover cloud infrastructure in accordance with least privilege. Organizations should limit the number of users within the organization with an IAM role that has administrative privileges, strive to reduce all permanent privileged role assignments, and conduct periodic entitlement reviews on IAM users, roles and policies. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0169 | Detection Strategy for Cloud Infrastructure Discovery | AN0481 | Defenders should monitor for suspicious enumeration of cloud infrastructure components via APIs or CLI tools. Observable behaviors include repeated listing or description operations for compute instances, snapshots, storage buckets, and volumes. From a defender’s perspective, risky activity is often identified by new or untrusted identities making discovery calls (e.g., DescribeInstances, ListBuckets, az vm list, gcloud compute instances list), enumeration from unusual geolocations or IPs, or rapid multi-service discovery in sequence. Correlating discovery API usage with later snapshot creation or instance modification provides further context of adversary behavior. |

---

## References

- [Amazon. (n.d.). describe-instance-information. Retrieved March 3, 2020.](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-instance-information.html)
- [Amazon. (n.d.). DescribeInstances. Retrieved May 26, 2020.](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html)
- [Amazon Web Services. (n.d.). Retrieved May 28, 2021.](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html)
- [Amazon Web Services. (n.d.). AWS HeadBucket. Retrieved February 14, 2022.](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html)
- [Google. (n.d.). gcloud compute instances list. Retrieved May 26, 2020.](https://cloud.google.com/sdk/gcloud/reference/compute/instances/list)
- [Microsoft. (n.d.). az ad user. Retrieved October 6, 2019.](https://docs.microsoft.com/en-us/cli/azure/ad/user?view=azure-cli-latest)
- [Vasilios Hioureas. (2019, September 13). Hacking with AWS: incorporating leaky buckets into your OSINT workflow. Retrieved February 14, 2022.](https://blog.malwarebytes.com/researchers-corner/2019/09/hacking-with-aws-incorporating-leaky-buckets-osint-workflow/)
- [A. Randazzo, B. Manahan and S. Lipton. (2020, April 28). Finding Evil in AWS. Retrieved June 25, 2020.](https://expel.io/blog/finding-evil-in-aws/)
- [Mandiant. (2020, February). M-Trends 2020. Retrieved November 17, 2024.](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf)
- [Amazon Web Services. (n.d.). Retrieved May 28, 2021.](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html)
- [Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.](https://github.com/RhinoSecurityLabs/pacu)
- [Microsoft. (2023, October 25). Octo Tempest crosses boundaries to facilitate extortion, encryption, and destruction. Retrieved March 18, 2024.](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/)
- [Mandiant Incident Response. (2025, May 6). Defending Against UNC3944: Cybercrime Hardening Guidance from the Frontlines. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)
- [Counter Adversary Operations. (2025, July 2). CrowdStrike Services Observes SCATTERED SPIDER Escalate Attacks Across Industries. Retrieved October 13, 2025.](https://www.crowdstrike.com/en-us/blog/crowdstrike-services-observes-scattered-spider-escalate-attacks/)
- [Microsoft Threat Intelligence. (2025, August 27). Storm-0501’s evolving techniques lead to cloud-based ransomware. Retrieved October 19, 2025.](https://www.microsoft.com/en-us/security/blog/2025/08/27/storm-0501s-evolving-techniques-lead-to-cloud-based-ransomware/)
- [Trufflesecurity. (2026, April 8). TruffleHog Enterprise. Retrieved April 15, 2026.](https://github.com/trufflesecurity/trufflehog)

---

# Cloud Service Discovery

## Description

An adversary may attempt to enumerate the cloud services running on a system after gaining access. These methods can differ from platform-as-a-service (PaaS), to infrastructure-as-a-service (IaaS), or software-as-a-service (SaaS). Many services exist throughout the various cloud providers and can include Continuous Integration and Continuous Delivery (CI/CD), Lambda Functions, Entra ID, etc. They may also include security services, such as AWS GuardDuty and Microsoft Defender for Cloud, and logging services, such as AWS CloudTrail and Google Cloud Audit Logs.

Adversaries may attempt to discover information about the services enabled throughout the environment. Azure tools and APIs, such as the Microsoft Graph API and Azure Resource Manager API, can enumerate resources and services, including applications, management groups, resources and policy definitions, and their relationships that are accessible by an identity. [1] [2]

For example, Stormspotter is an open source tool for enumerating and constructing a graph for Azure resources and services, and Pacu is an open source AWS exploitation framework that supports several methods for discovering cloud services. [3] [4]

Adversaries may use the information gained to shape follow-on behaviors, such as targeting data or credentials from enumerated services or evading identified defenses through Disable or Modify Tools or Disable or Modify Cloud Log .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0677 | AADInternals | AADInternals can enumerate information about a variety of cloud services, such as Office 365 and Sharepoint instances or OpenID Configurations. [5] |
| S1091 | Pacu | Pacu can enumerate AWS services, such as CloudTrail and CloudWatch. [4] |
| S0684 | ROADTools | ROADTools can enumerate Azure AD applications and service principals. [6] |
| G1053 | Storm-0501 | Storm-0501 has discovered the victim environment’s protections to include Azure policies, resource locks, and Azure Storage immutability policies. [7] |
| S9009 | TruffleHog | TruffleHog has the ability to scan code repositories and CI/CD platforms. [8] [9] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0402 | Detection Strategy for Cloud Service Discovery | AN1127 | Unusual enumeration of services and resources through cloud APIs such as AWS CLI describe-* , Azure Resource Manager queries, or GCP project listings. Defender perspective includes anomalous API calls, unexpected volume of service enumeration, and correlation of discovery with recently compromised sessions. |
| AN1128 | Enumeration of directories, applications, or service principals through APIs such as Microsoft Graph or Okta API. Defender perspective includes unexpected listing of users, roles, applications, and abnormal access to identity management endpoints. |  |  |
| AN1129 | Discovery of SaaS services connected to productivity platforms (e.g., Microsoft 365, Google Workspace). Defender perspective includes unexpected enumeration of enabled services, API integrations, or OAuth applications tied to user accounts. |  |  |
| AN1130 | Discovery of connected SaaS applications, APIs, or configurations within platforms like Salesforce, Slack, or Zoom. Defender perspective includes enumeration of available integrations, abnormal querying of service metadata, and follow-on attempts to exploit or persist via discovered services. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0402 | Detection Strategy for Cloud Service Discovery | AN1127 | Unusual enumeration of services and resources through cloud APIs such as AWS CLI describe-* , Azure Resource Manager queries, or GCP project listings. Defender perspective includes anomalous API calls, unexpected volume of service enumeration, and correlation of discovery with recently compromised sessions. |
| AN1128 | Enumeration of directories, applications, or service principals through APIs such as Microsoft Graph or Okta API. Defender perspective includes unexpected listing of users, roles, applications, and abnormal access to identity management endpoints. |  |  |
| AN1129 | Discovery of SaaS services connected to productivity platforms (e.g., Microsoft 365, Google Workspace). Defender perspective includes unexpected enumeration of enabled services, API integrations, or OAuth applications tied to user accounts. |  |  |
| AN1130 | Discovery of connected SaaS applications, APIs, or configurations within platforms like Salesforce, Slack, or Zoom. Defender perspective includes enumeration of available integrations, abnormal querying of service metadata, and follow-on attempts to exploit or persist via discovered services. |  |  |

---

## References

- [Microsoft. (2019, May 20). Azure Resource Manager. Retrieved June 17, 2020.](https://docs.microsoft.com/en-us/rest/api/resources/)
- [Microsoft. (2016, March 26). Operations overview | Graph API concepts. Retrieved June 18, 2020.](https://docs.microsoft.com/en-us/previous-versions/azure/ad/graph/howto/azure-ad-graph-api-operations-overview)
- [Microsoft. (2020). Azure Stormspotter GitHub. Retrieved June 17, 2020.](https://github.com/Azure/Stormspotter)
- [Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.](https://github.com/RhinoSecurityLabs/pacu)
- [Dr. Nestori Syynimaa. (2018, October 25). AADInternals. Retrieved February 18, 2022.](https://o365blog.com/aadinternals)
- [Dirk-jan Mollema. (2020, April 16). Introducing ROADtools - The Azure AD exploration framework. Retrieved January 31, 2022.](https://dirkjanm.io/introducing-roadtools-and-roadrecon-azure-ad-exploration-framework/)
- [Microsoft Threat Intelligence. (2025, August 27). Storm-0501’s evolving techniques lead to cloud-based ransomware. Retrieved October 19, 2025.](https://www.microsoft.com/en-us/security/blog/2025/08/27/storm-0501s-evolving-techniques-lead-to-cloud-based-ransomware/)
- [Chris Traynor. (2024, January 18). Rooting For Secrets with TruffleHog. Retrieved April 15, 2026.](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)
- [Trufflesecurity. (2026, April 8). TruffleHog Enterprise. Retrieved April 15, 2026.](https://github.com/trufflesecurity/trufflehog)

---

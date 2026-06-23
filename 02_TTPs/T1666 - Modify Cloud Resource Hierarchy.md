# Modify Cloud Resource Hierarchy

## Description

Adversaries may attempt to modify hierarchical structures in infrastructure-as-a-service (IaaS) environments in order to evade defenses.

IaaS environments often group resources into a hierarchy, enabling improved resource management and application of policies to relevant groups. Hierarchical structures differ among cloud providers. For example, in AWS environments, multiple accounts can be grouped under a single organization, while in Azure environments, multiple subscriptions can be grouped under a single management group. [1] [2]

Adversaries may add, delete, or otherwise modify resource groups within an IaaS hierarchy. For example, in Azure environments, an adversary who has gained access to a Global Administrator account may create new subscriptions in which to deploy resources. They may also engage in subscription hijacking by transferring an existing pay-as-you-go subscription from a victim tenant to an adversary-controlled tenant. This will allow the adversary to use the victim’s compute resources without generating logs on the victim tenant. [3] [4]

In AWS environments, adversaries with appropriate permissions in a given account may call the LeaveOrganization API, causing the account to be severed from the AWS Organization to which it was tied and removing any Service Control Policies, guardrails, or restrictions imposed upon it by its former Organization. Alternatively, adversaries may call the CreateAccount API in order to create a new account within an AWS Organization. This account will use the same payment methods registered to the payment account but may not be subject to existing detections or Service Control Policies. [5]

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Periodically audit resource groups in the cloud management console to ensure that only expected items exist, especially close to the top of the hierarchy (e.g., AWS accounts and Azure subscriptions). Typically, top-level accounts (such as the AWS management account) should not contain any workloads or resources. [6] |
| M1054 | Software Configuration | In Azure environments, consider setting a policy to block subscription transfers. [7] In AWS environments, consider using Service Control Policies to prevent the use of the LeaveOrganization API call. [8] |
| M1018 | User Account Management | Limit permissions to add, delete, or modify resource groups to only those required. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0155 | Detection Strategy for Modify Cloud Resource Hierarchy | AN0442 | Monitor for unauthorized or unusual modifications to cloud resource hierarchies such as AWS Organizations or Azure Management Groups. Defenders may observe anomalous calls to APIs like LeaveOrganization , CreateAccount , MoveAccount , or Azure subscription transfers. Correlate account activity with administrative role assignments, tenant transfers, or new subscription creation that deviates from organizational baselines. Multi-event correlation should track role elevation followed by hierarchy modifications within a short time window. |

---

## References

- [AWS. (n.d.). Terminology and concepts for AWS Organizations. Retrieved September 25, 2024.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html)
- [Microsoft Azure. (2024, May 31). Organize your Azure resources effectively. Retrieved September 25, 2024.](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-setup-guide/organize-resources)
- [Microsoft Threat Intelligence. (2023, September 14). Peach Sandstorm password spray campaigns enable intelligence collection at high-value targets. Retrieved September 18, 2023.](https://www.microsoft.com/en-us/security/blog/2023/09/14/peach-sandstorm-password-spray-campaigns-enable-intelligence-collection-at-high-value-targets/)
- [Dor Edry. (2022, August 24). Hunt for compromised Azure subscriptions using Microsoft Defender for Cloud Apps. Retrieved September 5, 2023.](https://techcommunity.microsoft.com/t5/microsoft-365-defender-blog/hunt-for-compromised-azure-subscriptions-using-microsoft/ba-p/3607121)
- [AWS re Inforce. (2024, June). Retrieved April 15, 2026.](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/events/approved/reinforce-2025/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)
- [AWS. (n.d.). Best practices for the management account. Retrieved October 16, 2024.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)
- [Microsoft Azure. (2024, March 21). Manage Azure subscription policies. Retrieved September 25, 2024.](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-azure-subscription-policy)
- [Ben Fletcher and Steve de Vera. (2024, June). New tactics and techniques for proactive threat detection. Retrieved September 25, 2024.](https://reinforce.awsevents.com/content/dam/reinforce/2024/slides/TDR432_New-tactics-and-techniques-for-proactive-threat-detection.pdf)

---

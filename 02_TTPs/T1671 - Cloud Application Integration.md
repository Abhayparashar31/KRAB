# Cloud Application Integration

## Description

Adversaries may achieve persistence by leveraging OAuth application integrations in a software-as-a-service environment. Adversaries may create a custom application, add a legitimate application into the environment, or even co-opt an existing integration to achieve malicious ends. [1] [2]

OAuth is an open standard that allows users to authorize applications to access their information on their behalf. In a SaaS environment such as Microsoft 365 or Google Workspace, users may integrate applications to improve their workflow and achieve tasks.

Leveraging application integrations may allow adversaries to persist in an environment – for example, by granting consent to an application from a high-privileged adversary-controlled account in order to maintain access to its data, even in the event of losing access to the account. [3] [4] [5] In some cases, integrations may remain valid even after the original consenting user account is disabled. [6] Application integrations may also allow adversaries to bypass multi-factor authentication requirements through the use of Application Access Token s. Finally, they may enable persistent Automated Exfiltration over time. [7]

Creating or adding a new application may require the adversary to create a dedicated Cloud Account for the application and assign it Additional Cloud Roles – for example, in Microsoft 365 environments, an application can only access resources via an associated service principal. [8]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0059 | Salesforce Data Exfiltration | During Salesforce Data Exfiltration , threat actors deceived victims into authorizing malicious connected apps to their organization's Salesforce portal. [9] [10] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Periodically review SaaS integrations for unapproved or potentially malicious applications. |
| M1042 | Disable or Remove Feature or Program | Do not allow users to add new application integrations into a SaaS environment. In Entra ID environments, consider enforcing the "Do not allow user consent" option. [11] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0539 | Detection Strategy for Cloud Application Integration | AN1487 | Detects suspicious OAuth application integrations within Office 365 or Google Workspace environments, such as new app registrations, unexpected consent grants, or privilege assignments. Defenders should correlate between application creation/modification events and associated user or service principal activity to identify persistence via app integrations. |
| AN1488 | Detects anomalous SaaS application integration activity across environments such as Slack, Salesforce, or other enterprise SaaS services. Focus is on unauthorized app additions, unusual permission grants, and persistence through service principal tokens. |  |  |

---

## References

- [Luke Jennings. (2022, November 29). Maintaining persistent access in a SaaS-first world. Retrieved March 20, 2025.](https://pushsecurity.com/blog/maintaining-persistent-access-in-a-saas-first-world/)
- [Push Security. (n.d.). Evil twin integrations. Retrieved March 20, 2025.](https://github.com/pushsecurity/saas-attacks/blob/main/techniques/evil_twin_integrations/description.md)
- [Lior Sonntag. (2024, February 8). Midnight Blizzard attack on Microsoft corporate environment: a detailed analysis, detections and recommendations. Retrieved March 20, 2025.](https://www.wiz.io/blog/midnight-blizzard-microsoft-breach-analysis-and-best-practices)
- [Microsoft Threat Intelligence. (2022, September 22). Malicious OAuth applications abuse cloud email services to spread spam. Retrieved March 20, 2025.](https://www.microsoft.com/en-us/security/blog/2022/09/22/malicious-OAuth-applications-used-to-compromise-email-servers-and-spread-spam/)
- [Sharon Martin. (2024, November 5). Legitimate Apps as Traitorware for Persistent Microsoft 365 Compromise. Retrieved March 20, 2025.](https://www.huntress.com/blog/legitimate-apps-as-traitorware-for-persistent-microsoft-365-compromise)
- [Luke Jennings. (2023, October 24). Slack Attack: A phisher's guide to persistence and lateral movement. Retrieved March 20, 2025.](https://pushsecurity.com/blog/phishing-slack-persistence/)
- [syne0. (2023, July 10). Malicious Azure Application PERFECTDATA SOFTWARE and Microsoft 365 Business Email Compromise. Retrieved March 20, 2025.](https://cybercorner.tech/malicious-azure-application-perfectdata-software-and-office365-business-email-compromise/)
- [Microsoft. (2023, December 15). Application and service principal objects in Microsoft Entra ID. Retrieved February 28, 2024.](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals?tabs=browser)
- [FBI Cyber Division. (2025, September 12). Cyber Criminal Groups UNC6040 and UNC6395 Compromising Salesforce Instances for Data Theft and Extortion. Retrieved October 22, 2025.](https://www.ic3.gov/CSA/2025/250912.pdf)
- [Google Threat Intelligence Group. (2025, June 4). The Cost of a Call: From Voice Phishing to Data Extortion. Retrieved October 22, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion)
- [Microsoft Entra. (2024, September 16). Configure how users consent to applications. Retrieved March 20, 2025.](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent?pivots=portal)

---

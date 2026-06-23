# Serverless Execution

## Description

Adversaries may abuse serverless computing, integration, and automation services to execute arbitrary code in cloud environments. Many cloud providers offer a variety of serverless resources, including compute engines, application integration services, and web servers.

Adversaries may abuse these resources in various ways as a means of executing arbitrary commands. For example, adversaries may use serverless functions to execute malicious code, such as crypto-mining malware (i.e. Resource Hijacking ). [1] Adversaries may also create functions that enable further compromise of the cloud environment. For example, an adversary may use the IAM:PassRole permission in AWS or the iam.serviceAccounts.actAs permission in Google Cloud to add Additional Cloud Roles to a serverless cloud function, which may then be able to perform actions the original user cannot. [2] [3]

Serverless functions can also be invoked in response to cloud events (i.e. Event Triggered Execution ), potentially enabling persistent execution over time. For example, in AWS environments, an adversary may create a Lambda function that automatically adds Additional Cloud Credentials to a user and a corresponding CloudWatch events rule that invokes that function whenever a new user is created. [4] This is also possible in many cloud-based office application suites. For example, in Microsoft 365 environments, an adversary may create a Power Automate workflow that forwards all emails a user receives or creates anonymous sharing links whenever a user is granted access to a document in SharePoint. [5] [6] In Google Workspace environments, they may instead create an Apps Script that exfiltrates a user's data when they open a file. [7] [8]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1091 | Pacu | Pacu can create malicious Lambda functions. [9] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1036 | Account Use Policies | Where possible, consider restricting access to and use of serverless functions. For examples, conditional access policies can be applied to users attempting to create workflows in Microsoft Power Automate. Google Apps Scripts that use OAuth can be limited by restricting access to high-risk OAuth scopes. [10] [11] |
| M1018 | User Account Management | Remove permissions to create, modify, or run serverless resources from users that do not explicitly require them. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0374 | Detection Strategy for Serverless Execution (T1648) | AN1053 | Correlate creation or modification of serverless functions (e.g., AWS Lambda, GCP Cloud Functions, Azure Functions) with anomalous IAM role assignments or permissions escalation events. Detect subsequent executions of newly created functions that perform unexpected actions such as spawning outbound network connections, accessing sensitive resources, or creating additional credentials. |
| AN1054 | Monitor for creation of new Power Automate flows or equivalent automation scripts that trigger on user or file events. Detect anomalous actions performed by these automations, such as email forwarding, anonymous link creation, or unexpected API calls to external endpoints. |  |  |
| AN1055 | Track creation or update of SaaS automation scripts (e.g., Google Workspace Apps Script). Detect when these scripts are bound to user events such as file opens or account modifications, and correlate with subsequent abnormal API calls that exfiltrate or modify user data. |  |  |

---

## References

- [Matt Muir. (2022, April 6). Cado Discovers Denonia: The First Malware Specifically Targeting Lambda. Retrieved May 27, 2022.](https://www.cadosecurity.com/cado-discovers-denonia-the-first-malware-specifically-targeting-lambda/)
- [Rhino Security Labs. (n.d.). AWS IAM Privilege Escalation – Methods and Mitigation. Retrieved May 27, 2022.](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
- [Spencer Gietzen. (n.d.). Privilege Escalation in Google Cloud Platform – Part 1 (IAM). Retrieved May 27, 2022.](https://rhinosecuritylabs.com/gcp/privilege-escalation-google-cloud-platform-part-1/)
- [Daniel Grzelak. (2016, July 9). Backdooring an AWS account. Retrieved May 27, 2022.](https://medium.com/daniel-grzelak/backdooring-an-aws-account-da007d36f8f9)
- [Eric Saraga. (2022, February 2). Using Power Automate for Covert Data Exfiltration in Microsoft 365. Retrieved May 27, 2022.](https://www.varonis.com/blog/power-automate-data-exfiltration)
- [Berk Veral. (2020, March 9). Real-life cybercrime stories from DART, the Microsoft Detection and Response Team. Retrieved May 27, 2022.](https://www.microsoft.com/security/blog/2020/03/09/real-life-cybercrime-stories-dart-microsoft-detection-and-response-team)
- [HackTricks Cloud. (n.d.). GWS - App Scripts. Retrieved July 1, 2024.](https://cloud.hacktricks.xyz/pentesting-cloud/workspace-security/gws-google-platforms-phishing/gws-app-scripts)
- [L'Hutereau Arnaud. (n.d.). Google Workspace Malicious App Script analysis. Retrieved October 2, 2024.](https://www.own.security/ressources/blog/google-workspace-malicious-app-script-analysis)
- [Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.](https://github.com/RhinoSecurityLabs/pacu)
- [Microsoft Developer Support. (2020, May 9). Control Access to Power Apps and Power Automate with Azure AD Conditional Access Policies. Retrieved July 1, 2024.](https://devblogs.microsoft.com/premier-developer/control-access-to-power-apps-and-power-automate-with-azure-ad-conditional-access-policies/)
- [Google Workspace. (2024, March 5). Monitor & restrict data access. Retrieved July 1, 2024.](https://developers.google.com/apps-script/guides/admin/monitor-restrict-oauth-scopes)

---

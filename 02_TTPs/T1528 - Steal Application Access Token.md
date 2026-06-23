# Steal Application Access Token

## Description

Adversaries can steal application access tokens as a means of acquiring credentials to access remote systems and resources.

Application access tokens are used to make authorized API requests on behalf of a user or service and are commonly used as a way to access resources in cloud and container-based applications and software-as-a-service (SaaS). [1] Adversaries who steal account API tokens in cloud and containerized environments may be able to access data and perform actions with the permissions of these accounts, which can lead to privilege escalation and further compromise of the environment.

For example, in Kubernetes environments, processes running inside a container may communicate with the Kubernetes API server using service account tokens. If a container is compromised, an adversary may be able to steal the container’s token and thereby gain access to Kubernetes API commands. [2]

Similarly, instances within continuous-development / continuous-integration (CI/CD) pipelines will often use API tokens to authenticate to other services for testing and deployment. [3] If these pipelines are compromised, adversaries may be able to steal these tokens and leverage their privileges.

In Azure, an adversary who compromises a resource with an attached Managed Identity, such as an Azure VM, can request short-lived tokens through the Azure Instance Metadata Service (IMDS). These tokens can then facilitate unauthorized actions or further access to other Azure services, bypassing typical credential-based authentication. [4] [5]

Token theft can also occur through social engineering, in which case user action may be required to grant access. OAuth is one commonly implemented framework that issues tokens to users for access to systems. An application desiring access to cloud-based services or protected APIs can gain entry using OAuth 2.0 through a variety of authorization protocols. An example commonly-used sequence is Microsoft's Authorization Code Grant flow. [6] [7] An OAuth access token enables a third-party application to interact with resources containing user data in the ways requested by the application without obtaining user credentials.

Adversaries can leverage OAuth authorization by constructing a malicious application designed to be granted access to resources with the target user's OAuth token. [8] [9] The adversary will need to complete registration of their application with the authorization server, for example Microsoft Identity Platform using Azure Portal, the Visual Studio IDE, the command-line interface, PowerShell, or REST API calls. [10] Then, they can send a Spearphishing Link to the target user to entice them to grant access to the application. Once the OAuth access token is granted, the application can gain potentially long-term access to features of the user account through Application Access Token . [11]

Application access tokens may function within a limited lifetime, limiting how long an adversary can utilize the stolen token. However, in some cases, adversaries can also steal application refresh tokens [12] , allowing them to obtain new access tokens without prompting the user.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0677 | AADInternals | AADInternals can steal users’ access tokens via phishing emails containing malicious links. [13] |
| G0007 | APT28 | APT28 has used several malicious applications to steal user OAuth access tokens including applications masquerading as "Google Defender" "Google Email Protection," and "Google Scanner" for Gmail users. They also targeted Yahoo users with applications masquerading as "Delivery Service" and "McAfee Email Protection". [9] |
| G0016 | APT29 | APT29 uses stolen tokens to access victim accounts, without needing a password. [14] |
| C0049 | Leviathan Australian Intrusions | Leviathan abused access to compromised appliances to collect JSON Web Tokens (JWTs), used for creating virtual desktop sessions, during Leviathan Australian Intrusions . [15] |
| S0683 | Peirates | Peirates gathers Kubernetes service account tokens using a variety of techniques. [16] |
| S9008 | Shai-Hulud | Shai-Hulud has stolen access tokens and API tokens from with CI/CD pipeline solutions and repositories. [17] [18] [19] [20] |
| S9009 | TruffleHog | TruffleHog has gathered access tokens and API tokens from CI/CD pipeline solutions and repositories. [21] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Administrators should audit all cloud and container accounts to ensure that they are necessary and that the permissions granted to them are appropriate. Additionally, administrators should perform an audit of all OAuth applications and the permissions they have been granted to access organizational data. This should be done extensively on all applications in order to establish a baseline, followed up on with periodic audits of new or updated applications. Suspicious applications should be investigated and removed. |
| M1021 | Restrict Web-Based Content | Administrators can block end-user consent to OAuth applications, disabling users from authorizing third-party apps through OAuth 2.0 and forcing administrative consent for all requests. They can also block end-user registration of applications by their users, to reduce risk. A Cloud Access Security Broker can also be used to ban applications. Azure offers a couple of enterprise policy settings in the Azure Management Portal that may help: "Users -> User settings -> App registrations: Users can register applications" can be set to "no" to prevent users from registering new applications. "Enterprise applications -> User settings -> Enterprise applications: Users can consent to apps accessing company data on their behalf" can be set to "no" to prevent users from consenting to allow third-party multi-tenant applications |
| M1018 | User Account Management | Enforce role-based access control to limit accounts to the least privileges they require. A Cloud Access Security Broker (CASB) can be used to set usage policies and manage user permissions on cloud applications to prevent access to application access tokens. In Kubernetes applications, set "automountServiceAccountToken: false" in the YAML specification of pods that do not require access to service account tokens. [22] |
| M1017 | User Training | Users need to be trained to not authorize third-party applications they don’t recognize. The user should pay particular attention to the redirect URL: if the URL is a misspelled or convoluted sequence of words related to an expected service or SaaS application, the website is likely trying to spoof a legitimate service. Users should also be cautious about the permissions they are granting to apps. For example, offline access and access to read emails should excite higher suspicions because adversaries can utilize SaaS APIs to discover credentials and other sensitive communications. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0515 | Detection Strategy for T1528 - Steal Application Access Token | AN1423 | Access and retrieval of container service account tokens followed by unauthorized API requests using those tokens to interact with the Kubernetes API server or internal services. |
| AN1424 | Token retrieval from instance metadata endpoints such as AWS IMDS or Azure IMDS, followed by API usage using the obtained token from non-standard applications. |  |  |
| AN1425 | Unusual OAuth app registration followed by user-granted OAuth tokens and subsequent high-privilege resource access via those tokens. |  |  |
| AN1426 | Use of OAuth tokens by third-party apps to access user mail, calendar, or SharePoint resources where the token was granted recently or via spearphishing. |  |  |
| AN1427 | Programmatic access to user content via stolen access tokens in platforms like Slack, GitHub, Google Workspace — especially from new IPs, apps, or excessive resource access. |  |  |

---

## References

- [Auth0. (n.d.). Why You Should Always Use Access Tokens to Secure APIs. Retrieved September 12, 2019.](https://auth0.com/blog/why-should-use-accesstokens-to-secure-an-api/)
- [Kubernetes. (2022, February 26). Configure Service Accounts for Pods. Retrieved April 1, 2022.](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)
- [Daniel Krivelevich and Omer Gil. (n.d.). Top 10 CI/CD Security Risks. Retrieved November 17, 2024.](https://web.archive.org/web/20220316130828/https://www.cidersecurity.io/top-10-cicd-security-risks/)
- [Microsoft Entra. (2025, February 27). How to use managed identities for Azure resources on an Azure VM to acquire an access token. Retrieved March 18, 2025.](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/how-to-use-vm-token)
- [Andy Robbins. (2022, June 6). Managed Identity Attack Paths, Part 1: Automation Accounts. Retrieved March 18, 2025.](https://posts.specterops.io/managed-identity-attack-paths-part-1-automation-accounts-82667d17187a?gi=6a9daedade1c)
- [Microsoft. (n.d.). Retrieved September 12, 2019.](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-protocols)
- [Microsoft. (n.d.). Microsoft identity platform and OAuth 2.0 authorization code flow. Retrieved September 12, 2019.](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow)
- [Amnesty International. (2019, August 16). Evolving Phishing Attacks Targeting Journalists and Human Rights Defenders from the Middle-East and North Africa. Retrieved October 8, 2019.](https://www.amnesty.org/en/latest/research/2019/08/evolving-phishing-attacks-targeting-journalists-and-human-rights-defenders-from-the-middle-east-and-north-africa/)
- [Hacquebord, F.. (2017, April 25). Pawn Storm Abuses Open Authentication in Advanced Social Engineering Attacks. Retrieved October 4, 2019.](https://blog.trendmicro.com/trendlabs-security-intelligence/pawn-storm-abuses-open-authentication-advanced-social-engineering-attacks)
- [Microsoft. (2019, May 8). Quickstart: Register an application with the Microsoft identity platform. Retrieved September 12, 2019.](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Microsoft. (2019, August 29). Microsoft identity platform access tokens. Retrieved September 12, 2019.](https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens)
- [Auth0 Inc.. (n.d.). Understanding Refresh Tokens. Retrieved November 17, 2024.](https://auth0.com/learn/refresh-tokens)
- [Dr. Nestori Syynimaa. (2018, October 25). AADInternals. Retrieved February 18, 2022.](https://o365blog.com/aadinternals)
- [UK National Cyber Security Center et al. (2024, February). SVR cyber actors adapt tactics for initial cloud access. Retrieved March 1, 2024.](https://www.ic3.gov/Media/News/2024/240226.pdf)
- [CISA et al. (2024, July 8). People’s Republic of China (PRC) Ministry of State Security APT40 Tradecraft in Action. Retrieved February 3, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a)
- [InGuardians. (2022, January 5). Peirates GitHub. Retrieved February 8, 2022.](https://github.com/inguardians/peirates)
- [Gianpietro Cutolo. (2025, November 26). Shai-Hulud 2.0: Aggressive, Automated, and Fast Spreading. Retrieved April 9, 2026.](https://www.netskope.com/blog/shai-hulud-2-0-aggressive-automated-one-of-fastest-spreading-npm-supply-chain-attacks-ever-observed)
- [Justin Moore. (2025, November 25). "Shai-Hulud" Worm Compromises npm Ecosystem in Supply Chain Attack (Updated November 26). Retrieved April 9, 2026.](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
- [Merav Bar, Rami McCarthy, Barak Sharoni. (2025, September 16). Shai-Hulud: Ongoing Package Supply Chain Worm Delivering Data-Stealing Malware. Retrieved April 9, 2026.](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack)
- [Socket Research Team. (2025, November 24). Shai Hulud Strikes Again (v2). Retrieved April 9, 2026.](https://socket.dev/blog/shai-hulud-strikes-again-v2)
- [Chris Traynor. (2024, January 18). Rooting For Secrets with TruffleHog. Retrieved April 15, 2026.](https://www.blackhillsinfosec.com/rooting-for-secrets-with-trufflehog/)
- [National Security Agency, Cybersecurity and Infrastructure Security Agency. (2022, March). Kubernetes Hardening Guide. Retrieved April 1, 2022.](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

---


### 🔗 KRAB Intelligence Correlation
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2026 Enterprise LMS and Canvas Data Extortion Campaign]] [related_campaign:: [[2026 Enterprise LMS and Canvas Data Extortion Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[Salesforce Massive Corporate Extortion Wave]] [related_campaign:: [[Salesforce Massive Corporate Extortion Wave]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Scattered Lapsus$ Hunters]] [related_actor:: [[Scattered Lapsus$ Hunters]]]

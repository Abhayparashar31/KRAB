# Multi-Factor Authentication Request Generation

## Description

Adversaries may attempt to bypass multi-factor authentication (MFA) mechanisms and gain access to accounts by generating MFA requests sent to users.

Adversaries in possession of credentials to Valid Accounts may be unable to complete the login process if they lack access to the 2FA or MFA mechanisms required as an additional credential and security control. To circumvent this, adversaries may abuse the automatic generation of push notifications to MFA services such as Duo Push, Microsoft Authenticator, Okta, or similar services to have the user grant access to their account. If adversaries lack credentials to victim accounts, they may also abuse automatic push notification generation when this option is configured for self-service password reset (SSPR). [1]

In some cases, adversaries may continuously repeat login attempts in order to bombard users with MFA push notifications, SMS messages, and phone calls, potentially resulting in the user finally accepting the authentication request in response to "MFA fatigue." [2] [3] [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0016 | APT29 | APT29 has used repeated MFA requests to gain access to victim accounts. [4] [5] |
| C0027 | C0027 | During C0027 , Scattered Spider attempted to gain access by continuously sending MFA messages to the victim until they accept the MFA push challenge. [6] |
| G1004 | LAPSUS$ | LAPSUS$ has spammed target users with MFA prompts in the hope that the legitimate user will grant necessary approval. [7] |
| G1015 | Scattered Spider | Scattered Spider has used multifactor authentication (MFA) fatigue by sending repeated MFA authentication requests to targets. [8] [9] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1036 | Account Use Policies | Enable account restrictions to prevent login attempts, and the subsequent 2FA/MFA service requests, from being initiated from suspicious locations or when the source of the login attempts do not match the location of the 2FA/MFA smart device. Use conditional access policies to block logins from non-compliant devices or from outside defined organization IP ranges. [10] |
| M1032 | Multi-factor Authentication | Implement more secure 2FA/MFA mechanisms in replacement of simple push or one-click 2FA/MFA options. For example, having users enter a one-time code provided by the login screen into the 2FA/MFA application or utilizing other out-of-band 2FA/MFA mechanisms (such as rotating code-based hardware tokens providing rotating codes that need an accompanying user pin) may be more secure. Furthermore, change default configurations and implement limits upon the maximum number of 2FA/MFA request prompts that can be sent to users in period of time. [3] |
| M1017 | User Training | Train users to only accept 2FA/MFA requests from login attempts they initiated, to review source location of the login attempt prompting the 2FA/MFA requests, and to report suspicious/unsolicited prompts. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0160 | Detection Strategy for Multi-Factor Authentication Request Generation (T1621) | AN0449 | Monitor for excessive or anomalous MFA push notifications or token requests, especially when login attempts originate from unusual IPs or geolocations and do not correspond to legitimate user-initiated sessions. |
| AN0450 | Detect abnormal MFA activity within cloud service provider logs, such as repeated generation of MFA challenges for the same user session or mismatched MFA device and login origin. |  |  |
| AN0451 | Detect repeated failed login events followed by MFA challenges triggered in rapid succession, especially if originating from service accounts or anomalous IP addresses. |  |  |
| AN0452 | Monitor PAM and syslog entries for unusual frequency of login attempts that trigger MFA prompts, particularly when MFA challenges do not match expected user behavior. |  |  |
| AN0453 | Detect anomalous OAuth or SSO logins that repeatedly generate MFA challenges, particularly where MFA approvals are denied or timed out by the user. |  |  |
| AN0454 | Detect user account logon attempts that trigger multiple MFA challenges through enterprise identity integrations, especially if MFA push requests are generated without successful interactive login. |  |  |

---

## References

- [Noah Corradin and Shuyang Wang. (2023, August 1). Behind The Breach: Self-Service Password Reset (SSPR) Abuse in Azure AD. Retrieved March 28, 2024.](https://www.obsidiansecurity.com/blog/behind-the-breach-self-service-password-reset-azure-ad/)
- [Catalin Cimpanu. (2021, December 9). Russian hackers bypass 2FA by annoying victims with repeated push notifications. Retrieved March 31, 2022.](https://therecord.media/russian-hackers-bypass-2fa-by-annoying-victims-with-repeated-push-notifications/)
- [Jessica Haworth. (2022, February 16). MFA fatigue attacks: Users tricked into allowing device access due to overload of push notifications. Retrieved March 31, 2022.](https://portswigger.net/daily-swig/mfa-fatigue-attacks-users-tricked-into-allowing-device-access-due-to-overload-of-push-notifications)
- [Luke Jenkins, Sarah Hawley, Parnian Najafi, Doug Bienstock. (2021, December 6). Suspected Russian Activity Targeting Government and Business Entities Around the Globe. Retrieved April 15, 2022.](https://www.mandiant.com/resources/russian-targeting-gov-business)
- [UK National Cyber Security Center et al. (2024, February). SVR cyber actors adapt tactics for initial cloud access. Retrieved March 1, 2024.](https://www.ic3.gov/Media/News/2024/240226.pdf)
- [Parisi, T. (2022, December 2). Not a SIMulation: CrowdStrike Investigations Reveal Intrusion Campaign Targeting Telco and BPO Companies. Retrieved June 30, 2023.](https://www.crowdstrike.com/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/)
- [MSTIC, DART, M365 Defender. (2022, March 24). DEV-0537 Criminal Actor Targeting Organizations for Data Exfiltration and Destruction. Retrieved May 17, 2022.](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)
- [CrowdStrike. (2023, January 10). SCATTERED SPIDER Exploits Windows Security Deficiencies with Bring-Your-Own-Vulnerable-Driver Tactic in Attempt to Bypass Endpoint Security. Retrieved July 5, 2023.](https://www.crowdstrike.com/blog/scattered-spider-attempts-to-avoid-detection-with-bring-your-own-vulnerable-driver-tactic/)
- [Check Point Team. (2025, July 7). Exposing Scattered Spider: New Indicators Highlight Growing Threat to Enterprises and Aviation. Retrieved October 13, 2025.](https://blog.checkpoint.com/research/exposing-scattered-spider-new-indicators-highlight-growing-threat-to-enterprises-and-aviation/)
- [Microsoft. (2022, December 14). Conditional Access templates. Retrieved February 21, 2023.](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[ShinyHunters]] [related_actor:: [[ShinyHunters]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025-2026 SaaS and Cloud Exploitation Wave]] [related_campaign:: [[2025-2026 SaaS and Cloud Exploitation Wave]]]

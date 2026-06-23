# Acquire Access

## Description

Adversaries may purchase or otherwise acquire an existing access to a target system or network. A variety of online services and initial access broker networks are available to sell access to previously compromised systems. [1] [2] [3] In some cases, adversary groups may form partnerships to share compromised systems with each other. [4]

Footholds to compromised systems may take a variety of forms, such as access to planted backdoors (e.g., Web Shell ) or established access via External Remote Services . In some cases, access brokers will implant compromised systems with a "load" that can be used to install additional malware for paying customers. [1]

By leveraging existing access broker networks rather than developing or obtaining their own initial access capabilities, an adversary can potentially reduce the resources required to gain a foothold on a target network and focus their efforts on later stages of compromise. Adversaries may prioritize acquiring access to systems that have been determined to lack security monitoring or that have high privileges, or systems that belong to organizations in a particular sector. [1] [2]

In some cases, purchasing access to an organization in sectors such as IT contracting, software development, or telecommunications may allow an adversary to compromise additional victims via a Trusted Relationship , Multi-Factor Authentication Interception , or even Supply Chain Compromise .

Note: while this technique is distinct from other behaviors such as Purchase Technical Data and Credentials , they may often be used in conjunction (especially where the acquired foothold requires Valid Accounts ).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1051 | Medusa Group | Medusa Group has purchased user credentials and other sensitive data from Initial Access Brokers (IABs). [5] [6] [7] [8] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0884 | Detection of Acquire Access | AN2016 | Much of this takes place outside the visibility of the target organization, making detection difficult for defenders. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access. |

---

## References

- [Microsoft. (2022, May 9). Ransomware as a service: Understanding the cybercrime gig economy and how to protect yourself. Retrieved March 10, 2023.](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)
- [CrowdStrike Intelligence Team. (2022, February 23). Access Brokers: Who Are the Targets, and What Are They Worth?. Retrieved March 10, 2023.](https://www.crowdstrike.com/blog/access-brokers-targets-and-worth/)
- [Brian Krebs. (2012, October 22). Service Sells Access to Fortune 500 Firms. Retrieved March 10, 2023.](https://krebsonsecurity.com/2012/10/service-sells-access-to-fortune-500-firms/)
- [Cybersecurity Infrastructure and Defense Agency. (2022, June 2). Karakurt Data Extortion Group. Retrieved March 10, 2023.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-152a)
- [Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
- [Check Point. (2025, April 16). The 2025 Ransomware Surge: Context for Medusa’s Rise. Retrieved October 15, 2025.](https://www.checkpoint.com/cyber-hub/threat-prevention/ransomware/medusa-ransomware-group/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Intel471. (2025, May 14). Threat hunting case study: Medusa ransomware. Retrieved October 15, 2025.](https://www.intel471.com/blog/threat-hunting-case-study-medusa-ransomware)

---

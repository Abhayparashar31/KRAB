# Social Engineering

## Description

Adversaries may use social engineering techniques to influence users to take actions that result in unauthorized access, approval of changes, disclosure of sensitive information, or execution of adversary-supplied instructions (i.e., introduction of malicious payloads or software), while minimizing technical indicators.

Adversaries may leverage trust-building methods across multiple channels (e.g., executive, vendor, or help desk scenarios, including AI-enabled voice interactions) to prompt user-authorized actions such as password resets, MFA changes, financial approvals, or the disclosure of sensitive information. Adversaries may also leverage common business communications and workflows such as email, collaboration platforms, voice communications, recruiting processes, help desk interactions, and SaaS consent mechanisms to make malicious requests appear routine and legitimate. [1] [2] [3]

Additionally, adversaries have persuaded victims to take actions through references of current events, harnessing relevant themes to the work role or the organizations mission. For example, adversaries may use scare tactics (i.e., threaten repercussions for non-compliance) or otherwise incite victims’ emotions in order to generate a sense of urgency to take action. [4] [5]

This technique may include common social engineering patterns such as Phishing and Spearphishing Voice , often supported by convincing and targeted narratives. [2] [6]

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1036 | Account Use Policies | Adds verification for helpdesk resets, approvals, and app consents commonly targeted by impersonation. [2] [3] |
| M1047 | Audit | Enables correlation of email/identity/SaaS/endpoint activity that appears legitimate. [1] [7] |
| M1017 | User Training | Reduces success of phishing/vishing/impersonation and modern "human interface" lures. [2] [8] [7] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0899 | Detect Social Engineering | AN2037 | Detects users executing commands copied from chats, tickets, or emails, including curl|bash patterns, shell script launches from temp directories, credential changes, or SSH key additions shortly after communication events. |
| AN2035 | Detects user execution of newly received content or instructions shortly after external communication, including script launches, Office child process spawning, browser-to-script execution chains, or credential prompts followed by new logon sessions. |  |  |
| AN2034 | Detects consent grants, password resets, role changes, external sharing, or token creation shortly after user interaction with messages, invites, or help desk workflows. Emphasis is placed on unusual requester relationships, new device context, or off-hours approvals. |  |  |
| AN2033 | Detects suspicious inbound communications or collaboration requests followed by rapid sensitive user actions such as file sharing changes, macro enablement, OAuth consent, credential submission, or financial workflow approvals that deviate from historical relationships or normal approval patterns. |  |  |
| AN2036 | Detects user-authorized execution of downloaded content or scripts after communication prompts, including browser downloads followed by osascript, shell, or installer execution and subsequent network activity. |  |  |

---

## References

- [Lesnewich, G. et al. (2024, April 16). From Social Engineering to DMARC Abuse: TA427’s Art of Information Gathering. Retrieved May 3, 2024.](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)
- [SentinelOne. (2025, August 19). 15 Types of Social Engineering Attacks. Retrieved April 15, 2026.](https://www.sentinelone.com/cybersecurity-101/threat-intelligence/types-of-social-engineering-attacks/)
- [David Jones. (2025, August 19). Hackers target Workday in social engineering attack. Retrieved April 15, 2026.](https://www.cybersecuritydive.com/news/hackers-target-workday-in-social-engineering-attack/758095/#:~:text=Researchers%20cite%20increasing%20evidence%20of,told%20Cybersecurity%20Dive%20via%20email.)
- [Proofpoint. (n.d.). What Is Social Engineering?. Retrieved April 15, 2026.](https://www.proofpoint.com/us/threat-reference/social-engineering)
- [SentinelOne. (2023, October 19). Social Engineering Attacks | How to Recognize and Resist The Bait. Retrieved April 15, 2026.](https://www.sentinelone.com/blog/social-engineering-attacks-how-to-recognize-and-resist-the-bait/)
- [Fortinet. (n.d.). Recent Cyber Attacks & Emerging Cybersecurity Trends. Retrieved April 15, 2026.](https://www.fortinet.com/uk/resources/cyberglossary/recent-cyber-attacks)
- [Palo Alto Networks Unit 42. (n.d.). Global Incident Response Report 2026. Retrieved April 15, 2026.](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report#:~:text=The%20Browser%20Attack%20Surface:%20Attacks%20at%20the%20Human%20Interface&text=The%20site%20used%20social-engineering,deployment%20and%20broader%20operational%20disruption)
- [Jagadeesh Chandraiah, Tonmoy Jitu, Dmitry Samosseiko, Matt Wixey. (2026, March 11). Evil evolution: ClickFix and macOS infostealers. Retrieved April 15, 2026.](https://www.sophos.com/en-us/blog/evil-evolution-clickfix-and-macos-infostealers)

---

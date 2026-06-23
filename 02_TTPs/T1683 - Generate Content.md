# Generate Content

## Description

Adversaries may create or generate content to support targeting and operations. This content may be used to establish personas, impersonate known individuals or organizations, and support Social Engineering , fraud, or influence activities. Written materials, audio, images, video, or other media may be developed and tailored to the target and objective. [1]

Content development may occur prior to or during an operation. Adversaries may develop or generate content in-house, source it through third parties, or produce it using AI-assisted tools. Adversaries may use AI to research targets, develop pretexts, and better understand the organizations and individuals they intend to target or deceive prior to generating content (i.e., Query Public AI Services ); for obtaining access to AI tools used in content generation, see Artificial Intelligence .

Content may be leveraged in support of techniques such as Phishing , Phishing for Information , Social Engineering , Financial Theft , or Establish Accounts . Generated or developed content does not include malicious code or scripts (i.e., Develop Capabilities and Artificial Intelligence ).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0062 | Anthropic AI-orchestrated Campaign | During the Anthropic AI-orchestrated Campaign , the adversary utilized Claude Code to automatically generate comprehensive documentation throughout the phases of the attack, including discovered services, harvested credentials, sensitive data, exploitation techniques, and complete attack progression. [2] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on designing defenses that are not reliant on atomic indicators. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0916 | Detection of Generate Content | AN2059 | Much of this takes place outside the visibility of the target organization, making detection difficult for defenders. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access. |

---

## References

- [Tim Mucci. (n.d.). What is AI-Generated Content?. Retrieved April 22, 2026.](https://www.ibm.com/think/insights/ai-generated-content)
- [Anthropic. (2025, November). Disrupting the first reported AI-orchestrated cyber espionage campaign. Retrieved April 20, 2026.](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)

---

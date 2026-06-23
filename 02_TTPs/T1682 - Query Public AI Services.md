# Query Public AI Services

## Description

Adversaries may query publicly accessible artificial intelligence (AI) services, such as large language models (LLMs), to support targeting and operations. In addition to searching websites or databases directly (i.e., Search Open Websites/Domains ), adversaries may use AI services to synthesize, aggregate, and analyze publicly available information at scale. This may include identifying individuals or organizations to target, researching organizational structures and personnel, identifying technologies used by target organizations, researching business relationships to develop plausible pretexts for Social Engineering approaches, identifying contact information for use in Phishing or Phishing for Information , or gathering derogatory or sensitive information about individuals that may be used for extortion or coercion. [1] [2]

Information gathered through AI services may be leveraged for other behaviors, such as establishing operational resources (i.e., Generate Content or Establish Accounts . For obtaining access to AI tools and services, see Artificial Intelligence .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1044 | APT42 | APT42 has leveraged LLMs to search for official emails to build target lists, and conduct reconnaissance on potential business partners. [2] |
| G0094 | Kimsuky | Kimsuky has used LLMs to identify think tanks, government organizations, and experts to inform targeting for spearphishing campaigns. [1] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on designing defenses that are not reliant on atomic indicators. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0919 | Detection of Query Public AI Services | AN2062 | Much of this takes place outside the visibility of the target organization, making detection difficult for defenders. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access. |

---

## References

- [Microsoft Threat Intelligence. (2024, February 14). Staying ahead of threat actors in the age of AI. Retrieved March 11, 2024.](https://www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai/)
- [Google Threat Intelligence Group . (2026, February 12). GTIG AI Threat Tracker: Distillation, Experimentation, and (Continued) Integration of AI for Adversarial Use. Retrieved March 25, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use)

---

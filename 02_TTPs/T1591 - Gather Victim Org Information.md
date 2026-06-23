# Gather Victim Org Information

## Description

Adversaries may gather information about the victim's organization that can be used during targeting. Information about an organization may include a variety of details, including the names of divisions/departments, specifics of business operations, as well as the roles and responsibilities of key employees.

Adversaries may gather this information in various ways, such as direct elicitation via Phishing for Information . Information about an organization may also be exposed to adversaries via online or other accessible data sets (ex: Social Media or Search Victim-Owned Websites ). [1] [2] Gathering this information may reveal opportunities for other forms of reconnaissance (ex: Phishing for Information or Search Open Websites/Domains ), establishing operational resources (ex: Establish Accounts or Compromise Accounts ), and/or initial access (ex: Phishing or Trusted Relationship ).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0007 | APT28 | APT28 has used large language models (LLMs) to gather information about satellite capabilities. [3] [4] |
| G0046 | FIN7 | FIN7 has compiled a list of victims by filtering companies by revenue using Zoominfo, which is a service that provides business information. [5] |
| G0094 | Kimsuky | Kimsuky has collected victim organization information including but not limited to organization hierarchy, functions, press releases, and others. [6] Kimsuky has also used large language models (LLMs) to gather information about potential targets of interest. [3] |
| G0032 | Lazarus Group | Lazarus Group has studied publicly available information about a targeted organization to tailor spearphishing efforts against specific departments and/or individuals. [7] |
| G1054 | MirrorFace | MirrorFace has placed specific content in phishing emails to target members of particular political parties. [8] |
| G1036 | Moonstone Sleet | Moonstone Sleet has gathered information on victim organizations through email and social media interaction. [9] |
| C0061 | Operation Digital Eye | During Operation Digital Eye , threat actors concealed malicious activity by using terms that aligned with the technological context of the targeted organization. [10] |
| C0022 | Operation Dream Job | For Operation Dream Job , Lazarus Group gathered victim organization information to identify specific targets. [11] |
| G1017 | Volt Typhoon | Volt Typhoon has conducted extensive reconnaissance pre-compromise to gain information about the targeted organization. [12] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0890 | Detection of Gather Victim Org Information | AN2022 | Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access. |

---

## References

- [Seals, T. (2020, October 15). Broadvoice Leak Exposes 350M Records, Personal Voicemail Transcripts. Retrieved October 20, 2020.](https://threatpost.com/broadvoice-leaks-350m-records-voicemail-transcripts/160158/)
- [U.S. SEC. (n.d.). EDGAR - Search and Access. Retrieved November 17, 2024.](https://www.sec.gov/edgar/search/)
- [Microsoft Threat Intelligence. (2024, February 14). Staying ahead of threat actors in the age of AI. Retrieved March 11, 2024.](https://www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai/)
- [OpenAI. (2024, February 14). Disrupting malicious uses of AI by state-affiliated threat actors. Retrieved September 12, 2024.](https://openai.com/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [KISA. (2021). Phishing Target Reconnaissance and Attack Resource Analysis Operation Muzabi. Retrieved March 8, 2024.](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
- [Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle. Retrieved October 27, 2021.](https://securelist.com/lazarus-threatneedle/100803/)
- [Breitenbacher, D. (2022, December 14). Unmasking MirrorFace: Operation LiberalFace targeting Japanese political entities. Retrieved April 17, 2026.](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
- [Microsoft Threat Intelligence. (2024, May 28). Moonstone Sleet emerges as new North Korean threat actor with new bag of tricks. Retrieved August 26, 2024.](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)
- [Aleksandar Milenkoski, Luigi Martire. (2024, December 10). Operation Digital Eye | Chinese APT Compromises Critical Digital Infrastructure via Visual Studio Code Tunnels. Retrieved February 27, 2025.](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels/)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)

---

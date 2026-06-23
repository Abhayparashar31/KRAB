# Search Open Websites/Domains

## Description

Adversaries may search freely available websites and/or domains for information about victims that can be used during targeting. Information about victims may be available in various online sites, such as social media, new sites, or those hosting information about business operations such as hiring or requested/rewarded contracts. [1] [2] [3]

Adversaries may search in different online sites depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: Phishing for Information or Search Open Technical Databases ), establishing operational resources (ex: Establish Accounts or Compromise Accounts ), and/or initial access (ex: External Remote Services or Phishing ).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0099 | APT-C-36 | APT-C-36 has gathered information on Colombian financial institutions, including Bancolombia, BBVA, Banco Caja Social, and Davivienda to craft phishing pages. [4] |
| G1052 | Contagious Interview | Contagious Interview has utilized open-source indicator of compromise repositories to determine their exposure to include VirusTotal, and MalTrail. [5] |
| G0129 | Mustang Panda | Mustang Panda has used open-source research to identify information about victims to use in targeting to include creating weaponized phishing lures and attachments. [6] [7] |
| G0034 | Sandworm Team | Sandworm Team researched Ukraine's unique legal entity identifier (called an "EDRPOU" number), including running queries on the EDRPOU website, in preparation for the NotPetya attack. Sandworm Team has also researched third-party websites to help it craft credible spearphishing emails. [8] |
| G1033 | Star Blizzard | Star Blizzard has used open-source research to identify information about victims to use in targeting. [9] [10] |
| G1017 | Volt Typhoon | Volt Typhoon has conducted pre-compromise web searches for victim information. [11] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1013 | Application Developer Guidance | Application developers uploading to public code repositories should be careful to avoid publishing sensitive information such as credentials and API keys. |
| M1047 | Audit | Scan public code repositories for exposed credentials or other sensitive information before making commits. Ensure that any leaked credentials are removed from the commit history, not just the current latest version of the code. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0856 | Detection of Search Open Websites/Domains | AN1988 | Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access. |

---

## References

- [Cyware Hacker News. (2019, October 2). How Hackers Exploit Social Media To Break Into Your Company. Retrieved October 20, 2020.](https://cyware.com/news/how-hackers-exploit-social-media-to-break-into-your-company-88e8da8e)
- [Borges, E. (2019, March 5). Exploring Google Hacking Techniques. Retrieved September 12, 2024.](https://www.recordedfuture.com/threat-intelligence-101/threat-analysis-techniques/google-dorks)
- [Offensive Security. (n.d.). Google Hacking Database. Retrieved October 23, 2020.](https://www.exploit-db.com/google-hacking-database)
- [Melnyk, S. (2025, June 27). Tracing Blind Eagle to Proton66. Retrieved April 16, 2026.](https://www.levelblue.com/blogs/spiderlabs-blog/tracing-blind-eagle-to-proton66/)
- [Aleksandar Milenkoski, Sreekar Madabushi, Kenneth Kinion. (2025, September 4). Contagious Interview | North Korean Threat Actors Reveal Plans and Ops by Abusing Cyber Intel Platforms. Retrieved October 20, 2025.](https://www.sentinelone.com/labs/contagious-interview-threat-actors-scout-cyber-intel-platforms-reveal-plans-and-ops/)
- [Golo Muhr, Joshua Chung. (2025, June 23). Hive0154 aka Mustang Panda shifts focus on Tibetan community to deploy Pubload backdoor. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-mustang-panda-shifts-focus-tibetan-community-deploy-pubload-backdoor)
- [Golo Muhr, Joshua Chung. (2025, May 15). Hive0154 targeting US, Philippines, Pakistan and Taiwan in suspected espionage campaign. Retrieved August 4, 2025.](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
- [Scott W. Brady. (2020, October 15). United States vs. Yuriy Sergeyevich Andrienko et al.. Retrieved November 25, 2020.](https://www.justice.gov/opa/press-release/file/1328521/download)
- [Microsoft Threat Intelligence. (2022, August 15). Disrupting SEABORGIUM’s ongoing phishing operations. Retrieved June 13, 2024.](https://www.microsoft.com/en-us/security/blog/2022/08/15/disrupting-seaborgiums-ongoing-phishing-operations/)
- [CISA, et al. (2023, December 7). Russian FSB Cyber Actor Star Blizzard Continues Worldwide Spear-phishing Campaigns. Retrieved June 13, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-341a)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)

---

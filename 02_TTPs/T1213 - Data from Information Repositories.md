# Data from Information Repositories

## Description

Adversaries may leverage information repositories to mine valuable information. Information repositories are tools that allow for storage of information, typically to facilitate collaboration or information sharing between users, and can store a wide variety of data that may aid adversaries in further objectives, such as Credential Access, Lateral Movement, or Defense Evasion, or direct access to the target information. Adversaries may also abuse external sharing features to share sensitive documents with recipients outside of the organization (i.e., Transfer Data to Cloud Account ).

The following is a brief list of example information that may hold potential value to an adversary and may also be found on an information repository:

Information stored in a repository may vary based on the specific instance or environment. Specific common information repositories include the following:

In some cases, information repositories have been improperly secured, typically by unintentionally allowing for overly-broad access by all users or even public access to unauthenticated users. This is particularly common with cloud-native or cloud-hosted services, such as AWS Relational Database Service (RDS), Redis, or ElasticSearch. [1] [2] [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0007 | APT28 | APT28 has collected files from various information repositories. [4] |
| S1148 | Raccoon Stealer | Raccoon Stealer gathers information from repositories associated with cryptocurrency wallets and the Telegram messaging service. [5] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 accessed victims' internal knowledge repositories (wikis) to view sensitive corporate information on products, services, and internal business operations. [6] |
| S1196 | Troll Stealer | Troll Stealer gathers information from the Government Public Key Infrastructure (GPKI) folder, associated with South Korean government public key infrastructure, on infected systems. [7] [8] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Consider periodic review of accounts and privileges for critical and sensitive repositories. Ensure that repositories such as cloud-hosted databases are not unintentionally exposed to the public, and that security groups assigned to them permit only necessary and authorized hosts. [9] |
| M1041 | Encrypt Sensitive Information | Encrypt data stored at rest in databases. |
| M1032 | Multi-factor Authentication | Use two or more pieces of evidence to authenticate to a system; such as username and password in addition to a token from a physical smart card or token generator. |
| M1060 | Out-of-Band Communications Channel | Create plans for leveraging a secure out-of-band communications channel, rather than existing in-network chat applications, in case of a security incident. [10] |
| M1054 | Software Configuration | Consider implementing data retention policies to automate periodically archiving and/or deleting data that is no longer needed. |
| M1018 | User Account Management | Enforce the principle of least-privilege. Consider implementing access control mechanisms that include both authentication and authorization. |
| M1017 | User Training | Develop and publish policies that define acceptable information to be stored in repositories. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0413 | Abuse of Information Repositories for Data Collection | AN1160 | Programmatic or excessive access to file shares, SharePoint, or database repositories by users not typically interacting with them. This includes abnormal access by privileged accounts, enumeration of large numbers of files, or downloads of sensitive content in bursts. |
| AN1161 | Command-line tools (e.g., curl, rsync, wget, or custom Python scripts) used to scrape documentation systems or internal REST APIs. Unusual access patterns to knowledge base folders or shared team drives. |  |  |
| AN1162 | Abuse of SaaS platforms such as Confluence, GitHub, SharePoint Online, or Slack to access excessive internal documentation or export source code/data. Includes use of tokens or browser automation from unapproved IPs. |  |  |
| AN1163 | Access of mounted cloud shares or document repositories via browser, terminal, or Finder by users not typically interacting with those resources. Includes script-based enumeration or mass download. |  |  |

---

## References

- [Ariel Szarf, Doron Karmi, and Lionel Saposnik. (n.d.). Oops, I Leaked It Again — How Mitiga Found PII in Exposed Amazon RDS Snapshots. Retrieved September 24, 2024.](https://www.mitiga.io/blog/how-mitiga-found-pii-in-exposed-amazon-rds-snapshots)
- [David Fiser and Jaromir Horejsi. (2020, April 21). Exposed Redis Instances Abused for Remote Code Execution, Cryptocurrency Mining. Retrieved September 25, 2024.](https://www.trendmicro.com/en_us/research/20/d/exposed-redis-instances-abused-for-remote-code-execution-cryptocurrency-mining.html)
- [Vilius Petkauskas . (2022, November 3). Thomson Reuters collected and leaked at least 3TB of sensitive data. Retrieved September 25, 2024.](https://cybernews.com/security/thomson-reuters-leaked-terabytes-sensitive-data/)
- [NSA, CISA, FBI, NCSC. (2021, July). Russian GRU Conducting Global Brute Force Campaign to Compromise Enterprise and Cloud Environments. Retrieved July 26, 2021.](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [CrowdStrike. (2022, January 27). Early Bird Catches the Wormhole: Observations from the StellarParticle Campaign. Retrieved February 7, 2022.](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)
- [Jiho Kim & Sebin Lee, S2W. (2024, February 7). Kimsuky disguised as a Korean company signed with a valid certificate to distribute Troll Stealer (English ver.). Retrieved January 17, 2025.](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
- [Symantec Threat Hunter Team. (2024, May 16). Springtail: New Linux Backdoor Added to Toolkit. Retrieved January 17, 2025.](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
- [AWS. (n.d.). Working with a DB instance in a VPC. Retrieved September 24, 2024.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)
- [Tyler Hudak. (2022, December 29). To OOB, or Not to OOB?: Why Out-of-Band Communications are Essential for Incident Response. Retrieved August 30, 2024.](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)

---

# Search Victim-Owned Websites

## Description

Adversaries may search websites owned by the victim for information that can be used during targeting. Victim-owned websites may contain a variety of details, including names of departments/divisions, physical locations, and data about key employees such as names, roles, and contact info (ex: Email Addresses ). These sites may also have details highlighting business operations and relationships. [1]

Adversaries may search victim-owned websites to gather actionable information. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: Phishing for Information or Search Open Technical Databases ), establishing operational resources (ex: Establish Accounts or Compromise Accounts ), and/or initial access (ex: Trusted Relationship or Phishing ).

In addition to manually browsing the website, adversaries may attempt to identify hidden directories or files that could contain additional sensitive information or vulnerable functionality. They may do this through automated activities such as Wordlist Scanning , as well as by leveraging files such as sitemap.xml and robots.txt. [2] [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0040 | APT41 DUST | APT41 DUST involved access of external victim websites for target development. [4] |
| C0029 | Cutting Edge | During Cutting Edge , threat actors peformed reconnaissance of victims' internal websites via proxied connections. [5] |
| G1011 | EXOTIC LILY | EXOTIC LILY has used contact forms on victim websites to generate phishing e-mails. [6] |
| G0094 | Kimsuky | Kimsuky has searched for information on the target company's website. [7] |
| C0049 | Leviathan Australian Intrusions | Leviathan enumerated compromised web application resources to identify additional endpoints and resources linkd to the website for follow-on access during Leviathan Australian Intrusions . [8] |
| G0034 | Sandworm Team | Sandworm Team has conducted research against potential victim websites as part of its operational planning. [9] |
| G0122 | Silent Librarian | Silent Librarian has searched victim's websites to identify the interests and academic areas of targeted individuals and to scrape source code, branding, and organizational contact information for phishing pages. [10] [11] [12] |
| G1038 | TA578 | TA578 has filled out contact forms on victims' websites to direct them to adversary-controlled URLs. [13] |
| G1017 | Volt Typhoon | Volt Typhoon has conducted pre-compromise reconnaissance on victim-owned sites. [14] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0810 | Detection of Search Victim-Owned Websites | AN1942 | Monitor for suspicious network traffic that could be indicative of adversary reconnaissance, such as rapid successions of requests indicative of web crawling and/or large quantities of requests originating from a single source (especially if the source is known to be associated with an adversary). Analyzing web metadata may also reveal artifacts that can be attributed to potentially malicious activity, such as referer or user-agent string HTTP/S fields. |

---

## References

- [Bischoff, P. (2020, October 15). Broadvoice database of more than 350 million customer records exposed online. Retrieved October 20, 2020.](https://www.comparitech.com/blog/vpn-privacy/350-million-customer-records-exposed-online/)
- [Adi Perez. (2023, February 22). How Attackers Can Misuse Sitemaps to Enumerate Users and Discover Sensitive Information. Retrieved July 18, 2024.](https://medium.com/@adimenia/how-attackers-can-misuse-sitemaps-to-enumerate-users-and-discover-sensitive-information-361a5065857a)
- [Darren Pauli. (2015, May 19). Robots.txt tells hackers the places you don't want them to look. Retrieved July 18, 2024.](https://www.theregister.com/2015/05/19/robotstxt/)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Meltzer, M. et al. (2024, January 10). Active Exploitation of Two Zero-Day Vulnerabilities in Ivanti Connect Secure VPN. Retrieved February 27, 2024.](https://www.volexity.com/blog/2024/01/10/active-exploitation-of-two-zero-day-vulnerabilities-in-ivanti-connect-secure-vpn/)
- [Stolyarov, V. (2022, March 17). Exposing initial access broker with ties to Conti. Retrieved August 18, 2022.](https://blog.google/threat-analysis-group/exposing-initial-access-broker-ties-conti/)
- [KISA. (2021). Phishing Target Reconnaissance and Attack Resource Analysis Operation Muzabi. Retrieved March 8, 2024.](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
- [CISA et al. (2024, July 8). People’s Republic of China (PRC) Ministry of State Security APT40 Tradecraft in Action. Retrieved February 3, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a)
- [Scott W. Brady. (2020, October 15). United States vs. Yuriy Sergeyevich Andrienko et al.. Retrieved November 25, 2020.](https://www.justice.gov/opa/press-release/file/1328521/download)
- [DOJ. (2018, March 23). U.S. v. Rafatnejad et al . Retrieved February 3, 2021.](https://www.justice.gov/usao-sdny/press-release/file/1045781/download)
- [Hassold, Crane. (2018, March 26). Silent Librarian: More to the Story of the Iranian Mabna Institute Indictment. Retrieved February 3, 2021.](https://info.phishlabs.com/blog/silent-librarian-more-to-the-story-of-the-iranian-mabna-institute-indictment)
- [Proofpoint Threat Insight Team. (2019, September 5). Threat Actor Profile: TA407, the Silent Librarian. Retrieved February 3, 2021.](https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta407-silent-librarian)
- [Proofpoint Threat Research and Team Cymru S2 Threat Research. (2024, April 4). Latrodectus: This Spider Bytes Like Ice . Retrieved May 31, 2024.](https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)

---

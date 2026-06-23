# Search Open Technical Databases

## Description

Adversaries may search freely available technical databases for information about victims that can be used during targeting. Information about victims may be available in online databases and repositories, such as registrations of domains/certificates as well as public collections of network data/artifacts gathered from traffic and/or scans. [1] [2] [3] [4] [5] [6] [7]

Adversaries may search in different open databases depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: Phishing for Information or Search Open Websites/Domains ), establishing operational resources (ex: Acquire Infrastructure or Compromise Infrastructure ), and/or initial access (ex: External Remote Services or Trusted Relationship ).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0007 | APT28 | APT28 has used large language models (LLMs) to assist in script development and deployment. [8] [9] |
| G0094 | Kimsuky | Kimsuky has used LLMs to better understand publicly reported vulnerabilities. [8] [9] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0860 | Detection of Search Open Technical Databases | AN1992 | Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access. |

---

## References

- [NTT America. (n.d.). Whois Lookup. Retrieved November 17, 2024.](https://who.is/)
- [Hacker Target. (n.d.). DNS Dumpster. Retrieved October 20, 2020.](https://dnsdumpster.com/)
- [CIRCL Computer Incident Response Center. (n.d.). Passive DNS. Retrieved October 20, 2020.](https://www.circl.lu/services/passive-dns/)
- [Jain, M. (2019, September 16). Export & Download — SSL Certificate from Server (Site URL). Retrieved October 20, 2020.](https://medium.com/@menakajain/export-download-ssl-certificate-from-server-site-url-bcfc41ea46a2)
- [SSL Shopper. (n.d.). SSL Checker. Retrieved October 20, 2020.](https://www.sslshopper.com/ssl-checker.html)
- [Swisscom & Digital Shadows. (2017, September 6). Content Delivery Networks (CDNs) Can Leave You Exposed – How You Might Be Affected And What You Can Do About It. Retrieved October 20, 2020.](https://www.digitalshadows.com/blog-and-research/content-delivery-networks-cdns-can-leave-you-exposed-how-you-might-be-affected-and-what-you-can-do-about-it/)
- [Shodan. (n.d.). Shodan. Retrieved October 20, 2020.](https://shodan.io)
- [Microsoft Threat Intelligence. (2024, February 14). Staying ahead of threat actors in the age of AI. Retrieved March 11, 2024.](https://www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai/)
- [OpenAI. (2024, February 14). Disrupting malicious uses of AI by state-affiliated threat actors. Retrieved September 12, 2024.](https://openai.com/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/)

---

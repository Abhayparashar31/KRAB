# Gather Victim Network Information

## Description

Adversaries may gather information about the victim's networks that can be used during targeting. Information about networks may include a variety of details, including administrative data (ex: IP ranges, domain names, etc.) as well as specifics regarding its topology and operations.

Adversaries may gather this information in various ways, such as direct collection actions via Active Scanning or Phishing for Information . Information about networks may also be exposed to adversaries via online or other accessible data sets (ex: Search Open Technical Databases ). [1] [2] [3] Gathering this information may reveal opportunities for other forms of reconnaissance (ex: Active Scanning or Search Open Websites/Domains ), establishing operational resources (ex: Acquire Infrastructure or Compromise Infrastructure ), and/or initial access (ex: Trusted Relationship ).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0125 | HAFNIUM | HAFNIUM gathered the fully qualified domain names (FQDNs) for targeted Exchange servers in the victim's environment. [4] |
| G0119 | Indrik Spider | Indrik Spider has downloaded tools, such as the Advanced Port Scanner utility and Lansweeper, to conduct internal reconnaissance of the victim network. Indrik Spider has also accessed the victim’s VMware VCenter, which had information about host configuration, clusters, etc. [5] |
| G1017 | Volt Typhoon | Volt Typhoon has conducted extensive pre-compromise reconnaissance to learn about the target organization’s network. [6] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0869 | Detection of Gather Victim Network Information | AN2001 | Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access. |

---

## References

- [NTT America. (n.d.). Whois Lookup. Retrieved November 17, 2024.](https://who.is/)
- [Hacker Target. (n.d.). DNS Dumpster. Retrieved October 20, 2020.](https://dnsdumpster.com/)
- [CIRCL Computer Incident Response Center. (n.d.). Passive DNS. Retrieved October 20, 2020.](https://www.circl.lu/services/passive-dns/)
- [Gruzweig, J. et al. (2021, March 2). Operation Exchange Marauder: Active Exploitation of Multiple Zero-Day Microsoft Exchange Vulnerabilities. Retrieved March 3, 2021.](https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/)
- [Mandiant Intelligence. (2022, June 2). To HADES and Back: UNC2165 Shifts to LOCKBIT to Evade Sanctions. Retrieved July 29, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)

---

# Gather Victim Host Information

## Description

Adversaries may gather information about the victim's hosts that can be used during targeting. Information about hosts may include a variety of details, including administrative data (ex: name, assigned IP, functionality, etc.) as well as specifics regarding its configuration (ex: operating system, language, etc.).

Adversaries may gather this information in various ways, such as direct collection actions via Active Scanning or Phishing for Information . Adversaries may also compromise sites then include malicious content designed to collect host information from visitors. [1] Information about hosts may also be exposed to adversaries via online or other accessible data sets (ex: Social Media or Search Victim-Owned Websites ). Gathering this information may reveal opportunities for other forms of reconnaissance (ex: Search Open Websites/Domains or Search Open Technical Databases ), establishing operational resources (ex: Develop Capabilities or Obtain Capabilities ), and/or initial access (ex: Supply Chain Compromise or External Remote Services ).

Adversaries may also gather victim host information via User-Agent HTTP headers, which are sent to a server to identify the application, operating system, vendor, and/or version of the requesting user agent. This can be used to inform the adversary’s follow-on action. For example, adversaries may check user agents for the requesting operating system, then only serve malware for target operating systems while ignoring others. [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1017 | Volt Typhoon | Volt Typhoon has conducted pre-compromise reconnaissance for victim host information. [3] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0826 | Detection of Gather Victim Host Information | AN1958 | Internet scanners may be used to look for patterns associated with malicious content designed to collect host information from visitors. [4] [1] Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Initial Access. |

---

## References

- [Blasco, J. (2014, August 28). Scanbox: A Reconnaissance Framework Used with Watering Hole Attacks. Retrieved October 19, 2020.](https://cybersecurity.att.com/blogs/labs-research/scanbox-a-reconnaissance-framework-used-on-watering-hole-attacks)
- [Pham Duy Phuc, John Fokker J.E., Alejandro Houspanossian and Mathanraj Thangaraju. (2023, March 7). Qakbot Evolves to OneNote Malware Distribution. Retrieved August 1, 2024.](https://www.trellix.com/blogs/research/qakbot-evolves-to-onenote-malware-distribution/)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [ThreatConnect. (2020, December 15). Infrastructure Research and Hunting: Boiling the Domain Ocean. Retrieved October 12, 2021.](https://threatconnect.com/blog/infrastructure-research-hunting/)

---

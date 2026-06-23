# Search Threat Vendor Data

## Description

Threat actors may seek information/indicators from closed or open threat intelligence sources gathered about their own campaigns, as well as those conducted by other adversaries that may align with their target industries, capabilities/objectives, or other operational concerns. These reports may include descriptions of behavior, detailed breakdowns of attacks, atomic indicators such as malware hashes or IP addresses, timelines of a group’s activity, and more. Adversaries may change their behavior when planning their future operations.

Adversaries have been observed replacing atomic indicators mentioned in blog posts in under a week. [1] Adversaries have also been seen searching for their own domain names in threat vendor data and then taking them down, likely to avoid seizure or further investigation. [2]

This technique is distinct from Threat Intel Vendors in that it describes threat actors performing reconnaissance on their own activity, not in search of victim information.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1052 | Contagious Interview | Contagious Interview has registered accounts with Threat Intelligence vendor services to check for reporting associated with their infrastructure and to evaluate new potential infrastructure. [2] |
| G1048 | UNC3886 | UNC3886 has replaced indicators mentioned in open-source threat intelligence publications at times under a week after their release. [1] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on designing defenses that are not reliant on atomic indicators. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0866 | Detection of Search Threat Vendor Data | AN1998 | Much of this activity may have a very high occurrence and associated false positive rate, as well as potentially taking place outside the visibility of the target organization, making detection difficult for defenders. |

---

## References

- [Alexander Marvi, Brad Slaybaugh, Ron Craft, and Rufus Brown. (2023, June 13). VMware ESXi Zero-Day Used by Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)
- [Aleksandar Milenkoski, Sreekar Madabushi, Kenneth Kinion. (2025, September 4). Contagious Interview | North Korean Threat Actors Reveal Plans and Ops by Abusing Cyber Intel Platforms. Retrieved October 20, 2025.](https://www.sentinelone.com/labs/contagious-interview-threat-actors-scout-cyber-intel-platforms-reveal-plans-and-ops/)

---

# Data Manipulation

## Description

Adversaries may insert, delete, or manipulate data in order to influence external outcomes or hide activity, thus threatening the integrity of the data. [1] By manipulating data, adversaries may attempt to affect a business process, organizational understanding, or decision making.

The type of modification and the impact it will have depends on the target application and process as well as the goals and objectives of the adversary. For complex systems, an adversary would likely need special expertise and possibly access to specialized software related to the system that would typically be gained through a prolonged information gathering campaign in order to have the desired impact.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1016 | FIN13 | FIN13 has injected fraudulent transactions into compromised networks that mimic legitimate behavior to siphon off incremental amounts of money. [1] |
| S9014 | PHASEJAM | PHASEJAM has blocked legitimate upgrades of Ivanti Connect Secure systems and falsely indicates a successful upgrade while operating on an older version. [2] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1041 | Encrypt Sensitive Information | Consider encrypting important information to reduce an adversary’s ability to perform tailored data modifications. |
| M1030 | Network Segmentation | Identify critical business and system processes that may be targeted by adversaries and work to isolate and secure those systems against unauthorized access and tampering. |
| M1029 | Remote Data Storage | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data. [3] Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and manipulate backups. |
| M1022 | Restrict File and Directory Permissions | Ensure least privilege principles are applied to important information resources to reduce exposure to data manipulation risk. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0059 | Detection Strategy for Data Manipulation | AN0162 | Correlate unauthorized or anomalous file modifications, deletions, or metadata changes with suspicious process execution or API calls. Detect abnormal changes to structured data (e.g., database files, logs, financial records) outside expected business process activity. |
| AN0163 | Detect unauthorized manipulation of log files, database entries, or system configuration files through auditd and syslog. Correlate shell commands that alter HISTFILE or data-related processes with abnormal file access patterns. |  |  |
| AN0164 | Detect manipulation of system or application files in /Library , /System , or user data directories using FSEvents and Unified Logs. Identify anomalous process execution modifying plist files, structured data, or logs outside expected update cycles. |  |  |

---

## References

- [Sygnia Incident Response Team. (2022, January 5). TG2003: ELEPHANT BEETLE UNCOVERING AN ORGANIZED FINANCIAL-THEFT OPERATION. Retrieved February 9, 2023.](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)
- [John Wolfram, Josh Murchie, Matt Lin, Daniel Ainsworth, Robert Wallace, Dimiter Andonov, Dhanesh Kizhakkinan, Jacob Thompson. (2025, January 8). Ivanti Connect Secure VPN Targeted in New Zero-Day Exploitation. Retrieved April 14, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
- [Ready.gov. (n.d.). IT Disaster Recovery Plan. Retrieved March 15, 2019.](https://www.ready.gov/business/implementation/IT)

---

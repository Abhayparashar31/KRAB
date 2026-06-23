# Active Scanning

## Description

Adversaries may execute active reconnaissance scans to gather information that can be used during targeting. Active scans are those where the adversary probes victim infrastructure via network traffic, as opposed to other forms of reconnaissance that do not involve direct interaction.

Adversaries may perform different forms of active scanning depending on what information they seek to gather. These scans can also be performed in various ways, including using native features of network protocols such as ICMP. [1] [2] Information from these scans may reveal opportunities for other forms of reconnaissance (ex: Search Open Websites/Domains or Search Open Technical Databases ), establishing operational resources (ex: Develop Capabilities or Obtain Capabilities ), and/or initial access (ex: External Remote Services or Exploit Public-Facing Application ).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0030 | Triton Safety Instrumented System Attack | In the Triton Safety Instrumented System Attack , TEMP.Veles engaged in network reconnaissance against targets of interest. [3] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0830 | Detection of Active Scanning | AN1962 | Monitor network data for uncommon data flows. Processes utilizing the network that do not normally have network communication or have never been seen before are suspicious. Monitor and analyze traffic patterns and packet inspection associated to protocol(s) that do not follow the expected protocol standards and traffic flows (e.g extraneous packets that do not belong to established flows, gratuitous or anomalous traffic patterns, anomalous syntax, or structure). Consider correlation with process monitoring and command line to detect anomalous processes execution and command line arguments associated to traffic patterns (e.g. monitor anomalies in use of files that do not normally initiate connections for respective protocol(s)). |

---

## References

- [Dainotti, A. et al. (2012). Analysis of a “/0” Stealth Scan from a Botnet. Retrieved October 20, 2020.](https://www.caida.org/publications/papers/2012/analysis_slash_zero/analysis_slash_zero.pdf)
- [OWASP Wiki. (2018, February 16). OAT-004 Fingerprinting. Retrieved October 20, 2020.](https://wiki.owasp.org/index.php/OAT-004_Fingerprinting)
- [FireEye Intelligence . (2018, October 23). TRITON Attribution: Russian Government-Owned Lab Most Likely Built Custom Intrusion Tools for TRITON Attackers. Retrieved April 16, 2019.](https://www.fireeye.com/blog/threat-research/2018/10/triton-attribution-russian-government-owned-lab-most-likely-built-tools.html)

---

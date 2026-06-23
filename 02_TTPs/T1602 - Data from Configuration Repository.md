# Data from Configuration Repository

## Description

Adversaries may collect data related to managed devices from configuration repositories. Configuration repositories are used by management systems in order to configure, manage, and control data on remote systems. Configuration repositories may also facilitate remote access and administration of devices.

Adversaries may target these repositories in order to collect large quantities of sensitive system administration data. Data from configuration repositories may be exposed by various protocols and software and can store a wide variety of data, much of which may align with adversary Discovery objectives. [1] [2]

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1041 | Encrypt Sensitive Information | Configure SNMPv3 to use the highest level of security (authPriv) available. [2] |
| M1037 | Filter Network Traffic | Apply extended ACLs to block unauthorized protocols outside the trusted network. [2] |
| M1031 | Network Intrusion Prevention | Configure intrusion prevention devices to detect SNMP queries and commands from unauthorized sources. [1] |
| M1030 | Network Segmentation | Segregate SNMP traffic on a separate management network. [2] |
| M1054 | Software Configuration | Allowlist MIB objects and implement SNMP views. [3] |
| M1051 | Update Software | Keep system images and software updated and migrate to SNMPv3. [4] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0592 | Detection Strategy for Data from Configuration Repository on Network Devices | AN1630 | Defenders may observe adversary attempts to extract configuration data from management repositories by monitoring for anomalous SNMP queries, API calls, or protocol requests (e.g., NETCONF, RESTCONF) that enumerate system configuration. Suspicious sequences include repeated queries from untrusted IPs, abnormal query types requesting sensitive configuration data, or repository access occurring outside of normal administrative maintenance windows. Abnormal authentication attempts, sudden enumeration of device inventory, or bulk data transfer of configuration files may also be observed. |

---

## References

- [US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved October 19, 2020.](https://www.us-cert.gov/ncas/alerts/TA18-106A)
- [US-CERT. (2017, June 5). Reducing the Risk of SNMP Abuse. Retrieved October 19, 2020.](https://us-cert.cisa.gov/ncas/alerts/TA17-156A)
- [Cisco. (2006, May 10). Securing Simple Network Management Protocol. Retrieved October 19, 2020.](https://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/20370-snmpsecurity-20370.html)
- [Omar Santos. (2020, October 19). Attackers Continue to Target Legacy Devices. Retrieved October 20, 2020.](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)

---

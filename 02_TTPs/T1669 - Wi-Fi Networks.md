# Wi-Fi Networks

## Description

Adversaries may gain initial access to target systems by connecting to wireless networks. They may accomplish this by exploiting open Wi-Fi networks used by target devices or by accessing secured Wi-Fi networks — requiring Valid Accounts — belonging to a target organization. [1] [2] Establishing a connection to a Wi-Fi access point requires a certain level of proximity to both discover and maintain a stable network connection.

Adversaries may establish a wireless connection through various methods, such as by physically positioning themselves near a Wi-Fi network to conduct close access operations. To bypass the need for physical proximity, adversaries may attempt to remotely compromise nearby third-party systems that have both wired and wireless network connections available (i.e., dual-homed systems). These third-party compromised devices can then serve as a bridge to connect to a target’s Wi-Fi network. [2]

Once an initial wireless connection is achieved, adversaries may leverage this access for follow-on activities in the victim network or further targeting of specific devices on the network. Adversaries may perform Network Sniffing or Adversary-in-the-Middle activities for Credential Access or Discovery .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0007 | APT28 | APT28 has exploited open Wi-Fi access points for initial access to target devices using the network. [2] [1] |
| C0051 | APT28 Nearest Neighbor Campaign | During APT28 Nearest Neighbor Campaign , APT28 established wireless connections to secure, enterprise Wi-Fi networks belonging to a target organization for initial access into the environment. [2] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1041 | Encrypt Sensitive Information | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure that web traffic that may contain credentials is protected by SSL/TLS. |
| M1032 | Multi-factor Authentication | Harden access requirements for Wi-Fi networks through using two or more pieces of evidence to authenticate, such as a username and password in addition to a token from a physical smart card or token generator. |
| M1030 | Network Segmentation | Network segmentation can be used to isolate infrastructure components that do not require broad network access. Separate networking environments for Wi-Fi and Ethernet-wired networks, particularly where Ethernet-based networks allow for access to sensitive resources. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0536 | Detection Strategy for Wi-Fi Networks | AN1476 | Detects anomalous wireless connections such as unexpected SSID associations, failed or repeated authentication attempts, and connections outside of known geofenced networks. Defenders should monitor wireless connection logs and event codes for network discovery, authentication, and association events. |
| AN1477 | Detects unauthorized wireless associations by monitoring wpa_supplicant logs, NetworkManager events, and system calls related to interface state changes. Anomalies include repeated association failures, new SSIDs outside baselined values, and rogue AP connections. |  |  |
| AN1478 | Detects unauthorized Wi-Fi associations and SSID scanning activity using unified logs and airport command telemetry. Anomalies include rapid SSID switching, connections to unapproved SSIDs, or repeated authentication failures. |  |  |
| AN1479 | Detects rogue or suspicious wireless access attempts by monitoring firewall, WIDS/WIPS, and controller logs. Focus is on firewall rule changes, rogue AP detection, and anomalous MAC addresses connecting to access points. |  |  |

---

## References

- [U.S. Department of Justice. (2018, October 4). U.S. Charges Russian GRU Officers with International Hacking and Related Influence and Disinformation Operations. Retrieved February 25, 2025.](https://www.justice.gov/archives/opa/pr/us-charges-russian-gru-officers-international-hacking-and-related-influence-and)
- [Koessel, Sean. Adair, Steven. Lancaster, Tom. (2024, November 22). The Nearest Neighbor Attack: How A Russian APT Weaponized Nearby Wi-Fi Networks for Covert Access. Retrieved February 25, 2025.](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)

---

# Network Boundary Bridging

## Description

Adversaries may bridge network boundaries by compromising perimeter network devices or internal devices responsible for network segmentation. Breaching these devices may enable an adversary to bypass restrictions on traffic routing that otherwise separate trusted and untrusted networks.

Devices such as routers and firewalls can be used to create boundaries between trusted and untrusted networks. They achieve this by restricting traffic types to enforce organizational policy in an attempt to reduce the risk inherent in such connections. Restriction of traffic can be achieved by prohibiting IP addresses, layer 4 protocol ports, or through deep packet inspection to identify applications. To participate with the rest of the network, these devices can be directly addressable or transparent, but their mode of operation has no bearing on how the adversary can bypass them when compromised.

When an adversary takes control of such a boundary device, they can bypass its policy enforcement to pass normally prohibited traffic across the trust boundary between the two separated networks without hinderance. By achieving sufficient rights on the device, an adversary can reconfigure the device to allow the traffic they want, allowing them to then further achieve goals such as command and control via Multi-hop Proxy or exfiltration of data via Traffic Duplication . Adversaries may also target internal devices responsible for network segmentation and abuse these in conjunction with Internal Proxy to achieve the same goals. [1] In the cases where a border device separates two separate organizations, the adversary can also facilitate lateral movement into new victim environments.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0096 | APT41 | APT41 used NATBypass to bypass firewall restrictions and to access compromised systems via RDP. [2] |
| C0043 | Indian Critical Infrastructure Intrusions | Indian Critical Infrastructure Intrusions involved the use of FRP to bridge network boundaries and overcome NAT. [3] Indian Critical Infrastructure Intrusions also involved the use of VPN tunnels with a potentially compromised MSP entity allowing for direct access to critical infrastructure entity networks. [4] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1043 | Credential Access Protection | Some embedded network devices are capable of storing passwords for local accounts in either plain-text or encrypted formats. Ensure that, where available, local passwords are always encrypted, per vendor recommendations. [5] |
| M1037 | Filter Network Traffic | Upon identifying a compromised network device being used to bridge a network boundary, block the malicious packets using an unaffected network device in path, such as a firewall or a router that has not been compromised. Continue to monitor for additional activity and to ensure that the blocks are indeed effective. |
| M1032 | Multi-factor Authentication | Use multi-factor authentication for user and privileged accounts. Most embedded network devices support TACACS+ and/or RADIUS. Follow vendor prescribed best practices for hardening access control. [6] |
| M1027 | Password Policies | Refer to NIST guidelines when creating password policies. [7] |
| M1026 | Privileged Account Management | Restrict administrator accounts to as few individuals as possible, following least privilege principles. Prevent credential overlap across systems of administrator and privileged accounts, particularly between network and non-network platforms, such as servers or endpoints. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0006 | Detection Strategy for Network Boundary Bridging | AN0015 | From a defender’s perspective, suspicious bridging is observed when network devices begin allowing traffic that contradicts existing segmentation or access policies. Observable behaviors include sudden modifications to ACLs or firewall rules, unusual cross-boundary traffic flows (e.g., east-west communications across separated VLANs), or simultaneous ingress/egress anomalies. Multi-event correlation is key: configuration changes on a router/firewall followed by unexpected traffic patterns, especially from unusual sources, is a strong indicator of compromise. |

---

## References

- [Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle. Retrieved October 27, 2021.](https://securelist.com/lazarus-threatneedle/100803/)
- [DCSO CyTec Blog. (2022, December 24). APT41 — The spy who failed to encrypt me. Retrieved June 13, 2024.](https://medium.com/@DCSO_CyTec/apt41-the-spy-who-failed-to-encrypt-me-24fc0f49cad1)
- [Recorded Future Insikt Group. (2022, April 6). Continued Targeting of Indian Power Grid Assets by Chinese State-Sponsored Activity Group. Retrieved November 21, 2024.](https://go.recordedfuture.com/hubfs/reports/ta-2022-0406.pdf)
- [Dragos. (2022). 2021 ICS Cybersecurity Year in Review. Retrieved November 21, 2024.](https://hub.dragos.com/hubfs/333%20Year%20in%20Review/2021/2021%20ICS%20OT%20Cybersecurity%20Year%20In%20Review%20-%20Dragos%202021.pdf?hsLang=en)
- [Cisco. (n.d.). Cisco IOS Software Integrity Assurance - AAA. Retrieved October 19, 2020.](https://tools.cisco.com/security/center/resources/integrity_assurance.html#38)
- [Cisco. (n.d.). Cisco IOS Software Integrity Assurance - TACACS. Retrieved October 19, 2020.](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)
- [Grassi, P., et al. (2017, December 1). SP 800-63-3, Digital Identity Guidelines. Retrieved January 16, 2019.](https://pages.nist.gov/800-63-3/sp800-63b.html)

---

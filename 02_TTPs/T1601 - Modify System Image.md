# Modify System Image

## Description

Adversaries may make changes to the operating system of embedded network devices to weaken defenses and provide new capabilities for themselves. On such devices, the operating systems are typically monolithic and most of the device functionality and capabilities are contained within a single file.

To change the operating system, the adversary typically only needs to affect this one file, replacing or modifying it. This can either be done live in memory during system runtime for immediate effect, or in storage to implement the change on the next boot of the network device.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S9013 | DRYHOOK | DRYHOOK has modified the Ivanti Connect Secure VPN authentication Perl module DSAuth.pm by reading its contents in the buffer, then finding and replacing select lines of code. [1] [2] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1046 | Boot Integrity | Some vendors of embedded network devices provide cryptographic signing to ensure the integrity of operating system images at boot time. Implement where available, following vendor guidelines. [3] |
| M1045 | Code Signing | Many vendors provide digitally signed operating system images to validate the integrity of the software used on their platform. Make use of this feature where possible in order to prevent and/or detect attempts by adversaries to compromise the system image. [4] |
| M1043 | Credential Access Protection | Some embedded network devices are capable of storing passwords for local accounts in either plain-text or encrypted formats. Ensure that, where available, local passwords are always encrypted, per vendor recommendations. [5] |
| M1032 | Multi-factor Authentication | Use multi-factor authentication for user and privileged accounts. Most embedded network devices support TACACS+ and/or RADIUS. Follow vendor prescribed best practices for hardening access control. [6] |
| M1027 | Password Policies | Refer to NIST guidelines when creating password policies. [7] |
| M1026 | Privileged Account Management | Restrict administrator accounts to as few individuals as possible, following least privilege principles. Prevent credential overlap across systems of administrator and privileged accounts, particularly between network and non-network platforms, such as servers or endpoints. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0170 | Detection Strategy for Modify System Image on Network Devices | AN0482 | Defenders may observe adversary attempts to alter or replace a network device’s operating system image through anomalous CLI commands, unexpected firmware updates, integrity check failures, or mismatches in version and checksum validation. Suspicious behavior includes modification of image files on storage, OS version output inconsistent with baselines, unexpected reloads or reboots after image replacement, and changes to boot configuration that load non-standard system images. |

---

## References

- [John Wolfram, Josh Murchie, Matt Lin, Daniel Ainsworth, Robert Wallace, Dimiter Andonov, Dhanesh Kizhakkinan, Jacob Thompson. (2025, January 8). Ivanti Connect Secure VPN Targeted in New Zero-Day Exploitation. Retrieved April 14, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
- [Sila Ozeren Hacioglu. (2025, May 5). UNC5221’s Latest Exploit: Weaponizing CVE-2025-22457 in Ivanti Connect Secure. Retrieved April 13, 2026.](https://www.picussecurity.com/resource/blog/unc5221-cve-2025-22457-ivanti-connect-secure)
- [Cisco. (n.d.). Cisco IOS Software Integrity Assurance - Secure Boot. Retrieved October 19, 2020.](https://tools.cisco.com/security/center/resources/integrity_assurance.html#35)
- [Cisco. (n.d.). Cisco IOS Software Integrity Assurance - Deploy Signed IOS. Retrieved October 21, 2020.](https://tools.cisco.com/security/center/resources/integrity_assurance.html#34)
- [Cisco. (n.d.). Cisco IOS Software Integrity Assurance - Credentials Management. Retrieved October 19, 2020.](https://tools.cisco.com/security/center/resources/integrity_assurance.html#40)
- [Cisco. (n.d.). Cisco IOS Software Integrity Assurance - TACACS. Retrieved October 19, 2020.](https://tools.cisco.com/security/center/resources/integrity_assurance.html#39)
- [Grassi, P., et al. (2017, December 1). SP 800-63-3, Digital Identity Guidelines. Retrieved January 16, 2019.](https://pages.nist.gov/800-63-3/sp800-63b.html)

---

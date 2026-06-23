# Weaken Encryption

## Description

Adversaries may compromise a network device’s encryption capability in order to bypass encryption that would otherwise protect data communications. [1]

Encryption can be used to protect transmitted network traffic to maintain its confidentiality (protect against unauthorized disclosure) and integrity (protect against unauthorized changes). Encryption ciphers are used to convert a plaintext message to ciphertext and can be computationally intensive to decipher without the associated decryption key. Typically, longer keys increase the cost of cryptanalysis, or decryption without the key.

Adversaries can compromise and manipulate devices that perform encryption of network traffic. For example, through behaviors such as Modify System Image , Reduce Key Space , and Disable Crypto Hardware , an adversary can negatively effect and/or eliminate a device’s ability to securely encrypt network traffic. This poses a greater risk of unauthorized disclosure and may help facilitate data manipulation, Credential Access, or Collection efforts. [2]

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0339 | Detection Strategy for Weaken Encryption on Network Devices | AN0961 | Defenders may observe unauthorized modifications to encryption-related configuration files, firmware, or crypto modules on network devices. Suspicious patterns include changes to cipher suite configurations, unexpected firmware updates affecting crypto libraries, disabling of hardware cryptographic accelerators, or reductions in key length policies. Correlating configuration changes with anomalies in encrypted traffic characteristics (e.g., weaker ciphers or sudden plaintext transmission) strengthens detection. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0339 | Detection Strategy for Weaken Encryption on Network Devices | AN0961 | Defenders may observe unauthorized modifications to encryption-related configuration files, firmware, or crypto modules on network devices. Suspicious patterns include changes to cipher suite configurations, unexpected firmware updates affecting crypto libraries, disabling of hardware cryptographic accelerators, or reductions in key length policies. Correlating configuration changes with anomalies in encrypted traffic characteristics (e.g., weaker ciphers or sudden plaintext transmission) strengthens detection. |

---

## References

- [Graham Holmes. (2015, October 8). Evolution of attacks on Cisco IOS devices. Retrieved October 19, 2020.](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)
- [Omar Santos. (2020, October 19). Attackers Continue to Target Legacy Devices. Retrieved October 20, 2020.](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)

---

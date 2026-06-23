# Steal or Forge Authentication Certificates

## Description

Adversaries may steal or forge certificates used for authentication to access remote systems or resources. Digital certificates are often used to sign and encrypt messages and/or files. Certificates are also used as authentication material. For example, Entra ID device certificates and Active Directory Certificate Services (AD CS) certificates bind to an identity and can be used as credentials for domain accounts. [1] [2]

Authentication certificates can be both stolen and forged. For example, AD CS certificates can be stolen from encrypted storage (in the Registry or files) [3] , misplaced certificate files (i.e. Unsecured Credentials ), or directly from the Windows certificate store via various crypto APIs. [4] [5] [6] With appropriate enrollment rights, users and/or machines within a domain can also request and/or manually renew certificates from enterprise certificate authorities (CA). This enrollment process defines various settings and permissions associated with the certificate. Of note, the certificate’s extended key usage (EKU) values define signing, encryption, and authentication use cases, while the certificate’s subject alternative name (SAN) values define the certificate owner’s alternate names. [7]

Abusing certificates for authentication credentials may enable other behaviors such as Lateral Movement . Certificate-related misconfigurations may also enable opportunities for Privilege Escalation , by way of allowing users to impersonate or assume privileged accounts or permissions via the identities (SANs) associated with a certificate. These abuses may also enable Persistence via stealing or forging certificates that can be used as Valid Accounts for the duration of the certificate's validity, despite user password resets. Authentication certificates can also be stolen and forged for machine accounts.

Adversaries who have access to root (or subordinate) CA certificate private keys (or mechanisms protecting/managing these keys) may also establish Persistence by forging arbitrary authentication certificates for the victim domain (known as "golden" certificates). [7] Adversaries may also target certificates and related services in order to access other forms of credentials, such as Golden Ticket ticket-granting tickets (TGT) or NTLM plaintext. [7]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0677 | AADInternals | AADInternals can create and export various authentication certificates, including those associated with Azure AD joined/registered devices. [8] |
| G0016 | APT29 | APT29 has abused misconfigured AD CS certificate templates to impersonate admin users and create additional authentication certificates. [9] |
| S0002 | Mimikatz | Mimikatz 's CRYPTO module can create and export various types of authentication certificates. [10] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1015 | Active Directory Configuration | Ensure certificate authorities (CA) are properly secured, including treating CA servers (and other resources hosting CA certificates) as tier 0 assets. Harden abusable CA settings and attributes. For example, consider disabling the usage of AD CS certificate SANs within relevant authentication protocol settings to enforce strict user mappings and prevent certificates from authenticating as other identifies. [4] Also consider enforcing CA Certificate Manager approval for the templates that include SAN as an issuance requirement. |
| M1047 | Audit | Check and remediate unneeded existing authentication certificates as well as common abusable misconfigurations of CA settings and permissions, such as AD CS certificate enrollment permissions and published overly permissive certificate templates (which define available settings for created certificates). For example, available AD CS certificate templates can be checked via the Certificate Authority MMC snap-in ( certsrv.msc ). certutil.exe can also be used to examine various information within an AD CS CA database. [4] [11] [12] |
| M1042 | Disable or Remove Feature or Program | Consider disabling old/dangerous authentication protocols (e.g. NTLM), as well as unnecessary certificate features, such as potentially vulnerable AD CS web and other enrollment server roles. [4] |
| M1041 | Encrypt Sensitive Information | Ensure certificates as well as associated private keys are appropriately secured. Consider utilizing additional hardware credential protections such as trusted platform modules (TPM) or hardware security modules (HSM). Enforce HTTPS and enable Extended Protection for Authentication. [4] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0240 | Detection Strategy for Steal or Forge Authentication Certificates | AN0671 | Monitor for abnormal certificate enrollment and usage activity in Active Directory Certificate Services (AD CS), registry access to certificate storage locations, and unusual process executions that attempt to export or access private keys. |
| AN0672 | Monitor for file access to certificate directories, commands invoking OpenSSL or PKCS#12 utilities to export or modify certificates, and processes accessing sensitive key storage paths. |  |  |
| AN0673 | Monitor for security commands and API calls interacting with the Keychain, as well as file access attempts to stored certificates and private keys in ~/Library/Keychains or /Library/Keychains. |  |  |
| AN0674 | Monitor for abnormal certificate enrollment events in identity platforms, unexpected use of token-signing certificates, and unusual CA configuration modifications. |  |  |

---

## References

- [Syynimaa, N. (2022, February 15). Stealing and faking Azure AD device identities. Retrieved August 3, 2022.](https://o365blog.com/post/deviceidentity/)
- [Microsoft. (2016, August 31). Active Directory Certificate Services Overview. Retrieved August 2, 2022.](https://docs.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831740(v=ws.11))
- [Thibault Van Geluwe De Berlaere. (2022, November 8). They See Me Roaming: Following APT29 by Taking a Deeper Look at Windows Credential Roaming. Retrieved November 9, 2022.](https://www.mandiant.com/resources/blog/apt29-windows-credential-roaming)
- [Schroeder, W. & Christensen, L. (2021, June 22). Certified Pre-Owned - Abusing Active Directory Certificate Services. Retrieved August 2, 2022.](https://web.archive.org/web/20220818094600/https://specterops.io/assets/resources/Certified_Pre-Owned.pdf)
- [TheWover. (2021, April 21). CertStealer. Retrieved August 2, 2022.](https://github.com/TheWover/CertStealer)
- [HarmJ0y. (2018, August 22). SharpDPAPI - Certificates. Retrieved August 2, 2022.](https://github.com/GhostPack/SharpDPAPI#certificates)
- [Schroeder, W. (2021, June 17). Certified Pre-Owned. Retrieved August 2, 2022.](https://posts.specterops.io/certified-pre-owned-d95910965cd2)
- [Dr. Nestori Syynimaa. (2018, October 25). AADInternals. Retrieved February 18, 2022.](https://o365blog.com/aadinternals)
- [Wolfram, J. et al. (2022, April 28). Trello From the Other Side: Tracking APT29 Phishing Campaigns. Retrieved August 3, 2022.](https://www.mandiant.com/resources/tracking-apt29-phishing-campaigns)
- [Metcalf, S. (2015, November 13). Unofficial Guide to Mimikatz & Command Reference. Retrieved December 23, 2015.](https://adsecurity.org/?page_id=1821)
- [HarmJ0y et al. (2021, June 16). PSPKIAudit. Retrieved August 2, 2022.](https://github.com/GhostPack/PSPKIAudit)
- [HarmJ0y et al. (2021, June 9). Certify. Retrieved August 4, 2022.](https://github.com/GhostPack/Certify/)

---

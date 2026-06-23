# Steal or Forge Kerberos Tickets

## Description

Adversaries may attempt to subvert Kerberos authentication by stealing or forging Kerberos tickets to enable Pass the Ticket . Kerberos is an authentication protocol widely used in modern Windows domain environments. In Kerberos environments, referred to as "realms", there are three basic participants: client, service, and Key Distribution Center (KDC). [1] Clients request access to a service and through the exchange of Kerberos tickets, originating from KDC, they are granted access after having successfully authenticated. The KDC is responsible for both authentication and ticket granting. Adversaries may attempt to abuse Kerberos by stealing tickets or forging tickets to enable unauthorized access.

On Windows, the built-in klist utility can be used to list and analyze cached Kerberos tickets. [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries used the Rubeus tool to forge a Diamond Ticket that is a modified legitimate Kerberos ticket. [3] |
| G1024 | Akira | Akira have used scripts to dump Kerberos authentication credentials. [4] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1015 | Active Directory Configuration | For containing the impact of a previously generated golden ticket, reset the built-in KRBTGT account password twice, which will invalidate any existing golden tickets that have been created with the KRBTGT hash and other Kerberos tickets derived from it. For each domain, change the KRBTGT account password once, force replication, and then change the password a second time. Consider rotating the KRBTGT account password every 180 days. [5] |
| M1047 | Audit | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |
| M1043 | Credential Access Protection | On Linux systems, protect resources with Security Enhanced Linux (SELinux) by defining entry points, process types, and file labels. [6] |
| M1041 | Encrypt Sensitive Information | Enable AES Kerberos encryption (or another stronger encryption algorithm), rather than RC4, where possible. [7] |
| M1027 | Password Policies | Ensure strong password length (ideally 25+ characters) and complexity for service accounts and that these passwords periodically expire. [7] Also consider using Group Managed Service Accounts or another third party product such as password vaulting. [7] |
| M1026 | Privileged Account Management | Limit domain admin account permissions to domain controllers and limited servers. Delegate other admin functions to separate accounts. Limit service accounts to minimal required privileges, including membership in privileged groups such as Domain Administrators. [7] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0522 | Detect Kerberos Ticket Theft or Forgery (T1558) | AN1443 | Detects anomalous Kerberos activity such as forged or stolen tickets by correlating malformed fields in logon events, RC4-encrypted TGTs, or TGS requests without corresponding TGT requests. Also detects suspicious processes accessing LSASS memory for ticket extraction. |
| AN1444 | Detects suspicious access to SSSD secrets database and Kerberos key material indicating ticket theft or replay attempts. Correlates anomalous file access with unusual Kerberos service ticket requests. |  |  |
| AN1445 | Detects attempts to forge or replay Kerberos tickets by monitoring Unified Logs for anomalous kinit/klist activity and correlating unusual authentication sequences. |  |  |

---

## References

- [Sean Metcalf. (2014, September 12). Kerberos, Active Directory’s Secret Decoder Ring. Retrieved February 27, 2020.](https://adsecurity.org/?p=227)
- [Microsoft. (2021, March 3). klist. Retrieved October 14, 2021.](https://docs.microsoft.com/windows-server/administration/windows-commands/klist)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Nutland, J. and Szeliga, M. (2024, October 21). Akira ransomware continues to evolve. Retrieved December 10, 2024.](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
- [UCF. (n.d.). The password for the krbtgt account on a domain must be reset at least every 180 days. Retrieved November 5, 2020.](https://www.stigviewer.com/stig/windows_server_2016/2019-12-12/finding/V-91779)
- [Tim Wadhwa-Brown. (2018, November). Where 2 worlds collide Bringing Mimikatz et al to UNIX. Retrieved October 13, 2021.](https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf)
- [Metcalf, S. (2015, December 31). Cracking Kerberos TGS Tickets Using Kerberoast – Exploiting Kerberos to Compromise the Active Directory Domain. Retrieved March 22, 2018.](https://adsecurity.org/?p=2293)

---

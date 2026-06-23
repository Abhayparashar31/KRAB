# Trusted Relationship

## Description

Adversaries may breach or otherwise leverage organizations who have access to intended victims. Access through trusted third party relationship abuses an existing connection that may not be protected or receives less scrutiny than standard mechanisms of gaining access to a network.

Organizations often grant elevated access to second or third-party external providers in order to allow them to manage internal systems as well as cloud-based environments. Some examples of these relationships include IT services contractors, managed security providers, infrastructure contractors (e.g. HVAC, elevators, physical security). The third-party provider's access may be intended to be limited to the infrastructure being maintained, but may exist on the same network as the rest of the enterprise. As such, Valid Accounts used by the other party for access to internal network systems may be compromised and used. [1]

In Office 365 environments, organizations may grant Microsoft partners or resellers delegated administrator permissions. By compromising a partner or reseller account, an adversary may be able to leverage existing delegated administrator relationships or send new delegated administrator offers to clients in order to gain administrative control over the victim tenant. [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0007 | APT28 | Once APT28 gained access to the DCCC network, the group then proceeded to use that access to compromise the DNC network. [3] |
| G0016 | APT29 | APT29 has compromised IT, cloud services, and managed services providers to gain broad access to multiple customers for subsequent operations. [4] |
| G0115 | GOLD SOUTHFIELD | GOLD SOUTHFIELD has breached Managed Service Providers (MSP's) to deliver malware to MSP customers. [5] |
| G0125 | HAFNIUM | HAFNIUM has used stolen API keys and credentials associated with privilege access management (PAM), cloud app providers, and cloud data management companies to access downstream customer environments. [6] |
| G1004 | LAPSUS$ | LAPSUS$ has accessed internet-facing identity providers such as Azure Active Directory and Okta to target specific organizations. [7] |
| G0045 | menuPass | menuPass has used legitimate access granted to Managed Service Providers in order to access victims of interest. [8] [9] [10] [11] [12] |
| G1005 | POLONIUM | POLONIUM has used compromised credentials from an IT company to target downstream customers including a law firm and aviation company. [13] |
| G1039 | RedCurl | RedCurl has gained access to a contractor to pivot to the victim’s infrastructure. [14] |
| G0034 | Sandworm Team | Sandworm Team has used dedicated network connections from one victim organization to gain unauthorized access to a separate organization. [15] Additionally, Sandworm Team has accessed Internet service providers and telecommunication entities that provide mobile connectivity. [16] |
| G1041 | Sea Turtle | Sea Turtle targeted third-party entities in trusted relationships with primary targets to ultimately achieve access at primary targets. Entities targeted included DNS registrars, telecommunication companies, and internet service providers. [17] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 gained access through compromised accounts at cloud solution partners, and used compromised certificates issued by Mimecast to authenticate to Mimecast customer systems. [18] [19] |
| G0027 | Threat Group-3390 | Threat Group-3390 has compromised third party service providers to gain access to victim's environments. [20] |
| G1055 | VOID MANTICORE | VOID MANTICORE has targeted IT and service providers in an effort to obtain credentials, relying largely on compromised VPN accounts for initial access. [21] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1032 | Multi-factor Authentication | Require MFA for all delegated administrator accounts. [22] |
| M1030 | Network Segmentation | Network segmentation can be used to isolate infrastructure components that do not require broad network access. |
| M1018 | User Account Management | Properly manage accounts and permissions used by parties in trusted relationships to minimize potential abuse by the party and if the party is compromised by an adversary. In Office 365 environments, partner relationships and roles can be viewed under the "Partner Relationships" page. [23] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0488 | Detect abuse of Trusted Relationships (third-party and delegated admin access) | AN1344 | Behavioral chain: (1) a login from a third-party account or untrusted source network establishes an interactive/remote session; (2) the session acquires elevated privileges or accesses sensitive resources atypical for that account; (3) subsequent lateral movement or data access occurs from the same session/device. Correlate Windows logon events, token elevation/privileged use, and resource access with third-party context. |
| AN1345 | Behavioral chain: (1) sshd or federated SSO logins from third-party networks or identities; (2) rapid sudo/su privilege elevation; (3) access to sensitive paths or east-west SSH. Correlate auth logs, process execution, and network flows. |  |  |
| AN1346 | Behavioral chain: (1) third-party interactive login or mobileconfig-based device enrollment; (2) privilege use or admin group change; (3) lateral movement mounts/ssh. Correlate unified logs and network telemetry. |  |  |
| AN1347 | Behavioral chain: (1) delegated admin or external identity establishes session (e.g., partner/reseller DAP, B2B guest, SAML/OAuth trust); (2) role elevation or app consent/permission grant; (3) downstream privileged actions in the tenant. Correlate IdP sign-in, admin/role assignment, and consent/admin-on-behalf events. |  |  |
| AN1348 | Behavioral chain: (1) cross-account or third-party principal assumes a role into the tenant/subscription/project; (2) privileged API calls are made in short succession; (3) access originates from unfamiliar networks or geos. Correlate assume-role/federation events with sensitive API usage. |  |  |
| AN1349 | Behavioral chain: (1) third-party app or admin connects via OAuth/marketplace install; (2) high-privilege scopes granted; (3) anomalous actions (mass read/exports, admin changes). |  |  |
| AN1350 | Behavioral chain: (1) delegated administration offers/relationships created or modified by partner tenants; (2) mailbox delegation/impersonation enabled; (3) follow-on access from partner IPs. |  |  |

---

## References

- [CISA. (n.d.). APTs Targeting IT Service Provider Customers. Retrieved November 16, 2020.](https://us-cert.cisa.gov/APTs-Targeting-IT-Service-Provider-Customers)
- [Microsoft. (n.d.). Partners: Offer delegated administration. Retrieved May 27, 2022.](https://support.microsoft.com/en-us/topic/partners-offer-delegated-administration-26530dc0-ebba-415b-86b1-b55bc06b073e?ui=en-us&rs=en-us&ad=us)
- [Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved November 17, 2024.](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)
- [Microsoft Threat Intelligence Center. (2021, October 25). NOBELIUM targeting delegated administrative privileges to facilitate broader attacks. Retrieved March 25, 2022.](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks/)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [Microsoft Threat Intelligence . (2025, March 5). Silk Typhoon targeting IT supply chain. Retrieved March 20, 2025.](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/)
- [MSTIC, DART, M365 Defender. (2022, March 24). DEV-0537 Criminal Actor Targeting Organizations for Data Exfiltration and Destruction. Retrieved May 17, 2022.](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [FireEye iSIGHT Intelligence. (2017, April 6). APT10 (MenuPass Group): New Tools, Global Campaign Latest Manifestation of Longstanding Threat. Retrieved June 29, 2017.](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)
- [Symantec. (2020, November 17). Japan-Linked Organizations Targeted in Long-Running and Sophisticated Attack Campaign. Retrieved December 17, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)
- [United States District Court Southern District of New York (USDC SDNY) . (2018, December 17). United States of America v. Zhu Hua and Zhang Shilong. Retrieved April 17, 2019.](https://www.justice.gov/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion)
- [US District Court Southern District of New York. (2018, December 17). United States v. Zhu Hua Indictment. Retrieved December 17, 2020.](https://www.justice.gov/opa/page/file/1122671/download)
- [Microsoft. (2022, June 2). Exposing POLONIUM activity and infrastructure targeting Israeli organizations. Retrieved July 1, 2022.](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
- [Antoniuk, D. (2023, July 17). RedCurl hackers return to spy on 'major Russian bank,' Australian company. Retrieved August 9, 2024.](https://therecord.media/redcurl-hackers-russian-bank-australian-company)
- [Scott W. Brady. (2020, October 15). United States vs. Yuriy Sergeyevich Andrienko et al.. Retrieved November 25, 2020.](https://www.justice.gov/opa/press-release/file/1328521/download)
- [Roncone, G. et al. (n.d.). APT44: Unearthing Sandworm. Retrieved July 11, 2024.](https://services.google.com/fh/files/misc/apt44-unearthing-sandworm.pdf)
- [Cisco Talos. (2019, April 17). Sea Turtle: DNS Hijacking Abuses Trust In Core Internet Service. Retrieved November 20, 2024.](https://blog.talosintelligence.com/seaturtle/)
- [NCSC, CISA, FBI, NSA. (2021, May 7). Further TTPs associated with SVR cyber actors. Retrieved July 29, 2021.](https://www.ncsc.gov.uk/files/Advisory-further-TTPs-associated-with-SVR-cyber-actors.pdf)
- [CrowdStrike. (2022, January 27). Early Bird Catches the Wormhole: Observations from the StellarParticle Campaign. Retrieved February 7, 2022.](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)
- [Global Threat Center, Intelligence Team. (2020, December). APT27 Turns to Ransomware. Retrieved November 12, 2021.](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
- [Check Point Research. (2026, March 12). “Handala Hack” – Unveiling Group’s Modus Operandi. Retrieved April 20, 2026.](https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/)
- [Microsoft Threat Intelligence Center. (2021, October 25). NOBELIUM targeting delegated administrative privileges to facilitate broader attacks. Retrieved January 31, 2022.](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks)
- [Microsoft. (2022, March 4). Manage partner relationships. Retrieved May 27, 2022.](https://docs.microsoft.com/en-us/microsoft-365/commerce/manage-partners?view=o365-worldwide)

---

# Acquire Infrastructure

## Description

Adversaries may buy, lease, rent, or obtain infrastructure that can be used during targeting. A wide variety of infrastructure exists for hosting and orchestrating adversary operations. Infrastructure solutions include physical or cloud servers, domains, and third-party web services. [1] Some infrastructure providers offer free trial periods, enabling infrastructure acquisition at limited to no cost. [2] Additionally, botnets are available for rent or purchase.

Use of these infrastructure solutions allows adversaries to stage, launch, and execute operations. Solutions may help adversary operations blend in with traffic that is seen as normal, such as contacting third-party web services or acquiring infrastructure to support Proxy , including from residential proxy services. [3] [4] [5] Depending on the implementation, adversaries may use infrastructure that makes it difficult to physically tie back to them as well as utilize infrastructure that can be rapidly provisioned, modified, and shut down.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1030 | Agrius | Agrius typically uses commercial VPN services for anonymizing last-hop traffic to victim networks, such as ProtonVPN. [6] |
| G1052 | Contagious Interview | Contagious Interview has used services such as Astrill VPN. [7] [8] |
| G1003 | Ember Bear | Ember Bear uses services such as IVPN, SurfShark, and Tor to add anonymization to operations. [9] |
| G0119 | Indrik Spider | Indrik Spider has purchased access to victim VPNs to facilitate access to victim environments. [10] |
| G0094 | Kimsuky | Kimsuky has used funds from stolen and laundered cryptocurrency to acquire operational infrastructure. [11] |
| G0034 | Sandworm Team | Sandworm Team used various third-party email campaign management services to deliver phishing emails. [12] |
| G1041 | Sea Turtle | Sea Turtle accessed victim networks from VPN service provider networks. [13] |
| G1033 | Star Blizzard | Star Blizzard has used HubSpot and MailerLite marketing platform services to hide the true sender of phishing emails. [14] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0895 | Detection of Acquire Infrastructure | AN2027 | Monitor for contextual data about an Internet-facing resource gathered from a scan, such as running services or ports that may buy, lease, or rent infrastructure that can be used during targeting. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. Once adversaries have provisioned infrastructure (ex: a server for use in command and control), internet scans may help proactively discover adversary acquired infrastructure. Consider looking for identifiable patterns such as services listening, certificates in use, SSL/TLS negotiation features, or other response artifacts associated with adversary C2 software. [15] [16] [17] Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. Monitor for queried domain name system (DNS) registry data that may buy, lease, or rent infrastructure that can be used during targeting. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. Monitor for logged domain name system (DNS) data that may buy, lease, or rent infrastructure that can be used during targeting. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. Consider use of services that may aid in tracking of newly acquired infrastructure, such as WHOIS databases for domain registration information. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. |

---

## References

- [Max Goncharov. (2015, July 15). Criminal Hideouts for Lease: Bulletproof Hosting Services. Retrieved March 6, 2017.](https://documents.trendmicro.com/assets/wp/wp-criminal-hideouts-for-lease.pdf)
- [Gamazo, William. Quist, Nathaniel.. (2023, January 5). PurpleUrchin Bypasses CAPTCHA and Steals Cloud Platform Resources. Retrieved February 28, 2024.](https://unit42.paloaltonetworks.com/purpleurchin-steals-cloud-resources/)
- [Amnesty International Security Lab. (2021, July 18). Forensic Methodology Report: How to catch NSO Group’s Pegasus. Retrieved February 22, 2022.](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/)
- [FBI. (2022, August 18). Proxies and Configurations Used for Credential Stuffing Attacks on Online Customer Accounts . Retrieved July 6, 2023.](https://www.ic3.gov/Media/News/2022/220818.pdf)
- [Douglas Bienstock. (2022, August 18). You Can’t Audit Me: APT29 Continues Targeting Microsoft 365. Retrieved February 23, 2023.](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [Aleksandar Milenkoski, Sreekar Madabushi, Kenneth Kinion. (2025, September 4). Contagious Interview | North Korean Threat Actors Reveal Plans and Ops by Abusing Cyber Intel Platforms. Retrieved October 20, 2025.](https://www.sentinelone.com/labs/contagious-interview-threat-actors-scout-cyber-intel-platforms-reveal-plans-and-ops/)
- [Insikt Group. (2025, February 13). Inside the Scam: North Korea’s IT Worker Threat. Retrieved October 17, 2025.](https://www.recordedfuture.com/research/inside-the-scam-north-koreas-it-worker-threat)
- [Microsoft Threat Intelligence. (2023, June 14). Cadet Blizzard emerges as a novel and distinct Russian threat actor. Retrieved July 10, 2023.](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)
- [Mandiant Intelligence. (2022, June 2). To HADES and Back: UNC2165 Shifts to LOCKBIT to Evade Sanctions. Retrieved July 29, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)
- [Mandiant. (2024, March 14). APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations. Retrieved May 3, 2024.](https://services.google.com/fh/files/misc/apt43-report-en.pdf)
- [Billy Leonard. (2023, April 19). Ukraine remains Russia’s biggest cyber focus in 2023. Retrieved March 1, 2024.](https://blog.google/threat-analysis-group/ukraine-remains-russias-biggest-cyber-focus-in-2023/)
- [Hunt & Hackett Research Team. (2024, January 5). Turkish espionage campaigns in the Netherlands. Retrieved November 20, 2024.](https://www.huntandhackett.com/blog/turkish-espionage-campaigns)
- [Microsoft Threat Intelligence. (2023, December 7). Star Blizzard increases sophistication and evasion in ongoing attacks. Retrieved February 13, 2024.](https://www.microsoft.com/en-us/security/blog/2023/12/07/star-blizzard-increases-sophistication-and-evasion-in-ongoing-attacks/)
- [ThreatConnect. (2020, December 15). Infrastructure Research and Hunting: Boiling the Domain Ocean. Retrieved October 12, 2021.](https://threatconnect.com/blog/infrastructure-research-hunting/)
- [Stephens, A. (2020, July 13). SCANdalous! (External Detection Using Network Scan Data and Automation). Retrieved November 17, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/scandalous-external-detection-using-network-scan-data-and-automation/)
- [Koczwara, M. (2021, September 7). Hunting Cobalt Strike C2 with Shodan. Retrieved October 12, 2021.](https://michaelkoczwara.medium.com/cobalt-strike-c2-hunting-with-shodan-c448d501a6e2)

---

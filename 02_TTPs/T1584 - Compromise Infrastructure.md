# Compromise Infrastructure

## Description

Adversaries may compromise third-party infrastructure that can be used during targeting. Infrastructure solutions include physical or cloud servers, domains, network devices, and third-party web and DNS services. Instead of buying, leasing, or renting infrastructure an adversary may compromise infrastructure and use it during other phases of the adversary lifecycle. [1] [2] [3] [4] Additionally, adversaries may compromise numerous machines to form a botnet they can leverage.

Use of compromised infrastructure allows adversaries to stage, launch, and execute operations. Compromised infrastructure can help adversary operations blend in with traffic that is seen as normal, such as contact with high reputation or trusted sites. For example, adversaries may leverage compromised infrastructure (potentially also in conjunction with Digital Certificates ) to further blend in and support staged information gathering and/or Phishing campaigns. [5] Adversaries may also compromise numerous machines to support Proxy and/or proxyware services or to form a botnet. [6] [7] Additionally, adversaries may compromise infrastructure residing in close proximity to a target in order to gain Initial Access via Wi-Fi Networks . [8]

By using compromised infrastructure, adversaries may enable follow-on malicious operations. Prior to targeting, adversaries may also compromise the infrastructure of other adversaries. [9]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0051 | APT28 Nearest Neighbor Campaign | During APT28 Nearest Neighbor Campaign , APT28 compromised third-party infrastructure in physical proximity to targets of interest for follow-on activities. [8] |
| C0043 | Indian Critical Infrastructure Intrusions | Indian Critical Infrastructure Intrusions included the use of compromised infrastructure, such as DVR and IP camera devices, for command and control purposes in ShadowPad activity. [10] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1056 | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0885 | Detection of Compromise Infrastructure | AN2017 | Once adversaries have provisioned compromised infrastructure (ex: a server for use in command and control), internet scans may help proactively discover compromised infrastructure. Consider looking for identifiable patterns such as services listening, certificates in use, SSL/TLS negotiation features, or other response artifacts associated with adversary C2 software. [11] [12] [13] Consider monitoring for anomalous changes to domain registrant information and/or domain resolution information that may indicate the compromise of a domain. Efforts may need to be tailored to specific domains of interest as benign registration and resolution changes are a common occurrence on the internet. Monitor for queried domain name system (DNS) registry data that may compromise third-party infrastructure that can be used during targeting. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. Monitor for logged domain name system (DNS) data that may compromise third-party infrastructure that can be used during targeting. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. Monitor for contextual data about an Internet-facing resource gathered from a scan, such as running services or ports that may compromise third-party infrastructure that can be used during targeting. Detection efforts may be focused on related stages of the adversary lifecycle, such as during Command and Control. |

---

## References

- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [ICANN Security and Stability Advisory Committee. (2005, July 12). Domain Name Hijacking: Incidents, Threats, Risks and Remediation. Retrieved November 17, 2024.](https://www.icann.org/en/ssac/registration-services/documents/sac-007-domain-name-hijacking-incidents-threats-risks-and-remediation-12-07-2005-en)
- [Mercer, W., Rascagneres, P. (2018, November 27). DNSpionage Campaign Targets Middle East. Retrieved October 9, 2020.](https://blog.talosintelligence.com/2018/11/dnspionage-campaign-targets-middle-east.html)
- [Winters, R. (2015, December 20). The EPS Awakens - Part 2. Retrieved January 22, 2016.](https://web.archive.org/web/20151226205946/https://www.fireeye.com/blog/threat-research/2015/12/the-eps-awakens-part-two.html)
- [Hirani, M., Jones, S., Read, B. (2019, January 10). Global DNS Hijacking Campaign: DNS Record Manipulation at Scale. Retrieved October 9, 2020.](https://www.fireeye.com/blog/threat-research/2019/01/global-dns-hijacking-campaign-dns-record-manipulation-at-scale.html)
- [Amnesty International Security Lab. (2021, July 18). Forensic Methodology Report: How to catch NSO Group’s Pegasus. Retrieved February 22, 2022.](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/)
- [Crystal Morin. (2023, April 4). Proxyjacking has Entered the Chat. Retrieved July 6, 2023.](https://sysdig.com/blog/proxyjacking-attackers-log4j-exploited/)
- [Koessel, Sean. Adair, Steven. Lancaster, Tom. (2024, November 22). The Nearest Neighbor Attack: How A Russian APT Weaponized Nearby Wi-Fi Networks for Covert Access. Retrieved February 25, 2025.](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)
- [NSA/NCSC. (2019, October 21). Cybersecurity Advisory: Turla Group Exploits Iranian APT To Expand Coverage Of Victims. Retrieved October 16, 2020.](https://media.defense.gov/2019/Oct/18/2002197242/-1/-1/0/NSA_CSA_Turla_20191021%20ver%204%20-%20nsa.gov.pdf)
- [Recorded Future Insikt Group. (2022, April 6). Continued Targeting of Indian Power Grid Assets by Chinese State-Sponsored Activity Group. Retrieved November 21, 2024.](https://go.recordedfuture.com/hubfs/reports/ta-2022-0406.pdf)
- [ThreatConnect. (2020, December 15). Infrastructure Research and Hunting: Boiling the Domain Ocean. Retrieved October 12, 2021.](https://threatconnect.com/blog/infrastructure-research-hunting/)
- [Stephens, A. (2020, July 13). SCANdalous! (External Detection Using Network Scan Data and Automation). Retrieved November 17, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/scandalous-external-detection-using-network-scan-data-and-automation/)
- [Koczwara, M. (2021, September 7). Hunting Cobalt Strike C2 with Shodan. Retrieved October 12, 2021.](https://michaelkoczwara.medium.com/cobalt-strike-c2-hunting-with-shodan-c448d501a6e2)

---

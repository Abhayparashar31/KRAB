# Cloud Service Dashboard

## Description

An adversary may use a cloud service dashboard GUI with stolen credentials to gain useful information from an operational cloud environment, such as specific services, resources, and features. For example, the GCP Command Center can be used to view all assets, review findings of potential security risks, and run additional queries, such as finding public IP addresses and open ports. [1]

Depending on the configuration of the environment, an adversary may be able to enumerate more information via the graphical dashboard than an API. This also allows the adversary to gain information without manually making any API requests.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1015 | Scattered Spider | Scattered Spider abused AWS Systems Manager Inventory to identify targets on the compromised network prior to lateral movement. [2] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1018 | User Account Management | Enforce the principle of least-privilege by limiting dashboard visibility to only the resources required. This may limit the discovery value of the dashboard in the event of a compromised account. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0291 | Detection of Cloud Service Dashboard Usage via GUI-Based Cloud Access | AN0808 | Detects web console login events followed by read-only or metadata retrieval activity from GUI sources (e.g., browser session, mobile client) rather than API/CLI sources. Correlates across CloudTrail, IAM identity logs, and user-agent context. |
| AN0809 | Detects successful login to cloud identity portals (e.g., Okta, Azure AD, Google Identity) from atypical geolocations, devices, or user agents immediately followed by dashboard/portal navigation to sensitive pages such as user or app configuration. |  |  |
| AN0810 | Detects login to admin consoles (e.g., Microsoft 365 Admin Center) from unrecognized users, devices, or geolocations followed by non-API data review or configuration read actions that suggest GUI dashboard use. |  |  |
| AN0811 | Detects SaaS web login followed by dashboard or web GUI page views from unfamiliar locations, devices, or access patterns. Identifies use of sensitive reporting or configuration consoles accessed from high-risk accounts. |  |  |

---

## References

- [Google. (2019, October 3). Quickstart: Using the dashboard. Retrieved October 8, 2019.](https://cloud.google.com/security-command-center/docs/quickstart-scc-dashboard)
- [CISA. (2023, November 16). Cybersecurity Advisory: Scattered Spider (AA23-320A). Retrieved March 18, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[ShinyHunters]] [related_actor:: [[ShinyHunters]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025-2026 SaaS and Cloud Exploitation Wave]] [related_campaign:: [[2025-2026 SaaS and Cloud Exploitation Wave]]]

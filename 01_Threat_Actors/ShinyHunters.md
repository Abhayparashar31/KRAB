---
entity_type: threat-actor
title: ShinyHunters
aliases:
  - UNC6040
  - UNC6661
  - UNC6671
  - UNC6240
summary: A highly prolific, financially motivated cybercriminal data extortion collective specializing in large-scale data theft, cloud/SaaS platform infiltration, and strategic zero-day vulnerability exploitation.
origin_country: Canada, France
suspected_sponsor: None
attribution_confidence: high
actor_type: criminal
motivation:
  - Financial Gain
  - Extortion
  - Notoriety
sophistication: high
operational_maturity: high
first_seen: 2019-11
last_seen: 2026-06
active: true
targeted_sectors:
  - Higher Education
  - Technology
  - Healthcare
  - Financial Services
  - Retail
  - Telecommunications
  - Entertainment
targeted_regions:
  - Global
  - North America
  - Europe
  - Australia
targeted_platforms:
  - Linux OS
  - Windows OS
  - Cloud SaaS
  - Oracle PeopleSoft
  - Canvas LMS
  - Snowflake
  - Salesforce
campaigns:
  - "[[03_Campaigns/2026 Enterprise LMS and Canvas Data Extortion Campaign]]"
  - "[[03_Campaigns/2026 Oracle PeopleSoft Mass Data Theft Campaign]]"
  - "[[03_Campaigns/2025-2026 SaaS and Cloud Exploitation Wave]]"
malware_used:
  - "[[04_Malware/MeshCentral]]"
  - "[[04_Malware/Lumma Stealer]]"
  - "[[04_Malware/Vidar Stealer]]"
ttps:
  - "[[02_TTPs/T1190 - Exploit Public-Facing Application]]"
  - "[[02_TTPs/T1566.003 - Phishing- Spearphishing SMS]]"
  - "[[02_TTPs/T1059 - Command and Scripting Interpreter]]"
  - "[[02_TTPs/T1219 - Remote Access Software]]"
  - "[[02_TTPs/T1068 - Exploitation for Privilege Escalation]]"
  - "[[02_TTPs/T1562 - Impair Defenses]]"
  - "[[02_TTPs/T1078 - Valid Accounts]]"
  - "[[02_TTPs/T1621 - Multi-Factor Authentication Request Generation]]"
  - "[[02_TTPs/T1538 - Cloud Service Dashboard]]"
  - "[[02_TTPs/T1021 - Remote Services]]"
  - "[[02_TTPs/T1114 - Email Collection]]"
  - "[[02_TTPs/T1567.002 - Exfiltration Over Web Service- Exfiltration to Cloud Storage]]"
  - "[[02_TTPs/T1486 - Data Encrypted for Impact]]"
vulnerabilities_exploited:
  - "[[05_Vulnerabilities/CVE-2026-35273]]"
infrastructure:
  - "[[06_IOCs/azurenetfiles[.]net]]"
iocs:
  - "[[06_IOCs/176.120.22.24]]"
  - "[[06_IOCs/142.11.200.186]]"
  - "[[06_IOCs/108.174.202.99]]"
  - "[[06_IOCs/azurenetfiles[.]net]]"
related_threat_actors:
  - "[[01_Threat_Actors/Scattered Spider]]"
  - "[[01_Threat_Actors/Lapsus$]]"
related_collections: []
detection_opportunities:
  - Monitor for unauthorized outbound TCP port 445 traffic from ERP/PeopleSoft environments to external destinations.
  - Identify cross-site scripting (XXSS) payload structures in public-facing SaaS applications or learning management systems.
mitigations:
  - Enforce phishing-resistant MFA across all enterprise identity architectures.
  - Apply Oracle out-of-band security patch CPU187 immediately to address PeopleTools vulnerabilities.
references:
  - Mandiant. (2026). ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit.
  - "UltraViolet Cyber. (2026). Threat Advisory: ShinyHunters Canvas Attack."
  - MoxFive. (2026). ShinyHunters Exploits Oracle PeopleSoft Zero-Day CVE-2026-35273.
source_reliability: A - Reliable
information_credibility: 1 - Confirmed by multiple sources
analytic_confidence: high
tlp: TLP:CLEAR
classification: Unclassified
created: 2026-06-22
updated: 2026-06-22
tags:
  - shinyhunters
  - unc6040
  - data-extortion
  - saas-breach
  - peoplesoft
  - canvas
---

# ShinyHunters

## Executive Summary
ShinyHunters is a highly sophisticated, financially motivated cybercriminal data extortion collective that poses a severe threat to global enterprise data storage nodes, software-as-a-service (SaaS) environments, and institutional ERP deployments. The group operates an aggressive "pay-or-leak" monetization model, focusing on high-volume database theft rather than traditional system-wide file encryption. Their strategic significance lies in an operational evolution from standard dark-web data brokering to executing multi-stage network intrusions combining zero-day software exploitation, supply chain infiltration, and high-velocity identity-based social engineering. Their primary targets include higher education, enterprise cloud architectures, health systems, and technology vendors where a single breach can yield multi-organization downstream access.

## Attribution Assessment
The group operates as an independent cybercriminal syndicate with core members historically localized in Canada and France. It is tracked across the security industry under designations including UNC6040, UNC6661, UNC6671, and UNC6240. Despite global law enforcement coordination resulting in the arrest of several key French operators in June 2025, the ShinyHunters moniker continues to function effectively as an active, decentralized brand. Recent intelligence demonstrates an operational convergence, infrastructure sharing, and compound alignment with [[01_Threat_Actors/Scattered Spider]] and remnants of [[01_Threat_Actors/Lapsus$]], confirming the collective's deep integration within the cybercriminal ecosystem known as "The Com."

## Operational Profile
The operational objective of ShinyHunters is the monetization of massive corporate datasets through public data-leak listings and direct executive extortion. Their victimology favors large organizations that aggregate consumer or institutional data, focusing heavily on North American, European, and Australian entities. The group leverages public-facing software vulnerabilities, supply-chain positioning, and automated credential reuse to breach perimeters. Once initial access is achieved, their post-exploitation behavior shifts toward rapid directory mapping, session hijacking, and database staging. If an organization rejects extortion terms, ShinyHunters escalates pressure by weaponizing the victim's public interfaces or distributing sensitive database segments on dark web forums.

## Campaign Activity (Past 14 Months)

* [[03_Campaigns/2026 Enterprise LMS and Canvas Data Extortion Campaign]]
  * **Operational Goal:** Multi-tier institutional data exfiltration and public portal manipulation for ransom escalation.
  * **Description of the Campaign:** In April-May 2026, ShinyHunters compromised Instructure's Canvas platform, affecting 9,000 schools and 275 million users. They exploited XSS flaws in Free-for-Teacher accounts to steal administrative tokens and harvest 3.65 TB of private records. When the vendor refused initial payment, the actors re-entered, defacing portal interfaces with ransom notes during final exams.
  * **Timeframe:** April 2026 – May 2026.
  * **Notable Tradecraft:** Cross-Site Scripting (XSS) token harvesting, administrative session reproduction, and public portal interface defacement.
  * **Targeted Organizations:** Instructure (Canvas LMS), global universities, and K-12 school districts.

* [[03_Campaigns/2026 Oracle PeopleSoft Mass Data Theft Campaign]]
  * **Operational Goal:** Perimeter zero-day exploitation, automated lateral movement, and high-value ERP data harvesting.
  * **Description of the Campaign:** Spanning May-June 2026, ShinyHunters executed an automated campaign targeting Oracle PeopleSoft applications, compromising over 300 instances at 100+ organizations. The actors combined a critical zero-day SSRF vulnerability with post-compromise lateral automation scripts to systematically harvest administrative configurations and exfiltrate employee, financial, and student data.
  * **Timeframe:** May 2026 – June 2026.
  * **Notable Tradecraft:** Unauthenticated SSRF zero-day exploitation, automated host scanning, and SSH credential spraying.
  * **Targeted Organizations:** Global enterprise business services, higher education institutions, and payroll networks.

* [[03_Campaigns/2025-2026 SaaS and Cloud Exploitation Wave]]
  * **Operational Goal:** Cross-SaaS boundary exploitation, session hijacking, and joint-actor extortion waves.
  * **Description of the Campaign:** Initiated in mid-2025 and stretching into 2026, this campaign represents a structural merger tracked as "Scattered LAPSUS$ Hunters." The collective specialized in breaking single sign-on constraints and infiltrating multi-tenant repositories. A major incident involved the November 2025 compromise of Mixpanel analytics, allowing downstream extortion against integrated customer platforms.
  * **Timeframe:** April 2025 – Ongoing into June 2026.
  * **Notable Tradecraft:** Third-party vendor smishing, session token manipulation, and interactive helpdesk vishing.
  * **Targeted Organizations:** Mixpanel analytics, Snowflake data cloud environments, Salesforce configurations, and consumer brands.

## Malware & Tooling
* **Remote Access Agents:** The group heavily relies on the deployment of [[04_Malware/MeshCentral]] agent binaries to establish stable, long-term interactive command-and-control loops inside Linux and Windows environments.
* **Information Stealers:** The actors utilize [[04_Malware/Lumma Stealer]] and [[04_Malware/Vidar Stealer]] frameworks via targeted phishing mechanisms to steal initial browser cookie structures and active session IDs.
* **Automation Frameworks:** ShinyHunters deploys custom Bash automation utilities (e.g., `_fanout.sh`) designed to ingest configurations like `/etc/hosts`, automatically verify common administrative usernames (`psoft`, `oracle`, `linuxadm`), and drop unified extortion payloads over SSH.

## Exploited Vulnerabilities

* [[05_Vulnerabilities/CVE-2026-35273]]
  * **Exploitation Purpose:** Remote unauthenticated initial entry point to execute arbitrary command strings.
  * **Exploitation Timing:** Zero-day initial access phase during the May-June 2026 campaign.
  * **Operational Impact:** Enabled complete authentication bypass across the Oracle PeopleSoft Enterprise PeopleTools Environment Management hub, triggering mass data exfiltration and lateral host discovery.

## ATT&CK Tradecraft

### Initial Access
* [[02_TTPs/T1190 - Exploit Public-Facing Application]]: Exploiting remote unauthenticated bugs in ERP setups or XSS flaws within freemium SaaS account configurations.
* [[02_TTPs/T1566.003 - Phishing- Spearphishing SMS]]: Distributing corporate-themed lure messages to intercept secondary validation values and credentials.

### Execution
* [[02_TTPs/T1059 - Command and Scripting Interpreter]]: Utilizing custom shell command infrastructure and Python data parsing utilities to execute local reconnaissance.

### Persistence
* [[02_TTPs/T1219 - Remote Access Software]]: Planting unauthorized open-source monitoring utilities like MeshCentral to retain secondary communication lanes.

### Privilege Escalation
* [[02_TTPs/T1068 - Exploitation for Privilege Escalation]]: Chaining perimeter access vectors with internal authentication configuration flaws to elevate to high-privilege administrative status.

### Defense Evasion
* [[02_TTPs/T1562 - Impair Defenses]]: Forcibly stopping local security audit trails and masking persistent backdoor process names to mirror authorized vendor agents.

### Credential Access
* [[02_TTPs/T1078 - Valid Accounts]]: Repetitive spraying and reuse of default administrative account arrays over internal communication tunnels.
* [[02_TTPs/T1621 - Multi-Factor Authentication Request Generation]]: Flooding targeted mobile apps with authorization push sequences to bypass defensive gates.

### Discovery
* [[02_TTPs/T1538 - Cloud Service Dashboard]]: Navigating structural cloud portals to evaluate target database parameters and configuration paths.

### Lateral Movement
* [[02_TTPs/T1021 - Remote Services]]: Leveraging active internal SSH protocols and shared credential keys to replicate access across adjacent system arrays.

### Collection
* [[02_TTPs/T1114 - Email Collection]]: Scraping central organizational message layers and internal support chat transcripts for sensitive design parameters.

### Exfiltration
* [[02_TTPs/T1567.002 - Exfiltration Over Web Service- Exfiltration to Cloud Storage]]: Ingesting structured file targets into compressed blocks and moving data out via legitimate cloud management tools.

### Impact
* [[02_TTPs/T1486 - Data Encrypted for Impact]]: Executing target hypervisor encryption models if data-only extortion approaches reach a negotiation impasse.

## Infrastructure & IOC Patterns
The group uses a distinct combination of public hosting blocks, residential proxy systems, and lookalike infrastructure. They lease network space across flexible bulletproof providers and frequently route traffic through Tor exit nodes during database discovery stages.
* **Lookalike Domains:** `azurenetfiles[.]net`, `okta-verification-portal[.]com`
* **Network Nodes:** `176.120.22[.]24`, `142.11.200[.]186`, `108.174.202[.]99`

## Detection Engineering Notes

### Behavioral Indicators
* Inbound HTTP configurations targeting sensitive components like `/PSEMHUB/hub` stemming from unverified external networks.
* The presence of anomalous ransom marker text artifacts (e.g., `README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED.TXT`) across centralized web servers.

### Detection Opportunities
* Flag sudden spikes in cross-site script submission formats containing encoded administrative action overrides inside trial account paths.
* Implement network rules that generate critical alerts when application servers trigger unexpected outbound TCP port 445 (SMB) connections to public external spaces.

### Log Sources
* Centralized WebLogic and Application Web Server Logs.
* Cloud Directory Authentication Logs (Okta System Log, Entra ID Sign-ins).
* Host-level process execution command lines.

### Telemetry Requirements
* Continuous capture of outbound endpoint netflow, file creation modifications inside system cache repositories, and API query metadata volume metrics.

## Intelligence Assessment
There is a high level of confidence that ShinyHunters will expand their operation through tactical mergers with loose extortion networks like Scattered Spider. Their structural maturity is high, as evidenced by their transition from basic data theft to automated, wide-scale zero-day deployment campaigns like the Oracle PeopleSoft intrusions of 2026. The group's focus on high-volume shared SaaS structures implies that the impact radius of their campaigns will continue to grow, making proactive identity configuration reviews and application layer hardening critical across all target industries.

## Intelligence Gaps
* The exact organizational pipeline providing the initial validation and employee profiling details used for helpdesk exploitation.
* Full technical insight into potential proprietary binary modification tools used by group affiliates to target hypervisor environments.

## Recommended Defensive Actions

### Immediate
* Apply vendor out-of-band security updates (such as Document ID: CPU187 for Oracle systems) across all accessible perimeters.
* Scan application directories for unauthorized web shell strings or newly created `.jsp` file configurations.

### Tactical
* Block outbound NetBIOS and SMB protocols (Ports 137, 139, 445) from core databases heading to the public internet to mitigate credential capture attempts.
* Mandate phishing-resistant multi-factor authentication (FIDO2 tokens) across all enterprise identity access planes.

### Strategic
* Redesign IT support verification policies, removing public identifiers and adopting cryptographically verified out-of-band authorization steps for credentials.

### Long-Term
* Segment multi-tenant SaaS environments and perform strict least-privilege scoping on third-party API integration layers to prevent a single service exploit from pivoting across downstream clients.

## Related Threat Actors
* [[01_Threat_Actors/Scattered Spider]]: High TTP and infrastructure alignment, collaborating within the joint "Scattered LAPSUS$ Hunters" extortion cluster.
* [[01_Threat_Actors/Lapsus$]]: Strong operational overlap involving targeted identities, communication structures, and rapid extortion processes.

## Sources
Mandiant. (2026). ShinyHunters Targets Education Sector with Oracle PeopleSoft Exploit. Milpitas, CA: Google Cloud.

MoxFive. (2026). ShinyHunters Exploits Oracle PeopleSoft Zero-Day CVE-2026-35273. MoxFive Threat Intelligence.

UltraViolet Cyber. (2026). Threat Advisory: ShinyHunters Canvas Attack. UltraViolet Cyber Security Operations.

## Changelog
* Created: 2026-06-22
* Updated: 2026-06-22
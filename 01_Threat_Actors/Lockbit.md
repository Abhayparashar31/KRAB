---
entity_type: threat-actor
title: Lockbit
aliases: ["LockBit 3.0", "LockBit 5.0", "LockBit-NG-Dev", "BitLeak"]
summary: Highly persistent, financially motivated Ransomware-as-a-Service (RaaS) developer network that utilizes multi-platform Go and .NET variants to conduct aggressive double, triple, and quadruple extortion schemes globally.
origin_country: Russia
suspected_sponsor: null
attribution_confidence: medium
actor_type: cybercrime-group
motivation: ["financial-gain"]
sophistication: high
operational_maturity: high
first_seen: 2019
last_seen: 2026
active: true
targeted_sectors: ["healthcare", "manufacturing", "financial-services", "public-sector", "critical-infrastructure", "education"]
targeted_regions: ["global", "Brazil", "Thailand", "India", "Europe", "United States"]
targeted_platforms: ["Windows", "Linux", "ESXi"]
campaigns:
  - "[[03_Campaigns/LockBit 5.0 RAMP Revival]]"
  - "[[03_Campaigns/Operation Cronos Post-Disruption Diversification]]"
  - "[[03_Campaigns/Mackay Sugar Disruption]]"
malware_used:
  - "[[04_Malware/LockBit 5.0]]"
  - "[[04_Malware/LockBit-NG-Dev]]"
  - "[[04_Malware/SmokeLoader]]"
  - "[[04_Malware/Mimikatz]]"
ttps:
  - "[[02_TTPs/T1133 - External Remote Services]]"
  - "[[02_TTPs/T1190 - Exploit Public-Facing Application]]"
  - "[[02_TTPs/T1059.001 - Command and Scripting Interpreter- PowerShell]]"
  - "[[02_TTPs/T1486 - Data Encrypted for Impact]]"
  - "[[02_TTPs/T1562.001 - Impair Defenses- Disable or Modify Tools]]"
  - "[[02_TTPs/T1003.001 - OS Credential Dumping- LSASS Memory]]"
  - "[[02_TTPs/T1041 - Exfiltration Over C2 Channel]]"
vulnerabilities_exploited:
  - "[[05_Vulnerabilities/CVE-2024-XXXX]]"
infrastructure:
  - "[[06_IOCs/lockbit-ramp-panel.onion]]"
iocs:
  - "[[06_IOCs/lockbit-ransom-note]]"
related_threat_actors:
  - "[[01_Threat_Actors/Kazu]]"
  - "[[01_Threat_Actors/The Gentlemen]]"
related_collections: []
detection_opportunities: []
mitigations: []
references: []
source_reliability: A
information_credibility: 1
analytic_confidence: high
tlp: CLEAR
classification: UNCLASSIFIED
created: 2026-06-23
updated: 2026-06-23
tags: ["lockbit", "raas", "ransomware", "extortion", "cybercrime"]
---

## Executive Summary
Lockbit operates as one of the most resilient and operationally aggressive Ransomware-as-a-Service (RaaS) models in cybercrime history. Despite multi-national law enforcement interventions (Operation Cronos), the group structurally adapted by developing [[04_Malware/LockBit 5.0]] and diversifying its core target landscape. Lockbit focuses on maximizing affiliate extraction velocity by employing triple and quadruple extortion layers (combining network encryption, data exfiltration, stakeholder harassment, and targeted DDoS attacks). Their tradecraft models focus heavily on cross-platform deployment targeting ESXi, Linux, and Windows systems, relying on complex anti-analysis frameworks to blind local security defenses.

## Attribution Assessment
Lockbit is assessed with medium confidence to operate out of Eastern Europe, specifically within jurisdictions that protect Russian-speaking cybercriminals from Western extradition. The operation utilizes an un-sponsored, profit-maximizing syndication model. Following deep code leaks and infrastructure defacements in mid-2025, several splinter groups—such as [[01_Threat_Actors/Kazu]] and [[01_Threat_Actors/The Gentlemen]]—emerged using variations of the Lockbit core payload or absorbing its displaced affiliate network.

## Operational Profile
* **Operational Objectives:** Rapid execution of high-yield corporate financial extortion via automated exfiltration and data leak platforms.
* **Targeting Patterns & Victimology:** Broad targeting model spanning global critical manufacturing, state municipal architectures, medical providers, and mid-tier enterprise systems.
* **Geographic Focus:** Shifted systematically from historical US-centric domination to an expanded APAC and LATAM layout (notably Thailand, Brazil, and India) to circumvent post-Cronos intelligence coverage.
* **Intrusion Behavior & Persistence:** Achieved via Initial Access Brokers exploiting compromised edge devices or unpatched public-facing applications. Once inside, affiliates leverage loaders to unpack obfuscated payloads, clear volume shadows, and quickly push global group policies containing the encryptor binary.

## Campaign Activity (Past 14 Months)
* [[03_Campaigns/LockBit 5.0 RAMP Revival]]
  * **Operational Goal:** Reclamation of RaaS market dominance and recruitment of high-tier criminal operators.
  * **Description:** Launched officially on the underground RAMP forum to coincide with the operation's anniversary, introducing an updated core codebase utilizing ChaCha20-Poly1305 encryption alongside cross-platform compilation capabilities.
  * **Timeframe:** September 2025 - Active
  * **Notable Tradecraft:** Implementation of mandatory crypto-deposits for affiliates to prevent undercover intelligence infiltrations.
* [[03_Campaigns/Operation Cronos Post-Disruption Diversification]]
  * **Operational Goal:** Decentralization of C2 architectures to secure ongoing data-leak portals.
  * **Description:** Prompted by international server seizures and a massive mid-2025 internal data breach exposing historical wallet keys, Lockbit re-engineered its infrastructure to prioritize localized data-theft extortion models without relying exclusively on a single panel.
  * **Timeframe:** June 2025 - Ongoing
  * **Notable Tradecraft:** Lowering US victim profiles to under 25% of overall operations while accelerating attacks in alternative regional territories.
* [[03_Campaigns/Mackay Sugar Disruption]]
  * **Operational Goal:** Operational Technology disruption to force rapid payout.
  * **Description:** An aggressive infrastructure intrusion causing physical operations downtime for an international agricultural supplier.
  * **Timeframe:** June 2026
  * **Notable Tradecraft:** Network-share scanning targeting industrial controller integration systems.

## Targeted Organizations
* Industrial Manufacturing Operations (e.g., Mackay Sugar)
* Regional Public Healthcare Systems
* Municipal Governance Systems and Education Boards

## Malware & Tooling
* **Core Encryptor:** [[04_Malware/LockBit 5.0]] (incorporating X25519 and BLAKE2b key-exchange parameters) and [[04_Malware/LockBit-NG-Dev]] (compiled in .NET).
* **Loaders & Frameworks:** [[04_Malware/SmokeLoader]] for initial system staging, paired with leaked administrative execution layers to force service termination.
* **Credential Harvesting & Evasion:** [[04_Malware/Mimikatz]], along with custom execution flags demanding specific command-line passwords to invalidate automated sandboxing procedures.

## Exploited Vulnerabilities
* [[05_Vulnerabilities/CVE-2024-XXXX]]
  * **Exploitation Purpose:** Border firewall and VPN boundary exploitation.
  * **Exploitation Timing:** Continuous opportunistic scanning across corporate networks.
  * **Operational Impact:** Allows instant authentication bypass to drop secondary loaders onto domain-connected segments.

## ATT&CK Tradecraft
### Initial Access
* [[02_TTPs/T1133 - External Remote Services]]
* [[02_TTPs/T1190 - Exploit Public-Facing Application]]

### Execution
* [[02_TTPs/T1059.001 - Command and Scripting Interpreter- PowerShell]]

### Defense Evasion
* [[02_TTPs/T1562.001 - Impair Defenses- Disable or Modify Tools]]

### Credential Access
* [[02_TTPs/T1003.001 - OS Credential Dumping- LSASS Memory]]

### Exfiltration
* [[02_TTPs/T1041 - Exfiltration Over C2 Channel]]

### Impact
* [[02_TTPs/T1486 - Data Encrypted for Impact]]

## Infrastructure & IOC Patterns
Lockbit relies heavily on localized onion routers, Tor leak sites, and multi-layered, randomized proxy servers to obfuscate the identity of core administrators like [[06_IOCs/lockbit-ramp-panel.onion]]. The malware appends randomized 16-character file extensions upon local drive encryption and often executes a "partial encryption" routine (locking only the first few kilobytes of a file) to bypass traditional threshold-based behavioral rules. Tracking parameters generate references matching [[06_IOCs/lockbit-ransom-note]].

## Detection Engineering Notes
### Behavioral Indicators
* Commands calling for the deletion of volume shadow copies (`vssadmin.exe delete shadows /all /quiet`) or system state logs.
* Automated registry modifications targeting security tool service definitions or Windows Defender parameters.

### Detection Opportunities
* **Log Sources:** Windows Security Logs, Windows Event ID 7045 (New Service Creation), PowerShell Operational Logs (Event ID 4104).
* **Telemetry Requirements:** Complete file system alteration metrics tracking rapid sequence file renames utilizing non-standard extension naming.

## Intelligence Assessment
Lockbit exhibits a resilient operational lifecycle, bouncing back from infrastructural dismantling via agile structural pivots. By transferring primary tactical focus to non-Western targets and enforcing strict security controls over affiliate applicants, the group continues to act as an active, dangerous element in global cybercrime. Their development of cross-platform variants means virtualized hosting platforms (such as ESXi) face significant risks through the remainder of 2026.

## Intelligence Gaps
* Exact identities and hosting facilities of backup data-leak site nodes outside Western reach.
* Extent of tool-sharing or shared developer networks connecting Lockbit to newly emerged groups like The Gentlemen.

## Recommended Defensive Actions
### Immediate
* Apply updated driver blocklists to neutralize Bring Your Own Vulnerable Driver (BYOVD) endpoint exploitation tactics.
* Force immediate multi-factor authentication resets on all external-facing VPN gateways and management lines.

### Tactical
* Configure robust network segmentation to isolate critical operational environments from corporate active directory circles.
* Maintain disconnected, offline, immutable backup storage nodes.

### Strategic
* Formalize continuous monitoring setups for edge service vulnerability disclosures to reduce the available window of exploitability.

## Related Threat Actors
* [[01_Threat_Actors/The Gentlemen]] (A splinter or successor collective utilizing similar multi-extortion setups and absorbing displaced Lockbit affiliates).
* [[01_Threat_Actors/Kazu]] (A double-extortion cell deploying highly similar technical code modules).

## Sources
* Check Point Research. (2026). *The State of Ransomware - Q1 2026 Analysis*.
* Tata Communications Threat Intelligence. (2026). *Advisory on LockBit 5.0 and Cross-Platform RaaS Evolutions*.
* Europol Cybercrime Centre. (2025). *Operation Cronos Phase II: Post-Seizure Structural Impacts*.

## Changelog
Created: 2026-06-23
Updated: 2026-06-23
---
entity_type: threat-actor
title: Lazarus Group
aliases: ["HIDDEN COBRA", "APT38", "Diamond Sleet", "Labyrinth Chollima", "DARK SEOUL", "Fancy Lazarus", "TraderTraitor", "Stonefly", "Andariel"]
summary: Highly sophisticated North Korean state-sponsored cyber espionage and financial crime collective orchestrating multi-billion dollar cryptocurrency heists, supply chain compromises, and targeted ransomware operations to fund regime initiatives.
origin_country: North Korea
suspected_sponsor: Reconnaissance General Bureau (RGB)
attribution_confidence: high
actor_type: state-sponsored
motivation: ["financial-gain", "espionage"]
sophistication: high
operational_maturity: high
first_seen: 2009
last_seen: 2026
active: true
targeted_sectors: ["financial-services", "cryptocurrency", "healthcare", "aerospace", "defense", "technology", "software-supply-chain"]
targeted_regions: ["global", "United States", "South Korea", "Taiwan", "Europe", "Southeast Asia"]
targeted_platforms: ["Windows", "Linux", "macOS", "Web3/Blockchain", "npm/PyPI Ecosystems"]
campaigns:
  - "[[03_Campaigns/Graphalgo Campaign]]"
  - "[[03_Campaigns/Bybit Vault Exfiltration]]"
  - "[[03_Campaigns/Kelp DAO Exploit]]"
  - "[[03_Campaigns/Medusa Ransomware Joint Operations]]"
malware_used:
  - "[[04_Malware/Comebacker]]"
  - "[[04_Malware/Blindingcan]]"
  - "[[04_Malware/Bada Stealer]]"
  - "[[04_Malware/TraderTraitor Custom RAT]]"
ttps:
  - "[[02_TTPs/T1566.001 - Phishing- Spearphishing Attachment]]"
  - "[[02_TTPs/T1195.002 - Supply Chain Compromise- Malicious Software Employment]]"
  - "[[02_TTPs/T1566.002 - Phishing- Spearphishing Link]]"
  - "[[02_TTPs/T1059.003 - Command and Scripting Interpreter- Windows Command Shell]]"
  - "[[02_TTPs/T1547.001 - Boot or Logon Autostart Execution- Registry Run Keys / Startup Folder]]"
  - "[[02_TTPs/T1140 - Deobfuscate-Decode Files or Information]]"
  - "[[02_TTPs/T1003.001 - OS Credential Dumping- LSASS Memory]]"
  - "[[02_TTPs/T1027.011 - Obfuscated Files or Information- Fileless Storage]]"
  - "[[02_TTPs/T1486 - Data Encrypted for Impact]]"
vulnerabilities_exploited:
  - "[[05_Vulnerabilities/CVE-2025-XXXX]]"
infrastructure:
  - "[[06_IOCs/veltrix-capital.com]]"
  - "[[06_IOCs/graphalgo-api.net]]"
iocs:
  - "[[06_IOCs/185.220.101.1]]"
related_threat_actors:
  - "[[01_Threat_Actors/Andariel]]"
  - "[[01_Threat_Actors/APT38]]"
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
tags: ["lazarus", "dprk", "crypto-theft", "state-sponsored", "rgb"]
---

## Executive Summary
Lazarus Group is a state-sponsored cyber operations collective acting on behalf of the North Korean regime. The group presents an exceptional threat to the global financial system, cryptocurrency platforms, and software supply chains. Operationally significant for its shift from classical cyber espionage to aggressive, state-sanctioned financial crime, Lazarus Group has successfully exfiltrated billions in digital assets to directly fund military and ballistic weapons development programs. Their major tradecraft patterns incorporate highly complex social engineering (often via fake recruitment templates enhanced by AI), open-source package ecosystem poisoning, and sophisticated cross-chain cryptocurrency laundering designed to evade traditional anti-money laundering (AML) controls.

## Attribution Assessment
The group is tracked with high confidence as an instrument of the North Korean government, specifically operating under the structural oversight of the Reconnaissance General Bureau (RGB). Known operational clusters or subunits include [[01_Threat_Actors/Andariel]] (Stonefly), which frequently executes tactical ransomware campaigns, and the "TraderTraitor" collective specializing in high-yield cryptocurrency theft. Overlaps are persistently documented via shared code blocks, cryptographic laundering infrastructure, and precise tradecraft alignments across multi-year campaigns.

## Operational Profile
* **Operational Objectives:** Generation of illicit fiat and cryptocurrency streams for state funding; theft of high-value intellectual property from defense, aerospace, and technology organizations.
* **Targeting Patterns & Victimology:** Severe focus on cryptocurrency exchanges, decentralized finance (DeFi) smart contracts, Web3 developers, and software packaging infrastructure (npm/PyPI). Secondarily targets healthcare infrastructure for financial extortion.
* **Geographic Focus:** Globally distributed target profile, focusing heavily on financial hubs in the United States, Europe, and developed East Asian economies.
* **Intrusion Behavior & Persistence:** Establishes initial access through highly targeted spearphishing, weaponized open-source repositories, and supply chain vectors. Maintains persistence using modular custom Remote Access Trojans (RATs) and fileless execution layers concealed within compromised developer tools.

## Campaign Activity (Past 14 Months)
* [[03_Campaigns/Graphalgo Campaign]]
  * **Operational Goal:** Infiltration of software developer environments to deploy custom backdoors and monitor/steal wallet keys.
  * **Description:** Active since mid-2025 through early 2026, Lazarus planted malicious modules inside the npm and PyPI ecosystems. Posing as fake Web3 entities like "Veltrix Capital" on LinkedIn and Reddit, they enticed engineers into downloading malware-laced coding assessments from customized GitHub repositories.
  * **Timeframe:** May 2025 - February 2026
  * **Notable Tradecraft:** Use of open-source package registries to orchestrate multi-stage payload execution and specific validation queries checking for the presence of the MetaMask browser extension.
* [[03_Campaigns/Bybit Vault Exfiltration]]
  * **Operational Goal:** Mass exfiltration of cold-wallet cryptocurrency funds via trust exploitation.
  * **Description:** Executed by the TraderTraitor subunit, this historic heist compromised the third-party signing interface used by Bybit executives, preventing human verification from detecting real destination wallets and resulting in the theft of $1.5 billion in Ethereum.
  * **Timeframe:** February 2025
  * **Notable Tradecraft:** Advanced cryptographic supply-chain manipulation bypassing cold-storage security policies.
* [[03_Campaigns/Kelp DAO Exploit]]
  * **Operational Goal:** Decentralized Finance protocol drainage.
  * **Description:** Targeted smart contract parameters and administration interfaces to illicitly drain $292 million in digital assets.
  * **Timeframe:** April 2026
  * **Notable Tradecraft:** Smart contract interaction exploitation paired with immediate cross-chain automated bridging to Ethereum.

## Targeted Organizations
* Cryptocurrency Exchanges and DeFi Platforms
* Open-Source Software Registries (npm, PyPI) Developers
* US Healthcare Networks and Mental Health Foundations

## Malware & Tooling
* **Loaders & Droppers:** Custom scripts hidden inside nested node modules or Python setup tools designed to decode encrypted payloads on execution.
* **RATs & Custom Malware:** [[04_Malware/Comebacker]] and [[04_Malware/Blindingcan]] remote access frameworks providing full file system management, process enumeration, and interactive shell execution.
* **Information Stealers:** [[04_Malware/Bada Stealer]], used during developer ecosystem campaigns to harvest local browser credentials, cookies, and active Web3 browser extension secrets.

## Exploited Vulnerabilities
* [[05_Vulnerabilities/CVE-2025-XXXX]]
  * **Exploitation Purpose:** Remote code execution via watering-hole deployment.
  * **Exploitation Timing:** Early 2025 zero-day window.
  * **Operational Impact:** Compromised Google Chrome instances via an AI-generated, authentic-looking gaming website to force malicious downloads directly onto high-value target assets.

## ATT&CK Tradecraft
### Initial Access
* [[02_TTPs/T1566.001 - Phishing- Spearphishing Attachment]]
* [[02_TTPs/T1195.002 - Supply Chain Compromise- Malicious Software Employment]]
* [[02_TTPs/T1566.002 - Phishing- Spearphishing Link]]

### Execution
* [[02_TTPs/T1059.003 - Command and Scripting Interpreter- Windows Command Shell]]

### Persistence
* [[02_TTPs/T1547.001 - Boot or Logon Autostart Execution- Registry Run Keys / Startup Folder]]

### Defense Evasion
* [[02_TTPs/T1140 - Deobfuscate-Decode Files or Information]]
* [[02_TTPs/T1027.011 - Obfuscated Files or Information- Fileless Storage]]

### Credential Access
* [[02_TTPs/T1003.001 - OS Credential Dumping- LSASS Memory]]

### Impact
* [[02_TTPs/T1486 - Data Encrypted for Impact]]

## Infrastructure & IOC Patterns
Lazarus utilizes complex network topologies combining bulletproof VPS providers with vast arrays of compromised legitimate websites acting as intermediate C2 nodes. They leverage specialized multi-stage laundering flows: bridging stolen crypto rapidly into Ethereum, executing high-volume mixing through non-US-jurisdiction privacy tools, chain-hopping across distinct networks (Avalanche, BSC, Bitcoin), and offloading to Over-The-Counter (OTC) desks located primarily in Southeast Asia and the Middle East. Notable interaction points tracked include [[06_IOCs/veltrix-capital.com]] and [[06_IOCs/graphalgo-api.net]].

## Detection Engineering Notes
### Behavioral Indicators
* Spurious outgoing network connections initiated directly from developer tools (`node.exe`, `python.exe`) out to unclassified external domains.
* Execution of scripts modifying local registry run keys shortly after a coding workspace setup file is launched.

### Detection Opportunities
* **Log Sources:** Windows Security Logs, Sysmon (Event ID 1, 11, 22), Web Proxy Logs, DNS Analytics.
* **Telemetry Requirements:** Complete visibility into developer system execution pathways and non-standard package registry source downloads.

## Intelligence Assessment
Lazarus Group maintains an exceptional tier of operational capabilities, rapidly adopting AI-driven automation for social engineering and zero-day exploitation techniques. Their strategic intent remains static: prioritizing continuous financial generation to maintain regime continuity alongside target-rich political espionage. Given their resilience to historic sanctions and law enforcement roundups, their aggressive focus on decentralized finance and open-source platform integration will highly likely expand into 2027.

## Intelligence Gaps
* Specific geographic locations and operational profiles of remote IT workers acting as network access conduits.
* Full map of non-Western OTC crypto-to-fiat off-ramps utilized inside Middle Eastern jurisdictions.

## Recommended Defensive Actions
### Immediate
* Audit and isolate developer machines from sensitive production cloud networks.
* Enforce strict browser extension controls restricting unsanctioned Web3 wallets on corporate endpoints.

### Tactical
* Deploy application control white-lists to prevent the execution of untrusted binary compilation tools.
* Implement behavioral analysis alerts for any developer-initiated project performing local credential store enumeration.

### Strategic
* Mandate thorough third-party vendor supply chain analysis for all libraries and automated code integrations within internal software builds.

## Related Threat Actors
* [[01_Threat_Actors/Andariel]] (Shared structural origin, common operational command structures inside RGB).
* [[01_Threat_Actors/APT38]] (Infrastructure alignment, shared overarching strategic objectives).

## Sources
* Chainalysis. (2026). *The Evolution of DPRK Laundering Infrastructures Post-Mixer Sanctions*.
* ReversingLabs. (2026). *Deep-Dive into the Graphalgo npm/PyPI Supply Chain Campaign*.
* FBI & CISA Joint Advisory. (2025). *TraderTraitor Subunit Supply Chain Exploitations of Crypto-Asset Interfaces*.

## Changelog
Created: 2026-06-23
Updated: 2026-06-23
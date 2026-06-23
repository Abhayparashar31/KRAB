---
entity_type: campaign
title: "MGM Resorts and Caesars Entertainment Extortion Campaign"
aliases: ["MGM Caesars Extortion Blitz", "Las Vegas Ransomware Surge"]
summary: "A landmark cyber extortion campaign that severely disrupted the hospitality and gaming sectors by combining advanced help-desk vishing with the deployment of high-impact locker variants across centralized hypervisor environments."
first_seen: "2023-08-27"
last_seen: "2023-09-20"
status: "Completed"
attribution: "[[01_Threat_Actors/Scattered Spider]]"
attribution_confidence: "high"
targeted_sectors: ["Commercial Facilities", "Financial Services"]
targeted_regions: ["United States"]
targeted_technologies: ["Okta IAM", "VMware ESXi", "Azure AD", "ALPHV Ransomware Core"]
objectives: ["Mass Financial Extortion", "Operational Disruption"]
threat_actors: ["[[01_Threat_Actors/Scattered Spider]]", "[[01_Threat_Actors/ALPHV BlackCat]]"]
malware: ["[[04_Malware/Cobalt Strike]]", "[[04_Malware/Mimikatz]]"]
vulnerabilities: []
ttps: ["[[02_TTPs/T1566.004 - Phishing- Voice Phishing]]", "[[02_TTPs/T1556.006 - Modify Authentication Process- Multi-Factor Authentication]]", "[[02_TTPs/T1486 - Data Encrypted for Impact]]", "[[02_TTPs/T1489 - Service Stop]]"]
related_iocs: []
infection_vectors: ["Help Desk Deception / Vishing", "MFA Fatigue", "Hypervisor Takeover"]
infrastructure_patterns: ["Residential proxy routing spans", "Tor-hosted negotiation rooms"]
victimology: ["Major US-based luxury gaming resorts and hospitality conglomerates running expansive identity federations and central virtualized reservation backends."]
detection_opportunities: ["Sudden help-desk driven password resets on domain admin accounts followed immediately by bulk MFA changes.", "Mass service stop activities on virtual infrastructure management panels."]
mitigations: ["Implement mandatory cryptographic or manager out-of-band validation for all identity resets.", "Enforce strict network isolation boundaries between corporate IAM frameworks and ESXi hosting clusters."]
references: ["Federal Bureau of Investigation. (2023). Scattered Spider Activity in the Gaming Sector.", "Mandiant. (2023). Threat Briefing: Cyber Crime Trends in Hospitality."]
source_reliability: "high"
information_credibility: "high"
analytic_confidence: "high"
tags: ["campaign", "mgm", "caesars", "scattered-spider", "alphv", "vishing", "esxi"]
created: "2026-06-23"
updated: "2026-06-23"
author: "Senior Cyber Threat Intelligence Analyst"
---

# MGM Resorts and Caesars Entertainment Extortion Campaign

## Executive Summary
The MGM Resorts and Caesars Entertainment Extortion Campaign stands as one of the most operationally disruptive cyber extortion events in history, executed by [[01_Threat_Actors/Scattered Spider]] (collaborating under the [[01_Threat_Actors/ALPHV BlackCat]] RaaS model). By combining sophisticated voice phishing (vishing) techniques to trick internal IT help desks with aggressive domain takeover strategies, the threat actors gained full control over the target organizations' Okta and Active Directory identity systems. The subsequent deployment of encryption payloads across central VMware ESXi hypervisors paralyzed hotel reservation engines, slot machines, electronic room keys, and digital payment networks. This campaign highlighted the extreme vulnerability of large enterprises to identity-based attacks that pivot directly into critical operational infrastructure.

## Campaign Overview
The intrusion workflow began with exhaustive research into victim employee profiles via LinkedIn and public data leak repositories. Native English-speaking operators called the target organizations' IT help desks, impersonating high-level administrators to request password and MFA overrides. By leveraging social engineering techniques and pre-acquired PII, the actors successfully bypassed security verification questions.

Once inside the central identity architecture (Okta and Azure AD), the group established persistence by creating rogue administrative accounts and configuring secondary identity provider (`IdP`) trusts. When the victim organizations attempted to isolate the threat by severing the compromised identity access paths, the threat actors used their pre-staged access tokens to pivot directly into the core VMware ESXi virtualized environments. Using native administrative tools, they terminated running virtual machines and deployed custom ransomware variants, causing widespread operational disruption across multiple resort properties.

## Threat Actor Associations
* **[[01_Threat_Actors/Scattered Spider]]**: Planned and executed the initial vishing operations, identity infrastructure takeovers, lateral movement, and negotiation phases.
* **[[01_Threat_Actors/ALPHV BlackCat]]**: Provided the backend ransomware infrastructure, custom encryptor builds, and data leak hosting platforms used to leak victim data.

## Malware & Tooling
* **[[04_Malware/Cobalt Strike]]**: Leveraged extensively as the primary command-and-control framework for interactive post-exploitation and lateral movement.
* **[[04_Malware/Mimikatz]]**: Deployed within local systems to extract active memory credential states and capture domain hashes.
* **ALPHV Locker Build**: A customized ransomware payload written in Rust, optimized for fast file encryption across Linux and VMware ESXi environments.

## Exploited Vulnerabilities
* **None**: The campaign relied entirely on social engineering, credential theft, and the abuse of built-in administrative tools, avoiding the use of software exploits.

## ATT&CK Tradecraft

### Initial Access
* [[02_TTPs/T1566.004 - Phishing- Voice Phishing]]: Executing targeted vishing campaigns against IT help desks to compromise legitimate employee user accounts.

### Execution
* [[02_TTPs/T1059 - Command and Scripting Interpreter]]: Running automated scripts to coordinate internal mapping and clear logs.

### Persistence
* [[02_TTPs/T1556.006 - Modify Authentication Process- Multi-Factor Authentication]]: Configuring rogue MFA tokens and secondary identity sync paths within compromised IAM tenants.

### Defense Evasion
* [[02_TTPs/T1556.006 - Modify Authentication Process- Multi-Factor Authentication]]: Utilizing legitimate, modified administrative configurations to hide malicious lateral movement from security detection tools.

### Credential Access
* [[02_TTPs/T1003 - OS Credential Dumping]]: Extracting active administrative passwords and session hashes from local memory spaces.

### Discovery
* [[02_TTPs/T1046 - Network Service Discovery]]: Mapping connected virtual machine clusters, storage networks, and hypervisor management dashboards.

### Lateral Movement
* [[02_TTPs/T1021.001 - Remote Services- Remote Desktop Protocol]]: Pivoting across internal subnets using valid administrative credentials.

### Impact
* [[02_TTPs/T1486 - Data Encrypted for Impact]]: Deploying customized ransomware payloads across the core storage engines of central hypervisor farms.
* [[02_TTPs/T1489 - Service Stop]]: Terminating active virtual machine instances to ensure complete lock cycles on underlying server arrays.

## Infrastructure & IOC Patterns
The threat actors routed their administrative interactions through commercial residential proxy pools, making malicious traffic blend in with normal remote employee login locations. Extortion negotiations and proof of data theft were handled via private Tor communication sites.

## Victimology
The campaign targeted major US hospitality and gaming giants on the Las Vegas Strip that operate highly integrated, low-downtime customer service environments, reservation platforms, and digital payment systems.

## Detection & Hunting

### Behavioral Indicators
* Help-desk accounts executing password overrides on administrative profiles, immediately followed by the registration of new authentication devices from unexpected residential network locations.
* Volumetric process shutdowns on hypervisors followed by immediate file extension renames across `.vmdk` assets.

### Detection Opportunities
* Monitor identity provider logs for anomalous modifications to cross-tenant trust settings or the unexpected creation of new administrative profiles.

### Log Sources
* Okta System Logs and Azure AD Audit records.
* VMware ESXi `hostd` and `syslog` audit trails.
* Windows Event Logs (specifically tracking Event IDs 4624 and 7045).

### Telemetry Requirements
* Comprehensive capture of authentication source locations, identity configuration modifications, and hypervisor command histories.

### Hunt Ideas
* Search for instances where an administrative identity suddenly logs in from a new residential network span and begins enumerating virtual machine cluster details.

## Intelligence Assessment
The MGM and Caesars Entertainment Campaign demonstrated the significant threat that identity-focused threat actors pose to enterprise networks. By targeting human verification weaknesses at the help desk and leveraging misconfigured identity permissions, [[01_Threat_Actors/Scattered Spider]] successfully bypassed advanced endpoint defenses to disrupt critical business operations. This campaign established a tactical model for identity takeover and hypervisor disruption that continues to influence modern cybercrime operations.

## Mitigations

### Immediate
* Require strict, out-of-band secondary verification (such as video or manager sign-off) for all help-desk driven password and MFA resets.
* Audit all active administrative accounts and cross-tenant configurations within cloud identity environments.

### Tactical
* Enforce phishing-resistant FIDO2 hardware keys across all administrative and help-desk personnel profiles.
* Isolate hypervisor management interfaces behind dedicated, firewalled jump hosts that require multi-factor authentication.

### Strategic
* Transition toward an Identity Zero-Trust framework that continuously validates user context, device health, and network behavior to detect and block session hijacking attempts.

## Sources
Federal Bureau of Investigation. (2023). *Cyber Criminal Elements Target Hospitality and Gaming Sectors via Advanced Vishing (Advisory BC-23-11A)*. FBI Cyber Division.

Mandiant. (2023). *Scattered Spider: Inside the Identity-Centric Attacks Disrupting the Service Sector*. Milpitas, CA: Google Cloud.

## Changelog
* Created: 2026-06-23
* Updated: 2026-06-23
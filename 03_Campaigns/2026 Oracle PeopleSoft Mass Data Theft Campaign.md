---
entity_type: campaign
title: "2026 Oracle PeopleSoft Mass Data Theft Campaign"
aliases: ["PeopleSoft Data Theft Wave 2026"]
summary: "A targeted cyber crime campaign focusing on the compromise and mass data extraction of corporate payroll, human resources, and financial directories via session hijacking and administrative credential abuse within Oracle PeopleSoft ERP deployments."
first_seen: "2026-03-02"
last_seen: "2026-06-23"
status: "Active"
attribution: "[[01_Threat_Actors/Scattered Lapsus$ Hunters]]"
attribution_confidence: "medium"
targeted_sectors: ["Financial Services", "Healthcare", "Government Facilities", "Technology"]
targeted_regions: ["United States", "United Kingdom", "France"]
targeted_technologies: ["Oracle PeopleSoft ERP", "PeopleTools", "SQL Databases"]
objectives: ["Financial Data Theft", "Corporate Extortion"]
threat_actors: ["[[01_Threat_Actors/Scattered Lapsus$ Hunters]]"]
malware: []
vulnerabilities: []
ttps: ["[[02_TTPs/T1078 - Valid Accounts]]", "[[02_TTPs/T1539 - Steal Web Session Cookie]]", "[[02_TTPs/T1119 - Automated Collection]]", "[[02_TTPs/T1020 - Automated Exfiltration]]"]
related_iocs: []
infection_vectors: ["Session Hijacking", "Credential Stuffing"]
infrastructure_patterns: ["Commercial cloud staging architectures", "Encrypted underground distribution panels"]
victimology: ["Large corporate entities and public sector frameworks relying on legacy or cloud-migrated Oracle PeopleSoft environments for core HR, payroll, and internal resource management operations."]
detection_opportunities: ["Atypical administrative database queries targeting full payroll records.", "Active PeopleSoft web console connections initiated from unexpected external network domains."]
mitigations: ["Enforce continuous, mandatory session token re-authentication rules for all PeopleTools components.", "Isolate corporate ERP frameworks within dedicated network segments behind strict access access lists."]
references: ["LevelBlue. (2025). Scattered LAPSUS$ Hunters: Anatomy of a Federated Cybercriminal Brand.", "Immersive Labs. (2025). Scattered LAPSUS$ Hunters: The Cybercrime Group Redefining Threats."]
source_reliability: "high"
information_credibility: "high"
analytic_confidence: "high"
tags: ["campaign", "oracle", "peoplesoft", "erp", "data-theft", "slh"]
created: "2026-06-23"
updated: "2026-06-23"
author: "Senior Cyber Threat Intelligence Analyst"
---

# 2026 Oracle PeopleSoft Mass Data Theft Campaign

## Executive Summary
The 2026 Oracle PeopleSoft Mass Data Theft Campaign is a technically precise and financially damaging operation conducted by [[01_Threat_Actors/Scattered Lapsus$ Hunters]]. The campaign targets the core Enterprise Resource Planning (ERP) engines of major corporations, focusing on Oracle PeopleSoft suites. By capturing high-privilege web session states and administrative credentials, the threat actors gain direct access to sensitive payroll data, corporate bank routing profiles, tax records, and employee directories. This campaign presents a severe corporate risk, as the exfiltrated datasets allow for both direct executive extortion and extensive downstream corporate identity fraud.

## Campaign Overview
The threat actors carry out this campaign by bypassing traditional perimeter firewalls through identity token theft. Rather than attempting server-side exploit compilation, operators use session cookies and administrative credentials harvested via specialized infostealer tracking networks or help desk social engineering campaigns.

Once inside the PeopleSoft web interface (`PIA`), the actors leverage native PeopleTools configuration panels to execute high-volume data extractions. They manipulate internal query managers to bypass standard export limits, gathering large database blocks that include employee identification numbers, salary scales, direct deposit bank info, and corporate structures. The stolen information is bundled directly within the cloud database platform and pushed out through standard web protocols to external storage buckets, avoiding detection by host-based security systems.

## Threat Actor Associations
* **[[01_Threat_Actors/Scattered Lapsus$ Hunters]]**: Managed the initial credential sourcing, internal database querying parameters, and the subsequent financial extortion cycles targeting victim management.

## Malware & Tooling
* **Pure Identity-Based Footprint**: The campaign relies completely on legitimate system features and administrative query tools, avoiding the use of traditional malware payloads.
* **Custom Database Collectors**: The group uses automated web scripts designed to interact directly with PeopleTools data export structures to accelerate the harvesting process.

## Exploited Vulnerabilities
* **None**: The campaign relies entirely on the reuse of valid session tokens, credential abuse, and overly permissive internal database access controls.

## ATT&CK Tradecraft

### Initial Access
* [[02_TTPs/T1078 - Valid Accounts]]: Reusing hijacked high-privilege administrative keys to log directly into the target ERP web portal.

### Execution
* [[02_TTPs/T1059 - Command and Scripting Interpreter]]: Deploying automated web scripts to systematically interact with internal data query interfaces.

### Defense Evasion
* [[02_TTPs/T1539 - Steal Web Session Cookie]]: Hijacking active administrative web session states to bypass multi-factor authentication steps during console access.

### Discovery
* [[02_TTPs/T1046 - Network Service Discovery]]: Mapping internal database tables and parsing payroll object records within the ERP suite.

### Collection
* [[02_TTPs/T1119 - Automated Collection]]: Utilizing built-in PeopleSoft query tools to aggregate large sets of employee and financial data.

### Exfiltration
* [[02_TTPs/T1020 - Automated Exfiltration]]: Exporting collected database records through standard HTTPS channels directly to actor-controlled cloud architectures.

## Infrastructure & IOC Patterns
The actors route their command and extraction traffic through legitimate commercial cloud networks, making malicious data queries blend in with normal business traffic. Detailed victim lists and data samples are managed through the group's extortion communication networks.

## Victimology
The campaign primary targets mid-to-large scale financial organizations, regional healthcare networks, and public service infrastructures that run centralized PeopleSoft environments across the US and Western Europe.

## Detection & Hunting

### Behavioral Indicators
* Administrative ERP accounts executing large data export queries that do not match established baseline operational frequencies.
* Active web console connections for administrative profiles originating from anomalous ISP ranges or residential proxy networks.

### Detection Opportunities
* Configure real-time alerts within the PeopleSoft application log layer to detect when standard query tools are used to access or export extensive payroll or banking tables outside normal business hours.

### Log Sources
* PeopleSoft Internet Architecture (`PIA`) Access logs.
* Database Audit trails (SQL Server, Oracle DB tracking tables).
* Centralized Web Server logs (WebLogic, WebSphere).

### Telemetry Requirements
* Monitoring of web console session lifecycles, calling IP addresses, and specific data table query metrics.

### Hunt Ideas
* Search for instances where an active user session abruptly changes its network location while continuously executing large data extraction operations.

## Intelligence Assessment
The Oracle PeopleSoft Mass Data Theft Campaign demonstrates the threat actor's capacity to target high-value corporate ERP environments. By focusing on session hijacking and abusing built-in query systems, [[01_Threat_Actors/Scattered Lapsus$ Hunters]] can easily exfiltrate critical datasets while evading detection by standard endpoint security tools. It is highly probable that the group will continue to target these critical business systems as long as organizations rely on legacy authentication models for central ERP portals.

## Mitigations

### Immediate
* Invalidate all active session tokens and force web console re-authentication across all PeopleSoft environments.
* Audit and restrict administrative access privileges within the PeopleTools configuration panel.

### Tactical
* Implement context-aware, conditional access controls that restrict ERP web console access to verified corporate network segments or secure VPN endpoints.
* Enable advanced database-level logging for all tables containing payroll, banking, or PII assets.

### Strategic
* Transition core ERP management suites toward modern identity architectures that support phishing-resistant hardware-bound authentication keys and continuous session validation models.

## Sources
Immersive Labs. (2025). *Scattered LAPSUS$ Hunters: The Cybercrime Group Redefining Threats*. Threat Analysis Series.

LevelBlue. (2025). *Scattered LAPSUS$ Hunters: Anatomy of a Federated Cybercriminal Brand*. LevelBlue Research Reports.

## Changelog
* Created: 2026-06-23
* Updated: 2026-06-23
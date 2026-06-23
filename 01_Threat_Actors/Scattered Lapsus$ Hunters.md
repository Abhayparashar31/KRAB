---
entity_type: threat-actor
title: Scattered Lapsus$ Hunters
aliases:
  - SLH
  - Trinity of Chaos
  - UNC6040
  - UNC6395
summary: Scattered Lapsus$ Hunters is a high-profile cybercrime supergroup and federated alliance combining members of Scattered Spider, Lapsus$, and ShinyHunters. Emerging in August 2025, the group specializes in identity-centric data extortion, targeting large cloud/SaaS aggregators like Salesforce and Zendesk through advanced social engineering, vishing, and OAuth token manipulation.
origin_country: Unknown
suspected_sponsor: null
attribution_confidence: medium
actor_type: cybercrime_group
motivation:
  - financial
sophistication: high
operational_maturity: high
first_seen: 2025-08-08
last_seen: 2026-06-23
active: true
targeted_sectors:
  - Technology
  - Retail
  - Luxury Fashion
  - Aviation
  - Insurance
  - Government
targeted_regions:
  - United States
  - United Kingdom
  - Canada
  - Australia
  - France
  - Germany
targeted_platforms:
  - Cloud
  - SaaS
  - Salesforce
  - Zendesk
  - GitHub
  - AWS
campaigns:
  - "[[03_Campaigns/Salesforce Massive Corporate Extortion Wave]]"
  - "[[03_Campaigns/Zendesk Typosquatting and Phishing Campaign]]"
  - "[[03_Campaigns/Vishing Roster Diversification Drive]]"
malware_used:
  - "[[04_Malware/ShinySp1d3r]]"
  - "[[04_Malware/AnyDesk]]"
  - "[[04_Malware/TeamViewer]]"
ttps:
  - "[[02_TTPs/T1566.004 - Phishing- Voice Phishing]]"
  - "[[02_TTPs/T1078.004 - Valid Accounts- Cloud Accounts]]"
  - "[[02_TTPs/T1556.006 - Modify Authentication Process- Multi-Factor Authentication]]"
  - "[[02_TTPs/T1528 - Steal Application Access Token]]"
  - "[[02_TTPs/T1539 - Steal Web Session Cookie]]"
  - "[[02_TTPs/T1059 - Command and Scripting Interpreter]]"
  - "[[02_TTPs/T1046 - Network Service Discovery]]"
  - "[[02_TTPs/T1119 - Automated Collection]]"
  - "[[02_TTPs/T1020 - Automated Exfiltration]]"
vulnerabilities_exploited: []
infrastructure:
  - "[[06_IOCs/znedesk.com]]"
  - "[[06_IOCs/vpn-zendesk.com]]"
iocs: []
related_threat_actors:
  - "[[01_Threat_Actors/Scattered Spider]]"
  - "[[01_Threat_Actors/Lapsus$]]"
  - "[[01_Threat_Actors/ShinyHunters]]"
related_collections: []
detection_opportunities: []
mitigations: []
references:
  - "LevelBlue. (2025). Scattered LAPSUS$ Hunters: Anatomy of a Federated Cybercriminal Brand. LevelBlue Labs."
  - "SOCRadar. (2025). Dark Web Profile: Scattered Lapsus$ Hunters. SOCRadar."
  - "Immersive Labs. (2025). Scattered LAPSUS$ Hunters: The Cybercrime Group Redefining Threats. Immersive Labs."
  - "Dataminr. (2026). Cyber Intel Brief: Scattered Lapsus$ Hunters (SLH) Kicks Off Campaign to Recruitment of Women. Dataminr."
source_reliability: high
information_credibility: high
analytic_confidence: high
tlp: CLEAR
classification: UNCLASSIFIED
created: 2026-06-23
updated: 2026-06-23
tags:
  - threat-actor
  - slh
  - cybercrime
  - extortion
  - the-com
  - trinity-of-chaos
---

# Executive Summary
Scattered Lapsus$ Hunters (SLH) is an aggressive cybercrime "supergroup" and federated alliance that emerged in August 2025, uniting the personnel, operational methods, and reputations of three notorious extortion networks: Scattered Spider, Lapsus$, and ShinyHunters[cite: 2]. Also tracked as the "Trinity of Chaos", UNC6040, or UNC6395, this group represents a paradigm shift in modern cybercrime by favoring an identity-centric, cloud-first extraction philosophy characterized by the phrase "log in, not hack in"[cite: 2]. Bypassing traditional malware-driven perimeter intrusion, SLH relies heavily on high-velocity voice phishing (vishing), malicious OAuth application integrations, and insider recruitment to compromise high-value SaaS environments and multi-tenant customer relationship databases[cite: 2]. The group possesses a high degree of operational maturity and has compromised over 1.5 billion enterprise records globally[cite: 2]. They maintain a highly performative extortion style, utilizing public Telegram channels and dark web portals to maximize reputational duress for financial extortion[cite: 2].

# Attribution Assessment
* **Attribution Status:** Federated Cybercriminal Alliance / Underground Collective[cite: 2]
* **Known Aliases:** Trinity of Chaos, UNC6040, UNC6395[cite: 2]
* **Sponsoring Nation or Organization:** None (Financially motivated underground)[cite: 2]
* **Confidence Level:** High[cite: 2]
* **Overlaps with other tracked groups:** Scattered Lapsus$ Hunters is a situational, federated brand rather than a fully centralized corporate entity[cite: 2]. Intelligence indicates it operates under an umbrella alliance pulling active threat actors from [[01_Threat_Actors/Scattered Spider]], [[01_Threat_Actors/Lapsus$]], and [[01_Threat_Actors/ShinyHunters]][cite: 2]. The group functions within the broader English-speaking cybercriminal subculture known as "The Com"[cite: 2]. Research links its primary administrative and technical operational persona, known as "Rey," directly to historical activity involving the Hellcat ransomware leak site and recent management tracking of the BreachForums data platform[cite: 2].
* **Reporting Consistency:** High[cite: 2]. Major threat intelligence providers (including LevelBlue, SOCRadar, ReliaQuest, and Dataminr) maintain a cohesive operational matrix identifying SLH as a multi-threat alliance pooling social engineering, SIM-swapping, and data-exfiltration playbooks[cite: 2].

# Operational Profile
* **Operational Objectives:** Mass enterprise data exfiltration, corporate extortion, platform compromise monetization, and dark-web reputational prestige within "The Com" hierarchy[cite: 2].
* **Targeting Patterns:** Highly deliberate focus on large-scale third-party data aggregators, multi-tenant software-as-a-service (SaaS) providers, corporate CRM engines, and centralized source repositories offering maximum data yields[cite: 2].
* **Victimology:** Multinational conglomerates operating within Technology, Retail, Luxury Fashion, Aviation, Insurance, and Western Government agencies[cite: 2].
* **Geographic Focus:** Predominantly English-speaking markets, specifically targeting institutions in the United States, United Kingdom, Canada, and Australia, with documented expansion into France and Germany[cite: 2].
* **Intrusion Behavior:** Purely identity-focused[cite: 2]. Adversaries use pre-acquired PII to systematically fool internal company service desks, deploy trojanized integrations, or harvest high-privilege administrative sessions to move invisibly through legitimate corporate APIs[cite: 2].
* **Preferred Access Vectors:** Elite high-velocity voice phishing (vishing) campaigns augmented by automated AI voice synthesis, deployment of malicious OAuth enterprise integrations, session hijacking from infostealer logs, and public employee recruitment drives[cite: 2].
* **Persistence Style:** Installing fraudulent API hooks and connected cloud applications, bypassing traditional endpoint security entirely by operating inside SaaS-to-SaaS cloud infrastructure environments[cite: 2].
* **Post-Exploitation Behavior:** Bulk data scraping from active repositories (e.g., Salesforce, Zendesk, AWS, GitHub) accompanied by direct, loud, and public data doxxing via social applications to trigger immediate executive compliance[cite: 2].

# Campaign Activity (Past 14 Months Time Period: April 2025 - June 2026)
* [[03_Campaigns/Salesforce Massive Corporate Extortion Wave]]
  - **Operational Goal:** Multi-tenant customer data exfiltration and centralized corporate extortion[cite: 2].
  - **Description:** SLH breached a connected GitHub repository belonging to the integration vendor Salesloft[cite: 2]. Using hardcoded credentials found within, they accessed a cloud storage environment, harvested Active OAuth application tokens, and systematically extracted over 1 billion customer records across 39 interconnected enterprise Salesforce databases without exploiting software vulnerabilities[cite: 2].
  - **Timeframe:** March 2025 - October 2025[cite: 2].
  - **Notable Tradecraft:** Third-party integration compromise, GitHub-to-AWS pivoting, OAuth token theft, and launch of an "extortionware" dark web portal targeting Cisco and Google data layers[cite: 2].
* [[03_Campaigns/Zendesk Typosquatting and Phishing Campaign]]
  - **Operational Goal:** Administrative credential harvesting and support console compromise[cite: 2].
  - **Description:** Operational deployment of over 40 distinct typosquatted domains closely mimicking customer support infrastructure to stand up cloned Single Sign-On (SSO) authentication nodes and push malicious support tickets targeting enterprise help desks[cite: 2].
  - **Timeframe:** January 2026 - June 2026[cite: 2].
  - **Notable Tradecraft:** Mass typosquatting registry tracking, SSO gateway cloning, and direct help-desk endpoint infection using Trojanized ticket attachments[cite: 2].
* [[03_Campaigns/Vishing Roster Diversification Drive]]
  - **Operational Goal:** Velocity scaling of voice social engineering attacks by diversifying execution profiles[cite: 2].
  - **Description:** Coordinated underground recruitment drives on public Telegram boards offering high upfront financial incentives to source female threat actors for service desk social engineering campaigns, supplying pre-written operational scripts to increase help-desk deception efficacy[cite: 2].
  - **Timeframe:** February 2026 - May 2026[cite: 2].
  - **Notable Tradecraft:** Financial accomplice recruitment, script automation, and integration of specialized AI-driven voice agent synthesis[cite: 2].

# Targeted Organizations
* **Technology & SaaS Providers:** Integration platforms, AI chatbot vendors, sales engagement architectures, and customer support networks (e.g., Zendesk, Salesloft)[cite: 2].
* **Government & Law Enforcement:** Central databases housing sensitive data rings; noted for doxxing hundreds of DHS, ICE, FBI, and DOJ agency officials[cite: 2].
* **Global Retail & Luxury Fashion:** Large-scale commercial vendors housing comprehensive loyalty programs, customer contact cards, and corporate tracking data sets[cite: 2].

# Malware & Tooling
* **Offensive Frameworks & Custom Deliverables:**
  - [[04_Malware/ShinySp1d3r]] - An upcoming Custom Ransomware-as-a-Service (RaaS) engine advertised by the alliance on corporate chat channels for eventual local file encryption operations[cite: 2].
* **Administrative & Remote Management Tools (RMM):**
  - [[04_Malware/AnyDesk]] - Leveraged extensively to maintain interactive endpoints inside corporate operational networks[cite: 2].
  - [[04_Malware/TeamViewer]] - Deployed to simulate normal remote support actions[cite: 2].
* **Automation & Exploitation Tools:**
  - AI-driven Voice Agents - Highly tailored voice simulation modules utilized to execute scalable automated calls, bypassing accents and regional help-desk alert thresholds[cite: 2].
  - Malicious App Integrations - Custom-crafted OAuth applications mimicking trusted business utility software to ensure structural background access[cite: 2].

# Exploited Vulnerabilities
* *Note:* Consistent with their baseline methodology ("log in, not hack in"), Scattered Lapsus$ Hunters bypass software vulnerability exploitation entirely[cite: 2]. Their historical track record over the past 14 months displays zero reliance on zero-day flaws or local CVE code compilation execution, operating exclusively via social engineering, token theft, and structural misconfigurations[cite: 2].

# ATT&CK Tradecraft

### Initial Access
* [[02_TTPs/T1566.004 - Phishing- Voice Phishing]]
  - Procedural Example: Conducting targeted vishing calls using pre-researched PII to manipulate help-desk teams into overriding employee MFA parameters[cite: 2].
* [[02_TTPs/T1078.004 - Valid Accounts- Cloud Accounts]]
  - Procedural Example: Publicly offering $500 to $1,000 stipends on dark web forums to purchase access or credentials directly from malicious internal corporate employees[cite: 2].

### Execution
* [[02_TTPs/T1059 - Command and Scripting Interpreter]]
  - Procedural Example: Executing custom cloud-management scripts inside stolen AWS environments to scan for accessible client secrets[cite: 2].

### Persistence
* [[02_TTPs/T1528 - Steal Application Access Token]]
  - Procedural Example: Registering trojanized OAuth integrations inside client CRM platforms to retain API-level data query rights indefinitely[cite: 2].

### Defense Evasion
* [[02_TTPs/T1556.006 - Modify Authentication Process- Multi-Factor Authentication]]
  - Procedural Example: Forcing target accounts to generate valid session keys via automated MFA fatigue bombing or executing cross-carrier SIM-swapping[cite: 2].

### Credential Access
* [[02_TTPs/T1539 - Steal Web Session Cookie]]
  - Procedural Example: Scraping structural enterprise session cookies out of stolen dark-web infostealer logs to instantly duplicate valid cloud sessions[cite: 2].

### Discovery
* [[02_TTPs/T1046 - Network Service Discovery]]
  - Procedural Example: Programmatically enumerating connected cloud storage configurations and external database paths to target high-value information lakes[cite: 2].

### Collection
* [[02_TTPs/T1119 - Automated Collection]]
  - Procedural Example: Utilizing automated data scraping tools to collect full contact spreadsheets, loyalty profiles, and code repository files into internal cloud staging areas[cite: 2].

### Exfiltration
* [[02_TTPs/T1020 - Automated Exfiltration]]
  - Procedural Example: Exfiltrating large database profiles across multi-tenant networks directly through active API data export requests[cite: 2].

# Infrastructure & IOC Patterns
The alliance utilizes specialized, high-velocity infrastructure configurations:
* **Domain Typosquatting:** Massive domain generation strategies targeting support networks[cite: 2]. Recent registrations include over 40 Zendesk variations (e.g., [[06_IOCs/znedesk.com]], [[06_IOCs/vpn-zendesk.com]])[cite: 2]. These domains consistently route through the *NiceNic* registrar, use masked Cloudflare nameservers, and provide false US/UK contact credentials[cite: 2].
* **Telegram Management Nodes:** Coordinated Telegram platforms serve as the foundational center for public extortion posting, data leakage schedules, personnel recruiting operations, and real-time taunting of international law enforcement bodies[cite: 2].
* **SSO Phishing Portals:** Implementation of cloned Single Sign-On landing structures directly preceding target business cloud platforms, designed to mimic federated identity systems to split out cleartext user credentials[cite: 2].

# Detection Engineering Notes
* **Behavioral Indicators:**
  - Simultaneous alerts indicating rapid OAuth connected-app integration additions followed immediately by massive programmatic API bulk export actions[cite: 2].
  - Authentication session cookie reuse showing extreme geographic discrepancies or sudden shifts across anomalous IP networks[cite: 2].
  - A high frequency of password reset tickets originating from the same telephone vector accompanied by instant alterations to high-privilege MFA structures[cite: 2].
* **Log Sources:** Azure AD Sign-in logs / Okta System logs (tracking Session Identifier reuse and MFA modification strings), AWS CloudTrail / Salesforce Event Monitoring logs (tracking connected application additions and bulk API data extraction queries)[cite: 2].
* **KQL Query Example (Suspicious OAuth App Consent/Data Access):**
```kql
AuditLogs
| where OperationName has "Consent to application" or OperationName has "Add OAuth2PermissionGrant"
| extend InitiatedBy = tostring(InitiatedBy.user.userPrincipalName)
| extend TargetApp = tostring(TargetResources[0].displayName)
| project TimeGenerated, OperationName, InitiatingUser = InitiatedBy, TargetApplication = TargetApp, Result
```[cite: 2]
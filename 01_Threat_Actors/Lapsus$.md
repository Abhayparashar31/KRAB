---
entity_type: threat-actor
title: Lapsus$
aliases:
  - Strawberry Tempest
  - Slippy Spider
summary: A highly volatile, globally organized cyber extortion group notoriously distinct for high-visibility public shaming, sophisticated helpdesk vishing, and multi-tenant identity infrastructure compromises without relying on traditional system encryption.
origin_country: United Kingdom, Brazil
suspected_sponsor: None
attribution_confidence: high
actor_type: criminal
motivation:
  - Financial Gain
  - Notoriety
sophistication: high
operational_maturity: medium
first_seen: 2021-12
last_seen: 2026-06
active: true
targeted_sectors:
  - Technology
  - Telecommunications
  - Government
  - Gaming
  - Manufacturing
  - Healthcare
  - Media
targeted_regions:
  - Global
  - North America
  - Europe
  - South America
targeted_platforms:
  - Windows OS
  - Cloud SaaS
  - Azure AD
  - Okta
campaigns:
  - "[[03_Campaigns/Scattered LAPSUS$ Hunters Consolidated Wave]]"
  - "[[03_Campaigns/2022 Big Tech Infrastructure Breach Surge]]"
malware_used:
  - "[[04_Malware/RedLine Stealer]]"
  - "[[04_Malware/Mimikatz]]"
ttps:
  - "[[02_TTPs/T1566.003 - Phishing- Spearphishing SMS]]"
  - "[[02_TTPs/T1059 - Command and Scripting Interpreter]]"
  - "[[02_TTPs/T1078.004 - Valid Accounts- Cloud Accounts]]"
  - "[[02_TTPs/T1068 - Exploitation for Privilege Escalation]]"
  - "[[02_TTPs/T1562.001 - Impair Defenses- Disable or Modify Tools]]"
  - "[[02_TTPs/T1003.001 - OS Credential Dumping- LSASS Memory]]"
  - "[[02_TTPs/T1087 - Account Discovery]]"
  - "[[02_TTPs/T1021.001 - Remote Services- Remote Desktop Protocol]]"
  - "[[02_TTPs/T1114 - Email Collection]]"
  - "[[02_TTPs/T1567.002 - Exfiltration Over Web Service- Exfiltration to Cloud Storage]]"
  - "[[02_TTPs/T1489 - Service Stop]]"
vulnerabilities_exploited: []
infrastructure:
  - "[[06_IOCs/okta-verification-portal[.]com]]"
iocs: []
related_threat_actors:
  - "[[01_Threat_Actors/Scattered Spider]]"
  - "[[01_Threat_Actors/ShinyHunters]]"
related_collections: []
detection_opportunities:
  - Monitor for suspicious multi-factor authentication (MFA) push-fatigue patterns mapped to active IT helpdesk communication windows.
  - Identify unusual Azure Active Directory administrative token creations originating from residential proxy address networks.
mitigations:
  - Enforce hardware-based, phishing-resistant FIDO2 authentication keys across all corporate core identity channels.
  - Establish strict out-of-band secondary cryptographically verified validation processes for IT helpdesk password reset requests.
references:
  - "Recorded Future. (2026). State of Security: Fragmentation and Social Engineering Trends."
  - "Vectra AI. (2025). Threat Actor Intelligence Card: LAPSUS$."
  - "NJCCIC. (2026). 2026 Cyber Threat Assessment: Structural Exploitation Waves."
source_reliability: A - Reliable
information_credibility: 1 - Confirmed by multiple sources
analytic_confidence: high
tlp: TLP:CLEAR
classification: Unclassified
created: 2026-06-23
updated: 2026-06-23
tags:
  - lapsus
  - strawberry-tempest
  - slippy-spider
  - vishing
  - extortion
  - the-com
---

# Lapsus$

## Executive Summary
Lapsus$ (tracked as Strawberry Tempest or Slippy Spider) is a unique and aggressive cyber extortion group that fundamentally altered traditional enterprise response models. Composed historically of decentralized teenage actors integrated within the broader underground scene known as "The Com," the group completely bypasses traditional file-encryption tactics. Instead, Lapsus$ relies entirely on direct data exfiltration, source code repository theft, and high-publicity extortion via viral messaging platforms. Their tactical framework is heavily dependent on subverting the human layer of security through insider bribery, SIM swapping, and interactive vishing (voice phishing) targeting enterprise helpdesks. Their primary targets include multinational technology providers, telecommunication hubs, gaming conglomerates, and government platforms where data exposure ruins market confidence.

## Attribution Assessment
The group operates as a loose, globally distributed criminal collective with prominent administrative actors historically identified and arrested within the United Kingdom and Brazil throughout 2022 and 2023. Despite legal interventions, the structural framework and signature extortion playbooks of Lapsus$ survived. In mid-to-late 2025 and moving into mid-2026, threat intelligence telemetry confirmed an operational rebirth. Remaining elements of the group pooled infrastructure resources, forming a highly volatile joint-extortion merger with [[01_Threat_Actors/Scattered Spider]] and [[01_Threat_Actors/ShinyHunters]], operating under the collective tracking moniker "Scattered LAPSUS$ Hunters."

## Operational Profile
The operational objective of Lapsus$ is rapid financial monetization paired with intense public notoriety. Their victimology is focused entirely on elite corporate ecosystems possessing high-value source code libraries, master identity stores, or customer data pools. Lapsus$ achieves perimeter access by manipulating credentials bought from access clearings, executing target-specific mobile SIM swaps to intercept MFA codes, or calling customer support centers to override account access parameters. Once inside a network domain, they navigate aggressively without maintaining typical operational security boundaries, moving straight to collaborative structures (Slack, Teams, Confluence, GitHub) to aggregate documentation before leaking files to public Telegram spaces.

## Campaign Activity (Past 14 Months)

* [[03_Campaigns/Scattered LAPSUS$ Hunters Consolidated Wave]]
  * **Operational Goal:** Infiltrate high-profile enterprise infrastructures via advanced social engineering and leverage public-facing shaming to enforce massive extortion payouts.
  * **Description of the Campaign:** Formed as a strategic consolidation in late 2025, this campaign represents a structural merger blending Lapsus$'s chaotic messaging models with Scattered Spider's precision identity theft. A major highlighted incident in August-September 2025 involved an intrusion against British automaker Jaguar Land Rover. Affiliates utilized interactive helpdesk vishing to manipulate identity tokens, ultimately halting manufacturing plants and causing an estimated $2.5 billion in systemic economic impacts.
  * **Timeframe:** August 2025 – Ongoing into June 2026.
  * **Notable Tradecraft:** Helpdesk impersonation, MFA exhaustion loops, toxic public Telegram data dumps, and cloud dashboard manipulation.
  * **Targeted Organizations:** Jaguar Land Rover, multi-national logistics companies, and Tier-1 automotive distribution links across the United Kingdom and United States.

## Malware & Tooling
* **Credential Harvesters:** While the group heavily relies on native cloud administration modules, they leverage commodity implants such as [[04_Malware/RedLine Stealer]] distributed via initial access brokers to collect baseline corporate environment sessions and cookies.
* **Privilege Dumping Utilities:** Affiliates consistently employ [[04_Malware/Mimikatz]] alongside native tools like `ntdsutil` to capture active local domain structures and extract service tokens.

## Exploited Vulnerabilities
* None / Unknown: Lapsus$ historically avoids sophisticated custom zero-day vulnerability exploits. They choose instead to leverage legitimate access configurations and social manipulation paths to bypass security bounds.

## ATT&CK Tradecraft

### Initial Access
* [[02_TTPs/T1566.003 - Phishing- Spearphishing SMS]]: Executing corporate smishing waves to collect active credentials or targeting helpdesk employees directly via vishing.

### Execution
* [[02_TTPs/T1059 - Command and Scripting Interpreter]]: Deploying native command processors and administrative shell lines to run tools provided by insider links.

### Persistence
* [[02_TTPs/T1078.004 - Valid Accounts- Cloud Accounts]]: Creating unauthorized federated identity links or re-registering secondary user endpoints to maintain persistent cloud control.

### Privilege Escalation
* [[02_TTPs/T1068 - Exploitation for Privilege Escalation]]: Capitalizing on configuration weaknesses inside enterprise environments (e.g., Jira, Confluence) to escalate active roles.

### Defense Evasion
* [[02_TTPs/T1562.001 - Impair Defenses- Disable or Modify Tools]]: Removing tracking solutions, modifying global security policies, and deploying legitimate credentials to mimic normal operational traffic.

### Credential Access
* [[02_TTPs/T1003.001 - OS Credential Dumping- LSASS Memory]]: Dumping host access hashes and running DCSync scripts to harvest network credentials.

### Discovery
* [[02_TTPs/T1087 - Account Discovery]]: Navigating cloud directory dashboards, internal wikis, and document servers to look for hidden plaintext credential logs.

### Lateral Movement
* [[02_TTPs/T1021.001 - Remote Services- Remote Desktop Protocol]]: Pivoting to distinct administrative components across internal targets over active VPN or RDP structures.

### Exfiltration
* [[02_TTPs/T1567.002 - Exfiltration Over Web Service- Exfiltration to Cloud Storage]]: Directly uploading compressed corporate source-code trees and user repositories to actor-owned public data channels.

### Impact
* [[02_TTPs/T1489 - Service Stop]]: Forcibly stopping enterprise web applications and altering corporate domain configurations to disrupt live services.

## Infrastructure & IOC Patterns
The infrastructure profile of Lapsus$ is famously unstable. Rather than relying on custom covert virtual private network structures, they utilize widely available residential proxies (e.g., proxies routing through consumer ISP blocks) to match the geographic origin of compromised employees, blinding simple location-based login checks.
* **Lookalike Portal Nodes:** `okta-verification-portal[.]com`

## Detection Engineering Notes

### Behavioral Indicators
* Multiple failed authentication attempts across a single account followed by a sudden successful login matching a completely distinct ISP routing block.
* Rapid data collection actions pulling code trees or document collections from internal repositories via newly added administrative profiles.

### Detection Opportunities
* Monitor and alert on instant modifications made to global cloud tenant access rules, specifically tracking the initialization of external unverified federation configurations.
* Flag instances where a single active identity registers a secondary multi-factor authentication token from a separate network zone within a narrow window.

### Log Sources
* Identity Provider Logs (Okta System Log, Entra ID Interactive Sign-Ins).
* Source Code Management Platform Audit Trails (GitHub, GitLab Event Logs).
* Internal collaboration application tracking logs (Slack, Microsoft Teams).

### Telemetry Requirements
* Capture of authentication location variables, multi-factor token creation details, and real-time process command execution histories.

## Intelligence Assessment
Lapsus$ represents a dangerous shift toward pure identity subversion and psychological extortion models. Their ongoing operations within the "Scattered LAPSUS$ Hunters" cluster into mid-2026 show that traditional perimeter technical protections are highly vulnerable when faced with coordinated, low-tech social engineering campaigns. The group's lack of interest in complex file lockers means their deployment cycle is incredibly fast, allowing them to breach, extract data, and destroy corporate confidence within hours.

## Intelligence Gaps
* The technical pipeline used to secure and maintain insider collusion links inside global telecommunication infrastructures.
* The formal economic conversion frameworks driving cash-out distribution pools inside decentralized non-cooperative digital spaces.

## Recommended Defensive Actions

### Immediate
* Transition all tier-1 administrative identity nodes away from carrier-dependent SMS validation frameworks.
* Implement behavioral alerting rules tracking high-volume file downloads across internal documentation directories.

### Tactical
* Restrict the creation of new global cloud tenant permissions to dedicated, multi-party authorization protocols.
* Harden IT service desk operational flows, prohibiting password overrides based solely on basic public user data metrics.

### Strategic
* Migrate corporate architecture completely to phishing-resistant authentication technologies (FIDO2 authentication standards).

### Long-Term
* Institute strict conditional access architectures checking system baseline hygiene properties prior to granting active application-layer authentication tokens.

## Related Threat Actors
* [[01_Threat_Actors/Scattered Spider]]: Core collaboration partner forming the structural backplane of current 2025–2026 extortion campaigns.
* [[01_Threat_Actors/ShinyHunters]]: Collaborative network link exchanging stolen identity structures and coordinating public data exposures.

## Sources
NJCCIC. (2026). 2026 Cyber Threat Assessment: Structural Exploitation Waves. Trenton, NJ: New Jersey State Government.

Recorded Future. (2026). Fragmentation Defined 2025's Threat Landscape. Here's What It Means for 2026. Insikt Group Research.

Vectra AI. (2025). Is Your Organization Safe from LAPSUS$ Ransomware Attacks? Vectra Threat Intelligence Library.

## Changelog
* Created: 2026-06-23
* Updated: 2026-06-23
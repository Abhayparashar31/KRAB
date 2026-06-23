---
entity_type: campaign
title: "Zendesk Typosquatting and Phishing Campaign"
aliases: ["Zendesk Infrastructure Infiltration Wave", "Help-Desk Customer Support Blitz"]
summary: "An active, high-velocity campaign targeting customer support infrastructure by deploying dozens of typosquatted domains and cloned Single Sign-On (SSO) portals to harvest corporate credentials and deliver trojanized support tickets."
first_seen: "2026-01-10"
last_seen: "2026-06-23"
status: "Active"
attribution: "[[01_Threat_Actors/Scattered Lapsus$ Hunters]]"
attribution_confidence: "high"
targeted_sectors: ["Technology", "Retail", "Customer Support Networks"]
targeted_regions: ["United States", "United Kingdom", "Europe"]
targeted_technologies: ["Zendesk Support Portals", "Single Sign-On (SSO) Gateways", "Domain Name Services (DNS)"]
objectives: ["Administrative Credential Harvesting", "Endpoint Compromise", "Downstream Network Access"]
threat_actors: ["[[01_Threat_Actors/Scattered Lapsus$ Hunters]]"]
malware: ["[[04_Malware/AnyDesk]]"]
vulnerabilities: []
ttps: ["[[02_TTPs/T1566.004 - Phishing- Voice Phishing]]", "[[02_TTPs/T1539 - Steal Web Session Cookie]]", "[[02_TTPs/T1078.004 - Valid Accounts- Cloud Accounts]]", "[[02_TTPs/T1021.001 - Remote Services- Remote Desktop Protocol]]"]
related_iocs: ["[[06_IOCs/znedesk[.]com]]", "[[06_IOCs/vpn-zendesk[.]com]]"]
infection_vectors: ["Typosquatted Domain Phishing", "Cloned SSO Portal Capture", "Malicious Support Ticket Attachments"]
infrastructure_patterns: ["NiceNic domain registrations", "Cloudflare-masked nameservers", "Deceptive multi-brand URLs"]
victimology: ["Global enterprise operations and customer relationship networks that rely heavily on central Zendesk environments to process user support communications."]
detection_opportunities: ["Internal connections from enterprise endpoints to newly registered Zendesk-themed domains.", "Volumetric submission of external support tickets containing abnormal or executable attachment types."]
mitigations: ["Enforce strict domain verification policies across all customer support portals.", "Implement rigorous email and file scanning controls on all external support ticket attachments."]
references: ["ReliaQuest. (2026). Is Zendesk Scattered Lapsus$ Hunters' Latest Campaign Target?", "SOCRadar. (2025). Dark Web Profile: Scattered Lapsus$ Hunters."]
source_reliability: "high"
information_credibility: "high"
analytic_confidence: "high"
tags: ["campaign", "zendesk", "phishing", "typosquatting", "sso-theft", "slh"]
created: "2026-06-23"
updated: "2026-06-23"
author: "Senior Cyber Threat Intelligence Analyst"
---

# Zendesk Typosquatting and Phishing Campaign

## Executive Summary
The Zendesk Typosquatting and Phishing Campaign is a highly targeted and ongoing identity-harvesting operation orchestrated by [[01_Threat_Actors/Scattered Lapsus$ Hunters]]. The campaign focuses on compromising corporate customer service and help-desk environments by deploying over 40 meticulously crafted typosquatted domains (e.g., `znedesk[.]com`) and cloned Single Sign-On (SSO) authentication portals. By mimicking legitimate customer service platforms, the threat actors harvest high-privilege support credentials and use fraudulent ticket submissions to deliver malware to support staff. This campaign presents a severe risk to corporate supply chains, as compromising a centralized support platform grants adversaries direct access to sensitive customer data and trusted communication channels.

## Campaign Overview
The operational methodology relies on the systematic registration of lookalike domains through the *NiceNic* registrar, utilizing Cloudflare nameservers to mask backend hosting infrastructures. These domains host cloned corporate authentication portals designed to capture cleartext credentials and session tokens from unsuspecting support staff.

In parallel, the threat actors submit fraudulent support tickets directly to legitimate company help desks. These tickets contain well-crafted social engineering pretexts—such as urgent system restoration requests or fake password reset demands—and include trojanized attachments. When support personnel interact with these attachments, remote access trojans (RATs) are executed on their local endpoints, granting the actors an initial foothold inside the corporate network for subsequent lateral movement.

## Threat Actor Associations
* **[[01_Threat_Actors/Scattered Lapsus$ Hunters]]**: Managed the bulk infrastructure setup, domain registration strategies, cloned SSO configuration drops, and malicious ticket submission workflows.

## Malware & Tooling
* **Trojanized Support Files**: Malicious attachments disguised as system documents or configuration files designed to deploy remote access payloads.
* **[[04_Malware/AnyDesk]]**: Repurposed as a persistent remote monitoring and management (RMM) utility to maintain access to compromised help-desk endpoints.

## Exploited Vulnerabilities
* **None**: The campaign relies entirely on infrastructure typosquatting, user deception, and the abuse of trusted help-desk communication channels, avoiding the use of software vulnerabilities.

## ATT&CK Tradecraft

### Initial Access
* [[02_TTPs/T1566.004 - Phishing- Voice Phishing]]: Utilizing social engineering pretexts and lookalike web domains to trick support staff into entering credentials into phishing portals.
* [[02_TTPs/T1078.004 - Valid Accounts- Cloud Accounts]]: Accessing customer support environments using harvested administrative credentials.

### Execution
* [[02_TTPs/T1059 - Command and Scripting Interpreter]]: Executing malicious payloads embedded within trojanized support ticket attachments on user endpoints.

### Defense Evasion
* [[02_TTPs/T1539 - Steal Web Session Cookie]]: Reusing stolen session tokens through premium proxy networks to match legitimate user browser profiles and bypass authentication alerts.

### Lateral Movement
* [[02_TTPs/T1021.001 - Remote Services- Remote Desktop Protocol]]: Moving laterally across internal corporate networks from compromised help-desk endpoints using hijacked domain accounts.

### Collection
* [[02_TTPs/T1119 - Automated Collection]]: Running script tools to harvest sensitive customer information, contact directories, and historical communications from the compromised Zendesk instance.

## Infrastructure & IOC Patterns
The campaign features highly standardized infrastructure characteristics across all registered phishing assets:
* **Registration Provider:** NiceNic
* **DNS Protection Layer:** Cloudflare-masked nameservers
* **Contact Profiles:** Fake United States or United Kingdom administrative details
* **Primary Phishing Indicators:** `znedesk[.]com`, `vpn-zendesk[.]com`

## Victimology
The campaign primary targets multinational technology firms, consumer retail networks, and global service providers that deploy centralized Zendesk instances to manage high volumes of customer and corporate communications.

## Detection & Hunting

### Behavioral Indicators
* Inbound network connections from internal corporate hosts to newly registered Zendesk-themed domains using non-standard naming schemas.
* Customer support accounts initiating sessions from unexpected residential proxy networks immediately after a support ticket interaction.

### Detection Opportunities
* Implement real-time monitoring to detect and block outbound traffic toward domains containing common typosquatted variations of critical enterprise platforms like Zendesk.

### Log Sources
* Corporate DNS Query logs.
* Enterprise Web Application Firewall (WAF) and proxy access tracking.
* Zendesk Application Audit histories and ticket attachment modification logs.

### Telemetry Requirements
* Central aggregation of corporate resolution logs, endpoint connection histories, and third-party application access tokens.

### Hunt Ideas
* Search for instances where help-desk endpoints show sudden outbound connections to unverified external IP addresses immediately following the processing of a new external support ticket.

## Intelligence Assessment
The Zendesk Typosquatting and Phishing Campaign demonstrates the capability of [[01_Threat_Actors/Scattered Lapsus$ Hunters]] to identify and exploit trusted communication paths. By targeting customer support portals, the group can easily harvest credentials and deliver payloads while evading traditional network defenses. It is highly probable that the group will continue to target these platforms as long as organizations treat customer service channels as lower security priorities than primary corporate networks.

## Mitigations

### Immediate
* Audit and block all internal network traffic to known typosquatted domains like `znedesk[.]com` and `vpn-zendesk[.]com`.
* Force session re-authentication for all active users within the corporate Zendesk environment.

### Tactical
* Enforce phishing-resistant FIDO2 hardware keys for all customer support and help-desk personnel.
* Implement automated file analysis and sandboxing controls to scan all incoming attachments submitted via external support tickets.

### Strategic
* Treat customer support platforms as critical infrastructure within the enterprise security architecture, applying strict conditional access rules and continuous session validation models to all connected profiles.

## Sources
ReliaQuest. (2026). *Is Zendesk Scattered Lapsus$ Hunters' Latest Campaign Target?*. ReliaQuest Threat Insights.

SOCRadar. (2025). *Dark Web Profile: Scattered Lapsus$ Hunters*. Cyber Crime Research Center.

## Changelog
* Created: 2026-06-23
* Updated: 2026-06-23
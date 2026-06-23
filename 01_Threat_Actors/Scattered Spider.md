---
entity_type: threat_actor
title: Scattered Spider
aliases:
  - UNC3944
  - Octo Tempest
  - Muddled Libra
  - Scatter Swine
  - Starfraud
  - Roasted 0ktapus
  - Storm-0875
summary: A highly aggressive, native English-speaking cybercriminal cluster specializing in advanced social engineering, identity infrastructure compromise, and cloud/SaaS environment exploitation to deploy ransomware and execute double-extortion data theft.
origin_country: United States, United Kingdom
suspected_sponsor: None
attribution_confidence: high
actor_type: criminal
motivation:
  - Financial Gain
  - Extortion
  - Notoriety
sophistication: high
operational_maturity: high
first_seen: 2022-05
last_seen: 2026-06
active: true
targeted_sectors:
  - Hospitality
  - Casinos
  - Technology
  - Telecommunications
  - Retail
  - Airlines
  - Food Services
  - Managed Service Providers (MSPs)
  - Healthcare
  - Financial Services
targeted_regions:
  - North America
  - Europe
  - Australia
targeted_platforms:
  - Windows OS
  - Linux OS
  - VMware ESXi
  - Microsoft Azure
  - Amazon Web Services (AWS)
  - Okta
  - Google Workspace
  - Snowflake
campaigns:
  - "[[03_Campaigns/2023 Casino Extortion Campaign]]"
  - "[[03_Campaigns/2025-2026 SaaS and Cloud Exploitation Wave]]"
malware_used:
  - "[[04_Malware/BlackCat]]"
  - "[[04_Malware/DragonForce]]"
  - "[[04_Malware/BlackSuit]]"
  - "[[04_Malware/Qakbot]]"
  - "[[04_Malware/Lumma Stealer]]"
  - "[[04_Malware/Vidar Stealer]]"
  - "[[04_Malware/Chisel]]"
  - "[[04_Malware/Teleport]]"
ttps:
  - "[[02_TTPs/T1566.001 - Phishing- Spearphishing Attachment]]"
  - "[[02_TTPs/T1621 - Multi-Factor Authentication Request Generation]]"
  - "[[02_TTPs/T1078 - Valid Accounts]]"
  - "[[02_TTPs/T1562 - Impair Defenses]]"
  - "[[02_TTPs/T1486 - Data Encrypted for Impact]]"
vulnerabilities_exploited:
  - "[[05_Vulnerabilities/CVE-2015-2291]]"
infrastructure:
  - "[[06_IOCs/login-microsoft365-auth[.]com]]"
iocs:
  - "[[06_IOCs/login-microsoft365-auth[.]com]]"
related_threat_actors:
  - "[[01_Threat_Actors/ALPHV]]"
  - "[[01_Threat_Actors/ShinyHunters]]"
  - "[[01_Threat_Actors/Lapsus$]]"
related_collections: []
detection_opportunities:
  - Monitor for anomalous help desk password reset workflows combined with immediate MFA device registration changes.
  - Track bulk data exfiltration configurations via synchronization utilities to cloud infrastructure targets.
  - Detect unauthorized multi-factor authentication push notifications targeting high-privilege administrative directory entities.
mitigations:
  - Enforce phishing-resistant multi-factor authentication across identity providers.
  - Implement multi-layered behavioral verification steps for corporate helpdesk password/MFA resets.
  - Strictly regulate outbound remote management monitoring tools and proxy execution paths.
references:
  - "CISA & FBI. (2023). Joint Cybersecurity Advisory: Scattered Spider (AA23-320A)."
  - Microsoft Threat Intelligence. (2025). Protecting customers from Octo Tempest attacks across multiple industries.
  - Mandiant. (2024). UNC3944 Targets SaaS Applications.
source_reliability: A - Reliable
information_credibility: 1 - Confirmed by multiple sources
analytic_confidence: high
tlp: TLP:CLEAR
classification: Unclassified
created: 2026-06-22
updated: 2026-06-22
tags:
  - scat-spider
  - unc3944
  - octo-tempest
  - raas
  - social-eng
  - identity
author: Senior Cyber Threat Intelligence Analyst
---


## Executive Summary
Scattered Spider is a highly prolific, aggressive, and adaptive cybercriminal cluster composed primarily of native English-speaking individuals. The group represents a fundamental shift in modern corporate intrusion vectors, treating enterprise identity infrastructures and cloud permission frameworks as their primary attack surfaces rather than depending heavily on traditional automated technical exploits. Their targets include high-profile global enterprises in the hospitality, casino, aviation, telecommunications, retail, and technology sectors. Their operations are defined by highly tailored voice-phishing (vishing) campaigns targeting outsourced IT service desks, targeted SIM-swapping, multi-factor authentication (MFA) push notification bombing, extensive data theft from software-as-a-service (SaaS) structures, and the deployment of multi-platform ransomware for large-scale extortion.

## Attribution Assessment
The attribution confidence is high that Scattered Spider operates as an independent cybercriminal network devoid of state sponsorship. The group is known under various alternative industry trackers including [[01_Threat_Actors/UNC3944]], [[01_Threat_Actors/Octo Tempest]], [[01_Threat_Actors/Muddled Libra]], [[01_Threat_Actors/Scatter Swine]], [[01_Threat_Actors/Starfraud]], and [[01_Threat_Actors/Storm-0875]]. Cross-industry reporting indicates that the cluster forms close, loose tactical alliances with underground digital communities collectively referred to as "The Com". Notable operational, infrastructure, and messaging overlaps discovered in late 2025 and 2026 indicate deep collaborative links and mergers with groups such as [[01_Threat_Actors/ShinyHunters]] and [[01_Threat_Actors/Lapsus$]]. The cluster functions as a premier affiliate for prominent Ransomware-as-a-Service (RaaS) operations, exhibiting massive tool and revenue sharing with [[01_Threat_Actors/ALPHV]] (BlackCat) and [[01_Threat_Actors/DragonForce]] core developers.

## Operational Profile
The threat cluster focuses entirely on financial extortion through double-extortion schemes. They intentionally target large enterprise organizations containing expansive internal directories, segmented multi-cloud environments, and distributed help desk functions highly vulnerable to interpersonal exploitation. Geographically, their intrusions center heavily on targets across North America, Europe, and Australia. 

The group's preferred initial access vectors rely on sophisticated social engineering: deploying SMS-phishing campaigns featuring weaponized, corporate-themed lookalike single sign-on (SSO) portals, executing targeted SIM-swapping to intercept verification numbers, or calling corporate technical support services to trick operators into resetting passwords or registering new MFA keys. To maintain persistent access, the group configures malicious federated identity configurations, registers unauthorized devices into identity provider lists, or creates secondary cloud compute instances. During post-exploitation, they aggressively sweep internal channels like Slack, Microsoft Teams, and Microsoft Exchange to monitor internal incident response activities, often directly joining remediation bridge calls to circumvent defensive actions.

## Campaign Activity
* [[03_Campaigns/2025 Multi-Industry Hypervisor and Retail Extortion Campaign]]
	- **Operational Goal:** Large-scale corporate server encryption, backup sabotage, and financial extortion via white-label ransomware deployment models.
	- **Description of the Campaign:** This campaign surfaced prominently in April 2025 with a high-impact network intrusion targeting the major British retailer Marks & Spencer (M&S), causing approximately £40 million per week in operational losses and compromising the records of 9.4 million customers. The event highlighted a critical strategic shift as Scattered Spider actively collaborated with the Russia-based DragonForce ransomware cartel, moving toward a white-label RaaS deployment framework. Its appearance shifted across multiple economic sectors over the past 14 months, aggressively impacting food services, hospitality, and insurance between April and July 2025 before transitioning directly to the global airline sector. A major update to their playbook involved a reversal of their traditional methodology: instead of using cloud identity privileges to pivot to on-premises resources, the actors targeted on-premises virtualization management planes and VMware ESXi hypervisors at the initial stage of the intrusion before expanding upward into cloud platforms. This tactical variation allowed them to disable corporate backup capabilities and endpoint monitoring systems simultaneously prior to triggering domain-wide encryption.
	- **Timeframe:** April 2025 – December 2025.
	- **Notable Tradecraft:** Compromise of third-party IT contractor email accounts, safe mode system reboots, execution of Bring Your Own Vulnerable Driver (BYOVD) tactics to terminate EDR agents, and deployment of hypervisor-targeted DragonForce ransomware variants.
	- **Targeted Organizations:** Marks & Spencer (M&S), international commercial airlines, food services conglomerates, enterprise hospitality providers, and corporate insurance firms.

* [[03_Campaigns/2025-2026 SaaS Identity Crisis and Help Desk Exploitation Wave]]

	- **Operational Goal:** Direct SaaS application compromise, cloud storage credential abuse, automated data harvesting, and public-facing decentralized extortion.
	- **Description of the Campaign:** Brought to light through escalated monitoring between late 2025 and June 2026, this campaign represents an industrialized escalation of identity-centric corporate compromise. Driven by an improved technical defense landscape that dropped email-phishing to a fraction of incidents, Scattered Spider pivoted completely to an interactive SaaS identity crisis strategy. A highlighted incident occurred in August 2025 when Scattered Spider forged a decentralized extortion alliance with Lapsus$ and ShinyHunters, deploying at least 16 collaborative Telegram communication channels under the moniker "Scattered LAPSUS$ Hunters". This represented a strategic shift from silent credential harvesting to chaotic, public-facing extortion operations. Major updates observed in early 2026 included the weaponization of native enterprise productivity tools; the group leveraged embedded AI assistants like Microsoft Copilot in compromised SharePoint networks to accelerate reconnaissance and map out privileged access groups. Furthermore, the campaign optimized helpdesk vishing execution to move from initial access to full domain administrator status in roughly 40 minutes, routinely exfiltrating terabytes of corporate data from distributed cloud spaces like Snowflake and AWS without deploying standard file-system malware.
	    
	- **Timeframe:** August 2025 – June 2026 (Ongoing).
	    
	- **Notable Tradecraft:** Caller-ID spoofing, highly interactive corporate helpdesk vishing, aggressive multi-channel MFA push-bombing, AzureHound post-compromise directory mapping, session hijacking, and AI-assisted cloud privilege discovery.
	    
	- **Targeted Organizations:** Enterprise software-as-a-service (SaaS) environments, multi-tenant cloud data platform customers (Snowflake), global technology companies, managed service providers (MSPs), and commercial retail entities.

## Malware & Tooling
* **Ransomware & RATs:** The group routinely deploys multi-platform ransomware payloads obtained from RaaS networks, specifically [[04_Malware/BlackCat]], [[04_Malware/DragonForce]], and [[04_Malware/BlackSuit]]. They leverage [[04_Malware/Chisel]] and [[04_Malware/Teleport]] to establish secure, interactive reverse tunnels over web channels.
* **Credential Theft & Loaders:** Information stealers like [[04_Malware/Lumma Stealer]] and [[04_Malware/Vidar Stealer]] are used to collect host credentials, while tools like Mimikatz are used to dump domain structures.
* **LOLBins & Remote Management Software:** Attackers heavily abuse legitimate Remote Monitoring and Management (RMM) utilities—including AnyDesk, TeamViewer, Citrix, and FleetDM—to maintain active connections without triggering traditional host-based malware signatures.
* **Notable Defensive Evasion Tooling:** The group uses custom driver manipulation scripts and tools to perform Bring Your Own Vulnerable Driver (BYOVD) operations, terminating active host monitoring systems.

## Exploited Vulnerabilities
* [[05_Vulnerabilities/CVE-2015-2291]]
  * **Exploitation Purpose:** Execution of Bring Your Own Vulnerable Driver (BYOVD) attacks.
  * **Exploitation Timing:** Post-exploitation privilege stability phase.
  * **Operational Impact:** Allows the threat actors to leverage a signed, vulnerable Intel network driver to execute arbitrary kernel-mode code, enabling them to completely disable or bypass running Endpoint Detection and Response (EDR) software.

## ATT&CK Tradecraft

### Initial Access
* [[02_TTPs/T1566.001 - Phishing- Spearphishing Attachment]]: Observed during localized outreach operations to deliver initial info-stealer attachments to targeted endpoints.
* [[02_TTPs/T1566.003 - Phishing- Spearphishing SMS]]: Mass deployment of SMS smishing lures simulating urgent HR notices or IT update requests to steer targets to lookalike SSO pages.

### Execution
* [[02_TTPs/T1059 - Command and Scripting Interpreter]]: Extensive use of administrative PowerShell environments and command prompt terminals to execute internal configuration scripts.

### Persistence
* [[02_TTPs/T1078 - Valid Accounts]]: Immediate hijacking and subsequent continuous usage of authorized enterprise accounts across Active Directory and Okta instances.
* [[02_TTPs/T1136.003 - Account Creation- Cloud Account]]: Generating hidden administrative accounts within Microsoft Entra ID or AWS environments to ensure secondary access pathways.

### Privilege Escalation
* [[02_TTPs/T1548 - Abuse Elevation Control Mechanism]]: Bypassing User Account Control (UAC) frameworks using custom administrative utilities like `PowerRun.exe` to trigger high-integrity processes.

### Defense Evasion
* [[02_TTPs/T1562 - Impair Defenses]]: Forcible termination of endpoint security services and stripping of active kernel telemetry hooks using BYOVD toolsets.
* [[02_TTPs/T1070 - Indicator Removal]]: Deleting Windows Event Logs using native utilities (`wevtutil`) and purging host prefetch data to disrupt active forensic tracking.

### Credential Access
* [[02_TTPs/T1621 - Multi-Factor Authentication Request Generation]]: Executing aggressive MFA fatigue and push-bombing scripts to swamp users until they accidentally accept access.
* [[02_TTPs/T1003.001 - OS Credential Dumping- LSASS Memory]]: Invoking direct memory extraction tools to harvest cleartext domain secrets out of local LSASS memory boundaries.

### Discovery
* [[02_TTPs/T1046 - Network Service Discovery]]: Running network scanning utilities like RustScan to enumerate accessible entry points across virtualized host architectures and ESXi targets.
* [[02_TTPs/T1538 - Cloud Service Dashboard]]: Browsing central cloud configuration management interfaces to map out accessible storage nodes and target databases.

### Lateral Movement
* [[02_TTPs/T1021 - Remote Services]]: Leveraging active internal RDP connections and abusing legitimate system tools to map and move across adjacent segments.

### Collection
* [[02_TTPs/T1530 - Data from Cloud Storage Object]]: Accessing and staging massive structural backups located across centralized cloud storage platforms like Snowflake and AWS S3 objects.

### Exfiltration
* [[02_TTPs/T1567.002 - Exfiltration Over Web Service- Exfiltration to Cloud Storage]]: Moving staged corporate data repositories to external MEGA accounts using legitimate cloud synchronization tools.

### Impact
* [[02_TTPs/T1486 - Data Encrypted for Impact]]: Triggering ransomware payloads across endpoints and hypervisors to obstruct business operations and apply financial pressure.
* [[02_TTPs/T1490 - Inhibit System Recovery]]: Automated destruction of volume shadow copy records and native recovery points to block restoration steps.

## Infrastructure & IOC Patterns
The threat cluster heavily relies on domain registration infrastructure built to mimic victim organizations' single sign-on (SSO) interfaces. Typical structural formats involve variations like `[victimname]-sso[.]com`, `[victimname]-okta[.]com`, or `[victimname]-portal[.]com`. External connectivity is routed via commercial virtual private servers (VPS) and legitimate cloud synchronization protocols to mask command-and-control (C2) paths within normal network traffic patterns.
* [[06_IOCs/login-microsoft365-auth[.]com]]
* [[06_IOCs/okta-verification-portal[.]com]]

## Detection Engineering Notes

### Behavioral Indicators
* Spikes in helpdesk service modification logs, specifically regarding sudden user password changes immediately followed by the registration of entirely new multi-factor authentication hardware keys.
* Process creation events invoking legacy, signed drivers (e.g., outdated Intel network utility files) followed by immediate configuration adjustments or service failures in local EDR tools.

### Detection Opportunities & Telemetry Requirements
* Monitor cloud authentication telemetry for sudden single sign-on changes, such as the introduction of new identity federation properties inside Microsoft Entra ID.
* Audit process command execution logs for remote utilities (e.g., Chisel, Ngrok) launching from unusual storage repositories like `%TEMP%` or `%USERPROFILE%\Downloads`.

### Log Sources
* Centralized identity provider logs (Okta, Entra ID, Ping Identity).
* Internal IT service management and helpdesk ticketing modification sequences.
* Endpoint process creation parameters and network egress records tracking known cloud synchronization domains.

## Intelligence Assessment
Scattered Spider remains an active, high-threat cybercriminal group characterized by rapid technical adjustments and highly effective social engineering tactics. Their ability to quickly master and weaponize a victim's internal SaaS configurations and operational frameworks gives them an edge over traditional static detection methods. The likelihood of operational escalation remains high as the cluster deepens its integration with underground ransomware developer networks and supply-chain access structures.

## Intelligence Gaps
* Granular mapping of the external initial access broker (IAB) supply networks that provide the target phone logs and personal data used to execute targeted helpdesk social engineering.
* Complete visibility into the development consistency and potential payload variations within their newly surfaced non-Windows binaries built for VMware ESXi environments.

## Recommended Defensive Actions

### Immediate
* Mandate the enforcement of phishing-resistant multi-factor authentication (such as FIDO2 security keys or device-bound passkeys) across all corporate accounts, prioritizing administrative and directory management access layers.

### Tactical
* Harden corporate helpdesk reset policies by requiring multi-layered out-of-band validation procedures to confirm identity, moving completely away from reliance on public personal information (such as SSN or birthdates).

### Strategic
* Enforce Endpoint Detection and Response (EDR) agents to operate strictly in block mode, ensuring that built-in tamper-protection capabilities are locked to prevent service modification or driver-abuse scripts.

### Long-Term
* Configure egress firewall filtering and network boundaries to prevent domain controller entities and core system elements from initiating outbound communication with unauthorized public data storage destinations or cloud sync portals.

## Related Threat Actors
* [[01_Threat_Actors/ALPHV]]: High operational overlap; Scattered Spider acts as a premier affiliate deploying their core BlackCat ransomware code in major extortion campaigns.
* [[01_Threat_Actors/ShinyHunters]]: Structural integration and shared communication avenues discovered across underground criminal marketplaces.
* [[01_Threat_Actors/Lapsus$]]: Shared behavioral patterns and tactical preferences, specifically around helpdesk social engineering, SIM-swapping, and extorting data from large enterprise environments.

## Sources
CISA & FBI. (2023). Joint Cybersecurity Advisory: Scattered Spider (AA23-320A). Washington, DC: CISA.

Microsoft Threat Intelligence. (2025). Protecting customers from Octo Tempest attacks across multiple industries. Redmond, WA: Microsoft.

Mandiant. (2024). UNC3944 Targets SaaS Applications. Milpitas, CA: Google Cloud.

## Changelog
* Created: 2026-06-22
* Updated: 2026-06-22
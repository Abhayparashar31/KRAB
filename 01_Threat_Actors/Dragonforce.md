---
entity_type: threat-actor
title: DragonForce
aliases:
  - Water Tambanakua
summary: A highly aggressive Russian-speaking Ransomware-as-a-Service (RaaS) syndicate and criminal cartel executing double-extortion campaigns globally across Windows, Linux, and VMware ESXi environments.
origin_country: Russia
suspected_sponsor: None
attribution_confidence: medium
actor_type: criminal
motivation:
  - Financial Gain
sophistication: high
operational_maturity: high
first_seen: 2023-08
last_seen: 2026-06
active: true
targeted_sectors:
  - Retail
  - Manufacturing
  - Healthcare
  - Government
  - Critical Infrastructure
  - Financial Services
targeted_regions:
  - Global
  - North America
  - Europe
  - Australia
  - Asia
targeted_platforms:
  - Windows OS
  - Linux OS
  - VMware ESXi
  - NAS Platforms
campaigns:
  - "[[03_Campaigns/2025-2026 Retail and Supply Chain Extortion Blitz]]"
  - "[[03_Campaigns/2025 Managed Service Provider Infiltration Wave]]"
malware_used:
  - "[[04_Malware/Munchkin]]"
  - "[[04_Malware/Cobalt Strike]]"
  - "[[Mamona]]"
  - "[[04_Malware/DragonForce]]"
ttps:
  - "[[02_TTPs/T1190 - Exploit Public-Facing Application]]"
  - "[[02_TTPs/T1078 - Valid Accounts]]"
  - "[[02_TTPs/T1059 - Command and Scripting Interpreter]]"
  - "[[02_TTPs/T1547 - Boot or Logon Autostart Execution]]"
  - "[[02_TTPs/T1068 - Exploitation for Privilege Escalation]]"
  - "[[02_TTPs/T1562 - Impair Defenses]]"
  - "[[02_TTPs/T1003.001 - OS Credential Dumping- LSASS Memory]]"
  - "[[02_TTPs/T1021.001 - Remote Services- Remote Desktop Protocol]]"
  - "[[02_TTPs/T1567.002 - Exfiltration Over Web Service- Exfiltration to Cloud Storage]]"
  - "[[02_TTPs/T1486 - Data Encrypted for Impact]]"
vulnerabilities_exploited:
  - "[[05_Vulnerabilities/CVE-2024-57727]]"
  - "[[05_Vulnerabilities/CVE-2024-57728]]"
  - "[[05_Vulnerabilities/CVE-2024-57726]]"
infrastructure:
  - "[[06_IOCs/dragonleaks-onion]]"
iocs:
  - "[[06_IOCs/185.220.101.1]]"
related_threat_actors:
  - "[[01_Threat_Actors/Scattered Spider]]"
  - "[[01_Threat_Actors/RansomHub]]"
related_collections: []
detection_opportunities:
  - Monitor for endpoint volume shadow copy and system state backup deletions using vssadmin or wbadmin tool execution loops.
  - Identify unauthorized execution of PsExec or WMI commands initiating unsigned Rust or Go binary execution configurations across hypervisors.
mitigations:
  - Deploy immediate patches for vulnerable remote monitoring and management architectures and public-facing boundary routers.
  - Implement strict Bring Your Own Vulnerable Driver mitigation baselines across enterprise endpoints to prevent kernel defense blinding.
references:
  - "Trend Micro. (2025). Ransomware Spotlight: DragonForce."
  - Sophos X-Ops. (2025). DragonForce actors target SimpleHelp vulnerabilities to attack MSP, customers.
  - "Analyst1. (2025). DragonForce: The Cyber Cartel Helping Hackers Hit the High Street."
source_reliability: A - Reliable
information_credibility: 1 - Confirmed by multiple sources
analytic_confidence: high
tlp: TLP:CLEAR
classification: Unclassified
created: 2026-06-23
updated: 2026-06-23
tags:
  - dragonforce
  - water-tambanakua
  - raas
  - cartel
  - ransomware
---

# DragonForce

## Executive Summary
DragonForce (tracked by security researchers under the alias Water Tambanakua) is an aggressive, operationally mature Ransomware-as-a-Service (RaaS) platform and cybercriminal cartel presenting a severe threat to global enterprise infrastructure. Rising to prominence between late 2023 and mid-2026, the group transitioned from deploying modified legacy leaked builders to managing an independent, highly automated double-extortion framework. DragonForce is operationally significant due to its multi-platform encryption engines targeting Windows, Linux, and VMware ESXi, alongside its strategic alliances with sophisticated initial access cells. Their primary targets cross critical infrastructure nodes, high-revenue retail networks, manufacturing supply links, and regional managed service providers (MSPs).

## Attribution Assessment
Based on code composition, structural linguistic artifacts within ransom communications, and underground platform positioning, DragonForce operators are assessed with medium confidence to be Russian-speaking threat actors operating within the CIS region. While early name tracking led to confusion with the Malaysia-based hacktivist collective "DragonForce Malaysia," forensic indicators show completely decoupled operational pipelines. DragonForce ransomware developers initially shared tooling roots with LockBit 3.0 leaked source code before developing a fully independent platform. They maintain loose, collaborative infrastructure ties and affiliate data sharing pools with [[01_Threat_Actors/Scattered Spider]] and modern fragments of the RaaS ecosystem.

## Operational Profile
The core operational objective of DragonForce is extracting multi-million dollar extortion settlements by employing tight dual-pressure frameworks through their dark web leak portal, "DragonLeaks." The group targets organizations opportunistically, prioritizing entities with revenue baselines exceeding $5,000,000 USD across North America, Europe, Australia, and parts of Asia. Preferred initial access vectors rely extensively on valid credential exploitation obtained from log brokers or targeting edge software systems. Once access is established, the group executes highly compressed operational cycles, moving laterally using native administrative components and completely blinding active endpoint detection solutions prior to deploying multi-threaded cryptographic file lockers.

## Campaign Activity (Apr 25-Jun 26)

* [[03_Campaigns/2025-2026 Retail and Supply Chain Extortion Blitz]]
  * **Operational Goal:** Compromise administrative backend frameworks of high-revenue commercial networks to exfiltrate proprietary transaction repositories.
  * **Description of the Campaign:** Throughout late 2025 and moving into mid-2026, DragonForce initialized an intensive campaign across the United States and United Kingdom. Working alongside [[01_Threat_Actors/Scattered Spider]], who facilitated entry points via interactive identity vishing, affiliates gained footholds inside core corporate domains. Operators quickly centralized and transferred massive data stores holding customer PII before triggering automated file lockers.
  * **Timeframe:** April 2025 – Ongoing into June 2026.
  * **Notable Tradecraft:** Multi-tenant session manipulation, helpdesk engineering, and high-velocity staging infrastructure.
  * **Targeted Organizations:** Global commercial chains, consumer goods suppliers, and luxury retail markets.

* [[03_Campaigns/2025 Managed Service Provider Infiltration Wave]]
  * **Operational Goal:** Compromise Managed Service Provider (MSP) infrastructure to push automated downstream ransomware payloads to client targets.
  * **Description of the Campaign:** In mid-2025, DragonForce affiliates orchestrated a highly disruptive supply-chain execution wave exploiting systemic remote tracking applications. By building out functional exploits against unpatched path traversal vulnerabilities in SimpleHelp instances, affiliates completely subverted master MSP environments. This allowed automated execution chains to drop ransomware payloads silently onto hundreds of downstream corporate target endpoints within a narrow execution window.
  * **Timeframe:** May 2025 – August 2025.
  * **Notable Tradecraft:** Remote Monitoring and Management (RMM) subversion, path traversal command parsing, and automated lateral network scripts.
  * **Targeted Organizations:** Regional Managed Service Providers (MSPs), medical medical centers, and local government data centers.

## Malware & Tooling
* **Cryptographic Frameworks:** The group utilizes [[04_Malware/DragonForce Ransomware]], an advanced multi-threaded encryption utility compiled across architecture platforms to seamlessly compromise Windows systems, Linux kernels, and VMware ESXi virtualization paths.
* **Evasion Environments:** Affiliates use [[04_Malware/Munchkin]], a highly locked-down, customized Alpine Linux ISO deployment wrapper. This execution shell isolates core tool execution from the parent operating system, blinding local EDR monitoring.
* **Command and Control:** Attackers employ customized instances of [[04_Malware/Cobalt Strike]] beacons to maintain active internal access lines.
* **Administrative Utilities:** Affiliates heavily leverage `PsExec`, `WMI`, and Advanced IP Scanner binaries to map local directories and script wide execution loops across domain structures.

## Exploited Vulnerabilities

* [[05_Vulnerabilities/CVE-2024-57727]]
  * **Exploitation Purpose:** Execute remote unauthenticated path traversal lookups to harvest configuration records.
  * **Exploitation Timing:** Exploited during the initial exploitation phase of the 2025 MSP wave.
  * **Operational Impact:** Allowed operators to view restricted database parameters and extract primary administrative configurations from SimpleHelp instances.

* [[05_Vulnerabilities/CVE-2024-57728]]
  * **Exploitation Purpose:** Upload unauthenticated malicious binary payloads directly onto management paths.
  * **Exploitation Timing:** Leveraged immediately following configuration discovery in mid-2025.
  * **Operational Impact:** Facilitated the direct placement of installer tools and automation modules into production file tracts.

* [[05_Vulnerabilities/CVE-2024-57726]]
  * **Exploitation Purpose:** Elevate low-privilege application accounts into full SYSTEM context.
  * **Exploitation Timing:** Executed as the final privilege escalation gate prior to fleet-wide execution.
  * **Operational Impact:** Bypassed standard role constraints, providing complete command execution authority over all connected downstream endpoints.

## ATT&CK Tradecraft

### Initial Access
* [[02_TTPs/T1190 - Exploit Public-Facing Application]]: Targeting unpatched vulnerabilities in boundary applications and remote monitoring infrastructure.
* [[02_TTPs/T1078 - Valid Accounts]]: Leveraging legitimate credentials bought from access markets to log directly into internal corporate endpoints.

### Execution
* [[02_TTPs/T1059 - Command and Scripting Interpreter]]: Orchestrating secondary internal steps via custom PowerShell scripts, batch automation arrays, and administrative terminal commands.

### Persistence
* [[02_TTPs/T1547 - Boot or Logon Autostart Execution]]: Forcing persistent local access by modifying startup behaviors or creating scheduled execution routines.

### Privilege Escalation
* [[02_TTPs/T1068 - Exploitation for Privilege Escalation]]: Triggering localized application privilege bugs to transform standard service context into absolute domain control.

### Defense Evasion
* [[02_TTPs/T1562 - Impair Defenses]]: Employing Bring Your Own Vulnerable Driver (BYOVD) exploits to terminate EDR monitoring processes at the kernel layer.

### Credential Access
* [[02_TTPs/T1003.001 - OS Credential Dumping- LSASS Memory]]: Extracting stored plaintext authentication variables from local subsystem memories via custom execution blocks.

### Lateral Movement
* [[02_TTPs/T1021.001 - Remote Services- Remote Desktop Protocol]]: Navigating across internal target servers using hijacked administrative accounts over internal remote desk connections.

### Exfiltration
* [[02_TTPs/T1567.002 - Exfiltration Over Web Service- Exfiltration to Cloud Storage]]: Transferring target database sets to secure off-site cloud folders using tools like Rclone or Exmatter.

### Impact
* [[02_TTPs/T1486 - Data Encrypted for Impact]]: Running multi-threaded encryption routines that natively stop virtualization hypervisors and dropping corporate ransom notices across target endpoints.

## Infrastructure & IOC Patterns
DragonForce runs a robust network back-end relying on bulletproof hosting blocks situated across non-cooperative legal spaces. Affiliates track targets using an automated administrative panel. On August 23, 2025, the cartel integrated a custom data analysis module onto their leak interface, automating file indexing and parsing to lower the technical barrier for third-party extortion monetization.
* **Leak Interface Portal:** `dragonleaks-onion`
* **Static Host Indicator:** `185.220.101[.]1`

## Detection Engineering Notes

### Behavioral Indicators
* Command executions forcefully suppressing machine boot recovery loops and dropping active volume snapshots:
  * `vssadmin.exe delete shadows /all /quiet`
  * `wbadmin.exe delete systemstatebackup`
  * `bcdedit.exe /set {default} recoveryenabled No`

### Detection Opportunities
* Flag instances where unverified virtual disk images or Alpine Linux setups (`Munchkin` behaviors) generate high-volume outbound network queries across local hypervisor nodes.
* Audit endpoint system logs for anomalous kernel driver load flags, which may indicate a BYOVD execution path targeting local defense tools.

### Log Sources
* Endpoint Detection and Response (EDR) telemetry tracking.
* Windows Event Logs (Event IDs 4624, 7045, 4688).
* VMware ESXi administrative syslog records and RMM management console transaction charts.

### Telemetry Requirements
* Monitoring active process command arguments, tracking kernel driver hashes, and identifying sudden network mapping activities stemming from single localized accounts.

## Intelligence Assessment
DragonForce represents a sophisticated, highly adaptive threat syndicate whose shift to a formalized ransomware cartel model demonstrates sophisticated commercial growth. Their technical capability to exploit supply chain channels through MSP vectors, combined with an aggressive multi-platform malware footprint, makes them a significant threat to global networks. The group's deployment of a specialized data analysis architecture on August 23, 2025, reflects an ongoing operational evolution toward specialized data monetization. It is highly likely that DragonForce will continue to refine its alliances with skilled social-engineering cells, resulting in rapid, high-impact intrusion cycles targeting enterprise perimeters throughout 2026.

## Intelligence Gaps
* The detailed organizational agreements and exact infrastructure links between core cartel operators and historical regional hacktivist entities.
* Comprehensive technical mapping of the exact parsing libraries driving their updated data analysis module.
* Complete visibility into the total volume of specific vulnerable third-party driver binaries used across separate affiliate teams.

## Recommended Defensive Actions

### Immediate
* Apply out-of-band security updates across all public-facing remote monitoring infrastructures (specifically patching SimpleHelp vulnerability footprints).
* Verify backup isolation parameters, ensuring primary production domains cannot map to repository roots.

### Tactical
* Configure rigid application protection constraints to intercept unverified kernel driver load attempts and mitigate BYOVD exploitation patterns.
* Enforce network routing constraints that block direct inter-subnet `PsExec` and raw WMI execution scripts between non-management terminal nodes.

### Strategic
* Migrate central identity structures to phishing-resistant authentication frameworks (FIDO2 keys) to prevent credential compromise via vishing loops.

### Long-Term
* Implement end-to-end telemetry auditing and strict data isolation perimeters over all integrated vendor connections and third-party Managed Service Provider networks.

## Related Threat Actors
* [[01_Threat_Actors/Scattered Spider]]: Collaborated directly as an initial access broker, providing production network entry vectors to facilitate downstream DragonForce ransomware execution.
* [[01_Threat_Actors/RansomHub]]: Functions as a primary operational competitor; DragonForce publicly targeted RansomHub's affiliate network in mid-2025 to scale its cartel infrastructure.

## Sources
Analyst1. (2025). DragonForce: The Cyber Cartel Helping Hackers Hit the High Street. Analyst1 Cyber Research.

Sophos X-Ops. (2025). DragonForce actors target SimpleHelp vulnerabilities to attack MSP, customers. Sophos Threat Research Blog.

Trend Micro. (2025). Ransomware Spotlight: DragonForce. Trend Micro Research Insights.

## Changelog
* Created: 2026-06-23
* Updated: 2026-06-23
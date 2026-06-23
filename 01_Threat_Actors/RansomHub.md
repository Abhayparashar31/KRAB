---
entity_type: threat-actor
title: RansomHub
aliases:
  - Cyclops
  - Knight
summary: RansomHub is a highly efficient and prolific Ransomware-as-a-Service (RaaS) operation that emerged in February 2024. Operating under a double-extortion model, it has rapidly targeted over 210 organizations globally across critical infrastructure sectors, including healthcare, water, and information technology.
origin_country: Unknown
suspected_sponsor: null
attribution_confidence: medium
actor_type: cybercrime_group
motivation:
  - financial
sophistication: high
operational_maturity: high
first_seen: 2024-02-02
last_seen: 2026-06-23
active: true
targeted_sectors:
  - Water and Wastewater Systems
  - Information Technology
  - Government Facilities
  - Healthcare and Public Health
  - Emergency Services
  - Food and Agriculture
  - Financial Services
  - Commercial Facilities
  - Aerospace
  - Defense
  - Agriculture
  - Automotive
  - Retail
targeted_regions:
  - Global
  - United States
  - United Kingdom
  - Europe
targeted_platforms:
  - Windows
  - Linux
  - ESXi
campaigns:
  - "[[03_Campaigns/RansomHub Critical Infrastructure Surge]]"
  - "[[03_Campaigns/Change Healthcare Residual Extortion Escalation]]"
malware_used:
  - "[[04_Malware/RansomHub Encryptor]]"
  - "[[04_Malware/EDRKillShifter]]"
  - "[[04_Malware/Cobalt Strike]]"
  - "[[04_Malware/Mimikatz]]"
  - "[[04_Malware/Rclone]]"
  - "[[04_Malware/WinSCP]]"
  - "[[04_Malware/PuTTY]]"
  - "[[04_Malware/Nmap]]"
  - "[[04_Malware/AngryIPScanner]]"
  - "[[04_Malware/Metasploit]]"
ttps:
  - "[[02_TTPs/T1190 - Exploit Public-Facing Application]]"
  - "[[02_TTPs/T1566.001 - Phishing- Spearphishing Attachment]]"
  - "[[02_TTPs/T1110.003 - Brute Force- Password Spraying]]"
  - "[[02_TTPs/T1059 - Command and Scripting Interpreter]]"
  - "[[02_TTPs/T1047 - Windows Management Instrumentation]]"
  - "[[02_TTPs/T1078 - Valid Accounts]]"
  - "[[02_TTPs/T1068 - Exploitation for Privilege Escalation]]"
  - "[[02_TTPs/T1562.001 - Impair Defenses- Disable or Modify Tools]]"
  - "[[02_TTPs/T1070.004 - Indicator Removal- File Deletion]]"
  - "[[02_TTPs/T1003 - OS Credential Dumping]]"
  - "[[02_TTPs/T1046 - Network Service Discovery]]"
  - "[[02_TTPs/T1082 - System Information Discovery]]"
  - "[[02_TTPs/T1021.001 - Remote Services- Remote Desktop Protocol]]"
  - "[[02_TTPs/T1119 - Automated Collection]]"
  - "[[02_TTPs/T1020 - Automated Exfiltration]]"
  - "[[02_TTPs/T1486 - Data Encrypted for Impact]]"
  - "[[02_TTPs/T1489 - Service Stop]]"
vulnerabilities_exploited:
  - "[[05_Vulnerabilities/CVE-2023-3519]]"
  - "[[05_Vulnerabilities/CVE-2023-27997]]"
  - "[[05_Vulnerabilities/CVE-2023-46604]]"
  - "[[05_Vulnerabilities/CVE-2023-22515]]"
  - "[[05_Vulnerabilities/CVE-2023-46747]]"
  - "[[05_Vulnerabilities/CVE-2023-48788]]"
  - "[[05_Vulnerabilities/CVE-2020-1472]]"
  - "[[05_Vulnerabilities/CVE-2020-0787]]"
infrastructure: []
iocs:
  - "[[06_IOCs/How To Restore Your Files.txt]]"
  - "[[06_IOCs/README_]]"
related_threat_actors:
  - "[[01_Threat_Actors/LockBit]]"
  - "[[01_Threat_Actors/ALPHV BlackCat]]"
related_collections: []
detection_opportunities: []
mitigations: []
references:
  - "Federal Bureau of Investigation, Cybersecurity and Infrastructure Security Agency. (2024). #StopRansomware: RansomHub Ransomware (AA24-242A). CISA."
  - "Arete Incident Response. (2024). Malware Spotlight: RansomHub Ransomware. Arete."
  - "Cyble. (2024). Critical Advisory on RansomHub Ransomware: A Comprehensive Analysis and Mitigation Guide. Cyble."
  - "TXOne Networks. (2024). Inside RansomHub: Anatomy of an OT-Focused Operation. TXOne."
source_reliability: high
information_credibility: high
analytic_confidence: high
tlp: CLEAR
classification: UNCLASSIFIED
created: 2026-06-23
updated: 2026-06-23
tags:
  - threat-actor
  - raas
  - ransomhub
  - cybercrime
  - extortion
---

# Executive Summary
RansomHub is a highly organized, active, and sophisticated Ransomware-as-a-Service (RaaS) platform that first emerged in February 2024. The group employs an aggressive double-extortion operational model, combining fast intermittent data encryption on target hosts with data exfiltration to their dedicated dark web leaks platform. RansomHub has rapidly established itself as one of the most prolific ransomware syndicates globally, effectively capitalizing on the vacuum left by the law enforcement disruption of legacy networks like [[01_Threat_Actors/LockBit]] and [[01_Threat_Actors/ALPHV BlackCat]]. The group operates under a highly appealing affiliate model, providing decentralized operators up to a 90% payout. Its primary targets span multiple critical infrastructure sectors globally, including healthcare, information technology, government facilities, and water networks. Its strategic relevance lies in its high operational maturity, rapid expansion, and tactical adaptability across multiple target platforms.

# Attribution Assessment
* **Attribution Status:** Unattributed / Independent Cybercriminal Syndicate
* **Known Aliases:** Cyclops, Knight
* **Sponsoring Nation or Organization:** None
* **Confidence Level:** Medium
* **Overlaps with other tracked groups:** Strong operational and malware code overlaps indicate that RansomHub represents an evolution or direct rebrand of the Knight (formerly Cyclops) ransomware family. Additionally, following the systemic disruption and exit-scam activities of [[01_Threat_Actors/LockBit]] and [[01_Threat_Actors/ALPHV BlackCat]] in early 2024, a massive influx of legacy affiliates migrated to the RansomHub ecosystem. This massive movement resulted in significant infrastructure, toolset, and tradecraft overlap with actions previously tracked under other cybercrime banners.
* **Reporting Consistency:** High. Major international cybersecurity authorities (including CISA, FBI, HHS, and MS-ISAC) and private sector CTI teams maintain a unified tracking profile of RansomHub as a global multi-affiliate network.

# Operational Profile
* **Operational Objectives:** Financial extraction via system-wide extortion, intellectual property theft, and corporate data commoditization.
* **Targeting Patterns:** Opportunistic initial entry mixed with highly targeted post-exploitation targeting of high-revenue enterprises. The group deliberately prioritizes industries with low tolerance for downtime, such as clinical networks or municipal utilities, to amplify payment pressure.
* **Victimology:** Cross-sector targeting with focus on Water and Wastewater Systems, Information Technology, Government Services, Healthcare, Emergency Services, and Financial Institutions.
* **Geographic Focus:** Globally distributed, with heavily documented concentrations in the United States, United Kingdom, European Union, and Australia.
* **Intrusion Behavior:** Highly streamlined execution post-breach. Affiliates prioritize rapid credential harvesting, host mapping via dual-use administration tools, the blinding of endpoint detection agents, and comprehensive file staging before deploying the final ransomware payload.
* **Preferred Access Vectors:** Perimeter exploitation of unpatched public-facing appliances, corporate password spraying against weak authentication setups, and specialized spear-phishing campaigns.
* **Persistence Style:** Maintenance of continuous access via compromised valid administrative accounts, installation of remote monitoring tools, and interactive backup shells.
* **Post-Exploitation Behavior:** Heavy reliance on Living-off-the-Land (LotL) tactics, utilizing native command interpreters, management infrastructure, and custom helper applications to disable defense telemetry, drop logs, and suppress local system automated recovery capabilities.

# Campaign Activity (Past 14 Months Time Period: April 2025 - June 2026)
* [[03_Campaigns/RansomHub Critical Infrastructure Surge]]
  * **Operational Goal:** Extortion and monetization via systematic targeting of industrial control networks and public utilities.
  * **Description:** A concerted series of operations focusing heavily on Operational Technology (OT) environments, SCADA networks, and municipal water treatment facilities across North America and Europe to enforce immediate compliance with ransom terms.
  * **Timeframe:** May 2025 - November 2025
  * **Notable Tradecraft:** Use of Bring Your Own Vulnerable Driver (BYOVD) toolsets, exploitation of edge firewalls, and selective data scraping from localized network shares.
* [[03_Campaigns/Change Healthcare Residual Extortion Escalation]]
  * **Operational Goal:** Secondary monetization of data assets acquired from legacy breaches.
  * **Description:** RansomHub facilitated the public hosting, sale, and targeted re-extortion of compromised sensitive healthcare logs originally exfiltrated during the ALPHV/BlackCat compromise, demonstrating cross-group data commoditization.
  * **Timeframe:** April 2025 - June 2025
  * **Notable Tradecraft:** Tor data leak site monetization, negotiation matching via custom corporate portals, and public data doxxing.

# Targeted Organizations
* **Water and Wastewater Systems:** Municipal water facilities and treatment networks throughout North America.
* **Healthcare and Public Health:** Regional hospital groups, medical cloud operators, and healthcare management portals.
* **Information Technology:** Managed Service Providers (MSPs), internet gateways, and software distribution channels.
* **Government Facilities:** Municipal network backbones, county services databases, and local agency infrastructure.

# Malware & Tooling
* **Loaders & Droppers:** Custom Go and C++ based compilation stubs designed to drop or inject obfuscated binaries into system processes.
* **RATs & Offensive Frameworks:**
  - [[04_Malware/Cobalt Strike]] - Leveraged extensively for interactive operational command and internal lateral movement.
  - [[04_Malware/Metasploit]] - Used during post-breach network exploration for automated internal exploitation.
* **Credential Theft Tools:**
  - [[04_Malware/Mimikatz]] - Utilized to execute active memory dumping and capture active session tokens.
* **Custom Malware & Evasion Tools:**
  - [[04_Malware/EDRKillShifter]] - A specialized executable loader used to implement Bring Your Own Vulnerable Driver (BYOVD) attacks, injecting outdated or vulnerable signed drivers to terminate security processes from kernel space.
* **Exfiltration Utilities:**
  - [[04_Malware/Rclone]] - Heavily favored tool for multi-threaded data transfers to cloud service buckets.
  - [[04_Malware/WinSCP]] - Utilized to securely copy gathered data files out to actor-controlled servers.
* **LOLBins & Administrative Tools:**
  - `vssadmin.exe` - Systematically invoked to destroy system local volume copies.
  - `PowerShell` - Extensively used to run configuration scripts and handle domain enumeration.
  - `WMI` - Employed to force-stop system background defense applications and strip anti-malware tracking.

# Exploited Vulnerabilities
* [[05_Vulnerabilities/CVE-2023-3519]]
  - **Exploitation Purpose:** Remote Code Execution (RCE) on unprotected Citrix ADC and Gateway endpoints.
  - **Exploitation Timing:** Initial compromise phase.
  - **Operational Impact:** Permits unauthenticated adversaries to execute code on edge architecture, establishing a high-privilege perimeter foothold.
* [[05_Vulnerabilities/CVE-2020-1472]]
  - **Exploitation Purpose:** Core privilege escalation within Active Directory via Netlogon protocol flaws (Zerologon).
  - **Exploitation Timing:** Lateral movement phase.
  - **Operational Impact:** Enables immediate acquisition of complete Domain Administrator privileges from an unprivileged position.
* [[05_Vulnerabilities/CVE-2023-27997]]
  - **Exploitation Purpose:** Heap overflow execution within Fortinet FortiGate VPN systems.
  - **Exploitation Timing:** Initial access phase.
  - **Operational Impact:** Grants unauthorized external access into secure corporate network rings without user interaction.

# ATT&CK Tradecraft

### Initial Access
* [[02_TTPs/T1190 - Exploit Public-Facing Application]]
  - Procedural Example: Scanning and weaponizing unpatched public-facing appliances (Citrix, Fortinet, F5) to execute reverse shells.
* [[02_TTPs/T1566.001 - Phishing- Spearphishing Attachment]]
  - Procedural Example: Delivering tailored corporate communications with weaponized macros or archive links to accounting or HR personnel.
* [[02_TTPs/T1110.003 - Brute Force- Password Spraying]]
  - Procedural Example: Executing automated single-password verification sweeps across internet-facing portals against wide corporate rosters.

### Execution
* [[02_TTPs/T1059 - Command and Scripting Interpreter]]
  - Procedural Example: Direct execution of automated PowerShell modules to pass variables, pull payloads, and handle bulk configurations.
* [[02_TTPs/T1047 - Windows Management Instrumentation]]
  - Procedural Example: Interrogating active system tables via WMI commands to locate connected backup servers and trace infrastructure assets.

### Persistence
* [[02_TTPs/T1078 - Valid Accounts]]
  - Procedural Example: Creating or hijacking permanent domain service credentials to maintain network access during administrative password resets.

### Privilege Escalation
* [[02_TTPs/T1068 - Exploitation for Privilege Escalation]]
  - Procedural Example: Actively launching tools targeting internal flaws like Zerologon on domain controllers to immediately force privilege elevation.

### Defense Evasion
* [[02_TTPs/T1562.001 - Impair Defenses- Disable or Modify Tools]]
  - Procedural Example: Deploying the custom [[04_Malware/EDRKillShifter]] asset to install a vulnerable hardware driver, using it to forcefully strip endpoint security agents out of kernel operations.
* [[02_TTPs/T1070.004 - Indicator Removal- File Deletion]]
  - Procedural Example: Relying on scripts to scrub active Windows Application and System Security event logs to obstruct post-incident investigation.

### Credential Access
* [[02_TTPs/T1003 - OS Credential Dumping]]
  - Procedural Example: Extracting active user passwords and NT hashes from the local LSASS space using customized Mimikatz binaries.

### Discovery
* [[02_TTPs/T1046 - Network Service Discovery]]
  - Procedural Example: Running internal ping sweeps and mapping targets via open-source tools like AngryIPScanner or Nmap.
* [[02_TTPs/T1082 - System Information Discovery]]
  - Procedural Example: Built-in checks within the ransomware engine parsing hostname strings and disk geometry before beginning lock cycles.

### Lateral Movement
* [[02_TTPs/T1021.001 - Remote Services- Remote Desktop Protocol]]
  - Procedural Example: Pivotting through the network using native administrative RDP connections paired with compromised domain keys.

### Collection
* [[02_TTPs/T1119 - Automated Collection]]
  - Procedural Example: Utilizing automated data scraping tools to collect full contact spreadsheets, loyalty profiles, and code repository files into internal cloud staging areas.

### Exfiltration
* [[02_TTPs/T1020 - Automated Exfiltration]]
  - Procedural Example: Activating multi-threaded Rclone uploads pushing collected data staging archives straight into remote Amazon S3 storage buckets.

### Impact
* [[02_TTPs/T1486 - Data Encrypted for Impact]]
  - Procedural Example: Deploying the main Go/C++ executable to carry out intermittent encryption, locking 0x100000 byte sections while skipping 0x200000 byte blocks across local and network targets.
* [[02_TTPs/T1489 - Service Stop]]
  - Procedural Example: Halting foundational production services (such as MS Exchange, Oracle, or hypervisors) to clear open file holds, enabling unhindered data encryption.

# Infrastructure & IOC Patterns
RansomHub operates a highly partitioned network framework:
* **Tor Infrastructure:** The group utilizes high-availability onion routing configurations to keep their target leak portals and interactive chat spaces online. Each compromise is assigned a distinct client reference tag that allows entry only into a designated, locked communication module.
* **Exfiltration Framework:** Rather than deploying custom file-hosting command nodes, affiliates exploit established public cloud ecosystems. Staged content is systematically routed into short-lived, actor-controlled Amazon S3 endpoints or anonymous web storage spaces.
* **Command & Control VPS:** Affiliates stand up temporary interactive C2 management nodes on infrastructure procured from bulletproof hosting entities via cryptocurrency. These structures often leverage generic SSL layers or mimic typical corporate cloud signatures to mask communications.

Notable IOC categories include:
* [[06_IOCs/How To Restore Your Files.txt]]
* [[06_IOCs/README_]]

# Detection Engineering Notes
* **Behavioral Indicators:**
  - Deployment and instantaneous activation of deprecated, historically vulnerable signed drivers followed by the unexpected crash or cessation of active endpoint protection processes.
  - Programmatic process invocation of `vssadmin.exe delete shadows /all /quiet` or related WMI strings.
  - Automated, rapid data connections established from staging hosts toward cloud storage providers using standalone command-line network tools.
* **Log Sources:** Windows Security Event Log (Logon tracking via Event ID 4624), Windows PowerShell Operational Log (Script execution tracking via Event ID 4104), Sysmon (Process tracking via Event ID 1, File modification via Event ID 11, DNS mapping via Event ID 22), and central perimeter egress firewall logs.
* **KQL Query Example (EDR/Shadow Copy Removal Detection):**
```kql
DeviceProcessEvents
| where ProcessCommandLine has "vssadmin" and ProcessCommandLine has "delete" and ProcessCommandLine has "shadows"
| union (
    DeviceProcessEvents
    | where ProcessCommandLine has "wmic" and ProcessCommandLine has "shadowcopy" and ProcessCommandLine has "delete"
)
| project TimeGenerated, DeviceName, AccountName, InitiatingProcessFileName, ProcessCommandLine
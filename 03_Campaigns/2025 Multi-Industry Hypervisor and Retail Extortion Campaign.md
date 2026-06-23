---
entity_type: campaign
title: "2025 Multi-Industry Hypervisor and Retail Extortion Campaign"
aliases: ["Hypervisor Retail Sweep 2025"]
summary: "A devastating multi-vector ransomware and double-extortion campaign focused on compromising virtualization layers, specifically VMware ESXi infrastructures, and targeting global retail and supply chain organizations."
first_seen: "2025-01-15"
last_seen: "2025-12-20"
status: "Completed"
attribution: "[[01_Threat_Actors/RansomHub]]"
attribution_confidence: "high"
targeted_sectors: ["Retail", "Logistics", "Commercial Facilities"]
targeted_regions: ["United States", "Europe", "Australia"]
targeted_technologies: ["VMware ESXi", "Linux", "Windows Server"]
objectives: ["Financial Extraction", "Operational Disruption"]
threat_actors: ["[[01_Threat_Actors/RansomHub]]"]
malware: ["[[04_Malware/RansomHub Encryptor]]", "[[04_Malware/EDRKillShifter]]", "[[04_Malware/Rclone]]"]
vulnerabilities: ["[[05_Vulnerabilities/CVE-2023-3519]]", "[[05_Vulnerabilities/CVE-2023-46604]]"]
ttps: ["[[02_TTPs/T1190 - Exploit Public-Facing Application]]", "[[02_TTPs/T1562.001 - Impair Defenses- Disable or Modify Tools]]", "[[02_TTPs/T1486 - Data Encrypted for Impact]]", "[[02_TTPs/T1489 - Service Stop]]", "[[02_TTPs/T1020 - Automated Exfiltration]]"]
related_iocs: ["[[06_IOCs/How To Restore Your Files.txt]]"]
infection_vectors: ["Edge Appliance Exploitation", "BYOVD Evasion"]
infrastructure_patterns: ["Bulletproof hosting VPS networks", "Tor negotiations architecture"]
victimology: ["High-revenue retail conglomerates and distributed inventory supply hubs with dependencies on central hypervisor engines."]
detection_opportunities: ["Sudden programmatic shutdown commands issued to ESXi command lines via local scripts.", "Kernel space loading of unsigned or deprecated driver payloads."]
mitigations: ["Disable SSH endpoints on VMware ESXi hypervisors.", "Enforce strict host credential separation patterns.", "Implement immutable, air-gapped backup networks."]
references: ["Cybersecurity and Infrastructure Security Agency. (2025). RansomHub Campaigns Targeting Hypervisors.", "CrowdStrike. (2025). The 2025 Retail Ransomware Vector Analysis."]
source_reliability: "high"
information_credibility: "high"
analytic_confidence: "high"
tags: ["campaign", "hypervisor", "esxi", "retail", "ransomhub", "extortion"]
created: "2026-06-23"
updated: "2026-06-23"
author: "Senior Cyber Threat Intelligence Analyst"
---

# 2025 Multi-Industry Hypervisor and Retail Extortion Campaign

## Executive Summary
The 2025 Multi-Industry Hypervisor and Retail Extortion Campaign represents a highly structured and operationally aggressive effort by [[01_Threat_Actors/RansomHub]] to maximize financial leverage by crippling the central virtualization cores of multi-national retail chains. By executing Bring Your Own Vulnerable Driver (BYOVD) tactics to mask operations and pivoting directly into ESXi infrastructure environments, the threat actors paralyzed supply-chain tracking systems and point-of-sale backends. This campaign underscores a critical shift where threat networks avoid individual host deployment to focus on the systematic destruction of underlying hypervisors to force rapid extortion compliance.

## Campaign Overview
The intrusion methodology relied heavily on the swift weaponization of perimeter edge devices, using known flaws like [[05_Vulnerabilities/CVE-2023-3519]] to drop initial interactive access configurations. Once inside corporate management planes, affiliates deployed the custom [[04_Malware/EDRKillShifter]] utility to disable kernel security visibility. 

With security tracking neutralized, operations pivoted towards active domain controllers to extract high-privilege virtualization keys. Rather than spending time encrypting distributed user endpoints, the adversaries immediately routed to center-stage ESXi clusters. Leveraging automated bash commands via SSH access, the actors dropped active background virtual machines, wiped volume backups, and launched the [[04_Malware/RansomHub Encryptor]] optimized for Linux architectures. In parallel, multi-threaded data harvesters utilized [[04_Malware/Rclone]] to siphon core customer transaction data to external storage assets.

## Threat Actor Associations
* **[[01_Threat_Actors/RansomHub]]**: Planned, customized, and executed the baseline delivery, payload adjustments, and the double-extortion lifecycles over the entire 12-month campaign window.

## Malware & Tooling
* **[[04_Malware/RansomHub Encryptor]]**: Core Go/C++ cross-platform locking application configured with parameters for fast block-skipping encryption routines on Linux systems.
* **[[04_Malware/EDRKillShifter]]**: Specialized execution stub dropping vulnerable signed drivers to target and disable active endpoint detection processes from ring 0.
* **[[04_Malware/Rclone]]**: Open-source synchronization command asset repurposed for fast background data exfiltration loops.

## Exploited Vulnerabilities
* [[05_Vulnerabilities/CVE-2023-3519]]: Weaponized during the early compromise windows to gain unauthenticated remote execution footholds on network perimeter appliances.
* [[05_Vulnerabilities/CVE-2023-46604]]: Exploited to handle remote internal execution across secondary management applications.

## ATT&CK Tradecraft

### Initial Access
* [[02_TTPs/T1190 - Exploit Public-Facing Application]]: Finding and exploiting unpatched edge infrastructure to launch interactive command lines.

### Execution
* [[02_TTPs/T1059 - Command and Scripting Interpreter]]: Pushing malicious bash scripts directly to hypervisor terminal connections.

### Persistence
* [[02_TTPs/T1078 - Valid Accounts]]: Hijacking native administrative hypervisor keys to ensure continuous control over virtualization environments.

### Defense Evasion
* [[02_TTPs/T1562.001 - Impair Defenses- Disable or Modify Tools]]: Utilizing BYOVD techniques via [[04_Malware/EDRKillShifter]] to disable EDR monitoring layers.

### Discovery
* [[02_TTPs/T1046 - Network Service Discovery]]: Executing internal sweeps to catalog hypervisor control panels and centralized SAN configurations.

### Lateral Movement
* [[02_TTPs/T1021.001 - Remote Services- Remote Desktop Protocol]]: Bouncing internally from compromised workstations to hypervisor management servers.

### Collection
* [[02_TTPs/T1119 - Automated Collection]]: Running commands to locate and stage database images hosting customer data profiles.

### Exfiltration
* [[02_TTPs/T1020 - Automated Exfiltration]]: Directing structured data out via [[04_Malware/Rclone]] straight to external cloud assets.

### Impact
* [[02_TTPs/T1486 - Data Encrypted for Impact]]: Running cross-platform encryption modules directly over central virtual machine storage arrays (`.vmdk`).
* [[02_TTPs/T1489 - Service Stop]]: Invoking `esxcli` parameters to gracefully kill active guest operations to open file blocks for encryption.

## Infrastructure & IOC Patterns
The actors deployed distinct, dedicated command proxies routed through regional data center providers to blend tracking signatures. File staging and leak scheduling utilized customized dark web nodes.
* **Ransom Indicator:** [[06_IOCs/How To Restore Your Files.txt]]

## Victimology
The victim selection parameters focused on high-volume, multi-national retail chains, e-commerce backend distributors, and commercial logistics warehouses holding low-downtime thresholds across the US, UK, and European regions.

## Detection & Hunting

### Behavioral Indicators
* Immediate termination patterns across local system security processes coupled with unverified kernel-level hardware driver registration.
* Creation of rapid SSH command profiles targeting ESXi hosts executing mass VM suspension sequences (`vim-cmd vmsvc/power.off`).

### Detection Opportunities
* Monitor authentication logs for sudden administrative access into virtualization suites originating from non-standard internal network zones.

### Log Sources
* ESXi syslog profiles (`/var/log/syslog.log` and `/var/log/hostd.log`).
* Endpoint Detection (EDR) driver load logs.
* Core network flow logs showing unexpected cloud backup uploads.

### Telemetry Requirements
* Central aggregation of hypervisor command histories and host kernel manipulation flags.

### Hunt Ideas
* Search for any internal occurrences of `vssadmin` or `esxcli` service stop strings executed across compressed windows.

## Intelligence Assessment
The campaign highlights RansomHub’s expansion into virtualization layer operations. By directly disabling EDR tooling and focusing encryption efforts on single hypervisor hosts, the group dramatically contracted defensive reaction times. This operational baseline will highly likely continue as standard multi-platform cybercrime networks mature their Linux encryption capabilities.

## Mitigations

### Immediate
* Revoke broad network-level SSH permissions across all active ESXi clusters.
* Terminate outdated or unneeded storage sync connections.

### Tactical
* Enforce absolute multi-factor validation requirements for any hypervisor control panel interaction.
* Implement driver blocklists to prevent BYOVD execution.

### Strategic
* Migrate completely to immutable, air-gapped data retention architectures entirely independent of active corporate domain structures.

## Sources
Cybersecurity and Infrastructure Security Agency. (2025). *#StopRansomware: RansomHub Hypervisor Tactics (AA25-104A)*. CISA.

CrowdStrike. (2025). *Threat Report: Overcoming Hypervisor Compromise in the Retail Space*. Austin, TX.

## Changelog
* Created: 2026-06-23
* Updated: 2026-06-23
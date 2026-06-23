---
entity_type: campaign
title: "FIN7"
aliases: ["Carbon Spider", "GOLD NIAGARA", "ELBRUS", "Sangria Tempest", "ITG14", "Carbanak"]
summary: "A highly resilient, sophisticated, and financially motivated cybercriminal enterprise originating from Eastern Europe, specializing in high-value corporate targeting, advanced social engineering, and strategic big game hunting ransomware operations."
origin_country: "Russia"
suspected_sponsor: "None"
attribution_confidence: "high"
actor_type: "criminal"
motivation: ["Financial Gain"]
sophistication: "high"
operational_maturity: "high"
first_seen: "2013-11"
last_seen: "2026-06"
active: true
targeted_sectors: ["Retail", "Restaurant", "Hospitality", "Automotive", "Defense", "Transportation", "Financial Services", "Pharmaceutical"]
targeted_regions: ["North America", "Europe", "Global"]
targeted_platforms: ["Windows OS", "Linux OS"]
campaigns: ["[[03_Campaigns/2025-2026 US Automotive and Supply Chain Infiltration Campaign]]", "[[03_Campaigns/Big Game Hunting Ransomware Deployments]]"]
malware_used: ["[[04_Malware/Carbanak]]", "[[04_Malware/DiceLoader]]", "[[04_Malware/Lizar]]", "[[04_Malware/Anunak]]", "[[04_Malware/POWERTRASH]]", "[[04_Malware/Cobalt Strike]]"]
ttps: ["[[02_TTPs/T1566.002 - Phishing- Spearphishing Link]]", "[[02_TTPs/T1059.001 - Command and Scripting Interpreter- PowerShell]]", "[[02_TTPs/T1547.001 - Boot or Logon Autostart Execution- Registry Run Keys / Startup Folder]]", "[[02_TTPs/T1068 - Exploitation for Privilege Escalation]]", "[[02_TTPs/T1562.001 - Impair Defenses- Disable or Modify Tools]]", "[[02_TTPs/T1003.001 - OS Credential Dumping- LSASS Memory]]", "[[02_TTPs/T1082 - System Information Discovery]]", "[[02_TTPs/T1021.001 - Remote Services- Remote Desktop Protocol]]", "[[02_TTPs/T1114 - Email Collection]]", "[[02_TTPs/T1567.002 - Exfiltration Over Web Service- Exfiltration to Cloud Storage]]", "[[02_TTPs/T1486 - Data Encrypted for Impact]]"]
vulnerabilities_exploited: []
infrastructure: ["[[06_IOCs/advanced-ip-sccanner[.]com]]"]
iocs: ["[[06_IOCs/advanced-ip-sccanner[.]com]]"]
related_threat_actors: ["[[01_Threat_Actors/ALPHV]]", "[[01_Threat_Actors/Scattered Spider]]", "[[01_Threat_Actors/RansomHub]]"]
related_collections: []
detection_opportunities: ["Monitor for typosquatted administrative utility downloads routing to unauthorized external storage nodes.", "Identify POWERTRASH execution vectors unpacking reflective code scripts via PowerShell transcript logging blocks."]
mitigations: ["Enforce rigid external network DNS filtering protocols to isolate lookalike typosquatted domain mappings.", "Implement strict localized account execution rules blocking unsigned administrative components from initializing external data shells."]
references: ["Arctic Wolf. (2024). Threat Group FIN7 Targets the U.S. Automotive Industry. Arctic Wolf Labs.", "MITRE ATT&CK. (2026). FIN7 Group Profile G0046. MITRE Corporation.", "Huntress. (2024). FIN7 Cybercrime Group - Tactics, Tools, and Threat Insights."]
source_reliability: "A - Reliable"
information_credibility: "1 - Confirmed by multiple sources"
analytic_confidence: "high"
tlp: "TLP:CLEAR"
classification: "Unclassified"
created: "2026-06-23"
updated: "2026-06-23"
tags: ["fin7", "carbon-spider", "sangria-tempest", "elbrus", "big-game-hunting", "carbanak"]
---

# FIN7

## Executive Summary
FIN7 (also tracked as Carbon Spider, Sangria Tempest, and ELBRUS) is an exceptionally resilient, highly structured Russian-speaking cybercriminal syndicate that poses a severe threat to global commercial sectors. Active for over a decade, the group historically specialized in high-volume Point-of-Sale (POS) infrastructure compromises. In recent years, FIN7 executed a definitive strategic pivot toward Big Game Hunting (BGH) ransomware operations and precision corporate network exploitation. Their tradecraft is highly professionalized, marked by the historical use of a fake cybersecurity front company ("Combi Security") to recruit unwitting talent, the creation of highly customized modular backdoors, and advanced social engineering workflows. Their primary targets now include critical transportation systems, major defense contractors, pharmaceutical enterprises, and high-revenue automotive manufacturers where extortion terms yield multi-million dollar payouts.

## Attribution Assessment
The group operates as an independent cybercriminal network located primarily within Eastern Europe and Russia. The U.S. Department of Justice unsealed indictments against multiple senior Ukrainian operators associated with FIN7's core administration between 2018 and 2021; however, the group adjusted its command structure seamlessly, demonstrating high operational continuity. FIN7 maintains deep developer ties, shared infrastructure pipelines, and tactical tooling overlaps with top-tier RaaS platforms, including historic affiliations with REvil, DarkSide, and BlackMatter. Forensic evidence throughout 2025 and 2026 confirms that FIN7 maintains active collaboration networks with [[01_Threat_Actors/ALPHV]] code remnants and operates as a high-tier affiliate cluster for dominant ransomware platforms.

## Operational Profile
The primary operational objective of FIN7 is direct financial extraction via data theft and deployment of disruptive network-wide extortion payloads. Their victimology favors high-revenue corporate networks within North America and Europe. FIN7 utilizes precision reconnaissance, targeting technical staff and network administrators who hold high-level corporate authorization. Their entry playbooks balance sophisticated typosquatted software pages with targeted spear-phishing tracks. Post-compromise behavior involves rapid internal asset mapping using native components (Living off the Land), token theft, and service control manipulation to blind defensive EDR sensors before pivoting to absolute data extraction.

## Campaign Activity (Past 14 Months)

* [[03_Campaigns/2025-2026 US Automotive and Supply Chain Infiltration Campaign]]
  * **Operational Goal:** Target high-privilege IT administrators within automotive supply chains to drop persistent backdoors and harvest proprietary network layouts.
  * **Description of the Campaign:** Escalating throughout late 2024 and continuing across 2025, FIN7 launched a targeted campaign aiming at defense and automotive systems in the US. The actors profiled internal system engineers on professional platforms, subsequently directing them via phishing channels to typosquatted domains hosting trojanized IT administration tools. Once inside, they deployed their signature Anunak and Lizar backdoors to compromise the central identity layer.
  * **Timeframe:** June 2024 – Ongoing into 2026.
  * **Notable Tradecraft:** Administrative typosquatting, Dropbox-hosted multi-stage payload delivery, and custom Living-off-the-Land obfuscation.
  * **Targeted Organizations:** Tier-1 US automotive manufacturers, component logistics providers, and heavy transport systems.

## Malware & Tooling
* **Custom Backdoors:** FIN7 utilizes [[04_Malware/DiceLoader]] (also known as Lizar or Carbanak descendants), a highly modular, lightweight architecture designed to run fileless execution blocks directly in memory.
* **Obfuscation Helpers:** The actors leverage [[04_Malware/POWERTRASH]], a custom-crafted PowerShell script layer that contains highly obfuscated, compressed shellcode fragments used to securely unpack downstream implants without triggering static detection tools.
* **Offensive Frameworks:** The group continues to utilize highly modified variations of [[04_Malware/Cobalt Strike]] beacons to maintain persistent terminal access loops inside target enterprise environments.

## Exploited Vulnerabilities
* None / Unknown: Intrusions within the past 14 months heavily prioritize identity compromise, typosquatted utility deployment, and social engineering over unpatched perimeter software exploitation.

## ATT&CK Tradecraft

### Initial Access
* [[02_TTPs/T1566.002 - Phishing- Spearphishing Link]]: Constructing precise communication vectors directing high-privilege target personnel to lookalike domain hubs.

### Execution
* [[02_TTPs/T1059.001 - Command and Scripting Interpreter- PowerShell]]: Deploying inline commands to call remote scripts and establish local memory backdoors.

### Persistence
* [[02_TTPs/T1547.001 - Boot or Logon Autostart Execution- Registry Run Keys / Startup Folder]]: Writing hidden parameters inside standard registry hubs to sustain administrative persistence across restarts.

### Privilege Escalation
* [[02_TTPs/T1068 - Exploitation for Privilege Escalation]]: Weaponizing internal administrative configuration weaknesses to elevate system shell parameters.

### Defense Evasion
* [[02_TTPs/T1562.001 - Impair Defenses- Disable or Modify Tools]]: Forcefully resetting firewall rule patterns and blocking defensive logging pathways to preserve backdoor execution.

### Credential Access
* [[02_TTPs/T1003.001 - OS Credential Dumping- LSASS Memory]]: Dumping local authorization database memories to extract plaintext service parameters.

### Discovery
* [[02_TTPs/T1082 - System Information Discovery]]: Mapping internal server structures, local active host tables, and domain permission groupings.

### Lateral Movement
* [[02_TTPs/T1021.001 - Remote Services- Remote Desktop Protocol]]: Pivoting across adjacent target segments using valid stolen administrative tokens over standard internal RDP tunnels.

### Exfiltration
* [[02_TTPs/T1567.002 - Exfiltration Over Web Service- Exfiltration to Cloud Storage]]: Bundling multi-terabyte internal data tracts into hidden file blocks and moving them out via legitimate web application interfaces.

### Impact
* [[02_TTPs/T1486 - Data Encrypted for Impact]]: Pushing fleet-wide network encryption modules to force immediate operational halts if ransom discussions reach an impasse.

## Infrastructure & IOC Patterns
FIN7 relies heavily on lookalike domain branding, registering domains that mimic common IT infrastructure software, diagnostic scanners, and corporate collaboration suites. They frequently make use of commercial cloud providers (such as Dropbox or Amazon S3 buckets) to stage intermediary malware dropping scripts.
* **Typosquat Domaining:** `advanced-ip-sccanner[.]com`

## Detection Engineering Notes

### Behavioral Indicators
* Spikes in `certutil.exe` execution involving specific decode switches (`-decode hex`) occurring inside non-administrative user paths.
* Local executions calling `net group "Domain Admins" /domain` linked directly to anomalous script interpreter chains.

### Detection Opportunities
* Monitor and generate high-priority alerts for endpoint processes dropping localized `.dat` or `.tmp` file patterns that map directly to memory injection loops inside `cmd.exe` paths.
* Audit outbound network telemetry for persistent, long-duration encrypted openSSH connections routing to unverified public external networks.

### Log Sources
* PowerShell Script Block Logging (Event ID 4104).
* Windows Security Auditing logs mapping process creations (Event ID 4688).
* DNS Resolution Logs and Cloud Provider Access Metadata.

### Telemetry Requirements
* Host-level process argument monitoring, deep script tracking blocks, and real-time capture of external API interactions stemming from administrative processes.

## Intelligence Assessment
FIN7 is an exceptionally sophisticated threat actor whose ongoing survival and operational evolution highlight a high corporate-style adaptation capability. Their transition toward targeted big-game hunting ransomware operations proves that the syndicate prioritizes high-margin corporate targets over low-yield opportunistic credit card harvesting. The tactical alignment with top-tier RaaS components implies that FIN7 will continue to serve as a critical core element within the cybercriminal ecosystem through 2026, leveraging custom memory implants to routinely outpace traditional signature-based security perimeters.

## Intelligence Gaps
* Detailed visibility into the internal leadership structures driving developer cycles following the latest law enforcement disruption waves.
* Precise structural definitions of the active financial laundering pathways used to convert massive multi-million dollar cryptocurrency ransoms.

## Recommended Defensive Actions

### Immediate
* Block and blacklist all confirmed typosquatted application distribution domains across corporate gateway blocks.
* Review PowerShell logging parameters to ensure full visibility into host script execution strings.

### Tactical
* Restrict the execution of basic internal discovery binaries (`net.exe`, `tasklist.exe`) for standard non-administrative user brackets.
* Deploy enhanced detection patterns monitoring for unverified process memory changes targeting standard Windows sub-components.

### Strategic
* Enforce phishing-resistant MFA models across all remote enterprise validation paths to mitigate credential theft vectors.

### Long-Term
* Build out a Zero Trust architecture that isolates administrative management lanes from common internet-facing corporate communications.

## Related Threat Actors
* [[01_Threat_Actors/ALPHV]]: High operational overlap, with FIN7 serving as a core partner and custom builder developer for their ransomware program.
* [[01_Threat_Actors/Scattered Spider]]: Shared targeting alignments and data broker exchanges tracking high-value North American targets.

## Sources
Arctic Wolf. (2024). Threat Group FIN7 Targets the U.S. Automotive Industry. Arctic Wolf Labs Threat Research.

Huntress. (2024). FIN7 Cybercrime Group - Tactics, Tools, and Threat Insights. Huntress Threat Library.

MITRE ATT&CK. (2026). FIN7 Group Profile G0046. MITRE Corporation.

## Changelog
* Created: 2026-06-23
* Updated: 2026-06-23
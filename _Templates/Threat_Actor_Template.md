---
entity_type: threat_actor
profile_version: "1.0"
actor_name: ""
actor_id: "TA-<###>"
aliases: []
actor_type: nation_state | criminal | hacktivist | insider | unknown
suspected_origin: ""
nation_state_sponsor: ""
attribution_confidence: low | moderate | high
admiralty_reliability: ""
admiralty_credibility: ""
primary_motivation: []
secondary_motivation: []
threat_level: low | medium | high | critical
activity_status: active | dormant | disbanded | unknown
first_observed: ""
last_observed: ""
target_sectors: []
target_regions: []
target_technologies: []
primary_tactics: []
known_techniques: []
malware_arsenal: []
associated_campaigns: []
linked_actors: []
infrastructure_indicators: []
notable_incidents: []
ioc_references: []
diamond_model:
  adversary: ""
  capability: ""
  infrastructure: ""
  victim: ""
detection_priority: low | medium | high | critical
analytic_confidence: low | moderate | high
open_intelligence_gaps: []
pir_references: []
tlp_classification: TLP:AMBER
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
author: ""
profile_status: draft | reviewed | published
---

# <actor_name>

**Type:** <actor_type> | **Origin:** <suspected_origin> | **Threat Level:** <threat_level> | **Status:** <activity_status>

---

## Executive Summary

Write 3–5 sentences covering:
- Who is this actor and who sponsors or directs them?
- What sectors, regions, and technologies do they target?
- Why are they relevant to the organization right now?
- What is the bottom-line risk?

---

## Identity & Background

| Field | Value |
|-------|-------|
| Primary Name | |
| Aliases | |
| Actor Type | Nation-state / Criminal / Hacktivist / Unknown |
| Suspected Origin | |
| State Sponsor | |
| First Observed | |
| Last Active | |
| Activity Status | Active / Dormant / Disbanded |
| Attribution Confidence | Low / Moderate / High |
| Admiralty Source Reliability | A–F |
| Admiralty Information Credibility | 1–6 |

### Background & History
Narrative covering suspected origins, geopolitical context, known affiliations, and how this actor has evolved over time. Note competing vendor attributions or divergent assessments.

---

## Diamond Model Assessment

| Node | Assessment |
|------|-----------|
| **Adversary** | Who they are — identity, sponsorship, intent |
| **Capability** | TTPs, malware, sophistication level |
| **Infrastructure** | Domains, IPs, hosting, tooling delivery |
| **Victim** | Target sectors, geographies, technologies |

---

## Motivations & Strategic Goals

- **Primary Motivation:** Espionage / Financial / Sabotage / Hacktivism / Other
- **Secondary Motivation:**
- **Assessed Strategic Goals:** What is the actor ultimately trying to achieve?
- **Sponsor Objectives:** How does this actor's activity align with state or organizational goals?
- **Financial vs. Intelligence Priorities:** Where does the balance sit?

---

## Targeting Profile

### Target Sectors
| Sector | Confidence | Notes |
|--------|-----------|-------|
| | | |

### Target Regions
| Region / Country | Confidence | Context |
|-----------------|-----------|---------|
| | | |

### Target Technologies
| Technology / Platform | Why Targeted |
|----------------------|-------------|
| | |

---

## Tactics, Techniques & Procedures

Organized by ATT&CK tactic phase. Use wikilinks for all techniques.

### Initial Access
- Technique Name — observed implementation

### Execution
-

### Persistence
-

### Privilege Escalation
-

### Defense Evasion
-

### Credential Access
-

### Discovery
-

### Lateral Movement
-

### Collection
-

### Command & Control
-

### Exfiltration
-

### Impact
-

> **Tip:** Use Sherman-Kent Words of Estimative Probability when describing assessed (vs. confirmed) TTPs.

---

## Malware & Tooling Arsenal

| Tool / Malware | Type | Role | Exclusivity |
|---------------|------|------|-------------|
| Tool/ Malware Name | RAT / Loader / Wiper / etc. | | Exclusive / Shared / Commodity |

---

## Infrastructure Patterns

Describe observed infrastructure tradecraft:
- **Hosting Provider Preferences:** Bulletproof hosting, cloud VPS, compromised infrastructure
- **Domain Patterns:** Lookalike domains, DGA, registrar preferences, WHOIS patterns
- **SSL/TLS Patterns:** Certificate reuse, Let's Encrypt, self-signed certs
- **VPN / Proxy Use:** Infrastructure obfuscation layers
- **Email Infrastructure:** Phishing origins, spoofing methods
- **Known C2 IP Ranges / ASNs:**

---

## Associated Campaigns

| Campaign | Period | Role | Status |
|----------|--------|------|--------|
| Campaign Name | | Primary / Supporting | Ongoing / Concluded |

---

## Linked Threat Actors

| Actor | Relationship | Confidence |
|-------|-------------|------------|
| Threat Actor Name | Shared infrastructure / Shared tooling / Same group / Allied | |

---

## Notable Incidents

| Date | Incident | Victim / Sector | Notes |
|------|---------|----------------|-------|
| | | | |

---

## Activity Timeline

```chronos
- [YYYY] First observed activity

- [YYYY-MM-DD~YYYY-MM-DD] Major campaign period

- [YYYY-MM-DD] Notable incident or attribution event

@ [YYYY-MM-DD~YYYY-MM-DD] Peak activity window
```

---

## Indicators of Compromise

- IOCs

---

## Detection & Hunting Guidance

### Detection Priorities
What behaviors or artifacts should defenders focus on for this actor?

### Required Telemetry
- **Endpoint:** EDR, Sysmon, AV
- **Network:** DNS, proxy, firewall, NetFlow
- **Identity:** Active Directory, Entra ID, MFA logs, PAM
- **Cloud:** CloudTrail, Unified Audit Log, CSPM alerts
- **Email:** Header metadata, delivery infrastructure

### Behavioral Patterns to Hunt
Specific process chains, network flows, or authentication sequences tied to this actor:
-

### Hunt Ideas
1. **Hunt:** [Name] — [Hypothesis]
2.

### Detection Rule References
-

---

## Analytic Assessment

- **Intent:** What is this actor fundamentally trying to achieve?
- **Capability:** Sophistication level, investment in tradecraft, tool maturity
- **Opportunity:** What conditions or access do they exploit?
- **Organizational Relevance:** Does this actor target our sector, technology, or region?
- **Threat Trajectory:** Is this actor escalating, stable, or declining in activity?
- **Expected Evolution:** How might TTPs or targeting change?
- **Analytic Confidence:** Low / Moderate / High — justify

> Use Sherman-Kent Words of Estimative Probability to qualify likelihood statements.

---

## Intelligence Gaps

| Gap | Impact | Priority | Collection Recommendation |
|-----|--------|----------|--------------------------|
| | | | |

---

## Recommended Actions

### Immediate (0–72 hours)
-

### Short-Term (1–4 weeks)
-

### Long-Term (1–6 months)
-

---

## Sources

All sources in APA format:
-

---

## Changelog

| Date | Analyst | Change |
|------|---------|--------|
| YYYY-MM-DD | | Profile created |

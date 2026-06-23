---
entity_type: pir
profile_version: "1.0"
pir_title: ""
pir_id: "PIR-<YYYY>-<###>"
pir_status: draft | active | under_review | retired
priority: critical | high | medium | low
classification: internal_only | tlp_amber | tlp_green
category: strategic | operational | tactical | technical
focus_areas: []
primary_question: ""
sub_questions: []
pir_owner: ""
stakeholders: []
intelligence_consumers: []
business_drivers: []
risk_themes: []
time_horizon: ongoing | quarterly | annual | incident_driven
review_cadence: weekly | monthly | quarterly | as_needed
required_outputs: []
success_criteria: []
collection_topics: []
collection_sources_internal: []
collection_sources_external: []
collection_methods: []
collection_constraints: []
data_sources_internal: []
data_sources_external: []
related_threat_actors: []
related_campaigns: []
related_malware: []
related_technologies: []
related_business_units: []
kpis: []
analytic_confidence: low | moderate | high
last_evaluated: "YYYY-MM-DD"
last_evaluated_by: ""
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
author: ""
profile_status: draft | reviewed | active | retired
---

# <pir_title>

**PIR ID:** <pir_id> | **Status:** <pir_status> | **Priority:** <priority> | **Owner:** <pir_owner>

---

## Primary Intelligence Question

> **<primary_question>**

### Sub-Questions
Break the primary question into answerable components:
1.
2.
3.

> **Guidance:** A good PIR is decision-focused, not curiosity-driven. Ask: *What decision will this intelligence enable?* If you can't name a decision, reconsider the PIR.

---

## Business Context & Rationale

### Why Does This PIR Exist?
Describe the business problem, threat scenario, or risk gap this PIR addresses:
-

### Business Drivers
What organizational objective, risk register item, or leadership concern created this requirement?
-

### Risk Themes
What categories of risk does this PIR address?
- Fraud / Financial Loss
- Ransomware / Business Disruption
- Regulatory / Compliance Exposure
- Account Takeover / Identity Risk
- Supply Chain / Third-Party Risk
- Reputational Damage
- Other:

---

## Stakeholders, Owner & Consumers

| Role | Name / Team | Responsibility |
|------|------------|----------------|
| PIR Owner | | Accountable for collection, analysis, and reporting |
| Primary Stakeholder | | Requested or funds this PIR |
| Intelligence Consumers | | Teams that act on the intelligence produced |

> **Note:** Clearly separating owners from consumers prevents unclear accountability when answers are needed urgently.

---

## Scope & Boundaries

### Category
- **Strategic** — Long-horizon questions about adversary intent, geopolitical context
- **Operational** — Questions about active campaigns, actor behavior, targeting
- **Tactical** — Short-term, incident-linked, specific IOC or TTP focus
- **Technical** — Product/system-level questions about vulnerabilities, configurations

### Focus Areas
-

### Time Horizon
- **Duration:** <time_horizon>
- **Review Cadence:** <review_cadence>

### In Scope
Define what this PIR explicitly covers:
-

### Out of Scope
Define what is deliberately excluded — avoids scope creep:
-

---

## Required Intelligence Outputs

What products or deliverables will this PIR generate?

| Output Type | Frequency | Audience | Format |
|-------------|-----------|----------|--------|
| Weekly briefing inclusion | Weekly | Security leadership | Briefings |
| Threat actor profile update | As needed | SOC / IR | Threat Actors |
| Hunt package | Quarterly | Threat hunting team | KQL / Sigma |
| Incident enrichment | Per incident | IR team | Case notes |

### Success Criteria
How will you know this PIR is being answered effectively?
- Decision-makers can answer [specific question] using CTI output
- Detection coverage improves for [specific threat type]
- Reduction in [specific loss type or incident category]
- Time to answer stakeholder ad-hoc questions drops to < [threshold]

---

## Collection Guidance

### Key Collection Topics
What specific information must be collected to answer this PIR?
-

### Internal Collection Sources

| Source | Type | Collection Method | Frequency |
|--------|------|-------------------|-----------|
| SIEM / Splunk | Log analysis | Automated query | Continuous |
| EDR (CrowdStrike / Defender) | Endpoint telemetry | Hunt / alert review | Daily |
| Email security gateway | Phishing analysis | Alert triage | Daily |
| Identity / IAM logs | Auth events | UEBA / manual review | Daily |
| Threat intel platform | Enrichment | Automated / manual | Per indicator |

### External Collection Sources

| Source | Type | Collection Method |
|--------|------|-------------------|
| Commercial threat intel feeds | Structured IOC / reporting | API / manual |
| ISAC / industry sharing | Sector-specific intel | Membership feeds |
| OSINT (Shodan, VirusTotal, etc.) | Technical recon | Manual / automated |
| Vendor advisories | Vulnerability / threat | RSS / email |
| Government advisories (CISA, FBI) | Threat / vulnerability | RSS / manual |

### Collection Methods
- Automated log ingestion and alerting
- Proactive threat hunting
- Case-driven investigation and enrichment
- OSINT and open-source research
- Vendor and partner intelligence sharing

### Constraints & Considerations
- Legal or privacy restrictions on collection
- Data retention limitations
- Technical gaps (blind spots in logging or telemetry)
- Resource constraints on analyst time

---

## Data Sources & Telemetry Requirements

Document the specific datasets needed to reliably answer this PIR.

### Internal Data Sources
- SIEM tables (specify table names if known)
- EDR telemetry (process events, network events, file events)
- Identity and IAM logs (Active Directory, Entra ID, Okta)
- Email security logs (inbound/outbound mail metadata)
- Application logs (loan origination system, servicing platforms, etc.)
- Network logs (DNS, proxy, firewall, NetFlow)

### External Data Sources
- Named commercial feeds and what they provide
- ISAC / sharing community subscriptions
- Open-source feeds (Abuse.ch, MISP communities, etc.)
- Vendor threat reports relevant to this PIR

---

## Related Intelligence Objects

Use Obsidian wikilinks to tie this PIR into the broader CTI knowledge graph.

| Category | Links |
|----------|-------|
| Threat Actors |  |
| Campaigns |  |
| Malware |  |
| Vulnerabilities | |
| Technologies | |
| Business Units | |

---

## Metrics & KPIs

How will effectiveness of this PIR be tracked?

| KPI | Target | Current |
|-----|--------|---------|
| % of relevant incidents enriched with PIR-related CTI | >80% | |
| Time to answer stakeholder questions on this topic | < 4 hours | |
| Detections or hunts derived from this PIR per quarter | | |
| Intelligence gaps closed per review cycle | | |
| Reduction in related loss type | | |

**Last Evaluated:** <last_evaluated> by <last_evaluated_by>

---

## Current Analytic Assessment

Summarize where intelligence stands today relative to this PIR:
- What is known with confidence?
- What remains uncertain or unconfirmed?
- What is the current coverage level (well-covered / partial / significant gaps)?
- Has the threat this PIR addresses changed since last review?

**Analytic Confidence:** <analytic_confidence>

---

## Intelligence Gaps & Collection Recommendations

| Gap | Impact on PIR | Priority | Recommended Action |
|-----|---------------|----------|-------------------|
| | | | |

**What new data, access, tooling, or partnerships would materially improve the ability to answer this PIR?**
-

---

## Notes & Changelog

### Working Notes
-

### Changelog

| Date | Analyst | Change |
|------|---------|--------|
| YYYY-MM-DD | | PIR created |

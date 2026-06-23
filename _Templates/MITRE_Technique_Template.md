---
entity_type: mitre_technique
profile_version: "1.0"
technique_id: ""
subtechnique_id: ""
technique_name: ""
parent_technique: ""
tactic_phases: []
platforms: []
permissions_required: []
defense_bypassed: []
data_sources: []
mitre_version: "16"
attack_spec_version: ""
attack_source: Enterprise
is_subtechnique: false
deprecated: false
revoked: false
associated_actors: []
associated_malware: []
associated_campaigns: []
related_techniques: []
detection_priority: low | medium | high | critical
detection_maturity: none | minimal | moderate | strong
threat_score: 1
date_created: "YYYY-MM-DD"
date_updated: "YYYY-MM-DD"
author: ""
tags:
  - mitre
  - ttp
profile_status: draft | reviewed | published
---

# <technique_id> — <technique_name>

**Tactic(s):** | **Platforms:** | **Detection Priority:** <detection_priority> | **Detection Maturity:** <detection_maturity>

---

## Summary

Write 3–5 sentences covering:
- What does this technique do and at what stage of an attack is it used?
- Why do adversaries prefer this technique — what advantage does it provide?
- What does successful use enable the attacker to do next?
- How commonly is it observed in real-world intrusions?

---

## Tactic Phases


---

## Technical Description

Provide a thorough technical explanation:

- **Mechanism:** How the technique works at a technical level
- **Typical Execution Flow:** Step-by-step walkthrough of common implementation
- **Affected Platforms:** Windows / Linux / macOS / Cloud / Containers / OT/ICS — per-platform nuances
- **Why Adversaries Use It:** What makes this preferable to alternatives
- **Subtechniques:** List and briefly describe each (link where profiled)
- **Observed Variations:** Real-world deviations from the canonical definition

---

## Procedure Examples

Real-world observed use. Structure: Actor → Malware → Campaign.

### Threat Actors
- specific observed implementation

### Malware & Tools
- how this technique is implemented in the tool

### Campaigns
-  how this technique featured in the operation

---

## Associated Threat Actors

| Actor | Frequency | Notes |
|-------|-----------|-------|
| Actor Name | Frequently / Occasionally / Rarely | |

---

## Associated Malware & Tools

| Tool | Role | Notes |
|------|------|-------|
| | | |

---

## Associated Campaigns

| Campaign | Context |
|----------|---------|
| | |

---

## Detection Engineering

### Detection Logic

**Endpoint / Host Telemetry**
- Process creation patterns and parent-child relationships to look for
- File system writes or reads that are indicative
- Registry modifications
- Memory anomalies (injection, hollowing, reflective loading)

**Network Telemetry**
- Traffic patterns, protocols, unusual destinations
- DNS query patterns or tunneling behaviors

**Cloud Telemetry**
- API calls, IAM changes, configuration modifications
- Audit log patterns across AWS / Azure / GCP

**Identity Telemetry**
- Authentication event patterns
- Token manipulation or abuse
- Privileged account misuse

### Required Data Sources

Derived from YAML `data_sources`. For each:
- Log/telemetry type and where it comes from
- Minimum collection requirements (Sysmon config, Windows audit policy, EDR settings, cloud logging level)

### Detection Gaps & Blind Spots
- Where detection commonly fails for this technique
- Platform or environment conditions that reduce signal quality
- EDR-specific gaps or vendor coverage variations

---

## Hunting Queries

### KQL — Microsoft Sentinel
```kql
// Threat hunt for <technique_id> — <technique_name>
// Replace with functional or reference query
let timeframe = 7d;
// query body
```

### Sigma Rule
```yaml
title: Hunt for <technique_id> - <technique_name>
status: experimental
description: ""
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        CommandLine|contains: ''
    condition: selection
falsepositives:
    - Legitimate admin activity
level: medium
```

### EDR / OSQuery / Velociraptor
```sql
-- Platform-specific hunt logic
```

---

## False Positive Profile

Document benign activity that may trigger detection for this technique:

| Trigger | Root Cause | Tuning Recommendation |
|---------|------------|----------------------|
| | | |

- **Common Benign Triggers:** IT admin tools, software installers, monitoring agents
- **Expected System Behaviors:** What normal looks like for this activity type
- **Baselining Guidance:** How to establish a noise baseline before alerting

---

## Prevention & Hardening

### Endpoint Controls
- AppLocker / WDAC policy recommendations
- Attack Surface Reduction (ASR) rules
- EDR prevention mode settings

### Identity Controls
- Least-privilege guidance
- MFA requirements
- PAM / JIT access recommendations
- Conditional access policies

### Network Controls
- Segmentation recommendations
- Egress filtering
- Proxy enforcement

### Cloud Controls
- CSPM policy settings
- SCP / Organization Policy guardrails
- IAM guardrails specific to this technique

### ATT&CK Mitigations

| Mitigation ID | Mitigation Name | Implementation Notes |
|---------------|-----------------|----------------------|
| M#### | | |

---

## Impact

- **What the Attacker Gains:** Immediate capability unlocked by this technique
- **Business Risk:** Downstream organizational impact
- **Chaining Risk:** What techniques this enables or supports — link related TTPs

---

## Telemetry & Artifact Patterns

Observable artifacts specific to this technique:

| Artifact Type | Pattern / Value |
|--------------|-----------------|
| Process Names | |
| Command-Line Patterns | |
| File Paths | |
| Registry Keys | |
| Network Ports / Protocols | |
| User-Agents | |
| JA3 Fingerprints | |
| Memory Strings | |
| Named Pipes | |

---

## Identities & Roles at Risk

Which account types or roles are most exposed:
- Domain Admins
- Service Accounts
- Cloud privileged roles (Global Admin, Owner, Privileged Identity Manager)
- Local Administrators
- Non-privileged users (where social engineering is involved)

---

## Related Techniques

| Technique | Relationship |
|-----------|-------------|
| Technique Name | Precedes / Follows / Enables / Variant of |

---

## Analyst Notes

Internal CTI/SOC observations, lessons learned from past incidents, or environment-specific context:
-

---

## References

- MITRE ATT&CK: https://attack.mitre.org/techniques/<technique_id>/
- Additional APA-formatted public sources:

---

## Changelog

| Date | Analyst | Change |
|------|---------|--------|
| YYYY-MM-DD | | Profile created |

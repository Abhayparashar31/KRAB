---
entity_type: daily_journal
date: "<%tp.file.creation_date('YYYY-MM-DD')%>"
day_of_week: "<%tp.file.creation_date('dddd')%>"
analyst: ""
shift: day | night | on_call
mood: focused | distracted | fatigued | energized | stressed
energy_level: 1 | 2 | 3 | 4 | 5
primary_focus: ""
pir_touchpoints: []
incident_references: []
hunt_references: []
cases_worked: 0
detections_fired: 0
false_positives: 0
true_positives: 0
escalations_made: 0
date_created: "<%tp.file.creation_date('YYYY-MM-DD')%>"
date_updated: "<%tp.file.last_modified_date('YYYY-MM-DD')%>"
tags:
  - daily
  - journal
banner: 99_Attachments/CIPHER Obsidian Banner.png
banner-height: 300
content-start: 301
---

# Daily Analysis Journal — <%tp.file.creation_date("YYYY-MM-DD")%>

**Analyst:** | **Shift:** | **Energy:** /5 | **Primary Focus:**

---

## Intent for the Day

Answer in 2–4 bullet points:
- What is the primary mission or goal for today?
- What PIRs or investigations are getting focused time?
- What am I *not* doing today — what's being deprioritized consciously?
- What does a successful day look like?

---

## Intelligence Inputs

### Overnight & Early Activity
What came in before active work began — alerts, feeds, news, vendor reports:
-

### PIR Touchpoints
Which Priority Intelligence Requirements had new developments?

| PIR | Reference | Update |
|-----|-----------|--------|
| | `[[PIRs/PIR_Name]]` | |

### Threat Actor / Campaign Developments
New activity, reporting, or telemetry tied to tracked actors or campaigns:
-

### Notable Alerts, Incidents & Anomalies
Anything that required triage or investigation this shift:
-

---

## Operational Work

### Active Cases & IR Tasks

| Case ID | Description | Status | Time Spent |
|---------|-------------|--------|------------|
| | | Open / Escalated / Closed | |

### Threat Hunting Activity

| Hunt Name | Hypothesis | Data Sources Used | Outcome |
|-----------|------------|-------------------|---------|
| | | | Positive / Negative / Inconclusive |

### Research Threads
Topics being investigated, malware samples analyzed, TTPs studied:
-

### Detection Engineering & Tooling
Rules written, tuned, or tested; automation built; data source work:
-

---

## Metrics

| Metric | Value |
|--------|-------|
| Cases Worked | |
| Alerts Triaged | |
| True Positives | |
| False Positives | |
| MTTD (Mean Time to Detect) | |
| MTTA (Mean Time to Acknowledge) | |
| MTTR (Mean Time to Respond) | |
| Escalations Made | |
| Hunts Executed | |
| Rules Deployed / Tuned | |

---

## Learning & Skill Development

### New TTPs, Tools, or Techniques Encountered
What did you learn today that you didn't know this morning?
-

### Rabbit Holes Skipped (To Revisit)
Interesting threads that were deliberately deferred:
-

### Skill or Knowledge Gap Identified
Something you realized you don't know well enough:
-

### Resources Consumed
Blogs, papers, reports, videos, or training reviewed today:
-

---

## Analyst Reflection

Answer briefly — these build pattern recognition over time.

**What patterns did I notice today?**
-

**What surprised me?**
-

**What did I over- or under-estimate?**
-

**Where did I lose time or focus?**
-

**What would I do differently if I reset the day?**
-

**What am I most curious about going into tomorrow?**
-

---

## End-of-Day Summary

### Wins
What went well — detections fired, investigations closed, skills applied:
-

### Gaps & Misses
What was missed, slow, or incomplete:
-

### Handoffs & Escalations
Items being passed to another analyst, team, or shift:
-

### Open Threads — Carry Forward Tomorrow
Unresolved work that needs to continue:
-

---

## Backlinks

```dataview
table without id file.inlinks as "Linked From"
where file.name = this.file.name
```

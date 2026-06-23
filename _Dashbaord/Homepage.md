# 🎛️ KRAB Intelligence Dashboard

> [!info] KRAB Threat Intelligence Brain
> Central operational dashboard for threat intelligence correlation, ATT&CK mapping, malware analysis, campaign intelligence, vulnerability exploitation, infrastructure clustering, and detection engineering.

## 📊 KRAB Overview

| Intelligence Domain | Purpose |
| :--- | :--- |
| **Threat Actors** | Attribution & adversary tracking |
| **Campaigns** | Operational activity tracking |
| **Malware** | Capability & tooling analysis |
| **TTPs** | ATT&CK behavioral intelligence |
| **Vulnerabilities** | Exploitation tracking |
| **Observables** | Infrastructure & IOC correlation |
| **Collections** | Threat landscape aggregation |

---

## 🌎 Threat Landscape Overview

### Threat Actors
```dataview
TABLE
origin_country AS "Origin",
last_seen AS "Last Activity",
length(campaigns) AS "Campaigns",
length(malware_used) AS "Malware",
length(ttps) AS "TTPs"
FROM "01_Threat_Actors"
```



### Active Campaigns
```dataview
TABLE
threat_actors AS "Actors",
last_seen AS "Last Activity",
malware AS "Malware",
vulnerabilities AS "CVEs"
FROM "03_Campaigns"
LIMIT 20
```




---

## 🧠 ATT&CK Intelligence

### Most Operationally Reused TTPs
```dataview
TABLE 
    default(length(related_actor), 0) AS "TA",
    default(length(related_campaign), 0) AS "Campaigns",
    default(length(related_malware), 0) AS "Malware",
    default(length(related_vuln), 0) AS "Vulnerabilities",
    (default(length(related_actor), 0) + 
     default(length(related_campaign), 0) + 
     default(length(related_malware), 0) + 
     default(length(related_vuln), 0)) AS "Total"
FROM "02_TTPs"
WHERE related_actor OR related_campaign OR related_malware OR related_vuln
SORT (default(length(related_actor), 0) + 
      default(length(related_campaign), 0) + 
      default(length(related_malware), 0) + 
      default(length(related_vuln), 0)) DESC
LIMIT 25
```

## MITRE Techniques Used By Multiple Threat Actors

```dataview
TABLE 
    related_actor AS "Linked Actors", 
    (default(length(related_actor), 0) + default(length(related_campaign), 0)) AS "Reused By"
FROM "02_TTPs"
WHERE (length(related_actor) + length(related_campaign)) >= 2
SORT (length(related_actor) + length(related_campaign)) DESC
LIMIT 10
```

### Credential Access Techniques
```dataview
LIST
FROM "02_TTPs"
WHERE contains(file.name, "Credential")
OR contains(file.name, "LSASS")
```

---

## 🔬 Vulnerability Exploitation Intelligence

### High Impact Vulnerabilities
```dataview
TABLE 
    length(ttps) AS "TTPs Exploiting This", 
    cvss_score AS "CVSS",
    status AS "Status",
    affected_products AS "Affected Products",
    threat_actors AS "Threat Actors",
    malware AS "Associated Malware"
FROM "05_Vulnerabilities"
WHERE ttps
SORT length(ttps) DESC
LIMIT 10
```


```dataview
TABLE 
tactics AS "Attacker Tactics", 
length(threat_actors) AS "Active Actors"
FROM "05_Vulnerabilities"
WHERE ttps
SORT length(threat_actors) DESC
LIMIT 10
```

---

## 🦠 Malware Ecosystem

### Most Reused Malware Families
```dataview
TABLE
length(threat_actors) AS "Actors",
length(campaigns) AS "Campaigns",
last_seen AS "Last Seen"
FROM "04_Malware"
SORT length(campaigns) DESC
LIMIT 20
```

### Malware to TTPs Mapping
```dataview
TABLE 
related_malware AS "Associated Malware", 
length(related_malware) AS "Malware Count"
FROM "02_TTPs"
WHERE related_malware
SORT length(related_malware) DESC
LIMIT 10
```

### Credential Theft Malware
```dataview
LIST
FROM "04_Malware"
WHERE contains(capabilities, "credential theft") OR contains(summary, "credential")
```

### Malware Used By Multiple Threat Actors
```dataview
TABLE
threat_actors AS "Threat Actors"
FROM "04_Malware"
WHERE length(threat_actors) > 1
```


---
#### More to come soon.....
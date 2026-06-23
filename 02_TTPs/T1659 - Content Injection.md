# Content Injection

## Description

Adversaries may gain access and continuously communicate with victims by injecting malicious content into systems through online network traffic. Rather than luring victims to malicious payloads hosted on a compromised website (i.e., Drive-by Target followed by Drive-by Compromise ), adversaries may initially access victims through compromised data-transfer channels where they can manipulate traffic and/or inject their own content. These compromised online network channels may also be used to deliver additional payloads (i.e., Ingress Tool Transfer ) and other data to already compromised systems. [1]

Adversaries may inject content to victim systems in various ways, including:

Content injection is often the result of compromised upstream communication channels, for example at the level of an internet service provider (ISP) as is the case with "lawful interception." [3] [1] [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1088 | Disco | Disco has achieved initial access and execution through content injection into DNS, HTTP, and SMB replies to targeted hosts that redirect them to download malicious files. [5] |
| G1019 | MoustachedBouncer | MoustachedBouncer has injected content into DNS, HTTP, and SMB replies to redirect specifically-targeted victims to a fake Windows Update page to download malware. [5] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1041 | Encrypt Sensitive Information | Where possible, ensure that online traffic is appropriately encrypted through services such as trusted VPNs. |
| M1021 | Restrict Web-Based Content | Consider blocking download/transfer and execution of potentially uncommon file types known to be used in adversary campaigns. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0349 | Detection Strategy for Content Injection | AN0992 | Detect suspicious file creations and process executions triggered by browser activity (e.g., injected payloads written to %AppData% or Temp directories, then executed). Correlate network anomalies with subsequent local process creation or script execution. |
| AN0993 | Detect curl/wget commands saving executable/script payloads to /tmp or /var/tmp followed by execution. Monitor packet captures or IDS/IPS alerts for injected responses or mismatched content types. |  |  |
| AN0994 | Monitor unified logs for processes spawned from Safari or other browsers that immediately load scripts or executables. Detect file drops in ~/Library/Caches or ~/Downloads that execute shortly after being written. |  |  |

---

## References

- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 1, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [Kaspersky IT Encyclopedia. (n.d.). Man-in-the-middle attack. Retrieved September 1, 2023.](https://encyclopedia.kaspersky.com/glossary/man-in-the-middle-attack/)
- [Starikova, A. (2023, February 14). Man-on-the-side – peculiar attack. Retrieved September 1, 2023.](https://usa.kaspersky.com/blog/man-on-the-side/27854/)
- [Budington, B. (2015, April 2). China Uses Unencrypted Websites to Hijack Browsers in GitHub Attack. Retrieved September 1, 2023.](https://www.eff.org/deeplinks/2015/04/china-uses-unencrypted-websites-to-hijack-browsers-in-github-attack)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)

---

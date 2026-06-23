# Resource Hijacking

## Description

Adversaries may leverage the resources of co-opted systems to complete resource-intensive tasks, which may impact system and/or hosted service availability.

Resource hijacking may take a number of different forms. For example, adversaries may:

In some cases, adversaries may leverage multiple types of Resource Hijacking at once. [1]

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0267 | Resource Hijacking Detection Strategy | AN0741 | Persistent high CPU utilization combined with suspicious command-line execution (e.g., mining tools or obfuscated scripts) and outbound connections to mining/proxy networks. |
| AN0742 | Abnormal CPU/memory usage by unauthorized processes with outbound connections to known mining pools or using cron jobs/scripts to maintain persistence. |  |  |
| AN0743 | Background launch agents/daemons with high CPU use and network access to external mining services. |  |  |
| AN0744 | Sudden spikes in cloud VM CPU usage with outbound traffic to mining pools and unauthorized instance creation. |  |  |
| AN0745 | High CPU usage by unauthorized containers running mining binaries or public proxy tools. |  |  |
| AN0746 | Abuse of cloud messaging platforms to send mass spam or consume quota-based resources. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0267 | Resource Hijacking Detection Strategy | AN0741 | Persistent high CPU utilization combined with suspicious command-line execution (e.g., mining tools or obfuscated scripts) and outbound connections to mining/proxy networks. |
| AN0742 | Abnormal CPU/memory usage by unauthorized processes with outbound connections to known mining pools or using cron jobs/scripts to maintain persistence. |  |  |
| AN0743 | Background launch agents/daemons with high CPU use and network access to external mining services. |  |  |
| AN0744 | Sudden spikes in cloud VM CPU usage with outbound traffic to mining pools and unauthorized instance creation. |  |  |
| AN0745 | High CPU usage by unauthorized containers running mining binaries or public proxy tools. |  |  |
| AN0746 | Abuse of cloud messaging platforms to send mass spam or consume quota-based resources. |  |  |

---

## References

- [Miguel Hernandez. (2023, August 17). LABRAT: Stealthy Cryptojacking and Proxyjacking Campaign Targeting GitLab . Retrieved September 25, 2024.](https://sysdig.com/blog/labrat-cryptojacking-proxyjacking-campaign/)

---

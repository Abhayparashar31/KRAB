# Unused/Unsupported Cloud Regions

## Description

Adversaries may create cloud instances in unused geographic service regions in order to evade detection. Access is usually obtained through compromising accounts used to manage cloud infrastructure.

Cloud service providers often provide infrastructure throughout the world in order to improve performance, provide redundancy, and allow customers to meet compliance requirements. Oftentimes, a customer will only use a subset of the available regions and may not actively monitor other regions. If an adversary creates resources in an unused region, they may be able to operate undetected.

A variation on this behavior takes advantage of differences in functionality across cloud regions. An adversary could utilize regions which do not support advanced detection services in order to avoid detection of their activity.

An example of adversary use of unused AWS regions is to mine cryptocurrency through Resource Hijacking , which can cost organizations substantial amounts of money over time depending on the processing power used. [1]

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1054 | Software Configuration | Cloud service providers may allow customers to deactivate unused regions. [1] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0247 | Detection of Adversary Use of Unused or Unsupported Cloud Regions (IaaS) | AN0690 | Detects creation of cloud instances, services, or resources in normally unused or unsupported regions, especially following initial account access or credential use from known regions. Correlates resource provisioning across regions with absence of historical usage and alerting from standard logging services (e.g., GuardDuty not enabled in that region). |

---

## References

- [CloudSploit. (2019, June 8). The Danger of Unused AWS Regions. Retrieved October 8, 2019.](https://medium.com/cloudsploit/the-danger-of-unused-aws-regions-af0bf1b878fc)

---

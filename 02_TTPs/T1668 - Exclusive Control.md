# Exclusive Control

## Description

Adversaries who successfully compromise a system may attempt to maintain persistence by "closing the door" behind them – in other words, by preventing other threat actors from initially accessing or maintaining a foothold on the same system.

For example, adversaries may patch a vulnerable, compromised system [1] [2] to prevent other threat actors from leveraging that vulnerability in the future. They may "close the door" in other ways, such as disabling vulnerable services [3] , stripping privileges from accounts [4] , or removing other malware already on the compromised device. [5]

Hindering other threat actors may allow an adversary to maintain sole access to a compromised system or network. This prevents the threat actor from needing to compete with or even being removed themselves by other threat actors. It also reduces the "noise" in the environment, lowering the possibility of being caught and evicted by defenders. Finally, in the case of Resource Hijacking , leveraging a compromised device’s full power allows the threat actor to maximize profit. [3]

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0015 | Detection Strategy for Exclusive Control | AN0045 | Detects unusual command executions and service modifications that indicate self-patching or disabling of vulnerable services post-compromise. Defenders should monitor for service stop commands, suspicious process termination, and execution of binaries or scripts aligned with known patching or service management tools outside of expected admin contexts. |
| AN0046 | Detects adversary attempts to monopolize control of compromised systems by issuing service stop commands, unloading vulnerable modules, or forcefully killing competing processes. Defenders should monitor audit logs and syslog for administrative utilities (systemctl, service, kill) being invoked outside of normal change management. |  |  |
| AN0047 | Detects unauthorized termination of system daemons or commands issued through launchctl or kill to stop competing services or malware processes. Defenders should monitor unified logs and EDR telemetry for unusual service modifications or terminations. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0015 | Detection Strategy for Exclusive Control | AN0045 | Detects unusual command executions and service modifications that indicate self-patching or disabling of vulnerable services post-compromise. Defenders should monitor for service stop commands, suspicious process termination, and execution of binaries or scripts aligned with known patching or service management tools outside of expected admin contexts. |
| AN0046 | Detects adversary attempts to monopolize control of compromised systems by issuing service stop commands, unloading vulnerable modules, or forcefully killing competing processes. Defenders should monitor audit logs and syslog for administrative utilities (systemctl, service, kill) being invoked outside of normal change management. |  |  |
| AN0047 | Detects unauthorized termination of system daemons or commands issued through launchctl or kill to stop competing services or malware processes. Defenders should monitor unified logs and EDR telemetry for unusual service modifications or terminations. |  |  |

---

## References

- [Michael Raggi, Adam Aprahamian, Dan Kelly, Mathew Potaczek, Marcin Siedlarz, Austin Larsen. (2024, March 21). Bringing Access Back — Initial Access Brokers Exploit F5 BIG-IP (CVE-2023-46747) and ScreenConnect. Retrieved January 31, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/initial-access-brokers-exploit-f5-screenconnect)
- [CERT Austria. (2025, March 20). Ransomware-Gruppen nutzen weiterhin kritische Fortinet-Schwachstellen - Warnung vor gepatchten, aber bereits kompromittierten Geräten. Retrieved March 31, 2025.](https://www.cert.at/de/warnungen/2025/3/ransomware-gruppen-nutzen-weiterhin-kritische-fortinet-schwachstellen-warnung-vor-gepatchten-aber-bereits-kompromittierten-geraten)
- [Matt Wixey. (2022, August 9). Multiple attackers increase pressure on victims, complicate incident response. Retrieved January 31, 2025.](https://news.sophos.com/en-us/2022/08/09/multiple-attackers-increase-pressure-on-victims-complicate-incident-response/#:~:text=While%20some%20threat%20actors%20are%20interdependent%20%28e.g.%2C%20IABs,vulnerabilities%20or%20disabling%20vulnerable%20services%20after%20gaining%20access)
- [Assaf Morag. (2024, August 19). PG_MEM: A Malware Hidden in the Postgres Processes. Retrieved January 31, 2025.](https://www.aquasec.com/blog/pg_mem-a-malware-hidden-in-the-postgres-processes/)
- [F-Secure. (2004). Worm:W32/NetSky.H. Retrieved January 31, 2025.](https://www.f-secure.com/v-descs/netsky-h.shtml)

---

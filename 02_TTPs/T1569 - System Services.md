# System Services

## Description

Adversaries may abuse system services or daemons to execute commands or programs. Adversaries can execute malicious content by interacting with or creating services either locally or remotely. Many services are set to run at boot, which can aid in achieving persistence ( Create or Modify System Process ), but adversaries can also abuse services for one-time or temporary execution.

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1040 | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to block processes created by PsExec from running. [1] |
| M1026 | Privileged Account Management | Ensure that permissions disallow services that run at a higher permissions level from being created or interacted with by a user with a lower permission level. |
| M1022 | Restrict File and Directory Permissions | Ensure that high permission level service binaries cannot be replaced or modified by users with a lower permission level. |
| M1018 | User Account Management | Prevent users from installing their own launch agents or launch daemons. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0279 | Detection Strategy for System Services across OS platforms. | AN0778 | Monitor for abnormal creation or modification of Windows services (e.g., via sc.exe, PowerShell, or API calls) that load non-standard executables. Correlate registry changes in service keys with service creation events and process execution to detect service abuse for persistence or execution. |
| AN0779 | Detect unusual invocations of systemctl, service, or init scripts creating or modifying daemons. Monitor audit logs for execution of binaries from unexpected paths linked to service start/stop activity. |  |  |
| AN0780 | Monitor launchd service definitions and property list (.plist) modifications for non-standard executables. Detect unauthorized processes registered as launch daemons or agents. |  |  |

---

## References

- [Microsoft. (2021, July 2). Use attack surface reduction rules to prevent malware infection. Retrieved June 24, 2021.](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)

---

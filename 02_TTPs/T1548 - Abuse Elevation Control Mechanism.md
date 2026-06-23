# Abuse Elevation Control Mechanism

## Description

Adversaries may circumvent mechanisms designed to control privilege elevation to gain higher-level permissions. Most modern systems contain native elevation control mechanisms that are intended to limit privileges that a user can perform on a machine. Authorization has to be granted to specific users in order to perform tasks that can be considered of higher risk. [1] [2] An adversary can perform several methods to take advantage of built-in control mechanisms in order to escalate privileges on a system. [3] [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1130 | Raspberry Robin | Raspberry Robin implements a variation of the ucmDccwCOMMethod technique abusing the Windows AutoElevate backdoor to bypass UAC while elevating privileges. [5] |
| G1048 | UNC3886 | UNC3886 has used vSphere Installation Bundles (VIBs) that contained modified descriptor XML files with the acceptance-level set to partner which allowed for privilege escalation. [6] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Check for common UAC bypass weaknesses on Windows systems to be aware of the risk posture and address issues where appropriate. [7] |
| M1038 | Execution Prevention | System settings can prevent applications from running that haven't been downloaded from legitimate repositories which may help mitigate some of these issues. Not allowing unsigned applications from being run may also mitigate some risk. |
| M1028 | Operating System Configuration | Applications with known vulnerabilities or known shell escapes should not have the setuid or setgid bits set to reduce potential damage if an application is compromised. Additionally, the number of programs with setuid or setgid bits set should be minimized across a system. Ensuring that the sudo tty_tickets setting is enabled will prevent this leakage across tty sessions. |
| M1026 | Privileged Account Management | Remove users from the local administrator group on systems. By requiring a password, even if an adversary can get terminal access, they must know the password to run anything in the sudoers file. Setting the timestamp_timeout to 0 will require the user to input their password every time sudo is executed. |
| M1022 | Restrict File and Directory Permissions | The sudoers file should be strictly edited such that passwords are always required and that users can't spawn risky processes as users with higher privilege. |
| M1051 | Update Software | Perform regular software updates to mitigate exploitation risk. |
| M1052 | User Account Control | Although UAC bypass techniques exist, it is still prudent to use the highest enforcement level for UAC when possible and mitigate bypass opportunities that exist with techniques such as DLL . |
| M1018 | User Account Management | Limit the privileges of cloud accounts to assume, create, or impersonate additional roles, policies, and permissions to only those required. Where just-in-time access is enabled, consider requiring manual approval for temporary elevation of privileges. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0345 | Detection Strategy for Abuse Elevation Control Mechanism (T1548) | AN0975 | Correlate registry modifications (e.g., UAC bypass registry keys), unusual parent-child process relationships (e.g., control.exe spawning cmd.exe), and unsigned elevated process executions with non-standard tokens or elevation flags. |
| AN0976 | Monitor audit logs for setuid/setgid bit changes, executions where UID ≠ EUID (indicative of sudo or privilege escalation), and high-integrity binaries launched by unprivileged users. |  |  |
| AN0977 | Detect execution of /usr/libexec/security_authtrampoline or use of AuthorizationExecuteWithPrivileges API, and monitor process lineage for unusual launches of GUI apps with escalated privileges. |  |  |
| AN0978 | Monitor for unexpected privilege elevation operations via SAML assertion manipulation, role injection, or changes to identity mappings that result in access escalation. |  |  |
| AN0979 | Detect sudden privilege escalations such as IAM role changes, user-assigned privilege boundaries, or elevation via assumed roles beyond normal behavior. |  |  |

---

## References

- [Lich, B. (2016, May 31). How User Account Control Works. Retrieved June 3, 2016.](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/how-user-account-control-works)
- [Todd C. Miller. (2018). Sudo Man Page. Retrieved March 19, 2018.](https://www.sudo.ws/)
- [Marc-Etienne M.Leveille. (2016, July 6). New OSX/Keydnap malware is hungry for credentials. Retrieved July 3, 2017.](https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/)
- [Salvio, J., Joven, R. (2016, December 16). Malicious Macro Bypasses UAC to Elevate Privilege for Fareit Malware. Retrieved December 27, 2016.](https://blog.fortinet.com/2016/12/16/malicious-macro-bypasses-uac-to-elevate-privilege-for-fareit-malware)
- [Christopher So. (2022, December 20). Raspberry Robin Malware Targets Telecom, Governments. Retrieved May 17, 2024.](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
- [Alexander Marvi, Jeremy Koppen, Tufail Ahmed, and Jonathan Lepore. (2022, September 29). Bad VIB(E)s Part One: Investigating Novel Malware Persistence Within ESXi Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
- [UACME Project. (2016, June 16). UACMe. Retrieved July 26, 2016.](https://github.com/hfiref0x/UACME)

---

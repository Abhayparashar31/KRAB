# Server Software Component

## Description

Adversaries may abuse legitimate extensible development features of servers to establish persistent access to systems. Enterprise server applications may include features that allow developers to write and install software or scripts to extend the functionality of the main application. Adversaries may install malicious components to extend and abuse server applications. [1]

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Regularly check component software on critical services that adversaries may target for persistence to verify the integrity of the systems and identify if unexpected changes have been made. |
| M1046 | Boot Integrity | Enabling secure boot allows validation of software and drivers during initial system boot. |
| M1045 | Code Signing | Ensure all application component binaries are signed by the correct application developers. |
| M1042 | Disable or Remove Feature or Program | Consider disabling software components from servers when possible to prevent abuse by adversaries. [2] |
| M1026 | Privileged Account Management | Do not allow administrator accounts that have permissions to add component software on these services to be used for day-to-day operations that may expose them to potential adversaries on unprivileged systems. |
| M1024 | Restrict Registry Permissions | Consider using Group Policy to configure and block modifications to service and other critical server parameters in the Registry. [3] |
| M1018 | User Account Management | Enforce the principle of least privilege by limiting privileges of user accounts so only authorized accounts can modify and/or add server software components. [4] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0547 | Detection Strategy for T1505 - Server Software Component | AN1507 | Installation of malicious IIS/Apache/SQL server modules that later execute command-line interpreters or establish outbound connections. |
| AN1508 | Abuse of extensible server modules (e.g., Apache, Nginx, Tomcat) to load rogue plugins that initiate bash, connect to C2, or spawn reverse shells. |  |  |
| AN1509 | Malicious use of webserver plugins (e.g., for nginx, PHP, Node.js) that execute AppleScript or open network sockets. |  |  |
| AN1510 | Use of ESXi web interface plugins or vSphere extensions to embed persistent malicious scripts or services. |  |  |

---

## References

- [Adair, S., Lancaster, T., Volexity Threat Research. (2022, June 15). DriftingCloud: Zero-Day Sophos Firewall Exploitation and an Insidious Breach. Retrieved July 1, 2022.](https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/)
- [Kondratiev, A. (n.d.). Disabling dangerous PHP functions. Retrieved July 26, 2021.](https://itsyndicate.org/blog/disabling-dangerous-php-functions/)
- [Microsoft. (2018, February 17). Windows System Services Fundamentals. Retrieved March 28, 2022.](https://social.technet.microsoft.com/wiki/contents/articles/12229.windows-system-services-fundamentals.aspx)
- [NSA and ASD. (2020, April 3). Detect and Prevent Web Shell Malware. Retrieved July 23, 2021.](https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF)

---

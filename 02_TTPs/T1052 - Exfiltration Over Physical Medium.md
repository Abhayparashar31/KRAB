# Exfiltration Over Physical Medium

## Description

Adversaries may attempt to exfiltrate data via a physical medium, such as a removable drive. In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a physical medium or device introduced by a user. Such media could be an external hard drive, USB drive, cellular phone, MP3 player, or other removable storage and processing device. The physical medium or device could be used as the final exfiltration point or to hop between otherwise disconnected systems.

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1057 | Data Loss Prevention | Data loss prevention can detect and block sensitive data being copied to physical mediums. |
| M1042 | Disable or Remove Feature or Program | Disable Autorun if it is unnecessary. [1] Disallow or restrict removable media at an organizational policy level if they are not required for business operations. [2] |
| M1034 | Limit Hardware Installation | Limit the use of USB devices and removable media within a network. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0123 | Detection of Data Exfiltration via Removable Media | AN0342 | Detects removable drive insertion followed by unusual file access, compression, or staging activity by unauthorized users or unexpected processes. |
| AN0343 | Detects mounted external devices (via /media or /mnt) followed by large file read or copy operations by shell scripts, unauthorized users, or staging tools (e.g., tar, rsync). |  |  |
| AN0344 | Detects mounting of external volumes followed by high-volume or sensitive file access via Finder, terminal, or third-party apps (e.g., rsync, zip). |  |  |

---

## References

- [Microsoft. (n.d.). How to disable the Autorun functionality in Windows. Retrieved April 20, 2016.](https://support.microsoft.com/en-us/kb/967715)
- [Microsoft. (2007, August 31). https://technet.microsoft.com/en-us/library/cc771759(v=ws.10).aspx. Retrieved April 20, 2016.](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)

---

# Communication Through Removable Media

## Description

Adversaries can perform command and control between compromised hosts on potentially disconnected networks using removable media to transfer commands from system to system. [1] Both systems would need to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral movement by Replication Through Removable Media . Commands and files would be relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0007 | APT28 | APT28 uses a tool that captures information from air-gapped computers via an infected USB and transfers it to network-connected computer when the USB is inserted. [2] |
| S0023 | CHOPSTICK | Part of APT28 's operation involved using CHOPSTICK modules to copy itself to air-gapped machines, using files written to USB sticks to transfer data and command traffic. [3] [4] [2] |
| S0136 | USBStealer | USBStealer drops commands for a second victim onto a removable media drive inserted into the first victim, and commands are executed when the drive is inserted into the second victim. [1] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1042 | Disable or Remove Feature or Program | Disable Autoruns if it is unnecessary. [5] |
| M1028 | Operating System Configuration | Disallow or restrict removable media at an organizational policy level if they are not required for business operations. [6] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0090 | Cross-host C2 via Removable Media Relay | AN0247 | Behavioral sequence where removable media is mounted, files are written/updated, and subsequently read/executed on a separate host, suggesting removable-media relay communication. |
| AN0248 | Detection of file write-access to USB-mount directories (e.g., /media/, /run/media/) followed by same-file access or execution on another host. |  |  |
| AN0249 | Correlates removable volume mounts (disk arbitration) with file I/O events on that volume, followed by same file execution shortly after insert. |  |  |

---

## References

- [Calvet, J. (2014, November 11). Sednit Espionage Group Attacking Air-Gapped Networks. Retrieved January 4, 2017.](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
- [Anthe, C. et al. (2015, October 19). Microsoft Security Intelligence Report Volume 19. Retrieved December 23, 2015.](http://download.microsoft.com/download/4/4/C/44CDEF0E-7924-4787-A56A-16261691ACE3/Microsoft_Security_Intelligence_Report_Volume_19_English.pdf)
- [FireEye. (2015). APT28: A WINDOW INTO RUSSIA’S CYBER ESPIONAGE OPERATIONS?. Retrieved August 19, 2015.](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
- [ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
- [Microsoft. (n.d.). How to disable the Autorun functionality in Windows. Retrieved April 20, 2016.](https://support.microsoft.com/en-us/kb/967715)
- [Microsoft. (2007, August 31). https://technet.microsoft.com/en-us/library/cc771759(v=ws.10).aspx. Retrieved April 20, 2016.](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)

---

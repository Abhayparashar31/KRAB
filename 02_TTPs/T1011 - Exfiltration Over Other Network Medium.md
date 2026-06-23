# Exfiltration Over Other Network Medium

## Description

Adversaries may attempt to exfiltrate data over a different network medium than the command and control channel. If the command and control network is a wired Internet connection, the exfiltration may occur, for example, over a WiFi connection, modem, cellular data connection, Bluetooth, or another radio frequency (RF) channel.

Adversaries may choose to do this if they have sufficient access or proximity, and the connection might not be secured or defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1042 | Disable or Remove Feature or Program | Disable WiFi connection, modem, cellular data connection, Bluetooth, or another radio frequency (RF) channel in local computer security settings or by group policy if it is not needed within an environment. |
| M1028 | Operating System Configuration | Prevent the creation of new network adapters where possible. [1] [2] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0077 | Detection of Exfiltration Over Alternate Network Interfaces | AN0212 | Execution of file transfer or network access activity through non-primary interfaces (e.g., WiFi, Bluetooth, cellular) by processes not typically associated with such behavior (e.g., rundll32, powershell, regsvr32). |
| AN0213 | Use of rfkill , nmcli , or low-level tools (e.g., iw , hcitool , pppd ) to enable alternate interfaces followed by data transfer via non-primary NICs. |  |  |
| AN0214 | AppleScript or system calls to activate WiFi/Bluetooth interfaces ( networksetup , blueutil ), followed by exfiltration via AirDrop, cloud sync, or network socket. |  |  |

---

## References

- [Microsoft. (2009, February 9). Disabling Bluetooth and Infrared Beaming. Retrieved July 26, 2018.](https://technet.microsoft.com/library/dd252791.aspx)
- [Schauland, D. (2009, February 24). Configuring Wireless settings via Group Policy. Retrieved July 26, 2018.](https://www.techrepublic.com/blog/data-center/configuring-wireless-settings-via-group-policy/)

---

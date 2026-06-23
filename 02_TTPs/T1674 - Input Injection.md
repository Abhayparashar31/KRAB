# Input Injection

## Description

Adversaries may simulate keystrokes on a victim’s computer by various means to perform any type of action on behalf of the user, such as launching the command interpreter using keyboard shortcuts, typing an inline script to be executed, or interacting directly with a GUI-based application. These actions can be preprogrammed into adversary tooling or executed through physical devices such as Human Interface Devices (HIDs).

For example, adversaries have used tooling that monitors the Windows message loop to detect when a user visits bank-specific URLs. If detected, the tool then simulates keystrokes to open the developer console or select the address bar, pastes malicious JavaScript from the clipboard, and executes it - enabling manipulation of content within the browser, such as replacing bank account numbers during transactions. [1] [2]

Adversaries have also used malicious USB devices to emulate keystrokes that launch PowerShell, leading to the download and execution of malware from adversary-controlled servers. [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0046 | FIN7 | FIN7 has used malicious USBs to emulate keystrokes to launch PowerShell to download and execute malware from the adversary's server. [4] [5] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1038 | Execution Prevention | Denylist scripting and use application control where appropriate. For example, PowerShell Constrained Language mode can be used to restrict access to sensitive or otherwise dangerous language elements such as those used to execute arbitrary Windows APIs or files (e.g., Add-Type ). [6] |
| M1034 | Limit Hardware Installation | Limit the use of USB devices and removable media within a network. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0568 | Detection Strategy for Input Injection | AN1567 | Detects suspicious USB HID device enumeration and keystroke injection patterns, such as rapid sequences of input with no user context, scripts executed through simulated keystrokes, or rogue devices presenting themselves as keyboards. |
| AN1568 | Detects USB HID device enumeration under /sys/bus/usb/devices/ and rapid keystroke injection resulting in command execution such as bash or Python scripts launched without interactive user activity. |  |  |
| AN1569 | Detects abnormal HID device enumeration via I/O Registry (ioreg -p IOUSB) and keystroke injection targeting AppleScript, osascript, or PowerShell equivalents. Defender correlates new USB device connections with rapid script execution. |  |  |

---

## References

- [Catalin Cimpanu. (2018, May 25). BackSwap Banking Trojan Uses Never-Before-Seen Techniques. Retrieved March 27, 2025.](https://www.bleepingcomputer.com/news/security/backswap-banking-trojan-uses-never-before-seen-techniques/)
- [Michal Poslušný. (2018, May 25). BackSwap malware finds innovative ways to empty bank accounts. Retrieved March 27, 2025.](https://www.welivesecurity.com/2018/05/25/backswap-malware-empty-bank-accounts/)
- [Ionut Ilascu. (2020, March 27). FBI: Hackers Sending Malicious USB Drives & Teddy Bears via USPS. Retrieved March 27, 2025.](https://www.bleepingcomputer.com/news/security/fbi-hackers-sending-malicious-usb-drives-and-teddy-bears-via-usps/)
- [The Record. (2022, January 7). FBI: FIN7 hackers target US companies with BadUSB devices to install ransomware. Retrieved January 14, 2022.](https://therecord.media/fbi-fin7-hackers-target-us-companies-with-badusb-devices-to-install-ransomware/)
- [Gemini Advisory. (2022, January 13). FIN7 Uses Flash Drives to Spread Remote Access Trojan. Retrieved May 14, 2025.](https://geminiadvisory.io/fin7-flash-drives-spread-remote-access-trojan/)
- [PowerShell Team. (2017, November 2). PowerShell Constrained Language Mode. Retrieved March 27, 2023.](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)

---

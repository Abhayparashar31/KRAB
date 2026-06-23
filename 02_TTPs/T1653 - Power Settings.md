# Power Settings

## Description

Adversaries may impair a system's ability to hibernate, reboot, or shut down in order to extend access to infected machines. When a computer enters a dormant state, some or all software and hardware may cease to operate which can disrupt malicious activity. [1]

Adversaries may abuse system utilities and configuration settings to maintain access by preventing machines from entering a state, such as standby, that can terminate malicious activity. [2] [3]

For example, powercfg controls all configurable power system settings on a Windows system and can be abused to prevent an infected host from locking or shutting down. [4] Adversaries may also extend system lock screen timeout settings. [5] Other relevant settings, such as disk and hibernate timeout, can be similarly abused to keep the infected machine running even if no user is active. [6]

Aware that some malware cannot survive system reboots, adversaries may entirely delete files used to invoke system shut down or reboot. [7]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0046 | ArcaneDoor | ArcaneDoor involved exploitation of CVE-2024-20353 to force a victim Cisco ASA to reboot, triggering the automated unzipping and execution of the Line Runner implant. [8] |
| S1186 | Line Dancer | Line Dancer can modify the crash dump process on infected machines to skip crash dump generation and proceed directly to device reboot for both persistence and forensic evasion purposes. [8] |
| S1188 | Line Runner | Line Runner used CVE-2024-20353 to trigger victim devices to reboot, in the process unzipping and installing the Line Dancer payload. [8] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Periodically inspect systems for abnormal and unexpected power settings that may indicate malicious activty. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0417 | Detection Strategy for Power Settings Abuse | AN1174 | Monitor command execution of powercfg.exe with arguments modifying sleep, hibernate, or display timeouts. Abnormal or repeated modifications to power settings outside administrative baselines may indicate persistence attempts. Correlate process creation with registry and system configuration changes to build behavioral chains. |
| AN1175 | Detect execution of system utilities (systemctl, systemd-inhibit, systemdsleep) modifying sleep or hibernate behavior. Abnormal edits to system configuration files (e.g., /etc/systemd/sleep.conf) should be correlated with process execution to identify persistence techniques. |  |  |
| AN1176 | Monitor pmset command executions altering sleep/hibernate/standby parameters. Unexpected modifications to /Library/Preferences/SystemConfiguration/com.apple.PowerManagement.plist or similar files should be correlated with process activity. |  |  |

---

## References

- [AVG. (n.d.). Should You Shut Down, Sleep or Hibernate Your PC or Mac Laptop?. Retrieved June 8, 2023.](https://www.avg.com/en/signal/should-you-shut-down-sleep-or-hibernate-your-pc-or-mac-laptop)
- [Microsoft. (2021, December 15). Powercfg command-line options. Retrieved June 5, 2023.](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/powercfg-command-line-options?adlt=strict)
- [Man7. (n.d.). systemd-sleep.conf(5) — Linux manual page. Retrieved June 7, 2023.](https://man7.org/linux/man-pages/man5/systemd-sleep.conf.5.html)
- [Douglas Bonderud. (2018, September 17). Two New Monero Malware Attacks Target Windows and Android Users. Retrieved June 5, 2023.](https://securityintelligence.com/news/two-new-monero-malware-attacks-target-windows-and-android-users/)
- [Bethany Hardin, Lavine Oluoch, Tatiana Vollbrecht. (2022, November 14). BATLOADER: The Evasive Downloader Malware. Retrieved June 5, 2023.](https://blogs.vmware.com/security/2022/11/batloader-the-evasive-downloader-malware.html)
- [Avira. (2019, November 28). CoinLoader: A Sophisticated Malware Loader Campaign. Retrieved June 5, 2023.](https://www.avira.com/en/blog/coinloader-a-sophisticated-malware-loader-campaign)
- [Joie Salvio and Roy Tay. (2023, June 20). Condi DDoS Botnet Spreads via TP-Link's CVE-2023-1389. Retrieved September 5, 2023.](https://www.fortinet.com/blog/threat-research/condi-ddos-botnet-spreads-via-tp-links-cve-2023-1389)
- [Cisco Talos. (2024, April 24). ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices. Retrieved January 6, 2025.](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)

---

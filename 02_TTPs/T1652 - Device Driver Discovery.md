# Device Driver Discovery

## Description

Adversaries may attempt to enumerate local device drivers on a victim host. Information about device drivers may highlight various insights that shape follow-on behaviors, such as the function/purpose of the host, present security tools (i.e. Security Software Discovery ) or other defenses (e.g., Virtualization/Sandbox Evasion ), as well as potential exploitable vulnerabilities (e.g., Exploitation for Privilege Escalation ).

Many OS utilities may provide information about local device drivers, such as driverquery.exe and the EnumDeviceDrivers() API function on Windows. [1] [2] Information about device drivers (as well as associated services, i.e., System Service Discovery ) may also be available in the Registry. [3]

On Linux/macOS, device drivers (in the form of kernel modules) may be visible within /dev or using utilities such as lsmod and modinfo . [4] [5] [6]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0376 | HOPLIGHT | HOPLIGHT can enumerate device drivers located in the registry at HKLM\Software\WBEM\WDM . [7] |
| S1139 | INC Ransomware | INC Ransomware can verify the presence of specific drivers on compromised hosts including Microsoft Print to PDF and Microsoft XPS Document Writer. [8] |
| G1051 | Medusa Group | Medusa Group has queried drivers on the victim device through the command driverquery . [9] |
| S0125 | Remsec | Remsec has a plugin to detect active drivers of some security products. [10] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0579 | Detection Strategy for Device Driver Discovery | AN1595 | Monitor for suspicious usage of driver enumeration utilities (driverquery.exe) or API calls such as EnumDeviceDrivers(). Registry queries against HKLM\SYSTEM\CurrentControlSet\Services and HardwareProfiles that are abnormal may also indicate attempts to discover installed drivers and services. Correlate command execution, process creation, and registry access to build a behavioral chain of driver discovery. |
| AN1596 | Detect attempts to enumerate kernel modules through lsmod, modinfo, or inspection of /proc/modules and /dev entries. Focus on unusual execution contexts such as unprivileged users or processes outside expected administrative workflows. |  |  |
| AN1597 | Detect loading or inspection of kernel extensions (kextstat, kextfind) and file access to /System/Library/Extensions/. Monitor unexpected usage of these utilities by non-administrative users or scripts. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0579 | Detection Strategy for Device Driver Discovery | AN1595 | Monitor for suspicious usage of driver enumeration utilities (driverquery.exe) or API calls such as EnumDeviceDrivers(). Registry queries against HKLM\SYSTEM\CurrentControlSet\Services and HardwareProfiles that are abnormal may also indicate attempts to discover installed drivers and services. Correlate command execution, process creation, and registry access to build a behavioral chain of driver discovery. |
| AN1596 | Detect attempts to enumerate kernel modules through lsmod, modinfo, or inspection of /proc/modules and /dev entries. Focus on unusual execution contexts such as unprivileged users or processes outside expected administrative workflows. |  |  |
| AN1597 | Detect loading or inspection of kernel extensions (kextstat, kextfind) and file access to /System/Library/Extensions/. Monitor unexpected usage of these utilities by non-administrative users or scripts. |  |  |

---

## References

- [Microsoft. (n.d.). driverquery. Retrieved March 28, 2023.](https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery)
- [Microsoft. (2021, October 12). EnumDeviceDrivers function (psapi.h). Retrieved March 28, 2023.](https://learn.microsoft.com/windows/win32/api/psapi/nf-psapi-enumdevicedrivers)
- [Microsoft. (2021, December 14). Registry Trees for Devices and Drivers. Retrieved March 28, 2023.](https://learn.microsoft.com/windows-hardware/drivers/install/overview-of-registry-trees-and-keys)
- [Pomerantz, O., Salzman, P.. (2003, April 4). The Linux Kernel Module Programming Guide. Retrieved April 6, 2018.](https://www.tldp.org/LDP/lkmpg/2.4/lkmpg.pdf)
- [Kerrisk, M. (2022, December 18). lsmod(8) — Linux manual page. Retrieved March 28, 2023.](https://man7.org/linux/man-pages/man8/lsmod.8.html)
- [Russell, R. (n.d.). modinfo(8) - Linux man page. Retrieved March 28, 2023.](https://linux.die.net/man/8/modinfo)
- [US-CERT. (2019, April 10). MAR-10135536-8 – North Korean Trojan: HOPLIGHT. Retrieved April 19, 2019.](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)

---

# Boot or Logon Autostart Execution

## Description

Adversaries may configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. Operating systems may have mechanisms for automatically running a program on system boot or account logon. [1] [2] [3] [4] [5] These mechanisms may include automatically executing programs that are placed in specially designated directories or are referenced by repositories that store configuration information, such as the Windows Registry. An adversary may achieve the same goal by modifying or extending features of the kernel.

Since some boot or logon autostart programs run with higher privileges, an adversary may leverage these to elevate privileges.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1044 | APT42 | APT42 has modified the Registry to maintain persistence. [6] |
| S0651 | BoxCaon | BoxCaon established persistence by setting the HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows\load registry key to point to its executable. [7] |
| S0567 | Dtrack | Dtrack ’s RAT makes a persistent target file with auto execution on the host start. [8] |
| S0084 | Mis-Type | Mis-Type has created registry keys for persistence, including HKCU\Software\bkfouerioyou , HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\{6afa8072-b2b1-31a8-b5c1-{Unique Identifier} , and HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\{3BF41072-B2B1-31A8-B5C1-{Unique Identifier} . [9] |
| S0083 | Misdat | Misdat has created registry keys for persistence, including HKCU\Software\dnimtsoleht\StubPath , HKCU\Software\snimtsOleht\StubPath , HKCU\Software\Backtsaleht\StubPath , HKLM\SOFTWARE\Microsoft\Active Setup\Installed. Components\{3bf41072-b2b1-21c8-b5c1-bd56d32fbda7} , and HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\{3ef41072-a2f1-21c8-c5c1-70c2c3bc7905} . [9] |
| S0653 | xCaon | xCaon has added persistence via the Registry key HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows\load which causes the malware to run each time any user logs in. [7] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0274 | Boot or Logon Autostart Execution Detection Strategy | AN0764 | Correlation of registry key modification for Run/RunOnce with abnormal parent-child process relationships and outlier execution at user logon or system startup |
| AN0765 | Correlates creation/modification of systemd service files or /etc/init.d scripts with outlier process behavior during boot |  |  |
| AN0766 | Observes creation or modification of LaunchAgent/LaunchDaemon property list files combined with anomalous plist payload execution after user logon |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0274 | Boot or Logon Autostart Execution Detection Strategy | AN0764 | Correlation of registry key modification for Run/RunOnce with abnormal parent-child process relationships and outlier execution at user logon or system startup |
| AN0765 | Correlates creation/modification of systemd service files or /etc/init.d scripts with outlier process behavior during boot |  |  |
| AN0766 | Observes creation or modification of LaunchAgent/LaunchDaemon property list files combined with anomalous plist payload execution after user logon |  |  |

---

## References

- [Microsoft. (n.d.). Run and RunOnce Registry Keys. Retrieved September 12, 2024.](https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys)
- [Microsoft. (n.d.). Authentication Packages. Retrieved March 1, 2017.](https://msdn.microsoft.com/library/windows/desktop/aa374733.aspx)
- [Microsoft. (n.d.). Time Provider. Retrieved March 26, 2018.](https://msdn.microsoft.com/library/windows/desktop/ms725475.aspx)
- [Langendorf, S. (2013, September 24). Windows Registry Persistence, Part 2: The Run Keys and Search-Order. Retrieved November 17, 2024.](https://web.archive.org/web/20160214140250/http://blog.cylance.com/windows-registry-persistence-part-2-the-run-keys-and-search-order)
- [Pomerantz, O., Salzman, P.. (2003, April 4). The Linux Kernel Module Programming Guide. Retrieved April 6, 2018.](https://www.tldp.org/LDP/lkmpg/2.4/lkmpg.pdf)
- [Mandiant. (n.d.). APT42: Crooked Charms, Cons and Compromises. Retrieved October 9, 2024.](https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf)
- [CheckPoint Research. (2021, July 1). IndigoZebra APT continues to attack Central Asia with evolving tools. Retrieved September 24, 2021.](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
- [Konstantin Zykov. (2019, September 23). Hello! My name is Dtrack. Retrieved January 20, 2021.](https://securelist.com/my-name-is-dtrack/93338/)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Dragonforce]] [related_actor:: [[Dragonforce]]]

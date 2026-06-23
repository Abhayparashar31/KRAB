# Input Capture

## Description

Adversaries may use methods of capturing user input to obtain credentials or collect information. During normal system usage, users often provide credentials to various different locations, such as login pages/portals or system dialog boxes. Input capture mechanisms may be transparent to the user (e.g. Credential API Hooking ) or rely on deceiving the user into providing input into what they believe to be a genuine service (e.g. Web Portal Capture ).

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0087 | APT39 | APT39 has utilized tools to capture mouse movements. [1] |
| G1044 | APT42 | APT42 has used credential harvesting websites. [2] |
| S0631 | Chaes | Chaes has a module to perform any API hooking it desires. [3] |
| S0381 | FlawedAmmyy | FlawedAmmyy can collect mouse events. [4] |
| S1245 | InvisibleFerret | InvisibleFerret has collected mouse and keyboard events using "pyWinhook". [5] |
| S0641 | Kobalos | Kobalos has used a compromised SSH client to capture the hostname, port, username and password used to establish an SSH connection from the compromised host. [6] [7] |
| C0049 | Leviathan Australian Intrusions | Leviathan captured submitted multfactor authentication codes and other technical artifacts related to remote access sessions during Leviathan Australian Intrusions . [8] |
| S1060 | Mafalda | Mafalda can conduct mouse event logging. [9] |
| S1059 | metaMain | metaMain can log mouse events. [9] |
| S1131 | NPPSPY | NPPSPY captures user input into the Winlogon process by redirecting RPC traffic from legitimate listening DLLs within the operating system to a newly registered malicious item that allows for recording logon information in cleartext. [10] |
| G1046 | Storm-1811 | Storm-1811 has used a PowerShell script to capture user credentials after prompting a user to authenticate to run a malicious script masquerading as a legitimate update item. [11] |
| C0039 | Versa Director Zero Day Exploitation | Versa Director Zero Day Exploitation intercepted and harvested credentials from user logins to compromised devices. [12] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0102 | Behavioral Detection of Input Capture Across Platforms | AN0282 | Monitors for abnormal process behavior and API calls like SetWindowsHookEx, GetAsyncKeyState, or device input polling commonly used for keystroke logging. |
| AN0283 | Detects use of tools/scripts accessing input devices like /dev/input/* or evdev via suspicious processes lacking GUI context. |  |  |
| AN0284 | Monitors for TCC-bypassing or unauthorized access to input services like IOHIDSystem or Quartz Event Services used in keylogging or screen monitoring. |  |  |
| AN0285 | Detects web-based credential phishing by analyzing traffic to suspicious URLs that mimic login portals and POST credential content. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0102 | Behavioral Detection of Input Capture Across Platforms | AN0282 | Monitors for abnormal process behavior and API calls like SetWindowsHookEx, GetAsyncKeyState, or device input polling commonly used for keystroke logging. |
| AN0283 | Detects use of tools/scripts accessing input devices like /dev/input/* or evdev via suspicious processes lacking GUI context. |  |  |
| AN0284 | Monitors for TCC-bypassing or unauthorized access to input services like IOHIDSystem or Quartz Event Services used in keylogging or screen monitoring. |  |  |
| AN0285 | Detects web-based credential phishing by analyzing traffic to suspicious URLs that mimic login portals and POST credential content. |  |  |

---

## References

- [FBI. (2020, September 17). Indicators of Compromise Associated with Rana Intelligence Computing, also known as Advanced Persistent Threat 39, Chafer, Cadelspy, Remexi, and ITG07. Retrieved December 10, 2020.](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)
- [Rozmann, O., et al. (2024, May 1). Uncharmed: Untangling Iran's APT42 Operations. Retrieved October 9, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/untangling-iran-apt42-operations)
- [Salem, E. (2020, November 17). CHAES: Novel Malware Targeting Latin American E-Commerce. Retrieved June 30, 2021.](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
- [Financial Security Institute. (2020, February 28). Profiling of TA505 Threat Group That Continues to Attack the Financial Sector. Retrieved July 14, 2022.](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [M.Leveille, M., Sanmillan, I. (2021, February 2). Kobalos – A complex Linux threat to high performance computing infrastructure. Retrieved August 24, 2021.](https://www.welivesecurity.com/2021/02/02/kobalos-complex-linux-threat-high-performance-computing-infrastructure/)
- [M.Leveille, M., Sanmillan, I. (2021, January). A WILD KOBALOS APPEARS Tricksy Linux malware goes after HPCs. Retrieved August 24, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
- [CISA et al. (2024, July 8). People’s Republic of China (PRC) Ministry of State Security APT40 Tradecraft in Action. Retrieved February 3, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [Dray Agha. (2022, August 16). Cleartext Shenanigans: Gifting User Passwords to Adversaries With NPPSPY. Retrieved May 17, 2024.](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
- [Tyler McGraw, Thomas Elkins, and Evan McCann. (2024, May 10). Ongoing Social Engineering Campaign Linked to Black Basta Ransomware Operators. Retrieved January 31, 2025.](https://www.rapid7.com/blog/post/2024/05/10/ongoing-social-engineering-campaign-linked-to-black-basta-ransomware-operators)
- [Black Lotus Labs. (2024, August 27). Taking The Crossroads: The Versa Director Zero-Day Exploitaiton. Retrieved August 27, 2024.](https://blog.lumen.com/taking-the-crossroads-the-versa-director-zero-day-exploitation/)

---

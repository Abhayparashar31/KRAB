# Office Application Startup

## Description

Adversaries may leverage Microsoft Office-based applications for persistence between startups. Microsoft Office is a fairly common application suite on Windows-based operating systems within an enterprise network. There are multiple mechanisms that can be used with Office for persistence when an Office-based application is started; this can include the use of Office Template Macros and add-ins.

A variety of features have been discovered in Outlook that can be abused to obtain persistence, such as Outlook rules, forms, and Home Page. [1] These persistence mechanisms can work within Outlook or be used through Office 365. [2]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0050 | APT32 | APT32 have replaced Microsoft Outlook's VbaProject.OTM file to install a backdoor macro for persistence. [3] [4] |
| G0047 | Gamaredon Group | Gamaredon Group has inserted malicious macros into existing documents, providing persistence when they are reopened. Gamaredon Group has loaded the group's previously delivered VBA project by relaunching Microsoft Outlook with the /altvba option, once the Application.Startup event is received. [5] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1040 | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent Office applications from creating child processes and from writing potentially malicious executable content to disk. [6] |
| M1042 | Disable or Remove Feature or Program | Follow Office macro security best practices suitable for your environment. Disable Office VBA macros from executing. Disable Office add-ins. If they are required, follow best practices for securing them by requiring them to be signed and disabling user notification for allowing add-ins. For some add-ins types (WLL, VBA) additional mitigation is likely required as disabling add-ins in the Office Trust Center does not disable WLL nor does it prevent VBA code from executing. [7] |
| M1054 | Software Configuration | For the Office Test method, create the Registry key used to execute it and set the permissions to "Read Control" to prevent easy access to the key without administrator permissions or requiring Privilege Escalation. [8] |
| M1051 | Update Software | For the Outlook methods, blocking macros may be ineffective as the Visual Basic engine used for these features is separate from the macro scripting engine. [9] Microsoft has released patches to try to address each issue. Ensure KB3191938 which blocks Outlook Visual Basic and displays a malicious code warning, KB4011091 which disables custom forms by default, and KB4011162 which removes the legacy Home Page feature, are applied to systems. [10] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0398 | Detect Office Startup-Based Persistence via Macros, Forms, and Registry Hooks | AN1116 | Office-based persistence via Office template macros, Outlook forms/rules/homepage, or registry-persistent scripts. Adversary modifies registry keys or Office application directories to load malicious scripts at startup. |
| AN1117 | Startup-based persistence mechanisms within Microsoft Office Suite like template macros and home page redirects being configured through internal automation or client-side settings. |  |  |

---

## References

- [SensePost. (2016, August 18). Ruler: A tool to abuse Exchange services. Retrieved February 4, 2019.](https://github.com/sensepost/ruler)
- [Koeller, B.. (2018, February 21). Defending Against Rules and Forms Injection. Retrieved November 5, 2019.](https://blogs.technet.microsoft.com/office365security/defending-against-rules-and-forms-injection/)
- [Dahan, A. (2017, May 24). OPERATION COBALT KITTY: A LARGE-SCALE APT IN ASIA CARRIED OUT BY THE OCEANLOTUS GROUP. Retrieved November 5, 2018.](https://www.cybereason.com/blog/operation-cobalt-kitty-apt)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [Microsoft. (2021, July 2). Use attack surface reduction rules to prevent malware infection. Retrieved June 24, 2021.](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
- [Knowles, W. (2017, April 21). Add-In Opportunities for Office Persistence. Retrieved November 17, 2024.](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)
- [Falcone, R. (2016, July 20). Technical Walkthrough: Office Test Persistence Method Used In Recent Sofacy Attacks. Retrieved July 3, 2017.](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)
- [Stalmans, E. (2017, April 28). Outlook Forms and Shells. Retrieved February 4, 2019.](https://sensepost.com/blog/2017/outlook-forms-and-shells/)
- [Stalmans, E. (2017, October 11). Outlook Home Page – Another Ruler Vector. Retrieved February 4, 2019.](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)

---

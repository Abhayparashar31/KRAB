# BITS Jobs

## Description

Adversaries may abuse BITS jobs to persistently execute code and perform various background tasks. Windows Background Intelligent Transfer Service (BITS) is a low-bandwidth, asynchronous file transfer mechanism exposed through Component Object Model (COM). [1] [2] BITS is commonly used by updaters, messengers, and other applications preferred to operate in the background (using available idle bandwidth) without interrupting other networked applications. File transfer tasks are implemented as BITS jobs, which contain a queue of one or more file operations.

The interface to create and manage BITS jobs is accessible through PowerShell and the BITSAdmin tool. [2] [3]

Adversaries may abuse BITS to download (e.g. Ingress Tool Transfer ), execute, and even clean up after running malicious code (e.g. Indicator Removal ). BITS tasks are self-contained in the BITS job database, without new files or registry modifications, and often permitted by host firewalls. [4] [5] [6] BITS enabled execution may also enable persistence by creating long-standing jobs (the default maximum lifetime is 90 days and extendable) or invoking an arbitrary program when a job completes or errors (including after system reboots). [7] [4]

BITS upload functionalities can also be used to perform Exfiltration Over Alternative Protocol . [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0087 | APT39 | APT39 has used the BITS protocol to exfiltrate stolen data from a compromised host. [8] |
| G0096 | APT41 | APT41 used BITSAdmin to download and install payloads. [9] [10] |
| S0534 | Bazar | Bazar has been downloaded via Windows BITS functionality. [11] |
| S0190 | BITSAdmin | BITSAdmin can be used to create BITS Jobs to launch a malicious process. [12] |
| S0154 | Cobalt Strike | Cobalt Strike can download a hosted "beacon" payload using BITSAdmin . [13] [14] [15] |
| S0554 | Egregor | Egregor has used BITSadmin to download and execute malicious DLLs. [16] |
| S0201 | JPIN | A JPIN variant downloads the backdoor payload via the BITS service. [17] |
| G0065 | Leviathan | Leviathan has used BITSAdmin to download additional tools. [18] |
| S0652 | MarkiRAT | MarkiRAT can use BITS Utility to connect with the C2 server. [19] |
| G0040 | Patchwork | Patchwork has used BITS jobs to download malicious payloads. [20] |
| S0654 | ProLock | ProLock can use BITS jobs to download its malicious payload. [21] |
| S0333 | UBoatRAT | UBoatRAT takes advantage of the /SetNotifyCmdLine option in BITSAdmin to ensure it stays running on a system to maintain persistence. [7] |
| G0102 | Wizard Spider | Wizard Spider has used batch scripts that utilizes WMIC to execute a BITSAdmin transfer of a ransomware payload to each compromised machine. [22] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1037 | Filter Network Traffic | Modify network and/or host firewall rules, as well as other network controls, to only allow legitimate BITS traffic. |
| M1028 | Operating System Configuration | Consider reducing the default BITS job lifetime in Group Policy or by editing the JobInactivityTimeout and MaxDownloadTime Registry values in HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\BITS . [2] |
| M1018 | User Account Management | Consider limiting access to the BITS interface to specific users or groups. [6] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0098 | Detect abuse of Windows BITS Jobs for download, execution and persistence | AN0274 | Behavioral chain: (1) An actor creates or modifies a BITS job via bitsadmin.exe, PowerShell BITS cmdlets, or COM; (2) the job performs HTTP(S)/SMB network transfers while the owning user is logged on; (3) upon job completion/error, BITS launches a notify command (SetNotifyCmdLine) from svchost.exe -k netsvcs -s BITS, often establishing persistence by keeping long-lived jobs. The strategy correlates process creation, command/script telemetry, BITS-Client operational events, and network connections initiated by BITS. |

---

## References

- [Microsoft. (n.d.). Component Object Model (COM). Retrieved November 22, 2017.](https://msdn.microsoft.com/library/windows/desktop/ms680573.aspx)
- [Microsoft. (n.d.). Background Intelligent Transfer Service. Retrieved January 12, 2018.](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)
- [Microsoft. (n.d.). BITSAdmin Tool. Retrieved January 12, 2018.](https://msdn.microsoft.com/library/aa362813.aspx)
- [Counter Threat Unit Research Team. (2016, June 6). Malware Lingers with BITS. Retrieved January 12, 2018.](https://www.secureworks.com/blog/malware-lingers-with-bits)
- [Mondok, M. (2007, May 11). Malware piggybacks on Windows’ Background Intelligent Transfer Service. Retrieved January 12, 2018.](https://arstechnica.com/information-technology/2007/05/malware-piggybacks-on-windows-background-intelligent-transfer-service/)
- [Florio, E. (2007, May 9). Malware Update with Windows Update. Retrieved January 12, 2018.](https://www.symantec.com/connect/blogs/malware-update-windows-update)
- [Hayashi, K. (2017, November 28). UBoatRAT Navigates East Asia. Retrieved January 12, 2018.](https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/)
- [FBI. (2020, September 17). Indicators of Compromise Associated with Rana Intelligence Computing, also known as Advanced Persistent Threat 39, Chafer, Cadelspy, Remexi, and ITG07. Retrieved December 10, 2020.](https://www.iranwatch.org/sites/default/files/public-intelligence-alert.pdf)
- [Glyer, C, et al. (2020, March). This Is Not a Test: APT41 Initiates Global Intrusion Campaign Using Multiple Exploits. Retrieved April 28, 2020.](https://www.fireeye.com/blog/threat-research/2020/03/apt41-initiates-global-intrusion-campaign-using-multiple-exploits.html)
- [Crowdstrike. (2020, March 2). 2020 Global Threat Report. Retrieved December 11, 2020.](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)
- [Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1, 2020.](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
- [Horejsi, J., et al. (2018, March 14). Tropic Trooper’s New Strategy. Retrieved November 9, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/tropic-trooper-new-strategy/)
- [Strategic Cyber, LLC. (n.d.). Scripted Web Delivery. Retrieved January 23, 2018.](https://www.cobaltstrike.com/help-scripted-web-delivery)
- [Mavis, N. (2020, September 21). The Art and Science of Detecting Cobalt Strike. Retrieved September 12, 2024.](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Bichet, J. (2020, November 12). Egregor – Prolock: Fraternal Twins ?. Retrieved January 6, 2021.](https://www.intrinsec.com/egregor-prolock/?cn-reloaded=1)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [GReAT. (2021, June 16). Ferocious Kitten: 6 Years of Covert Surveillance in Iran. Retrieved September 22, 2021.](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
- [Hinchliffe, A. and Falcone, R. (2020, May 11). Updated BackConfig Malware Targeting Government and Military Organizations in South Asia. Retrieved June 17, 2020.](https://unit42.paloaltonetworks.com/updated-backconfig-malware-targeting-government-and-military-organizations/)
- [Group IB. (2020, September). LOCK LIKE A PRO. Retrieved November 17, 2024.](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)

---

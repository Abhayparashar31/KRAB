# System Shutdown/Reboot

## Description

Adversaries may shutdown/reboot systems to interrupt access to, or aid in the destruction of, those systems. Operating systems may contain commands to initiate a shutdown/reboot of a machine or network device. In some cases, these commands may also be used to initiate a shutdown/reboot of a remote computer or network device via Network Device CLI (e.g. reload ). [1] [2] They may also include shutdown/reboot of a virtual machine via hypervisor / cloud consoles or command line tools.

Shutting down or rebooting systems may disrupt access to computer resources for legitimate users while also impeding incident response/recovery.

Adversaries may also use Windows API functions, such as InitializeSystemShutdownExW or ExitWindowsEx , to force a system to shut down or reboot. [3] [4] Alternatively, the NtRaiseHardError or ZwRaiseHardError Windows API functions with the ResponseOption parameter set to OptionShutdownSystem may deliver a "blue screen of death" (BSOD) to a system. [5] [6] [7] In order to leverage these API functions, an adversary may need to acquire SeShutdownPrivilege (e.g., via Access Token Manipulation ). [4] In some cases, the system may not be able to boot again.

Adversaries may attempt to shutdown/reboot a system after impacting it in other ways, such as Disk Structure Wipe or Inhibit System Recovery , to hasten the intended effects on system availability. [8] [9]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries forced victim devices to reboot to finalize destruction of impacted systems. [10] [11] |
| S1167 | AcidPour | AcidPour includes functionality to reboot the victim system following wiping actions, similar to AcidRain . [12] |
| S1125 | AcidRain | AcidRain reboots the target system once the various wiping processes are complete. [13] |
| S1133 | Apostle | Apostle reboots the victim machine following wiping and related activity. [14] |
| G0067 | APT37 | APT37 has used malware that will issue the command shutdown /r /t 1 to reboot a system after wiping its MBR. [15] |
| G0082 | APT38 | APT38 has used a custom MBR wiper named BOOTWRECK, which will initiate a system reboot after wiping the victim's MBR. [16] |
| S1053 | AvosLocker | AvosLocker ’s Linux variant has terminated ESXi virtual machines. [17] |
| S1136 | BFG Agonizer | BFG Agonizer uses elevated privileges to call NtRaiseHardError to induce a "blue screen of death" on infected systems, causing a system crash. Once shut down, the system is no longer bootable. [4] |
| S1070 | Black Basta | Black Basta has used ShellExecuteA to shut down and restart the victim system. [18] |
| S1149 | CHIMNEYSWEEP | CHIMNEYSWEEP can reboot or shutdown the targeted system or logoff the current user. [19] |
| S1111 | DarkGate | DarkGate has used the shutdown command to shut down and/or restart the victim system. [20] |
| S1033 | DCSrv | DCSrv has a function to sleep for two hours before rebooting the system. [21] |
| S9038 | DynoWiper | DynoWiper has used the Microsoft Windows native ExitWindowsEx() function to log off the interactive user and shutdown the system. [22] |
| S0697 | HermeticWiper | HermeticWiper can initiate a system shutdown. [23] [24] |
| S0607 | KillDisk | KillDisk attempts to reboot the machine by terminating specific processes. [25] |
| S1160 | Latrodectus | Latrodectus has the ability to restart compromised hosts. [26] |
| G0032 | Lazarus Group | Lazarus Group has rebooted systems after destroying files and wiping the MBR on infected systems. [27] |
| S0372 | LockerGoga | LockerGoga has been observed shutting down infected systems. [28] |
| S0582 | LookBack | LookBack can shutdown and reboot the victim machine. [29] |
| S0449 | Maze | Maze has issued a shutdown command on a victim machine that, upon reboot, will run the ransomware within a VM. [30] |
| G1051 | Medusa Group | Medusa Group has manually turned off and encrypted virtual machines. [31] |
| S1135 | MultiLayer Wiper | MultiLayer Wiper reboots the infected system following wiping and related tasks to prevent system recovery. [4] |
| S0368 | NotPetya | NotPetya will reboot the system one hour after infection. [8] [32] |
| S0365 | Olympic Destroyer | Olympic Destroyer will shut down the compromised system after it is done modifying system configuration settings. [9] [32] |
| S1242 | Qilin | Qilin can initiate a reboot of the backup server to hinder recovery. [33] |
| S0332 | Remcos | Remcos can shutdown and restart remote devices. [34] |
| S0140 | Shamoon | Shamoon will reboot the infected system once the wiping functionality has been completed. [35] [36] |
| S1178 | ShrinkLocker | ShrinkLocker can restart the victim system if it encounters an error during execution, and will forcibly shutdown the system following encryption to lock out victim users. [37] |
| S0689 | WhisperGate | WhisperGate can shutdown a compromised host through execution of ExitWindowsEx with the EXW_SHUTDOWN flag. [38] |
| S1207 | XLoader | XLoader can initiate a system reboot or shutdown. [39] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0559 | Multi-Platform Shutdown or Reboot Detection via Execution and Host Status Events | AN1538 | Correlate process execution of shutdown/reboot commands (e.g., shutdown.exe, restart-computer) with host status change logs (Event IDs 1074, 6006) and absence of related administrative context (e.g., user not in Helpdesk group). |
| AN1539 | Detect 'shutdown', 'reboot', or 'systemctl poweroff' executions with auditd/syslog and absence of scheduled maintenance windows or approved user context. |  |  |
| AN1540 | Identify use of 'shutdown', 'reboot', or 'osascript' system shutdown invocations within unified logs and track unexpected shutdown sequences initiated by GUI or script. Cross-reference with user activity or absence thereof. |  |  |
| AN1541 | Detect commands such as 'esxcli system shutdown' or 'vim-cmd vmsvc/power.shutdown' executed outside of maintenance windows or via unusual users. Reboot logs in hostd.log and shell logs should be correlated. |  |  |
| AN1542 | Monitor CLI 'reload' commands issued without scheduled maintenance, and correlate to TACACS+/AAA logs for privilege validation. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0559 | Multi-Platform Shutdown or Reboot Detection via Execution and Host Status Events | AN1538 | Correlate process execution of shutdown/reboot commands (e.g., shutdown.exe, restart-computer) with host status change logs (Event IDs 1074, 6006) and absence of related administrative context (e.g., user not in Helpdesk group). |
| AN1539 | Detect 'shutdown', 'reboot', or 'systemctl poweroff' executions with auditd/syslog and absence of scheduled maintenance windows or approved user context. |  |  |
| AN1540 | Identify use of 'shutdown', 'reboot', or 'osascript' system shutdown invocations within unified logs and track unexpected shutdown sequences initiated by GUI or script. Cross-reference with user activity or absence thereof. |  |  |
| AN1541 | Detect commands such as 'esxcli system shutdown' or 'vim-cmd vmsvc/power.shutdown' executed outside of maintenance windows or via unusual users. Reboot logs in hostd.log and shell logs should be correlated. |  |  |
| AN1542 | Monitor CLI 'reload' commands issued without scheduled maintenance, and correlate to TACACS+/AAA logs for privilege validation. |  |  |

---

## References

- [Microsoft. (2017, October 15). Shutdown. Retrieved October 4, 2019.](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown)
- [CISA. (2018, April 20). Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved February 14, 2022.](https://www.cisa.gov/uscert/ncas/alerts/TA18-106A)
- [William Thomas, Adrian Liviu Arsene, Farid Hendi. (2022, February 25). CrowdStrike Falcon® Protects from New Wiper Malware Used in Ukraine Cyberattacks. Retrieved September 22, 2025.](https://www.crowdstrike.com/en-us/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [SecurityNews. (2024, July 12). Disarming DarkGate: A Deep Dive into Thwarting the Latest DarkGate Variant. Retrieved September 22, 2025.](https://www.sonicwall.com/blog/disarming-darkgate-a-deep-dive-into-thwarting-the-latest-darkgate-variant)
- [NtDoc. (n.d.). NtRaiseHardError - NtDoc. Retrieved September 22, 2025.](https://ntdoc.m417z.com/ntraiseharderror)
- [lzcapp. (n.d.). Retrieved September 22, 2025.](https://github.com/lzcapp/NotMe-BSOD)
- [Chiu, A. (2016, June 27). New Ransomware Variant "Nyetya" Compromises Systems Worldwide. Retrieved March 26, 2019.](https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html)
- [Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [ESET. (2026, January 30). Russian Sandworm group attacks energy company in Poland with DynoWiper, ESET Research discovers. Retrieved April 22, 2026.](https://www.eset.com/us/about/newsroom/research/eset-research-russian-sandwormapt-attacks-energy-company-poland-with-dynowiper/)
- [ESET. (2026, January 30). DynoWiper update: Technical analysis and attribution. Retrieved April 22, 2026.](https://www.welivesecurity.com/en/eset-research/dynowiper-update-technical-analysis-attribution/)
- [Juan Andrés Guerrero-Saade & Tom Hegel. (2024, March 21). AcidPour | New Embedded Wiper Variant of AcidRain Appears in Ukraine. Retrieved November 25, 2024.](https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/)
- [Juan Andres Guerrero-Saade and Max van Amerongen, SentinelOne. (2022, March 31). AcidRain | A Modem Wiper Rains Down on Europe. Retrieved March 25, 2024.](https://www.sentinelone.com/labs/acidrain-a-modem-wiper-rains-down-on-europe/)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [Mercer, W., Rascagneres, P. (2018, January 16). Korea In The Crosshairs. Retrieved May 21, 2018.](https://blog.talosintelligence.com/2018/01/korea-in-crosshairs.html)
- [FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)
- [Trend Micro Research. (2022, April 4). Ransomware Spotlight AvosLocker. Retrieved January 11, 2023.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-avoslocker)
- [Gonzalez, I., Chavez I., et al. (2022, May 9). Examining the Black Basta Ransomware’s Infection Routine. Retrieved March 7, 2023.](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [McGraw, T. (2024, December 4). Black Basta Ransomware Campaign Drops Zbot, DarkGate, and Custom Malware. Retrieved December 9, 2024.](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
- [Checkpoint Research. (2021, November 15). Uncovering MosesStaff techniques: Ideology over Money. Retrieved August 11, 2022.](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Guerrero-Saade, J. (2022, February 23). HermeticWiper | New Destructive Malware Used In Cyber Attacks on Ukraine. Retrieved March 25, 2022.](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack)
- [Dani, M. (2022, March 1). Ukrainian Targets Hit by HermeticWiper, New Datawiper Malware. Retrieved March 25, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
- [Gilbert Sison, Rheniel Ramos, Jay Yaneza, Alfredo Oliveira. (2018, January 15). KillDisk Variant Hits Latin American Financial Groups. Retrieved January 12, 2021.](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)
- [Stepanic, D. and Bousseaden, S. (2024, May 15). Spring Cleaning with LATRODECTUS: A Potential Replacement for ICEDID. Retrieved September 13, 2024.](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
- [US-CERT. (2018, March 09). Malware Analysis Report (MAR) - 10135536.11.WHITE. Retrieved June 13, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536.11.WHITE.pdf)
- [Greenberg, A. (2019, March 25). A Guide to LockerGoga, the Ransomware Crippling Industrial Firms. Retrieved July 17, 2019.](https://www.wired.com/story/lockergoga-ransomware-crippling-industrial-firms/)
- [Raggi, M. Schwarz, D.. (2019, August 1). LookBack Malware Targets the United States Utilities Sector with Phishing Attacks Impersonating Engineering Licensing Boards. Retrieved February 25, 2021.](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
- [Brandt, A., Mackenzie, P.. (2020, September 17). Maze Attackers Adopt Ragnar Locker Virtual Machine Technique. Retrieved October 9, 2020.](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Scott W. Brady. (2020, October 15). United States vs. Yuriy Sergeyevich Andrienko et al.. Retrieved November 25, 2020.](https://www.justice.gov/opa/press-release/file/1328521/download)
- [Hacioglu, S. (2025, March 10). Qilin Ransomware: Exposing the TTPs Behind One of the Most Active Ransomware Campaigns of 2024. Retrieved September 26, 2025.](https://www.picussecurity.com/resource/blog/qilin-ransomware)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Falcone, R. (2018, December 13). Shamoon 3 Targets Oil and Gas Organization. Retrieved March 14, 2019.](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
- [Mundo, A., Roccia, T., Saavedra-Morales, J., Beek, C.. (2018, December 14). Shamoon Returns to Wipe Systems in Middle East, Europe . Retrieved May 29, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/)
- [Cristian Souza, Eduardo Ovalle, Ashley Muñoz, & Christopher Zachor. (2024, May 23). ShrinkLocker: Turning BitLocker into ransomware. Retrieved December 7, 2024.](https://securelist.com/ransomware-abuses-bitlocker/112643/)
- [Biasini, N. et al.. (2022, January 21). Ukraine Campaign Delivers Defacement and Wipers, in Continued Escalation. Retrieved March 14, 2022.](https://blog.talosintelligence.com/2022/01/ukraine-campaign-delivers-defacement.html)
- [Nart Villeneuve, Randi Eitzman, Sandor Nemes & Tyler Dean, Google Cloud. (2017, October 5). Significant FormBook Distribution Campaigns Impacting the U.S. and South Korea. Retrieved March 11, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)

---

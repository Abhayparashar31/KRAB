# Service Stop

## Description

Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services or processes can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment. [1] [2]

Adversaries may accomplish this by disabling individual services of high importance to an organization, such as MSExchangeIS , which will make Exchange content inaccessible. [2] In some cases, adversaries may stop or disable many or all services to render systems unusable. [1] Services or processes may not allow for modification of their data stores while running. Adversaries may stop services or processes in order to conduct Data Destruction or Data Encrypted for Impact on the data stores of services like Exchange and SQL Server, or on virtual machines hosted on ESXi infrastructure. [3] [4]

Threat actors may also disable or stop service in cloud environments. For example, by leveraging the DisableAPIServiceAccess API in AWS, a threat actor may prevent the service from creating service-linked roles on new accounts in the AWS Organization. [5] [6]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1194 | Akira _v2 | Akira _v2 can stop running virtual machines. [7] [8] [9] |
| S0640 | Avaddon | Avaddon looks for and attempts to stop database processes. [10] |
| S1053 | AvosLocker | AvosLocker has terminated specific processes before encryption. [11] |
| S0638 | Babuk | Babuk can stop specific services related to backups. [12] [13] [14] |
| S1181 | BlackByte 2.0 Ransomware | BlackByte 2.0 Ransomware can terminate running services. [15] |
| S1068 | BlackCat | BlackCat has the ability to stop VM services on compromised networks. [16] [17] |
| S9015 | BRICKSTORM | BRICKSTORM has terminated an existing process to ensure that its own new process can execute. [18] |
| S1096 | Cheerscrypt | Cheerscrypt has the ability to terminate VM processes on compromised hosts through execution of esxcli vm process kill . [19] |
| S0611 | Clop | Clop can kill several processes and services related to backups and security solutions. [20] [21] |
| S0575 | Conti | Conti can stop up to 146 Windows services related to security, backup, database, and email solutions through the use of net stop . [22] |
| S0625 | Cuba | Cuba has a hardcoded list of services and processes to terminate. [23] |
| S0659 | Diavol | Diavol will terminate services using the Service Control Manager (SCM) API. [24] |
| S9013 | DRYHOOK | DRYHOOK has terminated all instances of the cgi-server process before activating the modified DSAuth.pm file. [25] |
| S0605 | EKANS | EKANS stops database, data backup solution, antivirus, and ICS-related processes. [26] [27] [28] |
| S1247 | Embargo | Embargo has terminated active processes and services based on a hardcoded list using the CloseServiceHandle() function. [29] Embargo has also leveraged MS4Killer to terminate processes contained in an embedded list of security software process names that were XOR-encrypted. [30] |
| S1211 | Hannotog | Hannotog can stop Windows services. [31] |
| S0697 | HermeticWiper | HermeticWiper has the ability to stop the Volume Shadow Copy service. [32] |
| S0431 | HotCroissant | HotCroissant has the ability to stop services on the infected host. [33] |
| S1139 | INC Ransomware | INC Ransomware can issue a command to kill a process on compromised hosts. [34] |
| G0119 | Indrik Spider | Indrik Spider has used PsExec to stop services prior to the execution of ransomware. [35] |
| S0604 | Industroyer | Industroyer ’s data wiper module writes zeros into the registry keys in SYSTEM\CurrentControlSet\Services to render a system inoperable. [36] |
| S1245 | InvisibleFerret | InvisibleFerret has terminated Chrome and Brave browsers using the taskkill command on Windows and the killall command on other systems such as Linux and macOS. [37] InvisibleFerret has also utilized it’s ssh_kill command to terminate Chrome and Brave browser processes. [38] |
| S0607 | KillDisk | KillDisk terminates various processes to get the user to reboot the victim machine. [39] |
| G0094 | Kimsuky | Kimsuky has disabled actively running virtual environments using the KillMe function to include VMware, Microsoft Hypervisors, and VirtualBox. [40] |
| G1004 | LAPSUS$ | LAPSUS$ has shut down virtual machines from within a victim's on-premise VMware ESXi infrastructure. [41] |
| G0032 | Lazarus Group | Lazarus Group has stopped the MSExchangeIS service to render Exchange contents inaccessible to users. [42] |
| S1199 | LockBit 2.0 | LockBit 2.0 can automatically terminate processes that may interfere with the encryption or file extraction processes. [43] |
| S1202 | LockBit 3.0 | LockBit 3.0 can terminate targeted processes and services related to security, backup, database management, and other applications that could stop or interfere with encryption. [44] [45] [46] [47] |
| S0582 | LookBack | LookBack can kill processes and delete services. [48] |
| S0449 | Maze | Maze has stopped SQL services to ensure it can encrypt any database. [49] |
| G1051 | Medusa Group | Medusa Group has terminated services related to backups, security, databases, communication, filesharing and websites. [50] [51] [52] |
| S1244 | Medusa Ransomware | Medusa Ransomware has the capability to terminate services related to backups, security, databases, communication, filesharing and websites. [50] [51] [52] Medusa Ransomware has also utilized the taskkill /F /IM <process> /T command to stop targeted processes and net stop <process> command to stop designated services. [51] [52] |
| S0576 | MegaCortex | MegaCortex can stop and disable services on the system. [53] |
| S1191 | Megazord | Megazord has the ability to terminate a list of services and processes. [9] |
| S0688 | Meteor | Meteor can disconnect all network adapters on a compromised host using powershell -Command "Get-WmiObject -class Win32_NetworkAdapter | ForEach { If ($.NetEnabled) { $.Disable() } }" > NUL . [54] |
| S0457 | Netwalker | Netwalker can terminate system processes and services, some of which relate to backup software. [55] |
| S0365 | Olympic Destroyer | Olympic Destroyer uses the API call ChangeServiceConfigW to disable all services on the affected system. [1] |
| S0556 | Pay2Key | Pay2Key can stop the MS SQL service at the end of the encryption process to release files locked by the service. [56] |
| S9014 | PHASEJAM | PHASEJAM has disabled the cgi-server process on Ivanti Connect Secure appliances. [25] |
| S1058 | Prestige | Prestige has attempted to stop the MSSQL Windows service to ensure successful encryption using C:\Windows\System32\net.exe stop MSSQLSERVER . [57] |
| S0583 | Pysa | Pysa can stop services and processes. [58] |
| S1242 | Qilin | Qilin can terminate specific services on compromised hosts. [59] [60] [61] [62] |
| S0481 | Ragnar Locker | Ragnar Locker has attempted to stop services associated with business applications and databases to release the lock on files used by these applications so they may be encrypted. [63] |
| S1212 | RansomHub | RansomHub has the ability to terminate specified services. [64] |
| S0496 | REvil | REvil has the capability to stop services and kill processes. [65] [66] |
| S1150 | ROADSWEEP | ROADSWEEP can disable critical services and processes. [67] |
| S0400 | RobbinHood | RobbinHood stops 181 Windows services on the system before beginning the encryption process. [68] |
| S1073 | Royal | Royal can use RmShutDown to kill applications and services using the resources that are targeted for encryption. [69] |
| S0446 | Ryuk | Ryuk has called kill.bat for stopping services, disabling services and killing processes. [70] |
| G0034 | Sandworm Team | Sandworm Team attempts to stop the MSSQL Windows service to ensure successful encryption of locked files. [57] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA has the capability to stop processes and services. [71] |
| S1217 | VIRTUALPITA | VIRTUALPITA can start and stop the vmsyslogd service. [72] |
| S0366 | WannaCry | WannaCry attempts to kill processes associated with Exchange, Microsoft SQL Server, and MySQL to make it possible to encrypt their data stores. [73] [3] |
| G0102 | Wizard Spider | Wizard Spider has used taskkill.exe and net.exe to stop backup, catalog, cloud, and other services prior to network encryption. [74] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1030 | Network Segmentation | Operate intrusion detection, analysis, and response systems on a separate network from the production environment to lessen the chances that an adversary can see and interfere with critical response functions. |
| M1060 | Out-of-Band Communications Channel | Develop and enforce security policies that include the use of out-of-band communication channels for critical communications during a security incident. [75] |
| M1022 | Restrict File and Directory Permissions | Ensure proper process and file permissions are in place to inhibit adversaries from disabling or interfering with critical services. |
| M1024 | Restrict Registry Permissions | Ensure proper registry permissions are in place to inhibit adversaries from disabling or interfering with critical services. |
| M1018 | User Account Management | Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service configurations. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0021 | Behavioral Detection for Service Stop across Platforms | AN0061 | Adversary disables or stops critical services (e.g., Exchange, SQL, AV, endpoint monitoring) using native utilities or API calls, often preceding destructive actions (T1485, T1486). Behavioral chain: Elevated execution context + stop-service or sc.exe or ChangeServiceConfigW + terminated or disabled service + possible follow-up file manipulation. |
| AN0062 | Adversary executes systemctl or service stop targeting high-value services (e.g., mysql, sshd), possibly followed by rm or shred against data stores. Behavioral chain: sudo/su usage + stop command + /var/log/messages or syslog entries + file access/delete. |  |  |
| AN0063 | Use of launchctl to stop services or kill critical background processes (e.g., securityd, com.apple.*), typically followed by command-line tools like rm or diskutil. Behavioral chain: Terminal or remote shell + launchctl bootout/disable + process termination + follow-on modification. |  |  |
| AN0064 | Attacker disables VM-related services or stops VMs forcibly to target vmdk or logs. Behavioral chain: esxcli or vim-cmd stop + audit log showing user privilege use + datastore file manipulation. |  |  |

---

## References

- [Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Counter Threat Unit Research Team. (2017, May 18). WCry Ransomware Analysis. Retrieved March 26, 2019.](https://www.secureworks.com/research/wcry-ransomware-analysis)
- [Michael Dawson. (2021, August 30). Hypervisor Jackpotting, Part 2: eCrime Actors Increase Targeting of ESXi Servers with Ransomware. Retrieved March 26, 2025.](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
- [Martin McCloskey. (2025, May 13). Tales from the cloud trenches: The Attacker doth persist too much, methinks. Retrieved May 22, 2025.](https://securitylabs.datadoghq.com/articles/tales-from-the-cloud-trenches-the-attacker-doth-persist-too-much/)
- [AWS. (n.d.). DisableAWSServiceAccess. Retrieved May 22, 2025.](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)
- [CISA et al. (2024, April 18). #StopRansomware: Akira Ransomware. Retrieved December 10, 2024.](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)
- [Nutland, J. and Szeliga, M. (2024, October 21). Akira ransomware continues to evolve. Retrieved December 10, 2024.](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
- [Zemah, Y. (2024, December 2). Threat Assessment: Howling Scorpius (Akira Ransomware). Retrieved January 8, 2025.](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)
- [Yuste, J. Pastrana, S. (2021, February 9). Avaddon ransomware: an in-depth analysis and decryption of infected systems. Retrieved August 19, 2021.](https://arxiv.org/pdf/2102.04796.pdf)
- [Hasherezade. (2021, July 23). AvosLocker enters the ransomware scene, asks for partners. Retrieved January 11, 2023.](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
- [Sogeti. (2021, March). Babuk Ransomware. Retrieved August 11, 2021.](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
- [Mundo, A. et al. (2021, February). Technical Analysis of Babuk Ransomware. Retrieved August 11, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
- [Centero, R. et al. (2021, February 5). New in Ransomware: Seth-Locker, Babuk Locker, Maoloa, TeslaCrypt, and CobraLocker. Retrieved August 11, 2021.](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [Brandt, Andrew. (2022, July 14). BlackCat ransomware attacks not merely a byproduct of bad luck. Retrieved December 20, 2022.](https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/)
- [DHS/CISA. (2026, February 11). AR25-338A: BRICKSTORM Backdoor. Retrieved April 16, 2026.](https://www.cisa.gov/news-events/analysis-reports/ar25-338a)
- [Dela Cruz, A. et al. (2022, May 25). New Linux-Based Ransomware Cheerscrypt Targeting ESXi Devices Linked to Leaked Babuk Source Code. Retrieved December 19, 2023.](https://www.trendmicro.com/en_se/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html)
- [Santos, D. (2021, April 13). Threat Assessment: Clop Ransomware. Retrieved July 30, 2021.](https://unit42.paloaltonetworks.com/clop-ransomware/)
- [Mundo, A. (2019, August 1). Clop Ransomware. Retrieved May 10, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
- [Baskin, B. (2020, July 8). TAU Threat Discovery: Conti Ransomware. Retrieved February 17, 2021.](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [John Wolfram, Josh Murchie, Matt Lin, Daniel Ainsworth, Robert Wallace, Dimiter Andonov, Dhanesh Kizhakkinan, Jacob Thompson. (2025, January 8). Ivanti Connect Secure VPN Targeted in New Zero-Day Exploitation. Retrieved April 14, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
- [Dragos. (2020, February 3). EKANS Ransomware and ICS Operations. Retrieved February 9, 2021.](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)
- [Zafra, D., et al. (2020, February 24). Ransomware Against the Machine: How Adversaries are Learning to Disrupt Industrial Production by Targeting IT and OT. Retrieved March 2, 2021.](https://www.fireeye.com/blog/threat-research/2020/02/ransomware-against-machine-learning-to-disrupt-industrial-production.html)
- [Hinchliffe, A. Santos, D. (2020, June 26). Threat Assessment: EKANS Ransomware. Retrieved February 9, 2021.](https://unit42.paloaltonetworks.com/threat-assessment-ekans-ransomware/)
- [Cyble. (2024, May 24). The Rust Revolution: New Embargo Ransomware Steps In. Retrieved October 19, 2025.](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
- [Jan Holman, Tomas Zvara. (2024, October 23). Embargo ransomware: Rock’n’Rust. Retrieved October 19, 2025.](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
- [Symntec Threat Hunter Team. (2022, November 12). Billbug: State-sponsored Actor Targets Cert Authority, Government Agencies in Multiple Asian Countries. Retrieved March 15, 2025.](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
- [Dani, M. (2022, March 1). Ukrainian Targets Hit by HermeticWiper, New Datawiper Malware. Retrieved March 25, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
- [Knight, S.. (2020, April 16). VMware Carbon Black TAU Threat Analysis: The Evolution of Lazarus. Retrieved May 1, 2020.](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [Symantec Threat Intelligence. (2020, June 25). WastedLocker: Symantec Identifies Wave of Attacks Against U.S. Organizations. Retrieved May 20, 2021.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)
- [Dragos Inc.. (2017, June 13). CRASHOVERRIDE Analysis of the Threat to Electric Grid Operations. Retrieved December 18, 2020.](https://dragos.com/blog/crashoverride/CrashOverride-01.pdf)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Gilbert Sison, Rheniel Ramos, Jay Yaneza, Alfredo Oliveira. (2018, January 15). KillDisk Variant Hits Latin American Financial Groups. Retrieved January 12, 2021.](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)
- [Varadharajan Krishnasamy, Aditya K Sood. (2025, July 29). From Reconnaissance to Control: The Operational Blueprint of Kimsuky APT for Cyber Espionage. Retrieved April 18, 2026.](https://www.aryaka.com/docs/reports/aryaka-kimsuky-apt-operational-blueprint.pdf)
- [Brown, D., et al. (2022, April 28). LAPSUS$: Recent techniques, tactics and procedures. Retrieved December 22, 2022.](https://research.nccgroup.com/2022/04/28/lapsus-recent-techniques-tactics-and-procedures/)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved November 17, 2024.](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)
- [SentinelOne. (n.d.). LockBit 2.0: In-Depth Analysis, Detection, Mitigation, and Removal. Retrieved January 24, 2025.](https://www.sentinelone.com/anthology/lockbit-2-0/)
- [CISA et al. (2023, June 14). UNDERSTANDING RANSOMWARE THREAT ACTORS: LOCKBIT. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)
- [Walter, J. (2022, July 21). LockBit 3.0 Update | Unpicking the Ransomware’s Latest Anti-Analysis and Evasion Techniques. Retrieved February 5, 2025.](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [INCIBE-CERT. (2024, March 14). LockBit: response and recovery actions. Retrieved February 5, 2025.](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
- [Raggi, M. Schwarz, D.. (2019, August 1). LookBack Malware Targets the United States Utilities Sector with Phishing Attacks Impersonating Engineering Licensing Boards. Retrieved February 25, 2021.](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
- [Brandt, A., Mackenzie, P.. (2020, September 17). Maze Attackers Adopt Ragnar Locker Virtual Machine Technique. Retrieved October 9, 2020.](https://news.sophos.com/en-us/2020/09/17/maze-attackers-adopt-ragnar-locker-virtual-machine-technique/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Del Fierro, C. Kessem, L.. (2020, January 8). From Mega to Giga: Cross-Version Comparison of Top MegaCortex Modifications. Retrieved February 15, 2021.](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
- [Check Point Research Team. (2021, August 14). Indra - Hackers Behind Recent Attacks on Iran. Retrieved February 17, 2022.](https://research.checkpoint.com/2021/indra-hackers-behind-recent-attacks-on-iran/)
- [Victor, K.. (2020, May 18). Netwalker Fileless Ransomware Injected via Reflective Loading . Retrieved May 26, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
- [Check Point. (2020, November 6). Ransomware Alert: Pay2Key. Retrieved January 4, 2021.](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)
- [MSTIC. (2022, October 14). New “Prestige” ransomware impacts organizations in Ukraine and Poland. Retrieved January 19, 2023.](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
- [CERT-FR. (2020, April 1). ATTACKS INVOLVING THE MESPINOZA/PYSA RANSOMWARE. Retrieved March 1, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
- [Magdy, S. et al. (2022, August 25). New Golang Ransomware Agenda Customizes Attacks. Retrieved September 26, 2025.](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
- [Halcyon RISE Team. (2024, October 24). New Qilin.B Ransomware Variant Boasts Enhanced Encryption and Defense Evasion. Retrieved September 26, 2025.](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
- [Health Sector Cybersecurity Coordination Center. (2024, June 18). Qilin, aka Agenda Ransomware. Retrieved September 26, 2025.](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [SophosLabs. (2020, May 21). Ragnar Locker ransomware deploys virtual machine to dodge security. Retrieved June 29, 2020.](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
- [Alfano, V. et al. (2025, February 12). RansomHub Never Sleeps Episode 1: The evolution of modern ransomware. Retrieved March 17, 2025.](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
- [Intel 471 Malware Intelligence team. (2020, March 31). REvil Ransomware-as-a-Service – An analysis of a ransomware affiliate operation. Retrieved August 4, 2020.](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [Lee, S. (2019, May 17). CB TAU Threat Intelligence Notification: RobbinHood Ransomware Stops 181 Windows Services Before Encryption. Retrieved July 29, 2019.](https://www.carbonblack.com/2019/05/17/cb-tau-threat-intelligence-notification-robbinhood-ransomware-stops-181-windows-services-before-encryption/)
- [Cybereason Global SOC and Cybereason Security Research Teams. (2022, December 14). Royal Rumble: Analysis of Royal Ransomware. Retrieved March 30, 2023.](https://www.cybereason.com/blog/royal-ransomware-analysis)
- [Hanel, A. (2019, January 10). Big Game Hunting with Ryuk: Another Lucrative Targeted Ransomware. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [Alexander Marvi, Jeremy Koppen, Tufail Ahmed, and Jonathan Lepore. (2022, September 29). Bad VIB(E)s Part One: Investigating Novel Malware Persistence Within ESXi Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
- [Berry, A., Homan, J., and Eitzman, R. (2017, May 23). WannaCry Malware Profile. Retrieved March 15, 2019.](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
- [The DFIR Report. (2020, October 8). Ryuk’s Return. Retrieved October 9, 2020.](https://thedfirreport.com/2020/10/08/ryuks-return/)
- [Tyler Hudak. (2022, December 29). To OOB, or Not to OOB?: Why Out-of-Band Communications are Essential for Incident Response. Retrieved August 30, 2024.](https://trustedsec.com/blog/to-oob-or-not-to-oob-why-out-of-band-communications-are-essential-for-incident-response)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Lapsus$]] [related_actor:: [[Lapsus$]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025 Multi-Industry Hypervisor and Retail Extortion Campaign]] [related_campaign:: [[2025 Multi-Industry Hypervisor and Retail Extortion Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[MGM Resorts and Caesars Entertainment Extortion Campaign]] [related_campaign:: [[MGM Resorts and Caesars Entertainment Extortion Campaign]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[RansomHub]] [related_actor:: [[RansomHub]]]

# Access Token Manipulation

## Description

Adversaries may modify access tokens to operate under a different user or system security context to perform actions and bypass access controls. Windows uses access tokens to determine the ownership of a running process. A user can manipulate access tokens to make a running process appear as though it is the child of a different process or belongs to someone other than the user that started the process. When this occurs, the process also takes on the security context associated with the new token.

An adversary can use built-in Windows API functions to copy access tokens from existing processes; this is known as token stealing. These token can then be applied to an existing process (i.e. Token Impersonation/Theft ) or used to spawn a new process (i.e. Create Process with Token ). An adversary must already be in a privileged user context (i.e. administrator) to steal a token. However, adversaries commonly use token stealing to elevate their security context from the administrator level to the SYSTEM level. An adversary can then use a token to authenticate to a remote system as the account for that token if the account has appropriate permissions on the remote system. [1]

Any standard user can use the runas command, and the Windows API functions, to create impersonation tokens; it does not require access to an administrator account. There are also other mechanisms, such as Active Directory fields, that can be used to modify access tokens.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0622 | AppleSeed | AppleSeed can gain system level privilege by passing SeDebugPrivilege to the AdjustTokenPrivilege API. [2] |
| S1068 | BlackCat | BlackCat has the ability modify access tokens. [3] [4] |
| G0108 | Blue Mockingbird | Blue Mockingbird has used JuicyPotato to abuse the SeImpersonate token privilege to escalate from web application pool accounts to NT Authority\SYSTEM. [5] |
| C0017 | C0017 | During C0017 , APT41 used a ConfuserEx obfuscated BADPOTATO exploit to abuse named-pipe impersonation for local NT AUTHORITY\SYSTEM privilege escalation. [6] |
| S0625 | Cuba | Cuba has used SeDebugPrivilege and AdjustTokenPrivileges to elevate privileges. [7] |
| S0038 | Duqu | Duqu examines running system processes for tokens that have specific system privileges. If it finds one, it will copy the token and store it for later use. Eventually it will start new processes with the stored token attached. It can also steal tokens to acquire administrative privileges. [8] |
| S0363 | Empire | Empire can use PowerSploit 's Invoke-TokenManipulation to manipulate access tokens. [9] |
| G0037 | FIN6 | FIN6 has used has used Metasploit’s named-pipe impersonation technique to escalate privileges. [10] |
| S0666 | Gelsemium | Gelsemium can use token manipulation to bypass UAC on Windows7 systems. [11] |
| S0697 | HermeticWiper | HermeticWiper can use AdjustTokenPrivileges to grant itself privileges for debugging with SeDebugPrivilege , creating backups with SeBackupPrivilege , loading drivers with SeLoadDriverPrivilege , and shutting down a local system with SeShutdownPrivilege . [12] [13] |
| S0203 | Hydraq | Hydraq creates a backdoor through which remote attackers can adjust token privileges. [14] |
| S0607 | KillDisk | KillDisk has attempted to get the access token of a process by calling OpenProcessToken . If KillDisk gets the access token, then it attempt to modify the token privileges with AdjustTokenPrivileges . [15] |
| G0030 | Lotus Blossom | Lotus Blossom has retrieved process tokens for processes to adjust the privileges of the launch process or other items. [16] |
| S1060 | Mafalda | Mafalda can use AdjustTokenPrivileges() to elevate privileges. [17] |
| S0576 | MegaCortex | MegaCortex can enable SeDebugPrivilege and adjust token privileges. [18] |
| S0378 | PoshC2 | PoshC2 can use Invoke-TokenManipulation for manipulating tokens. [19] |
| S0194 | PowerSploit | PowerSploit 's Invoke-TokenManipulation Exfiltration module can be used to manipulate tokens. [20] [21] |
| S1242 | Qilin | Qilin can use an embedded Mimikatz module for token manipulation. [22] |
| S0446 | Ryuk | Ryuk has attempted to adjust its token privileges to have the SeDebugPrivilege . [23] |
| S1210 | Sagerunex | Sagerunex finds the explorer.exe process after execution and uses it to change the token of its executing thread. [24] |
| S0633 | Sliver | Sliver has the ability to manipulate user tokens on targeted Windows systems. [25] [26] |
| S0058 | SslMM | SslMM contains a feature to manipulate process privileges and tokens. [27] |
| S0562 | SUNSPOT | SUNSPOT modified its security token to grants itself debugging privileges by adding SeDebugPrivilege . [28] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1026 | Privileged Account Management | Limit permissions so that users and user groups cannot create tokens. This setting should be defined for the local system account only. GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Create a token object. [29] Also define who can create a process level token to only the local and network service through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Replace a process level token. [30] Administrators should log in as a standard user but run their tools with administrator privileges using the built-in access token manipulation command runas . [31] |
| M1018 | User Account Management | An adversary must already have administrator level access on the local system to make full use of this technique; be sure to restrict users and accounts to the least privileges they require. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0283 | Behavior-chain detection for T1134 Access Token Manipulation on Windows | AN0786 | Detection of suspicious token manipulation chains: use of token-related APIs (e.g., LogonUser, DuplicateTokenEx) or commands (runas) → spawning of a new process under a different security context (e.g., SYSTEM) → mismatched parent-child process lineage or anomalies in Event Tracing for Windows (ETW) token/PPID data → abnormal lateral or privilege escalation activity. |

---

## References

- [netbiosX. (2017, April 3). Token Manipulation. Retrieved April 21, 2017.](https://pentestlab.blog/2017/04/03/token-manipulation/)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [Brandt, Andrew. (2022, July 14). BlackCat ransomware attacks not merely a byproduct of bad luck. Retrieved December 20, 2022.](https://news.sophos.com/en-us/2022/07/14/blackcat-ransomware-attacks-not-merely-a-byproduct-of-bad-luck/)
- [Lambert, T. (2020, May 7). Introducing Blue Mockingbird. Retrieved May 26, 2020.](https://redcanary.com/blog/blue-mockingbird-cryptominer/)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [Kaspersky Lab. (2015, June 11). The Duqu 2.0. Retrieved April 21, 2017.](https://web.archive.org/web/20150906233433/https://securelist.com/files/2015/06/The_Mystery_of_Duqu_2_0_a_sophisticated_cyberespionage_actor_returns.pdf)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Dani, M. (2022, March 1). Ukrainian Targets Hit by HermeticWiper, New Datawiper Malware. Retrieved March 25, 2022.](https://blog.qualys.com/vulnerabilities-threat-research/2022/03/01/ukrainian-targets-hit-by-hermeticwiper-new-datawiper-malware)
- [Thomas, W. et al. (2022, February 25). CrowdStrike Falcon Protects from New Wiper Malware Used in Ukraine Cyberattacks. Retrieved March 25, 2022.](https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/)
- [Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
- [Gilbert Sison, Rheniel Ramos, Jay Yaneza, Alfredo Oliveira. (2018, January 15). KillDisk Variant Hits Latin American Financial Groups. Retrieved January 12, 2021.](https://www.trendmicro.com/en_us/research/18/a/new-killdisk-variant-hits-financial-organizations-in-latin-america.html)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [SentinelLabs. (2022, September 22). Metador Technical Appendix. Retrieved April 4, 2023.](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
- [Del Fierro, C. Kessem, L.. (2020, January 8). From Mega to Giga: Cross-Version Comparison of Top MegaCortex Modifications. Retrieved February 15, 2021.](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.](https://github.com/PowerShellMafia/PowerSploit)
- [PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.](http://powersploit.readthedocs.io)
- [Hacioglu, S. (2025, March 10). Qilin Ransomware: Exposing the TTPs Behind One of the Most Active Ransomware Campaigns of 2024. Retrieved September 26, 2025.](https://www.picussecurity.com/resource/blog/qilin-ransomware)
- [Hanel, A. (2019, January 10). Big Game Hunting with Ryuk: Another Lucrative Targeted Ransomware. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
- [Symntec Threat Hunter Team. (2022, November 12). Billbug: State-sponsored Actor Targets Cert Authority, Government Agencies in Multiple Asian Countries. Retrieved March 15, 2025.](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
- [Kervella, R. (2019, August 4). Cross-platform General Purpose Implant Framework Written in Golang. Retrieved July 30, 2021.](https://labs.bishopfox.com/tech-blog/sliver)
- [BishopFox. (n.d.). Sliver. Retrieved September 15, 2021.](https://github.com/BishopFox/sliver/)
- [Baumgartner, K., Golovkin, M.. (2015, May). The MsnMM Campaigns: The Earliest Naikon APT Campaigns. Retrieved April 10, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
- [CrowdStrike Intelligence Team. (2021, January 11). SUNSPOT: An Implant in the Build Process. Retrieved January 11, 2021.](https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/)
- [Brower, N., Lich, B. (2017, April 19). Create a token object. Retrieved December 19, 2017.](https://docs.microsoft.com/windows/device-security/security-policy-settings/create-a-token-object)
- [Brower, N., Lich, B. (2017, April 19). Replace a process level token. Retrieved December 19, 2017.](https://docs.microsoft.com/windows/device-security/security-policy-settings/replace-a-process-level-token)
- [Microsoft TechNet. (n.d.). Runas. Retrieved April 21, 2017.](https://technet.microsoft.com/en-us/library/bb490994.aspx)

---

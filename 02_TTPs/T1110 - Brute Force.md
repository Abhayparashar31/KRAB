# Brute Force

## Description

Adversaries may use brute force techniques to gain access to accounts when passwords are unknown or when password hashes are obtained. [1] Without knowledge of the password for an account or set of accounts, an adversary may systematically guess the password using a repetitive or iterative mechanism. [2] Brute forcing passwords can take place via interaction with a service that will check the validity of those credentials or offline against previously acquired credential data, such as password hashes.

Brute forcing credentials may take place at various points during a breach. For example, adversaries may attempt to brute force access to Valid Accounts within a victim environment leveraging knowledge gathered from other post-compromise behaviors such as OS Credential Dumping , Account Discovery , or Password Policy Discovery . Adversaries may also combine brute forcing activity with behaviors such as External Remote Services as part of Initial Access.

If an adversary guesses the correct password but fails to login to a compromised account due to location-based conditional access policies, they may change their infrastructure until they match the victim’s location and therefore bypass those policies. [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0025 | 2016 Ukraine Electric Power Attack | During the 2016 Ukraine Electric Power Attack , Sandworm Team used a script to attempt RPC authentication against a number of hosts. [2] |
| G1030 | Agrius | Agrius engaged in various brute forcing activities via SMB in victim environments. [4] |
| G0007 | APT28 | APT28 can perform brute force attacks to obtain credentials. [5] [1] [6] |
| G0082 | APT38 | APT38 has used brute force techniques to attempt account access when passwords are unknown or when password hashes are unavailable. [7] |
| G0087 | APT39 | APT39 has used Ncrack to reveal credentials. [8] |
| G0096 | APT41 | APT41 performed password brute-force attacks on the local admin account. [9] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell has a module to perform brute force attacks on a system. [10] |
| S0220 | Chaos | Chaos conducts brute force attacks against SSH services to gain initial access. [11] |
| S0488 | CrackMapExec | CrackMapExec can brute force supplied user credentials across a network range. [12] |
| G0105 | DarkVishnya | DarkVishnya used brute-force attack to obtain login data. [13] |
| G0035 | Dragonfly | Dragonfly has attempted to brute force credentials to gain access. [14] |
| G1003 | Ember Bear | Ember Bear used the su-bruteforce tool to brute force specific users using the su command. [15] |
| G0053 | FIN5 | FIN5 has has used the tool GET2 Penetrator to look for remote login and hard-coded credentials. [16] [17] |
| G0117 | Fox Kitten | Fox Kitten has brute forced RDP credentials. [18] |
| G1001 | HEXANE | HEXANE has used brute force attacks to compromise valid credentials. [19] |
| S0599 | Kinsing | Kinsing has attempted to brute force hosts over SSH. [20] |
| G0049 | OilRig | OilRig has used brute force techniques to obtain credentials. [21] [22] |
| C0022 | Operation Dream Job | During Operation Dream Job , Lazarus Group performed brute force attacks against administrator accounts. [23] |
| S0378 | PoshC2 | PoshC2 has modules for brute forcing local administrator and AD user accounts. [24] |
| S0583 | Pysa | Pysa has used brute force attempts against a central management console, as well as some Active Directory accounts. [25] |
| S0650 | QakBot | QakBot can conduct brute force attacks to capture credentials. [26] [27] [28] |
| G1053 | Storm-0501 | Storm-0501 has leveraged brute force attacks to obtain credentials. [29] |
| G0010 | Turla | Turla may attempt to connect to systems within a victim's network using net use commands and a predefined list or collection of passwords. [30] |
| G1055 | VOID MANTICORE | VOID MANTICORE has conducted brute-force attempts against organizational VPN infrastructure. [31] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1036 | Account Use Policies | Set account lockout policies after a certain number of failed login attempts to prevent passwords from being guessed. Too strict a policy may create a denial of service condition and render environments un-usable, with all accounts used in the brute force being locked-out. Use conditional access policies to block logins from non-compliant devices or from outside defined organization IP ranges. [32] Consider blocking risky authentication requests, such as those originating from anonymizing services/proxies. [33] |
| M1032 | Multi-factor Authentication | Use multi-factor authentication. Where possible, also enable multi-factor authentication on externally facing services. |
| M1027 | Password Policies | Refer to NIST guidelines when creating password policies. [34] |
| M1018 | User Account Management | Proactively reset accounts that are known to be part of breached credentials either immediately, or after detecting bruteforce attempts. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0463 | Brute Force Authentication Failures with Multi-Platform Log Correlation | AN1275 | High volume of failed logon attempts followed by a successful one from a suspicious user, host, or timeframe |
| AN1276 | Multiple authentication failures for valid or invalid users followed by success from same IP/user |  |  |
| AN1277 | Password spraying or brute force attempts across user pool within short time intervals |  |  |
| AN1278 | Multiple failed authentications in unified logs (e.g., loginwindow or sshd) |  |  |
| AN1279 | Excessive login attempts followed by success from SaaS apps like O365, Dropbox, etc. |  |  |

---

## References

- [Hacquebord, F., Remorin, L. (2020, December 17). Pawn Storm’s Lack of Sophistication as a Strategy. Retrieved January 13, 2021.](https://www.trendmicro.com/en_us/research/20/l/pawn-storm-lack-of-sophistication-as-a-strategy.html)
- [Joe Slowik. (2018, October 12). Anatomy of an Attack: Detecting and Defeating CRASHOVERRIDE. Retrieved December 18, 2020.](https://www.dragos.com/wp-content/uploads/CRASHOVERRIDE2018.pdf)
- [Hayden Evans. (2024, April 4). Health Care Social Engineering Campaign. Retrieved May 22, 2025.](https://www.reliaquest.com/blog/health-care-social-engineering-campaign/)
- [Or Chechik, Tom Fakterman, Daniel Frank & Assaf Dahan. (2023, November 6). Agonizing Serpens (Aka Agrius) Targeting the Israeli Higher Education and Tech Sectors. Retrieved May 22, 2024.](https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/)
- [Hacquebord, F. (n.d.). Pawn Storm in 2019 A Year of Scanning and Credential Phishing on High-Profile Targets. Retrieved December 29, 2020.](https://documents.trendmicro.com/assets/white_papers/wp-pawn-storm-in-2019.pdf)
- [Burt, T. (2020, September 10). New cyberattacks targeting U.S. elections. Retrieved March 24, 2021.](https://blogs.microsoft.com/on-the-issues/2020/09/10/cyberattacks-us-elections-trump-biden/)
- [DHS/CISA. (2020, August 26). FASTCash 2.0: North Korea's BeagleBoyz Robbing Banks. Retrieved September 29, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa20-239a)
- [Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.](https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Sebastian Feldmann. (2018, February 14). Chaos: a Stolen Backdoor Rising Again. Retrieved March 5, 2018.](http://gosecure.net/2018/02/14/chaos-stolen-backdoor-rising/)
- [byt3bl33d3r. (2018, September 8). SMB: Command Reference. Retrieved July 17, 2020.](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
- [Golovanov, S. (2018, December 6). DarkVishnya: Banks attacked through direct connection to local network. Retrieved May 15, 2020.](https://securelist.com/darkvishnya/89169/)
- [CISA. (2020, December 1). Russian State-Sponsored Advanced Persistent Threat Actor Compromises U.S. Government Targets. Retrieved December 9, 2021.](https://www.cisa.gov/uscert/ncas/alerts/aa20-296a#revisions)
- [US Cybersecurity & Infrastructure Security Agency et al. (2024, September 5). Russian Military Cyber Actors Target U.S. and Global Critical Infrastructure. Retrieved September 6, 2024.](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)
- [Higgins, K. (2015, October 13). Prolific Cybercrime Gang Favors Legit Login Credentials. Retrieved October 4, 2017.](https://www.darkreading.com/analytics/prolific-cybercrime-gang-favors-legit-login-credentials/d/d-id/1322645?)
- [Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.](https://www.youtube.com/watch?v=fevGZs0EQu8)
- [ClearSky. (2020, December 17). Pay2Key Ransomware – A New Campaign by Fox Kitten. Retrieved December 21, 2020.](https://www.clearskysec.com/wp-content/uploads/2020/12/Pay2Kitten.pdf)
- [SecureWorks 2019, August 27 LYCEUM Takes Center Stage in Middle East Campaign Retrieved. 2019/11/19](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)
- [Singer, G. (2020, April 3). Threat Alert: Kinsing Malware Attacks Targeting Container Environments. Retrieved April 1, 2021.](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
- [Davis, S. and Caban, D. (2017, December 19). APT34 - New Targeted Attack in the Middle East. Retrieved December 20, 2017.](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)
- [Kessem, L. (2019, December 4). New Destructive Wiper ZeroCleare Targets Energy Sector in the Middle East. Retrieved September 4, 2024.](https://securityintelligence.com/posts/new-destructive-wiper-zerocleare-targets-energy-sector-in-the-middle-east/)
- [Breitenbacher, D and Osis, K. (2020, June 17). OPERATION IN(TER)CEPTION: Targeted Attacks Against European Aerospace and Military Companies. Retrieved December 20, 2021.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_Operation_Interception.pdf)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [CERT-FR. (2020, April 1). ATTACKS INVOLVING THE MESPINOZA/PYSA RANSOMWARE. Retrieved March 1, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
- [Sette, N. et al. (2020, June 4). Qakbot Malware Now Exfiltrating Emails for Sophisticated Thread Hijacking Attacks. Retrieved September 27, 2021.](https://www.kroll.com/en/insights/publications/cyber/qakbot-malware-exfiltrating-emails-thread-hijacking-attacks)
- [CS. (2020, October 7). Duck Hunting with Falcon Complete: A Fowl Banking Trojan Evolves, Part 2. Retrieved September 27, 2021.](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [Microsoft Threat Intelligence. (2024, September 26). Storm-0501: Ransomware attacks expanding to hybrid cloud environments. Retrieved October 19, 2025.](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [Check Point Research. (2026, March 12). “Handala Hack” – Unveiling Group’s Modus Operandi. Retrieved April 20, 2026.](https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/)
- [Microsoft. (2022, December 14). Conditional Access templates. Retrieved February 21, 2023.](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)
- [Moussa Diallo and Brett Winterford. (2024, April 26). How to Block Anonymizing Services using Okta. Retrieved May 28, 2024.](https://sec.okta.com/blockanonymizers)
- [Grassi, P., et al. (2017, December 1). SP 800-63-3, Digital Identity Guidelines. Retrieved January 16, 2019.](https://pages.nist.gov/800-63-3/sp800-63b.html)

---

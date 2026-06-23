# Valid Accounts

## Description

Adversaries may obtain and abuse credentials of existing accounts as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access, network devices, and remote desktop. [1] Compromised credentials may also grant an adversary increased privilege to specific systems or access to restricted areas of the network. Adversaries may choose not to use malware or tools in conjunction with the legitimate access those credentials provide to make it harder to detect their presence.

In some cases, adversaries may abuse inactive accounts: for example, those belonging to individuals who are no longer part of an organization. Using these accounts may allow the adversary to evade detection, as the original account user will not be present to identify any anomalous activity taking place on their account. [2]

The overlap of permissions for local, domain, and cloud accounts across a network of systems is of concern because the adversary may be able to pivot across accounts and systems to reach a high level of access (i.e., domain or enterprise administrator) to bypass access controls set within the enterprise. [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0028 | 2015 Ukraine Electric Power Attack | During the 2015 Ukraine Electric Power Attack , Sandworm Team used valid accounts on the corporate network to escalate privileges, move laterally, and establish persistence within the corporate network. [4] |
| C0057 | 3CX Supply Chain Attack | During 3CX Supply Chain Attack , AppleJeus has gained access to the 3CX corporate environment through legitimate VPN credentials. [5] |
| G1024 | Akira | Akira uses valid account information to remotely access victim networks, such as VPN credentials. [6] [7] [8] |
| C0062 | Anthropic AI-orchestrated Campaign | During the Anthropic AI-orchestrated Campaign , the adversary used harvested credentials to authenticate against internal APIs, database systems, container registries, and logging infrastructure across targeted networks. [9] |
| G0026 | APT18 | APT18 actors leverage legitimate credentials to log into external remote services. [10] |
| G0007 | APT28 | APT28 has used legitimate credentials to gain initial access, maintain access, and exfiltrate data from a victim network. The group has specifically used credentials stolen through a spearphishing email to login to the DCCC network. The group has also leveraged default manufacturer's passwords to gain initial access to corporate networks via IoT devices such as a VOIP phone, printer, and video decoder. [11] [12] [13] [14] |
| G0016 | APT29 | APT29 has used a compromised account to access an organization's VPN infrastructure. [15] |
| G0064 | APT33 | APT33 has used valid accounts for initial access and privilege escalation. [16] [17] |
| G0087 | APT39 | APT39 has used stolen credentials to compromise Outlook Web Access (OWA). [18] |
| G0096 | APT41 | APT41 used compromised credentials to log on to other systems. [19] [20] |
| G0001 | Axiom | Axiom has used previously compromised administrative accounts to escalate privileges. [21] |
| G1043 | BlackByte | BlackByte has gained access to victim environments through legitimate VPN credentials. [22] |
| C0032 | C0032 | During the C0032 campaign, TEMP.Veles used compromised VPN accounts. [23] |
| G0008 | Carbanak | Carbanak actors used legitimate credentials of banking employees to perform operations that sent them millions of dollars. [24] |
| G0114 | Chimera | Chimera has used a valid account to maintain persistence via scheduled task. [25] |
| G1021 | Cinnamon Tempest | Cinnamon Tempest has used compromised user accounts to deploy payloads and create system services. [26] |
| G0035 | Dragonfly | Dragonfly has compromised user credentials and used valid accounts for operations. [27] [28] [29] |
| S0567 | Dtrack | Dtrack used hard-coded credentials to gain access to a network share. [30] |
| S0038 | Duqu | Adversaries can instruct Duqu to spread laterally by copying itself to shares it has enumerated and for which it has obtained legitimate credentials (via keylogging or other means). The remote host is then infected by using the compromised credentials to schedule a task on remote machines that executes the malware. [31] |
| G0051 | FIN10 | FIN10 has used stolen credentials to connect remotely to victim networks using VPNs protected with only a single factor. [32] |
| G0085 | FIN4 | FIN4 has used legitimate credentials to hijack email communications. [33] [34] |
| G0053 | FIN5 | FIN5 has used legitimate VPN, RDP, Citrix, or VNC credentials to maintain access to a victim environment. [35] [36] [37] |
| G0037 | FIN6 | To move laterally on a victim network, FIN6 has used credentials stolen from various systems on which it gathered usernames and password hashes. [38] [39] [40] |
| G0046 | FIN7 | FIN7 has harvested valid administrative credentials for lateral movement. [41] |
| G0061 | FIN8 | FIN8 has used valid accounts for persistence and lateral movement. [42] |
| G0117 | Fox Kitten | Fox Kitten has used valid credentials with various services during lateral movement. [43] |
| G0093 | GALLIUM | GALLIUM leveraged valid accounts to maintain access to a victim network. [44] |
| C0038 | HomeLand Justice | During HomeLand Justice , threat actors used a compromised Exchange account to search mailboxes and create new Exchange accounts. [45] |
| G1032 | INC Ransom | INC Ransom has used compromised valid accounts for access to victim environments. [46] [47] [48] [49] |
| G0119 | Indrik Spider | Indrik Spider has used valid accounts for initial access and lateral movement. [50] Indrik Spider has also maintained access to the victim environment through the VPN infrastructure. [50] |
| S0604 | Industroyer | Industroyer can use supplied user credentials to execute processes and stop services. [51] |
| G0004 | Ke3chang | Ke3chang has used credential dumpers or stealers to obtain legitimate credentials, which they used to gain access to victim accounts. [52] |
| S0599 | Kinsing | Kinsing has used valid SSH credentials to access remote hosts. [53] |
| G1004 | LAPSUS$ | LAPSUS$ has used compromised credentials and/or session tokens to gain access into a victim's VPN, VDI, RDP, and IAMs. [54] [55] |
| G0032 | Lazarus Group | Lazarus Group has used administrator credentials to gain access to restricted network segments. [56] |
| G0065 | Leviathan | Leviathan has obtained valid accounts to gain initial access. [57] [58] [59] |
| C0049 | Leviathan Australian Intrusions | Leviathan used captured, valid account information to log into victim web applications and appliances during Leviathan Australian Intrusions . [59] |
| S0362 | Linux Rabbit | Linux Rabbit acquires valid SSH accounts through brute force. [60] |
| S9036 | LP-Notes | LP-Notes has used stolen Windows credentials to log in as the users. [61] |
| G1051 | Medusa Group | Medusa Group has utilized compromised legitimate local and domain accounts within the victim environment to facilitate remote access and lateral movement sometimes in combination with PsExec . [62] |
| G0045 | menuPass | menuPass has used valid accounts including shared between Managed Service Providers and clients to move between the two environments. [63] [64] [65] [66] |
| C0002 | Night Dragon | During Night Dragon , threat actors used compromised VPN accounts to gain access to victim systems. [67] |
| G0049 | OilRig | OilRig has used compromised credentials to access other systems on a victim network. [68] [69] [20] [70] |
| C0048 | Operation MidnightEclipse | During Operation MidnightEclipse , threat actors extracted sensitive credentials while moving laterally through compromised networks. [71] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors used valid VPN credentials to gain initial access. [72] |
| G0011 | PittyTiger | PittyTiger attempts to obtain legitimate credentials during operations. [73] |
| G1040 | Play | Play has used valid VPN accounts to achieve initial access. [74] |
| G1005 | POLONIUM | POLONIUM has used valid compromised credentials to gain access to victim environments. [75] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 used legitimate credentials to gain priviliged access to Juniper routers. [76] [77] |
| G0034 | Sandworm Team | Sandworm Team have used previously acquired legitimate credentials prior to attacks. [78] |
| G1015 | Scattered Spider | Scattered Spider has used compromised credentials for initial access. [79] [80] |
| G1041 | Sea Turtle | Sea Turtle used compromised credentials to maintain long-term access to victim environments. [81] |
| S0053 | SeaDuke | Some SeaDuke samples have a module to extract email from Microsoft Exchange servers using compromised credentials. [82] |
| G0091 | Silence | Silence has used compromised credentials to log on to other systems and escalate privileges. [83] |
| G0122 | Silent Librarian | Silent Librarian has used compromised credentials to obtain unauthorized access to online accounts. [84] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 used different compromised credentials for remote access and to move laterally. [85] [86] [87] |
| G1033 | Star Blizzard | Star Blizzard has used stolen credentials to sign into victim email accounts. [88] [89] |
| G0039 | Suckfly | Suckfly used legitimate account credentials that they dumped to navigate the internal victim network as though they were the legitimate account owner. [90] |
| G0027 | Threat Group-3390 | Threat Group-3390 actors obtain legitimate credentials using a variety of methods and use them to further lateral movement on victim networks. [91] |
| G1048 | UNC3886 | UNC3886 has used tools to hijack valid SSH accounts. [92] |
| G1055 | VOID MANTICORE | VOID MANTICORE has leveraged valid accounts to log into VPN infrastructure. [93] VOID MANTICORE has used compromised valid credentials to gain access to management infrastructure and enterprise control systems. [94] VOID MANTICORE has also validated and tested authentication using compromised credentials prior to malicious actions. [93] |
| G1017 | Volt Typhoon | Volt Typhoon relies primarily on valid credentials for persistence. [95] |
| G0102 | Wizard Spider | Wizard Spider has used valid credentials for privileged accounts with the goal of accessing domain controllers. [96] [97] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1036 | Account Use Policies | Use conditional access policies to block logins from non-compliant devices or from outside defined organization IP ranges. [98] |
| M1015 | Active Directory Configuration | Disable legacy authentication, which does not support MFA, and require the use of modern authentication protocols instead. |
| M1013 | Application Developer Guidance | Ensure that applications do not store sensitive data or credentials insecurely. (e.g. plaintext credentials in code, published credentials in repositories, or credentials in public cloud storage). |
| M1032 | Multi-factor Authentication | Implement multi-factor authentication (MFA) across all account types, including default, local, domain, and cloud accounts, to prevent unauthorized access, even if credentials are compromised. MFA provides a critical layer of security by requiring multiple forms of verification beyond just a password. This measure significantly reduces the risk of adversaries abusing valid accounts to gain initial access, escalate privileges, maintain persistence, or evade defenses within your network. |
| M1027 | Password Policies | Applications and appliances that utilize default username and password should be changed immediately after the installation, and before deployment to a production environment. [99] When possible, applications that use SSH keys should be updated periodically and properly secured. Policies should minimize (if not eliminate) reuse of passwords between different user accounts, especially employees using the same credentials for personal accounts that may not be defended by enterprise security resources. |
| M1026 | Privileged Account Management | Audit domain and local accounts as well as their permission levels routinely to look for situations that could allow an adversary to gain wide access by obtaining credentials of a privileged account. [3] [100] These audits should also include if default accounts have been enabled, or if new local accounts are created that have not been authorized. Follow best practices for design and administration of an enterprise network to limit privileged account use across administrative tiers. [101] |
| M1018 | User Account Management | Regularly audit user accounts for activity and deactivate or remove any that are no longer needed. |
| M1017 | User Training | Applications may send push notifications to verify a login as a form of multi-factor authentication (MFA). Train users to only accept valid push notifications and to report suspicious push notifications. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0560 | Detection of Valid Account Abuse Across Platforms | AN1543 | Detection of compromised or misused valid accounts via anomalous logon patterns, abnormal logon types, and inconsistent geographic or time-based activity across Windows endpoints. |
| AN1544 | Detection of valid account misuse through SSH logins, sudo/su abuse, and service account anomalies outside expected patterns. |  |  |
| AN1545 | Detection of interactive and remote logins by service accounts or users at unusual times, with unexpected child process activity. |  |  |
| AN1546 | Detection of valid account abuse in IdP logs via geographic anomalies, impossible travel, risky sign-ins, and multiple MFA attempts or failures. |  |  |
| AN1547 | Detection of containerized service accounts or compromised kubeconfigs being used for cluster access from unexpected nodes or IPs. |  |  |

---

## References

- [Adair, S., Lancaster, T., Volexity Threat Research. (2022, June 15). DriftingCloud: Zero-Day Sophos Firewall Exploitation and an Insidious Breach. Retrieved July 1, 2022.](https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/)
- [Cybersecurity and Infrastructure Security Agency. (2022, March 15). Russian State-Sponsored Cyber Actors Gain Network Access by Exploiting Default Multifactor Authentication Protocols and “PrintNightmare” Vulnerability. Retrieved March 16, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-074a)
- [Microsoft. (2016, April 15). Attractive Accounts for Credential Theft. Retrieved June 3, 2016.](https://technet.microsoft.com/en-us/library/dn535501.aspx)
- [Electricity Information Sharing and Analysis Center; SANS Industrial Control Systems. (2016, March 18). Analysis of the Cyber Attack on the Ukranian Power Grid: Defense Use Case. Retrieved March 27, 2018.](https://nsarchive.gwu.edu/sites/default/files/documents/3891751/SANS-and-Electricity-Information-Sharing-and.pdf)
- [Agathocles Prodromou. (2023, April 20). Security Update Thursday 20 April 2023 – Initial Intrusion Vector Found. Retrieved August 25, 2025.](https://www.3cx.com/blog/news/mandiant-security-update2/)
- [Secureworks. (n.d.). GOLD SAHARA. Retrieved February 20, 2024.](https://www.secureworks.com/research/threat-profiles/gold-sahara)
- [Steven Campbell, Akshay Suthar, & Connor Belfiorre. (2023, July 26). Conti and Akira: Chained Together. Retrieved February 20, 2024.](https://arcticwolf.com/resources/blog/conti-and-akira-chained-together/)
- [Nutland, J. and Szeliga, M. (2024, October 21). Akira ransomware continues to evolve. Retrieved December 10, 2024.](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
- [Anthropic. (2025, November). Disrupting the first reported AI-orchestrated cyber espionage campaign. Retrieved April 20, 2026.](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
- [Adair, S. (2017, February 17). Detecting and Responding to Advanced Threats within Exchange Environments. Retrieved November 17, 2024.](https://web.archive.org/web/20210803040540/https://published-prd.lanyonevents.com/published/rsaus17/sessionsFiles/5009/HTA-F02-Detecting-and-Responding-to-Advanced-Threats-within-Exchange-Environments.pdf)
- [Hacquebord, F.. (2017, April 25). Two Years of Pawn Storm: Examining an Increasingly Relevant Threat. Retrieved May 3, 2017.](https://documents.trendmicro.com/assets/wp/wp-two-years-of-pawn-storm.pdf)
- [Mueller, R. (2018, July 13). Indictment - United States of America vs. VIKTOR BORISOVICH NETYKSHO, et al. Retrieved November 17, 2024.](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)
- [MSRC Team. (2019, August 5). Corporate IoT – a path to intrusion. Retrieved August 16, 2019.](https://msrc-blog.microsoft.com/2019/08/05/corporate-iot-a-path-to-intrusion/)
- [NSA, CISA, FBI, NCSC. (2021, July). Russian GRU Conducting Global Brute Force Campaign to Compromise Enterprise and Cloud Environments. Retrieved July 26, 2021.](https://media.defense.gov/2021/Jul/01/2002753896/-1/-1/1/CSA_GRU_GLOBAL_BRUTE_FORCE_CAMPAIGN_UOO158036-21.PDF)
- [Douglas Bienstock. (2022, August 18). You Can’t Audit Me: APT29 Continues Targeting Microsoft 365. Retrieved February 23, 2023.](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)
- [Davis, S. and Carr, N. (2017, September 21). APT33: New Insights into Iranian Cyber Espionage Group. Retrieved February 15, 2018.](https://www.brighttalk.com/webcast/10703/275683)
- [Ackerman, G., et al. (2018, December 21). OVERRULED: Containing a Potentially Destructive Adversary. Retrieved January 17, 2019.](https://www.fireeye.com/blog/threat-research/2018/12/overruled-containing-a-potentially-destructive-adversary.html)
- [Hawley et al. (2019, January 29). APT39: An Iranian Cyber Espionage Group Focused on Personal Information. Retrieved February 19, 2019.](https://www.fireeye.com/blog/threat-research/2019/01/apt39-iranian-cyber-espionage-group-focused-on-personal-information.html)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [Crowdstrike. (2020, March 2). 2020 Global Threat Report. Retrieved December 11, 2020.](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf)
- [Novetta. (n.d.). Operation SMN: Axiom Threat Actor Group Report. Retrieved November 12, 2014.](https://web.archive.org/web/20230115144216/http://www.novetta.com/wp-content/uploads/2014/11/Executive_Summary-Final_1.pdf)
- [James Nutland, Craig Jackson, Terryn Valikodath, & Brennan Evans. (2024, August 28). BlackByte blends tried-and-true tradecraft with newly disclosed vulnerabilities to support ongoing attacks. Retrieved December 16, 2024.](https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/)
- [Miller, S, et al. (2019, April 10). TRITON Actor TTP Profile, Custom Attack Tools, Detections, and ATT&CK Mapping. Retrieved April 16, 2019.](https://www.fireeye.com/blog/threat-research/2019/04/triton-actor-ttp-profile-custom-attack-tools-detections.html)
- [Kaspersky Lab's Global Research and Analysis Team. (2015, February). CARBANAK APT THE GREAT BANK ROBBERY. Retrieved August 23, 2018.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf)
- [Cycraft. (2020, April 15). APT Group Chimera - APT Operation Skeleton key Targets Taiwan Semiconductor Vendors. Retrieved August 24, 2020..](https://cycraft.com/download/CyCraft-Whitepaper-Chimera_V4.1.pdf)
- [Biderman, O. et al. (2022, October 3). REVEALING EMPEROR DRAGONFLY: NIGHT SKY AND CHEERSCRYPT - A SINGLE RANSOMWARE GROUP. Retrieved December 6, 2023.](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [Slowik, J. (2021, October). THE BAFFLING BERSERK BEAR: A DECADE’S ACTIVITY TARGETING CRITICAL INFRASTRUCTURE. Retrieved December 6, 2021.](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
- [CISA. (2020, December 1). Russian State-Sponsored Advanced Persistent Threat Actor Compromises U.S. Government Targets. Retrieved December 9, 2021.](https://www.cisa.gov/uscert/ncas/alerts/aa20-296a#revisions)
- [Hod Gavriel. (2019, November 21). Dtrack: In-depth analysis of APT on a nuclear power plant. Retrieved January 20, 2021.](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
- [Symantec Security Response. (2011, November). W32.Duqu: The precursor to the next Stuxnet. Retrieved September 17, 2015.](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
- [FireEye iSIGHT Intelligence. (2017, June 16). FIN10: Anatomy of a Cyber Extortion Operation. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/rpt-fin-10-anatomy-of-a-cyber-en.pdf)
- [Vengerik, B. et al.. (2014, December 5). Hacking the Street? FIN4 Likely Playing the Market. Retrieved December 17, 2018.](https://www.mandiant.com/sites/default/files/2021-09/rpt-fin4.pdf)
- [Vengerik, B. & Dennesen, K.. (2014, December 5). Hacking the Street? FIN4 Likely Playing the Market. Retrieved January 15, 2019.](https://www2.fireeye.com/WBNR-14Q4NAMFIN4.html)
- [Scavella, T. and Rifki, A. (2017, July 20). Are you Ready to Respond? (Webinar). Retrieved October 4, 2017.](https://www2.fireeye.com/WBNR-Are-you-ready-to-respond.html)
- [Higgins, K. (2015, October 13). Prolific Cybercrime Gang Favors Legit Login Credentials. Retrieved October 4, 2017.](https://www.darkreading.com/analytics/prolific-cybercrime-gang-favors-legit-login-credentials/d/d-id/1322645?)
- [Bromiley, M. and Lewis, P. (2016, October 7). Attacking the Hospitality and Gaming Industries: Tracking an Attacker Around the World in 7 Years. Retrieved October 6, 2017.](https://www.youtube.com/watch?v=fevGZs0EQu8)
- [FireEye Threat Intelligence. (2016, April). Follow the Money: Dissecting the Operations of the Cyber Crime Group FIN6. Retrieved November 17, 2024.](https://web.archive.org/web/20190807112824/https://www2.fireeye.com/rs/848-DID-242/images/rpt-fin6.pdf)
- [McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)
- [Visa Public. (2019, February). FIN6 Cybercrime Group Expands Threat to eCommerce Merchants. Retrieved September 16, 2019.](https://usa.visa.com/dam/VCOM/global/support-legal/documents/fin6-cybercrime-group-expands-threat-To-ecommerce-merchants.pdf)
- [Loui, E. and Reynolds, J. (2021, August 30). CARBON SPIDER Embraces Big Game Hunting, Part 1. Retrieved September 20, 2021.](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)
- [Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy: New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)
- [CISA. (2020, September 15). Iran-Based Threat Actor Exploits VPN Vulnerabilities. Retrieved December 21, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-259a)
- [Cybereason Nocturnus. (2019, June 25). Operation Soft Cell: A Worldwide Campaign Against Telecommunications Providers. Retrieved July 18, 2019.](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)
- [CISA. (2022, September 23). AA22-264A Iranian State Actors Conduct Cyber Operations Against the Government of Albania. Retrieved August 6, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [Team Huntress. (2023, August 11). Investigating New INC Ransom Group Activity. Retrieved June 5, 2024.](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)
- [SOCRadar. (2024, January 24). Dark Web Profile: INC Ransom. Retrieved June 5, 2024.](https://socradar.io/dark-web-profile-inc-ransom/)
- [Carvey, H. (2024, May 1). LOLBin to INC Ransomware. Retrieved June 5, 2024.](https://www.huntress.com/blog/lolbin-to-inc-ransomware)
- [Mandiant Intelligence. (2022, June 2). To HADES and Back: UNC2165 Shifts to LOCKBIT to Evade Sanctions. Retrieved July 29, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)
- [Anton Cherepanov. (2017, June 12). Win32/Industroyer: A new threat for industrial controls systems. Retrieved December 18, 2020.](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Singer, G. (2020, April 3). Threat Alert: Kinsing Malware Attacks Targeting Container Environments. Retrieved April 1, 2021.](https://blog.aquasec.com/threat-alert-kinsing-malware-container-vulnerability)
- [MSTIC, DART, M365 Defender. (2022, March 24). DEV-0537 Criminal Actor Targeting Organizations for Data Exfiltration and Destruction. Retrieved May 17, 2022.](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)
- [Brown, D., et al. (2022, April 28). LAPSUS$: Recent techniques, tactics and procedures. Retrieved December 22, 2022.](https://research.nccgroup.com/2022/04/28/lapsus-recent-techniques-tactics-and-procedures/)
- [Vyacheslav Kopeytsev and Seongsu Park. (2021, February 25). Lazarus targets defense industry with ThreatNeedle. Retrieved October 27, 2021.](https://securelist.com/lazarus-threatneedle/100803/)
- [CISA. (2021, July 19). (AA21-200A) Joint Cybersecurity Advisory – Tactics, Techniques, and Procedures of Indicted APT40 Actors Associated with China’s MSS Hainan State Security Department. Retrieved August 12, 2021.](https://us-cert.cisa.gov/ncas/alerts/aa21-200a)
- [Accenture iDefense Unit. (2019, March 5). Mudcarp's Focus on Submarine Technologies. Retrieved August 24, 2021.](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
- [CISA et al. (2024, July 8). People’s Republic of China (PRC) Ministry of State Security APT40 Tradecraft in Action. Retrieved February 3, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a)
- [Anomali Labs. (2018, December 6). Pulling Linux Rabbit/Rabbot Malware Out of a Hat. Retrieved March 4, 2019.](https://www.anomali.com/blog/pulling-linux-rabbit-rabbot-malware-out-of-a-hat)
- [ESET Research. (2025, December 2). MuddyWater: Snakes by the riverbank. Retrieved February 17, 2026.](https://www.welivesecurity.com/en/eset-research/muddywater-snakes-riverbank/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper. Retrieved April 5, 2017.](https://web.archive.org/web/20220224041316/https:/www.pwc.co.uk/cyber-security/pdf/cloud-hopper-report-final-v4.pdf)
- [Symantec. (2020, November 17). Japan-Linked Organizations Targeted in Long-Running and Sophisticated Attack Campaign. Retrieved December 17, 2020.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage)
- [US District Court Southern District of New York. (2018, December 17). United States v. Zhu Hua Indictment. Retrieved December 17, 2020.](https://www.justice.gov/opa/page/file/1122671/download)
- [GREAT. (2021, March 30). APT10: sophisticated multi-layered loader Ecipekac discovered in A41APT campaign. Retrieved June 17, 2021.](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
- [McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)
- [Unit42. (2016, May 1). Evasive Serpens Unit 42 Playbook Viewer. Retrieved February 6, 2023.](https://pan-unit42.github.io/playbook_viewer/?pb=evasive-serpens)
- [Davis, S. and Caban, D. (2017, December 19). APT34 - New Targeted Attack in the Middle East. Retrieved December 20, 2017.](https://www.brighttalk.com/webcast/10703/296317/apt34-new-targeted-attack-in-the-middle-east)
- [Kessem, L. (2019, December 4). New Destructive Wiper ZeroCleare Targets Energy Sector in the Middle East. Retrieved September 4, 2024.](https://securityintelligence.com/posts/new-destructive-wiper-zerocleare-targets-energy-sector-in-the-middle-east/)
- [Volexity Threat Research. (2024, April 12). Zero-Day Exploitation of Unauthenticated Remote Code Execution Vulnerability in GlobalProtect (CVE-2024-3400). Retrieved November 20, 2024.](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Bizeul, D., Fontarensky, I., Mouchoux, R., Perigaud, F., Pernet, C. (2014, July 11). Eye of the Tiger. Retrieved September 29, 2015.](https://airbus-cyber-security.com/the-eye-of-the-tiger/)
- [CISA. (2023, December 18). #StopRansomware: Play Ransomware AA23-352A. Retrieved September 24, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)
- [Microsoft. (2022, June 2). Exposing POLONIUM activity and infrastructure targeting Israeli organizations. Retrieved July 1, 2022.](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
- [Lamparski, L. et al. (2025, March 11). Ghost in the Router: China-Nexus Espionage Actor UNC3886 Targets Juniper Routers. Retrieved June 24, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers)
- [Censys Research Team. (2025, March 14). JunOS and RedPenguin. Retrieved June 24, 2025.](https://censys.com/blog/junos-and-redpenguin)
- [US-CERT. (2016, February 25). ICS Alert (IR-ALERT-H-16-056-01) Cyber-Attack Against Ukrainian Critical Infrastructure. Retrieved June 10, 2020.](https://www.us-cert.gov/ics/alerts/IR-ALERT-H-16-056-01)
- [Mandiant Incident Response. (2025, May 6). Defending Against UNC3944: Cybercrime Hardening Guidance from the Frontlines. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)
- [Mandiant Incident Response. (2025, July 23). From Help Desk to Hypervisor: Defending Your VMware vSphere Estate from UNC3944. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)
- [Cisco Talos. (2019, April 17). Sea Turtle: DNS Hijacking Abuses Trust In Core Internet Service. Retrieved November 20, 2024.](https://blog.talosintelligence.com/seaturtle/)
- [Symantec Security Response. (2015, July 13). “Forkmeiamfamous”: Seaduke, latest weapon in the Duke armory. Retrieved July 22, 2015.](http://www.symantec.com/connect/blogs/forkmeiamfamous-seaduke-latest-weapon-duke-armory)
- [Group-IB. (2018, September). Silence: Moving Into the Darkside. Retrieved May 5, 2020.](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)
- [DOJ. (2018, March 23). U.S. v. Rafatnejad et al . Retrieved February 3, 2021.](https://www.justice.gov/usao-sdny/press-release/file/1045781/download)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [NCSC, CISA, FBI, NSA. (2021, May 7). Further TTPs associated with SVR cyber actors. Retrieved July 29, 2021.](https://www.ncsc.gov.uk/files/Advisory-further-TTPs-associated-with-SVR-cyber-actors.pdf)
- [Microsoft Threat Intelligence. (2022, August 15). Disrupting SEABORGIUM’s ongoing phishing operations. Retrieved June 13, 2024.](https://www.microsoft.com/en-us/security/blog/2022/08/15/disrupting-seaborgiums-ongoing-phishing-operations/)
- [CISA, et al. (2023, December 7). Russian FSB Cyber Actor Star Blizzard Continues Worldwide Spear-phishing Campaigns. Retrieved June 13, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-341a)
- [DiMaggio, J. (2016, May 17). Indian organizations targeted in Suckfly attacks. Retrieved August 3, 2016.](http://www.symantec.com/connect/blogs/indian-organizations-targeted-suckfly-attacks)
- [Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)
- [Punsaen Boonyakarn, Shawn Chew, Logeswaran Nadarajan, Mathew Potaczek, Jakub Jozwiak, and Alex Marvi. (2024, June 18). Cloaked and Covert: Uncovering UNC3886 Espionage Operations. Retrieved September 24, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [Check Point Research. (2026, March 12). “Handala Hack” – Unveiling Group’s Modus Operandi. Retrieved April 20, 2026.](https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/)
- [DomainTools Investigations. (2026, April 6). Handala: MOIS Linked Cyber Influence Ecosystem Threat Intelligence Assessment. Retrieved April 20, 2026.](https://dti.domaintools.com/research/handala-mois-linked-cyber-influence-ecosystem-threat-intelligence-assessment)
- [CISA et al.. (2024, February 7). PRC State-Sponsored Actors Compromise and Maintain Persistent Access to U.S. Critical Infrastructure. Retrieved May 15, 2024.](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)
- [John, E. and Carvey, H. (2019, May 30). Unraveling the Spiderweb: Timelining ATT&CK Artifacts Used by GRIM SPIDER. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/timelining-grim-spiders-big-game-hunting-tactics/)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [Microsoft. (2022, December 14). Conditional Access templates. Retrieved February 21, 2023.](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common)
- [US-CERT. (n.d.). Risks of Default Passwords on the Internet. Retrieved April 12, 2019.](https://www.us-cert.gov/ncas/alerts/TA13-175A)
- [Microsoft. (2016, April 16). Implementing Least-Privilege Administrative Models. Retrieved June 3, 2016.](https://technet.microsoft.com/en-us/library/dn487450.aspx)
- [Plett, C., Poggemeyer, L. (12, October 26). Securing Privileged Access Reference Material. Retrieved April 25, 2017.](https://docs.microsoft.com/en-us/windows-server/identity/securing-privileged-access/securing-privileged-access-reference-material#a-nameesaebmaesae-administrative-forest-design-approach)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[ShinyHunters]] [related_actor:: [[ShinyHunters]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Dragonforce]] [related_actor:: [[Dragonforce]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025 Multi-Industry Hypervisor and Retail Extortion Campaign]] [related_campaign:: [[2025 Multi-Industry Hypervisor and Retail Extortion Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025-2026 SaaS and Cloud Exploitation Wave]] [related_campaign:: [[2025-2026 SaaS and Cloud Exploitation Wave]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2026 Oracle PeopleSoft Mass Data Theft Campaign]] [related_campaign:: [[2026 Oracle PeopleSoft Mass Data Theft Campaign]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[RansomHub]] [related_actor:: [[RansomHub]]]
- 🦠 **Tooling Capability Integration:** Executed via malware family [[BlackCat]] [related_malware:: [[BlackCat]]]

# Domain Trust Discovery

## Description

Adversaries may attempt to gather information on domain trust relationships that may be used to identify lateral movement opportunities in Windows multi-domain/forest environments. Domain trusts provide a mechanism for a domain to allow access to resources based on the authentication procedures of another domain. [1] Domain trusts allow the users of the trusted domain to access resources in the trusting domain. The information discovered may help the adversary conduct SID-History Injection , Pass the Ticket , and Kerberoasting . [2] [3] Domain trusts can be enumerated using the DSEnumerateDomainTrusts() Win32 API call, .NET methods, and LDAP. [3] The Windows utility Nltest is known to be used by adversaries to enumerate domain trusts. [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0552 | AdFind | AdFind can gather information about organizational units (OUs) and domain trusts from Active Directory. [5] [6] [7] [8] |
| G1024 | Akira | Akira uses the built-in Nltest utility or tools such as AdFind to enumerate Active Directory trusts in victim environments. [9] |
| S1081 | BADHATCH | BADHATCH can use nltest.exe /domain_trusts to discover domain trust relationships on a compromised machine. [10] |
| S0534 | Bazar | Bazar can use Nltest tools to obtain information about the domain. [11] [12] |
| G1043 | BlackByte | BlackByte enumerated Active Directory information and trust relationships during operations. [13] [14] |
| S0521 | BloodHound | BloodHound has the ability to map domain trusts and identify misconfigurations for potential abuse. [15] |
| S1063 | Brute Ratel C4 | Brute Ratel C4 can use LDAP queries and nltest /domain_trusts for domain trust discovery. [16] [17] |
| C0015 | C0015 | During C0015 , the threat actors used the command nltest /domain_trusts /all_trusts to enumerate domain trusts. [18] |
| G0114 | Chimera | Chimera has nltest /domain_trusts to identify domain trust relationships. [19] |
| S0105 | dsquery | dsquery can be used to gather information on domain trusts with dsquery * -filter "(objectClass=trustedDomain)" -attr * . [3] |
| S1159 | DUSTTRAP | DUSTTRAP can identify Active Directory information and related items. [20] |
| G1006 | Earth Lusca | Earth Lusca has used Nltest to obtain information about domain controllers. [21] |
| S0363 | Empire | Empire has modules for enumerating domain trusts. [22] |
| G0061 | FIN8 | FIN8 has retrieved a list of trusted domains by using nltest.exe /domain_trusts . [23] |
| S0483 | IcedID | IcedID used Nltest during initial discovery. [24] [25] |
| S9035 | LAMEHUG | LAMEHUG can gather Active Directory domain information. [26] |
| S1160 | Latrodectus | Latrodectus can run C:\Windows\System32\cmd.exe /c nltest /domain_trusts to discover domain trusts. [27] [28] |
| C0049 | Leviathan Australian Intrusions | Leviathan performed Active Directory enumeration of victim environments during Leviathan Australian Intrusions . [29] |
| G0030 | Lotus Blossom | Lotus Blossom has used tools such as AdFind to make Active Directory queries. [30] |
| G0059 | Magic Hound | Magic Hound has used a web shell to execute nltest /trusted_domains to identify trust relationships. [31] |
| S1146 | MgBot | MgBot includes modules for collecting information on local domain users and permissions. [32] |
| G1054 | MirrorFace | MirrorFace has run nltest.exe /domain_trusts on compromised systems to discover domain relationships. [33] |
| S0359 | Nltest | Nltest may be used to enumerate trusted domains by using commands such as nltest /domain_trusts . [34] [35] |
| S1145 | Pikabot | Pikabot will gather information concerning the Windows Domain the victim machine is a member of during execution. [36] |
| S0378 | PoshC2 | PoshC2 has modules for enumerating domain trusts. [37] |
| S0194 | PowerSploit | PowerSploit has modules such as Get-NetDomainTrust and Get-NetForestTrust to enumerate domain and forest trusts. [38] [39] |
| S0650 | QakBot | QakBot can run nltest /domain_trusts /all_trusts for domain trust discovery. [40] |
| S1071 | Rubeus | Rubeus can gather information about domain trusts. [41] [42] |
| S1124 | SocGholish | SocGholish can profile compromised systems to identify domain trust relationships. [43] [44] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 used the Get-AcceptedDomain PowerShell cmdlet to enumerate accepted domains through an Exchange Management Shell. [45] They also used AdFind to enumerate domains and to discover trust between federated domains. [46] [47] |
| G1053 | Storm-0501 | Storm-0501 has used Windows native utility Nltest nltest.exe for discovery. [48] |
| G1046 | Storm-1811 | Storm-1811 has enumerated domain accounts and access during intrusions. [49] |
| S0266 | TrickBot | TrickBot can gather information about domain trusts by utilizing Nltest . [35] [50] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Map the trusts within existing domains/forests and keep trust relationships to a minimum. |
| M1030 | Network Segmentation | Employ network segmentation for sensitive domains. [3] . |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0007 | Detection of Domain Trust Discovery via API, Script, and CLI Enumeration | AN0016 | Adversary uses nltest, PowerShell, or Win32/.NET API to enumerate domain trust relationships (via DSEnumerateDomainTrusts, GetAllTrustRelationships, or LDAP queries), followed by discovery or authentication staging. |

---

## References

- [Microsoft. (2009, October 7). Trust Technologies. Retrieved February 14, 2019.](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc759554(v=ws.10))
- [Metcalf, S. (2015, July 15). It’s All About Trust – Forging Kerberos Trust Tickets to Spoof Access across Active Directory Trusts. Retrieved February 14, 2019.](https://adsecurity.org/?p=1588)
- [Schroeder, W. (2017, October 30). A Guide to Attacking Domain Trusts. Retrieved February 14, 2019.](https://posts.specterops.io/a-guide-to-attacking-domain-trusts-971e52cb2944)
- [Florio, E.. (2017, May 4). Windows Defender ATP thwarts Operation WilySupply software supply chain cyberattack. Retrieved February 14, 2019.](https://www.microsoft.com/security/blog/2017/05/04/windows-defender-atp-thwarts-operation-wilysupply-software-supply-chain-cyberattack/)
- [Brian Donohue, Katie Nickels, Paul Michaud, Adina Bodkins, Taylor Chapman, Tony Lambert, Jeff Felling, Kyle Rainey, Mike Haag, Matt Graeber, Aaron Didier.. (2020, October 29). A Bazar start: How one hospital thwarted a Ryuk ransomware outbreak. Retrieved October 30, 2020.](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)
- [McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)
- [Goody, K., et al (2019, January 11). A Nasty Trick: From Credential Theft Malware to Business Disruption. Retrieved May 12, 2020.](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)
- [Kamble, V. (2022, June 28). Bumblebee: New Loader Rapidly Assuming Central Position in Cyber-crime Ecosystem. Retrieved August 24, 2022.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime)
- [Steven Campbell, Akshay Suthar, & Connor Belfiorre. (2023, July 26). Conti and Akira: Chained Together. Retrieved February 20, 2024.](https://arcticwolf.com/resources/blog/conti-and-akira-chained-together/)
- [Vrabie, V., et al. (2021, March 10). FIN8 Returns with Improved BADHATCH Toolkit. Retrieved September 8, 2021.](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Pantazopoulos, N. (2020, June 2). In-depth analysis of the new Team9 malware family. Retrieved December 1, 2020.](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
- [US Federal Bureau of Investigation & US Secret Service. (2022, February 11). Indicators of Compromise Associated with BlackByte Ransomware. Retrieved December 16, 2024.](https://www.ic3.gov/CSA/2022/220211.pdf)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [Red Team Labs. (2018, April 24). Hidden Administrative Accounts: BloodHound to the Rescue. Retrieved October 28, 2020.](https://www.crowdstrike.com/blog/hidden-administrative-accounts-bloodhound-to-the-rescue/)
- [Harbison, M. and Renals, P. (2022, July 5). When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors. Retrieved February 1, 2023.](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
- [Kenefick, I. et al. (2022, October 12). Black Basta Ransomware Gang Infiltrates Networks via QAKBOT, Brute Ratel, and Cobalt Strike. Retrieved February 6, 2023.](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [Chen, J., et al. (2022). Delving Deep: An Analysis of Earth Lusca’s Operations. Retrieved July 1, 2022.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Martin Zugec. (2021, July 27). Deep Dive Into a FIN8 Attack - A Forensic Investigation. Retrieved September 1, 2021.](https://businessinsights.bitdefender.com/deep-dive-into-a-fin8-attack-a-forensic-investigation)
- [DFIR. (2021, March 29). Sodinokibi (aka REvil) Ransomware. Retrieved July 22, 2024.](https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/)
- [DFIR. (2022, April 25). Quantum Ransomware. Retrieved July 26, 2024.](https://thedfirreport.com/2022/04/25/quantum-ransomware/)
- [Google Threat Intelligence Group. (2025, November 5). GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools. Retrieved March 31, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
- [Stepanic, D. and Bousseaden, S. (2024, May 15). Spring Cleaning with LATRODECTUS: A Potential Replacement for ICEDID. Retrieved September 13, 2024.](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
- [Batista, J. (2024, June 17). Latrodectus, are you coming back?. Retrieved September 13, 2024.](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
- [CISA et al. (2024, July 8). People’s Republic of China (PRC) Ministry of State Security APT40 Tradecraft in Action. Retrieved February 3, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-190a)
- [Symntec Threat Hunter Team. (2022, November 12). Billbug: State-sponsored Actor Targets Cert Authority, Government Agencies in Multiple Asian Countries. Retrieved March 15, 2025.](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [Threat Hunter Team. (2023, April 20). Daggerfly: APT Actor Targets Telecoms Company in Africa. Retrieved July 25, 2024.](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
- [Trend Micro. (2024, November 19). Spot the Difference: Earth Kasha's New LODEINFO Campaign And The Correlation Analysis With The APT10 Umbrella. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html)
- [ss64. (n.d.). NLTEST.exe - Network Location Test. Retrieved February 14, 2019.](https://ss64.com/nt/nltest.html)
- [Bacurio Jr., F. and Salvio, J. (2018, April 9). Trickbot’s New Reconnaissance Plugin. Retrieved February 14, 2019.](https://www.fortinet.com/blog/threat-research/trickbot-s-new-reconnaissance-plugin.html)
- [Daniel Stepanic & Salim Bitam. (2024, February 23). PIKABOT, I choose you!. Retrieved July 12, 2024.](https://www.elastic.co/security-labs/pikabot-i-choose-you)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.](https://github.com/PowerShellMafia/PowerSploit)
- [PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.](http://powersploit.readthedocs.io)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [The DFIR Report. (2020, October 8). Ryuk’s Return. Retrieved October 9, 2020.](https://thedfirreport.com/2020/10/08/ryuks-return/)
- [The DFIR Report. (2020, November 5). Ryuk Speed Run, 2 Hours to Ransom. Retrieved November 6, 2020.](https://thedfirreport.com/2020/11/05/ryuk-speed-run-2-hours-to-ransom/)
- [Andrew Northern. (2022, November 22). SocGholish, a very real threat from a very fake update. Retrieved February 13, 2024.](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
- [Red Canary. (2024, March). Red Canary 2024 Threat Detection Report: SocGholish. Retrieved March 22, 2024.](https://redcanary.com/threat-detection-report/threats/socgholish/)
- [Cash, D. et al. (2020, December 14). Dark Halo Leverages SolarWinds Compromise to Breach Organizations. Retrieved December 29, 2020.](https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/)
- [CrowdStrike. (2022, January 27). Early Bird Catches the Wormhole: Observations from the StellarParticle Campaign. Retrieved February 7, 2022.](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)
- [MSTIC, CDOC, 365 Defender Research Team. (2021, January 20). Deep dive into the Solorigate second-stage activation: From SUNBURST to TEARDROP and Raindrop . Retrieved January 22, 2021.](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)
- [Microsoft Threat Intelligence. (2024, September 26). Storm-0501: Ransomware attacks expanding to hybrid cloud environments. Retrieved October 19, 2025.](https://www.microsoft.com/en-us/security/blog/2024/09/26/storm-0501-ransomware-attacks-expanding-to-hybrid-cloud-environments/)
- [Microsoft Threat Intelligence. (2024, May 15). Threat actors misusing Quick Assist in social engineering attacks leading to ransomware. Retrieved March 14, 2025.](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)
- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)

---

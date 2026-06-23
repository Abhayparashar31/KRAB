# Application Layer Protocol

## Description

Adversaries may communicate using OSI application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server.

Adversaries may utilize many different protocols, including those used for web browsing, transferring files, electronic mail, DNS, or publishing/subscribing. For connections that occur internally within an enclave (such as those between a proxy or pivot node and other nodes), commonly used protocols are SMB, SSH, or RDP. [1]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0660 | Clambling | Clambling has the ability to use Telnet for communication. [2] |
| S0038 | Duqu | Duqu uses a custom command and control protocol that communicates over commonly used ports, and is frequently encapsulated by application layer protocols. [3] |
| C0041 | FrostyGoop Incident | During FrostyGoop Incident , the adversary initiated Layer Two Tunnelling Protocol (L2TP) connections to Moscow-based IP addresses. [4] |
| S0601 | Hildegard | Hildegard has used an IRC channel for C2 communications. [5] |
| G1032 | INC Ransom | INC Ransom has used valid accounts over RDP to connect to targeted systems. [6] |
| S0532 | Lucifer | Lucifer can use the Stratum protocol on port 10001 for communication between the cryptojacking bot and the mining server. [7] |
| G0059 | Magic Hound | Magic Hound malware has used IRC for C2. [8] [9] |
| S0034 | NETEAGLE | Adversaries can also use NETEAGLE to establish an RDP connection with a controller over TCP/7519. |
| S1147 | Nightdoor | Nightdoor uses TCP and UDP communication for command and control traffic. [10] [11] |
| S1084 | QUIETEXIT | QUIETEXIT can use an inverse negotiated SSH connection as part of its C2. [1] |
| S1130 | Raspberry Robin | Raspberry Robin is capable of contacting the TOR network for delivering second-stage payloads. [12] [13] [14] |
| G0106 | Rocke | Rocke issued wget requests from infected systems to the C2. [15] |
| S0623 | Siloscape | Siloscape connects to an IRC server for C2. [16] |
| S0633 | Sliver | Sliver can utilize the Wireguard VPN protocol for command and control. [17] |
| G0139 | TeamTNT | TeamTNT has used an IRC bot for C2 communications. [18] |
| G1047 | Velvet Ant | Velvet Ant has used reverse SSH tunnels to communicate to victim devices. [19] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1037 | Filter Network Traffic | Use network appliances to filter ingress or egress traffic and perform protocol-based filtering. Configure software on endpoints to filter network traffic. |
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0444 | Detection of Command and Control Over Application Layer Protocols | AN1225 | Detects suspicious usage of common application-layer protocols (e.g., HTTP, HTTPS, DNS, SMB) by abnormal processes, with high outbound byte counts or irregular ports, possibly indicating command and control or data exfiltration. |
| AN1226 | Detects suspicious curl, wget, or custom socket traffic that leverages DNS, HTTPS, or IRC-style protocols with unbalanced traffic or beacon-like intervals. |  |  |
| AN1227 | Detects applications using abnormal protocols or high volume traffic not previously associated with the process image, such as Automator or AppleScript invoking curl or python sockets. |  |  |
| AN1228 | Detects application-layer tunneling or unauthorized app protocols like DNS-over-HTTPS, embedded C2 in TLS/HTTP headers, or misused SMB traffic crossing VLANs. |  |  |

---

## References

- [Mandiant. (2022, May 2). UNC3524: Eye Spy on Your Email. Retrieved August 17, 2023.](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Symantec Security Response. (2011, November). W32.Duqu: The precursor to the next Stuxnet. Retrieved September 17, 2015.](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
- [Mark Graham, Carolyn Ahlers, Kyle O'Meara; Dragos. (2024, July). Impact of FrostyGoop ICS Malware on Connected OT Systems. Retrieved November 20, 2024.](https://hub.dragos.com/hubfs/Reports/Dragos-FrostyGoop-ICS-Malware-Intel-Brief-0724_r2.pdf)
- [Chen, J. et al. (2021, February 3). Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes. Retrieved April 5, 2021.](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/)
- [Team Huntress. (2023, August 11). Investigating New INC Ransom Group Activity. Retrieved June 5, 2024.](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)
- [Hsu, K. et al. (2020, June 24). Lucifer: New Cryptojacking and DDoS Hybrid Malware Exploiting High and Critical Vulnerabilities to Infect Windows Devices. Retrieved November 16, 2020.](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
- [Lee, B. and Falcone, R. (2017, February 15). Magic Hound Campaign Attacks Saudi Targets. Retrieved December 27, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [Ahn Ho, Facundo Muñoz, & Marc-Etienne M.Léveillé. (2024, March 7). Evasive Panda leverages Monlam Festival to target Tibetans. Retrieved July 25, 2024.](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
- [Threat Hunter Team. (2024, July 23). Daggerfly: Espionage Group Makes Major Update to Toolset. Retrieved July 25, 2024.](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)
- [Lauren Podber and Stef Rand. (2022, May 5). Raspberry Robin gets the worm early. Retrieved May 17, 2024.](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)
- [Christopher So. (2022, December 20). Raspberry Robin Malware Targets Telecom, Governments. Retrieved May 17, 2024.](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
- [Patrick Schläpfer . (2024, April 10). Raspberry Robin Now Spreading Through Windows Script Files. Retrieved May 17, 2024.](https://threatresearch.ext.hp.com/raspberry-robin-now-spreading-through-windows-script-files/)
- [Liebenberg, D.. (2018, August 30). Rocke: The Champion of Monero Miners. Retrieved May 26, 2020.](https://blog.talosintelligence.com/2018/08/rocke-champion-of-monero-miners.html)
- [Prizmant, D. (2021, June 7). Siloscape: First Known Malware Targeting Windows Containers to Compromise Cloud Environments. Retrieved June 9, 2021.](https://unit42.paloaltonetworks.com/siloscape/)
- [Cybereason Global SOC and Incident Response Team. (n.d.). Sliver C2 Leveraged by Many Threat Actors. Retrieved March 24, 2025.](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)
- [Fiser, D. Oliveira, A. (n.d.). Tracking the Activities of TeamTNT A Closer Look at a Cloud-Focused Malicious Actor Group. Retrieved September 22, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-tracking-the-activities-of-teamTNT.pdf)
- [Sygnia Team. (2024, June 3). China-Nexus Threat Group ‘Velvet Ant’ Abuses F5 Load Balancers for Persistence. Retrieved March 14, 2025.](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)

---

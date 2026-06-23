# Encrypted Channel

## Description

Adversaries may employ an encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if secret keys are encoded and/or generated within malware samples/configuration files.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0016 | APT29 | APT29 has used multiple layers of encryption within malware to protect C2 communication. [1] |
| G1002 | BITTER | BITTER has encrypted their C2 communications. [2] |
| S0631 | Chaes | Chaes has used encryption for its C2 channel. [3] |
| S0498 | Cryptoistic | Cryptoistic can engage in encrypted communications with C2. [4] |
| S0367 | Emotet | Emotet has encrypted data before sending to the C2 server. [5] |
| S0032 | gh0st RAT | gh0st RAT has encrypted TCP communications to evade detection. [6] |
| S1198 | Gomir | Gomir uses a custom encryption algorithm for content sent to command and control infrastructure. [7] |
| C0035 | KV Botnet Activity | KV Botnet Activity command and control activity includes transmission of an RSA public key in communication from the server, but this is followed by subsequent negotiation stages that represent a form of handshake similar to TLS negotiation. [8] |
| S0681 | Lizar | Lizar can support encrypted communications between the client and server. [9] [10] [11] |
| S1016 | MacMa | MacMa has used TLS encryption to initialize a custom protocol for C2 communications. [12] |
| G0059 | Magic Hound | Magic Hound has used an encrypted http proxy in C2 communications. [13] |
| S0198 | NETWIRE | NETWIRE can encrypt C2 communications. [14] |
| S1012 | PowerLess | PowerLess can use an encrypted channel for C2 communications. [15] |
| S1046 | PowGoop | PowGoop can receive encrypted commands from C2. [16] |
| S0662 | RCSession | RCSession can use an encrypted beacon to check in with C2. [17] |
| C0030 | Triton Safety Instrumented System Attack | In the Triton Safety Instrumented System Attack , TEMP.Veles used cryptcat binaries to encrypt their traffic. [18] |
| G0081 | Tropic Trooper | Tropic Trooper has encrypted traffic with the C2 to prevent network detection. [19] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. |
| M1020 | SSL/TLS Inspection | SSL/TLS inspection can be used to see the contents of encrypted sessions to look for network-based indicators of malware communication protocols. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0273 | Detection Strategy for Encrypted Channel across OS Platforms | AN0759 | Processes that normally do not initiate network connections establishing outbound encrypted TLS/SSL sessions, especially with asymmetric traffic volumes (client sending more than receiving) or non-standard certificate chains. Defender observations correlate process creation with unexpected network encryption libraries being loaded. |
| AN0760 | Processes like curl, wget, python, socat, or custom binaries initiating TLS/SSL sessions to non-standard destinations. Defender sees abnormal syscalls for connect(), loading of libssl libraries, and persistent outbound encrypted traffic from daemons not normally communicating externally. |  |  |
| AN0761 | Applications or launchd jobs initiating encrypted TLS traffic to rare external hosts. Defender observes unified logs showing ssl/TLS API calls by processes not baseline-approved, and payload entropy suggesting encrypted C2 sessions. |  |  |
| AN0762 | VMware management daemons or guest processes initiating encrypted connections outside expected vCenter, update servers, or internal comms. Defender identifies hostd or vpxa initiating outbound TLS flows with uncommon destinations. |  |  |
| AN0763 | Unusual TLS tunnels through ports not normally encrypted (e.g., TLS on port 8080, 53). Defender sees NetFlow/IPFIX or packet inspection indicating high-entropy traffic volumes and asymmetric client/server exchange ratios. |  |  |

---

## References

- [Secureworks CTU. (n.d.). IRON HEMLOCK. Retrieved February 22, 2022.](http://www.secureworks.com/research/threat-profiles/iron-hemlock)
- [Dela Paz, R. (2016, October 21). BITTER: a targeted attack against Pakistan. Retrieved June 1, 2022.](https://www.forcepoint.com/blog/x-labs/bitter-targeted-attack-against-pakistan)
- [Salem, E. (2020, November 17). CHAES: Novel Malware Targeting Latin American E-Commerce. Retrieved June 30, 2021.](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
- [Stokes, P. (2020, July 27). Four Distinct Families of Lazarus Malware Target Apple’s macOS Platform. Retrieved August 7, 2020.](https://www.sentinelone.com/blog/four-distinct-families-of-lazarus-malware-target-apples-macos-platform/)
- [Xiaopeng Zhang. (2017, May 3). Deep Analysis of New Emotet Variant – Part 1. Retrieved April 1, 2019.](https://www.fortinet.com/blog/threat-research/deep-analysis-of-new-emotet-variant-part-1.html)
- [Quinn, J. (2019, March 25). The odd case of a Gh0stRAT variant. Retrieved July 15, 2020.](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
- [Symantec Threat Hunter Team. (2024, May 16). Springtail: New Linux Backdoor Added to Toolkit. Retrieved January 17, 2025.](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
- [Black Lotus Labs. (2023, December 13). Routers Roasting On An Open Firewall: The KV-Botnet Investigation. Retrieved June 10, 2024.](https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/)
- [Seals, T. (2021, May 14). FIN7 Backdoor Masquerades as Ethical Hacking Tool. Retrieved February 2, 2022.](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [Cocomazzi, Antonio. (2024, July 17). FIN7 Reboot | Cybercrime Gang Enhances Ops with New EDR Bypasses and Automated Attacks. Retrieved September 24, 2025.](https://www.sentinelone.com/labs/fin7-reboot-cybercrime-gang-enhances-ops-with-new-edr-bypasses-and-automated-attacks/)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [Lambert, T. (2020, January 29). Intro to Netwire. Retrieved January 7, 2021.](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
- [Cybereason Nocturnus. (2022, February 1). PowerLess Trojan: Iranian APT Phosphorus Adds New PowerShell Backdoor for Espionage. Retrieved June 1, 2022.](https://www.cybereason.com/blog/research/powerless-trojan-iranian-apt-phosphorus-adds-new-powershell-backdoor-for-espionage)
- [FBI, CISA, CNMF, NCSC-UK. (2022, February 24). Iranian Government-Sponsored Actors Conduct Cyber Operations Against Global Government and Commercial Networks. Retrieved September 27, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
- [Counter Threat Unit Research Team. (2019, December 29). BRONZE PRESIDENT Targets NGOs. Retrieved April 13, 2021.](https://www.secureworks.com/research/bronze-president-targets-ngos)
- [FireEye Intelligence . (2018, October 23). TRITON Attribution: Russian Government-Owned Lab Most Likely Built Custom Intrusion Tools for TRITON Attackers. Retrieved April 16, 2019.](https://www.fireeye.com/blog/threat-research/2018/10/triton-attribution-russian-government-owned-lab-most-likely-built-tools.html)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)

---

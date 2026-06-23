	# Data Obfuscation

## Description

Adversaries may obfuscate command and control traffic to make it more difficult to detect. [1] Command and control (C2) communications are hidden (but not necessarily encrypted) in an attempt to make the content more difficult to discover or decipher and to make the communication less conspicuous and hide commands from being seen. This encompasses many methods, such as adding junk data to protocol traffic, using steganography, or impersonating legitimate protocols.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1111 | DarkGate | DarkGate will retrieved encrypted commands from its command and control server for follow-on actions such as cryptocurrency mining. [2] |
| S9003 | evilginx2 | evilginx2 can modify the Origin and Referrer fields in HTTPS headers it relays between intended victims and legitimate websites to comply with cross-origin resource sharing (CORS) restrictions. [3] |
| S0381 | FlawedAmmyy | FlawedAmmyy may obfuscate portions of the initial C2 handshake. [4] |
| S1120 | FRAMESTING | FRAMESTING can send and receive zlib compressed data within POST requests. [5] |
| S1044 | FunnyDream | FunnyDream can send compressed and obfuscated packets to C2. [1] |
| G0047 | Gamaredon Group | Gamaredon Group has used obfuscated VBScripts with randomly generated variable names and concatenated strings. [6] |
| S1100 | Ninja | Ninja has the ability to modify headers and URL paths to hide malicious traffic in HTTP requests. [7] |
| S0439 | Okrum | Okrum leverages the HTTP protocol for C2 communication, while hiding the actual messages in the Cookie and Set-Cookie headers of the HTTP requests. [8] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors encrypted IP addresses used for "Agent" proxy hops with RC4. [9] |
| S0495 | RDAT | RDAT has used encoded data within subdomains as AES ciphertext to communicate from the host to the C2. [10] |
| S0610 | SideTwist | SideTwist can embed C2 responses in the source code of a fake Flickr webpage. [11] |
| S0533 | SLOTHFULMEDIA | SLOTHFULMEDIA has hashed a string containing system information prior to exfiltration via POST requests. [12] |
| S1183 | StrelaStealer | StrelaStealer encrypts the payload of HTTP POST communications using the same XOR key used for the malware's DLL payload. [13] |
| S9001 | SystemBC | SystemBC has encoded with XOR and encrypted with RC4 its beacon. [14] |
| S0682 | TrailBlazer | TrailBlazer can masquerade its C2 traffic as legitimate Google Notifications HTTP requests. [15] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate some obfuscation activity at the network level. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0053 | Detect Obfuscated C2 via Network Traffic Analysis | AN0144 | Detects excessive outbound traffic to remote host over HTTP(S) from uncommon or previously unseen processes. |
| AN0145 | Identifies custom or previously unseen userland processes initiating high-volume HTTP connections with low response volume. |  |  |
| AN0146 | Flags unexpected user applications initiating long-lived HTTP(S) sessions with irregular traffic patterns. |  |  |

---

## References

- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Gretzky, K.. (2018, July 26). Evilginx 2 - Next Generation of Phishing 2FA Tokens. Retrieved October 14, 2019.](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/)
- [Proofpoint Staff. (2018, March 7). Leaked Ammyy Admin Source Code Turned into Malware. Retrieved May 28, 2019.](https://www.proofpoint.com/us/threat-insight/post/leaked-ammyy-admin-source-code-turned-malware)
- [Lin, M. et al. (2024, January 31). Cutting Edge, Part 2: Investigating Ivanti Connect Secure VPN Zero-Day Exploitation. Retrieved February 27, 2024.](https://www.mandiant.com/resources/blog/investigating-ivanti-zero-day-exploitation)
- [Unit 42. (2022, December 20). Russia’s Trident Ursa (aka Gamaredon APT) Cyber Conflict Operations Unwavering Since Invasion of Ukraine. Retrieved September 12, 2024.](https://unit42.paloaltonetworks.com/trident-ursa/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Hromcova, Z. (2019, July). OKRUM AND KETRICAN: AN OVERVIEW OF RECENT KE3CHANG GROUP ACTIVITY. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Falcone, R. (2020, July 22). OilRig Targets Middle Eastern Telecommunications Organization and Adds Novel C2 Channel with Steganography to Its Inventory. Retrieved July 28, 2020.](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [DHS/CISA, Cyber National Mission Force. (2020, October 1). Malware Analysis Report (MAR) MAR-10303705-1.v1 – Remote Access Trojan: SLOTHFULMEDIA. Retrieved October 2, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
- [DCSO CyTec Blog. (2022, November 8). #ShortAndMalicious: StrelaStealer aims for mail credentials. Retrieved December 31, 2024.](https://medium.com/@DCSO_CyTec/shortandmalicious-strelastealer-aims-for-mail-credentials-a4c3e78c8abc)
- [Black Lotus Labs . (2025, September 18). SystemBC: Bringing the noise. Retrieved December 15, 2025.](https://blog.lumen.com/systembc-bringing-the-noise/)
- [CrowdStrike. (2022, January 27). Early Bird Catches the Wormhole: Observations from the StellarParticle Campaign. Retrieved February 7, 2022.](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)

---

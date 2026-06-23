# Data Encoding

## Description

Adversaries may encode data to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a standard data encoding system. Use of data encoding may adhere to existing protocol specifications and includes use of ASCII, Unicode, Base64, MIME, or other binary-to-text and character encoding systems. [1] [2] Some data encoding systems may also result in data compression, such as gzip.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0128 | BADNEWS | After encrypting C2 data, BADNEWS converts it into a hexadecimal representation and then encodes it into base64. [3] |
| S9003 | evilginx2 | evilginx2 can randomly generate and Base64 encode parameters in phishing links to defeat static detection. [4] |
| S0132 | H1N1 | H1N1 obfuscates C2 traffic with an altered version of base64. [5] |
| S9035 | LAMEHUG | LAMEHUG can encode queries sent to LLMs. [6] |
| S0362 | Linux Rabbit | Linux Rabbit sends the payload from the C2 server as an encoded URL parameter. [7] |
| S0699 | Mythic | Mythic provides various transform functions to encode and/or randomize C2 data. [8] |
| S0386 | Ursnif | Ursnif has used encoded data in HTTP URLs for C2. [9] |
| G1047 | Velvet Ant | Velvet Ant sent commands to compromised F5 BIG-IP devices in an encoded format requiring a passkey before interpretation and execution. [10] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool C2 signatures over time or construct protocols in such a way as to avoid detection by common defensive tools. [11] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0108 | Detection Strategy for Data Encoding in C2 Channels | AN0302 | Atypical processes (e.g., powershell.exe, regsvr32.exe) encode large outbound traffic using Base64 or other character encodings; this traffic is sent over uncommon ports or embedded in protocol fields (e.g., HTTP cookies or headers). |
| AN0303 | Custom scripts or processes encode outbound traffic using gzip, Base64, or hex prior to exfiltration via curl, wget, or custom sockets. Encoding typically occurs before or during outbound connections from non-network daemons. |  |  |
| AN0304 | Processes use built-in encoding utilities (e.g., base64 , xxd , or plutil ) to encode file contents followed by HTTP/HTTPS transfer via curl or custom applications. |  |  |
| AN0305 | ESXi daemons (e.g., hostd, vpxa) are wrapped or impersonated to send large outbound traffic using gzip/Base64 encoding over SSH or HTTP. These actions follow suspicious logins or shell access. |  |  |

---

## References

- [Wikipedia. (2016, December 26). Binary-to-text encoding. Retrieved March 1, 2017.](https://en.wikipedia.org/wiki/Binary-to-text_encoding)
- [Wikipedia. (2017, February 19). Character Encoding. Retrieved March 1, 2017.](https://en.wikipedia.org/wiki/Character_encoding)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Gretzky, K. (2020, September 14). Evilginx 2.4 - Gone Phishing. Retrieved January 27, 2026.](https://breakdev.org/evilginx-2-4-gone-phishing/)
- [Reynolds, J.. (2016, September 14). H1N1: Technical analysis reveals new capabilities – part 2. Retrieved November 17, 2024.](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)
- [Conteras, T., Splunk Research Team. (2025, September 25). From Prompt to Payload: LAMEHUG’s LLM-Driven Cyber Intrusion. Retrieved April 21, 2026.](https://www.splunk.com/en_us/blog/security/lamehug-ai-driven-malware-llm-cyber-intrusion-analysis.html)
- [Anomali Labs. (2018, December 6). Pulling Linux Rabbit/Rabbot Malware Out of a Hat. Retrieved March 4, 2019.](https://www.anomali.com/blog/pulling-linux-rabbit-rabbot-malware-out-of-a-hat)
- [Thomas, C. (n.d.). Mythc Documentation. Retrieved March 25, 2022.](https://docs.mythic-c2.net/)
- [Proofpoint Staff. (2016, August 25). Nightmare on Tor Street: Ursnif variant Dreambot adds Tor functionality. Retrieved June 5, 2019.](https://www.proofpoint.com/us/threat-insight/post/ursnif-variant-dreambot-adds-tor-functionality)
- [Sygnia Team. (2024, June 3). China-Nexus Threat Group ‘Velvet Ant’ Abuses F5 Load Balancers for Persistence. Retrieved March 14, 2025.](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
- [Gardiner, J., Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

---

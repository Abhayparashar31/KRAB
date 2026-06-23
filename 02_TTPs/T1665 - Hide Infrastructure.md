# Hide Infrastructure

## Description

Adversaries may manipulate network traffic in order to hide and evade detection of their C2 infrastructure. This can be accomplished by identifying and filtering traffic from defensive tools, [1] masking malicious domains to obfuscate the true destination from both automated scanning tools and security researchers, [2] [3] [4] and otherwise hiding malicious artifacts to delay discovery and prolong the effectiveness of adversary infrastructure that could otherwise be identified, blocked, or taken down entirely.

C2 networks may include the use of Proxy or VPNs to disguise IP addresses, which can allow adversaries to blend in with normal network traffic and bypass conditional access policies or anti-abuse protections. For example, an adversary may use a virtual private cloud to spoof their IP address to closer align with a victim's IP address ranges. This may also bypass security measures relying on geolocation of the source IP address. [5] [6]

Adversaries may also attempt to filter network traffic in order to evade defensive tools in numerous ways, including blocking/redirecting common incident responder or security appliance user agents. [7] [8] Filtering traffic based on IP and geo-fencing may also avoid automated sandboxing or researcher activity (i.e., Virtualization/Sandbox Evasion ). [1] [7]

Hiding C2 infrastructure may also be supported by Resource Development activities such as Acquire Infrastructure and Compromise Infrastructure . For example, using widely trusted hosting services or domains such as prominent URL shortening providers or marketing services for C2 networks may enable adversaries to present benign content that later redirects victims to malicious web pages or infrastructure once specific conditions are met. [9] [10]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0016 | APT29 | APT29 uses compromised residential endpoints, typically within the same ISP IP address range, as proxies to hide the true source of C2 traffic. [11] |
| S1111 | DarkGate | DarkGate command and control includes hard-coded domains in the malware masquerading as legitimate services such as Akamai CDN or Amazon Web Services. [12] |
| S1206 | JumbledPath | JumbledPath can use a chain of jump hosts to communicate with compromised devices to obscure actor infrastructure. [13] |
| C0061 | Operation Digital Eye | During Operation Digital Eye , threat actors used public Cloud infrastructure to mask malicious activity. [14] |
| C0055 | Quad7 Activity | Quad7 Activity has rotated the compromised SOHO IPs used in password spraying activity to hamper detection and network blocking activities by defenders. [15] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 set the hostnames of their C2 infrastructure to match legitimate hostnames in the victim environment. They also used IP addresses originating from the same country as the victim for their VPN infrastructure. [16] |
| S1164 | UPSTYLE | UPSTYLE attempts to retrieve a non-existent webpage from the command and control server resulting in hidden commands sent via resulting error messages. [17] |
| G0128 | ZIRCONIUM | ZIRCONIUM has utilized an ORB (operational relay box) network – consisting compromised devices such as small office and home office (SOHO) routers, IoT devices, and leased virtual private servers (VPS) – to obfuscate the origin of C2 traffic. [18] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0411 | Detection Strategy for Hide Infrastructure | AN1148 | Monitor DNS queries, proxy logs, and user-agent strings for anomalous patterns associated with adversary attempts to hide infrastructure. Defenders may observe DNS resolutions to short-lived domains, abnormal WHOIS registration data, or filtering of known defensive/responder IP addresses. |
| AN1149 | Detect adversaries filtering traffic or modifying server responses to evade scanning. Monitor iptables, nftables, or proxy configurations that deny or redirect requests from known scanning agents or defensive tools. |  |  |
| AN1150 | Monitor unified logs for manipulation of proxy configurations, DNS resolution, or filtering rules. Adversaries may redirect responses or use trusted domains that later resolve to malicious C2 infrastructure. |  |  |
| AN1151 | Inspect network telemetry for adversary attempts to blend malicious traffic with legitimate flows using VPNs, proxies, or geolocation spoofing. Defensive teams may observe anomalous tunnels, encrypted sessions to suspicious domains, or geo-mismatched IP activity. |  |  |
| AN1152 | Monitor VM-level DNS and network traffic logs for adversary-controlled domains or selective response behavior (e.g., dropped requests from security scanners). |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0411 | Detection Strategy for Hide Infrastructure | AN1148 | Monitor DNS queries, proxy logs, and user-agent strings for anomalous patterns associated with adversary attempts to hide infrastructure. Defenders may observe DNS resolutions to short-lived domains, abnormal WHOIS registration data, or filtering of known defensive/responder IP addresses. |
| AN1149 | Detect adversaries filtering traffic or modifying server responses to evade scanning. Monitor iptables, nftables, or proxy configurations that deny or redirect requests from known scanning agents or defensive tools. |  |  |
| AN1150 | Monitor unified logs for manipulation of proxy configurations, DNS resolution, or filtering rules. Adversaries may redirect responses or use trusted domains that later resolve to malicious C2 infrastructure. |  |  |
| AN1151 | Inspect network telemetry for adversary attempts to blend malicious traffic with legitimate flows using VPNs, proxies, or geolocation spoofing. Defensive teams may observe anomalous tunnels, encrypted sessions to suspicious domains, or geo-mismatched IP activity. |  |  |
| AN1152 | Monitor VM-level DNS and network traffic logs for adversary-controlled domains or selective response behavior (e.g., dropped requests from security scanners). |  |  |

---

## References

- [Axel F, Selena Larson. (2023, October 30). TA571 Delivers IcedID Forked Loader. Retrieved February 13, 2024.](https://www.proofpoint.com/us/blog/threat-insight/security-brief-ta571-delivers-icedid-forked-loader)
- [Nick Simonian. (2023, May 22). Don't @ Me: URL Obfuscation Through Schema Abuse. Retrieved February 13, 2024.](https://www.mandiant.com/resources/blog/url-obfuscation-schema-abuse)
- [Spyboy. (2023). Facad1ng. Retrieved February 13, 2024.](https://github.com/spyboy-productions/Facad1ng)
- [Dusty Miller. (2023, October 17). Are You Sure Your Browser is Up to Date? The Current Landscape of Fake Browser Updates . Retrieved February 13, 2024.](https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates)
- [Sysdig. (2023). Sysdig Global Cloud Threat Report. Retrieved March 1, 2024.](https://sysdig.com/content/c/pf-2023-global-cloud-threat-report?x=u_WFRi&xs=524303#page=1)
- [Orange Cyberdefense. (2024, March 14). Unveiling the depths of residential proxies providers. Retrieved April 11, 2024.](https://www.orangecyberdefense.com/global/blog/research/residential-proxies)
- [Bluescreenofjeff.com. (2015, April 12). Combatting Incident Responders with Apache mod_rewrite. Retrieved February 13, 2024.](https://bluescreenofjeff.com/2016-04-12-combatting-incident-responders-with-apache-mod_rewrite/)
- [Andrew Northern. (2022, November 22). SocGholish, a very real threat from a very fake update. Retrieved February 13, 2024.](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
- [Microsoft Threat Intelligence. (2023, December 7). Star Blizzard increases sophistication and evasion in ongoing attacks. Retrieved February 13, 2024.](https://www.microsoft.com/en-us/security/blog/2023/12/07/star-blizzard-increases-sophistication-and-evasion-in-ongoing-attacks/)
- [Nathaniel Raymond. (2023, August 16). Major Energy Company Targeted in Large QR Code Phishing Campaign. Retrieved February 13, 2024.](https://cofense.com/blog/major-energy-company-targeted-in-large-qr-code-campaign/)
- [UK National Cyber Security Center et al. (2024, February). SVR cyber actors adapt tactics for initial cloud access. Retrieved March 1, 2024.](https://www.ic3.gov/Media/News/2024/240226.pdf)
- [Ernesto Fernández Provecho, Pham Duy Phuc, Ciana Driscoll & Vinoo Thomas. (2023, November 21). The Continued Evolution of the DarkGate Malware-as-a-Service. Retrieved February 9, 2024.](https://www.trellix.com/blogs/research/the-continued-evolution-of-the-darkgate-malware-as-a-service/)
- [Cisco Talos. (2025, February 20). Weathering the storm: In the midst of a Typhoon. Retrieved February 24, 2025.](https://blog.talosintelligence.com/salt-typhoon-analysis/)
- [Aleksandar Milenkoski, Luigi Martire. (2024, December 10). Operation Digital Eye | Chinese APT Compromises Critical Digital Infrastructure via Visual Studio Code Tunnels. Retrieved February 27, 2025.](https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-studio-code-tunnels/)
- [Microsoft Threat Intelligence. (2024, October 31). Chinese threat actor Storm-0940 uses credentials from password spray attacks from a covert network. Retrieved June 4, 2025.](https://www.microsoft.com/en-us/security/blog/2024/10/31/chinese-threat-actor-storm-0940-uses-credentials-from-password-spray-attacks-from-a-covert-network/)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [Volexity Threat Research. (2024, April 12). Zero-Day Exploitation of Unauthenticated Remote Code Execution Vulnerability in GlobalProtect (CVE-2024-3400). Retrieved November 20, 2024.](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)
- [Raggi, Michael. (2024, May 22). IOC Extinction? China-Nexus Cyber Espionage Actors Use ORB Networks to Raise Cost on Defenders. Retrieved July 8, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-orb-networks)

---

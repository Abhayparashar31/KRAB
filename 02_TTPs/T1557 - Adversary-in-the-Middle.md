# Adversary-in-the-Middle

## Description

Adversaries may attempt to position themselves between two or more networked devices using an adversary-in-the-middle (AiTM) technique to support follow-on behaviors such as Network Sniffing , Transmitted Data Manipulation , or replay attacks ( Exploitation for Credential Access ). By abusing features of common networking protocols that can determine the flow of network traffic (e.g. ARP, DNS, LLMNR, etc.), adversaries may force a device to communicate through an adversary controlled system so they can collect information or perform additional actions. [1]

For example, adversaries may manipulate victim DNS settings to enable other malicious activities such as preventing/redirecting users from accessing legitimate sites and/or pushing additional malware. [2] [3] [4] Adversaries may also manipulate DNS and leverage their position in order to intercept user credentials, including access tokens ( Steal Application Access Token ) and session cookies ( Steal Web Session Cookie ). [5] [6] Downgrade Attack s can also be used to establish an AiTM position, such as by negotiating a less secure, deprecated, or weaker version of communication protocol (SSL/TLS) or encryption algorithm. [7] [8] [9]

Adversaries may also leverage the AiTM position to attempt to monitor and/or modify traffic, such as in Transmitted Data Manipulation . Adversaries can setup a position similar to AiTM to prevent traffic from flowing to the appropriate destination, potentially to impair defenses and/or in support of a Network Denial of Service .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0046 | ArcaneDoor | ArcaneDoor included interception of HTTP traffic to victim devices to identify and parse command and control information sent to the device. [10] |
| S0281 | Dok | Dok proxies web traffic to potentially monitor and alter victim HTTP(S) traffic. [11] [12] |
| S9003 | evilginx2 | evilginx2 has the ability to act as an adversary-in-the-middle (AiTM) relay between a legitimate website and a phished user to capture all transmitted data including usernames, passwords, authentication tokens, and session cookies and tokens. [13] [14] [15] [16] |
| G0094 | Kimsuky | Kimsuky has used modified versions of PHProxy to examine web traffic between the victim and the accessed website. [17] |
| S1188 | Line Runner | Line Runner intercepts HTTP requests to the victim Cisco ASA, looking for a request with a 32-character, victim dependent parameter. If that parameter matches a value in the malware, a contained payload is then written to a Lua script and executed. [10] |
| G0129 | Mustang Panda | Mustang Panda leveraged a captive portal hijack that redirected the victim to a webpage that prompted the victim to download a malicious payload. [18] |
| S1131 | NPPSPY | NPPSPY opens a new network listener for the mpnotify.exe process that is typically contacted by the Winlogon process in Windows. A new, alternative RPC channel is set up with a malicious DLL recording plaintext credentials entered into Winlogon, effectively intercepting and redirecting the logon information. [19] |
| G1041 | Sea Turtle | Sea Turtle modified DNS records at service providers to redirect traffic from legitimate resources to Sea Turtle -controlled servers to enable adversary-in-the-middle attacks for credential capture. [20] [21] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1042 | Disable or Remove Feature or Program | Disable legacy network protocols that may be used to intercept network traffic if applicable, especially those that are not needed within an environment. |
| M1041 | Encrypt Sensitive Information | Ensure that all wired and/or wireless traffic is encrypted appropriately. Use best practices for authentication protocols, such as Kerberos, and ensure web traffic that may contain credentials is protected by SSL/TLS. |
| M1037 | Filter Network Traffic | Use network appliances and host-based security software to block network traffic that is not necessary within the environment, such as legacy protocols that may be leveraged for AiTM conditions. |
| M1035 | Limit Access to Resource Over Network | Limit access to network infrastructure and resources that can be used to reshape traffic or otherwise produce AiTM conditions. |
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that can identify traffic patterns indicative of AiTM activity can be used to mitigate activity at the network level. |
| M1030 | Network Segmentation | Network segmentation can be used to isolate infrastructure components that do not require broad network access. This may mitigate, or at least alleviate, the scope of AiTM activity. |
| M1017 | User Training | Train users to be suspicious about certificate errors. Adversaries may use their own certificates in an attempt to intercept HTTPS traffic. Certificate errors may arise when the application’s certificate does not match the one expected by the host. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0296 | Detect Adversary-in-the-Middle via Network and Configuration Anomalies | AN0823 | Detects suspicious DNS/ARP poisoning attempts, unauthorized modifications to registry/network configuration, or abnormal TLS downgrade activity. Correlates changes in system configuration with subsequent unusual network flows or authentication events. |
| AN0824 | Detects unauthorized edits to /etc/hosts, /etc/resolv.conf, or suspicious ARP broadcasts. Correlates file modifications with subsequent unexpected network sessions or service creation. |  |  |
| AN0825 | Detects unauthorized edits to system configuration profiles, unexpected certificate trust changes, or abnormal ARP/DNS patterns indicative of interception. |  |  |
| AN0826 | Detects unauthorized firmware or configuration changes enabling adversary-in-the-middle positioning (e.g., route injection, DNS spoofing, SSL downgrade). Behavioral analytics focus on sudden changes to routing tables or image file integrity failures. |  |  |

---

## References

- [Rapid7. (n.d.). Man-in-the-Middle (MITM) Attacks. Retrieved March 2, 2020.](https://www.rapid7.com/fundamentals/man-in-the-middle-attacks/)
- [Tu, L. Ma, Y. Ye, G. (2020, October 1). Ttint: An IoT Remote Access Trojan spread through 2 0-day vulnerabilities. Retrieved October 28, 2021.](https://blog.netlab.360.com/ttint-an-iot-remote-control-trojan-spread-through-2-0-day-vulnerabilities/)
- [Abendan, O. (2012, June 14). How DNS Changer Trojans Direct Users to Threats. Retrieved October 28, 2021.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/web-attack/125/how-dns-changer-trojans-direct-users-to-threats)
- [Kuzmenko, A.. (2021, March 10). Ad blocker with miner included. Retrieved October 28, 2021.](https://securelist.com/ad-blocker-with-miner-included/101105/)
- [Adair, S., Lancaster, T., Volexity Threat Research. (2022, June 15). DriftingCloud: Zero-Day Sophos Firewall Exploitation and an Insidious Breach. Retrieved July 1, 2022.](https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/)
- [Microsoft Incident Response. (2022, November 16). Token tactics: How to prevent, detect, and respond to cloud token theft. Retrieved December 26, 2023.](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)
- [praetorian Editorial Team. (2014, August 19). Man-in-the-Middle TLS Protocol Downgrade Attack. Retrieved December 8, 2021.](https://www.praetorian.com/blog/man-in-the-middle-tls-ssl-protocol-downgrade-attack/)
- [Alashwali, E. S., Rasmussen, K. (2019, January 26). What's in a Downgrade? A Taxonomy of Downgrade Attacks in the TLS Protocol and Application Protocols Using TLS. Retrieved December 7, 2021.](https://arxiv.org/abs/1809.05681)
- [Team Cinnamon. (2017, February 3). Downgrade Attacks. Retrieved December 9, 2021.](https://tlseminar.github.io/downgrade-attacks/)
- [Cisco Talos. (2024, April 24). ArcaneDoor - New espionage-focused campaign found targeting perimeter network devices. Retrieved January 6, 2025.](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/)
- [Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.](https://objective-see.com/blog/blog_0x25.html)
- [Ofer Caspi. (2017, May 4). OSX Malware is Catching Up, and it wants to Read Your HTTPS Traffic. Retrieved October 5, 2021.](https://blog.checkpoint.com/2017/04/27/osx-malware-catching-wants-read-https-traffic/)
- [Gretzky, K.. (2018, July 26). Evilginx 2 - Next Generation of Phishing 2FA Tokens. Retrieved October 14, 2019.](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/)
- [Gretzky, K. (2023, May 10). Evilginx 3.0 + Evilginx Mastery. Retrieved January 27, 2026.](https://breakdev.org/evilginx-3-0-evilginx-mastery/)
- [Gretzky, K. (2023, August 24). Evilginx 3.2 - Swimming With The Phishes. Retrieved January 27, 2026.](https://breakdev.org/evilginx-3-2/)
- [Everts, M. (2025, March 28). Stealing user credentials with evilginx. Retrieved January 27, 2026.](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)
- [CISA, FBI, CNMF. (2020, October 27). https://us-cert.cisa.gov/ncas/alerts/aa20-301a. Retrieved November 4, 2020.](https://us-cert.cisa.gov/ncas/alerts/aa20-301a)
- [Patrick Whitsell. (2025, August 25). Deception in Depth: PRC-Nexus Espionage Campaign Hijacks Web Traffic to Target Diplomats. Retrieved September 9, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/prc-nexus-espionage-targets-diplomats)
- [Dray Agha. (2022, August 16). Cleartext Shenanigans: Gifting User Passwords to Adversaries With NPPSPY. Retrieved May 17, 2024.](https://www.huntress.com/blog/cleartext-shenanigans-gifting-user-passwords-to-adversaries-with-nppspy)
- [Cisco Talos. (2019, April 17). Sea Turtle: DNS Hijacking Abuses Trust In Core Internet Service. Retrieved November 20, 2024.](https://blog.talosintelligence.com/seaturtle/)
- [Paul Rascagneres. (2019, July 9). Sea Turtle keeps on swimming, finds new victims, DNS hijacking techniques. Retrieved November 20, 2024.](https://blog.talosintelligence.com/sea-turtle-keeps-on-swimming/)

---

# Remote Services

## Description

Adversaries may use Valid Accounts to log into a service that accepts remote connections, such as telnet, SSH, and VNC. The adversary may then perform actions as the logged-on user.

In an enterprise environment, servers and workstations can be organized into domains. Domains provide centralized identity management, allowing users to login using one set of credentials across the entire network. If an adversary is able to obtain a set of valid domain credentials, they could login to many different machines using remote access protocols such as secure shell (SSH) or remote desktop protocol (RDP). [1] [2] They could also login to accessible SaaS or IaaS services, such as those that federate their identities to the domain, or management platforms for internal virtualization environments such as VMware vCenter.

Legitimate applications (such as Software Deployment Tools and other administrative programs) may utilize Remote Services to access remote hosts. For example, Apple Remote Desktop (ARD) on macOS is native software used for remote management. ARD leverages a blend of protocols, including VNC to send the screen and control buffers and SSH for secure file transfer. [3] [4] [5] Adversaries can abuse applications such as ARD to gain remote code execution and perform lateral movement. In versions of macOS prior to 10.14, an adversary can escalate an SSH session to an ARD session which enables an adversary to accept TCC (Transparency, Consent, and Control) prompts without user interaction and gain access to data. [6] [7] [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0143 | Aquatic Panda | Aquatic Panda used remote scheduled tasks to install malicious software on victim systems during lateral movement actions. [8] |
| S1063 | Brute Ratel C4 | Brute Ratel C4 has the ability to use RPC for lateral movement. [9] |
| G1003 | Ember Bear | Ember Bear uses valid network credentials gathered through credential harvesting to move laterally within victim networks, often employing the Impacket framework to do so. [10] |
| S0437 | Kivars | Kivars has the ability to remotely trigger keyboard input and mouse clicks. [11] |
| S1016 | MacMa | MacMa can manage remote screen sessions. [12] |
| S0603 | Stuxnet | Stuxnet can propagate via peer-to-peer communication and updates using RPC. [13] |
| G0102 | Wizard Spider | Wizard Spider has used the WebDAV protocol to execute Ryuk payloads hosted on network file shares. [14] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Perform audits or scans of systems, permissions, insecure software, insecure configurations, etc. to identify potential weaknesses. |
| M1042 | Disable or Remove Feature or Program | If remote services, such as the ability to make direct connections to cloud virtual machines, are not required, disable these connection types where feasible. On ESXi servers, consider enabling lockdown mode, which disables direct access to an ESXi host and requires that the host be managed remotely using vCenter. [15] [16] |
| M1035 | Limit Access to Resource Over Network | Prevent unnecessary remote access to file shares, hypervisors, sensitive systems, etc. Mechanisms to limit access may include use of network concentrators, RDP gateways, etc. [17] |
| M1032 | Multi-factor Authentication | Use multi-factor authentication on remote service logons where possible. |
| M1027 | Password Policies | Do not reuse local administrator account passwords across systems. Ensure password complexity and uniqueness such that the passwords cannot be cracked or guessed. |
| M1018 | User Account Management | Limit the accounts that may use remote services. Limit the permissions for accounts that are at higher risk of compromise; for example, configure SSH so users can only run specific programs. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0269 | Behavioral Detection Strategy for Remote Service Logins and Post-Access Activity | AN0750 | Logon via RDP or WMI by a user account followed by uncommon command execution, file manipulation, or lateral network connections. |
| AN0751 | SSH session from new source IP followed by interactive shell or privilege escalation (e.g., sudo, su) and outbound lateral connection. |  |  |
| AN0752 | Remote login via ARD or SSH followed by screensharingd process activity or modification of TCC-protected files. |  |  |
| AN0753 | Use of cloud-based bastion or VM console session followed by commands that initiate outbound SSH or RDP sessions from the cloud instance to other environments. |  |  |
| AN0754 | vSphere API logins (vimService) or SSH to ESXi host followed by unauthorized shell commands or lateral remote logins from the ESXi host. |  |  |

---

## References

- [SSH.COM. (n.d.). SSH (Secure Shell). Retrieved March 23, 2020.](https://www.ssh.com/ssh)
- [Microsoft. (n.d.). Remote Desktop Services. Retrieved June 1, 2016.](https://technet.microsoft.com/en-us/windowsserver/ee236407.aspx)
- [Apple. (n.d.). Use MDM to enable Remote Management in macOS. Retrieved September 23, 2021.](https://support.apple.com/en-us/HT209161)
- [Apple. (n.d.). Use the kickstart command-line utility in Apple Remote Desktop. Retrieved September 23, 2021.](https://support.apple.com/en-us/HT201710)
- [Apple. (n.d.). Apple Remote Desktop Administrator Guide Version 3.3. Retrieved October 5, 2021.](https://images.apple.com/remotedesktop/pdf/ARD_Admin_Guide_v3.3.pdf)
- [Jake Nicastro, Willi Ballenthin. (2019, October 9). Living off the Orchard: Leveraging Apple Remote Desktop for Good and Evil. Retrieved August 16, 2021.](https://www.fireeye.com/blog/threat-research/2019/10/leveraging-apple-remote-desktop-for-good-and-evil.html)
- [Dan Borges. (2019, July 21). MacOS Red Teaming 206: ARD (Apple Remote Desktop Protocol). Retrieved September 10, 2021.](http://lockboxx.blogspot.com/2019/07/macos-red-teaming-206-ard-apple-remote.html)
- [CrowdStrike. (2023). 2022 Falcon OverWatch Threat Hunting Report. Retrieved May 20, 2024.](https://go.crowdstrike.com/rs/281-OBQ-266/images/2022OverWatchThreatHuntingReport.pdf)
- [Harbison, M. and Renals, P. (2022, July 5). When Pentest Tools Go Brutal: Red-Teaming Tool Being Abused by Malicious Actors. Retrieved February 1, 2023.](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
- [Microsoft Threat Intelligence. (2023, June 14). Cadet Blizzard emerges as a novel and distinct Russian threat actor. Retrieved July 10, 2023.](https://www.microsoft.com/en-us/security/blog/2023/06/14/cadet-blizzard-emerges-as-a-novel-and-distinct-russian-threat-actor/)
- [Bermejo, L., et al. (2017, June 22). Following the Trail of BlackTech’s Cyber Espionage Campaigns. Retrieved May 5, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [Alex Marvi, Greg Blaum, and Ron Craft. (2023, June 28). Detection, Containment, and Hardening Opportunities for Privileged Guest Operations, Anomalous Behavior, and VMCI Backdoors on Compromised VMware Hosts. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/vmware-detection-containment-hardening)
- [Broadcom. (2025, February 12). Enabling or disabling Lockdown mode on an ESXi host. Retrieved March 27, 2025.](https://knowledge.broadcom.com/external/article/336894/enabling-or-disabling-lockdown-mode-on-a.html)
- [Nital Ruzin and Omer Kidron. (2024, May 15). ESXi Ransomware Attacks: Evolution, Impact, and Defense Strategy. Retrieved April 4, 2025.](https://www.sygnia.co/blog/esxi-ransomware-attacks/)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[ShinyHunters]] [related_actor:: [[ShinyHunters]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025-2026 SaaS and Cloud Exploitation Wave]] [related_campaign:: [[2025-2026 SaaS and Cloud Exploitation Wave]]]

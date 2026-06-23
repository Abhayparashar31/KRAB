# User Execution

## Description

An adversary may rely upon specific actions by a user in order to gain execution. Users may be subjected to social engineering to get them to execute malicious code by, for example, opening a malicious document file or link. These user actions will typically be observed as follow-on behavior from forms of Phishing .

While User Execution frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after Internal Spearphishing .

Adversaries may also deceive users into performing actions such as:

For example, tech support scams can be facilitated through Phishing , vishing, or various forms of user interaction. Adversaries can use a combination of these methods, such as spoofing and promoting toll-free numbers or call centers that are used to direct victims to malicious websites, to deliver and execute payloads containing malware or Remote Access Tools . [5]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1004 | LAPSUS$ | LAPSUS$ has recruited target organization employees or contractors who provide credentials and approve an associated MFA prompt, or install remote management software onto a corporate workstation, allowing LAPSUS$ to take control of an authenticated system. [6] |
| S1213 | Lumma Stealer | Lumma Stealer has been distributed through a fake CAPTCHA that presents instructions to the victim to open Windows Run window ("Windows Button + R") and paste clipboard contents ("CTRL + V") and press "Enter" to execute a Base64-encoded PowerShell. [7] [8] [9] |
| S1130 | Raspberry Robin | Raspberry Robin execution can rely on users directly interacting with malicious LNK files. [10] |
| G1015 | Scattered Spider | Scattered Spider has impersonated organization IT and helpdesk staff to instruct victims to execute commercial remote access tools to gain initial access. [11] |
| C0037 | Water Curupira Pikabot Distribution | Water Curupira Pikabot Distribution requires users to interact with malicious attachments in order to start Pikabot installation. [12] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1040 | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent executable files from running unless they meet a prevalence, age, or trusted list criteria and to prevent Office applications from creating potentially malicious executable content by blocking malicious code from being written to disk. Note: cloud-delivered protection must be enabled to use certain rules. [13] |
| M1038 | Execution Prevention | Application control may be able to prevent the running of executables masquerading as other files. |
| M1033 | Limit Software Installation | Where possible, consider requiring developers to pull from internal repositories containing verified and approved packages rather than from external ones. |
| M1031 | Network Intrusion Prevention | If a link is being visited by a user, network intrusion prevention systems and systems designed to scan and remove malicious downloads can be used to block activity. |
| M1021 | Restrict Web-Based Content | If a link is being visited by a user, block unknown or unused files in transit by default that should not be downloaded or by policy from suspicious sites as a best practice to prevent some vectors, such as .scr, .exe, .pif, .cpl, etc. Some download scanning devices can open and analyze compressed and encrypted formats, such as zip and rar that may be used to conceal malicious files. |
| M1017 | User Training | Use user training as a way to bring awareness to common phishing and spearphishing techniques and how to raise suspicion for potentially malicious events. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0478 | User Execution – multi-surface behavior chain (documents/links → helper/unpacker → LOLBIN/child → egress) | AN1314 | Cause→effect chain: (1) User-facing app (Office/PDF/archiver/browser) records an open/click or abnormal event, then (2) a downloaded file is created in a user-writable path and/or decompressed, (3) the parent user app spawns a living-off-the-land binary (e.g., powershell/cmd/mshta/rundll32/msiexec/wscript/expand/zip) or installer, and (4) immediate outbound HTTP(S)/DNS/SMB from the same lineage. |
| AN1315 | Cause→effect chain: (1) User app/browser/archiver logs an open/click or abnormal exit, (2) new executable/script/archive extracted into $HOME/Downloads, /tmp, or ~/.cache, (3) parent app spawns shell/interpreter (bash/sh/python/node/curl/wget) or desktop file, and (4) new outbound connection(s) from the child lineage. |  |  |
| AN1316 | Cause→effect chain: (1) unified logs show application open/click or crash for Safari/Chrome/Office/Preview/archiver, (2) file write/extraction into ~/Downloads, /private/var/folders/* or ~/Library, (3) parent app spawns osascript/bash/zsh/curl/python or opens a quarantined app with Gatekeeper prompts, (4) network egress from child. |  |  |
| AN1317 | Cause→effect chain in CI/dev desktops: (1) user triggers container run/pull after opening a doc/link/script, (2) newly created image/container uses unexpected external registry or entrypoint, (3) container starts and immediately egresses to suspicious destinations. |  |  |
| AN1318 | Cause→effect chain in cloud consoles: (1) user clicks link then invokes instance/image creation via API, (2) instance/image originates from external AMI or unknown image, (3) instance immediately egresses or retrieves payloads. |  |  |

---

## References

- [Tiago Pereira. (2023, November 2). Attackers use JavaScript URLs, API forms and more to scam users in popular online game “Roblox”. Retrieved January 2, 2024.](https://blog.talosintelligence.com/roblox-scam-overview/)
- [Brian Krebs. (2023, May 30). Discord Admins Hacked by Malicious Bookmarks. Retrieved January 2, 2024.](https://krebsonsecurity.com/2023/05/discord-admins-hacked-by-malicious-bookmarks/)
- [Reliaquest. (2024, May 31). New Execution Technique in ClearFake Campaign. Retrieved August 2, 2024.](https://www.reliaquest.com/blog/new-execution-technique-in-clearfake-campaign/)
- [Tommy Madjar, Dusty Miller, Selena Larson. (2024, June 17). From Clipboard to Compromise: A PowerShell Self-Pwn. Retrieved August 2, 2024.](https://www.proofpoint.com/us/blog/threat-insight/clipboard-compromise-powershell-self-pwn)
- [Selena Larson, Sam Scholten, Timothy Kromphardt. (2021, November 4). Caught Beneath the Landline: A 411 on Telephone Oriented Attack Delivery. Retrieved January 5, 2022.](https://www.proofpoint.com/us/blog/threat-insight/caught-beneath-landline-411-telephone-oriented-attack-delivery)
- [MSTIC, DART, M365 Defender. (2022, March 24). DEV-0537 Criminal Actor Targeting Organizations for Data Exfiltration and Destruction. Retrieved May 17, 2022.](https://www.microsoft.com/security/blog/2022/03/22/dev-0537-criminal-actor-targeting-organizations-for-data-exfiltration-and-destruction/)
- [Vishwajeet Kumar, Qualys. (2024, October 20). Unmasking Lumma Stealer: Analyzing Deceptive Tactics with Fake CAPTCHA. Retrieved March 22, 2025.](https://blog.qualys.com/vulnerabilities-threat-research/2024/10/20/unmasking-lumma-stealer-analyzing-deceptive-tactics-with-fake-captcha)
- [Cybereaon Security Services Team. (n.d.). Your Data Is Under New Lummanagement: The Rise of LummaStealer. Retrieved March 22, 2025.](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)
- [Leandro Fróes, Netskope. (2025, January 23). Lumma Stealer: Fake CAPTCHAs & New Techniques to Evade Detection. Retrieved March 22, 2025.](https://www.netskope.com/blog/lumma-stealer-fake-captchas-new-techniques-to-evade-detection)
- [Microsoft Threat Intelligence. (2022, October 27). Raspberry Robin worm part of larger ecosystem facilitating pre-ransomware activity. Retrieved May 17, 2024.](https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/)
- [CISA. (2023, November 16). Cybersecurity Advisory: Scattered Spider (AA23-320A). Retrieved March 18, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)
- [Shinji Robert Arasawa, Joshua Aquino, Charles Steven Derion, Juhn Emmanuel Atanque, Francisrey Joshua Castillo, John Carlo Marquez, Henry Salcedo, John Rainier Navato, Arianne Dela Cruz, Raymart Yambot & Ian Kenefick. (2024, January 9). Black Basta-Affiliated Water Curupira’s Pikabot Spam Campaign. Retrieved July 17, 2024.](https://www.trendmicro.com/en_us/research/24/a/a-look-into-pikabot-spam-wave-campaign.html)
- [Microsoft. (2021, July 2). Use attack surface reduction rules to prevent malware infection. Retrieved June 24, 2021.](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)

---

# Steal Web Session Cookie

## Description

An adversary may steal web application or service session cookies and use them to gain access to web applications or Internet services as an authenticated user without needing credentials. Web applications and services often use session cookies as an authentication token after a user has authenticated to a website.

Cookies are often valid for an extended period of time, even if the web application is not actively used. Cookies can be found on disk, in the process memory of the browser, and in network traffic to remote systems. Additionally, other applications on the targets machine might store sensitive authentication cookies in memory (e.g. apps which authenticate to cloud services). Session cookies can be used to bypasses some multi-factor authentication protocols. [1]

There are several examples of malware targeting cookies from web browsers on the local system. [2] [3] Adversaries may also steal cookies by injecting malicious JavaScript content into websites or relying on User Execution by tricking victims into running malicious JavaScript in their browser. [4] [5]

There are also open source frameworks such as Evilginx2 and Muraena that can gather session cookies through a malicious proxy (e.g., Adversary-in-the-Middle ) that can be set up by an adversary and used in phishing campaigns. [6] [7]

After an adversary acquires a valid cookie, they can then perform a Web Session Cookie technique to login to the corresponding web application.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1044 | APT42 | APT42 has used custom malware to steal login and cookie data from common browsers. [8] |
| S0657 | BLUELIGHT | BLUELIGHT can harvest cookies from Internet Explorer, Edge, Chrome, and Naver Whale browsers. [9] |
| S0631 | Chaes | Chaes has used a script that extracts the web session cookie and sends it to the C2 server. [10] |
| S0492 | CookieMiner | CookieMiner can steal Google Chrome and Apple Safari browser cookies from the victim’s machine. [11] |
| S1111 | DarkGate | DarkGate attempts to steal Opera cookies, if present, after terminating the related process. [12] |
| S9003 | evilginx2 | evilginx2 can collect information on each session with a victim including the session cookie. [13] [14] |
| S0568 | EVILNUM | EVILNUM can harvest cookies and upload them to the C2 server. [15] |
| G0120 | Evilnum | Evilnum can steal cookies and session information from browsers. [16] |
| S9010 | GlassWorm | GlassWorm has harvested Safari cookies stored within /Library/Containers/com.apple.Safari/Data/Library/Cookies/ Cookies.binarycookies . [17] GlassWorm has also stolen cookies within Chromium and Firefox browsers. [18] [17] |
| S0531 | Grandoreiro | Grandoreiro can steal the victim's cookies to use for duplicating the active session from another device. [19] |
| G0094 | Kimsuky | Kimsuky has used malware, such as TRANSLATEXT , to steal and exfiltrate browser cookies. [20] [21] |
| S9020 | LODEINFO | LODEINFO can list the contents of %LocalAppData%\Google\Chrome\User Data\ and %LocalAppData%\Microsoft\Edge\User Data\ to obtain cookies. [22] |
| G0030 | Lotus Blossom | Lotus Blossom has used publicly-available tools to steal cookies from browsers such as Chrome. [23] |
| G1014 | LuminousMoth | LuminousMoth has used an unnamed post-exploitation tool to steal cookies from the Chrome browser. [24] |
| S1213 | Lumma Stealer | Lumma Stealer has harvested cookies from various browsers. [25] [26] [27] |
| S1146 | MgBot | MgBot includes modules that can steal cookies from Firefox, Chrome, and Edge web browsers. [28] |
| S0650 | QakBot | QakBot has the ability to capture web session cookies. [29] [30] |
| S1148 | Raccoon Stealer | Raccoon Stealer attempts to steal cookies and related information in browser history. [31] |
| S1240 | RedLine Stealer | RedLine Stealer has stolen browser cookies and settings. [32] [33] [34] [35] |
| G0034 | Sandworm Team | Sandworm Team used information stealer malware to collect browser session cookies. [36] |
| G1015 | Scattered Spider | Scattered Spider retrieves browser cookies via Raccoon Stealer. [37] |
| C0024 | SolarWinds Compromise | During the SolarWinds Compromise , APT29 stole Chrome browser cookies by copying the Chrome profile directories of targeted users. [38] |
| S1140 | Spica | Spica has the ability to steal cookies from Chrome, Firefox, Opera, and Edge browsers. [39] |
| G1033 | Star Blizzard | Star Blizzard has used EvilGinx to steal the session cookies of victims directed to phishing domains. [40] |
| S0467 | TajMahal | TajMahal has the ability to steal web session cookies from Internet Explorer, Netscape Navigator, FireFox and RealNetworks applications. [2] |
| S1201 | TRANSLATEXT | TRANSLATEXT has exfiltrated updated cookies from Google, Naver, Kakao or Daum to the C2 server. [20] |
| S0658 | XCSSET | XCSSET uses scp to access the ~/Library/Cookies/Cookies.binarycookies file. [41] |
| S1207 | XLoader | XLoader can capture web session cookies and session information from victim browsers. [42] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1047 | Audit | Implement auditing for authentication activities and user logins to detect the use of stolen session cookies. Monitor for impossible travel scenarios and anomalous behavior that could indicate the use of compromised session tokens or cookies. |
| M1032 | Multi-factor Authentication | Deploy hardware-based token (e.g., YubiKey or FIDO key), which incorporates the target login domain as part of the negotiation protocol, will prevent session cookie theft through proxy methods. Implement Conditional Access policies to only allow logins from trusted devices, such as those enrolled in Intune or joined via Hybrid/Entra. This mitigates the risk of session cookie replay attacks by ensuring that stolen tokens cannot be reused on unauthorized devices. |
| M1021 | Restrict Web-Based Content | Restrict or block web-based content that could be used to extract session cookies or credentials stored in browsers. Use browser security settings, such as disabling third-party cookies and restricting browser extensions, to limit the attack surface. |
| M1054 | Software Configuration | Configure browsers or tasks to regularly delete persistent cookies. Additionally, minimize the length of time a web cookie is viable to potentially reduce the impact of stolen cookies while also increasing the needed frequency of cookie theft attempts – providing defenders with additional chances at detection. [43] For example, use non-persistent cookies to limit the duration a session ID will remain on the web client cache where an attacker could obtain it. [44] |
| M1051 | Update Software | Regularly update web browsers, password managers, and all related software to the latest versions. Keeping software up-to-date reduces the risk of vulnerabilities being exploited by attackers to extract stored credentials or session cookies. |
| M1017 | User Training | Train users to identify aspects of phishing attempts where they're asked to enter credentials into a site that has the incorrect domain for the application they are logging into. Additionally, train users not to run untrusted JavaScript in their browser, such as by copying and pasting code or dragging and dropping bookmarklets. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0509 | Detection of Web Session Cookie Theft via File, Memory, and Network Artifacts | AN1402 | Detects suspicious access to browser session cookie storage (e.g., Chrome’s Cookies SQLite DB) or memory reads of browser processes. Anomalous injection or memory dump utilities targeting browser processes such as chrome.exe , firefox.exe , or msedge.exe . |
| AN1403 | Detects access to known browser cookie files (e.g., ~/.mozilla/firefox/*.default/cookies.sqlite , ~/.config/google-chrome/ ) and suspicious reads of browser memory via /proc/[pid]/mem or ptrace. |  |  |
| AN1404 | Detects unauthorized access to browser cookie paths (e.g., ~/Library/Application Support/Google/Chrome/Default/Cookies ) or task_for_pid / vm_read calls to Safari/Chrome memory space. |  |  |
| AN1405 | Detects automation macros or VBA scripts in documents that access browser file paths, read cookie data, or attempt to exfiltrate browser session tokens over HTTP. |  |  |
| AN1406 | Detects use of session cookies or authentication tokens from unusual user agents or locations. Identifies token reuse without reauthentication or attempts to bypass MFA using previously stolen cookies. |  |  |

---

## References

- [Rehberger, J. (2018, December). Pivot to the Cloud using Pass the Cookie. Retrieved April 5, 2019.](https://wunderwuzzi23.github.io/blog/passthecookie.html)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Chen, Y., Hu, W., Xu, Z., et. al. (2019, January 31). Mac Malware Steals Cryptocurrency Exchanges’ Cookies. Retrieved October 14, 2019.](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
- [Tiago Pereira. (2023, November 2). Attackers use JavaScript URLs, API forms and more to scam users in popular online game “Roblox”. Retrieved January 2, 2024.](https://blog.talosintelligence.com/roblox-scam-overview/)
- [Brian Krebs. (2023, May 30). Discord Admins Hacked by Malicious Bookmarks. Retrieved January 2, 2024.](https://krebsonsecurity.com/2023/05/discord-admins-hacked-by-malicious-bookmarks/)
- [Gretzky, Kuba. (2019, April 10). Retrieved October 8, 2019.](https://github.com/kgretzky/evilginx2)
- [Orrù, M., Trotta, G.. (2019, September 11). Muraena. Retrieved October 14, 2019.](https://github.com/muraenateam/muraena)
- [Mandiant. (n.d.). APT42: Crooked Charms, Cons and Compromises. Retrieved October 9, 2024.](https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf)
- [Cash, D., Grunzweig, J., Meltzer, M., Adair, S., Lancaster, T. (2021, August 17). North Korean APT InkySquid Infects Victims Using Browser Exploits. Retrieved September 30, 2021.](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
- [Salem, E. (2020, November 17). CHAES: Novel Malware Targeting Latin American E-Commerce. Retrieved June 30, 2021.](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
- [Chen, y., et al. (2019, January 31). Mac Malware Steals Cryptocurrency Exchanges’ Cookies. Retrieved July 22, 2020.](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
- [McGraw, T. (2024, December 4). Black Basta Ransomware Campaign Drops Zbot, DarkGate, and Custom Malware. Retrieved December 9, 2024.](https://www.rapid7.com/blog/post/2024/12/04/black-basta-ransomware-campaign-drops-zbot-darkgate-and-custom-malware/)
- [Gretzky, K.. (2018, July 26). Evilginx 2 - Next Generation of Phishing 2FA Tokens. Retrieved October 14, 2019.](https://breakdev.org/evilginx-2-next-generation-of-phishing-2fa-tokens/)
- [Everts, M. (2025, March 28). Stealing user credentials with evilginx. Retrieved January 27, 2026.](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)
- [Adamitis, D. (2020, May 6). Phantom in the Command Shell. Retrieved November 17, 2024.](https://web.archive.org/web/20221209052853/https://www.prevailion.com/phantom-in-the-command-shell-2/)
- [Porolli, M. (2020, July 9). More evil: A deep look at Evilnum and its toolset. Retrieved January 22, 2021.](https://www.welivesecurity.com/2020/07/09/more-evil-deep-look-evilnum-toolset/)
- [Kirill Boychenko. (2026, January 31). GlassWorm Loader Hits Open VSX via Developer Account Compromise. Retrieved April 10, 2026.](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
- [Gal Hachamov. (2025, December 29). GlassWorm Goes Mac: Fresh Infrastructure, New Tricks. Retrieved April 10, 2026.](https://www.koi.ai/blog/glassworm-goes-mac-fresh-infrastructure-new-tricks)
- [Abramov, D. (2020, April 13). Grandoreiro Malware Now Targeting Banks in Spain. Retrieved November 12, 2020.](https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/)
- [Park, S. (2024, June 27). Kimsuky deploys TRANSLATEXT to target South Korean academia. Retrieved October 14, 2024.](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
- [Jiho Kim & Sebin Lee, S2W. (2024, February 7). Kimsuky disguised as a Korean company signed with a valid certificate to distribute Troll Stealer (English ver.). Retrieved January 17, 2025.](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
- [Breitenbacher, D. (2022, December 14). Unmasking MirrorFace: Operation LiberalFace targeting Japanese political entities. Retrieved April 17, 2026.](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [Lechtik, M, and etl. (2021, July 14). LuminousMoth APT: Sweeping attacks for the chosen few. Retrieved October 20, 2022.](https://securelist.com/apt-luminousmoth/103332/)
- [Cybereaon Security Services Team. (n.d.). Your Data Is Under New Lummanagement: The Rise of LummaStealer. Retrieved March 22, 2025.](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)
- [Cara Lin, Fortinet. (2024, January 8). Deceptive Cracked Software Spreads Lumma Variant on YouTube. Retrieved March 22, 2025.](https://www.fortinet.com/blog/threat-research/lumma-variant-on-youtube)
- [Buddy Tancio, Fe Cureg, and Jovit Samaniego, Trend Micro. (2025, January 30). Lumma Stealer’s GitHub-Based Delivery Explored via Managed Detection and Response. Retrieved March 22, 2025.](https://www.trendmicro.com/en_us/research/25/a/lumma-stealers-github-based-delivery-via-mdr.html)
- [Facundo Muñoz. (2023, April 26). Evasive Panda APT group delivers malware via updates for popular Chinese software. Retrieved July 25, 2024.](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)
- [Sette, N. et al. (2020, June 4). Qakbot Malware Now Exfiltrating Emails for Sophisticated Thread Hijacking Attacks. Retrieved September 27, 2021.](https://www.kroll.com/en/insights/publications/cyber/qakbot-malware-exfiltrating-emails-thread-hijacking-attacks)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [Pierre Le Bourhis, Quentin Bourgue, & Sekoia TDR. (2022, June 29). Raccoon Stealer v2 - Part 2: In-depth analysis. Retrieved August 1, 2024.](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
- [Alexandre Cote Cyr. (2024, November 8). Life on a crooked RedLine: Analyzing the infamous infostealer’s backend. Retrieved September 17, 2025.](https://www.welivesecurity.com/en/eset-research/life-crooked-redline-analyzing-infamous-infostealers-backend/)
- [George Glass. (2024, August 14). REDLINESTEALER Malware Driving the Initial Access Broker Market. Retrieved September 17, 2025.](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
- [Proofpoint Threat Insight Team, Jeremy H, Axel F. (2020, March 16). New Redline Password Stealer Malware. Retrieved September 17, 2025.](https://www.proofpoint.com/us/blog/threat-insight/new-redline-stealer-distributed-using-coronavirus-themed-email-campaign)
- [Splunk Threat Research Team. (2023, June 1). Do Not Cross The 'RedLine' Stealer: Detections and Analysis. Retrieved September 17, 2025.](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
- [Billy Leonard. (2023, April 19). Ukraine remains Russia’s biggest cyber focus in 2023. Retrieved March 1, 2024.](https://blog.google/threat-analysis-group/ukraine-remains-russias-biggest-cyber-focus-in-2023/)
- [CISA. (2023, November 16). Cybersecurity Advisory: Scattered Spider (AA23-320A). Retrieved March 18, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)
- [CrowdStrike. (2022, January 27). Early Bird Catches the Wormhole: Observations from the StellarParticle Campaign. Retrieved February 7, 2022.](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)
- [Shields, W. (2024, January 18). Russian threat group COLDRIVER expands its targeting of Western officials to include the use of malware. Retrieved June 13, 2024.](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/)
- [CISA, et al. (2023, December 7). Russian FSB Cyber Actor Star Blizzard Continues Worldwide Spear-phishing Campaigns. Retrieved June 13, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-341a)
- [Mac Threat Response, Mobile Research Team. (2020, August 13). The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSS Backdoor Planting in Safari, and Leverages Two Zero-day Exploits. Retrieved October 5, 2021.](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
- [Nart Villeneuve, Randi Eitzman, Sandor Nemes & Tyler Dean, Google Cloud. (2017, October 5). Significant FormBook Distribution Campaigns Impacting the U.S. and South Korea. Retrieved March 11, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)
- [Microsoft Incident Response. (2022, November 16). Token tactics: How to prevent, detect, and respond to cloud token theft. Retrieved December 26, 2023.](https://www.microsoft.com/en-us/security/blog/2022/11/16/token-tactics-how-to-prevent-detect-and-respond-to-cloud-token-theft/)
- [OWASP CheatSheets Series Team. (n.d.). Session Management Cheat Sheet. Retrieved December 26, 2023.](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

---


### 🔗 KRAB Intelligence Correlation
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025-2026 SaaS Identity Crisis and Help Desk Exploitation Wave]] [related_campaign:: [[2025-2026 SaaS Identity Crisis and Help Desk Exploitation Wave]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2026 Oracle PeopleSoft Mass Data Theft Campaign]] [related_campaign:: [[2026 Oracle PeopleSoft Mass Data Theft Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[Zendesk Typosquatting and Phishing Campaign]] [related_campaign:: [[Zendesk Typosquatting and Phishing Campaign]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Scattered Lapsus$ Hunters]] [related_actor:: [[Scattered Lapsus$ Hunters]]]
- 🦠 **Tooling Capability Integration:** Executed via malware family [[Lumma Stealer]] [related_malware:: [[Lumma Stealer]]]

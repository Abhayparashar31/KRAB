# Browser Session Hijacking

## Description

Adversaries may take advantage of security vulnerabilities and inherent functionality in browser software to change content, modify user-behaviors, and intercept information as part of various browser session hijacking techniques. [1]

A specific example is when an adversary injects software into a browser that allows them to inherit cookies, HTTP sessions, and SSL client certificates of a user then use the browser as a way to pivot into an authenticated intranet. [2] [3] Executing browser-based behaviors such as pivoting may require specific process permissions, such as SeDebugPrivilege and/or high-integrity/administrator rights.

Another example involves pivoting browser traffic from the adversary's browser through the user's browser by setting up a proxy which will redirect web traffic. This does not alter the user's traffic in any way, and the proxy connection can be severed as soon as the browser is closed. The adversary assumes the security context of whichever browser process the proxy is injected into. Browsers typically create a new process for each tab that is opened and permissions and certificates are separated accordingly. With these permissions, an adversary could potentially browse to any resource on an intranet, such as Sharepoint or webmail, that is accessible through the browser and which the browser has sufficient permissions. Browser pivoting may also bypass security provided by 2-factor authentication. [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0331 | Agent Tesla | Agent Tesla has the ability to use form-grabbing to extract data from web data forms. [5] |
| S0484 | Carberp | Carberp has captured credentials when a user performs login through a SSL session. [6] [7] |
| S0631 | Chaes | Chaes has used the Puppeteer module to hook and monitor the Chrome web browser to collect user information from infected hosts. [8] |
| S0154 | Cobalt Strike | Cobalt Strike can perform browser pivoting and inject into a user's browser to inherit cookies, authenticated HTTP sessions, and client SSL certificates. [4] [9] |
| S0384 | Dridex | Dridex can perform browser attacks via web injects to steal information such as credentials, certificates, and cookies. [10] |
| S9003 | evilginx2 | evilginx2 can inject custom POST arguments into requests to silently enable "Remember Me" options during authentication to stay logged in across browser sessions. [11] |
| S0531 | Grandoreiro | Grandoreiro can monitor browser activity for online banking actions and display full-screen overlay images to block user access to the intended site or present additional data fields. [12] [13] [14] |
| S0483 | IcedID | IcedID has used web injection attacks to redirect victims to spoofed sites designed to harvest banking and other credentials. IcedID can use a self signed TLS certificate in connection with the spoofed site and simultaneously maintains a live connection with the legitimate site to display the correct URL and certificates in the browser. [15] [16] |
| G0094 | Kimsuky | Kimsuky has the ability to use form-grabbing to extract emails and passwords from web data forms. [17] |
| S0530 | Melcoz | Melcoz can monitor the victim's browser for online banking sessions and display an overlay window to manipulate the session in the background. [12] |
| S0650 | QakBot | QakBot can use advanced web injects to steal web banking credentials. [18] [19] |
| S1201 | TRANSLATEXT | TRANSLATEXT has the ability to use form-grabbing and event-listening to extract data from web data forms. [17] |
| S0266 | TrickBot | TrickBot uses web injects and browser redirection to trick the user into providing their login credentials on a fake or modified web page. [20] [21] [22] [23] |
| S0386 | Ursnif | Ursnif has injected HTML codes into banking sites to steal sensitive online banking information (ex: usernames and passwords). [24] |
| S1207 | XLoader | XLoader can conduct form grabbing, steal cookies, and extract data from HTTP sessions. [25] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1018 | User Account Management | Since browser pivoting requires a high integrity process to launch from, restricting user permissions and addressing Privilege Escalation and Bypass User Account Control opportunities can limit the exposure to this technique. |
| M1017 | User Training | Close all browser sessions regularly and when they are no longer needed. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0507 | Detect browser session hijacking via privilege, handle access, and remote thread into browsers | AN1398 | Adversary gains high integrity or special privileges (e.g., SeDebugPrivilege), locates a running browser process, opens it with write/inject rights, and modifies it (e.g., CreateRemoteThread / DLL load) to inherit cookies/tokens or establish a browser pivot. Optional step: create a new logon session or use explicit credentials, then drive the victim browser to intranet resources. |

---

## References

- [Wikipedia. (2017, October 28). Man-in-the-browser. Retrieved January 10, 2018.](https://en.wikipedia.org/wiki/Man-in-the-browser)
- [Mudge, R. (n.d.). Browser Pivoting. Retrieved January 10, 2018.](https://www.cobaltstrike.com/help-browser-pivoting)
- [De Tore, M., Warner, J. (2018, January 15). MALICIOUS CHROME EXTENSIONS ENABLE CRIMINALS TO IMPACT OVER HALF A MILLION USERS AND GLOBAL BUSINESSES. Retrieved January 17, 2018.](https://www.icebrg.io/blog/malicious-chrome-extensions-enable-criminals-to-impact-over-half-a-million-users-and-global-businesses)
- [Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
- [Arsene, L. (2020, April 21). Oil & Gas Spearphishing Campaigns Drop Agent Tesla Spyware in Advance of Historic OPEC+ Deal. Retrieved May 19, 2020.](https://labs.bitdefender.com/2020/04/oil-gas-spearphishing-campaigns-drop-agent-tesla-spyware-in-advance-of-historic-opec-deal/)
- [Giuliani, M., Allievi, A. (2011, February 28). Carberp - a modular information stealing trojan. Retrieved September 12, 2024.](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
- [Trusteer Fraud Prevention Center. (2010, October 7). Carberp Under the Hood of Carberp: Malware & Configuration Analysis. Retrieved July 15, 2020.](https://web.archive.org/web/20111004014029/http://www.trusteer.com/sites/default/files/Carberp_Analysis.pdf)
- [Salem, E. (2020, November 17). CHAES: Novel Malware Targeting Latin American E-Commerce. Retrieved June 30, 2021.](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, October 13). Dridex (Bugat v5) Botnet Takeover Operation. Retrieved May 31, 2019.](https://www.secureworks.com/research/dridex-bugat-v5-botnet-takeover-operation)
- [Gretzky, K. (2018, November 22). Evilginx 2.2 - Jolly Winter Update. Retrieved January 27, 2026.](https://breakdev.org/evilginx-2-2-jolly-winter-update)
- [GReAT. (2020, July 14). The Tetrade: Brazilian banking malware goes global. Retrieved November 9, 2020.](https://securelist.com/the-tetrade-brazilian-banking-malware/97779/)
- [Abramov, D. (2020, April 13). Grandoreiro Malware Now Targeting Banks in Spain. Retrieved November 12, 2020.](https://securityintelligence.com/posts/grandoreiro-malware-now-targeting-banks-in-spain/)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [Kessem, L., et al. (2017, November 13). New Banking Trojan IcedID Discovered by IBM X-Force Research. Retrieved July 14, 2020.](https://securityintelligence.com/new-banking-trojan-icedid-discovered-by-ibm-x-force-research/)
- [Kimayong, P. (2020, June 18). COVID-19 and FMLA Campaigns used to install new IcedID banking malware. Retrieved July 14, 2020.](https://blogs.juniper.net/en-us/threat-research/covid-19-and-fmla-campaigns-used-to-install-new-icedid-banking-malware)
- [Park, S. (2024, June 27). Kimsuky deploys TRANSLATEXT to target South Korean academia. Retrieved October 14, 2024.](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
- [Cyberint. (2021, May 25). Qakbot Banking Trojan. Retrieved September 27, 2021.](https://blog.cyberint.com/qakbot-banking-trojan)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [Reaves, J. (2016, October 15). TrickBot: We Missed you, Dyre. Retrieved August 2, 2018.](https://www.fidelissecurity.com/threatgeek/2016/10/trickbot-we-missed-you-dyre)
- [Keshet, L. (2016, November 09). Tricks of the Trade: A Deeper Look Into TrickBot’s Machinations. Retrieved August 2, 2018.](https://securityintelligence.com/tricks-of-the-trade-a-deeper-look-into-trickbots-machinations/)
- [Pornasdoro, A. (2017, October 12). Trojan:Win32/Totbrick. Retrieved September 14, 2018.](https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=Trojan:Win32/Totbrick)
- [Anthony, N., Pascual, C.. (2018, November 1). Trickbot Shows Off New Trick: Password Grabber Module. Retrieved November 16, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)
- [Sioting, S. (2013, June 15). BKDR_URSNIF.SM. Retrieved June 5, 2019.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
- [Nart Villeneuve, Randi Eitzman, Sandor Nemes & Tyler Dean, Google Cloud. (2017, October 5). Significant FormBook Distribution Campaigns Impacting the U.S. and South Korea. Retrieved March 11, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)

---

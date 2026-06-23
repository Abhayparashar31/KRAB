# Scheduled Transfer

## Description

Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain intervals. This could be done to blend traffic patterns with normal activity or availability.

When scheduled exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out of the network, such as Exfiltration Over C2 Channel or Exfiltration Over Alternative Protocol .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0045 | ADVSTORESHELL | ADVSTORESHELL collects, compresses, encrypts, and exfiltrates data to the C2 server every 10 minutes. [1] |
| S0667 | Chrommme | Chrommme can set itself to sleep before requesting a new command from C2. [2] |
| S0154 | Cobalt Strike | Cobalt Strike can set its Beacon payload to reach out to the C2 server on an arbitrary and random interval. [3] |
| S0126 | ComRAT | ComRAT has been programmed to sleep outside local business hours (9 to 5, Monday to Friday). [4] |
| S0200 | Dipsind | Dipsind can be configured to only run during normal working hours, which would make its communications harder to distinguish from normal traffic. [5] |
| S0696 | Flagpro | Flagpro has the ability to wait for a specified time interval between communicating with and executing commands from C2. [6] |
| G0126 | Higaisa | Higaisa sent the victim computer identifier in a User-Agent string back to the C2 server every 10 minutes. [7] |
| S0283 | jRAT | jRAT can be configured to reconnect at certain intervals. [8] |
| S0265 | Kazuar | Kazuar can sleep for a specific time and be set to communicate at specific intervals. [9] |
| S0395 | LightNeuron | LightNeuron can be configured to exfiltrate data during nighttime or working hours. [10] |
| S0211 | Linfo | Linfo creates a backdoor through which remote attackers can change the frequency at which compromised hosts contact remote C2 infrastructure. [11] |
| S0409 | Machete | Machete sends stolen data to the C2 server every 10 minutes. [12] |
| S1100 | Ninja | Ninja can configure its agent to work only in specific time frames. [13] |
| S0223 | POWERSTATS | POWERSTATS can sleep for a given number of seconds. [14] |
| S0596 | ShadowPad | ShadowPad has sent data back to C2 every 8 hours. [15] |
| S1019 | Shark | Shark can pause C2 communications for a specified time. [16] |
| S0444 | ShimRat | ShimRat can sleep when instructed to do so by the C2. [17] |
| S0668 | TinyTurla | TinyTurla contacts its C2 based on a scheduled timing set in its configuration. [18] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1031 | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. Signatures are often for unique indicators within protocols and may be based on the specific obfuscation technique used by a particular adversary or tool, and will likely be different across various malware families and versions. Adversaries will likely change tool command and control signatures over time or construct protocols in such a way to avoid detection by common defensive tools. [19] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0399 | Detection Strategy for Scheduled Transfer and Recurrent Exfiltration Patterns | AN1118 | Recurring network exfiltration initiated by scheduled or script-based processes exhibiting time-based regularity and consistent external destinations. |
| AN1119 | Detection of cron-based or script-based recurring transfers where the same script, user, or destination reappears at predictable intervals. |  |  |
| AN1120 | LaunchAgent or launchd recurring jobs initiating data transfer to consistent external IPs or domains with repeat timing signatures. |  |  |

---

## References

- [ESET. (2016, October). En Route with Sednit - Part 2: Observing the Comings and Goings. Retrieved November 21, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Strategic Cyber LLC. (2017, March 14). Cobalt Strike Manual. Retrieved May 24, 2017.](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [PT ESC Threat Intelligence. (2020, June 4). COVID-19 and New Year greetings: an investigation into the tools and methods used by the Higaisa group. Retrieved March 2, 2021.](https://www.ptsecurity.com/ww-en/analytics/pt-esc-threat-intelligence/covid-19-and-new-year-greetings-the-higaisa-group/)
- [Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [Faou, M. (2019, May). Turla LightNeuron: One email away from remote code execution. Retrieved June 24, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
- [Zhou, R. (2012, May 15). Backdoor.Linfo. Retrieved February 23, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-051605-2535-99)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
- [GReAT. (2017, August 15). ShadowPad in corporate networks. Retrieved March 22, 2021.](https://securelist.com/shadowpad-in-corporate-networks/81432/)
- [ClearSky Cyber Security . (2021, August). New Iranian Espionage Campaign By “Siamesekitten” - Lyceum. Retrieved June 6, 2022.](https://www.clearskysec.com/siamesekitten/)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Cisco Talos. (2021, September 21). TinyTurla - Turla deploys new malware to keep a secret backdoor on victim machines. Retrieved December 2, 2021.](https://blog.talosintelligence.com/2021/09/tinyturla.html)
- [Gardiner, J., Cova, M., Nagaraja, S. (2014, February). Command & Control Understanding, Denying and Detecting. Retrieved April 20, 2016.](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)

---

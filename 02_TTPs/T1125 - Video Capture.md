# Video Capture

## Description

An adversary can leverage a computer's peripheral devices (e.g., integrated cameras or webcams) or applications (e.g., video call services) to capture video recordings for the purpose of gathering information. Images may also be captured from devices or applications, potentially in specified intervals, in lieu of video files.

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture video or images. Video or image files may be written to disk and exfiltrated later. This technique differs from Screen Capture due to use of specific devices or applications for video recording rather than capturing the victim's screen.

In macOS, there are a few different malware samples that record the user's webcam such as FruitFly and Proton. [1]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0331 | Agent Tesla | Agent Tesla can access the victim’s webcam and record video. [2] [3] |
| S1087 | AsyncRAT | AsyncRAT can record screen content on targeted systems. [4] |
| S0234 | Bandook | Bandook has modules that are capable of capturing video from a victim's webcam. [5] |
| S0660 | Clambling | Clambling can record screen content in AVI format. [6] [7] |
| S0338 | Cobian RAT | Cobian RAT has a feature to access the webcam on the victim’s machine. [8] |
| S0591 | ConnectWise | ConnectWise can record video on remote hosts. [9] |
| S0115 | Crimson | Crimson can capture webcam video on targeted systems. [10] [11] |
| S0334 | DarkComet | DarkComet can access the victim’s webcam to take pictures. [12] [13] |
| S0021 | Derusbi | Derusbi is capable of capturing video. [14] |
| G1003 | Ember Bear | Ember Bear has exfiltrated images from compromised IP cameras. [15] |
| S0363 | Empire | Empire can capture webcam data on Windows and macOS systems. [16] |
| S0152 | EvilGrab | EvilGrab has the capability to capture video from a victim machine. [17] |
| G0046 | FIN7 | FIN7 created a custom video recording capability that could be used to monitor operations in the victim's environment. [18] [19] |
| S0434 | Imminent Monitor | Imminent Monitor has a remote webcam monitoring capability. [20] [21] |
| S0260 | InvisiMole | InvisiMole can remotely activate the victim’s webcam to capture content. [22] [23] |
| S0283 | jRAT | jRAT has the capability to capture video from a webcam. [24] [25] |
| S0265 | Kazuar | Kazuar captures images from the webcam. [26] |
| S0409 | Machete | Machete takes photos from the computer’s web camera. [27] [28] [29] |
| S0336 | NanoCore | NanoCore can access the victim's webcam and capture data. [30] [31] |
| S0385 | njRAT | njRAT can access the victim's webcam. [32] [33] |
| S0644 | ObliqueRAT | ObliqueRAT can capture images from webcams on compromised hosts. [34] |
| S1050 | PcShare | PcShare can capture camera video as part of its collection process. [35] |
| S0428 | PoetRAT | PoetRAT has used a Python tool named Bewmac to record the webcam on compromised hosts. [36] |
| S0192 | Pupy | Pupy can access a connected webcam and capture pictures. [37] |
| S0262 | QuasarRAT | QuasarRAT can perform webcam viewing. [38] [39] |
| S1209 | Quick Assist | Quick Assist allows for the remote administrator to view the interactive session of the running machine, including full screen activity. [40] [41] |
| S0332 | Remcos | Remcos can access a system’s webcam and take pictures. [42] |
| S0379 | Revenge RAT | Revenge RAT has the ability to access the webcam. [43] [44] |
| S0461 | SDBbot | SDBbot has the ability to record video on a compromised host. [45] [46] |
| G0091 | Silence | Silence has been observed making videos of victims to observe bank employees day to day activities. [47] [48] |
| S0098 | T9000 | T9000 uses the Skype API to record audio and video calls. It writes encrypted data to %APPDATA%\Intel\Skype . [49] |
| S0467 | TajMahal | TajMahal has the ability to capture webcam video. [50] |
| G1055 | VOID MANTICORE | VOID MANTICORE has collected video from compromised victim devices. [51] |
| S0670 | WarzoneRAT | WarzoneRAT can access the webcam on a victim's machine. [52] [53] |
| S0412 | ZxShell | ZxShell has a command to perform video device spying. [54] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0197 | Behavior-chain, platform-aware detection strategy for T1125 Video Capture | AN0568 | A non-standard process (or script-hosted process) loads camera/video-capture libraries (e.g., avicap32.dll, mf.dll, ksproxy.ax), opens the Camera Frame Server/device, writes video/image artifacts (e.g., .mp4/.avi/.yuv) to unusual locations, and optionally initiates outbound transfer shortly after. |
| AN0569 | A process opens/reads /dev/video* (V4L2), performs ioctl/read loops, writes large/continuous video artifacts to disk, and/or quickly establishes outbound connections for exfiltration. |  |  |
| AN0570 | A non-whitelisted process receives TCC camera entitlement (kTCCServiceCamera), opens AppleCamera/AVFoundation device handles, writes .mov/.mp4 artifacts to unusual locations, and/or beacons/exfiltrates soon after. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0197 | Behavior-chain, platform-aware detection strategy for T1125 Video Capture | AN0568 | A non-standard process (or script-hosted process) loads camera/video-capture libraries (e.g., avicap32.dll, mf.dll, ksproxy.ax), opens the Camera Frame Server/device, writes video/image artifacts (e.g., .mp4/.avi/.yuv) to unusual locations, and optionally initiates outbound transfer shortly after. |
| AN0569 | A process opens/reads /dev/video* (V4L2), performs ioctl/read loops, writes large/continuous video artifacts to disk, and/or quickly establishes outbound connections for exfiltration. |  |  |
| AN0570 | A non-whitelisted process receives TCC camera entitlement (kTCCServiceCamera), opens AppleCamera/AVFoundation device handles, writes .mov/.mp4 artifacts to unusual locations, and/or beacons/exfiltrates soon after. |  |  |

---

## References

- [Patrick Wardle. (n.d.). Retrieved March 20, 2018.](https://objective-see.com/blog/blog_0x25.html)
- [The DigiTrust Group. (2017, January 12). The Rise of Agent Tesla. Retrieved November 5, 2018.](https://www.digitrustgroup.com/agent-tesla-keylogger/)
- [Brumaghin, E., et al. (2018, October 15). Old dog, new tricks - Analysing new RTF-based campaign distributing Agent Tesla, Loki with PyREbox. Retrieved November 5, 2018.](https://blog.talosintelligence.com/2018/10/old-dog-new-tricks-analysing-new-rtf_15.html)
- [Nyan-x-Cat. (n.d.). NYAN-x-CAT / AsyncRAT-C-Sharp. Retrieved October 3, 2023.](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)
- [Galperin, E., Et al.. (2016, August). I Got a Letter From the Government the Other Day.... Retrieved April 25, 2018.](https://www.eff.org/files/2016/08/03/i-got-a-letter-from-the-government.pdf)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Chen, T. and Chen, Z. (2020, February 17). CLAMBLING - A New Backdoor Base On Dropbox. Retrieved November 12, 2021.](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
- [Yadav, A., et al. (2017, August 31). Cobian RAT – A backdoored RAT. Retrieved November 13, 2018.](https://www.zscaler.com/blogs/research/cobian-rat-backdoored-rat)
- [Mele, G. et al. (2021, February 10). Probable Iranian Cyber Actors, Static Kitten, Conducting Cyberespionage Campaign Targeting UAE and Kuwait Government Agencies. Retrieved March 17, 2021.](https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [TrendMicro. (2014, September 03). DARKCOMET. Retrieved November 6, 2018.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
- [Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [US Cybersecurity & Infrastructure Security Agency et al. (2024, September 5). Russian Military Cyber Actors Target U.S. and Global Critical Infrastructure. Retrieved September 6, 2024.](https://www.cisa.gov/sites/default/files/2024-09/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [Carr, N., et al. (2018, August 01). On the Hunt for FIN7: Pursuing an Enigmatic and Evasive Global Criminal Operation. Retrieved August 23, 2018.](https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html)
- [Department of Justice. (2018, August 01). HOW FIN7 ATTACKED AND STOLE DATA. Retrieved August 24, 2018.](https://www.justice.gov/opa/press-release/file/1084361/download)
- [Unit 42. (2019, December 2). Imminent Monitor – a RAT Down Under. Retrieved May 5, 2020.](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)
- [QiAnXin Threat Intelligence Center. (2019, February 18). APT-C-36: Continuous Attacks Targeting Colombian Government Institutions and Corporations. Retrieved May 5, 2020.](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Sharma, R. (2018, August 15). Revamped jRAT Uses New Anti-Parsing Techniques. Retrieved September 21, 2018.](https://www.symantec.com/blogs/threat-intelligence/jrat-new-anti-parsing-techniques)
- [Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [Kaspersky Global Research and Analysis Team. (2014, August 20). El Machete. Retrieved September 13, 2019.](https://securelist.com/el-machete/66108/)
- [The Cylance Threat Research Team. (2017, March 22). El Machete's Malware Attacks Cut Through LATAM. Retrieved September 13, 2019.](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)
- [kate. (2020, September 25). APT-C-43 steals Venezuelan military secrets to provide intelligence support for the reactionaries — HpReact campaign. Retrieved November 20, 2020.](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)
- [The DigiTrust Group. (2017, January 01). NanoCore Is Not Your Average RAT. Retrieved November 9, 2018.](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
- [Kasza, A., Halfpop, T. (2016, February 09). NanoCoreRAT Behind an Increase in Tax-Themed Phishing E-mails. Retrieved November 9, 2018.](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
- [Fidelis Cybersecurity. (2013, June 28). Fidelis Threat Advisory #1009: "njRAT" Uncovered. Retrieved June 4, 2019.](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
- [Scott-Railton, J., et al. (2016, August 2). Group5: Syria and the Iranian Connection. Retrieved September 26, 2016.](https://citizenlab.ca/2016/08/group5-syria/)
- [Malhotra, A. (2021, March 2). ObliqueRAT returns with new campaign using hijacked websites. Retrieved September 2, 2021.](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Mercer, W, et al. (2020, April 16). PoetRAT: Python RAT uses COVID-19 lures to target Azerbaijan public and private sectors. Retrieved April 27, 2020.](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
- [Nicolas Verdier. (n.d.). Retrieved January 29, 2018.](https://github.com/n1nj4sec/pupy)
- [MaxXor. (n.d.). QuasarRAT. Retrieved July 10, 2018.](https://github.com/quasar/QuasarRAT)
- [Meltzer, M, et al. (2018, June 07). Patchwork APT Group Targets US Think Tanks. Retrieved July 16, 2018.](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)
- [Microsoft. (2024, September 4). Use Quick Assist to help users. Retrieved March 14, 2025.](https://learn.microsoft.com/en-us/windows/client-management/client-tools/quick-assist)
- [Microsoft Threat Intelligence. (2024, May 15). Threat actors misusing Quick Assist in social engineering attacks leading to ransomware. Retrieved March 14, 2025.](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)
- [Bacurio, F., Salvio, J. (2017, February 14). REMCOS: A New RAT In The Wild. Retrieved November 6, 2018.](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)
- [Livelli, K, et al. (2018, November 12). Operation Shaheen. Retrieved May 1, 2019.](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
- [Gannon, M. (2019, February 11). With Upgrades in Delivery and Support Infrastructure, Revenge RAT Malware is a Bigger Threat. Retrieved November 17, 2024.](https://web.archive.org/web/20200428173819/https://cofense.com/upgrades-delivery-support-infrastructure-revenge-rat-malware-bigger-threat/)
- [Schwarz, D. et al. (2019, October 16). TA505 Distributes New SDBbot Remote Access Trojan with Get2 Downloader. Retrieved May 29, 2020.](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
- [Frydrych, M. (2020, April 14). TA505 Continues to Infect Networks With SDBbot RAT. Retrieved May 29, 2020.](https://web.archive.org/web/20200420201624/https://securityintelligence.com/posts/ta505-continues-to-infect-networks-with-sdbbot-rat/)
- [GReAT. (2017, November 1). Silence – a new Trojan attacking financial organizations. Retrieved May 24, 2019.](https://securelist.com/the-silence/83009/)
- [Group-IB. (2018, September). Silence: Moving Into the Darkside. Retrieved May 5, 2020.](https://go.group-ib.com/report-silence-en?_gl=1*d1bh3a*_ga*MTIwMzM5Mzc5MS4xNjk4OTI5NzY4*_ga_QMES53K3Y2*MTcwNDcyMjU2OS40LjEuMTcwNDcyMzU1Mi41My4wLjA.)
- [Grunzweig, J. and Miller-Osborn, J.. (2016, February 4). T9000: Advanced Modular Backdoor Uses Complex Anti-Analysis Techniques. Retrieved April 15, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [FBI. (2026, March 20). FBI Flash: FLASH-20260320-001:Government of Iran Cyber Actors Deploy Telegram C2 to Push Malware to Identified Targets. Retrieved April 20, 2026.](https://www.ic3.gov/CSA/2026/260320.pdf)
- [Harakhavik, Y. (2020, February 3). Warzone: Behind the enemy lines. Retrieved December 17, 2021.](https://research.checkpoint.com/2020/warzone-behind-the-enemy-lines/)
- [Mohanta, A. (2020, November 25). Warzone RAT comes with UAC bypass technique. Retrieved April 7, 2022.](https://www.uptycs.com/blog/warzone-rat-comes-with-uac-bypass-technique)
- [Allievi, A., et al. (2014, October 28). Threat Spotlight: Group 72, Opening the ZxShell. Retrieved September 24, 2019.](https://blogs.cisco.com/security/talos/opening-zxshell)

---

# Audio Capture

## Description

An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g., voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to gather information. [1]

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture audio. Audio files may be written to disk and exfiltrated later.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0067 | APT37 | APT37 has used an audio capturing utility known as SOUNDWAVE that captures microphone input. [2] |
| S0438 | Attor | Attor 's has a plugin that is capable of recording audio using available input sound devices. [1] |
| S0234 | Bandook | Bandook has modules that are capable of capturing audio. [3] |
| S0454 | Cadelspy | Cadelspy has the ability to record audio from the compromised host. [4] |
| S0338 | Cobian RAT | Cobian RAT has a feature to perform voice recording on the victim’s machine. [5] |
| S0115 | Crimson | Crimson can perform audio surveillance using microphones. [6] |
| S0334 | DarkComet | DarkComet can listen in to victims' conversations through the system’s microphone. [7] [8] |
| S0021 | Derusbi | Derusbi is capable of performing audio captures. [9] |
| S0213 | DOGCALL | DOGCALL can capture microphone data from the victim's machine. [10] |
| S0152 | EvilGrab | EvilGrab has the capability to capture audio from a victim machine. [11] |
| S0143 | Flame | Flame can record audio using any existing hardware recording devices. [12] [13] |
| S0434 | Imminent Monitor | Imminent Monitor has a remote microphone monitoring capability. [14] [15] |
| S0260 | InvisiMole | InvisiMole can record sound using input audio devices. [16] [17] |
| S0163 | Janicab | Janicab captured audio and sent it out to a C2 server. [18] [19] |
| S0283 | jRAT | jRAT can capture microphone recordings. [20] |
| S1185 | LightSpy | LightSpy uses Apple's built-in AVFoundation Framework library to capture and manage audio recordings then transform them to JSON blobs for exfiltration. [21] |
| S0409 | Machete | Machete captures audio from the computer’s microphone. [22] [23] [24] |
| S1016 | MacMa | MacMa has the ability to record audio. [25] |
| S0282 | MacSpy | MacSpy can record the sounds from microphones on a computer. [26] |
| S1146 | MgBot | MgBot can capture input and output audio streams from infected devices. [27] [28] |
| S0339 | Micropsia | Micropsia can perform microphone recording. [29] |
| S0336 | NanoCore | NanoCore can capture audio feeds from the system. [30] [31] |
| S1090 | NightClub | NightClub can load a module to leverage the LAME encoder and mciSendStringW to control and capture audio. [32] |
| S0194 | PowerSploit | PowerSploit 's Get-MicrophoneAudio Exfiltration module can record system microphone audio. [33] [34] |
| S0192 | Pupy | Pupy can record sound with the microphone. [35] |
| S0332 | Remcos | Remcos can capture data from the system’s microphone. [36] [37] |
| S0379 | Revenge RAT | Revenge RAT has a plugin for microphone interception. [38] [39] |
| S0240 | ROKRAT | ROKRAT has an audio capture and eavesdropping module. [40] |
| S0098 | T9000 | T9000 uses the Skype API to record audio and video calls. It writes encrypted data to %APPDATA%\Intel\Skype . [41] |
| S0467 | TajMahal | TajMahal has the ability to capture VoiceIP application audio on an infected host. [42] |
| S0257 | VERMIN | VERMIN can perform audio capture. [43] |
| G1055 | VOID MANTICORE | VOID MANTICORE has gathered audio during a Zoom session. [44] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0221 | Behavioral Detection Strategy for T1123 Audio Capture Across Windows, Linux, macOS | AN0619 | Unusual or unauthorized processes accessing microphone APIs (e.g., winmm.dll, avrt.dll) followed by audio file writes to user-accessible or temp directories. |
| AN0620 | Processes accessing ALSA/PulseAudio devices or executing audio capture binaries like 'arecord', followed by file creation or suspicious child process spawning. |  |  |
| AN0621 | Processes invoking AVFoundation or CoreAudio frameworks, accessing input devices via TCC logs or Unified Logs, followed by writing AIFF/WAV/MP3 files to disk. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0221 | Behavioral Detection Strategy for T1123 Audio Capture Across Windows, Linux, macOS | AN0619 | Unusual or unauthorized processes accessing microphone APIs (e.g., winmm.dll, avrt.dll) followed by audio file writes to user-accessible or temp directories. |
| AN0620 | Processes accessing ALSA/PulseAudio devices or executing audio capture binaries like 'arecord', followed by file creation or suspicious child process spawning. |  |  |
| AN0621 | Processes invoking AVFoundation or CoreAudio frameworks, accessing input devices via TCC logs or Unified Logs, followed by writing AIFF/WAV/MP3 files to disk. |  |  |

---

## References

- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [FireEye. (2018, February 20). APT37 (Reaper): The Overlooked North Korean Actor. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
- [Galperin, E., Et al.. (2016, August). I Got a Letter From the Government the Other Day.... Retrieved April 25, 2018.](https://www.eff.org/files/2016/08/03/i-got-a-letter-from-the-government.pdf)
- [Symantec Security Response. (2015, December 7). Iran-based attackers use back door threats to spy on Middle Eastern targets. Retrieved April 17, 2019.](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
- [Yadav, A., et al. (2017, August 31). Cobian RAT – A backdoored RAT. Retrieved November 13, 2018.](https://www.zscaler.com/blogs/research/cobian-rat-backdoored-rat)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [TrendMicro. (2014, September 03). DARKCOMET. Retrieved November 6, 2018.](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/DARKCOMET)
- [Kujawa, A. (2018, March 27). You dirty RAT! Part 1: DarkComet. Retrieved November 6, 2018.](https://blog.malwarebytes.com/threat-analysis/2012/06/you-dirty-rat-part-1-darkcomet/)
- [FireEye. (2018, March 16). Suspected Chinese Cyber Espionage Group (TEMP.Periscope) Targeting U.S. Engineering and Maritime Industries. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
- [Grunzweig, J. (2018, October 01). NOKKI Almost Ties the Knot with DOGCALL: Reaper Group Uses New Malware to Deploy RAT. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [Gostev, A. (2012, May 28). The Flame: Questions and Answers. Retrieved March 1, 2017.](https://securelist.com/the-flame-questions-and-answers-51/34344/)
- [Gostev, A. (2012, May 30). Flame: Bunny, Frog, Munch and BeetleJuice…. Retrieved March 1, 2017.](https://securelist.com/flame-bunny-frog-munch-and-beetlejuice-2/32855/)
- [Unit 42. (2019, December 2). Imminent Monitor – a RAT Down Under. Retrieved May 5, 2020.](https://unit42.paloaltonetworks.com/imminent-monitor-a-rat-down-under/)
- [QiAnXin Threat Intelligence Center. (2019, February 18). APT-C-36: Continuous Attacks Targeting Colombian Government Institutions and Corporations. Retrieved May 5, 2020.](https://web.archive.org/web/20190625182633if_/https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Brod. (2013, July 15). Signed Mac Malware Using Right-to-Left Override Trick. Retrieved July 17, 2017.](https://www.f-secure.com/weblog/archives/00002576.html)
- [Thomas. (2013, July 15). New signed malware called Janicab. Retrieved July 17, 2017.](https://web.archive.org/web/20230331162455/https://www.thesafemac.com/new-signed-malware-called-janicab/)
- [Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
- [Stuart Ashenbrenner, Alden Schmidt. (2024, April 25). LightSpy Malware Variant Targeting macOS. Retrieved January 3, 2025.](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
- [Kaspersky Global Research and Analysis Team. (2014, August 20). El Machete. Retrieved September 13, 2019.](https://securelist.com/el-machete/66108/)
- [The Cylance Threat Research Team. (2017, March 22). El Machete's Malware Attacks Cut Through LATAM. Retrieved September 13, 2019.](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)
- [kate. (2020, September 25). APT-C-43 steals Venezuelan military secrets to provide intelligence support for the reactionaries — HpReact campaign. Retrieved November 20, 2020.](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)
- [Wardle, P. (2021, November 11). OSX.CDDS (OSX.MacMa). Retrieved June 30, 2022.](https://objective-see.org/blog/blog_0x69.html)
- [Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.](https://objective-see.com/blog/blog_0x25.html)
- [Facundo Muñoz. (2023, April 26). Evasive Panda APT group delivers malware via updates for popular Chinese software. Retrieved July 25, 2024.](https://www.welivesecurity.com/2023/04/26/evasive-panda-apt-group-malware-updates-popular-chinese-software/)
- [Threat Hunter Team. (2023, April 20). Daggerfly: APT Actor Targets Telecoms Company in Africa. Retrieved July 25, 2024.](https://symantec-enterprise-blogs.security.com/threat-intelligence/apt-attacks-telecoms-africa-mgbot)
- [Tsarfaty, Y. (2018, July 25). Micropsia Malware. Retrieved November 13, 2018.](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
- [The DigiTrust Group. (2017, January 01). NanoCore Is Not Your Average RAT. Retrieved November 9, 2018.](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
- [Kasza, A., Halfpop, T. (2016, February 09). NanoCoreRAT Behind an Increase in Tax-Themed Phishing E-mails. Retrieved November 9, 2018.](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
- [Faou, M. (2023, August 10). MoustachedBouncer: Espionage against foreign diplomats in Belarus. Retrieved September 25, 2023.](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
- [PowerShellMafia. (2012, May 26). PowerSploit - A PowerShell Post-Exploitation Framework. Retrieved February 6, 2018.](https://github.com/PowerShellMafia/PowerSploit)
- [PowerSploit. (n.d.). PowerSploit. Retrieved February 6, 2018.](http://powersploit.readthedocs.io)
- [Nicolas Verdier. (n.d.). Retrieved January 29, 2018.](https://github.com/n1nj4sec/pupy)
- [Bacurio, F., Salvio, J. (2017, February 14). REMCOS: A New RAT In The Wild. Retrieved November 6, 2018.](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)
- [Zhang, X. (2024, November 8). New Campaign Uses Remcos RAT to Exploit Victims. Retrieved April 16, 2026.](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
- [Livelli, K, et al. (2018, November 12). Operation Shaheen. Retrieved May 1, 2019.](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
- [Gannon, M. (2019, February 11). With Upgrades in Delivery and Support Infrastructure, Revenge RAT Malware is a Bigger Threat. Retrieved November 17, 2024.](https://web.archive.org/web/20200428173819/https://cofense.com/upgrades-delivery-support-infrastructure-revenge-rat-malware-bigger-threat/)
- [GReAT. (2019, May 13). ScarCruft continues to evolve, introduces Bluetooth harvester. Retrieved June 4, 2019.](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)
- [Grunzweig, J. and Miller-Osborn, J.. (2016, February 4). T9000: Advanced Modular Backdoor Uses Complex Anti-Analysis Techniques. Retrieved April 15, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
- [FBI. (2026, March 20). FBI Flash: FLASH-20260320-001:Government of Iran Cyber Actors Deploy Telegram C2 to Push Malware to Identified Targets. Retrieved April 20, 2026.](https://www.ic3.gov/CSA/2026/260320.pdf)

---

# Template Injection

## Description

Adversaries may create or modify references in user document templates to conceal malicious code or force authentication attempts. For example, Microsoft’s Office Open XML (OOXML) specification defines an XML-based format for Office documents (.docx, xlsx, .pptx) to replace older binary formats (.doc, .xls, .ppt). OOXML files are packed together ZIP archives compromised of various XML files, referred to as parts, containing properties that collectively define how a document is rendered. [1]

Properties within parts may reference shared public resources accessed via online URLs. For example, template properties may reference a file, serving as a pre-formatted document blueprint, that is fetched when the document is loaded.

Adversaries may abuse these templates to initially conceal malicious code to be executed via user documents. Template references injected into a document may enable malicious payloads to be fetched and executed when the document is loaded. [2] These documents can be delivered via other techniques such as Phishing and/or Taint Shared Content and may evade static detections since no typical indicators (VBA macro, script, etc.) are present until after the malicious payload is fetched. [3] Examples have been seen in the wild where template injection was used to load malicious code containing an exploit. [4]

Adversaries may also modify the *\template control word within an .rtf file to similarly conceal then download malicious code. This legitimate control word value is intended to be a file destination of a template file resource that is retrieved and loaded when an .rtf file is opened. However, adversaries may alter the bytes of an existing .rtf file to insert a template control word field to include a URL resource of a malicious payload. [5] [6]

This technique may also enable Forced Authentication by injecting a SMB/HTTPS (or other credential prompting) URL and triggering an authentication attempt. [7] [8] [9]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0007 | APT28 | APT28 used weaponized Microsoft Word documents abusing the remote template function to retrieve a malicious macro. [10] |
| S0631 | Chaes | Chaes changed the template target of the settings.xml file embedded in the Word document and populated that field with the downloaded URL of the next payload. [11] |
| G0142 | Confucius | Confucius has used a weaponized Microsoft Word document with an embedded RTF exploit. [12] |
| G0079 | DarkHydrus | DarkHydrus used an open-source tool, Phishery, to inject malicious remote template URLs into Microsoft Word documents and then sent them to victims to enable Forced Authentication . [13] |
| G0035 | Dragonfly | Dragonfly has injected SMB URLs into malicious Word spearphishing attachments to initiate Forced Authentication . [14] |
| C0001 | Frankenstein | During Frankenstein , the threat actors used trojanized documents that retrieved remote templates from an adversary-controlled website. [15] |
| G0047 | Gamaredon Group | Gamaredon Group has used DOCX files to download malicious DOT document templates and has used RTF template injection to download malicious payloads. [5] Gamaredon Group can also inject malicious macros or remote templates into documents already present on compromised systems. [16] [17] [18] [19] [20] [21] [22] |
| G0100 | Inception | Inception has used decoy documents to load malicious remote payloads via HTTP. [23] |
| G1054 | MirrorFace | MirrorFace has used remote template injection to retrieve malicious payloads from the C2. [24] |
| C0022 | Operation Dream Job | During Operation Dream Job , Lazarus Group used DOCX files to retrieve a malicious document template/DOTM file. [25] [26] |
| G0081 | Tropic Trooper | Tropic Trooper delivered malicious documents with the XLSX extension, typically used by OpenXML documents, but the file itself was actually an OLE (XLS) document. [27] |
| S0670 | WarzoneRAT | WarzoneRAT has been install via template injection through a malicious DLL embedded within a template RTF in a Word document. [12] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1049 | Antivirus/Antimalware | Network/Host intrusion prevention systems, antivirus, and detonation chambers can be employed to prevent documents from fetching and/or executing malicious payloads. [7] |
| M1042 | Disable or Remove Feature or Program | Consider disabling Microsoft Office macros/active content to prevent the execution of malicious payloads in documents [28] , though this setting may not mitigate the Forced Authentication use for this technique. |
| M1031 | Network Intrusion Prevention | Network/Host intrusion prevention systems, antivirus, and detonation chambers can be employed to prevent documents from fetching and/or executing malicious payloads. [7] |
| M1017 | User Training | Train users to identify social engineering techniques and spearphishing emails that could be used to deliver malicious documents. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0566 | Template Injection Detection - Windows | AN1564 | Detection of Office or document viewer processes (e.g., winword.exe) initiating network connections to remote templates or executing scripts due to manipulated template references (e.g., embedded in .docx, .rtf, or .dotm files), followed by suspicious child process creation (e.g., PowerShell). |

---

## References

- [Microsoft. (2014, July 9). Introducing the Office (2007) Open XML File Formats. Retrieved July 20, 2018.](https://docs.microsoft.com/previous-versions/office/developer/office-2007/aa338205(v=office.12))
- [Wiltse, B.. (2018, November 7). Template Injection Attacks - Bypassing Security Controls by Living off the Land. Retrieved April 10, 2019.](https://www.sans.org/reading-room/whitepapers/testing/template-injection-attacks-bypassing-security-controls-living-land-38780)
- [Hawkins, J. (2018, July 18). Executing Macros From a DOCX With Remote Template Injection. Retrieved October 12, 2018.](http://blog.redxorblue.com/2018/07/executing-macros-from-docx-with-remote.html)
- [Segura, J. (2017, October 13). Decoy Microsoft Word document delivers malware through a RAT. Retrieved July 21, 2018.](https://blog.malwarebytes.com/threat-analysis/2017/10/decoy-microsoft-word-document-delivers-malware-through-rat/)
- [Raggi, M. (2021, December 1). Injection is the New Black: Novel RTF Template Inject Technique Poised for Widespread Adoption Beyond APT Actors . Retrieved December 9, 2021.](https://www.proofpoint.com/us/blog/threat-insight/injection-new-black-novel-rtf-template-inject-technique-poised-widespread)
- [Pedrero, R.. (2021, July). Decoding malicious RTF files. Retrieved November 16, 2021.](https://ciberseguridad.blog/decodificando-ficheros-rtf-maliciosos/)
- [Intel_Acquisition_Team. (2018, March 1). Credential Harvesting and Malicious File Delivery using Microsoft Office Template Injection. Retrieved July 20, 2018.](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)
- [Baird, S. et al.. (2017, July 7). Attack on Critical Infrastructure Leverages Template Injection. Retrieved July 21, 2018.](https://blog.talosintelligence.com/2017/07/template-injection.html)
- [Hanson, R. (2016, September 24). phishery. Retrieved July 21, 2018.](https://github.com/ryhanson/phishery)
- [Lee, B., Falcone, R. (2018, December 12). Dear Joohn: The Sofacy Group’s Global Campaign. Retrieved April 19, 2019.](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)
- [Salem, E. (2020, November 17). CHAES: Novel Malware Targeting Latin American E-Commerce. Retrieved June 30, 2021.](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
- [Uptycs Threat Research Team. (2021, January 12). Confucius APT deploys Warzone RAT. Retrieved December 17, 2021.](https://www.uptycs.com/blog/confucius-apt-deploys-warzone-rat)
- [Falcone, R. (2018, August 07). DarkHydrus Uses Phishery to Harvest Credentials in the Middle East. Retrieved August 10, 2018.](https://researchcenter.paloaltonetworks.com/2018/08/unit42-darkhydrus-uses-phishery-harvest-credentials-middle-east/)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [Adamitis, D. et al. (2019, June 4). It's alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign. Retrieved May 11, 2020.](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
- [Kakara, H., Maruyama, E. (2020, April 17). Gamaredon APT Group Use Covid-19 Lure in Campaigns. Retrieved May 19, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/gamaredon-apt-group-use-covid-19-lure-in-campaigns/)
- [Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.](https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/)
- [CERT-EE. (2021, January 27). Gamaredon Infection: From Dropper to Entry. Retrieved February 17, 2022.](https://www.ria.ee/sites/default/files/content-editors/kuberturve/tale_of_gamaredon_infection.pdf)
- [Microsoft Threat Intelligence Center. (2022, February 4). ACTINIUM targets Ukrainian organizations. Retrieved February 18, 2022.](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
- [Unit 42. (2022, February 3). Russia’s Gamaredon aka Primitive Bear APT Group Actively Targeting Ukraine. Retrieved February 21, 2022.](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)
- [Secureworks CTU. (n.d.). IRON TILDEN. Retrieved February 24, 2022.](https://www.secureworks.com/research/threat-profiles/iron-tilden)
- [Rusnák, Z. (2024, September 26). Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023. Retrieved October 30, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/cyberespionage-gamaredon-way.pdf)
- [Lancaster, T. (2018, November 5). Inception Attackers Target Europe with Year-old Office Vulnerability. Retrieved May 8, 2020.](https://unit42.paloaltonetworks.com/unit42-inception-attackers-target-europe-year-old-office-vulnerability/)
- [ITOCHU. (2024, January 24). The Endless Struggle Against APT10: Insights from LODEINFO v0.6.6 - v0.7.3 Analysis. Retrieved April 17, 2026.](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
- [ClearSky Research Team. (2020, August 13). Operation 'Dream Job' Widespread North Korean Espionage Campaign. Retrieved December 20, 2021.](https://www.clearskysec.com/wp-content/uploads/2020/08/Dream-Job-Campaign.pdf)
- [Cashman, M. (2020, July 29). Operation North Star Campaign. Retrieved December 20, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-a-job-offer-thats-too-good-to-be-true/?hilite=%27Operation%27%2C%27North%27%2C%27Star%27)
- [Ray, V. (2016, November 22). Tropic Trooper Targets Taiwanese Government and Fossil Fuel Provider With Poison Ivy. Retrieved November 9, 2018.](https://researchcenter.paloaltonetworks.com/2016/11/unit42-tropic-trooper-targets-taiwanese-government-and-fossil-fuel-provider-with-poison-ivy/)
- [Microsoft. (n.d.). Enable or disable macros in Office files. Retrieved September 13, 2018.](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)

---

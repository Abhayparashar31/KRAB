# Shared Modules

## Description

Adversaries may execute malicious payloads via loading shared modules. Shared modules are executable files that are loaded into processes to provide access to reusable code, such as specific custom functions or invoking OS API functions (i.e., Native API ).

Adversaries may use this functionality as a way to execute arbitrary payloads on a victim system. For example, adversaries can modularize functionality of their malware into shared objects that perform various functions such as managing C2 network communications or execution of specific actions on objective.

The Linux & macOS module loader can load and execute shared objects from arbitrary local paths. This functionality resides in dlfcn.h in functions such as dlopen and dlsym . Although macOS can execute .so files, common practice uses .dylib files. [1] [2] [3] [4]

The Windows module loader can be instructed to load DLLs from arbitrary local paths and arbitrary Universal Naming Convention (UNC) network paths. This functionality resides in NTDLL.dll and is part of the Windows Native API which is called from functions like LoadLibrary at run time. [5]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0373 | Astaroth | Astaroth uses the LoadLibraryExW() function to load additional modules. [6] |
| S0438 | Attor | Attor 's dispatcher can execute additional plugins by loading the respective DLLs. [7] |
| S0520 | BLINDINGCAN | BLINDINGCAN has loaded and executed DLLs in memory during runtime on a victim machine. [8] |
| S0415 | BOOSTWRITE | BOOSTWRITE has used the DWriteCreateFactory() function to load additional modules. [9] |
| S1039 | Bumblebee | Bumblebee can use LoadLibrary to attempt to execute GdiPlus.dll. [10] |
| S0673 | DarkWatchman | DarkWatchman can load DLLs. [11] |
| S0567 | Dtrack | Dtrack contains a function that calls LoadLibrary and GetProcAddress . [12] |
| S0377 | Ebury | Ebury is executed through hooking the keyutils.so file used by legitimate versions of OpenSSH and libcurl . [13] |
| S0661 | FoggyWeb | FoggyWeb 's loader can call the load() function to load the FoggyWeb dll into an Application Domain on a compromised AD FS server. [14] |
| S0032 | gh0st RAT | gh0st RAT can load DLLs into memory. [15] |
| S0203 | Hydraq | Hydraq creates a backdoor through which remote attackers can load and call DLL functions. [16] [17] |
| S0607 | KillDisk | KillDisk loads and executes functions from a DLL. [18] |
| S1185 | LightSpy | LightSpy 's main executable and module .dylib binaries are loaded using a combination of dlopen() to load the library, _objc_getClass() to retrieve the class definition, and _objec_msgSend() to invoke/execute the specified method in the loaded class. [19] |
| S0455 | Metamorfo | Metamorfo had used AutoIt to load and execute the DLL payload. [20] |
| G0129 | Mustang Panda | Mustang Panda has leveraged LoadLibrary to load DLLs. [21] |
| S0352 | OSX_OCEANLOTUS.D | For network communications, OSX_OCEANLOTUS.D loads a dynamic library ( .dylib file) using dlopen() and obtains a function pointer to execute within that shared library using dlsym() . [4] |
| S0501 | PipeMon | PipeMon has used call to LoadLibrary to load its installer. PipeMon loads its modules using reflective loading or custom shellcode. [22] |
| S0196 | PUNCHBUGGY | PUNCHBUGGY can load a DLL using the LoadLibrary API. [23] |
| S1078 | RotaJakiro | RotaJakiro uses dynamically linked shared libraries ( .so files) to execute additional functionality using dlopen() and dlsym() . [3] |
| S0603 | Stuxnet | Stuxnet calls LoadLibrary then executes exports from a DLL. [24] |
| S0467 | TajMahal | TajMahal has the ability to inject the LoadLibrary call template DLL into running processes. [25] |
| S1154 | VersaMem | VersaMem relied on the Java Instrumentation API and Javassist to dynamically modify Java code existing in memory. [26] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1038 | Execution Prevention | Identify and block potentially malicious software executed through this technique by using application control tools capable of preventing unknown modules from being loaded. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0018 | Behavior-chain, platform-aware detection strategy for T1129 Shared Modules | AN0052 | A process (often LOLBin or user-launched program) loads a DLL from a user-writable/UNC/Temp path or unsigned/invalid signer. Within a short window the DLL is (a) newly written to disk, (b) spawned as follow-on execution (rundll32/regsvr32), or (c) establishes outbound C2. |
| AN0053 | A process loads a shared object (.so) via dlopen/LD_PRELOAD/open from non-standard or temporary locations (e.g., /tmp, /dev/shm), especially shortly after that .so is written or fetched, or linked via manipulated environment variables (LD_PRELOAD/LD_LIBRARY_PATH). |  |  |
| AN0054 | A process loads a non-system .dylib/.so via dyld (dlopen/dlsym) from user-writable locations (~/Library, /tmp) or after the library was recently created/downloaded, often followed by network egress or persistence. |  |  |

---

## References

- [Apple. (2012, July 23). Overview of Dynamic Libraries. Retrieved September 7, 2023.](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/OverviewOfDynamicLibraries.html)
- [Wheeler, D. (2003, April 11). Shared Libraries. Retrieved September 7, 2023.](https://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html)
- [Alex Turing, Hui Wang. (2021, April 28). RotaJakiro: A long live secret backdoor with 0 VT detection. Retrieved June 14, 2023.](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
- [Erye Hernandez and Danny Tsechansky. (2017, June 22). The New and Improved macOS Backdoor from OceanLotus. Retrieved September 8, 2023.](https://unit42.paloaltonetworks.com/unit42-new-improved-macos-backdoor-oceanlotus/)
- [Microsoft. (2023, April 28). What is a DLL. Retrieved September 7, 2023.](https://learn.microsoft.com/troubleshoot/windows-client/deployment/dynamic-link-library)
- [Salem, E. (2019, February 13). ASTAROTH MALWARE USES LEGITIMATE OS AND ANTIVIRUS PROCESSES TO STEAL PASSWORDS AND PERSONAL DATA. Retrieved April 17, 2019.](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
- [Hromcova, Z. (2019, October). AT COMMANDS, TOR-BASED COMMUNICATIONS: MEET ATTOR, A FANTASY CREATURE AND ALSO A SPY PLATFORM. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
- [US-CERT. (2020, August 19). MAR-10295134-1.v1 – North Korean Remote Access Trojan: BLINDINGCAN. Retrieved August 19, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
- [Carr, N, et all. (2019, October 10). Mahalo FIN7: Responding to the Criminal Operators’ New Tools and Techniques. Retrieved October 11, 2019.](https://www.fireeye.com/blog/threat-research/2019/10/mahalo-fin7-responding-to-new-tools-and-techniques.html)
- [Salem, A. (2022, April 27). The chronicles of Bumblebee: The Hook, the Bee, and the Trickbot connection. Retrieved September 2, 2022.](https://elis531989.medium.com/the-chronicles-of-bumblebee-the-hook-the-bee-and-the-trickbot-connection-686379311056)
- [Smith, S., Stafford, M. (2021, December 14). DarkWatchman: A new evolution in fileless techniques. Retrieved January 10, 2022.](https://web.archive.org/web/20220629230035/https://www.prevailion.com/darkwatchman-new-fileless-techniques/)
- [Hod Gavriel. (2019, November 21). Dtrack: In-depth analysis of APT on a nuclear power plant. Retrieved January 20, 2021.](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
- [Marc-Etienne M.Léveillé. (2024, May 1). Ebury is alive but unseen. Retrieved May 21, 2024.](https://web-assets.esetstatic.com/wls/en/papers/white-papers/ebury-is-alive-but-unseen.pdf)
- [Ramin Nafisi. (2021, September 27). FoggyWeb: Targeted NOBELIUM malware leads to persistent backdoor. Retrieved October 4, 2021.](https://www.microsoft.com/security/blog/2021/09/27/foggyweb-targeted-nobelium-malware-leads-to-persistent-backdoor/)
- [Quinn, J. (2019, March 25). The odd case of a Gh0stRAT variant. Retrieved July 15, 2020.](https://cybersecurity.att.com/blogs/labs-research/the-odd-case-of-a-gh0strat-variant)
- [Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
- [Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
- [Fernando Merces, Byron Gelera, Martin Co. (2018, June 7). KillDisk Variant Hits Latin American Finance Industry. Retrieved January 12, 2021.](https://www.trendmicro.com/en_us/research/18/f/new-killdisk-variant-hits-latin-american-financial-organizations-again.html)
- [Stuart Ashenbrenner, Alden Schmidt. (2024, April 25). LightSpy Malware Variant Targeting macOS. Retrieved January 3, 2025.](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
- [Zhang, X. (2020, February 4). Another Metamorfo Variant Targeting Customers of Financial Institutions in More Countries. Retrieved July 30, 2020.](https://www.fortinet.com/blog/threat-research/another-metamorfo-variant-targeting-customers-of-financial-institutions)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [Tartare, M. et al. (2020, May 21). No “Game over” for the Winnti Group. Retrieved August 24, 2020.](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
- [Elovitz, S. & Ahl, I. (2016, August 18). Know Your Enemy: New Financially-Motivated & Spear-Phishing Group. Retrieved February 26, 2018.](https://www2.fireeye.com/WBNR-Know-Your-Enemy-UNC622-Spear-Phishing.html)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Black Lotus Labs. (2024, August 27). Taking The Crossroads: The Versa Director Zero-Day Exploitaiton. Retrieved August 27, 2024.](https://blog.lumen.com/taking-the-crossroads-the-versa-director-zero-day-exploitation/)

---

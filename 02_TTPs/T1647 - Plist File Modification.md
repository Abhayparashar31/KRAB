# Plist File Modification

## Description

Adversaries may modify property list files (plist files) to enable other malicious activity, while also potentially evading and bypassing system defenses. macOS applications use plist files, such as the info.plist file, to store properties and configuration settings that inform the operating system how to handle the application at runtime. Plist files are structured metadata in key-value pairs formatted in XML based on Apple's Core Foundation DTD. Plist files can be saved in text or binary format. [1]

Adversaries can modify key-value pairs in plist files to influence system behaviors, such as hiding the execution of an application (i.e. Hidden Window ) or running additional commands for persistence (ex: Launch Agent / Launch Daemon or Re-opened Applications ).

For example, adversaries can add a malicious application path to the ~/Library/Preferences/com.apple.dock.plist file, which controls apps that appear in the Dock. Adversaries can also modify the LSUIElement key in an application’s info.plist file to run the app in the background. Adversaries can also insert key-value pairs to insert environment variables, such as LSEnvironment , to enable persistence via Dynamic Linker Hijacking . [2] [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1153 | Cuckoo Stealer | Cuckoo Stealer can create and populate property list (plist) files to enable execution. [4] [5] |
| S0658 | XCSSET | In older versions, XCSSET uses the plutil command to modify the LSUIElement , DFBundleDisplayName , and CFBundleIdentifier keys in the /Contents/Info.plist file to change how XCSSET is visible on the system. In later versions, XCSSET leverages a third-party notarized dockutil tool to modify the .plist file responsible for presenting applications to the user in the Dock and LaunchPad to point to a malicious application. [6] [7] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1013 | Application Developer Guidance | Ensure applications are using Apple's developer guidance which enables hardened runtime. [8] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0109 | Detection Strategy for Plist File Modification (T1647) | AN0306 | Monitor for unexpected modifications of plist files in persistence or configuration directories (e.g., ~/Library/LaunchAgents, ~/Library/Preferences, /Library/LaunchDaemons). Detect when modifications are followed by execution of new or unexpected binaries. Track use of utilities such as defaults, plutil, or text editors making changes to Info.plist files. Correlate file modifications with subsequent process launches or service starts that reference the altered plist. |

---

## References

- [FileInfo.com team. (2019, November 26). .PLIST File Extension. Retrieved October 12, 2021.](https://fileinfo.com/extension/plist)
- [Patrick Wardle. (2022, January 1). The Art of Mac Malware Volume 0x1:Analysis. Retrieved April 19, 2022.](https://taomm.org/PDFs/vol1/CH%200x02%20Persistence.pdf)
- [ESET. (2012, January 1). OSX/Flashback. Retrieved April 19, 2022.](https://www.welivesecurity.com/wp-content/uploads/200x/white-papers/osx_flashback.pdf)
- [Kohler, A. and Lopez, C. (2024, April 30). Malware: Cuckoo Behaves Like Cross Between Infostealer and Spyware. Retrieved August 20, 2024.](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
- [Stokes, P. (2024, May 9). macOS Cuckoo Stealer | Ensuring Detection and Defense as New Samples Rapidly Emerge. Retrieved August 20, 2024.](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)
- [Mac Threat Response, Mobile Research Team. (2020, August 13). The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSS Backdoor Planting in Safari, and Leverages Two Zero-day Exploits. Retrieved October 5, 2021.](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
- [Microsoft Threat Intelligence. (2025, March 11). New XCSSET malware adds new obfuscation, persistence techniques to infect Xcode projects. Retrieved April 2, 2025.](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)
- [Apple Inc.. (2021, January 1). Hardened Runtime: Manage security protections and resource access for your macOS apps.. Retrieved March 24, 2021.](https://developer.apple.com/documentation/security/hardened_runtime)

---

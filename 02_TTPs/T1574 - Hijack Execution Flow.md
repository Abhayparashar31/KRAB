# Hijack Execution Flow

## Description

Adversaries may execute their own malicious payloads by hijacking the way operating systems run programs. Hijacking execution flow can be for the purposes of persistence, since this hijacked execution may reoccur over time. Adversaries may also use these mechanisms to elevate privileges or evade defenses, such as application control or other restrictions on execution.

There are many ways an adversary may hijack the flow of execution, including by manipulating how the operating system locates programs to be executed. How the operating system locates libraries to be used by a program can also be intercepted. Locations where the operating system looks for programs/resources, such as file directories and in the case of Windows the Registry, could also be poisoned to include malicious payloads.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0017 | C0017 | During C0017 , APT41 established persistence by loading malicious libraries via modifications to the Import Address Table (IAT) within legitimate Microsoft binaries. [1] |
| S1105 | COATHANGER | COATHANGER will remove and write malicious shared objects associated with legitimate system functions such as read(2) . [2] |
| S1111 | DarkGate | DarkGate edits the Registry key HKCU\Software\Classes\mscfile\shell\open\command to execute a malicious AutoIt script. [3] When eventvwr.exe is executed, this will call the Microsoft Management Console (mmc.exe), which in turn references the modified Registry key. |
| S0354 | Denis | Denis replaces the nonexistent Windows DLL "msfte.dll" with its own malicious version, which is loaded by the SearchIndexer.exe and SearchProtocolHost.exe. [4] |
| S0567 | Dtrack | One of Dtrack can replace the normal flow of a program execution with malicious code. [5] |
| S1147 | Nightdoor | Nightdoor uses a legitimate executable to load a malicious DLL file for installation. [6] |
| C0036 | Pikabot Distribution February 2024 | Pikabot Distribution February 2024 utilized a tampered legitimate executable, grepWinNP3.exe , for its first stage Pikabot loader, modifying the open-source tool to execute malicious code when launched. [7] |
| S1130 | Raspberry Robin | Raspberry Robin will drop a copy of itself to a subfolder in %Program Data% or %Program Data%\Microsoft\ to attempt privilege elevation and defense evasion if not running in Session 0. [8] |
| S1018 | Saint Bot | Saint Bot will use the malicious file slideshow.mp4 if present to load the core API provided by ntdll.dll to avoid any hooks placed on calls to the original ntdll.dll file by endpoint detection and response or antimalware software. [9] |
| S0444 | ShimRat | ShimRat can hijack the cryptbase.dll within migwiz.exe to escalate privileges and bypass UAC controls. [10] |
| S9024 | SPAWNCHIMERA | SPAWNCHIMERA can persist across system upgrades by hijacking the execution flow of dspkginstall, a binary used during the system upgrade process. [11] [12] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1013 | Application Developer Guidance | When possible, include hash values in manifest files to help prevent side-loading of malicious libraries. [13] |
| M1047 | Audit | Use auditing tools capable of detecting hijacking opportunities on systems within an enterprise and correct them. Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for hijacking weaknesses. [14] Use the program sxstrace.exe that is included with Windows along with manual inspection to check manifest files for side-loading vulnerabilities in software. Find and eliminate path interception weaknesses in program configuration files, scripts, the PATH environment variable, services, and in shortcuts by surrounding PATH variables with quotation marks when functions allow for them. Be aware of the search order Windows uses for executing or loading binaries and use fully qualified paths wherever appropriate. Clean up old Windows Registry keys when software is uninstalled to avoid keys with no associated legitimate binaries. Periodically search for and correct or report path interception weaknesses on systems that may have been introduced using custom or available tools that report software using insecure path configurations. [15] [16] [17] |
| M1040 | Behavior Prevention on Endpoint | Some endpoint security solutions can be configured to block some types of behaviors related to process injection/memory tampering based on common sequences of indicators (ex: execution of specific API functions). |
| M1038 | Execution Prevention | Adversaries may use new payloads to execute this technique. Identify and block potentially malicious software executed through hijacking by using application control solutions also capable of blocking libraries loaded by legitimate software. |
| M1022 | Restrict File and Directory Permissions | Install software in write-protected locations. Set directory access controls to prevent file writes to the search paths for applications, both in the folders where applications are run from and the standard library folders. |
| M1044 | Restrict Library Loading | Disallow loading of remote DLLs. This is included by default in Windows Server 2012+ and is available by patch for XP+ and Server 2003+. Enable Safe DLL Search Mode to force search for system DLLs in directories with greater restrictions (e.g. %SYSTEMROOT% )to be used before local directory DLLs (e.g. a user's home directory) The Safe DLL Search Mode can be enabled via Group Policy at Computer Configuration > [Policies] > Administrative Templates > MSS (Legacy): MSS: (SafeDllSearchMode) Enable Safe DLL search mode. The associated Windows Registry key for this is located at HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\SafeDLLSearchMode [18] [19] |
| M1024 | Restrict Registry Permissions | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation. |
| M1051 | Update Software | Update software regularly to include patches that fix DLL side-loading vulnerabilities. |
| M1052 | User Account Control | Turn off UAC's privilege elevation for standard users [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System] to automatically deny elevation requests, add: "ConsentPromptBehaviorUser"=dword:00000000 . Consider enabling installer detection for all users by adding: "EnableInstallerDetection"=dword:00000001 . This will prompt for a password for installation and also log the attempt. To disable installer detection, instead add: "EnableInstallerDetection"=dword:00000000 . This may prevent potential elevation of privileges through exploitation during the process of UAC detecting the installer, but will allow the installation process to continue without being logged. [20] |
| M1018 | User Account Management | Limit privileges of user accounts and groups so that only authorized administrators can interact with service changes and service binary target path locations. Deny execution from user directories such as file download directories and temp directories where able. Ensure that proper permissions and directory access control are set to deny users the ability to write files to the top-level directory C: and system directories, such as C:\Windows\ , to reduce places where malicious files could be placed for execution. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0218 | Detection Strategy for Hijack Execution Flow across OS platforms. | AN0609 | Unusual modifications to service binary paths, registry keys, or DLL load paths resulting in alternate execution flow. Defender observes registry key modifications, suspicious file writes into system directories, and processes loading libraries from abnormal paths. |
| AN0610 | Adversary manipulation of shared library paths, environment variables, or replacement of service binaries. Defender observes suspicious modifications in /etc/ld.so.preload, service config changes, or file writes replacing existing executables. |  |  |
| AN0611 | Abuse of DYLD_INSERT_LIBRARIES or hijacking framework paths for malicious libraries. Defender observes processes invoking abnormal dylibs, modified plist files, or persistence entries pointing to altered binaries. |  |  |

---

## References

- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Dutch Military Intelligence and Security Service (MIVD) & Dutch General Intelligence and Security Service (AIVD). (2024, February 6). Ministry of Defense of the Netherlands uncovers COATHANGER, a stealthy Chinese FortiGate RAT. Retrieved February 7, 2024.](https://www.ncsc.nl/binaries/ncsc/documenten/publicaties/2024/februari/6/mivd-aivd-advisory-coathanger-tlp-clear/TLP-CLEAR+MIVD+AIVD+Advisory+COATHANGER.pdf)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Hod Gavriel. (2019, November 21). Dtrack: In-depth analysis of APT on a nuclear power plant. Retrieved January 20, 2021.](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
- [Threat Hunter Team. (2024, July 23). Daggerfly: Espionage Group Makes Major Update to Toolset. Retrieved July 25, 2024.](https://symantec-enterprise-blogs.security.com/threat-intelligence/daggerfly-espionage-updated-toolset)
- [Daniel Stepanic & Salim Bitam. (2024, February 23). PIKABOT, I choose you!. Retrieved July 12, 2024.](https://www.elastic.co/security-labs/pikabot-i-choose-you)
- [Christopher So. (2022, December 20). Raspberry Robin Malware Targets Telecom, Governments. Retrieved May 17, 2024.](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
- [Unit 42. (2022, February 25). Spear Phishing Attacks Target Organizations in Ukraine, Payloads Include the Document Stealer OutSteel and the Downloader SaintBot. Retrieved June 9, 2022.](https://unit42.paloaltonetworks.com/ukraine-targeted-outsteel-saintbot/)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [John Wolfram, Josh Murchie, Matt Lin, Daniel Ainsworth, Robert Wallace, Dimiter Andonov, Dhanesh Kizhakkinan, Jacob Thompson. (2025, January 8). Ivanti Connect Secure VPN Targeted in New Zero-Day Exploitation. Retrieved April 14, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-connect-secure-vpn-zero-day)
- [Matt Lin, Austin Larsen, John Wolfram, Ashley Pearson, Josh Murchie, Lukasz Lamparski, Joseph Pisano, Ryan Hall, Ron Craft, Shawn Crew, Billy Wong, Tyler McLellan. (2024, April 4). Cutting Edge, Part 4: Ivanti Connect Secure VPN Post-Exploitation Lateral Movement Case Studies. Retrieved April 16, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement)
- [Amanda Steward. (2014). FireEye DLL Side-Loading: A Thorn in the Side of the Anti-Virus Industry. Retrieved March 13, 2020.](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-dll-sideloading.pdf)
- [PowerSploit. (n.d.). Retrieved December 4, 2014.](https://github.com/mattifestation/PowerSploit)
- [Microsoft. (n.d.). CreateProcess function. Retrieved September 12, 2024.](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)
- [Microsoft. (n.d.). Dynamic-Link Library Security. Retrieved July 25, 2016.](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-security?redirectedfrom=MSDN)
- [Kanthak, S.. (2016, July 20). Vulnerability and Exploit Detector. Retrieved February 3, 2017.](https://skanthak.homepage.t-online.de/sentinel.html)
- [Microsoft. (2010, August 12). More information about the DLL Preloading remote attack vector. Retrieved December 5, 2014.](https://msrc-blog.microsoft.com/2010/08/23/more-information-about-the-dll-preloading-remote-attack-vector/)
- [Microsoft. (2018, May 31). Dynamic-Link Library Search Order. Retrieved November 30, 2014.](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order?redirectedfrom=MSDN)
- [Stefan Kanthak. (2015, December 8). Executable installers are vulnerable^WEVIL (case 7): 7z*.exe allows remote code execution with escalation of privilege. Retrieved December 4, 2014.](https://seclists.org/fulldisclosure/2015/Dec/34)

---

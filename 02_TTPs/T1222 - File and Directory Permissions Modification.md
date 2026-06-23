# File and Directory Permissions Modification

## Description

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files. [1] [2] File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Modifications may include changing specific access rights, which may require taking ownership of a file or directory and/or elevated permissions depending on the file or directory’s existing permissions. This may enable malicious activity such as modifying, replacing, or deleting specific files or directories. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via Accessibility Features , Boot or Logon Initialization Scripts , Unix Shell Configuration Modification , or tainting/hijacking other instrumental binary/configuration files via Hijack Execution Flow .

Adversaries may also change permissions of symbolic links. For example, malware (particularly ransomware) may modify symbolic links and associated settings to enable access to files from local shortcuts with remote paths. [3] [4] [5] [6] [7]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1242 | Qilin | Qilin can use symbolic links to redirect file paths for remote and local objects and can use chmod +x to make its payload binary executable. [8] [9] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1026 | Privileged Account Management | Ensure critical system files as well as those known to be abused by adversaries have restrictive permissions and are owned by an appropriately privileged account, especially if access is not required by users nor will inhibit system functionality. |
| M1022 | Restrict File and Directory Permissions | Applying more restrictive permissions to files and directories could prevent adversaries from modifying their access control lists. Additionally, ensure that user settings regarding local and remote symbolic links are properly set or disabled where unneeded. [10] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0299 | Multi-Platform File and Directory Permissions Modification Detection Strategy | AN0834 | Sequential behavioral chain of privilege escalation through permission modification: (1) Process creation of permission-modifying utilities (icacls, takeown, attrib, cacls), (2) Correlation with unusual user context or timing, (3) DACL modification events targeting sensitive files/directories, (4) Subsequent file access or modification attempts indicating successful privilege bypass |
| AN0835 | Behavioral sequence of unauthorized privilege escalation via permission modification: (1) chmod/chown/setfacl process execution with suspicious parameters, (2) Targeting of critical system files or unusual permission values, (3) Correlation with non-privileged user context or unusual timing patterns, (4) Follow-on file access indicating successful permission bypass |  |  |
| AN0836 | macOS-specific permission modification behavioral chain: (1) chmod/chown/chflags process execution, (2) System Integrity Protection (SIP) bypass attempts, (3) Extended attribute (xattr) modifications, (4) Unified log correlation with file system events, (5) Subsequent access to previously restricted resources |  |  |
| AN0837 | ESXi hypervisor permission modification behavioral chain: (1) SSH access to ESXi host, (2) chmod/chown execution on VMFS datastore files or system configuration, (3) Modification of VM configuration files (.vmx) or virtual disk permissions, (4) Hostd service log correlation, (5) vCenter permission change events if centrally managed |  |  |

---

## References

- [Hybrid Analysis. (2018, June 12). c9b65b764985dfd7a11d3faf599c56b8.exe. Retrieved August 19, 2018.](https://www.hybrid-analysis.com/sample/ef0d2628823e8e0a0de3b08b8eacaf41cf284c086a948bdfd67f4e4373c14e4d?environmentId=100)
- [Hybrid Analysis. (2018, May 30). 2a8efbfadd798f6111340f7c1c956bee.dll. Retrieved August 19, 2018.](https://www.hybrid-analysis.com/sample/22dab012c3e20e3d9291bce14a2bfc448036d3b966c6e78167f4626f5f9e38d6?environmentId=110)
- [Symantec Threat Hunter Team. (2021, December 16). Noberus: Technical Analysis Shows Sophistication of New Rust-based Ransomware. Retrieved January 14, 2022.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/noberus-blackcat-alphv-rust-ransomware)
- [Kaspersky Global Research & Analysis Team (GReAT). (2022). A Bad Luck BlackCat. Retrieved May 5, 2022.](https://go.kaspersky.com/rs/802-IJN-240/images/TR_BlackCat_Report.pdf)
- [Falcon OverWatch Team. (2022, March 23). Falcon OverWatch Threat Hunting Contributes to Seamless Protection Against Novel BlackCat Attack. Retrieved May 5, 2022.](https://www.crowdstrike.com/blog/falcon-overwatch-contributes-to-blackcat-protection/)
- [Pereira, T. Huey, C. (2022, March 17). From BlackMatter to BlackCat: Analyzing two attacks from one affiliate. Retrieved May 5, 2022.](https://blog.talosintelligence.com/2022/03/from-blackmatter-to-blackcat-analyzing.html)
- [Microsoft. (2021, September 27). fsutil behavior. Retrieved January 14, 2022.](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-behavior)
- [Hacioglu, S. (2025, March 10). Qilin Ransomware: Exposing the TTPs Behind One of the Most Active Ransomware Campaigns of 2024. Retrieved September 26, 2025.](https://www.picussecurity.com/resource/blog/qilin-ransomware)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [Microsoft. (2021, October 28). Create symbolic links. Retrieved April 27, 2022.](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links)

---

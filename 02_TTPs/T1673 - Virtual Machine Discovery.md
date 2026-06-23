# Virtual Machine Discovery

## Description

An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervisor. For example, adversaries may enumerate a list of VMs on an ESXi hypervisor using a Hypervisor CLI such as esxcli or vim-cmd (e.g. esxcli vm process list or vim-cmd vmsvc/getallvms ). [1] [2] Adversaries may also directly leverage a graphical user interface, such as VMware vCenter, in order to view virtual machines on a host.

Adversaries may use the information from Virtual Machine Discovery during discovery to shape follow-on behaviors. Subsequently discovered VMs may be leveraged for follow-on activities such as Service Stop or Data Encrypted for Impact . [1]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1096 | Cheerscrypt | Cheerscrypt has leveraged esxcli vm process list in order to gather a list of running virtual machines to terminate them. [3] |
| S9019 | PureCrypter | PureCrypter can identify virtual machines by querying the WMI object Win32_ComputerSystem for manufacturer and model and check it against the regular expression Microsoft|VMWare|Virtual. [4] |
| S1242 | Qilin | Qilin can detect virtual machine environments including ESXi hosts, datacenters, and clusters within vCenter environments. [5] [6] |
| G1048 | UNC3886 | UNC3886 has used scripts to enumerate ESXi hypervisors and their guest VMs. [7] |
| S1217 | VIRTUALPITA | VIRTUALPITA can target specific guest virtual machines for script execution. [8] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0199 | Detection Strategy for Virtual Machine Discovery | AN0572 | Monitor for execution of hypervisor management commands such as esxcli vm process list or vim-cmd vmsvc/getallvms that enumerate virtual machines. Defenders observe unexpected users issuing VM listing commands outside normal administrative workflows. |
| AN0573 | Detects attempts to enumerate VMs via hypervisor tools like virsh , VBoxManage , or qemu-img . Defender correlates suspicious command invocations with parent process lineage and unexpected users. |  |  |
| AN0574 | Detects enumeration of VMs using PowerShell ( Get-VM ), VMware Workstation ( vmrun.exe ), or Hyper-V ( VBoxManage.exe ). Defender observes suspicious command lines executed by unexpected users or outside normal administrative sessions. |  |  |
| AN0575 | Detects VM enumeration attempts using virtualization utilities such as VirtualBox ( VBoxManage ) or Parallels CLI. Defender observes abnormal invocation of VM listing commands correlated with non-admin users or unusual parent processes. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0199 | Detection Strategy for Virtual Machine Discovery | AN0572 | Monitor for execution of hypervisor management commands such as esxcli vm process list or vim-cmd vmsvc/getallvms that enumerate virtual machines. Defenders observe unexpected users issuing VM listing commands outside normal administrative workflows. |
| AN0573 | Detects attempts to enumerate VMs via hypervisor tools like virsh , VBoxManage , or qemu-img . Defender correlates suspicious command invocations with parent process lineage and unexpected users. |  |  |
| AN0574 | Detects enumeration of VMs using PowerShell ( Get-VM ), VMware Workstation ( vmrun.exe ), or Hyper-V ( VBoxManage.exe ). Defender observes suspicious command lines executed by unexpected users or outside normal administrative sessions. |  |  |
| AN0575 | Detects VM enumeration attempts using virtualization utilities such as VirtualBox ( VBoxManage ) or Parallels CLI. Defender observes abnormal invocation of VM listing commands correlated with non-admin users or unusual parent processes. |  |  |

---

## References

- [Michael Dawson. (2021, August 30). Hypervisor Jackpotting, Part 2: eCrime Actors Increase Targeting of ESXi Servers with Ransomware. Retrieved March 26, 2025.](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
- [Cj Arsley Mateo, Darrel Tristan Virtusio, Sarah Pearl Camiling, Andrei Alimboyao, Nathaniel Morales, Jacob Santos, Earl John Bareng. (2024, July 19). Play Ransomware Group’s New Linux Variant Targets ESXi, Shows Ties With Prolific Puma. Retrieved March 26, 2025.](https://www.trendmicro.com/en_us/research/24/g/new-play-ransomware-linux-variant-targets-esxi-shows-ties-with-p.html)
- [Dela Cruz, A. et al. (2022, May 25). New Linux-Based Ransomware Cheerscrypt Targeting ESXi Devices Linked to Leaked Babuk Source Code. Retrieved December 19, 2023.](https://www.trendmicro.com/en_se/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html)
- [Dumont, R. (2022, June 13). Technical Analysis of PureCrypter: A Fully-Functional Loader Distributing Remote Access Trojans and Information Stealers. Retrieved April 16, 2026.](https://www.zscaler.com/blogs/security-research/technical-analysis-purecrypter)
- [Halcyon RISE Team. (2024, October 24). New Qilin.B Ransomware Variant Boasts Enhanced Encryption and Defense Evasion. Retrieved September 26, 2025.](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [Alexander Marvi, Brad Slaybaugh, Ron Craft, and Rufus Brown. (2023, June 13). VMware ESXi Zero-Day Used by Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)
- [Alexander Marvi, Jeremy Koppen, Tufail Ahmed, and Jonathan Lepore. (2022, September 29). Bad VIB(E)s Part One: Investigating Novel Malware Persistence Within ESXi Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)

---

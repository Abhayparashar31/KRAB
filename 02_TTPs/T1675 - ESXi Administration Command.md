# ESXi Administration Command

## Description

Adversaries may abuse ESXi administration services to execute commands on guest machines hosted within an ESXi virtual environment. Persistent background services on ESXi-hosted VMs, such as the VMware Tools Daemon Service, allow for remote management from the ESXi server. The tools daemon service runs as vmtoolsd.exe on Windows guest operating systems, vmware-tools-daemon on macOS, and vmtoolsd on Linux. [1]

Adversaries may leverage a variety of tools to execute commands on ESXi-hosted VMs – for example, by using the vSphere Web Services SDK to programmatically execute commands and scripts via APIs such as StartProgramInGuest , ListProcessesInGuest , ListFileInGuest , and InitiateFileTransferFromGuest . [2] [3] This may enable follow-on behaviors on the guest VMs, such as File and Directory Discovery , Data from Local System , or OS Credential Dumping .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G1048 | UNC3886 | UNC3886 used vmtoolsd.exe to run commands on guest virtual machines from a compromised ESXi host. [4] [2] [5] [6] |
| S1217 | VIRTUALPITA | VIRTUALPITA can execute commands on guest virtual machines from compromised ESXi hypervisors. [4] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1018 | User Account Management | If not required, restrict the permissions of users to perform Guest Operations on ESXi-hosted VMs. [7] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0232 | Detection Strategy for ESXi Administration Command | AN0646 | Detects anomalous usage of ESXi Guest Operations APIs such as StartProgramInGuest, ListProcessesInGuest, ListFileInGuest, or InitiateFileTransferFromGuest. Defender perspective focuses on unusual frequency of guest API calls, invocation from unexpected management accounts, or execution outside of business hours. These correlated signals indicate adversarial abuse of ESXi administrative services to run commands on guest VMs. |

---

## References

- [Broadcom. (n.d.). VMware Tools Services. Retrieved March 28, 2025.](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/tools/12-4-0/vmware-tools-administration-12-4-0/introduction-to-vmware-tools/vmware-tools-service.html)
- [Alexander Marvi, Brad Slaybaugh, Ron Craft, and Rufus Brown. (2023, June 13). VMware ESXi Zero-Day Used by Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/)
- [Broadcom. (n.d.). Running Guest OS Operations. Retrieved March 28, 2025.](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/web-services-sdk-programming-guide/virtual-machine-guest-operations/running-guest-os-operations.html)
- [Alexander Marvi, Jeremy Koppen, Tufail Ahmed, and Jonathan Lepore. (2022, September 29). Bad VIB(E)s Part One: Investigating Novel Malware Persistence Within ESXi Hypervisors. Retrieved March 26, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
- [Punsaen Boonyakarn, Shawn Chew, Logeswaran Nadarajan, Mathew Potaczek, Jakub Jozwiak, and Alex Marvi. (2024, June 18). Cloaked and Covert: Uncovering UNC3886 Espionage Operations. Retrieved September 24, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations)
- [Marvi, A. et al.. (2023, March 16). Fortinet Zero-Day and Custom Malware Used by Suspected Chinese Actor in Espionage Operation. Retrieved March 22, 2023.](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
- [Broadcom. (n.d.). Virtual Machine Guest Operations Privileges. Retrieved March 28, 2025.](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vsphere-security-7-0/defined-privileges/virtual-machine-guest-operations-privileges.html)

---

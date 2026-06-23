# Cloud Administration Command

## Description

Adversaries may abuse cloud management services to execute commands within virtual machines. Resources such as AWS Systems Manager, Azure RunCommand, and Runbooks allow users to remotely run scripts in virtual machines by leveraging installed virtual machine agents. [1] [2]

If an adversary gains administrative access to a cloud environment, they may be able to abuse cloud management services to execute commands in the environment’s virtual machines. Additionally, an adversary that compromises a service provider or delegated administrator account may similarly be able to leverage a Trusted Relationship to execute commands in connected virtual machines. [3]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S0677 | AADInternals | AADInternals can execute commands on Azure virtual machines using the VM agent. [4] |
| G0016 | APT29 | APT29 has used Azure Run Command and Azure Admin-on-Behalf-of (AOBO) to execute code on virtual machines. [3] |
| S1091 | Pacu | Pacu can run commands on EC2 instances using AWS Systems Manager Run Command. [5] |
| G1055 | VOID MANTICORE | VOID MANTICORE has abused built-in remote wipe or factory reset commands to wipe devices managed within an organization’s Cloud management solution impacting laptops, servers, and mobile devices. [6] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1026 | Privileged Account Management | Limit the number of cloud accounts with permissions to remotely execute commands on virtual machines, and ensure that these are not used for day-to-day operations. In Azure, limit the number of accounts with the roles Azure Virtual Machine Contributer and above, and consider using temporary Just-in-Time (JIT) roles to avoid permanently assigning privileged access to virtual machines. [7] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0545 | Detection Strategy for Cloud Administration Command | AN1502 | Monitor for suspicious use of cloud-native administrative command services (e.g., AWS Systems Manager Run Command, Azure RunCommand, GCP OS Config) to execute code inside VMs. Detect anomalies such as commands/scripts executed by unexpected users, execution outside of maintenance windows, or commands initiated by service accounts not normally tied to administration. Correlate cloud control-plane activity logs with host-level execution (process creation, script execution) to validate if commands materialized inside the guest OS. |

---

## References

- [AWS. (n.d.). AWS Systems Manager Run Command. Retrieved March 13, 2023.](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html)
- [Microsoft. (2023, March 10). Run scripts in your VM by using Run Command. Retrieved March 13, 2023.](https://learn.microsoft.com/en-us/azure/virtual-machines/run-command-overview)
- [Microsoft Threat Intelligence Center. (2021, October 25). NOBELIUM targeting delegated administrative privileges to facilitate broader attacks. Retrieved March 25, 2022.](https://www.microsoft.com/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks/)
- [Dr. Nestori Syynimaa. (2020, June 4). Getting root access to Azure VMs as a Azure AD Global Administrator. Retrieved March 13, 2023.](https://aadinternals.com/post/azurevms/)
- [Rhino Security Labs. (2019, August 22). Pacu. Retrieved October 17, 2019.](https://github.com/RhinoSecurityLabs/pacu)
- [Justin Moore. (2026, March 16). Iranian Cyber Threat Evolution: From MBR Wipers to Identity Weaponization. Retrieved April 20, 2026.](https://unit42.paloaltonetworks.com/evolution-of-iran-cyber-threats/)
- [Adrien Bataille, Anders Vejlby, Jared Scott Wilson, and Nader Zaveri. (2021, December 14). Azure Run Command for Dummies. Retrieved March 13, 2023.](https://www.mandiant.com/resources/blog/azure-run-command-dummies)

---

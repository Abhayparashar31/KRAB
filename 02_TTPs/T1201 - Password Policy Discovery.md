# Password Policy Discovery

## Description

Adversaries may attempt to access detailed information about the password policy used within an enterprise network or cloud environment. Password policies are a way to enforce complex passwords that are difficult to guess or crack through Brute Force . This information may help the adversary to create a list of common passwords and launch dictionary and/or brute force attacks which adheres to the policy (e.g. if the minimum password length should be 8, then not trying passwords such as 'pass123'; not checking for more than 3-4 passwords per account if the lockout is set to 6 as to not lock out accounts).

Password policies can be set and discovered on Windows, Linux, and macOS systems via various command shell utilities such as net accounts (/domain) , Get-ADDefaultDomainPasswordPolicy , chage -l , cat /etc/pam.d/common-password , and pwpolicy getaccountpolicies [1] [2] . Adversaries may also leverage a Network Device CLI on network devices to discover password policy information (e.g. show aaa , show aaa common-criteria policy all ). [3]

Password policies can be discovered in cloud environments using available APIs such as GetAccountPasswordPolicy in AWS [4] .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0114 | Chimera | Chimera has used the NtdsAudit utility to collect information related to accounts and passwords. [5] |
| S0488 | CrackMapExec | CrackMapExec can discover the password policies applied to the target system. [6] |
| S0236 | Kwampirs | Kwampirs collects password policy information with the command net accounts . [7] |
| S0039 | Net | The net accounts and net accounts /domain commands with Net can be used to obtain password policy information. [8] |
| G0049 | OilRig | OilRig has used net.exe in a script with net accounts /domain to find the password policy of a domain. [9] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors used the net accounts command as part of their advanced reconnaissance. [10] |
| S0378 | PoshC2 | PoshC2 can use Get-PassPol to enumerate the domain password policy. [11] |
| G0010 | Turla | Turla has used net accounts and net accounts /domain to acquire password policy information. [12] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1027 | Password Policies | Ensure only valid password filters are registered. Filter DLLs must be present in Windows installation directory ( C:\Windows\System32\ by default) of a domain controller and/or local computer with a corresponding entry in HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Notification Packages . [13] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0161 | Password Policy Discovery – cross-platform behavior-chain analytics | AN0455 | Cause→effect chain: (1) a user or service spawns a shell/PowerShell that queries local/domain password policy via commands/cmdlets (e.g., net accounts , Get-ADDefaultDomainPasswordPolicy , secedit /export ); (2) optional directory/LDAP reads from DCs; (3) same principal performs adjacent Discovery or credential-related actions within a short window. Correlate sysmon process creation with PowerShell ScriptBlock and Security logs. |
| AN0456 | Chain: (1) interactive/non-interactive chage -l , grep / cat of PAM config (e.g., /etc/pam.d/common-password , /etc/security/pwquality.conf ); (2) optional reads of /etc/login.defs ; (3) same user performs account enumeration or password change attempts shortly after. Use auditd execve and file read events plus shell history collection. |  |  |
| AN0457 | Chain: (1) execution of pwpolicy or MDM/DirectoryService reads of account policies; (2) optional read of /Library/Preferences/com.apple.loginwindow or config profiles; (3) follow-on credential probing or lateral movement by same user/session. Use unified logs and process telemetry. |  |  |
| AN0458 | Chain: (1) cloud API calls that fetch tenant/organization password policy (e.g., AWS GetAccountPasswordPolicy , GCP/OCI equivalents or IAM settings reads); (2) within a short window, the same principal creates users, rotates creds, or changes auth settings. Use cloud audit logs. |  |  |
| AN0459 | Chain: (1) IdP policy/read operations by a principal (e.g., Microsoft Entra/Graph requests to read password or authentication policies); (2) adjacent risky changes (role assignment, app consent) by same principal. Use IdP audit logs. |  |  |
| AN0460 | Chain: (1) SaaS admin API or PowerShell remote session reads tenant password/authentication settings (e.g., M365 Unified Audit Log ‘Cmdlet’ with Get-MsolPasswordPolicy / Get-OrganizationConfig parameters that expose password settings); (2) same session proceeds to mailbox or tenant changes. |  |  |
| AN0461 | Chain: (1) privileged CLI sessions run read-only commands that dump AAA/password policies (e.g., show aaa , show password-policy ); (2) same account changes AAA or user DB shortly after. Use network device AAA/command accounting or syslog. |  |  |

---

## References

- [Matutiae, M. (2014, August 6). How to display password policy information for a user (Ubuntu)?. Retrieved April 5, 2018.](https://superuser.com/questions/150675/how-to-display-password-policy-information-for-a-user-ubuntu)
- [Holland, J. (2016, January 25). User password policies on non AD machines. Retrieved April 5, 2018.](https://www.jamf.com/jamf-nation/discussions/18574/user-password-policies-on-non-ad-machines)
- [US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved October 19, 2020.](https://www.us-cert.gov/ncas/alerts/TA18-106A)
- [Amazon Web Services. (n.d.). AWS API GetAccountPasswordPolicy. Retrieved June 8, 2021.](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountPasswordPolicy.html)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [byt3bl33d3r. (2018, September 8). SMB: Command Reference. Retrieved July 17, 2020.](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
- [Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
- [Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.](https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference)
- [Singh, S., Yin, H. (2016, May 22). https://www.fireeye.com/blog/threat-research/2016/05/targeted_attacksaga.html. Retrieved November 17, 2024.](https://web.archive.org/web/20200618235708/https://www.fireeye.com/blog/threat-research/2016/05/targeted_attacksaga.html)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [Microsoft. (n.d.). Installing and Registering a Password Filter DLL. Retrieved November 21, 2017.](https://msdn.microsoft.com/library/windows/desktop/ms721766.aspx)

---

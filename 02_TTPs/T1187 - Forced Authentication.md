# Forced Authentication

## Description

Adversaries may gather credential material by invoking or forcing a user to automatically provide authentication information through a mechanism in which they can intercept.

The Server Message Block (SMB) protocol is commonly used in Windows networks for authentication and communication between systems for access to resources and file sharing. When a Windows system attempts to connect to an SMB resource it will automatically attempt to authenticate and send credential information for the current user to the remote system. [1] This behavior is typical in enterprise environments so that users do not need to enter credentials to access network resources.

Web Distributed Authoring and Versioning (WebDAV) is also typically used by Windows systems as a backup protocol when SMB is blocked or fails. WebDAV is an extension of HTTP and will typically operate over TCP ports 80 and 443. [2] [3]

Adversaries may take advantage of this behavior to gain access to user account hashes through forced SMB/WebDAV authentication. An adversary can send an attachment to a user through spearphishing that contains a resource link to an external server controlled by the adversary (i.e. Template Injection ), or place a specially crafted file on navigation path for privileged accounts (e.g. .SCF file placed on desktop) or on a publicly accessible share to be accessed by victim(s). When the user's system accesses the untrusted resource, it will attempt authentication and send information, including the user's hashed credentials, over SMB to the adversary-controlled server. [4] With access to the credential hash, an adversary can perform off-line Brute Force cracking to gain access to plaintext credentials. [5]

There are several different ways this can occur. [6] Some specifics from in-the-wild use include:

Alternatively, by leveraging the EfsRpcOpenFileRaw function, an adversary can send SMB requests to a remote system's MS-EFSRPC interface and force the victim computer to initiate an authentication procedure and share its authentication details. The Encrypting File System Remote Protocol (EFSRPC) is a protocol used in Windows networks for maintenance and management operations on encrypted data that is stored remotely to be accessed over a network. Utilization of EfsRpcOpenFileRaw function in EFSRPC is used to open an encrypted object on the server for backup or restore. Adversaries can collect this data and abuse it as part of a NTLM relay attack to gain access to remote systems on the same internal network. [8] [9]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0079 | DarkHydrus | DarkHydrus used Template Injection to launch an authentication window for users to enter their credentials. [10] |
| G0035 | Dragonfly | Dragonfly has gathered hashed user credentials over SMB using spearphishing attachments with external resource links and by modifying .LNK file icon resources to collect credentials from virtualized systems. [11] [12] |
| S0634 | EnvyScout | EnvyScout can use protocol handlers to coax the operating system to send NTLMv2 authentication responses to attacker-controlled infrastructure. [13] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1037 | Filter Network Traffic | Block SMB traffic from exiting an enterprise network with egress filtering or by blocking TCP ports 139, 445 and UDP port 137. Filter or block WebDAV protocol traffic from exiting the network. If access to external resources over SMB and WebDAV is necessary, then traffic should be tightly limited with allowlisting. [14] [7] |
| M1027 | Password Policies | Use strong passwords to increase the difficulty of credential hashes from being cracked if they are obtained. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0022 | Detect Forced SMB/WebDAV Authentication via lure files and outbound NTLM | AN0065 | Adversary stages a lure that references a remote resource (e.g., LNK/SCF/Office template). When the user opens/renders the file or a shell enumerates icons, the host automatically attempts SMB or WebDAV authentication to the attacker host. The chain is: (1) lure file is created or modified in a user-exposed location → (2) user or system accesses the lure → (3) host makes outbound NTLM (SMB 139/445 or WebDAV over 80/443) to an untrusted destination → (4) repeated attempts from multiple users/hosts or from privileged workstations. |

---

## References

- [Wikipedia. (2017, December 16). Server Message Block. Retrieved December 21, 2017.](https://en.wikipedia.org/wiki/Server_Message_Block)
- [Stevens, D. (2017, November 13). WebDAV Traffic To Malicious Sites. Retrieved December 21, 2017.](https://blog.didierstevens.com/2017/11/13/webdav-traffic-to-malicious-sites/)
- [Microsoft. (n.d.). Managing WebDAV Security (IIS 6.0). Retrieved November 17, 2024.](https://web.archive.org/web/20100210125749/https://www.microsoft.com/technet/prodtechnol/WindowsServer2003/Library/IIS/4beddb35-0cba-424c-8b9b-a5832ad8e208.mspx)
- [Dunning, J. (2016, August 1). Hashjacking. Retrieved December 21, 2017.](https://github.com/hob0/hashjacking)
- [Cylance. (2015, April 13). Redirect to SMB. Retrieved December 21, 2017.](https://www.cylance.com/content/dam/cylance/pdfs/white_papers/RedirectToSMB.pdf)
- [Osanda Malith Jayathissa. (2017, March 24). Places of Interest in Stealing NetNTLM Hashes. Retrieved January 26, 2018.](https://osandamalith.com/2017/03/24/places-of-interest-in-stealing-netntlm-hashes/)
- [US-CERT. (2017, October 20). Alert (TA17-293A): Advanced Persistent Threat Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved November 2, 2017.](https://www.us-cert.gov/ncas/alerts/TA17-293A)
- [Condon, Caitlin. (2022, April 24). PetitPotam: Novel Attack Chain Can Fully Compromise Windows Domains. Retrieved May 30, 2025.](https://www.rapid7.com/blog/post/2021/08/03/petitpotam-novel-attack-chain-can-fully-compromise-windows-domains-running-ad-cs/)
- [topotam. (2021, July 18). PetitPotam. PoC tool to coerce Windows hosts to authenticate to other machines. Retrieved May 30, 2025.](https://github.com/topotam/PetitPotam)
- [Falcone, R. (2018, August 07). DarkHydrus Uses Phishery to Harvest Credentials in the Middle East. Retrieved August 10, 2018.](https://researchcenter.paloaltonetworks.com/2018/08/unit42-darkhydrus-uses-phishery-harvest-credentials-middle-east/)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [Slowik, J. (2021, October). THE BAFFLING BERSERK BEAR: A DECADE’S ACTIVITY TARGETING CRITICAL INFRASTRUCTURE. Retrieved December 6, 2021.](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
- [MSTIC. (2021, May 28). Breaking down NOBELIUM’s latest early-stage toolset. Retrieved August 4, 2021.](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
- [US-CERT. (2017, March 16). SMB Security Best Practices. Retrieved December 21, 2017.](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)

---

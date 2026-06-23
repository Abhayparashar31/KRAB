# Data Encrypted for Impact

## Description

Adversaries may encrypt data on target systems or on large numbers of systems in a network to interrupt availability to system and network resources. They can attempt to render stored data inaccessible by encrypting files or data on local and remote drives and withholding access to a decryption key. This may be done in order to extract monetary compensation from a victim in exchange for decryption or a decryption key (ransomware) or to render data permanently inaccessible in cases where the key is not saved or transmitted. [1] [2] [3] [4]

In the case of ransomware, it is typical that common user files like Office documents, PDFs, images, videos, audio, text, and source code files will be encrypted (and often renamed and/or tagged with specific file markers). Adversaries may need to first employ other behaviors, such as File and Directory Permissions Modification or System Shutdown/Reboot , in order to unlock and/or gain access to manipulate these files. [5] In some cases, adversaries may encrypt critical system files, disk partitions, and the MBR. [3] Adversaries may also encrypt virtual machines hosted on ESXi or other hypervisors. [6]

To maximize impact on the target organization, malware designed for encrypting data may have worm-like features to propagate across a network by leveraging other attack techniques like Valid Accounts , OS Credential Dumping , and SMB/Windows Admin Shares . [2] [3] Encryption malware may also leverage Internal Defacement , such as changing victim wallpapers or ESXi server login messages, or otherwise intimidate victims by sending ransom notes or other messages to connected printers (known as "print bombing"). [7] [8]

In cloud environments, storage objects within compromised accounts may also be encrypted. [9] For example, in AWS environments, adversaries may leverage services such as AWS’s Server-Side Encryption with Customer Provided Keys (SSE-C) to encrypt data. [10]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| S1129 | Akira | Akira can encrypt victim filesystems for financial extortion purposes including through the use of the ChaCha20 and ChaCha8 stream ciphers. [11] [12] [13] |
| G1024 | Akira | Akira encrypts files in victim environments as part of ransomware operations. [14] [12] |
| S1194 | Akira _v2 | The Akira _v2 encryptor targets the /vmfs/volumes/ path by default and can use the rust-crypto 0.2.36 library crate for the encryption processes. [13] [15] |
| S1133 | Apostle | Apostle creates new, encrypted versions of files then deletes the originals, with the new filenames consisting of a random GUID and ".lock" for an extension. [16] |
| G0082 | APT38 | APT38 has used Hermes ransomware to encrypt files with AES256. [17] |
| G0096 | APT41 | APT41 used a ransomware called Encryptor RaaS to encrypt files on the targeted systems and provide a ransom note to the user. [18] APT41 also used Microsoft Bitlocker to encrypt workstations and Jetico’s BestCrypt to encrypt servers. [19] |
| S0640 | Avaddon | Avaddon encrypts the victim system using a combination of AES256 and RSA encryption schemes. [20] |
| S1053 | AvosLocker | AvosLocker has encrypted files and network resources using AES-256 and added an .avos , .avos2 , or .AvosLinux extension to filenames. [21] [22] [23] [24] |
| S0638 | Babuk | Babuk can use ChaCha8 and ECDH to encrypt data. [25] [26] [27] [28] |
| S0606 | Bad Rabbit | Bad Rabbit has encrypted files and disks using AES-128-CBC and RSA-2048. [29] |
| S0570 | BitPaymer | BitPaymer can import a hard-coded RSA 1024-bit public key, generate a 128-bit RC4 key for each file, and encrypt the file in place, appending .locked to the filename. [30] |
| S1070 | Black Basta | Black Basta can encrypt files with the ChaCha20 cypher and using a multithreaded process to increase speed. [31] [32] [33] [34] [35] [36] [37] [38] [39] Black Basta has also encrypted files while the victim system is in safe mode, appending .basta upon completion. [40] |
| G1043 | BlackByte | BlackByte has encrypted victim files for ransom. Early versions of BlackByte ransomware used a common key for encryption, but later versions use unique keys per victim. [41] [42] [43] [44] [45] |
| S1181 | BlackByte 2.0 Ransomware | BlackByte 2.0 Ransomware is a ransomware variant associated with BlackByte operations. [44] |
| S1180 | BlackByte Ransomware | BlackByte Ransomware is ransomware using a shared key across victims for encryption. [46] |
| S1068 | BlackCat | BlackCat has the ability to encrypt Windows devices, Linux devices, and VMWare instances. [47] |
| C0015 | C0015 | During C0015 , the threat actors used Conti ransomware to encrypt a compromised network. [48] |
| C0018 | C0018 | During C0018 , the threat actors used AvosLocker ransomware to encrypt files on the compromised network. [23] [49] |
| S1096 | Cheerscrypt | Cheerscrypt can encrypt data on victim machines using a Sosemanuk stream cipher with an Elliptic-curve Diffie–Hellman (ECDH) generated key. [50] [51] |
| S0611 | Clop | Clop can encrypt files using AES, RSA, and RC4 and will add the ".clop" extension to encrypted files. [52] [53] [54] |
| S0575 | Conti | Conti can use CreateIoCompletionPort() , PostQueuedCompletionStatus() , and GetQueuedCompletionPort() to rapidly encrypt files, excluding those with the extensions of .exe, .dll, and .lnk. It has used a different AES-256 encryption key per file with a bundled RAS-4096 public encryption key that is unique for each victim. Conti can use "Windows Restart Manager" to ensure files are unlocked and open for encryption. [55] [5] [56] [57] [48] |
| S0625 | Cuba | Cuba has the ability to encrypt system data and add the ".cuba" extension to encrypted files. [58] |
| S1111 | DarkGate | DarkGate can deploy follow-on ransomware payloads. [59] |
| S1033 | DCSrv | DCSrv has encrypted drives using the core encryption mechanism from DiskCryptor. [60] |
| S0616 | DEATHRANSOM | DEATHRANSOM can use public and private key pair encryption to encrypt files for ransom payment. [61] |
| S0659 | Diavol | Diavol has encrypted files using an RSA key though the CryptEncrypt API and has appended filenames with ".lock64". [62] |
| S0554 | Egregor | Egregor can encrypt all non-system files using a hybrid AES-RSA algorithm prior to displaying a ransom note. [7] [63] |
| S0605 | EKANS | EKANS uses standard encryption library functions to encrypt files. [64] [65] |
| S1247 | Embargo | Embargo has the ability to encrypt files with the ChaCha20 and Curve25519 cryptographic algorithms. [66] Embargo also has the ability to encrypt system data and add a random six-letter extension consisting of hexadecimal characters such as ".b58eeb" or ".3d828a" to encrypted files. [67] |
| G0046 | FIN7 | FIN7 has encrypted virtual disk volumes on ESXi servers using a version of Darkside ransomware. [68] [69] Additionally, FIN7 has deployed ransomware as the end payload during big game hunting. [70] |
| G0061 | FIN8 | FIN8 has deployed ransomware such as Ragnar Locker , White Rabbit, and attempted to execute Noberus on compromised networks. [71] |
| S0618 | FIVEHANDS | FIVEHANDS can use an embedded NTRU public key to encrypt data for ransom. [61] [72] [73] |
| S0617 | HELLOKITTY | HELLOKITTY can use an embedded RSA-2048 public key to encrypt victim data for ransom. [61] |
| C0038 | HomeLand Justice | During HomeLand Justice , threat actors used ROADSWEEP ransomware to encrypt files on targeted systems. [74] [75] [76] |
| G1032 | INC Ransom | INC Ransom has used INC Ransomware to encrypt victim's data. [77] [78] [79] [80] [81] [82] |
| S1139 | INC Ransomware | INC Ransomware can encrypt data on victim systems, including through the use of partial encryption and multi-threading to speed encryption. [77] [78] [81] [82] [77] |
| G0119 | Indrik Spider | Indrik Spider has encrypted domain-controlled systems using BitPaymer . [30] Additionally, Indrik Spider used PsExec to execute a ransomware script. [83] |
| S0389 | JCry | JCry has encrypted files and demanded Bitcoin to decrypt those files. [84] |
| S0607 | KillDisk | KillDisk has a ransomware component that encrypts files with an AES key that is also RSA-1028 encrypted. [85] |
| S1199 | LockBit 2.0 | LockBit 2.0 can use standard AES and elliptic-curve cryptography algorithms to encrypt victim data. [86] [87] |
| S1202 | LockBit 3.0 | LockBit 3.0 can encrypt targeted data using the AES-256, ChaCha20, or RSA-2048 algorithms. [88] [89] [90] [91] |
| S0372 | LockerGoga | LockerGoga has encrypted files, including core Windows OS files, using RSA-OAEP MGF1 and then demanded Bitcoin be paid for the decryption key. [92] [93] [94] |
| S9020 | LODEINFO | LODEINFO can incorporate a ransom command to encrypt specified files and folders. [95] [96] [97] |
| G0059 | Magic Hound | Magic Hound has used BitLocker and DiskCryptor to encrypt targeted workstations. [98] [99] |
| S0449 | Maze | Maze has disrupted systems by encrypting files on targeted machines, claiming to decrypt files if a ransom payment is made. Maze has used the ChaCha algorithm, based on Salsa20, and an RSA algorithm to encrypt files. [100] |
| G1051 | Medusa Group | Medusa Group has encrypted files using AES-256 encryption which then appends the file extension ".medusa" to encrypted files and leaves a ransomware note named "!READ_ME_MEDUSA!!!.txt." [101] [102] [103] [104] |
| S1244 | Medusa Ransomware | Medusa Ransomware has encrypted files using AES-256 encryption, which then appends the file extension ".medusa" to encrypted files and leaves a ransomware note named "!READ_ME_MEDUSA!!!.txt." [101] [102] [103] [104] |
| S0576 | MegaCortex | MegaCortex has used the open-source library, Mbed Crypto, and generated AES keys to carry out the file encryption process. [105] [106] |
| S1191 | Megazord | Megazord can encrypt files on targeted Windows hosts leaving them with a ".powerranges" file extension. [12] [13] [15] |
| S1137 | Moneybird | Moneybird targets a common set of file types such as documents, certificates, and database files for encryption while avoiding executable, dynamic linked libraries, and similar items. [107] |
| G1036 | Moonstone Sleet | Moonstone Sleet has deployed ransomware in victim environments. [108] |
| S0457 | Netwalker | Netwalker can encrypt files on infected machines to extort victims. [109] |
| S0368 | NotPetya | NotPetya encrypts user files and disk structures like the MBR with 2048-bit RSA. [110] [3] [111] |
| S0556 | Pay2Key | Pay2Key can encrypt data on victim's machines using RSA and AES algorithms in order to extort a ransom payment for decryption. [112] [113] |
| S1162 | Playcrypt | Playcrypt encrypts files on targeted hosts with an AES-RSA hybrid encryption, encrypting every other file portion of 0x100000 bytes. [114] [115] |
| S1058 | Prestige | Prestige has leveraged the CryptoPP C++ library to encrypt files on target systems using AES and appended filenames with .enc . [116] |
| S0654 | ProLock | ProLock can encrypt files on a compromised host with RC6, and encrypts the key with RSA-1024. [117] |
| S0583 | Pysa | Pysa has used RSA and AES-CBC encryption algorithm to encrypt a list of targeted file extensions. [118] |
| S1242 | Qilin | Qilin can use AES-256 or ChaCha20 for domain-wide encryption of victim servers and workstations and RSA-4096 or RSA-2048 to secure generated encryption keys. [119] [120] [121] [122] [123] [124] [125] [126] |
| S0481 | Ragnar Locker | Ragnar Locker encrypts files on the local machine and mapped drives prior to displaying a note demanding a ransom. [127] [128] |
| S1212 | RansomHub | RansomHub can use Elliptic Curve Encryption to encrypt files on targeted systems. [129] RansomHub can also skip content at regular intervals (ex. encrypt 1 MB, skip 3 MB) to optomize performance and enable faster encryption for large files. [130] |
| S0496 | REvil | REvil can encrypt files on victim systems and demands a ransom to decrypt the files. [131] [132] [133] [134] [135] [136] [137] [138] |
| S1150 | ROADSWEEP | ROADSWEEP can RC4 encrypt content in blocks on targeted systems. [74] [75] [76] |
| S0400 | RobbinHood | RobbinHood will search for an RSA encryption key and then perform its encryption process on the system files. [139] |
| S1073 | Royal | Royal uses a multi-threaded encryption process that can partially encrypt targeted files with the OpenSSL library and the AES256 algorithm. [140] [141] [142] |
| S0446 | Ryuk | Ryuk has used a combination of symmetric (AES) and asymmetric (RSA) encryption to encrypt files. Files have been encrypted with their own AES key and given a file extension of .RYK. Encrypted directories have had a ransom note of RyukReadMe.txt written to the directory. [143] [57] |
| S0370 | SamSam | SamSam encrypts victim files using RSA-2048 encryption and demands a ransom be paid in Bitcoin to decrypt those files. [144] |
| G0034 | Sandworm Team | Sandworm Team has used Prestige ransomware to encrypt data at targeted organizations in transportation and related logistics industries in Ukraine and Poland. [116] |
| G1015 | Scattered Spider | Scattered Spider has used BlackCat and DragonForce ransomware to encrypt files including on VMWare ESXi servers. [145] [146] [147] [148] [149] |
| S0639 | Seth-Locker | Seth-Locker can encrypt files on a targeted system, appending them with the suffix .seth. [28] |
| S0140 | Shamoon | Shamoon has an operational mode for encrypting data instead of overwriting it. [150] [151] |
| C0058 | SharePoint ToolShell Exploitation | During SharePoint ToolShell Exploitation , threat actors deployed ransomware including 4L4MD4R and Warlock. [152] [153] |
| S1178 | ShrinkLocker | ShrinkLocker uses the legitimate BitLocker application to encrypt victim files for ransom. [154] [155] |
| G1053 | Storm-0501 | Storm-0501 has encrypted files in victim environments using ransomware as a service (RaaS) including Sabbath, Hive, BlackCat , Hunters International, LockBit 3.0 and Embargo ransomware. [156] |
| G1046 | Storm-1811 | Storm-1811 is a financially-motivated entity linked to the deployment of Black Basta ransomware in victim environments. [157] |
| S0242 | SynAck | SynAck encrypts the victims machine followed by asking the victim to pay a ransom. [158] |
| G0092 | TA505 | TA505 has used a wide variety of ransomware, such as Clop , Locky, Jaff, Bart, Philadelphia, and GlobeImposter, to encrypt victim files and demand a ransom payment. [159] |
| S0595 | ThiefQuest | ThiefQuest encrypts a set of file extensions on a host, deletes the original files, and provides a ransom note with no contact information. [160] |
| G1055 | VOID MANTICORE | VOID MANTICORE has utilized legitimate disk encryption utilities to increase likelihood of encrypting system drives and reduce system recovery efforts. [161] [162] |
| S0366 | WannaCry | WannaCry encrypts user files and demands that a ransom be paid in Bitcoin to decrypt those files. [163] [2] [164] |
| S0612 | WastedLocker | WastedLocker can encrypt data and leave a ransom note. [165] [166] [167] |
| G1050 | Water Galura | Water Galura has encrypted files on victim networks through the generation of Qilin ransomware payloads. [122] |
| S0341 | Xbash | Xbash has maliciously encrypted victim's database systems and demanded a cryptocurrency ransom be paid. [168] |
| S0658 | XCSSET | XCSSET performs AES-CBC encryption on files under ~/Documents , ~/Downloads , and ~/Desktop with a fixed key and renames files to give them a .enc extension. Only files with sizes less than 500MB are encrypted. [169] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1040 | Behavior Prevention on Endpoint | On Windows 10, enable cloud-delivered protection and Attack Surface Reduction (ASR) rules to block the execution of files that resemble ransomware. [170] In AWS environments, create an IAM policy to restrict or block the use of SSE-C on S3 buckets. [10] |
| M1053 | Data Backup | Consider implementing IT disaster recovery plans that contain procedures for regularly taking and testing data backups that can be used to restore organizational data. [171] Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. Consider enabling versioning in cloud environments to maintain backup copies of storage objects. [172] |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0215 | Detection of Multi-Platform File Encryption for Impact | AN0602 | High-frequency file write operations using uncommon extensions, followed by ransom note creation, registry tampering, or shadow copy deletion. Often uses CLI tools like vssadmin, wbadmin, cipher, or PowerShell. |
| AN0603 | Encryption via custom or open-source tools (e.g., openssl, gpg, aescrypt) recursively targeting user or system directories. Also includes overwrite of existing data and ransom note drops. |  |  |
| AN0604 | Userland or kernel-level ransomware encrypting user files (Documents, Desktop) using srm , gpg , or compiled payloads. Often correlated with ransom note creation in multiple directories. |  |  |
| AN0605 | Ransomware encrypts .vmdk, .vmx, .log, or VM config files in VMFS datastores. May rename to .locked or delete/overwrite with encrypted versions. Often correlates with shell commands run through dcui , SSH, or vSphere. |  |  |
| AN0606 | Encryption of cloud storage objects (e.g., S3 buckets) via Server-Side Encryption (SSE-C) or by replacing objects with encrypted variants. May include API patterns like PutObject with SSE-C headers. |  |  |

---

## References

- [US-CERT. (2016, March 31). Alert (TA16-091A): Ransomware and Recent Variants. Retrieved March 15, 2019.](https://www.us-cert.gov/ncas/alerts/TA16-091A)
- [Berry, A., Homan, J., and Eitzman, R. (2017, May 23). WannaCry Malware Profile. Retrieved March 15, 2019.](https://www.fireeye.com/blog/threat-research/2017/05/wannacry-malware-profile.html)
- [US-CERT. (2017, July 1). Alert (TA17-181A): Petya Ransomware. Retrieved March 15, 2019.](https://www.us-cert.gov/ncas/alerts/TA17-181A)
- [US-CERT. (2018, December 3). Alert (AA18-337A): SamSam Ransomware. Retrieved March 15, 2019.](https://www.us-cert.gov/ncas/alerts/AA18-337A)
- [Baskin, B. (2020, July 8). TAU Threat Discovery: Conti Ransomware. Retrieved February 17, 2021.](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [Michael Dawson. (2021, August 30). Hypervisor Jackpotting, Part 2: eCrime Actors Increase Targeting of ESXi Servers with Ransomware. Retrieved March 26, 2025.](https://www.crowdstrike.com/en-us/blog/hypervisor-jackpotting-ecrime-actors-increase-targeting-of-esxi-servers/)
- [NHS Digital. (2020, November 26). Egregor Ransomware The RaaS successor to Maze. Retrieved December 29, 2020.](https://digital.nhs.uk/cyber-alerts/2020/cc-3681#summary)
- [Jason Hill. (2023, February 8). VMware ESXi in the Line of Ransomware Fire. Retrieved March 26, 2025.](https://www.varonis.com/blog/vmware-esxi-in-the-line-of-ransomware-fire)
- [Gietzen, S. (n.d.). S3 Ransomware Part 1: Attack Vector. Retrieved April 14, 2021.](https://rhinosecuritylabs.com/aws/s3-ransomware-part-1-attack-vector/)
- [Halcyon RISE Team. (2025, January 13). Abusing AWS Native Services: Ransomware Encrypting S3 Buckets with SSE-C. Retrieved March 18, 2025.](https://www.halcyon.ai/blog/abusing-aws-native-services-ransomware-encrypting-s3-buckets-with-sse-c)
- [Max Kersten & Alexandre Mundo. (2023, November 29). Akira Ransomware. Retrieved April 4, 2024.](https://www.trellix.com/blogs/research/akira-ransomware/)
- [CISA et al. (2024, April 18). #StopRansomware: Akira Ransomware. Retrieved December 10, 2024.](https://www.cisa.gov/sites/default/files/2024-04/aa24-109a-stopransomware-akira-ransomware_2.pdf)
- [Nutland, J. and Szeliga, M. (2024, October 21). Akira ransomware continues to evolve. Retrieved December 10, 2024.](https://blog.talosintelligence.com/akira-ransomware-continues-to-evolve/)
- [Will Thomas. (2023, September 15). Tracking Adversaries: Akira, another descendent of Conti. Retrieved February 21, 2024.](https://blog.bushidotoken.net/2023/09/tracking-adversaries-akira-another.html)
- [Zemah, Y. (2024, December 2). Threat Assessment: Howling Scorpius (Akira Ransomware). Retrieved January 8, 2025.](https://unit42.paloaltonetworks.com/threat-assessment-howling-scorpius-akira-ransomware/)
- [Amitai Ben & Shushan Ehrlich. (2021, May). From Wiper to Ransomware: The Evolution of Agrius. Retrieved May 21, 2024.](https://assets.sentinelone.com/sentinellabs/evol-agrius)
- [FireEye. (2018, October 03). APT38: Un-usual Suspects. Retrieved November 17, 2024.](https://services.google.com/fh/files/misc/apt38-un-usual-suspects.pdf)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [DCSO CyTec Blog. (2022, December 24). APT41 — The spy who failed to encrypt me. Retrieved June 13, 2024.](https://medium.com/@DCSO_CyTec/apt41-the-spy-who-failed-to-encrypt-me-24fc0f49cad1)
- [Yuste, J. Pastrana, S. (2021, February 9). Avaddon ransomware: an in-depth analysis and decryption of infected systems. Retrieved August 19, 2021.](https://arxiv.org/pdf/2102.04796.pdf)
- [Hasherezade. (2021, July 23). AvosLocker enters the ransomware scene, asks for partners. Retrieved January 11, 2023.](https://www.malwarebytes.com/blog/threat-intelligence/2021/07/avoslocker-enters-the-ransomware-scene-asks-for-partners)
- [Trend Micro Research. (2022, April 4). Ransomware Spotlight AvosLocker. Retrieved January 11, 2023.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-avoslocker)
- [Venere, G. Neal, C. (2022, June 21). Avos ransomware group expands with new attack arsenal. Retrieved January 11, 2023.](https://blog.talosintelligence.com/avoslocker-new-arsenal/)
- [FBI, FinCEN, Treasury. (2022, March 17). Indicators of Compromise Associated with AvosLocker Ransomware. Retrieved January 11, 2023.](https://www.ic3.gov/Media/News/2022/220318.pdf)
- [Sogeti. (2021, March). Babuk Ransomware. Retrieved August 11, 2021.](https://www.sogeti.com/globalassets/reports/cybersecchronicles_-_babuk.pdf)
- [Mundo, A. et al. (2021, February). Technical Analysis of Babuk Ransomware. Retrieved August 11, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-babuk-ransomware.pdf)
- [Sebdraven. (2021, February 8). Babuk is distributed packed. Retrieved August 11, 2021.](https://sebdraven.medium.com/babuk-is-distributed-packed-78e2f5dd2e62)
- [Centero, R. et al. (2021, February 5). New in Ransomware: Seth-Locker, Babuk Locker, Maoloa, TeslaCrypt, and CobraLocker. Retrieved August 11, 2021.](https://www.trendmicro.com/en_us/research/21/b/new-in-ransomware.html)
- [Mamedov, O. Sinitsyn, F. Ivanov, A.. (2017, October 24). Bad Rabbit ransomware. Retrieved January 28, 2021.](https://securelist.com/bad-rabbit-ransomware/82851/)
- [Frankoff, S., Hartley, B. (2018, November 14). Big Game Hunting: The Evolution of INDRIK SPIDER From Dridex Wire Fraud to BitPaymer Targeted Ransomware. Retrieved January 6, 2021.](https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/)
- [Zargarov, N. (2022, May 2). New Black Basta Ransomware Hijacks Windows Fax Service. Retrieved March 7, 2023.](https://minerva-labs.com/blog/new-black-basta-ransomware-hijacks-windows-fax-service/)
- [Ballmer, D. (2022, May 6). Black Basta: Rebrand of Conti or Something New?. Retrieved March 7, 2023.](https://blogs.blackberry.com/en/2022/05/black-basta-rebrand-of-conti-or-something-new)
- [Cyble. (2022, May 6). New ransomware variant targeting high-value organizations. Retrieved November 17, 2024.](https://web.archive.org/web/20220506143054/https://blog.cyble.com/2022/05/06/black-basta-ransomware/)
- [Inman, R. and Gurney, P. (2022, June 6). Shining the Light on Black Basta. Retrieved March 8, 2023.](https://research.nccgroup.com/2022/06/06/shining-the-light-on-black-basta/)
- [Sharma, S. and Hegde, N. (2022, June 7). Black basta Ransomware Goes Cross-Platform, Now Targets ESXi Systems. Retrieved March 8, 2023.](https://www.uptycs.com/blog/black-basta-ransomware-goes-cross-platform-now-targets-esxi-systems)
- [Vilkomir-Preisman, S. (2022, August 18). Beating Black Basta Ransomware. Retrieved March 8, 2023.](https://www.deepinstinct.com/blog/black-basta-ransomware-threat-emergence)
- [Elsad, A. (2022, August 25). Threat Assessment: Black Basta Ransomware. Retrieved March 8, 2023.](https://unit42.paloaltonetworks.com/threat-assessment-black-basta-ransomware)
- [Trend Micro. (2022, September 1). Ransomware Spotlight Black Basta. Retrieved March 8, 2023.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-blackbasta)
- [Check Point. (2022, October 20). BLACK BASTA AND THE UNNOTICED DELIVERY. Retrieved March 8, 2023.](https://research.checkpoint.com/2022/black-basta-and-the-unnoticed-delivery/)
- [Gonzalez, I., Chavez I., et al. (2022, May 9). Examining the Black Basta Ransomware’s Infection Routine. Retrieved March 7, 2023.](https://www.trendmicro.com/en_us/research/22/e/examining-the-black-basta-ransomwares-infection-routine.html)
- [US Federal Bureau of Investigation & US Secret Service. (2022, February 11). Indicators of Compromise Associated with BlackByte Ransomware. Retrieved December 16, 2024.](https://www.ic3.gov/CSA/2022/220211.pdf)
- [Huseyin Can Yuceel. (2022, February 21). TTPs used by BlackByte Ransomware Targeting Critical Infrastructure. Retrieved December 16, 2024.](https://www.picussecurity.com/resource/ttps-used-by-blackbyte-ransomware-targeting-critical-infrastructure)
- [Symantec Threat Hunter Team. (2022, October 21). Exbyte: BlackByte Ransomware Attackers Deploy New Exfiltration Tool. Retrieved December 16, 2024.](https://www.security.com/threat-intelligence/blackbyte-exbyte-ransomware)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [James Nutland, Craig Jackson, Terryn Valikodath, & Brennan Evans. (2024, August 28). BlackByte blends tried-and-true tradecraft with newly disclosed vulnerabilities to support ongoing attacks. Retrieved December 16, 2024.](https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/)
- [Rodel Mendrez & Lloyd Macrohon. (2021, October 15). BlackByte Ransomware – Pt. 1 In-depth Analysis. Retrieved December 16, 2024.](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/blackbyte-ransomware-pt-1-in-depth-analysis/)
- [Microsoft Defender Threat Intelligence. (2022, June 13). The many lives of BlackCat ransomware. Retrieved December 20, 2022.](https://www.microsoft.com/en-us/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Costa, F. (2022, May 1). RaaS AvosLocker Incident Response Analysis. Retrieved January 11, 2023.](https://www.linkedin.com/pulse/raas-avoslocker-incident-response-analysis-fl%C3%A1vio-costa?trk=articles_directory)
- [Dela Cruz, A. et al. (2022, May 25). New Linux-Based Ransomware Cheerscrypt Targeting ESXi Devices Linked to Leaked Babuk Source Code. Retrieved December 19, 2023.](https://www.trendmicro.com/en_se/research/22/e/new-linux-based-ransomware-cheerscrypt-targets-exsi-devices.html)
- [Biderman, O. et al. (2022, October 3). REVEALING EMPEROR DRAGONFLY: NIGHT SKY AND CHEERSCRYPT - A SINGLE RANSOMWARE GROUP. Retrieved December 6, 2023.](https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group)
- [Mundo, A. (2019, August 1). Clop Ransomware. Retrieved May 10, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/clop-ransomware/)
- [Santos, D. (2021, April 13). Threat Assessment: Clop Ransomware. Retrieved July 30, 2021.](https://unit42.paloaltonetworks.com/clop-ransomware/)
- [Cybereason Nocturnus. (2020, December 23). Cybereason vs. Clop Ransomware. Retrieved May 11, 2021.](https://www.cybereason.com/blog/cybereason-vs.-clop-ransomware)
- [Rochberger, L. (2021, January 12). Cybereason vs. Conti Ransomware. Retrieved February 17, 2021.](https://www.cybereason.com/blog/cybereason-vs.-conti-ransomware)
- [Cybleinc. (2021, January 21). Conti Ransomware Resurfaces, Targeting Government & Large Organizations. Retrieved April 13, 2021.](https://cybleinc.com/2021/01/21/conti-ransomware-resurfaces-targeting-government-large-organizations/)
- [Podlosky, A., Hanel, A. et al. (2020, October 16). WIZARD SPIDER Update: Resilient, Reactive and Resolute. Retrieved June 15, 2021.](https://www.crowdstrike.com/blog/wizard-spider-adversary-update/)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [Adi Zeligson & Rotem Kerner. (2018, November 13). Enter The DarkGate - New Cryptocurrency Mining and Ransomware Campaign. Retrieved February 9, 2024.](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign)
- [Checkpoint Research. (2021, November 15). Uncovering MosesStaff techniques: Ideology over Money. Retrieved August 11, 2022.](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
- [McLellan, T. and Moore, J. et al. (2021, April 29). UNC2447 SOMBRAT and FIVEHANDS Ransomware: A Sophisticated Financial Threat. Retrieved June 2, 2021.](https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [Rochberger, L. (2020, November 26). Cybereason vs. Egregor Ransomware. Retrieved December 30, 2020.](https://www.cybereason.com/blog/cybereason-vs-egregor-ransomware)
- [Dragos. (2020, February 3). EKANS Ransomware and ICS Operations. Retrieved February 9, 2021.](https://www.dragos.com/blog/industry-news/ekans-ransomware-and-ics-operations/)
- [Hinchliffe, A. Santos, D. (2020, June 26). Threat Assessment: EKANS Ransomware. Retrieved February 9, 2021.](https://unit42.paloaltonetworks.com/threat-assessment-ekans-ransomware/)
- [Cyble. (2024, May 24). The Rust Revolution: New Embargo Ransomware Steps In. Retrieved October 19, 2025.](https://cyble.com/blog/the-rust-revolution-new-embargo-ransomware-steps-in/)
- [Jan Holman, Tomas Zvara. (2024, October 23). Embargo ransomware: Rock’n’Rust. Retrieved October 19, 2025.](https://www.welivesecurity.com/en/eset-research/embargo-ransomware-rocknrust/)
- [Loui, E. and Reynolds, J. (2021, August 30). CARBON SPIDER Embraces Big Game Hunting, Part 1. Retrieved September 20, 2021.](https://www.crowdstrike.com/blog/carbon-spider-embraces-big-game-hunting-part-1/)
- [Abdo, B., et al. (2022, April 4). FIN7 Power Hour: Adversary Archaeology and the Evolution of FIN7. Retrieved April 5, 2022.](https://www.mandiant.com/resources/evolution-of-fin7)
- [The BlackBerry Research and Intelligence Team. (2024, April 17). Threat Group FIN7 Targets the U.S. Automotive Industry. Retrieved May 1, 2025.](https://blogs.blackberry.com/en/2024/04/fin7-targets-the-united-states-automotive-industry)
- [Symantec Threat Hunter Team. (2023, July 18). FIN8 Uses Revamped Sardonic Backdoor to Deliver Noberus Ransomware. Retrieved August 9, 2023.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/syssphinx-fin8-backdoor)
- [CISA. (2021, May 6). Analysis Report (AR21-126A) FiveHands Ransomware. Retrieved June 7, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar21-126a)
- [Matthews, M. and Backhouse, W. (2021, June 15). Handy guide to a new Fivehands ransomware variant. Retrieved June 24, 2021.](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)
- [Jenkins, L. at al. (2022, August 4). ROADSWEEP Ransomware - Likely Iranian Threat Actor Conducts Politically Motivated Disruptive Activity Against Albanian Government Organizations. Retrieved August 6, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
- [CISA. (2022, September 23). AA22-264A Iranian State Actors Conduct Cyber Operations Against the Government of Albania. Retrieved August 6, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-264a)
- [MSTIC. (2022, September 8). Microsoft investigates Iranian attacks against the Albanian government. Retrieved August 6, 2024.](https://www.microsoft.com/en-us/security/blog/2022/09/08/microsoft-investigates-iranian-attacks-against-the-albanian-government/)
- [SentinelOne. (n.d.). What Is Inc. Ransomware?. Retrieved June 5, 2024.](https://www.sentinelone.com/anthology/inc-ransom/)
- [Team Huntress. (2023, August 11). Investigating New INC Ransom Group Activity. Retrieved June 5, 2024.](https://www.huntress.com/blog/investigating-new-inc-ransom-group-activity)
- [Toulas, B. (2024, March 27). INC Ransom threatens to leak 3TB of NHS Scotland stolen data. Retrieved June 5, 2024.](https://www.bleepingcomputer.com/news/security/inc-ransom-threatens-to-leak-3tb-of-nhs-scotland-stolen-data/)
- [Counter Threat Unit Research Team. (2024, April 15). GOLD IONIC DEPLOYS INC RANSOMWARE. Retrieved June 5, 2024.](https://www.secureworks.com/blog/gold-ionic-deploys-inc-ransomware)
- [Cybereason Security Research Team. (2023, November 20). Threat Alert: INC Ransomware. Retrieved June 5, 2024.](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
- [SOCRadar. (2024, January 24). Dark Web Profile: INC Ransom. Retrieved June 5, 2024.](https://socradar.io/dark-web-profile-inc-ransom/)
- [Mandiant Intelligence. (2022, June 2). To HADES and Back: UNC2165 Shifts to LOCKBIT to Evade Sanctions. Retrieved July 29, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/)
- [Lee, S.. (2019, May 14). JCry Ransomware. Retrieved June 18, 2019.](https://www.carbonblack.com/2019/05/14/cb-tau-threat-intelligence-notification-jcry-ransomware-pretends-to-be-adobe-flash-player-update-installer/)
- [Catalin Cimpanu. (2016, December 29). KillDisk Disk-Wiping Malware Adds Ransomware Component. Retrieved January 12, 2021.](https://www.bleepingcomputer.com/news/security/killdisk-disk-wiping-malware-adds-ransomware-component/)
- [Elsad, A. et al. (2022, June 9). LockBit 2.0: How This RaaS Operates and How to Protect Against It. Retrieved January 24, 2025.](https://unit42.paloaltonetworks.com/lockbit-2-ransomware/)
- [SentinelOne. (n.d.). LockBit 2.0: In-Depth Analysis, Detection, Mitigation, and Removal. Retrieved January 24, 2025.](https://www.sentinelone.com/anthology/lockbit-2-0/)
- [CISA et al. (2023, June 14). UNDERSTANDING RANSOMWARE THREAT ACTORS: LOCKBIT. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-06/aa23-165a_understanding_TA_LockBit_0.pdf)
- [Walter, J. (2022, July 21). LockBit 3.0 Update | Unpicking the Ransomware’s Latest Anti-Analysis and Evasion Techniques. Retrieved February 5, 2025.](https://www.sentinelone.com/labs/lockbit-3-0-update-unpicking-the-ransomwares-latest-anti-analysis-and-evasion-techniques)
- [FBI et al. (2023, March 16). #StopRansomware: LockBit 3.0. Retrieved February 5, 2025.](https://www.cisa.gov/sites/default/files/2023-03/aa23-075a-stop-ransomware-lockbit.pdf)
- [INCIBE-CERT. (2024, March 14). LockBit: response and recovery actions. Retrieved February 5, 2025.](https://www.incibe.es/en/incibe-cert/blog/lockbit-response-and-recovery-actions)
- [CarbonBlack Threat Analysis Unit. (2019, March 22). TAU Threat Intelligence Notification – LockerGoga Ransomware. Retrieved April 16, 2019.](https://www.carbonblack.com/2019/03/22/tau-threat-intelligence-notification-lockergoga-ransomware/)
- [Harbison, M. (2019, March 26). Born This Way? Origins of LockerGoga. Retrieved April 16, 2019.](https://unit42.paloaltonetworks.com/born-this-way-origins-of-lockergoga/)
- [Greenberg, A. (2019, March 25). A Guide to LockerGoga, the Ransomware Crippling Industrial Firms. Retrieved July 17, 2019.](https://www.wired.com/story/lockergoga-ransomware-crippling-industrial-firms/)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part II. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
- [Breitenbacher, D. (2022, December 14). Unmasking MirrorFace: Operation LiberalFace targeting Japanese political entities. Retrieved April 17, 2026.](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
- [ITOCHU. (2024, January 24). The Endless Struggle Against APT10: Insights from LODEINFO v0.6.6 - v0.7.3 Analysis. Retrieved April 17, 2026.](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [MSTIC. (2021, November 16). Evolving trends in Iranian threat actor activity – MSTIC presentation at CyberWarCon 2021. Retrieved January 12, 2023.](https://www.microsoft.com/en-us/security/blog/2021/11/16/evolving-trends-in-iranian-threat-actor-activity-mstic-presentation-at-cyberwarcon-2021)
- [Kennelly, J., Goody, K., Shilko, J. (2020, May 7). Navigating the MAZE: Tactics, Techniques and Procedures Associated With MAZE Ransomware Incidents. Retrieved May 18, 2020.](https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html)
- [Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [Threat Hunter Team Symantec and Carbon Black. (2025, March 6). Medusa Ransomware Activity Continues to Increase. Retrieved October 15, 2025.](https://www.security.com/threat-intelligence/medusa-ransomware-attacks)
- [Vlad Pasca. (2024, January 1). A Deep Dive into Medusa Ransomware. Retrieved October 15, 2025.](https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf)
- [Del Fierro, C. Kessem, L.. (2020, January 8). From Mega to Giga: Cross-Version Comparison of Top MegaCortex Modifications. Retrieved February 15, 2021.](https://securityintelligence.com/posts/from-mega-to-giga-cross-version-comparison-of-top-megacortex-modifications/)
- [ARMmbed. (2018, June 21). Mbed Crypto. Retrieved February 15, 2021.](https://github.com/ARMmbed/mbed-crypto)
- [Marc Salinas Fernandez & Jiri Vinopal. (2023, May 23). AGRIUS DEPLOYS MONEYBIRD IN TARGETED ATTACKS AGAINST ISRAELI ORGANIZATIONS. Retrieved May 21, 2024.](https://research.checkpoint.com/2023/agrius-deploys-moneybird-in-targeted-attacks-against-israeli-organizations/)
- [Microsoft Threat Intelligence. (2024, May 28). Moonstone Sleet emerges as new North Korean threat actor with new bag of tricks. Retrieved August 26, 2024.](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)
- [Victor, K.. (2020, May 18). Netwalker Fileless Ransomware Injected via Reflective Loading . Retrieved May 26, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/netwalker-fileless-ransomware-injected-via-reflective-loading/)
- [Chiu, A. (2016, June 27). New Ransomware Variant "Nyetya" Compromises Systems Worldwide. Retrieved March 26, 2019.](https://blog.talosintelligence.com/2017/06/worldwide-ransomware-variant.html)
- [Scott W. Brady. (2020, October 15). United States vs. Yuriy Sergeyevich Andrienko et al.. Retrieved November 25, 2020.](https://www.justice.gov/opa/press-release/file/1328521/download)
- [ClearSky. (2020, February 16). Fox Kitten – Widespread Iranian Espionage-Offensive Campaign. Retrieved December 21, 2020.](https://www.clearskysec.com/fox-kitten/)
- [Check Point. (2020, November 6). Ransomware Alert: Pay2Key. Retrieved January 4, 2021.](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)
- [CISA. (2023, December 18). #StopRansomware: Play Ransomware AA23-352A. Retrieved September 24, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)
- [Trend Micro Research. (2023, July 21). Ransomware Spotlight: Play. Retrieved September 24, 2024.](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-play)
- [MSTIC. (2022, October 14). New “Prestige” ransomware impacts organizations in Ukraine and Poland. Retrieved January 19, 2023.](https://www.microsoft.com/en-us/security/blog/2022/10/14/new-prestige-ransomware-impacts-organizations-in-ukraine-and-poland/)
- [Group IB. (2020, September). LOCK LIKE A PRO. Retrieved November 17, 2024.](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
- [CERT-FR. (2020, April 1). ATTACKS INVOLVING THE MESPINOZA/PYSA RANSOMWARE. Retrieved March 1, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
- [Magdy, S. et al. (2022, August 25). New Golang Ransomware Agenda Customizes Attacks. Retrieved September 26, 2025.](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
- [SentinelOne. (2022, November 30). Agenda (Qilin). Retrieved September 26, 2025.](https://www.sentinelone.com/anthology/agenda-qilin/)
- [Hacioglu, S. (2025, March 10). Qilin Ransomware: Exposing the TTPs Behind One of the Most Active Ransomware Campaigns of 2024. Retrieved September 26, 2025.](https://www.picussecurity.com/resource/blog/qilin-ransomware)
- [Thomas, W. (2024, June 12). Tracking Adversaries: The Qilin RaaS. Retrieved September 26, 2025.](https://blog.bushidotoken.net/2024/06/tracking-adversaries-qilin-raas.html)
- [Halcyon RISE Team. (2024, October 24). New Qilin.B Ransomware Variant Boasts Enhanced Encryption and Defense Evasion. Retrieved September 26, 2025.](https://www.halcyon.ai/blog/new-qilin-b-ransomware-variant-boasts-enhanced-encryption-and-defense-evasion)
- [Health Sector Cybersecurity Coordination Center. (2024, June 18). Qilin, aka Agenda Ransomware. Retrieved September 26, 2025.](https://www.aha.org/system/files/media/file/2024/06/tlp-clear-hc3-threat-profile-qilin-aka-agenda-ransomware-6-18-2024.pdf)
- [Trend Micro. (2025, October 23). Agenda Ransomware Deploys Linux Variant on Windows Systems Through Remote Management Tools and BYOVD Techniques. Retrieved March 26, 2026.](https://www.trendmicro.com/en_us/research/25/j/agenda-ransomware-deploys-linux-variant-on-windows-systems.html)
- [Takeda, T. et al. (2025, October 26). Uncovering Qilin attack methods exposed through multiple cases. Retrieved March 26, 2026.](https://blog.talosintelligence.com/uncovering-qilin-attack-methods-exposed-through-multiple-cases/)
- [SophosLabs. (2020, May 21). Ragnar Locker ransomware deploys virtual machine to dodge security. Retrieved June 29, 2020.](https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/)
- [Gold, B. (2020, April 27). Cynet Detection Report: Ragnar Locker Ransomware. Retrieved June 29, 2020.](https://www.cynet.com/blog/cynet-detection-report-ragnar-locker-ransomware/)
- [CISA et al. (2024, August 29). #StopRansomware: RansomHub Ransomware. Retrieved March 17, 2025.](https://www.cisa.gov/sites/default/files/2024-09/aa24-242a-stopransomware-ransomhub-ransomware_1.pdf)
- [Alfano, V. et al. (2025, February 12). RansomHub Never Sleeps Episode 1: The evolution of modern ransomware. Retrieved March 17, 2025.](https://www.group-ib.com/blog/ransomhub-never-sleeps-episode-1/)
- [Mamedov, O, et al. (2019, July 3). Sodin ransomware exploits Windows vulnerability and processor architecture. Retrieved August 4, 2020.](https://securelist.com/sodin-ransomware/91473/)
- [Cylance. (2019, July 3). hreat Spotlight: Sodinokibi Ransomware. Retrieved August 4, 2020.](https://threatvector.cylance.com/en_us/home/threat-spotlight-sodinokibi-ransomware.html)
- [Cadieux, P, et al (2019, April 30). Sodinokibi ransomware exploits WebLogic Server vulnerability. Retrieved August 4, 2020.](https://blog.talosintelligence.com/2019/04/sodinokibi-ransomware-exploits-weblogic.html)
- [Saavedra-Morales, J, et al. (2019, October 20). McAfee ATR Analyzes Sodinokibi aka REvil Ransomware-as-a-Service – Crescendo. Retrieved August 5, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/mcafee-atr-analyzes-sodinokibi-aka-revil-ransomware-as-a-service-crescendo/)
- [Intel 471 Malware Intelligence team. (2020, March 31). REvil Ransomware-as-a-Service – An analysis of a ransomware affiliate operation. Retrieved August 4, 2020.](https://intel471.com/blog/revil-ransomware-as-a-service-an-analysis-of-a-ransomware-affiliate-operation/)
- [Ozarslan, S. (2020, January 15). A Brief History of Sodinokibi. Retrieved August 5, 2020.](https://www.picussecurity.com/blog/a-brief-history-and-further-technical-analysis-of-sodinokibi-ransomware)
- [Counter Threat Unit Research Team. (2019, September 24). REvil/Sodinokibi Ransomware. Retrieved August 4, 2020.](https://www.secureworks.com/research/revil-sodinokibi-ransomware)
- [Tetra Defense. (2020, March). CAUSE AND EFFECT: SODINOKIBI RANSOMWARE ANALYSIS. Retrieved November 17, 2024.](https://web.archive.org/web/20210414101816/https://tetradefense.com/incident-response-services/cause-and-effect-sodinokibi-ransomware-analysis/)
- [Lee, S. (2019, May 17). CB TAU Threat Intelligence Notification: RobbinHood Ransomware Stops 181 Windows Services Before Encryption. Retrieved July 29, 2019.](https://www.carbonblack.com/2019/05/17/cb-tau-threat-intelligence-notification-robbinhood-ransomware-stops-181-windows-services-before-encryption/)
- [Cybereason Global SOC and Cybereason Security Research Teams. (2022, December 14). Royal Rumble: Analysis of Royal Ransomware. Retrieved March 30, 2023.](https://www.cybereason.com/blog/royal-ransomware-analysis)
- [Iacono, L. and Green, S. (2023, February 13). Royal Ransomware Deep Dive. Retrieved March 30, 2023.](https://www.kroll.com/en/insights/publications/cyber/royal-ransomware-deep-dive)
- [Morales, N. et al. (2023, February 20). Royal Ransomware Expands Attacks by Targeting Linux ESXi Servers. Retrieved March 30, 2023.](https://www.trendmicro.com/en_us/research/23/b/royal-ransomware-expands-attacks-by-targeting-linux-esxi-servers.html)
- [Hanel, A. (2019, January 10). Big Game Hunting with Ryuk: Another Lucrative Targeted Ransomware. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
- [Palotay, D. and Mackenzie, P. (2018, April). SamSam Ransomware Chooses Its Targets Carefully. Retrieved April 15, 2019.](https://www.sophos.com/en-us/medialibrary/PDFs/technical-papers/SamSam-ransomware-chooses-Its-targets-carefully-wpna.pdf)
- [CISA. (2023, November 16). Cybersecurity Advisory: Scattered Spider (AA23-320A). Retrieved March 18, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a)
- [Microsoft. (2023, October 25). Octo Tempest crosses boundaries to facilitate extortion, encryption, and destruction. Retrieved March 18, 2024.](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction/)
- [Counter Adversary Operations. (2025, July 2). CrowdStrike Services Observes SCATTERED SPIDER Escalate Attacks Across Industries. Retrieved October 13, 2025.](https://www.crowdstrike.com/en-us/blog/crowdstrike-services-observes-scattered-spider-escalate-attacks/)
- [Mandiant Incident Response. (2025, July 23). From Help Desk to Hypervisor: Defending Your VMware vSphere Estate from UNC3944. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944)
- [Check Point Team. (2025, July 7). Exposing Scattered Spider: New Indicators Highlight Growing Threat to Enterprises and Aviation. Retrieved October 13, 2025.](https://blog.checkpoint.com/research/exposing-scattered-spider-new-indicators-highlight-growing-threat-to-enterprises-and-aviation/)
- [Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [Falcone, R. (2018, December 13). Shamoon 3 Targets Oil and Gas Organization. Retrieved March 14, 2019.](https://unit42.paloaltonetworks.com/shamoon-3-targets-oil-gas-organization/)
- [Microsoft Threat Intelligence. (2025, July 22). Disrupting active exploitation of on-premises SharePoint vulnerabilities. Retrieved October 15, 2025.](https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/#storm-2603)
- [Unit 42. (2025, July 31). Active Exploitation of Microsoft SharePoint Vulnerabilities: Threat Brief (Updated). Retrieved October 15, 2025.](https://unit42.paloaltonetworks.com/microsoft-sharepoint-cve-2025-49704-cve-2025-49706-cve-2025-53770/)
- [Cristian Souza, Eduardo Ovalle, Ashley Muñoz, & Christopher Zachor. (2024, May 23). ShrinkLocker: Turning BitLocker into ransomware. Retrieved December 7, 2024.](https://securelist.com/ransomware-abuses-bitlocker/112643/)
- [Splunk Threat Research Team , Teoderick Contreras. (2024, September 5). ShrinkLocker Malware: Abusing BitLocker to Lock Your Data. Retrieved December 7, 2024.](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
- [Microsoft Threat Intelligence. (2025, August 27). Storm-0501’s evolving techniques lead to cloud-based ransomware. Retrieved October 19, 2025.](https://www.microsoft.com/en-us/security/blog/2025/08/27/storm-0501s-evolving-techniques-lead-to-cloud-based-ransomware/)
- [Microsoft Threat Intelligence. (2024, May 15). Threat actors misusing Quick Assist in social engineering attacks leading to ransomware. Retrieved March 14, 2025.](https://www.microsoft.com/en-us/security/blog/2024/05/15/threat-actors-misusing-quick-assist-in-social-engineering-attacks-leading-to-ransomware/)
- [Ivanov, A. et al. (2018, May 7). SynAck targeted ransomware uses the Doppelgänging technique. Retrieved May 22, 2018.](https://securelist.com/synack-targeted-ransomware-uses-the-doppelganging-technique/85431/)
- [Proofpoint Staff. (2017, September 27). Threat Actor Profile: TA505, From Dridex to GlobeImposter. Retrieved May 28, 2019.](https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta505-dridex-globeimposter)
- [Patrick Wardle. (2020, July 3). OSX.EvilQuest Uncovered part ii: insidious capabilities. Retrieved March 21, 2021.](https://objective-see.com/blog/blog_0x60.html)
- [Check Point Research. (2026, March 12). “Handala Hack” – Unveiling Group’s Modus Operandi. Retrieved April 20, 2026.](https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/)
- [DOJ/FBI. (2026, March 19). Case 1:26-mj-00683-CDA: Affidavit in Support of Seizure Warrant: In the Matter of the Seizure of Domain Names Justicehomeland[.]org; karmabelow80[.]org; handala-hack[.]to; and handala-redwatned[.]to. Retrieved April 20, 2026.](https://www.justice.gov/opa/media/1431956/dl?inline)
- [Noerenberg, E., Costis, A., and Quist, N. (2017, May 16). A Technical Analysis of WannaCry Ransomware. Retrieved December 8, 2024.](https://web.archive.org/web/20230522041200/https://logrhythm.com/blog/a-technical-analysis-of-wannacry-ransomware/)
- [Counter Threat Unit Research Team. (2017, May 18). WCry Ransomware Analysis. Retrieved March 26, 2019.](https://www.secureworks.com/research/wcry-ransomware-analysis)
- [Symantec Threat Intelligence. (2020, June 25). WastedLocker: Symantec Identifies Wave of Attacks Against U.S. Organizations. Retrieved May 20, 2021.](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us)
- [Antenucci, S., Pantazopoulos, N., Sandee, M. (2020, June 23). WastedLocker: A New Ransomware Variant Developed By The Evil Corp Group. Retrieved September 14, 2021.](https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/)
- [Walter, J.. (2020, July 23). WastedLocker Ransomware: Abusing ADS and NTFS File Attributes. Retrieved September 14, 2021.](https://www.sentinelone.com/labs/wastedlocker-ransomware-abusing-ads-and-ntfs-file-attributes/)
- [Xiao, C. (2018, September 17). Xbash Combines Botnet, Ransomware, Coinmining in Worm that Targets Linux and Windows. Retrieved November 14, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-xbash-combines-botnet-ransomware-coinmining-worm-targets-linux-windows/)
- [Mac Threat Response, Mobile Research Team. (2020, August 13). The XCSSET Malware: Inserts Malicious Code Into Xcode Projects, Performs UXSS Backdoor Planting in Safari, and Leverages Two Zero-day Exploits. Retrieved October 5, 2021.](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
- [Microsoft. (2021, July 2). Use attack surface reduction rules to prevent malware infection. Retrieved June 24, 2021.](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
- [Ready.gov. (n.d.). IT Disaster Recovery Plan. Retrieved March 15, 2019.](https://www.ready.gov/business/implementation/IT)
- [Gietzen, S. (n.d.). S3 Ransomware Part 2: Prevention and Defense. Retrieved April 14, 2021.](https://rhinosecuritylabs.com/aws/s3-ransomware-part-2-prevention-and-defense/)

---


### 🔗 KRAB Intelligence Correlation
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[ShinyHunters]] [related_actor:: [[ShinyHunters]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Dragonforce]] [related_actor:: [[Dragonforce]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[FIN7]] [related_actor:: [[FIN7]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Lazarus Group]] [related_actor:: [[Lazarus Group]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[Lockbit]] [related_actor:: [[Lockbit]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025 Multi-Industry Hypervisor and Retail Extortion Campaign]] [related_campaign:: [[2025 Multi-Industry Hypervisor and Retail Extortion Campaign]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[2025-2026 SaaS and Cloud Exploitation Wave]] [related_campaign:: [[2025-2026 SaaS and Cloud Exploitation Wave]]]
- ⚔️ **Active Operation Deployment:** Tracked in campaign [[MGM Resorts and Caesars Entertainment Extortion Campaign]] [related_campaign:: [[MGM Resorts and Caesars Entertainment Extortion Campaign]]]
- 🏴‍☠️ **Observed Adversary Tradecraft:** Leveraged by [[RansomHub]] [related_actor:: [[RansomHub]]]
- 🦠 **Tooling Capability Integration:** Executed via malware family [[DragonForce]] [related_malware:: [[DragonForce]]]
- 🦠 **Tooling Capability Integration:** Executed via malware family [[Mamona]] [related_malware:: [[Mamona]]]

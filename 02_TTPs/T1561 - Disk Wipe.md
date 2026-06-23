# Disk Wipe

## Description

Adversaries may wipe or corrupt raw disk data on specific systems or in large numbers in a network to interrupt availability to system and network resources. With direct write access to a disk, adversaries may attempt to overwrite portions of disk data. Adversaries may opt to wipe arbitrary portions of disk data and/or wipe disk structures like the master boot record (MBR). A complete wipe of all disk sectors may be attempted.

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware used for wiping disks may have worm-like features to propagate across a network by leveraging additional techniques like Valid Accounts , OS Credential Dumping , and SMB/Windows Admin Shares . [1]

On network devices, adversaries may wipe configuration files and other data from the device using Network Device CLI commands such as erase . [2]

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1053 | Data Backup | Consider implementing IT disaster recovery plans that contain procedures for taking regular data backups that can be used to restore organizational data. [3] Ensure backups are stored off system and is protected from common methods adversaries may use to gain access and destroy the backups to prevent recovery. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0137 | Detection Strategy for Disk Wipe via Direct Disk Access and Destructive Commands | AN0384 | Unusual direct disk access attempts (e.g., use of \.\PhysicalDrive notation), abnormal writes to MBR/boot sectors, and installation of kernel drivers that grant raw disk access. Correlate anomalous process creation with disk modification attempts and driver loads. |
| AN0385 | Processes invoking destructive commands (dd, shred, wipe) with raw device targets (e.g., /dev/sda, /dev/nvme0n1). Detect direct writes to disk partitions and abnormal superblock or bootloader modifications. Correlate shell execution with subsequent block device I/O. |  |  |
| AN0386 | Abnormal invocation of diskutil, asr, or low-level APIs (IOKit) to erase/partition drives. Correlate process execution with unified log entries showing destructive disk operations. |  |  |
| AN0387 | Execution of destructive CLI commands such as 'erase startup-config', 'erase flash:' or 'format disk' on routers/switches. Detect privilege level escalation preceding destructive commands. |  |  |

---

## References

- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Destructive Malware Report. Retrieved November 17, 2024.](https://web.archive.org/web/20160303200515/https:/operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Destructive-Malware-Report.pdf)
- [Cisco. (2022, August 16). erase - Cisco IOS Configuration Fundamentals Command Reference . Retrieved July 13, 2022.](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/cf_command_ref/D_through_E.html#wp3557227463)
- [Ready.gov. (n.d.). IT Disaster Recovery Plan. Retrieved March 15, 2019.](https://www.ready.gov/business/implementation/IT)

---

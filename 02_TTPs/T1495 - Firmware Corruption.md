# Firmware Corruption

## Description

Adversaries may overwrite or corrupt the flash memory contents of system BIOS or other firmware in devices attached to a system in order to render them inoperable or unable to boot, thus denying the availability to use the devices and/or the system. [1] Firmware is software that is loaded and executed from non-volatile memory on hardware devices in order to initialize and manage device functionality. These devices may include the motherboard, hard drive, or video cards.

In general, adversaries may manipulate, overwrite, or corrupt firmware in order to deny the use of the system or devices. For example, corruption of firmware responsible for loading the operating system for network devices may render the network devices inoperable. [2] [3] Depending on the device, this attack may also result in Data Destruction .

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , adversaries performed a factory-reset on compromised devices that hampered forensic investigations. [4] |
| S0606 | Bad Rabbit | Bad Rabbit has used an executable that installs a modified bootloader to prevent normal boot-up. [5] |
| S0266 | TrickBot | TrickBot module "Trickboot" can write or erase the UEFI/BIOS firmware of a compromised device. [6] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1046 | Boot Integrity | Check the integrity of the existing BIOS and device firmware to determine if it is vulnerable to modification. |
| M1026 | Privileged Account Management | Prevent adversary access to privileged accounts or access necessary to replace system firmware. |
| M1051 | Update Software | Patch the BIOS and other firmware as necessary to prevent successful use of known vulnerabilities. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0167 | Firmware Modification via Flash Tool or Corrupted Firmware Upload | AN0474 | Firmware flash utility invoked with elevated privileges followed by raw access to firmware device path or changes to boot configuration. |
| AN0475 | Direct write access to /dev/mem or /sys/firmware combined with usage of firmware flashing utilities (e.g., flashrom). |  |  |
| AN0476 | EFI updates executed via system processes or binaries outside of expected patch windows or using unsigned firmware packages. |  |  |
| AN0477 | Firmware image uploaded via TFTP/SCP or web interface followed by reboot or unexpected loss of connectivity. |  |  |

---

## References

- [Yamamura, M. (2002, April 25). W95.CIH. Retrieved April 12, 2019.](https://web.archive.org/web/20190508170055/https://www.symantec.com/security-center/writeup/2000-122010-2655-99)
- [U.S. Department of Homeland Security. (2016, August 30). The Increasing Threat to Network Infrastructure Devices and Recommended Mitigations. Retrieved July 29, 2022.](https://cyber.dhs.gov/assets/report/ar-16-20173.pdf)
- [CISA. (2022, April 28). Alert (AA22-057A) Update: Destructive Malware Targeting Organizations in Ukraine. Retrieved July 29, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-057a)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Mamedov, O. Sinitsyn, F. Ivanov, A.. (2017, October 24). Bad Rabbit ransomware. Retrieved January 28, 2021.](https://securelist.com/bad-rabbit-ransomware/82851/)
- [Eclypsium, Advanced Intelligence. (2020, December 1). TRICKBOT NOW OFFERS ‘TRICKBOOT’: PERSIST, BRICK, PROFIT. Retrieved March 15, 2021.](https://eclypsium.com/wp-content/uploads/2020/12/TrickBot-Now-Offers-TrickBoot-Persist-Brick-Profit.pdf)

---

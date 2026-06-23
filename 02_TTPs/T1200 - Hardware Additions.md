# Hardware Additions

## Description

Adversaries may physically introduce computer accessories, networking hardware, or other computing devices into a system or network that can be used as a vector to gain access. Rather than just connecting and distributing payloads via removable storage (i.e. Replication Through Removable Media ), more robust hardware additions can be used to introduce new functionalities and/or features into a system that can then be abused.

While public references of usage by threat actors are scarce, many red teams/penetration testers leverage hardware additions for initial access. Commercial and open source products can be leveraged with capabilities such as passive network tapping, network traffic modification (i.e. Adversary-in-the-Middle ), keystroke injection, kernel memory reading via DMA, addition of new wireless access points to an existing network, and others. [1] [2] [3] [4]

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| G0105 | DarkVishnya | DarkVishnya physically connected Bash Bunny, Raspberry Pi, netbooks, and inexpensive laptops to the target organization's environment to access the company’s local network. [5] |

---

## Mitigations

| ID | Mitigation | Description |
|---|---|---|
| M1035 | Limit Access to Resource Over Network | Establish network access control policies, such as using device certificates and the 802.1x standard. [6] Restrict use of DHCP to registered devices to prevent unregistered devices from communicating with trusted systems. |
| M1034 | Limit Hardware Installation | Block unknown devices and accessories by endpoint security configuration and monitoring agent. |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0069 | Detect unauthorized or suspicious Hardware Additions (USB/Thunderbolt/Network) | AN0185 | Chain: (1) a new external device is recognized by Windows (USB/Thunderbolt/PCIe) or a new block device appears; (2) within a short window, the same user/session spawns processes or the OS mounts a new volume; (3) optional follow-on activity such as HID keystroke injection, DMA driver load, or new network interface MAC on DHCP. Correlate Security EID 6416 / Kernel-PnP with sysmon and DHCP/network metadata. |
| AN0186 | Chain: (1) udev / kernel logs show hot-plug (USB/Thunderbolt/PCIe); (2) block device created by udisks/diskarbitration; (3) optional: new network interface or DHCP lease observed. Correlate /var/log/messages|syslog, auditd SYSCALL open/creat on /dev, and DHCP/Zeek. |  |  |
| AN0187 | Chain: (1) unified logs report IOUSBHost/IOThunderbolt device arrival; (2) diskarbitrationd attaches a new volume; (3) optional: config profile manipulation or new network interface MAC obtains a lease. Correlate unifiedlogs (subsystems: IOUSBHost, IOKit, diskarbitrationd), FSEvents, and DHCP/Zeek. |  |  |

---

## References

- [Michael Ossmann. (2011, February 17). Throwing Star LAN Tap. Retrieved March 30, 2018.](https://ossmann.blogspot.com/2011/02/throwing-star-lan-tap.html)
- [Nick Aleks. (2015, November 7). Weapons of a Pentester - Understanding the virtual & physical tools used by white/black hat hackers. Retrieved March 30, 2018.](https://www.youtube.com/watch?v=lDvf4ScWbcQ)
- [Ulf Frisk. (2016, August 5). Direct Memory Attack the Kernel. Retrieved March 30, 2018.](https://www.youtube.com/watch?v=fXthwl6ShOg)
- [Robert McMillan. (2012, March 3). The Pwn Plug is a little white box that can hack your network. Retrieved March 30, 2018.](https://arstechnica.com/information-technology/2012/03/the-pwn-plug-is-a-little-white-box-that-can-hack-your-network/)
- [Golovanov, S. (2018, December 6). DarkVishnya: Banks attacked through direct connection to local network. Retrieved May 15, 2020.](https://securelist.com/darkvishnya/89169/)
- [Wikipedia. (2018, March 30). IEEE 802.1X. Retrieved April 11, 2018.](https://en.wikipedia.org/wiki/IEEE_802.1X)

---

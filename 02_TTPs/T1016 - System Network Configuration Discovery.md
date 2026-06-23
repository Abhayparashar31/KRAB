# System Network Configuration Discovery

## Description

Adversaries may look for details about the network configuration and settings, such as IP and/or MAC addresses, of systems they access or through information discovery of remote systems. Several operating system administration utilities exist that can be used to gather this information. Examples include Arp , ipconfig / ifconfig , nbtstat , and route .

Adversaries may also leverage a Network Device CLI on network devices to gather information about configurations and settings, such as IP addresses of configured interfaces and static/dynamic routes (e.g. show ip route , show ip interface ). [1] [2] On ESXi, adversaries may leverage esxcli to gather network configuration information. For example, the command esxcli network nic list will retrieve the MAC address, while esxcli network ip interface ipv4 get will retrieve the local IPv4 address. [3]

Adversaries may use the information from System Network Configuration Discovery during automated discovery to shape follow-on behaviors, including determining certain access within the target network and what actions to do next.

---

## Procedure Examples

| ID | Name | Description |
|---|---|---|
| C0063 | 2025 Poland Wiper Attacks | During the 2025 Poland Wiper Attacks , the adversaries gathered network configuration details utilizing arp -a and nslookup commands. [4] |
| S1028 | Action RAT | Action RAT has the ability to collect the MAC address of an infected host. [5] |
| S0552 | AdFind | AdFind can extract subnet information from Active Directory. [6] [7] [8] |
| G0018 | admin@338 | admin@338 actors used the following command after exploiting a machine with LOWBALL malware to acquire information about local networks: ipconfig /all >> %temp%\download [9] |
| S0331 | Agent Tesla | Agent Tesla can collect the IP address of the victim machine and spawn instances of netsh.exe to enumerate wireless settings. [10] [11] |
| S0092 | Agent.btz | Agent.btz collects the network adapter’s IP and MAC address as well as IP addresses of the network adapter’s default gateway, primary/secondary WINS, DHCP, and DNS servers, and saves them into a log file. [12] |
| S1025 | Amadey | Amadey can identify the IP address of a victim machine. [13] |
| S0504 | Anchor | Anchor can determine the public IP and location of a compromised host. [14] |
| C0062 | Anthropic AI-orchestrated Campaign | During the Anthropic AI-orchestrated Campaign , the adversary configured Claude Code to identify and gather system configurations of discovered devices. [15] |
| S0622 | AppleSeed | AppleSeed can identify the IP of a targeted system. [16] |
| G0006 | APT1 | APT1 used the ipconfig /all command to gather network configuration information. [17] |
| G0073 | APT19 | APT19 used an HTTP malware variant and a Port 22 malware variant to collect the MAC address and IP address from the victim’s machine. [18] |
| G0022 | APT3 | A keylogging tool used by APT3 gathers network information from the victim, including the MAC address, IP address, WINS, DHCP server, and gateway. [19] [20] |
| G0050 | APT32 | APT32 used the ipconfig /all command to gather the IP address from the system. [21] |
| G0096 | APT41 | APT41 collected MAC addresses from victim machines. [22] [23] |
| G1044 | APT42 | APT42 has used malware, such as GHAMBAR and POWERPOST, to collect network information. [24] |
| S0456 | Aria-body | Aria-body has the ability to identify the location, public IP address, and domain name on a compromised host. [25] |
| S0099 | Arp | Arp can be used to display ARP configuration information on the host. [26] |
| S0373 | Astaroth | Astaroth collects the external IP address from the system. [27] |
| S1087 | AsyncRAT | AsyncRAT can enumerate the NetBIOS name on targeted machines. [28] |
| S0640 | Avaddon | Avaddon can collect the external IP address of the victim. [29] |
| S0473 | Avenger | Avenger can identify the domain of the compromised host. [30] |
| S0344 | Azorult | Azorult can collect host IP information from the victim’s machine. [31] |
| S0414 | BabyShark | BabyShark has executed the ipconfig /all command. [32] |
| S0093 | Backdoor.Oldrea | Backdoor.Oldrea collects information about the Internet adapter configuration. [33] [34] |
| S0245 | BADCALL | BADCALL collects the network adapter information. [35] |
| S0642 | BADFLICK | BADFLICK has captured victim IP address details. [36] |
| S0234 | Bandook | Bandook has a command to get the public IP address from a system. [37] |
| S0534 | Bazar | Bazar can collect the IP address and NetBIOS name of an infected machine. [38] |
| S0268 | Bisonal | Bisonal can execute ipconfig on the victim’s machine. [39] [40] [41] |
| G1043 | BlackByte | BlackByte used tools such as Arp to pull system network information and identify connected devices. [42] [43] |
| S0089 | BlackEnergy | BlackEnergy has gathered information about network IP configurations using ipconfig .exe and about routing tables using route .exe. [44] [45] |
| S0520 | BLINDINGCAN | BLINDINGCAN has collected the victim machine's local IP address information and MAC address. [46] |
| S0657 | BLUELIGHT | BLUELIGHT can collect IP information from the victim’s machine. [47] |
| S1184 | BOLDMOVE | BOLDMOVE enumerates network interfaces on the infected host. [48] |
| S0486 | Bonadan | Bonadan can find the external IP address of the infected host. [49] |
| S0651 | BoxCaon | BoxCaon can collect the victim's MAC address by using the GetAdaptersInfo API. [50] |
| S0252 | Brave Prince | Brave Prince gathers network configuration information as well as the ARP cache. [51] |
| C0015 | C0015 | During C0015 , the threat actors used code to obtain the external public-facing IPv4 address of the compromised host. [52] |
| C0017 | C0017 | During C0017 , APT41 used cmd.exe /c ping %userdomain% for discovery. [53] |
| C0018 | C0018 | During C0018 , the threat actors ran nslookup and Advanced IP Scanner on the target network. [54] |
| S0274 | Calisto | Calisto runs the ifconfig command to obtain the IP address from the victim’s machine. [55] |
| S0335 | Carbon | Carbon can collect the IP address of the victims and other computers on the network using the commands: ipconfig -all nbtstat -n , and nbtstat -s . [56] [57] |
| S0261 | Catchamas | Catchamas gathers the Mac address, IP address, and the network adapter information from the victim’s machine. [58] |
| S0572 | Caterpillar WebShell | Caterpillar WebShell can gather the IP address from the victim's machine using the IP config command. [59] |
| S1204 | cd00r | cd00r can discover the IP for the network interface on the compromised device. [60] |
| S0674 | CharmPower | CharmPower has the ability to use ipconfig to enumerate system network settings. [61] |
| G0114 | Chimera | Chimera has used ipconfig , Ping , and tracert to enumerate the IP address and network environment and settings of the local host. [62] |
| S0667 | Chrommme | Chrommme can enumerate the IP address of a compromised host. [63] |
| S0660 | Clambling | Clambling can enumerate the IP address of a compromised machine. [64] [65] |
| S0154 | Cobalt Strike | Cobalt Strike can determine the NetBios name and the IP addresses of targets machines including domain controllers. [66] [67] |
| S0244 | Comnie | Comnie uses ipconfig /all and route PRINT to identify network adapter and interface information. [68] |
| S0575 | Conti | Conti can retrieve the ARP cache from the local system by using the GetIpNetTable() API call and check to ensure IP addresses it connects to are for local, non-Internet, systems. [69] |
| S0488 | CrackMapExec | CrackMapExec can collect DNS information from the targeted system. [70] |
| S1024 | CreepySnail | CreepySnail can use getmac and Get-NetIPAddress to enumerate network settings. [71] |
| S0115 | Crimson | Crimson contains a command to collect the victim MAC address and LAN IP. [72] [73] |
| S0625 | Cuba | Cuba can retrieve the ARP cache from the local system by using GetIpNetTable . [74] |
| S0687 | Cyclops Blink | Cyclops Blink can use the Linux API if_nameindex to gather network interface names. [75] [76] |
| G0012 | Darkhotel | Darkhotel has collected the IP address and network adapter information from the victim’s machine. [77] [78] |
| S1052 | DEADEYE | DEADEYE can discover the DNS domain name of a targeted system. [53] |
| S0354 | Denis | Denis uses ipconfig to gather the IP address from the system. [21] |
| S0659 | Diavol | Diavol can enumerate victims' local and external IPs when registering with C2. [79] |
| S0472 | down_new | down_new has the ability to identify the MAC address of a compromised host. [30] |
| G0035 | Dragonfly | Dragonfly has used batch scripts to enumerate network information, including information about trusts, zones, and the domain. [80] |
| S0567 | Dtrack | Dtrack can collect the host's IP addresses using the ipconfig command. [81] [82] |
| S0038 | Duqu | The reconnaissance modules used with Duqu can collect information on network configuration. [83] |
| S1159 | DUSTTRAP | DUSTTRAP can enumerate infected system network information. [84] |
| S0024 | Dyre | Dyre has the ability to identify network settings on a compromised host. [85] |
| G1006 | Earth Lusca | Earth Lusca used the command ipconfig to obtain information about network configurations. [86] |
| S0605 | EKANS | EKANS can determine the domain of a compromised host. [87] |
| S0081 | Elise | Elise executes ipconfig /all after initial communication is made to the remote server. [88] [89] |
| S0082 | Emissary | Emissary has the capability to execute the command ipconfig /all . [90] |
| S0363 | Empire | Empire can acquire network configuration information like DNS servers, public IP, and network proxies used by a host. [91] [92] |
| S0091 | Epic | Epic uses the nbtstat -n and nbtstat -s commands on the victim’s machine. [93] |
| S9003 | evilginx2 | evilginx2 can capture information from each session with a victim including the public IP used to access the server and the user agent. [94] |
| S0569 | Explosive | Explosive has collected the MAC address from the victim's machine. [95] |
| S0181 | FALLCHILL | FALLCHILL collects MAC address and local IP address information from the victim. [96] |
| S0512 | FatDuke | FatDuke can identify the MAC address on the target computer. [97] |
| S0171 | Felismus | Felismus collects the victim LAN IP address and sends it to the C2 server. [98] |
| S0267 | FELIXROOT | FELIXROOT collects information about the network including the IP address and DHCP server. [99] |
| G1016 | FIN13 | FIN13 has used nslookup and ipconfig for network reconnaissance efforts. FIN13 has also utilized a compromised Symantec Altiris console and LanDesk account to retrieve network information. [100] [101] |
| S0696 | Flagpro | Flagpro has been used to execute the ipconfig /all command on a victim system. [102] |
| C0001 | Frankenstein | During Frankenstein , the threat actors used Empire to find the public IP address of a compromised system. [92] |
| S1044 | FunnyDream | FunnyDream can parse the ProxyServer string in the Registry to discover http proxies. [103] |
| C0007 | FunnyDream | During FunnyDream , the threat actors used ipconfig for discovery on remote systems. [103] |
| G0093 | GALLIUM | GALLIUM used ipconfig /all to obtain information about the victim network configuration. The group also ran a modified version of NBTscan to identify available NetBIOS name servers. [104] |
| S0049 | GeminiDuke | GeminiDuke collects information on network settings and Internet proxy settings from the victim. [105] |
| S0588 | GoldMax | GoldMax retrieved a list of the system's network interface after execution. [106] |
| S1198 | Gomir | Gomir collects network information on infected systems such as listing interface names, MAC and IP addresses, and IPv6 addresses. [107] |
| S1138 | Gootloader | Gootloader can use an embedded script to check the IP address of potential victims visiting compromised websites. [108] |
| S0531 | Grandoreiro | Grandoreiro can determine the IP and physical location of the compromised host via IPinfo. [109] |
| S0237 | GravityRAT | GravityRAT collects the victim IP address, MAC address, as well as the victim account domain name. [110] |
| S0690 | Green Lambert | Green Lambert can obtain proxy information from a victim's machine using system environment variables. [111] [112] |
| S0632 | GrimAgent | GrimAgent can enumerate the IP and domain of a target system. [113] |
| G0125 | HAFNIUM | HAFNIUM has collected IP information via IPInfo. [114] |
| S1229 | Havoc | Havoc has a module for network enumeration including determining IP addresses. [115] |
| G1001 | HEXANE | HEXANE has used Ping and tracert for network discovery. [116] |
| S1249 | HexEval Loader | HexEval Loader has leveraged server-side client configurations to identify the public IP of the victim host. [117] |
| G0126 | Higaisa | Higaisa used ipconfig to gather network configuration information. [118] [119] |
| S0431 | HotCroissant | HotCroissant has the ability to identify the IP address of the compromised machine. [120] |
| S0203 | Hydraq | Hydraq creates a backdoor through which remote attackers can retrieve IP addresses of compromised machines. [121] [122] |
| S1022 | IceApple | The IceApple ifconfig module can iterate over all network interfaces on the host and retrieve the name, description, MAC address, DNS suffix, DNS servers, gateways, IPv4 addresses, and subnet masks. [123] |
| S0483 | IcedID | IcedID used the ipconfig /all command and a batch script to gather network information. [124] |
| S0101 | ifconfig | ifconfig can be used to display adapter configuration on Unix systems, including information for TCP/IP, DNS, and DHCP. |
| S0278 | iKitten | iKitten will look for the current IP address. [125] |
| S0604 | Industroyer | Industroyer ’s 61850 payload component enumerates connected network adapters and their corresponding IP addresses. [126] |
| S1245 | InvisibleFerret | InvisibleFerret has collected the local IP address, and external IP. [127] [128] |
| S0260 | InvisiMole | InvisiMole gathers information on the IP forwarding table, MAC address, configured proxy, and network SSID. [129] [130] |
| S0100 | ipconfig | ipconfig can be used to display adapter configuration on Windows systems, including information for TCP/IP, DNS, and DHCP. |
| S0015 | Ixeshe | Ixeshe enumerates the IP address, network proxy settings, and domain name from a victim's system. [131] |
| S1203 | J-magic | J-magic can compare the host and remote IPs to check if a received packet is from the infected machine. [132] |
| S0044 | JHUHUGIT | A JHUHUGIT variant gathers network interface card information. [133] |
| S0201 | JPIN | JPIN can obtain network information, including DNS, IP, and proxies. [134] |
| S0283 | jRAT | jRAT can gather victim internal and external IPs. [135] |
| S0265 | Kazuar | Kazuar gathers information about network adapters. [136] |
| G0004 | Ke3chang | Ke3chang has performed local network configuration discovery using ipconfig . [137] [138] [139] |
| S0487 | Kessel | Kessel has collected the DNS address of the infected host. [49] |
| S1020 | Kevin | Kevin can collect the MAC address and other information from a victim machine using ipconfig/all . [116] |
| S0387 | KeyBoy | KeyBoy can determine the public or WAN IP address for the system. [140] |
| S0271 | KEYMARBLE | KEYMARBLE gathers the MAC address of the victim’s machine. [141] |
| G0094 | Kimsuky | Kimsuky has used ipconfig/all and web beacons sent via email to gather network configuration information. [142] [143] Kimsuky has also identified Host IP addresses leveraging the WMI class Win32_NetworkAdapterConfiguration . [144] |
| S0250 | Koadic | Koadic can retrieve the contents of the IP routing table as well as information about the Windows domain. [145] [146] |
| S0641 | Kobalos | Kobalos can record the IP address of the target machine. [147] |
| S0356 | KONNI | KONNI can collect the IP address from the victim’s machine. [148] |
| S1075 | KOPILUWAK | KOPILUWAK can use Arp to discover a target's network configuration setttings. [149] |
| C0035 | KV Botnet Activity | KV Botnet Activity gathers victim IP information during initial installation stages. [150] |
| S0236 | Kwampirs | Kwampirs collects network adapter and interface information by using the commands ipconfig /all , arp -a and route print . It also collects the system's MAC address with getmac and domain configuration with net config workstation . [151] |
| S9035 | LAMEHUG | LAMEHUG can enumerate network information on compromised hosts. [152] |
| S1160 | Latrodectus | Latrodectus can discover the IP and MAC address of a targeted host. [153] [154] |
| G0032 | Lazarus Group | Lazarus Group malware IndiaIndia obtains and sends to its C2 server information about the first network interface card’s configuration, including IP address, gateways, subnet mask, DHCP information, and whether WINS is available. [155] [156] |
| S0395 | LightNeuron | LightNeuron gathers information about network adapters using the Win32 API call GetAdaptersInfo . [157] |
| S0513 | LiteDuke | LiteDuke has the ability to discover the proxy configuration of Firefox and/or Opera. [97] |
| S0681 | Lizar | Lizar has retrieved network information from a compromised host, such as the MAC address. [158] [159] |
| S9020 | LODEINFO | LODEINFO can enumerate the MAC address of the compromised host. [160] |
| S0447 | Lokibot | Lokibot has the ability to discover the domain name of the infected host. [161] |
| G0030 | Lotus Blossom | Lotus Blossom has used commands such as ipconfig and netstat to gather network information on compromised hosts. [162] |
| S0451 | LoudMiner | LoudMiner used a script to gather the IP address of the infected machine before sending to the C2. [163] |
| S0532 | Lucifer | Lucifer can collect the IP address of a compromised host. [164] |
| S1143 | LunarLoader | LunarLoader can verify the targeted host's DNS name which is then used in the creation of a decyrption key. [165] |
| S1141 | LunarWeb | LunarWeb can use shell commands to discover network adapters and configuration. [165] |
| S0409 | Machete | Machete collects the MAC address of the target computer and other network configuration information. [166] [167] |
| S1016 | MacMa | MacMa can collect IP addresses from a compromised host. [168] |
| S1060 | Mafalda | Mafalda can use the GetAdaptersInfo function to retrieve information about network adapters and the GetIpNetTable function to retrieve the IPv4 to physical network address mapping table. [169] |
| G0059 | Magic Hound | Magic Hound malware gathers the victim's local IP address, MAC address, and external IP address. [170] [171] [172] |
| S1182 | MagicRAT | MagicRAT collects system network information using commands such as ipconfig /all . [173] |
| S1156 | Manjusaka | Manjusaka gathers information about current network connections, local and remote addresses associated with them, and associated processes. [174] |
| G1051 | Medusa Group | Medusa Group has obtained host network details utilizing the command cmd.exe /c ipconfig /all . [175] |
| G0045 | menuPass | menuPass has used several tools to scan for open NetBIOS nameservers and enumerate NetBIOS sessions. [176] |
| S1015 | Milan | Milan can run C:\Windows\system32\cmd.exe /c cmd /c ipconfig /all 2>&1 to discover network settings. [177] |
| G1054 | MirrorFace | MirrorFace has used ipconfig for reconnaissance. [178] |
| S0084 | Mis-Type | Mis-Type may create a file containing the results of the command cmd.exe /c ipconfig /all . [179] |
| G1036 | Moonstone Sleet | Moonstone Sleet has gathered information on victim network configuration. [180] |
| S0149 | MoonWind | MoonWind obtains the victim IP address. [181] |
| S0284 | More_eggs | More_eggs has the capability to gather the IP address from the victim's machine. [182] |
| G1009 | Moses Staff | Moses Staff has collected the domain name of a compromised network. [183] |
| S0256 | Mosquito | Mosquito uses the ipconfig command. [184] |
| G0069 | MuddyWater | MuddyWater has used malware to collect the victim’s IP address and domain name. [185] |
| G0129 | Mustang Panda | Mustang Panda has used ipconfig and arp to determine network configuration information. [186] Mustang Panda has also utilized SharpNBTScan to scan the victim environment. [187] |
| S0205 | Naid | Naid collects the domain name from a compromised host. [188] |
| G0019 | Naikon | Naikon uses commands such as netsh interface show to discover network interface settings. [189] |
| S0228 | NanHaiShu | NanHaiShu can gather information about the victim proxy server. [190] |
| S0336 | NanoCore | NanoCore gathers the IP address from the victim’s machine. [191] |
| S0590 | NBTscan | NBTscan can be used to collect MAC addresses. [192] [193] |
| S0102 | nbtstat | nbtstat can be used to discover local NetBIOS domain names. |
| S0691 | Neoichor | Neoichor can gather the IP address from an infected host. [139] |
| S0198 | NETWIRE | NETWIRE can collect the IP address of a compromised host. [194] [195] |
| S1106 | NGLite | NGLite identifies the victim system MAC and IPv4 addresses and uses these to establish a victim identifier. [196] |
| S1147 | Nightdoor | Nightdoor gathers information on victim system network configuration such as MAC addresses. [197] |
| S1100 | Ninja | Ninja can enumerate the IP address on compromised systems. [198] |
| S0359 | Nltest | Nltest may be used to enumerate the parent domain of a local machine using /parentdomain . [199] |
| S0353 | NOKKI | NOKKI can gather information on the victim IP address. [200] |
| S0346 | OceanSalt | OceanSalt can collect the victim’s IP address. [201] |
| S0340 | Octopus | Octopus can collect the host IP address from the victim’s machine. [202] |
| G0049 | OilRig | OilRig has run ipconfig /all on a victim. [203] [204] |
| S0439 | Okrum | Okrum can collect network information, including the host IP address, DNS, and proxy information. [205] |
| S0365 | Olympic Destroyer | Olympic Destroyer uses API calls to enumerate the infected system's ARP table. [206] |
| C0060 | Operation AkaiRyū | During Operation AkaiRyū , MirrorFace used Arp and dir for discovery in compromised environments. [207] |
| C0012 | Operation CuckooBees | During Operation CuckooBees , the threat actors used ipconfig , nbtstat , tracert , route print , and cat /etc/hosts commands. [208] |
| C0014 | Operation Wocao | During Operation Wocao , threat actors discovered the local network configuration with ipconfig . [209] |
| S0229 | Orz | Orz can gather victim proxy information. [190] |
| S0165 | OSInfo | OSInfo discovers the current domain information. [19] |
| S0352 | OSX_OCEANLOTUS.D | OSX_OCEANLOTUS.D can collect the network interface MAC address on the infected host. [210] [211] |
| S0556 | Pay2Key | Pay2Key can identify the IP and MAC addresses of the compromised host. [212] |
| S1050 | PcShare | PcShare can obtain the proxy settings of a compromised machine using InternetQueryOptionA and its IP address by running nslookup myip.opendns.comresolver1.opendns.com\r\n . [103] |
| S0587 | Penquin | Penquin can report the IP of the compromised host to attacker controlled infrastructure. [213] |
| S1145 | Pikabot | Pikabot gathers victim network information through commands such as ipconfig and ipconfig /all . [214] |
| S1031 | PingPull | PingPull can retrieve the IP address of a compromised host. [215] |
| S0501 | PipeMon | PipeMon can collect and send the local IP address, RDP information, and the network adapter physical address as a part of its C2 beacon. [216] |
| S0124 | Pisloader | Pisloader has a command to collect the victim's IP address. [217] |
| S0254 | PLAINTEE | PLAINTEE uses the ipconfig /all command to gather the victim’s IP address. [218] |
| G1040 | Play | Play has used the information-stealing tool Grixba to enumerate network information. [219] |
| S0013 | PlugX | PlugX has captured victim IP address details of the targeted machine. [220] [221] |
| S0378 | PoshC2 | PoshC2 can enumerate network adapter information. [222] |
| S0139 | PowerDuke | PowerDuke has a command to get the victim's domain and NetBIOS name. [223] |
| S0441 | PowerShower | PowerShower has the ability to identify the current Windows domain of the infected host. [224] |
| S0223 | POWERSTATS | POWERSTATS can retrieve IP, network adapter configuration information, and domain from compromised hosts. [225] [226] |
| S0184 | POWRUNER | POWRUNER may collect network configuration data by running ipconfig /all on a victim. [227] |
| S0113 | Prikormka | A module in Prikormka collects information from the victim about its IP addresses and MAC addresses. [228] |
| S0238 | Proxysvc | Proxysvc collects the network adapter information and domain/username information based on current remote sessions. [229] |
| S1228 | PUBLOAD | PUBLOAD has obtained information about local networks through the ipconfig /all command. [230] |
| S0192 | Pupy | Pupy has built in commands to identify a host’s IP address and find out other network configuration settings by viewing connected sessions. [231] |
| S0583 | Pysa | Pysa can perform network reconnaissance using the Advanced IP Scanner tool. [232] |
| S0650 | QakBot | QakBot can use net config workstation , arp -a , nslookup , and ipconfig /all to gather network configuration information. [233] [234] [235] [236] [237] |
| S1242 | Qilin | Qilin can accept a command line argument identifying specific IPs. [238] |
| S0269 | QUADAGENT | QUADAGENT gathers the current domain the victim system belongs to. [239] |
| S0262 | QuasarRAT | QuasarRAT has the ability to enumerate the Wide Area Network (WAN) IP through requests to ip-api[.]com, freegeoip[.]net, or api[.]ipify[.]org observed with user-agent string Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0 . [240] |
| S1076 | QUIETCANARY | QUIETCANARY can identify the default proxy setting on a compromised host. [149] |
| S0458 | Ramsay | Ramsay can use ipconfig and Arp to collect network configuration information, including routing information and ARP tables. [241] |
| S0241 | RATANKBA | RATANKBA gathers the victim’s IP address via the ipconfig -all command. [242] [243] |
| S0172 | Reaver | Reaver collects the victim's IP address. [244] |
| S0153 | RedLeaves | RedLeaves can obtain information about network parameters. [176] |
| S1240 | RedLine Stealer | RedLine Stealer can enumeate information about victims’ systems including IP addresses. [245] |
| C0056 | RedPenguin | During RedPenguin , UNC3886 leveraged JunoOS CLI queries to obtain the interface index which contains system and network details. [246] [247] |
| S0125 | Remsec | Remsec can obtain information about network configuration, including the routing table, ARP cache, and DNS cache. [248] |
| S0379 | Revenge RAT | Revenge RAT collects the IP address and MAC address from the system. [249] |
| S0433 | Rifdoor | Rifdoor has the ability to identify the IP address of the compromised host. [250] |
| S0448 | Rising Sun | Rising Sun can detect network adapter and IP address information. [251] |
| S0270 | RogueRobin | RogueRobin gathers the IP address and domain from the victim’s machine. [252] |
| S0103 | route | route can be used to discover routing configuration information. |
| S1073 | Royal | Royal can enumerate IP addresses using GetIpAddrTable . [253] |
| S0446 | Ryuk | Ryuk has called GetIpNetTable in attempt to identify all mounted drives and hosts that have Address Resolution Protocol (ARP) entries. [254] [255] |
| S0085 | S-Type | S-Type has used ipconfig /all on a compromised host. [179] |
| S1210 | Sagerunex | Sagerunex will gather system information such as MAC and IP addresses. [162] |
| S1018 | Saint Bot | Saint Bot can collect the IP address of a victim machine. [256] |
| S1085 | Sardonic | Sardonic has the ability to execute the ipconfig command. [257] |
| G1015 | Scattered Spider | Scattered Spider has used network reconnaissance commands for discovery including ping and nltest . [258] |
| S0461 | SDBbot | SDBbot has the ability to determine the domain name and whether a proxy is configured on a compromised host. [259] |
| S0596 | ShadowPad | ShadowPad has collected the domain name of the victim system. [260] |
| C0045 | ShadowRay | During ShadowRay , threat actors invoked DNS queries from targeted machines to identify their IP addresses. [261] |
| S0140 | Shamoon | Shamoon obtains the target's IP address and local network segment. [262] [263] |
| S0450 | SHARPSTATS | SHARPSTATS has the ability to identify the domain of the compromised host. [226] |
| S0445 | ShimRatReporter | ShimRatReporter gathered the local proxy, domain, IP, routing tables, mac address, gateway, DNS servers, and DHCP status information from an infected host. [264] |
| S1178 | ShrinkLocker | ShrinkLocker captures the IP address of the victim system and sends this to the attacker following encryption. [265] |
| S0589 | Sibot | Sibot checked if the compromised system is configured to use proxies. [106] |
| G1008 | SideCopy | SideCopy has identified the IP address of a compromised host. [5] |
| S0610 | SideTwist | SideTwist has the ability to collect the domain name on a compromised host. [266] |
| G0121 | Sidewinder | Sidewinder has used malware to collect information on network interfaces, including the MAC address. [267] |
| S0633 | Sliver | Sliver has the ability to gather network configuration information. [268] |
| S1035 | Small Sieve | Small Sieve can obtain the IP address of a victim host. [269] |
| S1124 | SocGholish | SocGholish has the ability to enumerate the domain name of a victim, as well as if the host is a member of an Active Directory domain. [270] [271] [272] |
| S0516 | SoreFang | SoreFang can collect the TCP/IP, DNS, DHCP, and network adapter configuration on a compromised host via ipconfig.exe /all . [273] |
| S0374 | SpeakUp | SpeakUp uses the ifconfig -a command. [274] |
| S0646 | SpicyOmelette | SpicyOmelette can identify the IP of a compromised system. [275] |
| S1030 | Squirrelwaffle | Squirrelwaffle has collected the victim’s external IP address. [276] |
| S1037 | STARWHALE | STARWHALE has the ability to collect the IP address of an infected host. [277] |
| G0038 | Stealth Falcon | Stealth Falcon malware gathers the Address Resolution Protocol (ARP) table from the victim. [278] |
| S0491 | StrongPity | StrongPity can identify the IP address of a compromised host. [279] |
| S0603 | Stuxnet | Stuxnet collects the IP address of a compromised system. [280] |
| S0559 | SUNBURST | SUNBURST collected all network interface MAC addresses that are up and not loopback devices, as well as IP address, DHCP configuration, and domain information. [281] |
| S0018 | Sykipot | Sykipot may use ipconfig /all to gather system network configuration details. [282] |
| S0060 | Sys10 | Sys10 collects the local IP address of the victim and sends it to the C2. [189] |
| S0663 | SysUpdate | SysUpdate can collected the IP address and domain name of a compromised host. [283] |
| S0098 | T9000 | T9000 gathers and beacons the MAC and IP addresses during installation. [284] |
| S0011 | Taidoor | Taidoor has collected the MAC address of a compromised host; it can also use GetAdaptersInfo to identify network adapters. [285] [286] |
| S0467 | TajMahal | TajMahal has the ability to identify the MAC address on an infected host. [287] |
| G0139 | TeamTNT | TeamTNT has enumerated the host machine’s IP address. [288] |
| G0027 | Threat Group-3390 | Threat Group-3390 actors use NBTscan to discover vulnerable systems. [289] |
| S0678 | Torisma | Torisma can collect the local MAC address using GetAdaptersInfo as well as the system's IP address. [290] |
| S0266 | TrickBot | TrickBot obtains the IP address, location, and other relevant network information from the victim’s machine. [291] [292] [66] |
| S0094 | Trojan.Karagany | Trojan.Karagany can gather information on the network configuration of a compromised host. [293] |
| S1196 | Troll Stealer | Troll Stealer collects the MAC address of victim devices. [294] |
| G0081 | Tropic Trooper | Tropic Trooper has used scripts to collect the host's network topology. [295] |
| S0436 | TSCookie | TSCookie has the ability to identify the IP of the infected host. [296] |
| S0647 | Turian | Turian can retrieve the internal IP address of a compromised host. [297] |
| G0010 | Turla | Turla surveys a system upon check-in to discover network configuration details using the arp -a , nbtstat -n , net config , ipconfig /all , and route commands, as well as NBTscan . [93] [298] [299] Turla RPC backdoors have also retrieved registered RPC interface information from process memory. [300] |
| S0130 | Unknown Logger | Unknown Logger can obtain information about the victim's IP address. [301] |
| S0275 | UPPERCUT | UPPERCUT has the capability to gather the victim's proxy information. [302] |
| S0452 | USBferry | USBferry can detect the infected machine's network topology using ipconfig and arp . [295] |
| S0476 | Valak | Valak has the ability to identify the domain and the MAC and IP addresses of an infected machine. [303] |
| S0257 | VERMIN | VERMIN gathers the local IP address. [304] |
| S0180 | Volgmer | Volgmer can gather the IP address from the victim's machine. [305] |
| G1017 | Volt Typhoon | Volt Typhoon has executed multiple commands to enumerate network topology and settings including ipconfig , netsh interface firewall show all , and netsh interface portproxy show all . [306] |
| S0366 | WannaCry | WannaCry will attempt to determine the local network segment it is a part of. [307] |
| S0515 | WellMail | WellMail can identify the IP address of the victim system. [308] |
| S0514 | WellMess | WellMess can identify the IP address and user domain on the target machine. [309] [310] |
| G0102 | Wizard Spider | Wizard Spider has used ipconfig to identify the network configuration of a victim machine. Wizard Spider has also used the PowerShell cmdlet Get-ADComputer to collect IP address data from Active Directory. [311] [312] |
| S1065 | Woody RAT | Woody RAT can retrieve network interface and proxy information. [313] |
| S0341 | Xbash | Xbash can collect IP addresses and local intranet information from a victim’s machine. [314] |
| S0653 | xCaon | xCaon has used the GetAdaptersInfo() API call to get the victim's MAC address. [50] |
| S1248 | XORIndex Loader | XORIndex Loader has leveraged webservices to identify the public IP of the victim host. [315] |
| S0248 | yty | yty runs ipconfig /all and collects the domain name. [316] |
| S0251 | Zebrocy | Zebrocy runs the ipconfig /all command. [317] |
| S0230 | ZeroT | ZeroT gathers the victim's IP address and domain information, and then sends it to its C2 server. [318] |
| G0128 | ZIRCONIUM | ZIRCONIUM has used a tool to enumerate proxy settings in the target environment. [319] |
| S0350 | zwShell | zwShell can obtain the victim IP address. [320] |

---

## Mitigations

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0195 | Behavioral Detection of System Network Configuration Discovery | AN0559 | Execution of built-in tools (e.g., ipconfig, route, netsh) or PowerShell/WMI queries to enumerate IP, MAC, interface status, or routing configuration. |
| AN0560 | Execution of ifconfig , ip a , or access to /proc/net/ indicating collection of local interface and route configuration. |  |  |
| AN0561 | Execution of ifconfig , networksetup , or system_profiler to query IP/MAC/interface configuration and status. |  |  |
| AN0562 | Use of esxcli network commands (e.g., esxcli network nic list , esxcli network ip interface ipv4 get ) via SSH or hostd to enumerate adapter and IP information. |  |  |
| AN0563 | CLI-based execution of interface and routing discovery commands (e.g., show ip interface , show arp , show route ) over Telnet, SSH, or console. |  |  |

---

## Detection Strategy

| ID | Name | Analytic ID | Analytic Description |
|---|---|---|---|
| DET0195 | Behavioral Detection of System Network Configuration Discovery | AN0559 | Execution of built-in tools (e.g., ipconfig, route, netsh) or PowerShell/WMI queries to enumerate IP, MAC, interface status, or routing configuration. |
| AN0560 | Execution of ifconfig , ip a , or access to /proc/net/ indicating collection of local interface and route configuration. |  |  |
| AN0561 | Execution of ifconfig , networksetup , or system_profiler to query IP/MAC/interface configuration and status. |  |  |
| AN0562 | Use of esxcli network commands (e.g., esxcli network nic list , esxcli network ip interface ipv4 get ) via SSH or hostd to enumerate adapter and IP information. |  |  |
| AN0563 | CLI-based execution of interface and routing discovery commands (e.g., show ip interface , show arp , show route ) over Telnet, SSH, or console. |  |  |

---

## References

- [US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure Devices. Retrieved October 19, 2020.](https://www.us-cert.gov/ncas/alerts/TA18-106A)
- [Gyler, C.,Perez D.,Jones, S.,Miller, S.. (2021, February 25). This is Not a Test: APT41 Initiates Global Intrusion Campaign Using Multiple Exploits. Retrieved February 17, 2022.](https://www.mandiant.com/resources/apt41-initiates-global-intrusion-campaign-using-multiple-exploits)
- [Pham Duy Phuc, Max Kersten, Noël Keijzer, and Michaël Schrijver. (2024, February 14). RansomHouse am See. Retrieved March 26, 2025.](https://www.trellix.com/en-au/blogs/research/ransomhouse-am-see/)
- [CERT Polska. (2026, January 30). Energy Sector Incident Report – 29 December. Retrieved April 22, 2026.](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Report_2025.pdf)
- [Threat Intelligence Team. (2021, December 2). SideCopy APT: Connecting lures victims, payloads to infrastructure. Retrieved June 13, 2022.](https://www.malwarebytes.com/blog/news/2021/12/sidecopy-apt-connecting-lures-to-victims-payloads-to-infrastructure)
- [Brian Donohue, Katie Nickels, Paul Michaud, Adina Bodkins, Taylor Chapman, Tony Lambert, Jeff Felling, Kyle Rainey, Mike Haag, Matt Graeber, Aaron Didier.. (2020, October 29). A Bazar start: How one hospital thwarted a Ryuk ransomware outbreak. Retrieved October 30, 2020.](https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/)
- [McKeague, B. et al. (2019, April 5). Pick-Six: Intercepting a FIN6 Intrusion, an Actor Recently Tied to Ryuk and LockerGoga Ransomware. Retrieved April 17, 2019.](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html)
- [Goody, K., et al (2019, January 11). A Nasty Trick: From Credential Theft Malware to Business Disruption. Retrieved May 12, 2020.](https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html)
- [FireEye Threat Intelligence. (2015, December 1). China-based Cyber Threat Group Uses Dropbox for Malware Communications and Targets Hong Kong Media Outlets. Retrieved December 4, 2015.](https://www.fireeye.com/blog/threat-research/2015/11/china-based-threat.html)
- [The DigiTrust Group. (2017, January 12). The Rise of Agent Tesla. Retrieved November 5, 2018.](https://www.digitrustgroup.com/agent-tesla-keylogger/)
- [Walter, J. (2020, August 10). Agent Tesla | Old RAT Uses New Tricks to Stay on Top. Retrieved December 11, 2020.](https://labs.sentinelone.com/agent-tesla-old-rat-uses-new-tricks-to-stay-on-top/)
- [Shevchenko, S.. (2008, November 30). Agent.btz - A Threat That Hit Pentagon. Retrieved April 8, 2016.](http://blog.threatexpert.com/2008/11/agentbtz-threat-that-hit-pentagon.html)
- [Kasuya, M. (2020, January 8). Threat Spotlight: Amadey Bot Targets Non-Russian Users. Retrieved July 14, 2022.](https://blogs.blackberry.com/en/2020/01/threat-spotlight-amadey-bot)
- [Grange, W. (2020, July 13). Anchor_dns malware goes cross platform. Retrieved September 10, 2020.](https://medium.com/stage-2-security/anchor-dns-malware-family-goes-cross-platform-d807ba13ca30)
- [Anthropic. (2025, November). Disrupting the first reported AI-orchestrated cyber espionage campaign. Retrieved April 20, 2026.](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
- [Jazi, H. (2021, June 1). Kimsuky APT continues to target South Korean government using AppleSeed backdoor. Retrieved June 10, 2021.](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
- [Mandiant. (n.d.). APT1 Exposing One of China’s Cyber Espionage Units. Retrieved July 18, 2016.](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
- [Grunzweig, J., Lee, B. (2016, January 22). New Attacks Linked to C0d0so0 Group. Retrieved August 2, 2018.](https://researchcenter.paloaltonetworks.com/2016/01/new-attacks-linked-to-c0d0s0-group/)
- [Symantec Security Response. (2016, September 6). Buckeye cyberespionage group shifts gaze from US to Hong Kong. Retrieved September 26, 2016.](https://web.archive.org/web/20160910124439/http://www.symantec.com/connect/blogs/buckeye-cyberespionage-group-shifts-gaze-us-hong-kong)
- [Yates, M. (2017, June 18). APT3 Uncovered: The code evolution of Pirpi. Retrieved September 28, 2017.](https://recon.cx/2017/montreal/resources/slides/RECON-MTL-2017-evolution_of_pirpi.pdf)
- [Dahan, A. (2017). Operation Cobalt Kitty. Retrieved December 27, 2018.](https://cdn2.hubspot.net/hubfs/3354902/Cybereason%20Labs%20Analysis%20Operation%20Cobalt%20Kitty.pdf)
- [Fraser, N., et al. (2019, August 7). Double DragonAPT41, a dual espionage and cyber crime operation APT41. Retrieved September 23, 2019.](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
- [Rostovcev, N. (2021, June 10). Big airline heist APT41 likely behind a third-party attack on Air India. Retrieved August 26, 2021.](https://www.group-ib.com/blog/colunmtk-apt41/)
- [Mandiant. (n.d.). APT42: Crooked Charms, Cons and Compromises. Retrieved October 9, 2024.](https://services.google.com/fh/files/misc/apt42-crooked-charms-cons-and-compromises.pdf)
- [CheckPoint. (2020, May 7). Naikon APT: Cyber Espionage Reloaded. Retrieved May 26, 2020.](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
- [Microsoft. (n.d.). Arp. Retrieved April 17, 2016.](https://technet.microsoft.com/en-us/library/bb490864.aspx)
- [Doaty, J., Garrett, P.. (2018, September 10). We’re Seeing a Resurgence of the Demonic Astaroth WMIC Trojan. Retrieved September 25, 2024.](https://web.archive.org/web/20200302071436/https://cofense.com/seeing-resurgence-demonic-astaroth-wmic-trojan/)
- [Dominik Breitenbacher. (2025, March 18). Operation AkaiRyū: MirrorFace invites Europe to Expo 2025 and revives ANEL backdoor. Retrieved May 22, 2025.](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)
- [Gahlot, A. (n.d.). Threat Hunting for Avaddon Ransomware. Retrieved August 19, 2021.](https://awakesecurity.com/blog/threat-hunting-for-avaddon-ransomware/)
- [Chen, J. et al. (2019, November). Operation ENDTRADE: TICK’s Multi-Stage Backdoors for Attacking Industries and Stealing Classified Data. Retrieved June 9, 2020.](https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf)
- [Yan, T., et al. (2018, November 21). New Wine in Old Bottle: New Azorult Variant Found in FindMyName Campaign using Fallout Exploit Kit. Retrieved November 29, 2018.](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
- [Unit 42. (2019, February 22). New BabyShark Malware Targets U.S. National Security Think Tanks. Retrieved October 7, 2019.](https://unit42.paloaltonetworks.com/new-babyshark-malware-targets-u-s-national-security-think-tanks/)
- [Symantec Security Response. (2014, June 30). Dragonfly: Cyberespionage Attacks Against Energy Suppliers. Retrieved April 8, 2016.](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
- [Slowik, J. (2021, October). THE BAFFLING BERSERK BEAR: A DECADE’S ACTIVITY TARGETING CRITICAL INFRASTRUCTURE. Retrieved December 6, 2021.](https://vblocalhost.com/uploads/VB2021-Slowik.pdf)
- [US-CERT. (2018, February 06). Malware Analysis Report (MAR) - 10135536-G. Retrieved June 7, 2018.](https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-G.PDF)
- [Accenture iDefense Unit. (2019, March 5). Mudcarp's Focus on Submarine Technologies. Retrieved August 24, 2021.](https://www.accenture.com/us-en/blogs/cyber-defense/mudcarps-focus-on-submarine-technologies)
- [Check Point. (2020, November 26). Bandook: Signed & Delivered. Retrieved May 31, 2021.](https://research.checkpoint.com/2020/bandook-signed-delivered/)
- [Cybereason Nocturnus. (2020, July 16). A BAZAR OF TRICKS: FOLLOWING TEAM9’S DEVELOPMENT CYCLES. Retrieved November 18, 2020.](https://www.cybereason.com/blog/a-bazar-of-tricks-following-team9s-development-cycles)
- [Hayashi, K., Ray, V. (2018, July 31). Bisonal Malware Used in Attacks Against Russia and South Korea. Retrieved August 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-bisonal-malware-used-attacks-russia-south-korea/)
- [Zykov, K. (2020, August 13). CactusPete APT group’s updated Bisonal backdoor. Retrieved May 5, 2021.](https://securelist.com/cactuspete-apt-groups-updated-bisonal-backdoor/97962/)
- [Mercer, W., et al. (2020, March 5). Bisonal: 10 years of play. Retrieved January 26, 2022.](https://blog.talosintelligence.com/2020/03/bisonal-10-years-of-play.html)
- [US Federal Bureau of Investigation & US Secret Service. (2022, February 11). Indicators of Compromise Associated with BlackByte Ransomware. Retrieved December 16, 2024.](https://www.ic3.gov/CSA/2022/220211.pdf)
- [Microsoft Incident Response. (2023, July 6). The five-day job: A BlackByte ransomware intrusion case study. Retrieved December 16, 2024.](https://www.microsoft.com/en-us/security/blog/2023/07/06/the-five-day-job-a-blackbyte-ransomware-intrusion-case-study/)
- [F-Secure Labs. (2014). BlackEnergy & Quedagh: The convergence of crimeware and APT attacks. Retrieved March 24, 2016.](https://blog-assets.f-secure.com/wp-content/uploads/2019/10/15163408/BlackEnergy_Quedagh.pdf)
- [Baumgartner, K. and Garnaeva, M.. (2014, November 3). BE2 custom plugins, router abuse, and target profiles. Retrieved March 24, 2016.](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
- [US-CERT. (2020, August 19). MAR-10295134-1.v1 – North Korean Remote Access Trojan: BLINDINGCAN. Retrieved August 19, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-232a)
- [Cash, D., Grunzweig, J., Meltzer, M., Adair, S., Lancaster, T. (2021, August 17). North Korean APT InkySquid Infects Victims Using Browser Exploits. Retrieved September 30, 2021.](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
- [Scott Henderson, Cristiana Kittner, Sarah Hawley & Mark Lechtik, Google Cloud. (2023, January 19). Suspected Chinese Threat Actors Exploiting FortiOS Vulnerability (CVE-2022-42475). Retrieved December 31, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/chinese-actors-exploit-fortios-flaw/)
- [Dumont, R., M.Léveillé, M., Porcher, H. (2018, December 1). THE DARK SIDE OF THE FORSSHE A landscape of OpenSSH backdoors. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2018/12/ESET-The_Dark_Side_of_the_ForSSHe.pdf)
- [CheckPoint Research. (2021, July 1). IndigoZebra APT continues to attack Central Asia with evolving tools. Retrieved September 24, 2021.](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
- [Sherstobitoff, R., Saavedra-Morales, J. (2018, February 02). Gold Dragon Widens Olympics Malware Attacks, Gains Permanent Presence on Victims’ Systems. Retrieved June 6, 2018.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/gold-dragon-widens-olympics-malware-attacks-gains-permanent-presence-on-victims-systems/)
- [DFIR Report. (2021, November 29). CONTInuing the Bazar Ransomware Story. Retrieved September 29, 2022.](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
- [Rufus Brown, Van Ta, Douglas Bienstock, Geoff Ackerman, John Wolfram. (2022, March 8). Does This Look Infected? A Summary of APT41 Targeting U.S. State Governments. Retrieved July 8, 2022.](https://www.mandiant.com/resources/apt41-us-state-governments)
- [Costa, F. (2022, May 1). RaaS AvosLocker Incident Response Analysis. Retrieved January 11, 2023.](https://www.linkedin.com/pulse/raas-avoslocker-incident-response-analysis-fl%C3%A1vio-costa?trk=articles_directory)
- [Kuzin, M., Zelensky S. (2018, July 20). Calisto Trojan for macOS. Retrieved September 7, 2018.](https://securelist.com/calisto-trojan-for-macos/86543/)
- [ESET. (2017, March 30). Carbon Paper: Peering into Turla’s second stage backdoor. Retrieved November 7, 2018.](https://www.welivesecurity.com/2017/03/30/carbon-paper-peering-turlas-second-stage-backdoor/)
- [GovCERT. (2016, May 23). Technical Report about the Espionage Case at RUAG. Retrieved November 7, 2018.](https://web.archive.org/web/20170718174931/https://www.melani.admin.ch/dam/melani/de/dokumente/2016/technical%20report%20ruag.pdf.download.pdf/Report_Ruag-Espionage-Case.pdf)
- [Balanza, M. (2018, April 02). Infostealer.Catchamas. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165711/https://www-west.symantec.com/content/symantec/english/en/security-center/writeup.html/2018-040209-1742-99)
- [ClearSky Cyber Security. (2021, January). “Lebanese Cedar” APT Global Lebanese Espionage Campaign Leveraging Web Servers. Retrieved February 10, 2021.](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)
- [Hartrell, Greg. (2002, August). Get a handle on cd00r: The invisible backdoor. Retrieved October 13, 2018.](https://www.giac.org/paper/gcih/342/handle-cd00r-invisible-backdoor/103631)
- [Check Point. (2022, January 11). APT35 exploits Log4j vulnerability to distribute new modular PowerShell toolkit. Retrieved January 24, 2022.](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
- [Jansen, W . (2021, January 12). Abusing cloud services to fly under the radar. Retrieved September 12, 2024.](https://web.archive.org/web/20230218064220/https://research.nccgroup.com/2021/01/12/abusing-cloud-services-to-fly-under-the-radar/)
- [Dupuy, T. and Faou, M. (2021, June). Gelsemium. Retrieved November 30, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
- [Lunghi, D. et al. (2020, February). Uncovering DRBControl. Retrieved November 12, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
- [Chen, T. and Chen, Z. (2020, February 17). CLAMBLING - A New Backdoor Base On Dropbox. Retrieved November 12, 2021.](https://www.talent-jump.com/article/2020/02/17/CLAMBLING-A-New-Backdoor-Base-On-Dropbox-en/)
- [Dahan, A. et al. (2019, December 11). DROPPING ANCHOR: FROM A TRICKBOT INFECTION TO THE DISCOVERY OF THE ANCHOR MALWARE. Retrieved September 10, 2020.](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware)
- [Strategic Cyber LLC. (2020, November 5). Cobalt Strike: Advanced Threat Tactics for Penetration Testers. Retrieved April 13, 2021.](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
- [Grunzweig, J. (2018, January 31). Comnie Continues to Target Organizations in East Asia. Retrieved June 7, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-comnie-continues-target-organizations-east-asia/)
- [Baskin, B. (2020, July 8). TAU Threat Discovery: Conti Ransomware. Retrieved February 17, 2021.](https://www.carbonblack.com/blog/tau-threat-discovery-conti-ransomware/)
- [byt3bl33d3r. (2018, September 8). SMB: Command Reference. Retrieved July 17, 2020.](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
- [Microsoft. (2022, June 2). Exposing POLONIUM activity and infrastructure targeting Israeli organizations. Retrieved July 1, 2022.](https://www.microsoft.com/security/blog/2022/06/02/exposing-polonium-activity-and-infrastructure-targeting-israeli-organizations/)
- [Huss, D. (2016, March 1). Operation Transparent Tribe. Retrieved June 8, 2016.](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
- [Dedola, G. (2020, August 20). Transparent Tribe: Evolution analysis, part 1. Retrieved September 2, 2021.](https://securelist.com/transparent-tribe-part-1/98127/)
- [Roccio, T., et al. (2021, April). Technical Analysis of Cuba Ransomware. Retrieved June 18, 2021.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-cuba-ransomware.pdf)
- [NCSC. (2022, February 23). Cyclops Blink Malware Analysis Report. Retrieved March 3, 2022.](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf)
- [Haquebord, F. et al. (2022, March 17). Cyclops Blink Sets Sights on Asus Routers. Retrieved March 17, 2022.](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html)
- [Kaspersky Lab's Global Research & Analysis Team. (2015, August 10). Darkhotel's attacks in 2015. Retrieved November 2, 2018.](https://securelist.com/darkhotels-attacks-in-2015/71713/)
- [Microsoft. (2016, July 14). Reverse engineering DUBNIUM – Stage 2 payload analysis . Retrieved March 31, 2021.](https://www.microsoft.com/security/blog/2016/07/14/reverse-engineering-dubnium-stage-2-payload-analysis/)
- [Neeamni, D., Rubinfeld, A.. (2021, July 1). Diavol - A New Ransomware Used By Wizard Spider?. Retrieved November 12, 2021.](https://www.fortinet.com/blog/threat-research/diavol-new-ransomware-used-by-wizard-spider)
- [US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other Critical Infrastructure Sectors. Retrieved June 6, 2018.](https://www.us-cert.gov/ncas/alerts/TA18-074A)
- [Konstantin Zykov. (2019, September 23). Hello! My name is Dtrack. Retrieved January 20, 2021.](https://securelist.com/my-name-is-dtrack/93338/)
- [Hod Gavriel. (2019, November 21). Dtrack: In-depth analysis of APT on a nuclear power plant. Retrieved January 20, 2021.](https://www.cyberbit.com/blog/endpoint-security/dtrack-apt-malware-found-in-nuclear-power-plant/)
- [Symantec Security Response. (2011, November). W32.Duqu: The precursor to the next Stuxnet. Retrieved September 17, 2015.](https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/w32_duqu_the_precursor_to_the_next_stuxnet.pdf)
- [Mike Stokkel et al. (2024, July 18). APT41 Has Arisen From the DUST. Retrieved September 16, 2024.](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
- [hasherezade. (2015, November 4). A Technical Look At Dyreza. Retrieved June 15, 2020.](https://blog.malwarebytes.com/threat-analysis/2015/11/a-technical-look-at-dyreza/)
- [Chen, J., et al. (2022). Delving Deep: An Analysis of Earth Lusca’s Operations. Retrieved July 1, 2022.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/22/a/earth-lusca-employs-sophisticated-infrastructure-varied-tools-and-techniques/technical-brief-delving-deep-an-analysis-of-earth-lusca-operations.pdf)
- [Singleton, C. and Kiefer, C. (2020, September 28). Ransomware 2020: Attack Trends Affecting Organizations Worldwide. Retrieved September 20, 2021.](https://securityintelligence.com/posts/ransomware-2020-attack-trends-new-techniques-affecting-organizations-worldwide/)
- [Falcone, R., et al.. (2015, June 16). Operation Lotus Blossom. Retrieved February 15, 2016.](https://www.paloaltonetworks.com/resources/research/unit42-operation-lotus-blossom.html)
- [Accenture Security. (2018, January 27). DRAGONFISH DELIVERS NEW FORM OF ELISE MALWARE TARGETING ASEAN DEFENCE MINISTERS’ MEETING AND ASSOCIATES. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165226/https://www.accenture.com/t20180127T003755Z_w_/us-en/_acnmedia/PDF-46/Accenture-Security-Dragonfish-Threat-Analysis.pdf)
- [Falcone, R. and Miller-Osborn, J. (2016, February 3). Emissary Trojan Changelog: Did Operation Lotus Blossom Cause It to Evolve?. Retrieved February 15, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/)
- [Schroeder, W., Warner, J., Nelson, M. (n.d.). Github PowerShellEmpire. Retrieved April 28, 2016.](https://github.com/PowerShellEmpire/Empire)
- [Adamitis, D. et al. (2019, June 4). It's alive: Threat actors cobble together open-source pieces into monstrous Frankenstein campaign. Retrieved May 11, 2020.](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
- [Kaspersky Lab's Global Research and Analysis Team. (2014, August 7). The Epic Turla Operation: Solving some of the mysteries of Snake/Uroburos. Retrieved December 11, 2014.](https://securelist.com/the-epic-turla-operation/65545/)
- [Everts, M. (2025, March 28). Stealing user credentials with evilginx. Retrieved January 27, 2026.](https://www.sophos.com/en-us/blog/stealing-user-credentials-with-evilginx)
- [Threat Intelligence and Research. (2015, March 30). VOLATILE CEDAR. Retrieved February 8, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/03/20082004/volatile-cedar-technical-report.pdf)
- [US-CERT. (2017, November 22). Alert (TA17-318A): HIDDEN COBRA – North Korean Remote Administration Tool: FALLCHILL. Retrieved December 7, 2017.](https://www.us-cert.gov/ncas/alerts/TA17-318A)
- [Faou, M., Tartare, M., Dupuy, T. (2019, October). OPERATION GHOST. Retrieved September 23, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Operation_Ghost_Dukes.pdf)
- [Somerville, L. and Toro, A. (2017, March 30). Playing Cat & Mouse: Introducing the Felismus Malware. Retrieved November 16, 2017.](https://blogs.forcepoint.com/security-labs/playing-cat-mouse-introducing-felismus-malware)
- [Cherepanov, A. (2018, October). GREYENERGY A successor to BlackEnergy. Retrieved November 15, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/10/ESET_GreyEnergy.pdf)
- [Ta, V., et al. (2022, August 8). FIN13: A Cybercriminal Threat Actor Focused on Mexico. Retrieved February 9, 2023.](https://www.mandiant.com/resources/blog/fin13-cybercriminal-mexico)
- [Sygnia Incident Response Team. (2022, January 5). TG2003: ELEPHANT BEETLE UNCOVERING AN ORGANIZED FINANCIAL-THEFT OPERATION. Retrieved February 9, 2023.](https://web.archive.org/web/20220105132433/https://f.hubspotusercontent30.net/hubfs/8776530/Sygnia-%20Elephant%20Beetle_Jan2022.pdf)
- [Hada, H. (2021, December 28). Flagpro The new malware used by BlackTech. Retrieved March 25, 2022.](https://insight-jp.nttsecurity.com/post/102hf3q/flagpro-the-new-malware-used-by-blacktech)
- [Vrabie, V. (2020, November). Dissecting a Chinese APT Targeting South Eastern Asian Government Institutions. Retrieved September 19, 2022.](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
- [Cybereason Nocturnus. (2019, June 25). Operation Soft Cell: A Worldwide Campaign Against Telecommunications Providers. Retrieved July 18, 2019.](https://www.cybereason.com/blog/operation-soft-cell-a-worldwide-campaign-against-telecommunications-providers)
- [F-Secure Labs. (2015, September 17). The Dukes: 7 years of Russian cyberespionage. Retrieved December 10, 2015.](https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf)
- [Nafisi, R., Lelli, A. (2021, March 4). GoldMax, GoldFinder, and Sibot: Analyzing NOBELIUM’s layered persistence. Retrieved March 8, 2021.](https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/)
- [Symantec Threat Hunter Team. (2024, May 16). Springtail: New Linux Backdoor Added to Toolkit. Retrieved January 17, 2025.](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
- [Pirozzi, A. (2021, June 16). Gootloader: ‘Initial Access as a Service’ Platform Expands Its Search for High Value Targets. Retrieved May 28, 2024.](https://www.sentinelone.com/labs/gootloader-initial-access-as-a-service-platform-expands-its-search-for-high-value-targets/)
- [ESET. (2020, April 28). Grandoreiro: How engorged can an EXE get?. Retrieved November 13, 2020.](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
- [Mercer, W., Rascagneres, P. (2018, April 26). GravityRAT - The Two-Year Evolution Of An APT Targeting India. Retrieved May 16, 2018.](https://blog.talosintelligence.com/2018/04/gravityrat-two-year-evolution-of-apt.html)
- [Sandvik, Runa. (2021, October 1). Made In America: Green Lambert for OS X. Retrieved March 21, 2022.](https://objective-see.com/blog/blog_0x68.html)
- [Sandvik, Runa. (2021, October 18). Green Lambert and ATT&CK. Retrieved November 17, 2024.](https://web.archive.org/web/20211018145402/https://www.glitch-cat.com/blog/green-lambert-and-attack)
- [Priego, A. (2021, July). THE BROTHERS GRIM: THE REVERSING TALE OF GRIMAGENT MALWARE USED BY RYUK. Retrieved September 19, 2024.](https://www.group-ib.com/blog/grimagent/)
- [Eoin Miller. (2021, March 23). Defending Against the Zero Day: Analyzing Attacker Behavior Post-Exploitation of Microsoft Exchange. Retrieved October 27, 2022.](https://www.rapid7.com/blog/post/2021/03/23/defending-against-the-zero-day-analyzing-attacker-behavior-post-exploitation-of-microsoft-exchange/)
- [Ungur, P. (n.d.). HAVOC. Retrieved August 4, 2025.](https://havocframework.com/docs/welcome)
- [Kayal, A. et al. (2021, October). LYCEUM REBORN: COUNTERINTELLIGENCE IN THE MIDDLE EAST. Retrieved June 14, 2022.](https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf)
- [Kirill Boychenko. (2025, June 25). Another Wave: North Korean Contagious Interview Campaign Drops 35 New Malicious npm Packages. Retrieved October 19, 2025.](https://socket.dev/blog/north-korean-contagious-interview-campaign-drops-35-new-malicious-npm-packages)
- [Malwarebytes Threat Intelligence Team. (2020, June 4). New LNK attack tied to Higaisa APT discovered. Retrieved March 2, 2021.](https://blog.malwarebytes.com/threat-analysis/2020/06/higaisa/)
- [Singh, S. Singh, A. (2020, June 11). The Return on the Higaisa APT. Retrieved March 2, 2021.](https://www.zscaler.com/blogs/security-research/return-higaisa-apt)
- [US-CERT. (2020, February 20). MAR-10271944-1.v1 – North Korean Trojan: HOTCROISSANT. Retrieved May 1, 2020.](https://www.us-cert.gov/ncas/analysis-reports/ar20-045d)
- [Symantec Security Response. (2010, January 18). The Trojan.Hydraq Incident. Retrieved February 20, 2018.](https://www.symantec.com/connect/blogs/trojanhydraq-incident)
- [Lelli, A. (2010, January 11). Trojan.Hydraq. Retrieved February 20, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
- [CrowdStrike. (2022, May). ICEAPPLE: A NOVEL INTERNET INFORMATION SERVICES (IIS) POST-EXPLOITATION FRAMEWORK. Retrieved June 27, 2022.](https://www.crowdstrike.com/wp-content/uploads/2022/05/crowdstrike-iceapple-a-novel-internet-information-services-post-exploitation-framework.pdf)
- [DFIR. (2022, April 25). Quantum Ransomware. Retrieved July 26, 2024.](https://thedfirreport.com/2022/04/25/quantum-ransomware/)
- [Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.](https://objective-see.com/blog/blog_0x25.html)
- [Anton Cherepanov. (2017, June 12). Win32/Industroyer: A new threat for industrial controls systems. Retrieved December 18, 2020.](https://www.welivesecurity.com/wp-content/uploads/2017/06/Win32_Industroyer.pdf)
- [Matej Havranek. (2025, February 20). DeceptiveDevelopment targets freelance developers. Retrieved October 17, 2025.](https://www.welivesecurity.com/en/eset-research/deceptivedevelopment-targets-freelance-developers/)
- [Unit 42. (2023, November 21). Hacking Employers and Seeking Employment: Two Job-Related Campaigns Bear Hallmarks of North Korean Threat Actors. Retrieved October 17, 2025.](https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/)
- [Hromcová, Z. (2018, June 07). InvisiMole: Surprisingly equipped spyware, undercover since 2013. Retrieved July 10, 2018.](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
- [Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
- [Sancho, D., et al. (2012, May 22). IXESHE An APT Campaign. Retrieved June 7, 2019.](https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp_ixeshe.pdf)
- [Black Lotus Labs. (2025, January 23). The J-Magic Show: Magic Packets and Where to find them. Retrieved February 17, 2025.](https://blog.lumen.com/the-j-magic-show-magic-packets-and-where-to-find-them/)
- [Unit 42. (2017, December 15). Unit 42 Playbook Viewer. Retrieved December 20, 2017.](https://pan-unit42.github.io/playbook_viewer/)
- [Windows Defender Advanced Threat Hunting Team. (2016, April 29). PLATINUM: Targeted attacks in South and Southeast Asia. Retrieved February 15, 2018.](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
- [Kamluk, V. & Gostev, A. (2016, February). Adwind - A Cross-Platform RAT. Retrieved April 23, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
- [Levene, B, et al. (2017, May 03). Kazuar: Multiplatform Espionage Backdoor with API Access. Retrieved July 17, 2018.](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
- [Villeneuve, N., Bennett, J. T., Moran, N., Haq, T., Scott, M., & Geers, K. (2014). OPERATION “KE3CHANG”: Targeted Attacks Against Ministries of Foreign Affairs. Retrieved November 12, 2014.](https://www.mandiant.com/resources/operation-ke3chang-targeted-attacks-against-ministries-of-foreign-affairs)
- [Smallridge, R. (2018, March 10). APT15 is alive and strong: An analysis of RoyalCli and RoyalDNS. Retrieved April 4, 2018.](https://research.nccgroup.com/2018/03/10/apt15-is-alive-and-strong-an-analysis-of-royalcli-and-royaldns/)
- [MSTIC. (2021, December 6). NICKEL targeting government organizations across Latin America and Europe. Retrieved March 18, 2022.](https://www.microsoft.com/security/blog/2021/12/06/nickel-targeting-government-organizations-across-latin-america-and-europe)
- [Parys, B. (2017, February 11). The KeyBoys are back in town. Retrieved June 13, 2019.](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)
- [US-CERT. (2018, August 09). MAR-10135536-17 – North Korean Trojan: KEYMARBLE. Retrieved August 16, 2018.](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
- [An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to high-profile South Korean targets. Retrieved December 29, 2021.](https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html)
- [Lesnewich, G. et al. (2024, April 16). From Social Engineering to DMARC Abuse: TA427’s Art of Information Gathering. Retrieved May 3, 2024.](https://www.proofpoint.com/us/blog/threat-insight/social-engineering-dmarc-abuse-ta427s-art-information-gathering)
- [Den Iuzvyk, Tim Peck. (2025, February 13). Analyzing DEEP#DRIVE: North Korean Threat Actors Observed Exploiting Trusted Platforms for Targeted Attacks. Retrieved August 19, 2025.](https://www.securonix.com/blog/analyzing-deepdrive-north-korean-threat-actors-observed-exploiting-trusted-platforms-for-targeted-attacks/)
- [Magius, J., et al. (2017, July 19). Koadic. Retrieved September 27, 2024.](https://github.com/offsecginger/koadic)
- [Jazi, H. (2021, February). LazyScripter: From Empire to double RAT. Retrieved November 17, 2024.](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
- [M.Leveille, M., Sanmillan, I. (2021, January). A WILD KOBALOS APPEARS Tricksy Linux malware goes after HPCs. Retrieved August 24, 2021.](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
- [Rascagneres, P. (2017, May 03). KONNI: A Malware Under The Radar For Years. Retrieved November 5, 2018.](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
- [Hawley, S. et al. (2023, February 2). Turla: A Galaxy of Opportunity. Retrieved May 15, 2023.](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
- [Black Lotus Labs. (2023, December 13). Routers Roasting On An Open Firewall: The KV-Botnet Investigation. Retrieved June 10, 2024.](https://blog.lumen.com/routers-roasting-on-an-open-firewall-the-kv-botnet-investigation/)
- [Symantec Security Response Attack Investigation Team. (2018, April 23). New Orangeworm attack group targets the healthcare sector in the U.S., Europe, and Asia. Retrieved May 8, 2018.](https://www.symantec.com/blogs/threat-intelligence/orangeworm-targets-healthcare-us-europe-asia)
- [Google Threat Intelligence Group. (2025, November 5). GTIG AI Threat Tracker: Advances in Threat Actor Usage of AI Tools. Retrieved March 31, 2026.](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
- [Stepanic, D. and Bousseaden, S. (2024, May 15). Spring Cleaning with LATRODECTUS: A Potential Replacement for ICEDID. Retrieved September 13, 2024.](https://www.elastic.co/security-labs/spring-cleaning-with-latrodectus)
- [Batista, J. (2024, June 17). Latrodectus, are you coming back?. Retrieved September 13, 2024.](https://www.bitsight.com/blog/latrodectus-are-you-coming-back)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Unraveling the Long Thread of the Sony Attack. Retrieved February 25, 2016.](https://web.archive.org/web/20160226161828/https://www.operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Report.pdf)
- [Novetta Threat Research Group. (2016, February 24). Operation Blockbuster: Loaders, Installers and Uninstallers Report. Retrieved November 17, 2024.](https://web.archive.org/web/20190508165631/https://operationblockbuster.com/wp-content/uploads/2016/02/Operation-Blockbuster-Loaders-Installers-and-Uninstallers-Report.pdf)
- [Faou, M. (2019, May). Turla LightNeuron: One email away from remote code execution. Retrieved June 24, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf)
- [BI.ZONE Cyber Threats Research Team. (2021, May 13). From pentest to APT attack: cybercriminal group FIN7 disguises its malware as an ethical hacker’s toolkit. Retrieved February 2, 2022.](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
- [Bourhis, P., Sekoia TDR. (2024, February 1). Unveiling the intricacies of DiceLoader. Retrieved May 14, 2025.](https://blog.sekoia.io/unveiling-the-intricacies-of-diceloader/)
- [Ishimaru, S. (2022, October 31). APT10: Tracking down LODEINFO 2022, part I. Retrieved April 17, 2026.](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-i/107742/)
- [Kazem, M. (2019, November 25). Trojan:W32/Lokibot. Retrieved May 15, 2020.](https://www.f-secure.com/v-descs/trojan_w32_lokibot.shtml)
- [Joey Chen, Cisco Talos. (2025, February 27). Lotus Blossom espionage group targets multiple industries with different versions of Sagerunex and hacking tools. Retrieved March 15, 2025.](https://blog.talosintelligence.com/lotus-blossom-espionage-group/)
- [Malik, M. (2019, June 20). LoudMiner: Cross-platform mining in cracked VST software. Retrieved May 18, 2020.](https://www.welivesecurity.com/2019/06/20/loudminer-mining-cracked-vst-software/)
- [Hsu, K. et al. (2020, June 24). Lucifer: New Cryptojacking and DDoS Hybrid Malware Exploiting High and Critical Vulnerabilities to Infect Windows Devices. Retrieved November 16, 2020.](https://unit42.paloaltonetworks.com/lucifer-new-cryptojacking-and-ddos-hybrid-malware/)
- [Jurčacko, F. (2024, May 15). To the Moon and back(doors): Lunar landing in diplomatic missions. Retrieved June 26, 2024.](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
- [ESET. (2019, July). MACHETE JUST GOT SHARPER Venezuelan government institutions under attack. Retrieved September 13, 2019.](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
- [kate. (2020, September 25). APT-C-43 steals Venezuelan military secrets to provide intelligence support for the reactionaries — HpReact campaign. Retrieved November 20, 2020.](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)
- [M.Léveillé, M., Cherepanov, A.. (2022, January 25). Watering hole deploys new macOS malware, DazzleSpy, in Asia. Retrieved May 6, 2022.](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
- [Ehrlich, A., et al. (2022, September). THE MYSTERY OF METADOR | AN UNATTRIBUTED THREAT HIDING IN TELCOS, ISPS, AND UNIVERSITIES. Retrieved January 23, 2023.](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
- [Lee, B. and Falcone, R. (2017, February 15). Magic Hound Campaign Attacks Saudi Targets. Retrieved December 27, 2017.](https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/)
- [DFIR Report. (2022, March 21). APT35 Automates Initial Access Using ProxyShell. Retrieved May 25, 2022.](https://thedfirreport.com/2022/03/21/apt35-automates-initial-access-using-proxyshell)
- [DFIR Report. (2021, November 15). Exchange Exploit Leads to Domain Wide Ransomware. Retrieved January 5, 2023.](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/)
- [Asheer Malhotra, Vitor Ventura & Jungsoo An, Cisco Talos. (2022, September 7). MagicRAT: Lazarus’ latest gateway into victim networks. Retrieved December 30, 2024.](https://blog.talosintelligence.com/lazarus-magicrat/)
- [Asheer Malhotra & Vitor Ventura. (2022, August 2). Manjusaka: A Chinese sibling of Sliver and Cobalt Strike. Retrieved September 4, 2024.](https://blog.talosintelligence.com/manjusaka-offensive-framework/)
- [Cybersecurity and Infrastructure Security Agency. (2025, March 12). AA25-071A #StopRansomware: Medusa Ransomware. Retrieved October 15, 2025.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a)
- [PwC and BAE Systems. (2017, April). Operation Cloud Hopper: Technical Annex. Retrieved April 13, 2017.](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
- [ClearSky Cyber Security . (2021, August). New Iranian Espionage Campaign By “Siamesekitten” - Lyceum. Retrieved June 6, 2022.](https://www.clearskysec.com/siamesekitten/)
- [Tomonaga, S. (2024, July 16). MirrorFace Attack against Japanese Organisations. Retrieved April 17, 2026.](https://blogs.jpcert.or.jp/en/2024/07/mirrorface-attack-against-japanese-organisations.html)
- [Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
- [Microsoft Threat Intelligence. (2024, May 28). Moonstone Sleet emerges as new North Korean threat actor with new bag of tricks. Retrieved August 26, 2024.](https://www.microsoft.com/en-us/security/blog/2024/05/28/moonstone-sleet-emerges-as-new-north-korean-threat-actor-with-new-bag-of-tricks/)
- [Miller-Osborn, J. and Grunzweig, J.. (2017, March 30). Trochilus and New MoonWind RATs Used In Attack Against Thai Organizations. Retrieved March 30, 2017.](http://researchcenter.paloaltonetworks.com/2017/03/unit42-trochilus-rat-new-moonwind-rat-used-attack-thai-utility-organizations/)
- [Svajcer, V. (2018, July 31). Multiple Cobalt Personality Disorder. Retrieved September 5, 2018.](https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html)
- [Checkpoint Research. (2021, November 15). Uncovering MosesStaff techniques: Ideology over Money. Retrieved August 11, 2022.](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
- [ESET, et al. (2018, January). Diplomats in Eastern Europe bitten by a Turla mosquito. Retrieved July 3, 2018.](https://www.welivesecurity.com/wp-content/uploads/2018/01/ESET_Turla_Mosquito.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 10). MuddyWater expands operations. Retrieved November 2, 2018.](https://securelist.com/muddywater/88059/)
- [Hamzeloofard, S. (2020, January 31). New wave of PlugX targets Hong Kong | Avira Blog. Retrieved April 13, 2021.](https://www.avira.com/en/blog/new-wave-of-plugx-targets-hong-kong)
- [Tom Fakterman. (2024, September 6). Chinese APT Abuses VSCode to Target Government in Asia. Retrieved March 24, 2025.](https://unit42.paloaltonetworks.com/stately-taurus-abuses-vscode-southeast-asian-espionage/)
- [Neville, A. (2012, June 15). Trojan.Naid. Retrieved February 22, 2018.](https://www.symantec.com/security_response/writeup.jsp?docid=2012-061518-4639-99)
- [Baumgartner, K., Golovkin, M.. (2015, May). The MsnMM Campaigns: The Earliest Naikon APT Campaigns. Retrieved April 10, 2019.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf)
- [Axel F, Pierre T. (2017, October 16). Leviathan: Espionage actor spearphishes maritime and defense targets. Retrieved February 15, 2018.](https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets)
- [The DigiTrust Group. (2017, January 01). NanoCore Is Not Your Average RAT. Retrieved November 9, 2018.](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
- [Bezroutchko, A. (2019, November 19). NBTscan man page. Retrieved March 17, 2021.](https://manpages.debian.org/testing/nbtscan/nbtscan.1.en.html)
- [SecTools. (2003, June 11). NBTscan. Retrieved March 17, 2021.](https://sectools.org/tool/nbtscan/)
- [Lambert, T. (2020, January 29). Intro to Netwire. Retrieved January 7, 2021.](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
- [Proofpoint. (2020, December 2). Geofenced NetWire Campaigns. Retrieved January 7, 2021.](https://www.proofpoint.com/us/blog/threat-insight/geofenced-netwire-campaigns)
- [Robert Falcone, Jeff White, and Peter Renals. (2021, November 7). Targeted Attack Campaign Against ManageEngine ADSelfService Plus Delivers Godzilla Webshells, NGLite Trojan and KdcSponge Stealer. Retrieved February 8, 2024.](https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/)
- [Ahn Ho, Facundo Muñoz, & Marc-Etienne M.Léveillé. (2024, March 7). Evasive Panda leverages Monlam Festival to target Tibetans. Retrieved July 25, 2024.](https://www.welivesecurity.com/en/eset-research/evasive-panda-leverages-monlam-festival-target-tibetans/)
- [Dedola, G. (2022, June 21). APT ToddyCat. Retrieved January 3, 2024.](https://securelist.com/toddycat/106799/)
- [ss64. (n.d.). NLTEST.exe - Network Location Test. Retrieved February 14, 2019.](https://ss64.com/nt/nltest.html)
- [Grunzweig, J., Lee, B. (2018, September 27). New KONNI Malware attacking Eurasia and Southeast Asia. Retrieved November 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-new-konni-malware-attacking-eurasia-southeast-asia/)
- [Sherstobitoff, R., Malhotra, A. (2018, October 18). ‘Operation Oceansalt’ Attacks South Korea, U.S., and Canada With Source Code From Chinese Hacker Group. Retrieved November 30, 2018.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-oceansalt.pdf)
- [Kaspersky Lab's Global Research & Analysis Team. (2018, October 15). Octopus-infested seas of Central Asia. Retrieved November 14, 2018.](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
- [Falcone, R. and Lee, B.. (2016, May 26). The OilRig Campaign: Attacks on Saudi Arabian Organizations Deliver Helminth Backdoor. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/)
- [Grunzweig, J. and Falcone, R.. (2016, October 4). OilRig Malware Campaign Updates Toolset and Expands Targets. Retrieved May 3, 2017.](http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/)
- [Hromcova, Z. (2019, July). OKRUM AND KETRICAN: AN OVERVIEW OF RECENT KE3CHANG GROUP ACTIVITY. Retrieved May 6, 2020.](https://www.welivesecurity.com/wp-content/uploads/2019/07/ESET_Okrum_and_Ketrican.pdf)
- [Mercer, W. and Rascagneres, P. (2018, February 12). Olympic Destroyer Takes Aim At Winter Olympics. Retrieved March 14, 2019.](https://blog.talosintelligence.com/2018/02/olympic-destroyer.html)
- [Hiroaki, H. (2024, November 26). Guess Who’s Back - The Return of ANEL in the Recent Earth Kasha Spear-phishing Campaign in 2024. Retrieved April 17, 2026.](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
- [Cybereason Nocturnus. (2022, May 4). Operation CuckooBees: Deep-Dive into Stealthy Winnti Techniques. Retrieved September 22, 2022.](https://www.cybereason.com/blog/operation-cuckoobees-deep-dive-into-stealthy-winnti-techniques)
- [Dantzig, M. v., Schamper, E. (2019, December 19). Operation Wocao: Shining a light on one of China’s hidden hacking groups. Retrieved October 8, 2020.](https://www.fox-it.com/media/kadlze5c/201912_report_operation_wocao.pdf)
- [Horejsi, J. (2018, April 04). New MacOS Backdoor Linked to OceanLotus Found. Retrieved November 13, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/new-macos-backdoor-linked-to-oceanlotus-found/)
- [Magisa, L. (2020, November 27). New MacOS Backdoor Connected to OceanLotus Surfaces. Retrieved December 2, 2020.](https://www.trendmicro.com/en_us/research/20/k/new-macos-backdoor-connected-to-oceanlotus-surfaces.html)
- [Check Point. (2020, November 6). Ransomware Alert: Pay2Key. Retrieved January 4, 2021.](https://research.checkpoint.com/2020/ransomware-alert-pay2key/)
- [Leonardo. (2020, May 29). MALWARE TECHNICAL INSIGHT TURLA “Penquin_x64”. Retrieved March 11, 2021.](https://www.leonardo.com/documents/20142/10868623/Malware+Technical+Insight+_Turla+%E2%80%9CPenquin_x64%E2%80%9D.pdf)
- [Brett Stone-Gross & Nikolaos Pantazopoulos. (2023, May 24). Technical Analysis of Pikabot. Retrieved July 12, 2024.](https://www.zscaler.com/blogs/security-research/technical-analysis-pikabot)
- [Unit 42. (2022, June 13). GALLIUM Expands Targeting Across Telecommunications, Government and Finance Sectors With New PingPull Tool. Retrieved August 7, 2022.](https://unit42.paloaltonetworks.com/pingpull-gallium/)
- [Tartare, M. et al. (2020, May 21). No “Game over” for the Winnti Group. Retrieved August 24, 2020.](https://www.welivesecurity.com/2020/05/21/no-game-over-winnti-group/)
- [Grunzweig, J., et al. (2016, May 24). New Wekby Attacks Use DNS Requests As Command and Control Mechanism. Retrieved August 17, 2016.](http://researchcenter.paloaltonetworks.com/2016/05/unit42-new-wekby-attacks-use-dns-requests-as-command-and-control-mechanism/)
- [Ash, B., et al. (2018, June 26). RANCOR: Targeted Attacks in South East Asia Using PLAINTEE and DDKONG Malware Families. Retrieved July 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/)
- [CISA. (2023, December 18). #StopRansomware: Play Ransomware AA23-352A. Retrieved September 24, 2024.](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-352a)
- [Alexandre Cote Cyr. (2022, March 23). Mustang Panda’s Hodur: Old tricks, new Korplug variant. Retrieved September 9, 2025.](https://www.welivesecurity.com/2022/03/23/mustang-panda-hodur-old-tricks-new-korplug-variant/)
- [DOJ. (2024, December 20). Mag. No. 24-mj-1387 AFFIDAVIT IN SUPPORT OF AN APPLICATION FOR A NINTH SEARCH AND SEIZURE WARRANT- IN THE MATTER OF THE SEARCH AND SEIZURE OF COMPUTERS IN THE UNITED STATES INFECTED WITH PLUGX MALWARE . Retrieved September 9, 2025.](https://www.justice.gov/archives/opa/media/1384136/dl)
- [Nettitude. (2018, July 23). Python Server for PoshC2. Retrieved April 23, 2019.](https://github.com/nettitude/PoshC2_Python)
- [Adair, S.. (2016, November 9). PowerDuke: Widespread Post-Election Spear Phishing Campaigns Targeting Think Tanks and NGOs. Retrieved January 11, 2017.](https://www.volexity.com/blog/2016/11/09/powerduke-post-election-spear-phishing-campaigns-targeting-think-tanks-and-ngos/)
- [GReAT. (2019, August 12). Recent Cloud Atlas activity. Retrieved May 8, 2020.](https://securelist.com/recent-cloud-atlas-activity/92016/)
- [Singh, S. et al.. (2018, March 13). Iranian Threat Group Updates Tactics, Techniques and Procedures in Spear Phishing Campaign. Retrieved April 11, 2018.](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
- [Lunghi, D. and Horejsi, J.. (2019, June 10). MuddyWater Resurfaces, Uses Multi-Stage Backdoor POWERSTATS V3 and New Post-Exploitation Tools. Retrieved May 14, 2020.](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
- [Sardiwal, M, et al. (2017, December 7). New Targeted Attack in the Middle East by APT34, a Suspected Iranian Threat Group, Using CVE-2017-11882 Exploit. Retrieved December 20, 2017.](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
- [Cherepanov, A.. (2016, May 17). Operation Groundbait: Analysis of a surveillance toolkit. Retrieved May 18, 2016.](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
- [Sherstobitoff, R., Malhotra, A. (2018, April 24). Analyzing Operation GhostSecret: Attack Seeks to Steal Data Worldwide. Retrieved May 16, 2018.](https://securingtomorrow.mcafee.com/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/)
- [Lenart Bermejo, Sunny Lu, Ted Lee. (2024, September 9). Earth Preta Evolves its Attacks with New Malware and Strategies. Retrieved August 4, 2025.](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
- [Nicolas Verdier. (n.d.). Retrieved January 29, 2018.](https://github.com/n1nj4sec/pupy)
- [CERT-FR. (2020, April 1). ATTACKS INVOLVING THE MESPINOZA/PYSA RANSOMWARE. Retrieved March 1, 2021.](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2020-CTI-003.pdf)
- [CS. (2020, October 7). Duck Hunting with Falcon Complete: A Fowl Banking Trojan Evolves, Part 2. Retrieved September 27, 2021.](https://www.crowdstrike.com/blog/duck-hunting-with-falcon-complete-qakbot-zip-based-campaign/)
- [Kuzmenko, A. et al. (2021, September 2). QakBot technical analysis. Retrieved September 27, 2021.](https://securelist.com/qakbot-technical-analysis/103931/)
- [Group IB. (2020, September). LOCK LIKE A PRO. Retrieved November 17, 2024.](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
- [Kenefick, I. et al. (2022, October 12). Black Basta Ransomware Gang Infiltrates Networks via QAKBOT, Brute Ratel, and Cobalt Strike. Retrieved February 6, 2023.](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html)
- [Microsoft. (2022, May 9). Ransomware as a service: Understanding the cybercrime gig economy and how to protect yourself. Retrieved March 10, 2023.](https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/)
- [Magdy, S. et al. (2022, August 25). New Golang Ransomware Agenda Customizes Attacks. Retrieved September 26, 2025.](https://www.trendmicro.com/en_us/research/22/h/new-golang-ransomware-agenda-customizes-attacks.html)
- [Lee, B., Falcone, R. (2018, July 25). OilRig Targets Technology Service Provider and Government Agency with QUADAGENT. Retrieved August 9, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-oilrig-targets-technology-service-provider-government-agency-quadagent/)
- [CISA. (2018, December 18). Analysis Report (AR18-352A) Quasar Open-Source Remote Administration Tool. Retrieved August 1, 2022.](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
- [Antiy CERT. (2020, April 20). Analysis of Ramsay components of Darkhotel's infiltration and isolation network. Retrieved March 24, 2021.](https://www.programmersought.com/article/62493896999/)
- [Lei, C., et al. (2018, January 24). Lazarus Campaign Targeting Cryptocurrencies Reveals Remote Controller Tool, an Evolved RATANKBA, and More. Retrieved May 22, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/lazarus-campaign-targeting-cryptocurrencies-reveals-remote-controller-tool-evolved-ratankba/)
- [Trend Micro. (2017, February 27). RATANKBA: Delving into Large-scale Watering Holes against Enterprises. Retrieved May 22, 2018.](https://www.trendmicro.com/en_us/research/17/b/ratankba-watering-holes-against-enterprises.html)
- [Grunzweig, J. and Miller-Osborn, J. (2017, November 10). New Malware with Ties to SunOrcal Discovered. Retrieved November 16, 2017.](https://researchcenter.paloaltonetworks.com/2017/11/unit42-new-malware-with-ties-to-sunorcal-discovered/)
- [George Glass. (2024, August 14). REDLINESTEALER Malware Driving the Initial Access Broker Market. Retrieved September 17, 2025.](https://www.kroll.com/en/publications/cyber/redlinestealer-malware)
- [Lamparski, L. et al. (2025, March 11). Ghost in the Router: China-Nexus Espionage Actor UNC3886 Targets Juniper Routers. Retrieved June 24, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-targets-juniper-routers)
- [Juniper Networks, Cybersecurity R&D. (2025, March 11). The RedPenguin Malware Incident. Retrieved June 24, 2025.](https://supportportal.juniper.net/sfc/servlet.shepherd/document/download/069Dp00000FzdmIIAR?operationContext=S1)
- [Kaspersky Lab's Global Research & Analysis Team. (2016, August 9). The ProjectSauron APT. Technical Analysis. Retrieved August 17, 2016.](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
- [Livelli, K, et al. (2018, November 12). Operation Shaheen. Retrieved May 1, 2019.](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
- [Knight, S.. (2020, April 16). VMware Carbon Black TAU Threat Analysis: The Evolution of Lazarus. Retrieved May 1, 2020.](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
- [Sherstobitoff, R., Malhotra, A., et. al.. (2018, December 18). Operation Sharpshooter Campaign Targets Global Defense, Critical Infrastructure. Retrieved May 14, 2020.](https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf)
- [Falcone, R., et al. (2018, July 27). New Threat Actor Group DarkHydrus Targets Middle East Government. Retrieved August 2, 2018.](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
- [Cybereason Global SOC and Cybereason Security Research Teams. (2022, December 14). Royal Rumble: Analysis of Royal Ransomware. Retrieved March 30, 2023.](https://www.cybereason.com/blog/royal-ransomware-analysis)
- [Hanel, A. (2019, January 10). Big Game Hunting with Ryuk: Another Lucrative Targeted Ransomware. Retrieved May 12, 2020.](https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/)
- [Abrams, L. (2021, January 14). Ryuk Ransomware Uses Wake-on-Lan To Encrypt Offline Devices. Retrieved February 11, 2021.](https://www.bleepingcomputer.com/news/security/ryuk-ransomware-uses-wake-on-lan-to-encrypt-offline-devices/)
- [Hasherezade. (2021, April 6). A deep dive into Saint Bot, a new downloader. Retrieved June 9, 2022.](https://blog.malwarebytes.com/threat-intelligence/2021/04/a-deep-dive-into-saint-bot-downloader/)
- [Budaca, E., et al. (2021, August 25). FIN8 Threat Actor Goes Agile with New Sardonic Backdoor. Retrieved August 9, 2023.](https://www.bitdefender.com/files/News/CaseStudies/study/401/Bitdefender-PR-Whitepaper-FIN8-creat5619-en-EN.pdf)
- [Mandiant Incident Response. (2025, May 6). Defending Against UNC3944: Cybercrime Hardening Guidance from the Frontlines. Retrieved October 13, 2025.](https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations)
- [Schwarz, D. et al. (2019, October 16). TA505 Distributes New SDBbot Remote Access Trojan with Get2 Downloader. Retrieved May 29, 2020.](https://www.proofpoint.com/us/threat-insight/post/ta505-distributes-new-sdbbot-remote-access-trojan-get2-downloader)
- [Kaspersky Lab. (2017, August). ShadowPad: popular server management software hit in supply chain attack. Retrieved March 22, 2021.](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2017/08/07172148/ShadowPad_technical_description_PDF.pdf)
- [Lumelsly, A. et al. (2024, March 26). ShadowRay: First Known Attack Campaign Targeting AI Workloads Actively Exploited In The Wild. Retrieved December 2, 2024.](https://www.oligo.security/blog/shadowray-attack-ai-workloads-actively-exploited-in-the-wild)
- [Falcone, R.. (2016, November 30). Shamoon 2: Return of the Disttrack Wiper. Retrieved January 11, 2017.](http://researchcenter.paloaltonetworks.com/2016/11/unit42-shamoon-2-return-disttrack-wiper/)
- [Mundo, A., Roccia, T., Saavedra-Morales, J., Beek, C.. (2018, December 14). Shamoon Returns to Wipe Systems in Middle East, Europe . Retrieved May 29, 2020.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/shamoon-returns-to-wipe-systems-in-middle-east-europe/)
- [Yonathan Klijnsma. (2016, May 17). Mofang: A politically motivated information stealing adversary. Retrieved May 12, 2020.](https://foxitsecurity.files.wordpress.com/2016/06/fox-it_mofang_threatreport_tlp-white.pdf)
- [Cristian Souza, Eduardo Ovalle, Ashley Muñoz, & Christopher Zachor. (2024, May 23). ShrinkLocker: Turning BitLocker into ransomware. Retrieved December 7, 2024.](https://securelist.com/ransomware-abuses-bitlocker/112643/)
- [Check Point. (2021, April 8). Iran’s APT34 Returns with an Updated Arsenal. Retrieved May 5, 2021.](https://research.checkpoint.com/2021/irans-apt34-returns-with-an-updated-arsenal/)
- [Hegel, T. (2021, January 13). A Global Perspective of the SideWinder APT. Retrieved January 27, 2021.](https://cdn-cybersecurity.att.com/docs/global-perspective-of-the-sidewinder-apt.pdf)
- [BishopFox. (n.d.). Sliver Ifconfig. Retrieved September 16, 2021.](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/network/ifconfig.go)
- [NCSC GCHQ. (2022, January 27). Small Sieve Malware Analysis Report. Retrieved August 22, 2022.](https://www.ncsc.gov.uk/files/NCSC-Malware-Analysis-Report-Small-Sieve.pdf)
- [Andrew Northern. (2022, November 22). SocGholish, a very real threat from a very fake update. Retrieved February 13, 2024.](https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update)
- [Red Canary. (2024, March). Red Canary 2024 Threat Detection Report: SocGholish. Retrieved March 22, 2024.](https://redcanary.com/threat-detection-report/threats/socgholish/)
- [Secureworks. (n.d.). GOLD PRELUDE . Retrieved March 22, 2024.](https://www.secureworks.com/research/threat-profiles/gold-prelude)
- [CISA. (2020, July 16). MAR-10296782-1.v1 – SOREFANG. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198a)
- [Check Point Research. (2019, February 4). SpeakUp: A New Undetected Backdoor Linux Trojan. Retrieved April 17, 2019.](https://research.checkpoint.com/speakup-a-new-undetected-backdoor-linux-trojan/)
- [CTU. (2018, September 27). Cybercriminals Increasingly Trying to Ensnare the Big Financial Fish. Retrieved September 20, 2021.](https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish)
- [Kumar, A., Stone-Gross, Brett. (2021, September 28). Squirrelwaffle: New Loader Delivering Cobalt Strike. Retrieved August 9, 2022.](https://www.zscaler.com/blogs/security-research/squirrelwaffle-new-loader-delivering-cobalt-strike)
- [FBI, CISA, CNMF, NCSC-UK. (2022, February 24). Iranian Government-Sponsored Actors Conduct Cyber Operations Against Global Government and Commercial Networks. Retrieved September 27, 2022.](https://www.cisa.gov/uscert/ncas/alerts/aa22-055a)
- [Marczak, B. and Scott-Railton, J.. (2016, May 29). Keep Calm and (Don’t) Enable Macros: A New Threat Actor Targets UAE Dissidents. Retrieved June 8, 2016.](https://citizenlab.org/2016/05/stealth-falcon/)
- [Mercer, W. et al. (2020, June 29). PROMETHIUM extends global reach with StrongPity3 APT. Retrieved July 20, 2020.](https://blog.talosintelligence.com/2020/06/promethium-extends-with-strongpity3.html)
- [Nicolas Falliere, Liam O Murchu, Eric Chien 2011, February W32.Stuxnet Dossier (Version 1.4) Retrieved November 17, 2024.](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
- [FireEye. (2020, December 13). Highly Evasive Attacker Leverages SolarWinds Supply Chain to Compromise Multiple Global Victims With SUNBURST Backdoor. Retrieved January 4, 2021.](https://www.fireeye.com/blog/threat-research/2020/12/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor.html)
- [Blasco, J. (2011, December 12). Another Sykipot sample likely targeting US federal agencies. Retrieved March 28, 2016.](https://www.alienvault.com/open-threat-exchange/blog/another-sykipot-sample-likely-targeting-us-federal-agencies)
- [Daniel Lunghi. (2023, March 1). Iron Tiger’s SysUpdate Reappears, Adds Linux Targeting. Retrieved March 20, 2023.](https://www.trendmicro.com/en_us/research/23/c/iron-tiger-sysupdate-adds-linux-targeting.html)
- [Grunzweig, J. and Miller-Osborn, J.. (2016, February 4). T9000: Advanced Modular Backdoor Uses Complex Anti-Analysis Techniques. Retrieved April 15, 2016.](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
- [Trend Micro. (2012). The Taidoor Campaign. Retrieved November 12, 2014.](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_the_taidoor_campaign.pdf)
- [CISA, FBI, DOD. (2021, August). MAR-10292089-1.v2 – Chinese Remote Access Trojan: TAIDOOR. Retrieved August 24, 2021.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-216a)
- [GReAT. (2019, April 10). Project TajMahal – a sophisticated new APT framework. Retrieved October 14, 2019.](https://securelist.com/project-tajmahal/90240/)
- [Fiser, D. Oliveira, A. (n.d.). Tracking the Activities of TeamTNT A Closer Look at a Cloud-Focused Malicious Actor Group. Retrieved September 22, 2021.](https://documents.trendmicro.com/assets/white_papers/wp-tracking-the-activities-of-teamTNT.pdf)
- [Dell SecureWorks Counter Threat Unit Threat Intelligence. (2015, August 5). Threat Group-3390 Targets Organizations for Cyberespionage. Retrieved August 18, 2018.](https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage)
- [Beek, C. (2020, November 5). Operation North Star: Behind The Scenes. Retrieved December 20, 2021.](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/operation-north-star-behind-the-scenes/)
- [Salinas, M., Holguin, J. (2017, June). Evolution of Trickbot. Retrieved July 31, 2018.](https://www.securityartwork.es/wp-content/uploads/2017/07/Trickbot-report-S2-Grupo.pdf)
- [Anthony, N., Pascual, C.. (2018, November 1). Trickbot Shows Off New Trick: Password Grabber Module. Retrieved November 16, 2018.](https://blog.trendmicro.com/trendlabs-security-intelligence/trickbot-shows-off-new-trick-password-grabber-module/)
- [Secureworks. (2019, July 24). Updated Karagany Malware Targets Energy Sector. Retrieved August 12, 2020.](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
- [Jiho Kim & Sebin Lee, S2W. (2024, February 7). Kimsuky disguised as a Korean company signed with a valid certificate to distribute Troll Stealer (English ver.). Retrieved January 17, 2025.](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
- [Chen, J.. (2020, May 12). Tropic Trooper’s Back: USBferry Attack Targets Air gapped Environments. Retrieved May 20, 2020.](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
- [Tomonaga, S. (2018, March 6). Malware “TSCookie”. Retrieved May 6, 2020.](https://blogs.jpcert.or.jp/en/2018/03/malware-tscooki-7aa0.html)
- [Adam Burgher. (2021, June 10). BackdoorDiplomacy: Upgrading from Quarian to Turian. Retrieved September 1, 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
- [Symantec DeepSight Adversary Intelligence Team. (2019, June 20). Waterbug: Espionage Group Rolls Out Brand-New Toolset in Attacks Against Governments. Retrieved July 8, 2019.](https://www.symantec.com/blogs/threat-intelligence/waterbug-espionage-governments)
- [Faou, M. (2020, May). From Agent.btz to ComRAT v4: A ten-year journey. Retrieved June 15, 2020.](https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf)
- [Faou, M. and Dumont R.. (2019, May 29). A dive into Turla PowerShell usage. Retrieved June 14, 2019.](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/)
- [Settle, A., et al. (2016, August 8). MONSOON - Analysis Of An APT Campaign. Retrieved September 22, 2016.](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
- [Matsuda, A., Muhammad I. (2018, September 13). APT10 Targeting Japanese Corporations Using Updated TTPs. Retrieved September 17, 2018.](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
- [Salem, E. et al. (2020, May 28). VALAK: MORE THAN MEETS THE EYE . Retrieved June 19, 2020.](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
- [Lancaster, T., Cortes, J. (2018, January 29). VERMIN: Quasar RAT and Custom Malware Used In Ukraine. Retrieved July 5, 2018.](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
- [Yagi, J. (2014, August 24). Trojan.Volgmer. Retrieved July 16, 2018.](https://web.archive.org/web/20181126143456/https://www.symantec.com/security-center/writeup/2014-081811-3237-99?tabid=2)
- [NSA et al. (2023, May 24). People's Republic of China State-Sponsored Cyber Actor Living off the Land to Evade Detection. Retrieved July 27, 2023.](https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF)
- [Counter Threat Unit Research Team. (2017, May 18). WCry Ransomware Analysis. Retrieved March 26, 2019.](https://www.secureworks.com/research/wcry-ransomware-analysis)
- [CISA. (2020, July 16). MAR-10296782-3.v1 – WELLMAIL. Retrieved September 29, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198c)
- [PWC. (2020, July 16). How WellMess malware has been used to target COVID-19 vaccines. Retrieved September 24, 2020.](https://www.pwc.co.uk/issues/cyber-security-services/insights/cleaning-up-after-wellmess.html)
- [CISA. (2020, July 16). MAR-10296782-2.v1 – WELLMESS. Retrieved September 24, 2020.](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-198b)
- [Sean Gallagher, Peter Mackenzie, Elida Leite, Syed Shahram, Bill Kearney, Anand Aijan, Sivagnanam Gn, Suraj Mundalik. (2020, October 14). They’re back: inside a new Ryuk ransomware attack. Retrieved October 14, 2020.](https://news.sophos.com/en-us/2020/10/14/inside-a-new-ryuk-ransomware-attack/)
- [Shilko, J., et al. (2021, October 7). FIN12: The Prolific Ransomware Intrusion Threat Actor That Has Aggressively Pursued Healthcare Targets. Retrieved June 15, 2023.](https://web.archive.org/web/20220313061955/https://www.mandiant.com/sites/default/files/2021-10/fin12-group-profile.pdf)
- [MalwareBytes Threat Intelligence Team. (2022, August 3). Woody RAT: A new feature-rich malware spotted in the wild. Retrieved December 6, 2022.](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
- [Xiao, C. (2018, September 17). Xbash Combines Botnet, Ransomware, Coinmining in Worm that Targets Linux and Windows. Retrieved November 14, 2018.](https://researchcenter.paloaltonetworks.com/2018/09/unit42-xbash-combines-botnet-ransomware-coinmining-worm-targets-linux-windows/)
- [Kirill Boychenko. (2025, July 14). Contagious Interview Campaign Escalates With 67 Malicious npm Packages and New Malware Loader. Retrieved October 19, 2025.](https://socket.dev/blog/contagious-interview-campaign-escalates-67-malicious-npm-packages)
- [Schwarz, D., Sopko J. (2018, March 08). Donot Team Leverages New Modular Malware Framework in South Asia. Retrieved June 11, 2018.](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
- [ESET Research. (2019, May 22). A journey to Zebrocy land. Retrieved June 20, 2019.](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
- [Huss, D., et al. (2017, February 2). Oops, they did it again: APT Targets Russia and Belarus with ZeroT and PlugX. Retrieved April 5, 2018.](https://www.proofpoint.com/us/threat-insight/post/APT-targets-russia-belarus-zerot-plugx)
- [Singh, S. and Antil, S. (2020, October 27). APT-31 Leverages COVID-19 Vaccine Theme and Abuses Legitimate Online Services. Retrieved March 24, 2021.](https://www.zscaler.com/blogs/security-research/apt-31-leverages-covid-19-vaccine-theme-and-abuses-legitimate-online)
- [McAfee® Foundstone® Professional Services and McAfee Labs™. (2011, February 10). Global Energy Cyberattacks: “Night Dragon”. Retrieved February 19, 2018.](https://scadahacker.com/library/Documents/Cyber_Events/McAfee%20-%20Night%20Dragon%20-%20Global%20Energy%20Cyberattacks.pdf)

---

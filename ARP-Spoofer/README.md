# ARP Spoof Attack Script using Scapy

**Author:** Abdelrahman Adel
**Date:** 2021
**License:** [MIT License](LICENSE)

## Description

This Python script utilizes Scapy to perform an ARP (Address Resolution Protocol) spoofing attack. The script manipulates ARP packets to deceive target devices and their corresponding routers into thinking that the attacker's machine is the router. This allows the attacker to intercept and potentially manipulate network traffic between the target and the router.

## How ARP Spoofing Works

1. The script sends ARP response packets to the target with the router's IP address, associating the router's IP with the attacker's MAC address.
2. Similarly, ARP response packets are sent to the router with the target's IP address, associating the target's IP with the attacker's MAC address.
3. As a result, both the target and the router believe that the attacker's machine is the other party in the communication.

## Usage

1. Ensure you have Python 3.11 or later installed on your system.
2. Run the script with the following command, specifying the interface and target IP address:

python3.11 arp_spoof.py -I <INTERFACE> -T <TARGET_IP>

Replace `<INTERFACE>` with the name of your attacker interface and `<TARGET_IP>` with the IP address of the target device.

3. The script will perform ARP spoofing, intercepting network traffic between the target and the router. Use this responsibly and only on networks and devices for which you have permission.

## Forwarding Packets

To enable packet forwarding on your system, execute the following commands:

- For the current session:
  echo 1 > /proc/sys/net/ipv4/ip_forward
  
- To persist the change, add or uncomment the following line in `/etc/sysctl.conf`:
  net.ipv4.ip_forward = 1

- Apply the changes:
  sysctl -p /etc/sysctl.conf

## Dependencies

- Python 3.11 or later.
- The `scapy` library is used for crafting and sending ARP packets. You can install it using `pip`:
  pip install scapy

- The `psutil` library is used for retrieving network interface information. You can install it using `pip`:
  pip install psutil


## License

This script is provided under the terms of the MIT license. Feel free to modify and distribute it as needed.

## Disclaimer

Use this script responsibly and only on networks and devices for which you have permission. Unauthorized network scanning and attacks may violate privacy and legal regulations.






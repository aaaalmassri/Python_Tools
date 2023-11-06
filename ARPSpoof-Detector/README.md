# ARP Spoofing Attack Detector Script

**Author:** Abdelrahman Adel
**Date:** 2021
**License:** [MIT License](LICENSE)

## Description

This Python script functions as an ARP (Address Resolution Protocol) spoofing attack detector. It captures network packets and checks for ARP response packets to identify potential ARP spoofing attacks. When a suspicious ARP reply is detected, the script reports the attack and identifies the source.

## Features

- Monitors network traffic for ARP packets.
- Identifies ARP response packets (op=2) with the source IP address equal to the router's IP address.
- Detects potential ARP spoofing attacks.
- Reports the attacker's MAC address when an attack is detected.

## Usage

1. Ensure you have Python 3.11 or later installed on your system.
2. Run the script with the following command, specifying the network interface to monitor:
   python3.11 arp_spoof_detector.py -I <INTERFACE_NAME>

Replace `<INTERFACE_NAME>` with the name of the network interface you want to monitor.

3. The script will monitor network traffic and report potential ARP spoofing attacks if detected.

## Dependencies

- Python 3.11 or later.
- The `scapy` library is used for packet capture and analysis. You can install it using `pip`:
  pip install scapy OR python3 -m pip install scapy

- The `colorama` library is used for colored output. You can install it using `pip`:
  pip install colorama OR pip3 install colorama


- The script may require superuser privileges to capture network packets.

## License

This script is provided under the terms of the MIT license. Feel free to modify and distribute it as needed.

## Disclaimer

Use this script responsibly and only on networks for which you have permission to monitor. Detecting and responding to ARP spoofing attacks without proper authorization may violate privacy and legal regulations.



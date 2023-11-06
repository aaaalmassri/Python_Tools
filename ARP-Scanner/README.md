# Simple Network Scanner Using ARP Protocol Logic

**Author:** Abdelrahman Adel
**Date:** 2021
**License:** [MIT License](LICENSE)

## Description

This Python script serves as a simple network scanner using ARP (Address Resolution Protocol) to send ARP requests to network devices and receive ARP responses. It's designed to identify devices on your local network and display their IP and MAC addresses.

## Features

- Send ARP requests to network devices.
- Receive and display ARP responses.
- Set the destination MAC address as the broadcast MAC "FF:FF:FF:FF:FF:FF".

## Usage

1. Ensure you have Python 3.11 or later installed on your system.
   
3. Run the script with the following command:
   
4. You will be prompted to enter the target IP address. Provide the IP address of the device you want to scan.

5. Next, you'll be asked to specify the network interface to use for the scan.

6. The script will then send ARP requests to the specified target and display the IP and MAC addresses of the devices that respond.

## Dependencies

- Python 3.11 or later.
- The `scapy` library is used for crafting and sending ARP packets. You can install it using `pip`:
  pip install scapy OR python3 -m pip install scapy

  
## License

This script is provided under the terms of the MIT license. Feel free to modify and distribute it as needed.

## Disclaimer

Use this script responsibly and only on networks and devices for which you have permission. Unauthorized network scanning may violate privacy and legal regulations.

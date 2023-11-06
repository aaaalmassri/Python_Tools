# Network Packet Sniffer

**Author:** Abdelrahman Adel
**Date:** 2021
**License:** [MIT License](LICENSE)

## Description

This Python script serves as a network packet sniffer, capturing and analyzing network packets that pass through the specified network interface. It uses the Scapy library to intercept and dissect packets, providing insights into the contents of HTTP requests and important network information.

## Features

- Sniffs and processes network packets using the Scapy library.
- Captures and analyzes HTTP requests for web information, including URLs, request methods, headers, and more.
- Identifies potential login information based on keywords in intercepted data.
- Displays source and destination IP addresses, MAC addresses, and port information.
- Provides data offset, sequence numbers, and acknowledgment details for captured packets.

## Usage

1. Ensure you have Python 3.11 or later installed on your system.

2. Run the script with the following command, specifying the network interface you want to capture packets from:

python3.11 network_packet_sniffer.py


The script will prompt you to enter the name of the network interface.

3. The script will start capturing network packets passing through the specified interface and analyze them, providing detailed information about intercepted HTTP requests and network data.

## Dependencies

- Python 3.11 or later.
- The `scapy` library is used for packet interception and analysis. You can install it using `pip`:

pip install scapy OR python3 -m pip install scapy


## Captured Information

This script is designed for educational purposes and network analysis. It can provide insights into HTTP requests and network traffic. Use it responsibly and only on networks for which you have permission.

## License

This script is provided under the terms of the MIT license. Feel free to modify and distribute it as needed.

## Disclaimer

Use this script responsibly and only on networks for which you have authorization. Unauthorized interception and analysis of network packets may violate privacy and legal regulations.


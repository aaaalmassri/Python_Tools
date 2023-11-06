# DNS Spoof Script Using Scapy

**Author:** Your Name
**Date:** Date
**License:** [MIT License](LICENSE)

## Description

This Python script serves as a DNS spoofing tool using Scapy. It allows you to intercept DNS requests and responses in a Man-in-the-Middle (MITM) attack, modify them, and then resend the modified packets to the target.

## DNS Spoofing Logic

1. Intercept target packets using a MITM attack and store them in a network queue.
2. Access the intercepted packets in the queue and modify them as needed.
3. Resend the modified packets to the target, potentially redirecting DNS queries to a different IP address.

## Features

- Captures DNS packets sent to a specific domain, in this case, "vulnweb.com".
- Modifies DNS responses to spoof the target's DNS queries with a different IP address.
- Uses Scapy for packet manipulation and network interception.
- Can be used in a Man-in-the-Middle attack scenario.

## Usage

1. Ensure you have Python 3.11 or later installed on your system.

2. Run the script with the following command, specifying the network interface:

python3.11 dns_spoof.py


The script will prompt you for the network interface to use. Provide the name of the interface you want to capture traffic on.

3. The script will intercept DNS packets targeting the "vulnweb.com" domain and modify the responses.

## Dependencies

- Python 3.11 or later.
- The `scapy` library is used for packet manipulation and analysis. You can install it using `pip`:

pip install scapy OR python3 -m pip install scapy

- The `netfilterqueue` library is used to create a network queue for capturing and processing network packets. You can install it using `pip`:
pip install netfilterqueue OR python3 -m pip install netfilterqueue



## DNS Spoofing

This script is designed for educational and testing purposes. DNS spoofing is a technique that can be used for various purposes, including security research and understanding network vulnerabilities. Use it responsibly and only on networks and domains for which you have permission.

## License

This script is provided under the terms of the MIT license. Feel free to modify and distribute it as needed.

## Disclaimer

Use this script responsibly and only on networks and domains for which you have authorization. Unauthorized DNS spoofing may violate privacy and legal regulations.

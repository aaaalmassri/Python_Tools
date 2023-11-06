# File Intercept and Replace Script

**Author:** Abdelrahman Adel
**Date:** 2021
**License:** [MIT License](LICENSE)

## Description

This Python script intercepts network traffic using a Man-in-the-Middle (MITM) attack and replaces requested files with an attack script file. The script is designed for educational and testing purposes to understand the concepts of MITM attacks and file manipulation during data interception.

## Script Phases

1. Intercept Phase:
   - Starts a MITM attack to capture network traffic.
   - Stores intercepted target packets in a Netfilter Queue using IP Tables.

2. Modification Phase:
   - Replaces the load field, which contains the target's requested file's hexadecimal code, with a redirection link to an attack file URL.
   - Deletes fields used by the target computer to check request integrity, including IP TTL (Time To Live), IP checksum, and TCP checksum.

3. Redirecting Phase:
   - After modifying the request packet, the modified packet is redirected to the target using the `.accept()` function to avoid interrupting the connection.

## Features

- Captures and modifies HTTP packets in a MITM attack scenario.
- Replaces the requested file with an attack file URL in HTTP responses.
- Demonstrates the interception and manipulation of network traffic.
- Uses the `netfilterqueue` library to create a network queue for packet processing.

## Usage

1. Ensure you have Python 3.11 or later installed on your system.

2. Run the script with the following command, specifying the Netfilter Queue number:

python3.11 file_intercept_and_replace.py


The script will prompt you for the Netfilter Queue number to use.

3. The script will intercept network traffic and modify HTTP responses to redirect requested files to the specified attack file URL.

## Dependencies

- Python 3.11 or later.
- The `scapy` library is used for packet manipulation and analysis. You can install it using `pip`:

pip install scapy OR python3 -m pip install scapy


- The `netfilterqueue` library is used to create a network queue for capturing and processing network packets. You can install it using `pip`:

pip install netfilterqueue OR python3 -m pip install netfilterqueue


## Redirected Files

This script is designed for educational purposes and demonstration of network interception and manipulation techniques. You can customize the attack file URL and the intercepted files as needed.

## License

This script is provided under the terms of the MIT license. Feel free to modify and distribute it as needed.

## Disclaimer

Use this script responsibly and only on networks and files for which you have authorization. Unauthorized interception and manipulation of network traffic may violate privacy and legal regulations.

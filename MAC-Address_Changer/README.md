# MAC Address Changer

**Author:** Abdelrahman Adel
**Date:** 2021
**License:** [MIT License](LICENSE)

## Description

This Python script allows you to change the MAC address of a network interface on your system. It provides a simple way to set a custom MAC address for the specified network interface, or it can generate a random one if no hardware address is provided.

## Features

- Change the MAC address of a network interface.
- Specify the target network interface and the hardware address (MAC address) you want to set.
- If no hardware address is provided, the script generates a random MAC address.
- Handles bringing the interface down, changing the MAC address, and bringing it back up.
- Provides feedback on the status of the interface and the assigned MAC address.

## Usage

1. Ensure you have Python 3.11 or later installed on your system.

2. Run the script with the following command, specifying the network interface and, optionally, the hardware address (MAC address) you want to set:

python3.11 mac_address_changer.py -I <interface> -H <new_mac>


Replace `<interface>` with the name of the network interface you want to modify, and `<new_mac>` with the new hardware address you wish to set.

3. The script will change the MAC address of the specified interface and provide feedback on the process.

## Dependencies

- Python 3.11 or later.

## License

This script is provided under the terms of the MIT license. Feel free to modify and distribute it as needed.

## Disclaimer

Use this script responsibly and only on network interfaces for which you have authorization to change the MAC address. Unauthorized MAC address modification may violate privacy and legal regulations.

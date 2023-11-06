# Code Injector Script

**Author:** Abdelrahman Adel
**Date:** 2021
**License:** [MIT License](LICENSE)

## Description

This Python script acts as a code injector, intercepting and modifying HTTP requests and responses to inject code into web pages. It uses NetfilterQueue to capture and manipulate network traffic. The code injection allows you to add or modify JavaScript code in the responses, which can be used for various purposes, including testing and experimentation.

## Features

- Captures and processes HTTP requests and responses.
- Modifies HTTP requests to remove "Accept-Encoding" headers, allowing the interception of server responses as plain HTML.
- Injects custom code into the HTTP responses, which can include JavaScript or other content.
- Adjusts the "Content-Length" header in the responses to match the modified content length.

## Usage

1. Ensure you have Python 3.11 or later installed on your system.

2. Run the script with the following command, specifying the Netfilter Queue number:

python3.11 code_injector.py -q <QUEUE_NUM>


Replace `<QUEUE_NUM>` with the Netfilter Queue number you want to use. Make sure you have the `netfilterqueue` library installed.

3. The script will capture HTTP requests and responses and inject your custom code into the web pages.

## Dependencies

- Python 3.11 or later.
- The `scapy` library is used for packet manipulation and analysis. You can install it using `pip`:

pip3 install scapy OR python3 -m pip3 install scapy 

- The `netfilterqueue` library is used for capturing and processing network packets. You can install it using `pip`:
pip3 install netfilterqueue OR python3 -m pip install netfilterqueue


## Code Injection

The script is designed to inject code into web pages by modifying the content of HTTP responses. You can customize the code to be injected by modifying the script to suit your needs.

## License

This script is provided under the terms of the MIT license. Feel free to modify and distribute it as needed.

## Disclaimer

Use this script responsibly and only on networks and web pages for which you have permission to perform code injection. Unauthorized code injection may violate privacy and legal regulations.

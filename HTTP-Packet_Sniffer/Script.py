#!/usr/bin/env python3.11
"""
 - Simple Sniff Script To Sniff Network Packets Which Go Through The Specified Interface Using Scapy.Sniff Module .
"""

from scapy.all import Raw, sniff
from scapy.layers.http import HTTPRequest
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP,TCP


def PacketProcessing(TRAFFIC) -> None:
    if TRAFFIC.haslayer(HTTPRequest) and TRAFFIC.haslayer(Raw):
        print("\n[WEB-INFORMATION]")
        print(f"[URL] {TRAFFIC[HTTPRequest].Host.decode()}{TRAFFIC[HTTPRequest].Path.decode()}")
        print(f"[REQUEST-METHOD] {TRAFFIC[HTTPRequest].Method.decode()}")
        print(f"[WEB-PATH] {TRAFFIC[HTTPRequest].Path.decode()}")
        print(f"[WEB-VERSION] {TRAFFIC[HTTPRequest].Http_Version.decode()}")
        print(f"[WEB-EXTENSIONS] {TRAFFIC[HTTPRequest].Accept.decode()}")
        print(f"[WEB-ENCODING] {TRAFFIC[HTTPRequest].Accept_Encoding.decode()}")
        print(f"[WEB-LANGUAGE] {TRAFFIC[HTTPRequest].Accept_Language.decode()}")
        print(f"[WEB-ACCESS-CONTROL] {TRAFFIC[HTTPRequest].Access_Control_Request_Headers}")
        print(f"[WEB-ACCESS-REQUEST-METHOD] {TRAFFIC[HTTPRequest].Access_Control_Request_Method}")
        print(f"[WEB-AUTHORIZATION] {TRAFFIC[HTTPRequest].Authorization}")
        print(f"[WEB-CACHE-CONTROL] {TRAFFIC[HTTPRequest].Cache_Control}")
        print(f"[WEB-CONNECTION] {TRAFFIC[HTTPRequest].Connection.decode()}")
        print(f"[WEB-CONTENT-LENGTH] {TRAFFIC[HTTPRequest].Content_Length.decode()}")
        print(f"[WEB-MD5] {TRAFFIC[HTTPRequest].Content_MD5}")
        print(f"[WEB-CONTENT-TYPE] {TRAFFIC[HTTPRequest].Content_Type.decode()}")
        print(f"[WEB-COOKIE] {TRAFFIC[HTTPRequest].Cookie}")
        print(f"[WEB-DNT] {TRAFFIC[HTTPRequest].DNT}")
        print(f"[WEB-ORIGIN] {TRAFFIC[HTTPRequest].Origin}")
        print(f"[WEB-REFERER] {TRAFFIC[HTTPRequest].Referer.decode()}")
        print(f"[WEB-USER-AGENT] {TRAFFIC[HTTPRequest].User_Agent.decode()}")
        print(f"[WEB-UNKNOWN-HEADER] {TRAFFIC[HTTPRequest].Unknown_Headers}")

        IMPORTANT_DATA: Raw = TRAFFIC[Raw].load
        for KEYW in ["Username", "username", "Login", "login", "user", "User", "Password", "password", "pass", "Pass"]:
            if KEYW in str(IMPORTANT_DATA):
                print("\n[LOGIN-INFORMATION]")
                print(f"[USERNAME-PASSWORD] {IMPORTANT_DATA.decode()}")
                break
        print("\n[ADDRESSES]")
        print(f"[SOURCE-IP] {TRAFFIC[IP].src}\n[DESTINATION-IP] {TRAFFIC[IP].dst}")
        print(f"[SOURCE-MAC] {TRAFFIC[Ether].src}\n[DESTINATION-MAC] {TRAFFIC[Ether].dst}")
        print("\n[PORTS]")
        print(f"[SRC-PORT] {TRAFFIC[TCP].sport}\n[DST-PORT]{TRAFFIC[TCP].dport}")
        print(f"\n[DATA-OFFSET] {TRAFFIC[TCP].dataofs}")
        print(f"[DATA-SEQUENCE] {TRAFFIC[TCP].seq}")
        print(f"[DATA-ACKNOWLEDGEMENT] {TRAFFIC[TCP].ack}")


def SNIFF() -> None:
    INTERFACE: str = input("[INTERFACE] : ")
    sniff(iface=INTERFACE, prn=PacketProcessing, store=False)


SNIFF()

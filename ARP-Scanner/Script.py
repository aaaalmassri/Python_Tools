#!/usr/bin/env python3.11
"""
 - Simple Network Scanner Using ARP Protocol Logic .
 * Send ARP Requests To Network Devices And Receive ARP Responses .
 * Set Destination MAC As Broadcast MAC "FF:FF:FF:FF:FF:FF" .
"""

from scapy.layers.l2 import ARP, Ether, srp
from optparse import OptionParser


class PacketGenerator:
    def __init__(self, dstIP):
        self.source_IP = "192.168.100.4"
        self.destination_IP = dstIP
        self.destination_MAC = "ff:ff:ff:ff:ff:ff"

    def ARPPackets(self) -> ARP:
        ARPacket: ARP = ARP(psrc=self.source_IP, pdst=self.destination_IP)
        return ARPacket

    def EtherPacket(self) -> Ether:
        ETHERPacket: Ether = Ether(dst=self.destination_MAC)
        return ETHERPacket


if TARGET := input("[TARGET-IP] : "):
    ARPPacket = (
        PacketGenerator(dstIP=TARGET).EtherPacket()
        / PacketGenerator(dstIP=TARGET).ARPPackets()
    )
else:
    raise ValueError("[ERROR] NO TARGET ADDRESS WAS PROVIDED ")


def SCANNER() -> None:
    INTERFACE: str = input("[INTERFACE] :  ")
    AnsweredPackets = srp(
        x=ARPPacket, timeout=10, verbose=False, iface=INTERFACE
    )[0]
    for INDEX, HOST in enumerate(AnsweredPackets, 1):
        print(f"[TARGET-{INDEX}] {HOST[0].pdst}        {HOST[1].src}")


SCANNER()

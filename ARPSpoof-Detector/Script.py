#!/usr/bin/env python3.11
"""
 - ARP Spoffing Attack Detector Script 
 - This Script Functionality Based On : 
 .1) Check If The Sniffed Packet Has ARP Layer In It . 
 .2) Check If The ARP Packet Type Is (Response ARP Packet op=2 is-at) .  
 .3) Check If The Source IP Address Of The ARP Packet Is Eq Router IP Address .
  
"""
from scapy.all import sniff, srp
from scapy.layers.l2 import ARP, Ether
from optparse import OptionParser
from colorama import init, Fore, Back
from subprocess import run, DEVNULL

USERArguments: OptionParser = OptionParser()
USERArguments.add_option("-I", "--interface", dest="IFACE", help="INTERFACE NAME ")
Options, Args = USERArguments.parse_args()
INTERFACE = Options.IFACE


def PKTProcessing(PACKET):
    if PACKET.haslayer(ARP):
        RouterIP = str(PACKET[ARP].psrc)
        if PACKET[ARP].op == 2 and RouterIP.endswith(str(1)):
            init()
            print(f"[+] ARP Replay Packet Detected By {Fore.GREEN + PACKET[ARP].hwsrc}")
            Fore.WHITE

            def CheckAttackerMAC(IPAddr):
                ARPRequest = ARP(pdst=IPAddr)
                HWBroadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
                FullPkt = HWBroadcast / ARPRequest
                AnswerdPackets = srp(
                    FullPkt,
                    verbose=False,
                    timeout=5,
                    iface=INTERFACE,
                )[0]
                return AnswerdPackets[0][1].hwsrc

            def AttackHanding():
                run(
                    ["ip", "neigh", "flush", "all"],
                    check=True,
                    text=True,
                    stderr=DEVNULL,
                    stdout=False,
                )
                run(
                    ["ifconfig", INTERFACE, "down"],
                    stdout=Flase,
                    stderr=DEVNULL,
                    check=True,
                    text=True,
                )

            ARPReplayHWAddress = CheckAttackerMAC(IPAddr=PACKET[ARP].psrc)
            if ARPReplayHWAddress != PACKET[ARP].hwsrc:
                print(
                    Fore.WHITE
                    + f"[!] ARP Spoofing Attack Detected By {Fore.RED + PACKET[ARP].hwsrc}"
                )

                print(
                    Fore.WHITE
                    + f"[+] Original MAC For {Fore.LIGHTBLUE_EX + PACKET[ARP].psrc} - {ARPReplayHWAddress}"
                )
                exit()
            else:
                print(Fore.WHITE + f"[+] Legtimate ARP Replay By {ARPReplayHWAddress}")
                exit()


def ARPSniffer():
    sniff(iface=INTERFACE, prn=PKTProcessing, store=False)


ARPSniffer()

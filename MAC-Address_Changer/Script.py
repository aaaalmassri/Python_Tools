#!/usr/bin/env python3.11
"""
 Simple MAC Address Changer Script .
"""

from contextlib import suppress
from subprocess import run, DEVNULL
from optparse import OptionParser
from datetime import datetime
from psutil import net_if_stats


with suppress(KeyboardInterrupt, ValueError, TypeError) as error:
    UserArguments: OptionParser = OptionParser()
    UserArguments.add_option("-I", "--interface", dest="INTERFACE", help="Interface Name")
    UserArguments.add_option(
        "-H", "--hardware", dest="HW", help="Hardware Address (MAC Address)"
    )
    Options, Arguments = UserArguments.parse_args()
    INTERFACE: str = Options.INTERFACE
    MAC: str = Options.HW

    def HWChanger(interface: str) -> None:
        if not MAC:
            run(
                ["ifconfig", interface, "hw", "ether", "00:1f:dc:23:4a:fa"],
                stdout=False,
                stderr=DEVNULL,
                check=True,
                text=True,
            )
        else:
            run(
                ["ifconfig", interface, "hw", "ether", MAC],
                stdout=False,
                stderr=DEVNULL,
                check=True,
                text=True,
            )

        run(
            ["ifconfig", interface, "up"],
            stdout=False,
            stderr=DEVNULL,
            check=True,
            text=True,
        )
        print(f"[INTERFACE-{datetime.now()}] UP - {MAC}")

    """
    Check Interface Status "Down | Up" 
    """
    INTERFACE_STATUS = net_if_stats()[INTERFACE]
    if INTERFACE_STATUS.isup:
        run(
            ["ifconfig", INTERFACE, "down"],
            stdout=False,
            stderr=False,
            check=True,
            text=True,
        )
        HWChanger(interface=INTERFACE)
    else:
        HWChanger(interface=INTERFACE)
    if error:
        print(f"[ERROR] {error}")

#!/usr/bin/env python3.10

"""
 - TCP Socket To Check For Open Ports
 - Port Scan Using TCP Socket .
"""
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue

TARGET: str = input("[TARGET] : ")
PORT_RANGE: int = int(input("[PORT-RANGE] : "))
PORTS_QUEUE: Queue = Queue()

for Port_No in range(PORT_RANGE):
    # Fill up the queue of ports numbers .
    PORTS_QUEUE.put(Port_No)


def scan_function():
    while not PORTS_QUEUE.empty():
        port: int = PORTS_QUEUE.get()
        with socket(family=AF_INET, type=SOCK_STREAM) as SCAN:
            try:
                SCAN.connect((TARGET, port))
                print(f"[SCAN] PORT {port} OPEN & LISTING ")
            except Exception:
                print(f"[SCAN] PORT {port} CLOSED ")
        PORTS_QUEUE.task_done()


for _ in range(30):
    SCAN_THREAD: Thread = Thread(target=scan_function, daemon=True)
    SCAN_THREAD.start()

PORTS_QUEUE.join()
print("[SCAN] FINISHED ")

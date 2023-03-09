#!/usr/bin/python3

from scapy.all import *
import signal


def def_handler(sig, frame):
        print("\n\n[!] Saliendo... ")
        sys.exit(1)

# Ctrl_C
signal.signal(signal.SIGINT, def_handler)

def dataParser(packet):
        if packet.haslayer(ICMP):
                if packet[ICMP].type == 8:
                        data = packet[ICMP].load[-4:].decode("utf-8")
                        print(data, flush=True, end='')

if __name__ == '__main__':

        sniff(iface='tun0', prn=dataParser)

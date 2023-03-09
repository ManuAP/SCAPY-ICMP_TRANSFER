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

EJ DEL OUTPUT:
❯ python3 icmp_transfer.py

127.0.0.1	localhost.localdomain	localhost
::1		localhost6.localdomain6	localhost6

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts

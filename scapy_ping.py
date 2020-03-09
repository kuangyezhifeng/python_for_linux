# -*- coding: utf-8 -*-
#scapy ping  tools
import logging
from scapy.all import *
# logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def ping(ip):
    ping_package = IP(dst=ip)/ICMP()
    ping_recv = sr1(ping_package, timeout=2, verbose=False)
    if ping_recv:
        print('destination host active! ')
        return ip, 1
    else:
        print('destination host dead !')
        return ip, 0


if __name__ == '__main__':
    ping('192.168.1.50')

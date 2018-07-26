#!/usr/bin/python

from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(filter='host 10.0.2.15 and tcp dst port 23',prn=print_pkt)
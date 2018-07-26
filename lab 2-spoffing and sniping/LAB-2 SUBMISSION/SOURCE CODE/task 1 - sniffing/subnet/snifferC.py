#!/usr/bin/python

from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(filter='net 8.8.8.0/24',prn=print_pkt)
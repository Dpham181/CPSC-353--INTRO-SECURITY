from  scapy.all import *


def print_pkt(pkt):
   pkt[ICMP].show()



pkt = sniff(filter="icmp",prn = print_pkt)

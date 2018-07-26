from  scapy.all import *

b = ICMP()







def spoofed_pkt(pkt):

   if IP in pkt:
	src = pkt[IP].src
	des = pkt[IP].dst
   	spoofed = IP(src=des, dst=src) / b
   	send(spoofed)
	


pkt = sniff(filter= "icmp",prn = spoofed_pkt)
   

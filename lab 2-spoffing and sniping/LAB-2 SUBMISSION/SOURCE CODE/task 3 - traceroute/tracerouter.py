from  scapy.all import *



# showing ip 
a = IP()

# icmp protocol

b = ICMP()
# target as cal fullerton server ip address
a.dst ="137.151.27.1"

# for loop to assigning the value for time to live 0 to 30 
for t in range(0,30):
     a.ttl= t
     trace= a/b
     send(trace)
     ls(a)	


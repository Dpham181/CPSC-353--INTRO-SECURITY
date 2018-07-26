from  scapy.all import *
# get scapy modules 

# showing ip 
a = IP()
# show datas in network
a.show()

# icmp protocol
b = ICMP()

# face ip when echo requrest 

IP1 ="192.168.1.1"
PORT = 9090
# VM B IP ADRRESS 
IP2 ="10.0.2.4"
PORT2= 9190



# SPOOFED THAT IP WITH ICMP PROTOCOL 

spoofed = IP(src=IP1, dst=IP2) / b

# SEND PACKET
send(spoofed)
# LISTING ALL DATA PRINT OUT 
ls(a)

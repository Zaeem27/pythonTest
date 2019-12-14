import scapy

from scapy.all import *

hostname = "bristol.ac.uk"

for i in range (1,25):
    pkt = IP(dst="137.222.0.38", ttl=i) / UDP(dport=33434)
    reply = sr1(pkt, verbose=0, timeout=1)
    if reply is None:
        break
    elif reply.type == 3:
        print("Done!", reply.src)
        break
    else:
        print("%d hops away: " % i , reply.src)
        

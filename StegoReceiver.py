import scapy
import random
import string

from scapy.all import *

ip = input("Enter sender IP: ")
filterIP = "ip and src " + ip
print("Listening...")
message=""
while 1:
    reply = sniff(count = 1, filter=filterIP)
    pktlen = reply[0].len
    #print(pktlen)
    #-14 for ethernet header being added somewhere
    if 126 > (pktlen) > 31 :
        message = message + (chr(len(reply[0])-14))
        if len(message) == 32:
            break

print(message.strip(" "))
    

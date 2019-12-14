import scapy
import random
import string

from scapy.all import *

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

ip = input("Enter reciever IP: ")

while 1:
    sentence = input("Enter a sentence less than 32 characters:")
    if len(sentence) > 32:
        print("Message too long")
    else:
        break
if len(sentence) < 32:
    sentence = sentence.ljust(32)

print("Sending...")

for char in sentence:
    junkSize = ord(char) - 20
    junkString = randomString(junkSize)
    pkt = IP(dst=ip, len=ord(char))/junkString
    #send(pkt)
    #print(len(pkt))
    sr1(pkt, verbose =0, timeout =1)

print("...Done...")

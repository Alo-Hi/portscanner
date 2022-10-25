#import ipaddress
import sys
import socket

ip_address = "localhost"
timeout = 0.001

print("scanning")
for port in range(1,65535):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(timeout)
    result = s.connect_ex((ip_address,port))
    if result == 0:
        print(str(port) + " is open on " + ip_address)
        
    s.close()


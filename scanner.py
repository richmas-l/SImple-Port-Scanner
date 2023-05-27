#!/bin/python3
#This is a very basic port scanner for your home network.
#It will scan ports 50-85
#Make some changes to make it more robust

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py")
	
#Add a pretty banner
print("-" * 50)
print("scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" *50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except keyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()

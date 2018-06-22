#!/usr/bin/python

import commands
import webbrowser
option='''
press 1 to check os version
press 2 to check wireless connected
press 3 to check internet access
perss 4 to check google access
'''

print option

choice=raw_input("enter any number") 

if choice == "1":
	print "check os version"
	os_version=commands.getoutput('cat /etc/os-release')
	print os_version

elif choice == "2":
	print "plz wait wireless is checking "
        cable_check=commands.getoutput('iw wlp6s0 link')
        if 'Connected' in cable_check:
		print "wireless is connected"
	else:
		print "wireless is not connected" 

elif choice == "3":
	print "internet connectivity is checking "
	cable_connectivity=commands.getoutput('ping 8.8.8.8 -c 4')
	if 'PING' in cable_connectivity:
		print "internet connectivity successful"
	else: 
		print "internet connectivity not succsseful"


elif choice == "4":
	print "check google access"
	access=webbrowser.open('http://www.google.com')
	print access

else :
	print "wrong choice"
	 


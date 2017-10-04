def bulk_whois(filename):
	import nclib
	import os
	import string
	import sys
	import win_inet_pton
	from time import strftime
	# Not needed in a function right?
	#fileName = ''.join(sys.argv[1:2])
	if fileName == '':
		fileName = raw_input('''
	Input the file with extension
	>''')
	with open(fileName, "r") as file:
		ip_list = file.readlines()
	ip_list = ''.join(ip_list)
	print "Looking up IPs now..."
	nc = nclib.Netcat(('whois.cymru.com', 43))
	nc.send(ip_list)
	lookup_output = nc.recv_all()
	nc.close()
	# Need to remove output header
	lookup_output = lookup_output.replace("NA","-")
	# Maybe test that NA is followed by either spaces and a "|" or a "\n"?
	now = strftime("%Y%m%d%H%M%S")
	with open("output/" + now + "_whois_output", "w") as file:
		file.write(lookup_output)

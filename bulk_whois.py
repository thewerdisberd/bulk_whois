"""
Input file format:
begin
verbose
<IPs Here>
end
"""
import nclib
import os
import string
import sys
import win_inet_pton
import time
fileName = ''.join(sys.argv[1:2])
print "\nBulk whois lookup tool using Team Cymru's whois service"
print "Version 1.0 - Last Edited: 2017/10/03\n"
if fileName == '':
    print "Enter an input method"
    print "Use Input File (1)"
    print "Enter Manually (2)"
    input_choice = raw_input("> ")
    if input_choice == "1":
        print "Input the file name with extension"
        fileName = raw_input("> ")
    elif input_choice == "2":
        pass
        # need to fix paste issue
        #print "Enter the IPs below"
        #print "Data needs to be in this format\nbegin\nverbose\n<IPs Here>\nend\n"
        #manual_input = raw_input("")
        #with open("lookup_list", "w") as file:
        #    file.write(manual_input)
        #fileName = 'lookup_list'
    else:
        print "Please enter a valid input method"
        input_choice = raw_input("> ")
time.sleep(.1)
with open(fileName, "r") as file:
    ip_list = file.readlines()
# Ensures proper EOF over the wire
ip_list[-1] = ip_list[-1].rstrip("\r\n")
ip_list[-1] = ip_list[-1] + "\n"
ip_list_count = len(ip_list) - 3
ip_list = ''.join(ip_list)
nc = nclib.Netcat(('whois.cymru.com', 43))
print "Connection opened."
time.sleep(.5)
print "Looking up %s IPs now..." % ip_list_count
nc.send(ip_list)
lookup_output = nc.recv_all()
time.sleep(.5)
nc.close()
print "Connection closed."
# Need to remove output header
lookup_output = lookup_output.replace("NA","-")
# Maybe test that NA is followed by either spaces and a "|" or a "\n"?
now = time.strftime("%Y%m%d%H%M%S")
output_file = now + "_whois_output"
with open("output/" + output_file, "w") as file:
    file.write(lookup_output)
print "Output saved to output/%s" % output_file
view_output = raw_input("Would you like to view the output now (Y/n)? ")
if view_output == "Y":
    print lookup_output
elif view_output == "y":
    print lookup_output
else:
    pass

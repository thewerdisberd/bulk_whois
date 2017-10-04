#!/bin/bash
################################################################################
#                                                                              #
# A CLI wrapper for the whois lookup tool run by Team Cymru.                   #
# http://www.team-cymru.org/IP-ASN-mapping.html                                #
# Requires the netcat-traditional package to be installed. Having nc (netcat-  #
# freebsd package) installed may cause problems because it uses netcat as an   #
# alias.                                                                       #
# Tested on Ubuntu 16.04                                                       #
#                                                                              #
################################################################################
clear
echo "Paste the list of IPs to lookup.
Leave a newline at the end.
Use CTRL + D to exit."
echo "begin" > lookup_list
echo "verbose" >> lookup_list
cat >> lookup_list
echo "end" >> lookup_list
clear
netcat whois.cymru.com 43 < lookup_list > lookup_results
TIME=$(date +"%Y-%m-%d.%H%M%S")
cp lookup_results ./output/$TIME.bulk_whois.txt
less lookup_results
rm lookup_list
rm lookup_results

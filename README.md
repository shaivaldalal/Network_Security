# Network Security
The following repo contains code for experiments with various elements of network security. These codes aim to understand networks, the way they work and demonstrate vulnerabilities in these netowkring protocols.

Language: Python<br>
The following concepts of computer networking were explored:
1. ARP (Address Resolution Protocol) - Folder: MITM
    * ARP is used to allow locally linked systems to communicate using IP by binding IP addresses to hardware based MAC addresses. 
    * The RFC is available <a href="https://tools.ietf.org/html/rfc6747">here</a>. 
    * We aim to explore the security considerations in the <a href="https://tools.ietf.org/html/rfc6747">RFC</a> by developing a proof-of-concept script in Python
2. DHCP (Dynamic Host Configuration Protocol) - Folder: DHCP_Starvation
    * DHCP allows devices on the network to be uniquely identified through an IP address without the need for static configuration
    * The RFC is available here <a href="https://tools.ietf.org/html/rfc2131">here</a>.
    * DHCP is vulnerable to exhaustion attacks through spoofed MAC adddresses. This can lead to exhaustion of IP addresses in a subnet resulting in a DOS attack. A proof-of-concept using Python has been developed to demonstrate this vulnerability.

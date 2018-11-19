## DHCP Starvation<br>
**Programming Language**: Python (3+)<br><br>
**Requirements**: Scapy, Numpy<br><br>
**Tested On**: Ubuntu 16.04 (amd64)<br><br>
**Description** <br>
* Code for exploiting a fundamental flaw in DHCP that allows attackers to carry out a denial-of-service attack on a local network. 
* The exploit enables attackers to exhaust the subnet's IP address pool thereby preventing new devices to enter the network and if run contiuously, over time, it prevents existing systems from accessing the network<br><br>
**Attack Type**: Denial of Service (DOS)<br><br>
**Execution Instruction**
>python3 starvation.py

*Notes*
 1. You can use *python* command directly as long as your system symlinks it to python3
 2. Please ensure that you set the subet in the subnet variable
 3. Please avoid running it on critical networks as it may cause disruption of services
 4. Strictly for educational purposes

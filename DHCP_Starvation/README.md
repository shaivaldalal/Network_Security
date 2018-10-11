## DHCP Starvation<br>
**Programming Language**: Python (3+)<br><br>
**Requirements**: Scapy, Numpy<br><br>
**Tested On**: Ubuntu 16.04 (amd64)<br><br>
**Description** <br>The code in this repo is able to starve a network of IP addresses. This essentially prevents any new device from entering the network which in turn results in a DOS attack.
<br><br>
**Execution Instruction**
>python3 starvation.py

*Notes*
 1. You can use *python* command directly as long as your system symlinks it to python3
 2. Please ensure that you set the subet in the subnet variable
 3. Please avoid running it on critical networks as it may cause disruption of services

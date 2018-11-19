## Man-In-The-Middle attack (MITM)<br>
**Programming Language**: Python (3+)<br><br>
**Requirements**: Scapy<br><br>
**Tested On**: Ubuntu 16.04 (amd64)<br><br>
**Description** <br>The following repo contains code to poison the ARP cache and perform an MITM attack to snoop on a network and capture packets for protocols vulnerable to a security downgrade attack.<br><br>
**Execution Instruction**
>./arppoison.sh<br>
>./sslstrip.sh

*Notes*
 1. You can use *python* command directly as long as your system symlinks it to python3
 2. Please ensure that you set the required parameters in the shell file for ARP poisoning
 3. Please avoid running it on critical networks as it may cause disruption of services
 4. The use of these programs must be for purely educational purposes

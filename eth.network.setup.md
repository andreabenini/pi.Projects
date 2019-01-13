# Static IP configuration on `eth0`
```
root@raspberrypi:~# cat /etc/network/interfaces.d/eth0 
auto eth0
iface eth0 inet static
    address 192.168.0.3
    netmask 255.255.255.0
    gateway 192.168.0.1
    dns-nameservers 192.168.0.2
```

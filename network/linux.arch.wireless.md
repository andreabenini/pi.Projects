
# Linux Arch wireless configuration on Raspberry Pi
Here's a sample config for Arch

```
[root@alarmpi ~]# cat /etc/netctl/wireless 
Description='My wireless connection'
Interface=wlan0
Connection=wireless

Security=wpa
IP=dhcp

ESSID=YOURSSIDHERE
# Prepend hexadecimal keys with \"
# If your key starts with ", write it as '""<key>"'
# See also: the section on special quoting rules in netctl.profile(5)
Key=PlainTextPublicKeyForIt
# Uncomment this if your ssid is hidden
Hidden=yes
# Set a priority for automatic profile selection
#Priority=10

```
With this file you can have a working wireless connection

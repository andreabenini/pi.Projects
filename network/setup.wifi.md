# How to setup a generic wireless network card in you RPi

- Insert the card
- Check if it's detected
```
# lsusb 
... (this one in my case)
Bus 001 Device 004: ID 0b05:1234 ASUSTek Computer, Inc. USB-100 802.11n Network Adapter [Realtek RTL8188]
...
```
- Use this command to get properly encoded password of your wifi
```
# wpa_passphrase "mywlan" "thecoolestpasswordforit"
network={
	ssid="mywlan"
	#psk="thecoolestpasswordforit"
	psk=a889448a38e814dd5a78f0bb440151509984c4ffbaf3a193ca1ced33ae0c2eb6
}
```
- Copy that from standard output
- Edit file /etc/wpa_supplicant/wpa_supplicant.conf with nano or your preferred editor
  - Change two letters country key `country=GB` with your current match if you're not living in the UK
  - Paste previous code at the end of the file
  - Delete line `#psk="...."` from file, you password won't be directly visible from here (suggested)
  - Save it
- Now type `wpa_cli -i wlan0 reconfigure` to get an hot config reload for that wifi card
- Wait for a while and issue command `ifconfig wlan0` to see if a proper ip address is set. DHCP must be present or you need
to set your own manual IP address for it

# Encode PSK
Please **do not** write your preshared key in clear text in _wpa_supplicant.conf_ text file, this is an huge security issue.
Use `wpa_passphrase` utility for that. Here's an example
```
$ wpa_passphrase 
usage: wpa_passphrase <ssid> [passphrase]

If passphrase is left out, it will be read from stdin

$ wpa_passphrase myssid mypasswordforit
network={
	ssid="myssid"
	#psk="mypasswordforit"
	psk=4a9be46ab2e1b1f89a4bf4e1fb43b5a0d82654e284a3394baa863f0ab4e6afb4
}
```
The utility generates a text output, grab it from there and paste into your _wpa_supplicant.conf_ configuration file, obviously withouth the commented _#psk*_ line

# Some Samples
Here are few configurations for different scenarios
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
# some country codes US|UK|IT|DE|ES
country=US

network={
# Public network, no auth
#    ssid="freenetwork"
#    key_mgmt=NONE

# WPA2-PSK network, basic auth
#    ssid="wpanetwork"
#    proto=RSN
# Add this option if you're using an hidden SSID
#    scan_ssid=1
#    key_mgmt=WPA-PSK
#    pairwise=CCMP TKIP
#    group=CCMP TKIP
#    psk="TheCoolestPasswordYouDontWantToShare"
}
```

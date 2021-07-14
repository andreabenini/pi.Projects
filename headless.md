# RaspberryPi Headless Hints
Pi won't boot without HDMI cable plugged in. It happened me more than once and it's widely reported with Pi4 (and newer) cards, it sometimes happens on older
ones where latest microcode is applied or when everything is left to defaults. Did it more than once on ArchPi too.

As reported from the forums (https://www.raspberrypi.org/forums/viewtopic.php?t=253312) this seems to be widely reported and a designated choice but might be
a problem for folks using them in headless mode.  
The preferred solution is RTFM (as usual) because those modes are documented from official documentation
(https://www.raspberrypi.org/documentation/configuration/config-txt/video.md).  

## config.txt
adding _hdmi_force_hotplug=1_ to `config.txt` is more than enough but I usually add these lines to **config.txt**
```
hdmi_force_hotplug=1
# Force HDMI group = CEA and resolution to 640x480
hdmi_group=1
hdmi_mode=1
```

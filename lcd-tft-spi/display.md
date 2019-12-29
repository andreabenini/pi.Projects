### /boot/config.txt
```
dtparam=i2c_arm=on
dtparam=spi=on
#dtoverlay=tft9341:rotate=270
dtoverlay=waveshare32b:rotate=90
```

### /boot/cmdline.txt
```
# `fbcon=` parameters are what you need to get it working
dwc_otg.lpm_enable=0 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait fbcon=map:10 fbcon=font:VGA8x8 logo.nologo
```

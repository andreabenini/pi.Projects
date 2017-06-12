## Measure CPU Core temperature on Raspberry Pi

### RPi Utility
```
# vcgencmd measure_temp
temp=45.1'C
```

### Bash'o'Rama
```
host:~ # CPU=`cat /sys/class/thermal/thermal_zone0/temp`
host:~ # echo $CPU
45084
host:~ # echo "$((CPU/1000))° C"
45° C
```

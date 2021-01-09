# Detecting underpowered raspberry devices
`vcgencmd` (_/usr/bin/vcgencmd_) is a generic utility to detect a lot of raspberry things like: temperature, underpowered device,
videocore information and so on.

One of its commands include: **get_throttled**, this returns the throttled state of the system. It is a bit pattern - a bit being set 
indicates the following meanings:

| Bit |	Hex Value | Meaning
|---- |---------- |:------------------------------------------------ |
| 0   | 1	      | Under-voltage detected
| 1	  | 2	      | Arm frequency capped
| 2	  | 4	      | Currently throttled
| 3	  | 8	      | Soft temperature limit active
| 16  | 10000 	  | Under-voltage has occurred
| 17  | 20000 	  | Arm frequency capping has occurred
| 18  | 40000 	  | Throttling has occurred
| 19  |	80000  	  | Soft temperature limit has occurred

A value of zero indicates that none of the above conditions is true.

To find if one of these bits has been set, convert the value returned to binary,
then number each bit along the top. You can then see which bits are set. For example:
```
0x50000 = 0101 0000 0000 0000 0000
```

Adding the bit numbers along the top we get:
```
19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0
 0  1  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
```

From this we can see that bits 18 and 16 are set, indicating that the Pi has previously been throttled due to under-voltage,
but is not currently throttled for any reason.

Alternately, the values can be derived using the hex values above, by successively subtracting the largest value:
```
0x50000 = 40000 + 10000
```

## Example
When you detect something like
```
~ $ vcgencmd get_throttled
throttled=0x0
```
means your Pi is safe and no power supply issues were detected 

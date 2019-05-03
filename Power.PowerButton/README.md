### Power button for the Raspberry Pi

Even the RaspberryPi might be powered on with a common switch. If you're using RPi3 with latest firmware there's an hidden
feature to power it on.
There's no need for additional hardware, connect a switch between GPIO3 and GND and everything is fine.<br>
When you shut down the Pi it will stay in a halt state, it still consumes a small amount of power just like every common PC
with ATX PSU of these days. From that state you can Recover-PowerOn the Pi again just by pressing that switch, everything is
done on firmware.

Provided python file might be used to shutdown the board with a software daemon

Take a look at [GPIO schematics](../gpio.HeaderPinout.png), Get it from GPIO3 and GND as shown below

| Name   | Pin        | Pin        | Name        |
|--------|------------|------------|-------------|
| 3.3v   | _01 ._     | _02 ._     | 5v DC Power |
| GPIO02 | _03 ._     | _04 ._     | 5v DC Power |
| GPIO03 | **05 [X]** | **06 [X]** | GND         |
| GPIO04 | _07 ._     | _08 ._     | GPIO14      |

### Powering the Raspberry Pi with GPIO

Be careful: you need a stable power supply because there is no voltage regulation or fuse protection on the GPIO to protect the Pi from over-voltage or current spikes.<br/>
If an incorrect voltage is applied, or a current spike occurs on the line you can __permanently damage your Raspberry Pi__. At best, you’ll burn out some or all of the GPIO pins, at worst you can fry your Pi! So be careful.

Take a look at [GPIO schematics](https://github.com/andreabenini/pi.Projects/blob/master/gpio.HeaderPinout.png), 5v Vcc goes on Pin #2, GND goes on Pin #6

| Name   | Pin    | Pin        | Name        |
|--------|--------|------------|-------------|
| 3.3v   | _01 ._ | **02 [X]** | 5v DC Power |
| GPIO02 | _03 ._ | _04 ._     | 5v DC Power |
| GPIO03 | _05 ._ | **06 [X]** | GND         |

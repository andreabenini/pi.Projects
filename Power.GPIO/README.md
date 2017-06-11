### Powering the Raspberry Pi with GPIO

Be careful about that, you need a stable power supply because there is no regulation or fuse protection on the GPIO to protect from over-voltage or current spikes.<br/>
If an incorrect voltage is applied, or a current spike occurs on the line you can __permanently damage your Raspberry Pi__. At best, you’ll burn out some or all of the GPIO pins, at worst you can fry your Pi! So be careful.

Take a look at [GPIO schematics](/andreabenini/pi.Projects/HeaderPinout.png), 5v Vcc goes on Pin #2, GND goes on Pin #6

| Name      | Pin | Pin | Name             |
|-----------|-----|-----|------------------|
| 3.3v (01) |  .  |  O  | 5v DC Power (02) |
| GPIO (02) |  .  |  .  | 5v DC Power (04) |
| GPIO (03) |  .  |  O  | GND         (06) |

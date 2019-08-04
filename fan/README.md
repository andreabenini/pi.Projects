# Assorted Raspberry Pi FAN circuits
- https://hackernoon.com/how-to-control-a-fan-to-cool-the-cpu-of-your-raspberrypi-3313b6e7f92c<br>
  Worst scheme ever, hardware idea on PCM (GPIO 18) is fine but using internal 5V and no current limiting resistors is
  not a good at all. Nice to see it but electronics needs a rewrite
- https://www.digikey.com/en/maker/projects/control-a-dc-fan-with-a-raspberry-pi/f3fa09ab84c049d08474b625bee8d8f2<br>
  This uses an external therm sensor to get it so it's not my intended usage, needs some adaptation for doing what I've
  planned but overall project is fine
- https://github.com/MrBiz/PiFan<br>
  Reasonable guide for the problem, three wire (PWM) 5v fan, seems correct even if he doesn't applied a current limiting
  resistor on the GPIO, with a proper schematic this seems to be a good project
- https://www.allaboutcircuits.com/projects/raspberry-pi-project-control-a-dc-fan/<br>
  this one seems to be reasonable, flyback protection with a schottky diode and a reasonable resistor on transistor base
- https://www.digikey.com/en/maker/blogs/2019/how-to-control-a-dc-fan-using-the-raspberry-pi<br>
  this is probably the best one because is documented carefully, arguments the topic with proper math and uses a power MOSFET
  (huge one but capable of controlling many fans)
- https://www.youtube.com/watch?v=9Qumu2h8FjY&feature=youtu.be&t=1060<br>
  An usual reader of hackaday probably already knows HomoFaciens and his projects, this one is simple and practical, it uses a
  12v external battery, a transistor and proper resistors in place. PWM input is not used, ON/OFF on the fan only
- https://www.instructables.com/id/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/<br>
  Basic and simple, useful for 5v fan(s)
- https://www.raspberrypi.org/forums/viewtopic.php?t=194621<br>
  And a nice forum discussion as well, take a look at the schematics at the bottom, it's something useful to take on
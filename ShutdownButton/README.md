**NOTE:** _outdated project_, use [Power.PowerButton](../Power.PowerButton) instead

# pi.ShutdownButton
__Safe shutdown daemon__

This button acts as a reset/shutdown button to deal unattended RPi machines.

- Short press the button to safely shutdown the board
- Long press to reboot it

See schematics to reproduce the circuit and use ShutdownButton.py daemon to manage it<br/>
Short press is dealt from software daemon (ShutdownButton.py), long press is managed from hw circuit so it can work even if the os is hanged somewhere.<br/>
Long press charges the capacitors and RPi reset pins are shorted from the button, this is why the circuit always does something. Short press is suggested to safely shutdown the machine, use long press only when daemon or the OS aren't working properly

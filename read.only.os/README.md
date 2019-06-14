### Note
Here's an useful collection of links I have used to properly set a generic RPi OS in read/only mode in order to:
- Avoid OS data corruption on improper power loss events
- Avoid SD corruption, SD storage devices are not made for long term operations with heavy read/write events done from an OS
- Have long lasting machines dedicated to single services, when nothing changes your system is stable and keeps your services
running without surprises
- Making `ro` a root partition is easy but it doesn't solve your problems if you don't design your system to adapt to it

### Links
- https://hallard.me/raspberry-pi-read-only/<br>
  Quite decent reference, it covers most cases and it's a good starting point for a quite common and standard system, 
  when you customize a lot of things you're on your own
- https://gist.github.com/yeokm1/8b0ffc03e622ce011010<br>
  Focused on Linux Arch but suggested hints are valid for everyone, just keep `pacman` hints away if you're not using Arch


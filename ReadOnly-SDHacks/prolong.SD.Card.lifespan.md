# Prolong your Raspberry Pi SD card’s lifespan
Use a few tweaks and USB-booting to prolong your SD card and avoid losing important Raspberry Pi projects.  

At some point during the lifetime of your Raspberry Pi, you’re likely to encounter a problem with your SD or microSD card.
If you’re lucky, this will be minimal— perhaps a reboot will fix it. If you’re unlucky, it could mean the end of your SD
card and the loss of all data on your Pi, including your latest project.
The simple fact is that SD cards do not last forever. Flash storage, by design, has a limited number of read/write cycles.
While errorcorrection software is built-in and cards ship with larger-than-described storage to cover damaged blocks,
eventually corruption will cause a problem.
SD card corruption occurs in various ways. It might be due to a sudden variation in voltage during a read/ write cycle or
from being removed from the Raspberry Pi. Flash storage is also susceptible to extreme temperatures and physical damage.
Cheap SD cards, meanwhile, are usually unreliable; whatever the situation, you should rely on the more expensive cards
from SanDisk or Kingston.
While it might be useful to regularly back up your flash storage to enable quick recovery, a more proactive option is to
bypass the SD card entirely by relying on other storage mediums for booting the Raspberry Pi, but you should also be aware
of various tools that can be used to protect your microSD card.  

### 1 DON’T FLASH A FRESH OS FOR EVERY PROJECT
The read/write cycle limit is a physical hardware restriction preventing infinite reuse of an SD card. So look after it!
While **swappiness** (the kernel parameter defining how much and often RAM is copied to storage) is apparently set low in
Raspbian, there is more you can do.
One way to extend the lifespan of the device is to avoid flashing a fresh version of Raspbian (or whatever your preferred
OS is) every single time you start a new project.
Doing so applies a card-wide reduction in the remaining read-write cycles. So by maintaining a working microSD card
throughout several projects, you avoid the effect that regular flashing has on the card.
This is not a perfect solution, but it will help you get projects started without the initial flashing and configuration
that is typically required. Need to keep things tidy?  
Remove software with `sudo apt get remove <APPNAME>`. This will uninstall the software you no longer need, but may be
time-consuming. In short, only flash Raspbian when you really must.

### 2 MAINTAIN A CONSTANT POWER SUPPLY
A reliable power supply is a major aspect in the preservation of your Raspberry Pi’s SD storage. If there’s much variation,
data can be lost, ultimately causing corruption of the card. At this point, your Pi probably won’t boot, and a new OS will
need flashing.
The Pi requires a constant voltage of 5V. This is available via the approved mains adaptors, but keep in mind that these
devices cannot account for failings in the sockets they’re plugged into. Don’t use cheap extension leads. Instead, ensure
your mains adaptor is connected either to the wall (if you have modern surge protection built in) or otherwise to an
extension with surge protection.
It’s common to attempt to squeeze as much power out of a Raspberry Pi through overclocking, but this too is a possible
cause of disk corruption. Rather than go through the rigmarole — and card-degrading — act of flashing a new ROM, it’s safer
to avoid overclocking the Pi’s CPU if you want to maintain a stable system.

### 3 WRITE TO RAM, NOT STORAGE
A great way to reduce the number of read/write cycles on your SD card is to not write to it in the first place. This
doesn’t mean leaving your Pi powered off! Instead, you can write everything to the computer’s RAM. As such, nothing will
be written to the microSD card, thereby extending its life. Better still, this is easy to set up using tempfs. Begin by
opening the fstab in nano with `sudo nano /etc/ fstab` . At the bottom of the file, add this line:
```
tmpfs /var/log tmpfs defaults,noatime,nosuid, oe= 0755,size=100m 0 0
```
Press **Ctrl-X** to exit and save. This moves the `/var/log` directory to RAM, reducing the microSD card’s read/write
cycles. Other locations can be safely moved to RAM too:
```
tmpfs /tmp tmpfs defaults,noatime,nosuid,siz =100m 0 0
tmpfs /var/tmp tmpfs defaults,noatime,nosuid size=30m 0 0
tmpfs /var/log tmpfsdefaults,noatime,nosuid,mo de=0755,size=100m 0 0
tmpfs /var/run tmpfs defaults,noatime,nosuid,
mode=0755,size=2m 0 0 tmpfs / var/spool/mqueue
tmpfs defaults,noatime,nosuid, mode=0700,gid=12,size=30m 0 0
```
**Beware:** this will only last until you reboot your Pi, at which point, everything is cleared from RAM.

### 4 BOOT YOUR PI FROM A USB STICK
Recent updates to Raspbian enable you to boot a Raspberry Pi 3 via an attached USB device (a flash drive, standard HDD
or even an SSD), bypassing the microSD card entirely.  
Via SSH, begin with: `sudo apt-get update sudo BRANCH=next rpi-update`
Then enable USB boot mode:
```
echo program_usb_boot_ mode=1 | sudo tee -a boot/config.txt
```
With the `program_usb_boot_mode=1` instruction added to the end of the **config.txt** file, reboot with `sudo reboot`.
When the Pi restarts, you’ll need to check if the one-time programmable (OTP) memory has been changed.
```
vcgencmd otp_ dump | grep 17:
```
If the previous steps have been successful, you should see something like `0x3020000a` (pictured, below).
Your Raspberry Pi is now ready to boot from a USB device, so connect the one that you want to use; but note that it
_SD cards do not last forever. Flash storage has a limited number of read/write cycles._
will be reformatted. You can Identify your USB device with `lsblk`, which will list all block devices.
Connected USB devices are usually called **sda**. Enter the following to unmount the device and run the Parted tool:
```
sudo umount /dev/sda sudo parted /dev/sda
```
This will take you to the Parted prompt.

### 5 COPY RASPBIAN TO YOUR USB DRIVE
At the prompt, enter:
```
mkpart primary fat32 0% 100M mkpart primary ext4 100M 100% print
```
Then use **Ctrl-C** to exit. Back at the command prompt, you will need to create both a new boot filesystem and
root filesystem:
```
sudo mkfs.vfat -n BOOT -F 32 /dev/sda1
sudo mkfs.ext4 /dev/sda2
```
Next, mount the target filesystems:
```
sudo mkdir /mnt/target
sudo mount /dev/sda2 /mnt/target/
sudo mkdir /mnt/target/boot
sudo mount /dev/sda1 /mnt/target/boot/
sudo apt-get update
sudo apt-get install rsync
```
Copy Raspbian to your USB with:
```
sudo rsync -ax --progress / /boot /mnt target
```
This will take a while to complete, so leave it to finish. Once done, you’ll need to copy the SSH host keys from
the microSD card to the USB device to maintain the connection via SSH. Enter the following a line at a time.
```
cd /mnt/target
sudo mount --bind /dev dev 
sudo mount --bind /sys sys
sudo mount --bind /proc proc
sudo chroot /mnt/target
rm /etc/ssh/ssh_host*
dpkg-reconfigure opensshserver
exit
sudo umount dev
sudo umount sys
sudo umount proc
```

### 6 PREPARE TO BOOT FROM USB
Before you reboot your Pi from the USB device, edit the **cmdline.txt** file again in the terminal:
```
sudo sed -i "s,root=/dev/mmcblk0p2,root=/dev sda2," /mnt/target/boot/ cmdline.txt
```
A similar change must also be made to _/etc/fstab_:
```
sudo sed -i “s,/dev/ mmcblk0p,/dev/sda,” /mnt/target/etc/fstab
```
You’re now ready to unmount the filesystem:
```
cd ~
sudo umount /mnt/target/boot
sudo umount /mnt/target
```
At this stage, you can enter the poweroff command to shut down your Pi. Once the lights are off, disconnect the power
supply and remove the microSD card. A few minutes later, you can reconnect the power and boot your Pi — from the USB
device !  
Your microSD card is now guaranteed a much longer lifespan. You might retain the Raspbian image, however, for preparing
other Pis for USB booting in future. Better still, this means that you can have as much storage as possible for your
Raspberry Pi. USB flash usually stops around the 512GB capacity (although there are larger devices) while mechanical
hard disk drives can potentially add terabytes of storage to your Pi. Alternatively, an SSD device will speed things
up considerably.

### 7 BOOT RASPBIAN ACROSS YOUR NETWORK
Booting from USB can be taken to the next level — network boot. Using a Pi as a server, you can set up a Raspberry Pi
3 with Raspbian Lite and set it to initially boot from USB. With the server and new client configured correctly, the
Pi can boot from the network, again reducing the impact on the SD card.  
- On your intended client, follow the previous steps up to the point of removing program_usb_boot_mode from
`/boot/config.txt`, then running the poweroff command.
- Next, remove the SD card and insert it into the Pi you’ll be using as a server. Boot this device, then run
`sudo raspi-config`. This will open the configuration options. Select the Expand Filesystem option. Then create
a copy of the root filesystem:
```
sudo mkdir -p /nfs/client1
sudo apt-get install rsync
sudo rsync -xa --progress --exclude /nfs /nfs/client1
```
This will take a while to complete, so be patient!

### 8 FIND THE ADDRESSES
Continue by maintaining your connection via SSH, by regenerating the SSH host keys:
```
cd /nfs/client1
sudo mount --bind /dev dev
sudo mount --bind /sys sys
sudo mount --bind /proc proc
sudo chroot . rm /etc/ssh/ssh_host_*
dpkg-reconfigure opensshserver
exit
sudo umount dev
sudo umount sys
sudo umount proc
```
Then find the address of your router. If you don’t know this, run:
```
ip route | grep default | awk ‘{print $3}’
```
Check your Pi’s own IP address with:
```
ip -4 addr show dev eth0 | grep inet
```
Then use `cat /etc/resolv.conf` to find the address of your DNS server. You should now have your device’s IP,
broadcast and DNS server addresses, so note these down. Run `sudo nano /etc/network/interfaces`
and edit the line `iface eth0 inet manual` so that it reads:
```
auto eth0
iface eth0
inet static address [YOUR_ IP_ ADDRESS]
netmask 255.255.255.0
gateway [YOUR_ BROADCAST_ ADDRESS]
```
Press **Ctrl-X** to save and exit. To make this work, you’ll need to disable DHCP networking, so run the
following and then reboot your Pi:
```
sudo systemctl disable dhcpcd
sudo systemctl enable networking
```

### 9 CONFIGURE YOUR SERVER’S NETWORK SETTINGS
Enter the following with the DNS IP address you noted earlier.
```
echo "nameserver [YOUR_ NAMESERVER_ IP]" | sudo tee -a /etc/resolv.conf
```
Prevent changes to this with:
```
sudo chattr +i /etc/ resolv.conf
```
You then need to install some software:
```
sudo apt-get update
sudo apt-get install dnsmasq tcpdump
```
The dnsmasq tool can cause problems, so prevent this with:
```
sudo rm /etc/resolvconf/ update.d/dnsmasq
```
Reboot again, then run `tcpdump` to detect DHCP from the client Pi.
```
sudo tcpdump -i eth0 port bootpc -v
```
At this stage, connect the client Pi to the network via Ethernet, and connect the power cable. 
After 10 seconds, the LEDs should light, and a packet from the client will be received by the server
and displayed in the tcpdump tool. Press **Ctrl-C** to exit, _then enter_:
```
sudo echo | sudo tee /etc/ dnsmasq.conf
sudo nano /etc/dnsmasq.conf
```
Delete everything in the file and add:
```
port=0
dhcp-range=[YOUR_ BROADCAST_ IP],proxy log-dhcp enable-tftp
tftp-root=/tftpboot
pxe-service=0,"Raspberry Pi Boot"
```
Next, create a new directory, **tftpboot**:
```
sudo mkdir     /tftpboot
sudo chmod 777 /tftpboot
sudo systemctl enable dnsmasq.service
sudo systemctl restart dnsmasq.service
```

### 10 PREPARE FOR NETWORK BOOT
Continue by monitoring the dnsmasq log with:
```
tail -f /var/log/daemon. log
```
If working, a _'not found'_ message will be displayed. Copy the necessary files with 
`cp -r / boot/* /tftpboot`. Then restart dnsmasq with `sudo systemctl restart dnsmasq` and the client Pi is ready to
boot the root filesystem and then boot from the network. The `/nfs/client1` filesystem must now be exported:
```
sudo apt-get install nfs-kernel-server
echo "/nfs/client1 *(rw,sync,no_subtree,check,no_root_squash)" | sudo tee -a /etc/ exports
sudo systemctl enable rpcbind
sudo systemctl restart rpcbind
sudo systemctl enable nfs-kernel-server
sudo systemctl restart nfs-kernel-server
```
Next, edit `/tftpboot/cmdline.txt`, changing the line beginning `root=` to:
```
root=/dev/nfs nfsroot=[YOUR_ DEVICE_ IP]:/nfs client1 rw ip=dhcp rootwait elevator=deadline
```
Open fstab with
`sudo nano / nfs/client1/etc/fstab` and remove the **/dev/mmcblkp1** and **/dev/mmcblkp2** lines. 
You’re done! Now start the client and wait for it to boot from the network.
This may be a little slower than what you’re used to (depending on your network speed), but will extend the life of
your Pi’s microSD card considerably.

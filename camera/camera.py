#!/usr/bin/env python
#
# Acquire image from builtin RaspberryPi camera
#       Straight forward script to test integrated camera
#       Use "apt install python3-picamera" to get packages
#
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/tmp/picture.jpg')
camera.stop_preview()

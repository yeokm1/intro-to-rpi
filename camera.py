#This code has not been tested. Reference: http://www.raspberrypi.org/documentation/usage/camera/python/README.md

import picamera
from time import sleep

#Get access to the camera
camera = picamera.PiCamera()

#Take a picture and save to "image.jpg"
camera.capture('image.jpg')


#Start preview
camera.start_preview()

#Show 5 seconds of preview
sleep(5)

#Stop preview
camera.stop_preview()

camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()


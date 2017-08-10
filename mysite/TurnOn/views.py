# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def TurnOn(request):
   from gpiozero import MotionSensor
   import picamera
   import time
   import datetime
   import MySQLdb
   import os.path
   import requests
   import os
   import RPi.GPIO as GPIO
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(4, GPIO.IN)

   pir = MotionSensor(4)
   db = MySQLdb.connect("localhost", "monitor", "password", "image")

   cursor = db.cursor()

   while True:
      if pir.motion_detected:
         camera = picamera.PiCamera()
         save_path = '/home/pi/mysite/personal/static'
         date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + '.jpg'
         complete = os.path.join(save_path, date)
         camera.resolution = (500, 400)      
         camera.capture(complete)
         query = "INSERT INTO images_images (filename) VALUES ('" + date + "')"
         cursor.execute(query)
         db.commit()
         camera.close()
         requests.post("https://maker.ifttt.com/trigger/snap_taken/with/key/cy66VEvYrBcNlpxh2dQE21")
         time.sleep(5)


   return render (request, 'personal/home.html')


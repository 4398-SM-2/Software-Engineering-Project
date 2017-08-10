# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here
def snapshot(request):
   import picamera
   import time
   import datetime
   import MySQLdb
   import os.path

   db = MySQLdb.connect("localhost", "monitor", "password", "image")
   cursor = db.cursor()
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

   return render (request, 'personal/home.html')

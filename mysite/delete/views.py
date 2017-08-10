# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def delete(request):
   import MySQLdb

   db = MySQLdb.connect("localhost", "monitor", "password", "image")
   cursor = db.cursor()
   query = "DELETE FROM images_images"
   cursor.execute(query)
   db.commit()
   return render (request, 'personal/home.html')

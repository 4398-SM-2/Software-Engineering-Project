# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def TurnOff(request):
   import RPi.GPIO as GPIO
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(4, GPIO.OUT)   
   GPIO.output(4, 0)

   return render (request, 'personal/home.html')

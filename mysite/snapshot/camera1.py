import picamera

class manualSnapshot:
   def cam(self):
      newPic = picamera.PiCamera()
      newPic.resolution = (500, 400)	
      newPic.capture('snapshot.jpg')

import picamera

#class manualSnapshot:
def cam():
   newPic = picamera.PiCamera()
   newPic.resolution = (500, 400)	
   newPic.capture('snapshot.jpg')
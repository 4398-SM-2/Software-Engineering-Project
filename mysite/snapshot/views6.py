import picamera

newPic = picamera.PiCamera()
newPic.resolution = (500, 400)	
newPic.capture('snapshot.jpg')
newPic.close()


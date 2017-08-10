https://github.com/4398-SM-2/Software-Engineering-Project

Group 4398 SM 2's project is security cam software, using the Respberry Pi, 
Raspberry Pi Module V2, and the PIR motion sensor.
The Pi hosts a web server, which deploys a web GUI that allows the user to 
send commands to the Pi, and shows the user all pictures captured by the Pi cam. 
The web GUI is built on the Django web framwork, and contains five apps.

All software was developed via ssh connection to the pi, then uploaded to github as
a completed project, ready for user install, where Django, Apache2 and Python
have already been set up. 

The one issue that we were not able to resolve, is that when the user turns off the camer from the GUI, 
then attempts to turn it back on, the web page displays an error message, but the script still succeeds 
at turning the camera back on, therefore functionaly, the button works.

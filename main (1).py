import ephem
import time
import sense_hat
from picamera import PiCamera
from time import sleep
from datetime import datetime
from sense_hat import SenseHat
import os
import datetime

#declares test as true
test = True
#declaring variable for SenseHat() & PiCamera()
sense = SenseHat()
camera = PiCamera()


name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   19036.09394694  .00001992  00000-0  38488-4 0  9999"
line2 = "2 25544  51.6434 298.1410 0005092 354.6679  85.0275 15.53235044154735"


iss = ephem.readtle(name, line1, line2)
# create a datetime variable to store the start time
start_time = datetime.datetime.now()
# create a datetime variable to store the current time
now_time = datetime.datetime.now()
#locate the iss position
iss.compute()

def came():
    
    now_time = datetime.datetime.now()
    camera.annotate_text = ("try camera:" + str(now_time) + " Lat: " + str(iss.sublat) + " Long: " + str(iss.sublong)) 
    camera.capture  ('/home/pi/image%s.jpg' % str(now_time) )
       
    
def sensors():
    
#iss_position 
    iss_ephem = ephem.FixedBody()
#declares_iss_observer
    iss_observer = ephem.Observer()
#works_azimuth   
    iss_ephem.compute(iss_observer)
    
    humidity = sense.get_humidity()
    temp = sense.get_temperature()
    press = sense.get_pressure()
    gyro = sense.get_gyroscope_raw()
    orient = sense.get_orientation_degrees()
    compass = sense.get_compass_raw()
    acc = sense.get_accelerometer_raw()
    
    file = open("/home/pi/data01.csv", "a")
    
    if os.stat("/home/pi/data01.csv").st_size == 0:
        file.write("Time Stamp,Latitude,Longitude,Humidity,Temperature,Pressure,Gyroscope Pitch, Gyroscope Yaw, Gyroscope Roll, Orientation X, orientation Y, orientation Z , Compass X, Compass Y, Compass Z, Acc X, Acc Y, Acc Z, Azimuth \n")
    
    file.write(str(now_time) + "," + str(iss.sublat) + "," + str(iss.sublong) + "," + str(humidity) + "," + str(temp) + "," + str(press) + "," + str(gyro) + "," + str(orient) + "," + str(compass) + "," + str(acc) + "," + str(iss_ephem.az) +"\n")
    time.sleep(1)
    file.close()

#declares image colours as b=blue, y=yellow, d=dark/none, w=white
b = [ 0,0,255]
y = [ 194,216,48]
d = [ 0,0,0]
w = [ 255,255,255]

image_1=[ 
        y,y,y,y,y,y,y,y,
        y,b,b,b,b,b,b,y,
        y,b,y,y,y,y,b,y,
        y,b,y,b,b,y,b,y,
        y,b,y,b,b,y,b,y,
        y,b,y,y,y,y,b,y,
        y,b,b,b,b,b,b,y,
        y,y,y,y,y,y,y,y,
        ]

image_2=[ 
        b,b,b,b,b,b,b,b,
        b,y,y,y,y,y,y,b,
        b,y,b,b,b,b,y,b,
        b,y,b,y,y,b,y,b,
        b,y,b,y,y,b,y,b,
        b,y,b,b,b,b,y,b,
        b,y,y,y,y,y,y,b,
        b,b,b,b,b,b,b,b,
        ]

finish_1=[
        w,w,d,d,w,w,d,d,
        w,w,d,d,w,w,d,d,
        d,d,w,w,d,d,w,w,
        d,d,w,w,d,d,w,w,
        w,w,d,d,w,w,d,d,
        w,w,d,d,w,w,d,d,
        d,d,w,w,d,d,w,w,
        d,d,w,w,d,d,w,w,
        ]
    
init_time = datetime.datetime.now()

#runs program until minutes = 178
while (now_time < start_time + datetime.timedelta(minutes=178)):
    now_time = datetime.datetime.now()
       
#updating image
    test = not test
    if test == True:
       sense.set_pixels(image_2)
    if test == False:
       sense.set_pixels(image_1)
   
    
#running program if sensors fail try camera
    try:
        sensors()
    
    except:
            sense.show_message("Sensor fail", scroll_speed = 0.09, text_colour = (0,0,255))
       #when minutes = 1 take photo
    if now_time >= init_time + datetime.timedelta(minutes=1):
        try:
            came()
            init_time = datetime.datetime.now()
             
        except:
             sense.show_message("Camera fail", scroll_speed = 0.09, text_colour = (0,0,255))

#shows finish flag when loop finishes
sense.set_pixels(finish_1)  

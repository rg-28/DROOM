import RPi.GPIO as GPIO
import time 
GPIO.setmode (GPIO.BCM)
TRIG = 17
ECHO = 27
print("Obstacle detection in progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:
    GPIO.output(TRIG,False)
    print ("waiting for the sensor detect any obstacle")
    time.sleep(2)

    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input (ECHO)==0:
        y = time.time()        
    while GPIO.input (ECHO)==1:
        x = time.time()

        
    z= (x-y)
    dist = z*17150
    dist = round(dist,2)

    if dist>2 and dist<20:
        print("obstacle detected!!!!\nAnd the distance is-:")
        print(dist)
        



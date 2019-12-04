import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from datetime import datetime

GPIO.setmode(GPIO.BCM)

TRIG1 = 4
ECHO1 = 18
TRIG2 = 22
ECHO2 = 24
RELAY1 = 17
RELAY2 = 27

maxTime = .5
threshold1 = 180
threshold2 = 70

distance1Arr = []
distance2Arr = []

GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.setup(RELAY1, GPIO.OUT)
GPIO.setup(RELAY2, GPIO.OUT)

GPIO.output(RELAY1, True)
GPIO.output(RELAY2, True)

#camera = PiCamera()

try:
    while True:

        GPIO.output(TRIG1, True)
        time.sleep(0.0001)
        GPIO.output(TRIG1, False)

        start = time.time()
        timeout = start + maxTime
        while GPIO.input(ECHO1) == False and start < timeout:
            start = time.time()

        end = time.time()
        timeout = end + maxTime
        while GPIO.input(ECHO1) == True and end < timeout:
            end = time.time()

        sig_time = end-start
        distance1 = sig_time / 0.000058

#	    if distance1Arr[0] >= threshold1 and distance1Arr[1] >= threshold1 and distance1Arr[2] >= threshold1:
#	        GPIO.output(RELAY2, True)

        time.sleep(0.05)

        GPIO.output(TRIG2, True)
        time.sleep(0.0001)
        GPIO.output(TRIG2, False)

        start2 = time.time()
        timeout2 = start2 + maxTime
        while GPIO.input(ECHO2) == False and start2 < timeout2:
            start2 = time.time()

        end2 = time.time()
        timeout2 = end2 + maxTime
        while GPIO.input(ECHO2) == True and end2 < timeout2:
            end2 = time.time()

        sig_time2 = end2-start2
        distance2 = sig_time2 / 0.000058

        print('Distance1: {} cm ---- Distance2: {} cm'.format(distance1, distance2))

        distance1Arr.append(distance1)
        distance2Arr.append(distance2)

        if len(distance1Arr) > 4:
            if distance1Arr[0] >= threshold1 and distance1Arr[1] >= threshold1 and distance1Arr[2] >= threshold1 and distance1Arr[3] >= threshold1 and distance2Arr[0] >= threshold2 and distance2Arr[1] >= threshold2 and distance2Arr[2] >= threshold2 and distance2Arr[3] >= threshold2:
                GPIO.output(RELAY1, True)
                GPIO.output(RELAY2, True)
            distance1Arr.pop(0)
            distance2Arr.pop(0)

        #if sensor inside is tripped, turn on both lights
            if distance1Arr[0] < threshold1 and distance1Arr[1] < threshold1 and distance1Arr[2] < threshold1 and distance1Arr[3] < threshold1:
                GPIO.output(RELAY1, False)
                GPIO.output(RELAY2, False)
                time.sleep(60)
#if sensor closest to the door is tripped, just turn on inside light
            if distance2Arr[0] < threshold2 and distance2Arr[1] < threshold2 and distance2Arr[2] < threshold2 and distance2Arr[3] < threshold2:
                GPIO.output(RELAY2, False)
                time.sleep(45)
#               now = datetime.now()
#               camera.start_preview() #probably not needed
#               camera.start_recording('smb://readyshare/roach media/securityFootage' + now.strftime("%m/%d/%Y, %H:%M:%S") + '.h264')
#               time.sleep(10)
#               camera.stop_recording()
#               camera.stop_preview() #probably not needed
        time.sleep(.05)
except Exception as e:
    print(e)
    GPIO.cleanup()

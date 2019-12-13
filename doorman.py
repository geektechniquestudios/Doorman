import RPi.GPIO as GPIO
import time
import subprocess
from picamera import PiCamera
from datetime import datetime

GPIO.setmode(GPIO.BCM)

#GPIO Pin values
TRIG1 = 4
ECHO1 = 18
TRIG2 = 22
ECHO2 = 24
RELAY1 = 17
RELAY2 = 27

#constants @todo rewrite these in all caps everywhere in program
maxTime = .5
threshold1 = 210
threshold2 = 65
sleepDur = 0.02

#for testing
#threshold1 = 10
#threshold2 = 10

#arrays for fault tolerance
distance1Arr = []
distance2Arr = []

#GPIO setup
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.setup(RELAY1, GPIO.OUT)
GPIO.setup(RELAY2, GPIO.OUT)

#make sure relay is in open state
GPIO.output(RELAY1, True)
GPIO.output(RELAY2, True)

#setup pi camera
camera = PiCamera()
camera.rotation = 270

#method for ultrasonic sensors
def getDistance(trig, echo):
    GPIO.output(trig, True)
    time.sleep(0.0001)
    GPIO.output(trig, False)

    start = time.time()
    timeout = start + maxTime
    while GPIO.input(echo) == False and start < timeout:
        start = time.time()

    end = time.time()
    timeout = end + maxTime
    while GPIO.input(echo) == True and end < timeout:
        end = time.time()

    sig_time = end-start
    distance = sig_time / 0.000058

    time.sleep(sleepDur)
    return distance

try:
    while True:

        distance1 = getDistance(TRIG1, ECHO1)
        distance2 = getDistance(TRIG2, ECHO2)

        print('Distance1: {} cm ---- Distance2: {} cm'.format(distance1, distance2))

        #add new values to arrays
        distance1Arr.append(distance1)
        distance2Arr.append(distance2)

        #makes sure at least 4 lines have been printed before using array
        if len(distance1Arr) > 4:
            #if distance thresholds are cleared, turn on the light
            if distance1Arr[0] >= threshold1 and distance1Arr[1] >= threshold1 and distance1Arr[2] >= threshold1 and distance1Arr[3] >= threshold1 and distance2Arr[0] >= threshold2 and distance2Arr[1] >= threshold2 and distance2Arr[2] >= threshold2 and distance2Arr[3] >= threshold2:
                GPIO.output(RELAY1, True)
                GPIO.output(RELAY2, True)
            #maintain arrays by removing old values
            distance1Arr.pop(0)
            distance2Arr.pop(0)

            #if sensor inside is tripped, turn on both lights #may consider recording here too
            if distance1Arr[0] < threshold1 and distance1Arr[1] < threshold1 and distance1Arr[2] < threshold1 and distance1Arr[3] < threshold1:
                GPIO.output(RELAY1, False)
                GPIO.output(RELAY2, False)
                time.sleep(60)
            #if sensor closest to the door is tripped, turn on inside light only
            if distance2Arr[0] < threshold2 and distance2Arr[1] < threshold2 and distance2Arr[2] < threshold2 and distance2Arr[3] < threshold2:
                GPIO.output(RELAY2, False)
                now = datetime.now()
                camera.start_preview()
                recordingFilename = 'security' + now.strftime("_%m-%d-%Y_%H:%M:%S") + '.h264'
                recordingPath = '/home/pi/Desktop/FrontDoorSensor/doorcam/'
                camera.start_recording(recordingPath + recordingFilename)

                time.sleep(10)
                camera.stop_recording()
                camera.stop_preview()

                #scp video to other computer @todo add ip of new rpi and make security_footage folder
                try:
                    subprocess.call(['scp ' + recordingPath + recordingFilename + ' pi@10.0.0.4:~/Desktop/security_footage/' + recordingFilename], shell = True)
                    subprocess.call(['rm ' + recordingPath + recordingFilename], shell = True)
                    print('Local file deleted')
                except:
                    print('Failed to backup security footage to server')
                time.sleep(35)
        time.sleep(sleepDur)
except Exception as e:
    print(e)
    GPIO.cleanup()
finally:
    GPIO.cleanup()

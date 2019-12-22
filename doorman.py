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
RELAY1 = 17 #outside
RELAY2 = 27 #inside

#global constants
MAXTIME = .5
THRESHOLD1 = 210
THRESHOLD2 = 65
SLEEPDUR = 0.02
recordingPath = '/home/pi/Desktop/FrontDoorSensor/doorcam/'
tickCounter = 0 # 1 tick ~= 80ms || 100 ticks ~= 8 seconds

#arrays for fault tolerance
distance1Arr = [300, 300, 300, 300]
distance2Arr = [300, 300, 300, 300]

#GPIO setup
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.setup(RELAY1, GPIO.OUT)
GPIO.setup(RELAY2, GPIO.OUT)

#make sure relay is in open state on boot
GPIO.output(RELAY1, True)
GPIO.output(RELAY2, True)

#make lights flicker so I know if something goes wrong
def lightFlicker(x):
    for i in range(x):
        GPIO.output(RELAY2, True)
        time.sleep(1)
        GPIO.output(RELAY2, False)
        time.sleep(1)

#method for ultrasonic sensors' distances
def getDistance(trig, echo):
    GPIO.output(trig, True)
    time.sleep(0.0001)
    GPIO.output(trig, False)

    start = time.time()
    timeout = start + MAXTIME
    while GPIO.input(echo) == False and start < timeout:
        start = time.time()

    end = time.time()
    timeout = end + MAXTIME
    while GPIO.input(echo) == True and end < timeout:
        end = time.time()

    sig_time = end-start
    return sig_time / 0.000058

def recordVideo():
    global recordingPath
    camera = PiCamera()
    camera.rotation = 270
    now = datetime.now()
    camera.start_preview(fullscreen=False, window = (170, 485, 640, 480))
    recordingFilename = 'security' + now.strftime("_%m-%d-%Y_%H:%M:%S") + '.h264'
    camera.start_recording(recordingPath + recordingFilename)
    print('Now Recording')
    time.sleep(30)
    camera.stop_recording()
    camera.stop_preview()
    camera.close()

    #scp video to other computer
    try:
        print('Requesting file transfer')
        subprocess.call(['scp ' + recordingPath + recordingFilename + ' pi@10.0.0.6:/media/pi/security_drive/' + recordingFilename], shell = True)
        print('Sending video to file server')
        subprocess.call(['rm ' + recordingPath + recordingFilename], shell = True)
        print('Local file deleted')
    except:
        print('Failed to backup security footage to server')
        lightFlicker(3)


def setState(state):
    global tickCounter
    global inOnVar

    if state == 'off':
        GPIO.output(RELAY1, True)
        GPIO.output(RELAY2, True)
    elif state == 'inOn':
        GPIO.output(RELAY2, False)
        tickCounter = 800 #about one min
    elif state == 'outOn':
        GPIO.output(RELAY1, False)
        tickCounter = 800
    else:
        state = 'off'
        setState(state)

try:
    while True:
        #get distance from sensors
        distance1 = getDistance(TRIG1, ECHO1)
        time.sleep(SLEEPDUR)
        distance2 = getDistance(TRIG2, ECHO2)

        print('Distance1: {} cm ---- Distance2: {} cm ---- TickCounter: {}'.format(distance1, distance2, tickCounter))

        #add new values to arrays
        distance1Arr.append(distance1)
        distance2Arr.append(distance2)
        #maintain arrays by removing old values
        distance1Arr.pop(0)
        distance2Arr.pop(0)

        #if distance thresholds are cleared, turn off the light
        if tickCounter <= 0 and distance1Arr[0] >= THRESHOLD1 and distance1Arr[1] >= THRESHOLD1 and distance1Arr[2] >= THRESHOLD1 and distance1Arr[3] >= THRESHOLD1 and distance2Arr[0] >= THRESHOLD2 and distance2Arr[1] >= THRESHOLD2 and distance2Arr[2] >= THRESHOLD2 and distance2Arr[3] >= THRESHOLD2:
            setState('off')

        #if sensor inside is tripped, turn on inside light
        if distance1Arr[0] < THRESHOLD1 and distance1Arr[1] < THRESHOLD1 and distance1Arr[2] < THRESHOLD1 and distance1Arr[3] < THRESHOLD1:
            setState('inOn')

        #outside sensor tripped: if inside light is off, turn it on, otherwise, turn on outside light
        if distance2Arr[0] < THRESHOLD2 and distance2Arr[1] < THRESHOLD2 and distance2Arr[2] < THRESHOLD2 and distance2Arr[3] < THRESHOLD2:
            if tickCounter == 0:
                setState('inOn')
            else:
                setState('outOn')
            recordVideo()

        if tickCounter > 0:
            tickCounter = tickCounter - 1
        time.sleep(SLEEPDUR)
except Exception as e:
    print(e)
    lightFlicker(1)
finally:
    GPIO.cleanup()
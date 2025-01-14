import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(0, GPIO.OUT)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

def digit():
    GPIO.output(21, True)
    GPIO.output(20, True)
    GPIO.output(26, True)
    GPIO.output(19, True)
    GPIO.output(13, True)
    GPIO.output(6, True)
    GPIO.output(1, False)
    time.sleep(1)
    GPIO.output(1, True)
    GPIO.output(7, False)
    time.sleep(1)
    GPIO.output(7, True)
    GPIO.output(8, False)
    time.sleep(1)
    GPIO.output(8, True)
    
try:
    while True:
        digit()
        time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()

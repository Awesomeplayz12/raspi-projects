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

def digit(digit):
    GPIO.output(21, True)
    GPIO.output(20, True)
    GPIO.output(26, True)
    GPIO.output(19, True)
    GPIO.output(13, True)
    GPIO.output(6, True)
    GPIO.output(digit, False)
    time.sleep(1)
    GPIO.output(digit, True)
    
try:
    while True:
        digit(7)
        time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()

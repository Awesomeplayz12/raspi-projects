import sys
import RPi.GPIO as GPIO
import time

triggerPIN = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPIN, GPIO.OUT)

buzzer = GPIO.PWM(triggerPIN, 100)
buzzer.start(10)

time.sleep(1)
GPIO.cleanup()
sys.exit

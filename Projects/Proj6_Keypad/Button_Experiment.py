import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(16, GPIO.IN)

GPIO.output(19, True)

while True:
    time.sleep(0.5)
    if GPIO.input(16) == 1:
        print("Nana boomer")
            
    if GPIO.input(16) == 0:
        print("Nana is a babbay")
 

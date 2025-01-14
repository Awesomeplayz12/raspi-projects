import RPi.GPIO as GPIO
import time

servoPIN = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start(5)

i = input("Enter the degrees you want the motor to rotate")

p.stop()
GPIO.cleanup()

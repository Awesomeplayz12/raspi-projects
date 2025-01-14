import RPi.GPIO as GPIO
import time

servoPIN = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) 
p.start(2.5)
try:
  while True:
    p.ChangeDutyCycle(5)
    time.sleep(0.25)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.25)
    p.ChangeDutyCycle(20)
    time.sleep(0.25)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.25)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

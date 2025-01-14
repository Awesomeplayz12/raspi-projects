import RPi.GPIO as GPIO
import time

servoPIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start(5)

print("How many degrees do you want the motor to spin?")
i = input("1. 180 degrees \n2. 90 degrees \n3. 45 degrees \n4. Exit \n")
    
while i != "4":
    
    if i == "1":
        #180 degree spin
        time.sleep(0.5)
        p.ChangeDutyCycle(15)
        time.sleep(1)
            
    if i == "2":
        #90 degree spin
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        time.sleep(1)
        
    if i == "3":
        #45 degree spin
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
    
    #Brings to starting postition
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(1)
    
    print("How many degrees do you want the motor to spin?")
    i = input("1. 180 degrees \n2. 90 degrees \n3. 45 degrees \n4. Exit \n")

p.stop()
GPIO.cleanup()

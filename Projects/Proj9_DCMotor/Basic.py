import RPi.GPIO as GPIO
import time

def speed_control(direction, speed):
    for x in range(0,49):
        if b == "1": 
            forward()
                
        if b == "2":
            backward()
            
        t = speed * 0.001
        u = 0.1 - t
        
        time.sleep(t)
        off()
        time.sleep(u)

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(20, False)
    GPIO.output(21, False)
    
def forward():
    GPIO.output(20, True)
    GPIO.output(21, False)

def backward():
    GPIO.output(20, False)
    GPIO.output(21, True)
    
def off():
    GPIO.output(20, False)
    GPIO.output(21, False)
       
init()

while True:
    b = input("1. Forward \n2. Backward \n3. Off \n4. Exit \n")

    if b == "1":
        off()
        time.sleep(1)
        speed_control(forward, 100)
        
    if b == "2":
        off()
        time.sleep(1)
        speed_control(backward, 100)
    
    if b == "3":
        off()
        time.sleep(1)
        
    if b == "4":
        off()
        time.sleep(1)
        
        break

    else:
        time.sleep(1)

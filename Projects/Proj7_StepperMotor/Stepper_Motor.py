import RPi.GPIO as GPIO  
import time  

IN1 = 2    
IN2 = 3  
IN3 = 4  
IN4 = 14  

def setStep(w1, w2, w3, w4):  
    GPIO.output(IN1, w1)  
    GPIO.output(IN2, w2)  
    GPIO.output(IN3, w3)  
    GPIO.output(IN4, w4)  

def stop():  
    setStep(0, 0, 0, 0)  

def forward(delay, steps):    
    for i in range(0, steps):  
        setStep(1, 0, 0, 0)  
        time.sleep(delay)  
        setStep(0, 1, 0, 0)  
        time.sleep(delay)  
        setStep(0, 0, 1, 0)  
        time.sleep(delay)  
        setStep(0, 0, 0, 1)  
        time.sleep(delay)  

def backward(delay, steps):    
    for i in range(0, steps):  
        setStep(0, 0, 0, 1)  
        time.sleep(delay)  
        setStep(0, 0, 1, 0)  
        time.sleep(delay)  
        setStep(0, 1, 0, 0)  
        time.sleep(delay)  
        setStep(1, 0, 0, 0)  
        time.sleep(delay)  

def setup():  
    GPIO.setwarnings(False)  
    GPIO.setmode(GPIO.BCM)       
    GPIO.setup(2, GPIO.OUT)       
    GPIO.setup(3, GPIO.OUT)  
    GPIO.setup(4, GPIO.OUT)  
    GPIO.setup(14, GPIO.OUT)  

def loop():
    a = "0"
    while a != "3":
        a = input("1. Clockwise \n2. Counterclockwise \n3. Exit \n")
        if a == "1":
            b = "0"
            while b != "6":
                b = input("1. 45 degrees \n2. 90 degrees \n3. 180 degrees \n4. 360 degrees \n5. Single step \n6. Exit \n")
                if b == "1":
                    forward(0.005, 64)
                if b == "2":
                    forward(0.005, 128)
                if b == "3":
                    forward(0.005, 256)
                if b == "4":
                    forward(0.005, 512)
                if b == "5":
                    forward(0.005, 8)
        if a == "2":
            b = "0"
            while b != "6":
                b = input("1. 45 degrees \n2. 90 degrees \n3. 180 degrees \n4. 360 degrees \n5. Single Step \n6. Exit \n")
                if b == "1":
                    backward(0.005, 64)
                if b == "2":
                    backward(0.005, 128)
                if b == "3":
                    backward(0.005, 256)
                if b == "4":
                    backward(0.005, 512)
                if b == "5":
                    backward(0.005, 8)

def destroy():  
	GPIO.cleanup()             

if __name__ == '__main__':      
    setup()  
    try:  
        loop()  
    except KeyboardInterrupt:  
            destroy()  

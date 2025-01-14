import RPi.GPIO as GPIO
from queue import Queue
import threading
import time
from pynput import keyboard

q = Queue(maxsize = 10)
m = 100

def speed_control(direction, speed):
    for x in range(0,49):
        if direction == "forward":   
            forward()
                
        if direction == "backward":
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

print("Up arrow - Forward \nDown arrow - Backward \nRight arrow - Speed increase \nLeft arrow - Speed decrease \nSpacebar - Off \nEscape - Exit")

def execution_thread():
    while True:
        if q.qsize() > 0:
            b = q.get()
            
            if b == "1":
                off()
                time.sleep(1)
                speed_control("forward", m)
                
            if b == "2":
                off()
                time.sleep(1)
                speed_control("backward", m)

            if b == "3":
                off()
                time.sleep(1)
                m -= 10

                if m < 70:
                    m += 10
            
            if b == "4":
                off()
                time.sleep(1)
                m += 10

                if m > 100:
                    m -= 10

            if b == "5":
                off()
                time.sleep(1)
                
            if b == "6":
                off()
                time.sleep(1)
                
                break

    listener.join()

def on_hold(key):
    if key == key.up:
        q.put("1")
        time.sleep(0.1)
    
    elif key == key.down:
        q.put("2")
        time.sleep(0.1)
        
    elif key == key.left:
        q.put("3")
        time.sleep(0.1)
       
    elif key == key.right:
        q.put("4")
        time.sleep(0.1)
        
    elif key == key.space:
        q.put("5")
        time.sleep(0.1)
        
    elif key == key.esc:
        q.put("6")
        time.sleep(0.1)

    else:
        print("cringe")

if __name__ == "__main__":
    execution_thread = threading.Thread(target = execution_thread)

    execution_thread.start()

with keyboard.Listener() as listener:
    on_hold = on_hold
    listener.join()

execution_thread.join()

import RPi.GPIO as GPIO
import time
    
def on0():
    tup1 = [21,20,26,19,13,6,5,0]
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[2], True)
    GPIO.output(tup1[3], True)
    GPIO.output(tup1[4], True)
    GPIO.output(tup1[5], True)
    
    return
    
def on1():
    tup1 = [21,20,26,19,13,6,5,0]
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[2], True)
    
    return

def on2():
    tup1 = [21,20,26,19,13,6,5,0]
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[6], True)
    GPIO.output(tup1[4], True)
    GPIO.output(tup1[3], True)
    
    return
    
def on3():
    tup1 = [21,20,26,19,13,6,5,0]
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[6], True)
    GPIO.output(tup1[2], True)
    GPIO.output(tup1[3], True)
    
    return

def on4():
    tup1 = [21,20,26,19,13,6,5,0]
    GPIO.output(tup1[5], True)
    GPIO.output(tup1[6], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[2], True)
    
    return

def on5():
    tup1 = [21,20,26,19,13,6,5,0]
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[5], True)
    GPIO.output(tup1[6], True)
    GPIO.output(tup1[2], True)
    GPIO.output(tup1[3], True)
    
    return

def on6():
    tup1 = [21,20,26,19,13,6,5,0]
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[5], True)
    GPIO.output(tup1[4], True)
    GPIO.output(tup1[3], True)
    GPIO.output(tup1[2], True)
    GPIO.output(tup1[6], True)
    
    return

def on7():
    tup1 = [21,20,26,19,13,6,5,0]
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[2], True)
    
    return

def on8():
    tup1 = [21,20,26,19,13,6,5,0]
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[2], True)
    GPIO.output(tup1[3], True)
    GPIO.output(tup1[4], True)
    GPIO.output(tup1[5], True)
    GPIO.output(tup1[6], True)
    
    return

def on9():
    tup1 = [21,20,26,19,13,6,5,0]
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[2], True)
    GPIO.output(tup1[3], True)
    GPIO.output(tup1[5], True)
    GPIO.output(tup1[6], True)
    
    return
    
def off():
    tup1 = [21,20,26,19,13,6,5,0]
    tup2 = [1,7,8,25]
    GPIO.output(tup1[0], False)
    GPIO.output(tup1[1], False)
    GPIO.output(tup1[2], False)
    GPIO.output(tup1[3], False)
    GPIO.output(tup1[4], False)
    GPIO.output(tup1[5], False)
    GPIO.output(tup1[6], False)
    GPIO.output(tup1[7], False)
    GPIO.output(tup2[0], True)
    GPIO.output(tup2[1], True)
    GPIO.output(tup2[2], True)
    GPIO.output(tup2[3], True)
    
    return

def check():
    GPIO.output(2, True)
    time.sleep(0.00001)
    GPIO.output(2, False)
    while not GPIO.input(3):
        pass
    t1 = time.time()
    while GPIO.input(3):
        pass
    t2 = time.time()
    a = (((t2 - t1) * 340 / 2) * 100) * 10
    b = int(a)
    c = float(b)
    d = b / 10
    print(d)
    
    e = d * 10
    t = int(e)
    m = t % 10
    q = t / 10
    t = q % 10
    n = int(t)
    r = q / 10
    u = r % 10
    o = int(u)
    s = r / 10
    v = s % 10
    p = int(v)
    
    print(p,o,n,m)
    
    tup1 = [21,20,26,19,13,6,5,0]
    tup2 = [1,7,8,25]
    tup3 = [p,o,n,m]
    
    for x in range(250):
        for w in range(4):
            if tup3[w] == 0:
                GPIO.output(tup2[w], False)
                on0()
                time.sleep(0.001)
                off()
                
            if tup3[w] == 1:
                GPIO.output(tup2[w], False)
                on1()
                time.sleep(0.001)
                off()
                
            if tup3[w] == 2:
                GPIO.output(tup2[w], False)
                on2()
                time.sleep(0.001)
                off()
                
            if tup3[w] == 3:
                GPIO.output(tup2[w], False)
                on3()
                time.sleep(0.001)
                off()
                
            if tup3[w] == 4:
                GPIO.output(tup2[w], False)
                on4()
                time.sleep(0.001)
                off()
                
            if tup3[w] == 5:
                GPIO.output(tup2[w], False)
                on5()
                time.sleep(0.001)
                off()
                
            if tup3[w] == 6:
                GPIO.output(tup2[w], False)
                on6()
                time.sleep(0.001)
                off()
                
            if tup3[w] == 7:
                GPIO.output(tup2[w], False)
                on7()
                time.sleep(0.001)
                off()
                
            if tup3[w] == 8:
                GPIO.output(tup2[w], False)
                on8()
                time.sleep(0.001)
                off()
                
            if tup3[w] == 9:
                GPIO.output(tup2[w], False)
                on9()
                time.sleep(0.001)
                off()
                
            if tup2[w] == 7:
                GPIO.output(tup1[7], True)
    
    return
 
def init():
    GPIO.setwarnings(False)    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.IN)
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
    time.sleep(1)

    tup1 = [21,20,26,19,13,6,5,0]
    tup2 = [1,7,8,25]

    for y in range(8):
        GPIO.output(tup1[y], False)
    for z in range(4):
        GPIO.output(tup2[z], True)
        
    return

try:
    init()
    while True:
        check()
        time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
        

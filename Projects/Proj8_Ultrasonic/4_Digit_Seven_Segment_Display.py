import RPi.GPIO as GPIO
import time

def init():
    
    tup1 = (21,20,26,19,13,6,5,0)
    tup2 = (1,7,8,25)
    a = 0
    b = 0
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    
    for x in range(8):
        GPIO.setup(tup1[a], GPIO.OUT)
        GPIO.output(tup1[a], False)
        a = a + 1
    a = a - 8
    
    for x in range(4):
        GPIO.setup(tup2[b], GPIO.OUT)
        GPIO.output(tup2[b], True)
        b = b + 1
    b = b - 4

    return
    
def testdigitsegment(digit, segment):
    
    GPIO.setup(digit, GPIO.OUT)
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(digit, False)
    GPIO.output(segment, True)
    time.sleep(0.25)
    GPIO.output(digit, True)
    GPIO.output(segment, False)
    
    return
    
def testdigitnumber(digit, number):
    
    GPIO.output(digit, False)
    
    if number == 0:
        on0()
        time.sleep(1)
        off()
        GPIO.output(digit, True)
        
    if number == 1:
        on1()
        time.sleep(1)
        off()
        GPIO.output(digit, True)
        
    if number == 2:
        on2()
        time.sleep(1)
        off()
        GPIO.output(digit, True)

    if number == 3:
        on3()
        time.sleep(1)
        off()
        GPIO.output(digit, True)

    if number == 4:
        on4()
        time.sleep(1)
        off()
        GPIO.output(digit, True)
        
    if number == 5:
        on5()
        time.sleep(1)
        off()
        GPIO.output(digit, True)

    if number == 6:
        on6()
        time.sleep(1)
        off()
        GPIO.output(digit, True)
        
    if number == 7:
        on7()
        time.sleep(1)
        off()
        GPIO.output(digit, True)
        
    if number == 8:
        on8()
        time.sleep(1)
        off()
        GPIO.output(digit, True)

    if number == 9:
        on9()
        time.sleep(1)
        off()
        GPIO.output(digit, True)
        
    return

def on0():
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[2], True)
    GPIO.output(tup1[3], True)
    GPIO.output(tup1[4], True)
    GPIO.output(tup1[5], True)
    
    return
    
def on1():
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[2], True)
    
    return

def on2():
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[6], True)
    GPIO.output(tup1[4], True)
    GPIO.output(tup1[3], True)
    
    return
    
def on3():
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[6], True)
    GPIO.output(tup1[2], True)
    GPIO.output(tup1[3], True)
    
    return

def on4():
    GPIO.output(tup1[5], True)
    GPIO.output(tup1[6], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[2], True)
    
    return

def on5():
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[5], True)
    GPIO.output(tup1[6], True)
    GPIO.output(tup1[2], True)
    GPIO.output(tup1[3], True)
    
    return

def on6():
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[5], True)
    GPIO.output(tup1[4], True)
    GPIO.output(tup1[3], True)
    GPIO.output(tup1[2], True)
    GPIO.output(tup1[6], True)
    
    return

def on7():
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[2], True)
    
    return

def on8():
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[2], True)
    GPIO.output(tup1[3], True)
    GPIO.output(tup1[4], True)
    GPIO.output(tup1[5], True)
    GPIO.output(tup1[6], True)
    
    return

def on9():
    GPIO.output(tup1[0], True)
    GPIO.output(tup1[1], True)
    GPIO.output(tup1[2], True)
    GPIO.output(tup1[3], True)
    GPIO.output(tup1[5], True)
    GPIO.output(tup1[6], True)
    
    return
    
def off():
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
        
def digitinput():
    l = input("Enter a 4 digit integer \n")
    t = int(l)
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
    
    tup3 = [p,o,n,m]
    x = 3

    if t >= 10000:
        print("Please enter a 4 digit integer.")
    
    for z in range(250):
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
            
try:
    tup1 = (21,20,26,19,13,6,5,0)
    tup2 = (1,7,8,25)
    k = 0
    
    init()
    i = "0"
    while True:
        i = input("Which one will you do? \n1. Diagnostic Test \n2. Digit Display \n3. Digit Input \n")
        
        if i == "1":
            j = "0"
            j = input("Which digit do you want? \n1. Digit 1 \n2. Digit 2 \n3. Digit 3 \n4. Digit 4 \n")
            
            if j == "1":
                for x in range(8):
                    testdigitsegment(tup2[0],tup1[k])
                    k = k + 1
                    time.sleep(0.25)
                k = k - 8
            if j == "2":
                for x in range(8):
                    testdigitsegment(tup2[1],tup1[k])
                    k = k + 1
                    time.sleep(0.25)
                k = k - 8
            if j == "3":
                for x in range(8):
                    testdigitsegment(tup2[2],tup1[k])
                    k = k + 1
                    time.sleep(0.25)
                k = k - 8
            if j == "4":
                for x in range(8):
                    testdigitsegment(tup2[3],tup1[k])
                    k = k + 1
                    time.sleep(0.25)
                k = k - 8
                
        if i == "2":
            j = "0"
            j = input("Which number do you want displayed? \n0 \n1 \n2 \n3 \n4 \n5 \n6 \n7 \n8 \n9 \n")
            
            for x in range(4):    
                testdigitnumber(tup2[k],int(j))
                k = k + 1
                time.sleep(1)
            k = k - 4
            
        if i == "3":
            digitinput()
                
except KeyboardInterrupt:
    GPIO.cleanup()

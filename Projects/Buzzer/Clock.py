from gpiozero import LED
import time
from datetime import datetime
import re
import threading

a = LED(2)
b = LED(3)
c = LED(4)
d = LED(14)
e = LED(15)
f = LED(18)
g = LED(17)
d4 = LED(27)
d3 = LED(22)
d2 = LED(23)
d1 = LED(24)
dp = LED(10)
active_on = LED(21)

def off():
    a.off()
    b.off()
    c.off()
    d.off()
    e.off()
    f.off()
    g.off()
    d1.on()
    d2.on()
    d3.on()
    d4.on()
    dp.off()
    
def on0():
    f.on()
    e.on()
    d.on()
    c.on()
    b.on()
    a.on()
     
def on1():
    b.on()
    c.on()
    
def on2():
    a.on()
    b.on()
    g.on()
    e.on()
    d.on()

def on3():
    a.on()
    b.on()
    g.on()
    c.on()
    d.on()
    
def on4():
    f.on()
    g.on()
    b.on()
    c.on()

def on5():
    a.on()
    f.on()
    g.on()
    d.on()
    c.on()

def on6():
    a.on()
    f.on()
    e.on()
    d.on()
    c.on()
    g.on()
    
def on7():
    a.on()
    b.on()
    c.on()
    
def on8():
    a.on()
    f.on()
    g.on()
    c.on()
    d.on()
    e.on()
    b.on()
    
def on9():
    a.on()
    f.on()
    g.on()
    b.on()
    c.on()
    d.on()
    
off()
active_on.on()

def thread_1():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H%M")

        t = int(current_time)
        digit_four = t % 10
        q = t / 10
        t = q % 10
        digit_three = int(t)
        r = q / 10
        u = r % 10
        digit_two = int(u)
        s = r / 10
        v = s % 10
        digit_one = int(v)
        
        if digit_one == 0:
            d1.off()
            on0()
            time.sleep(0.001)
            off()
            
        if digit_one == 1:
            d1.off()
            on1()
            time.sleep(0.001)
            off()
            
        if digit_one == 2:
            d1.off()
            on2()
            time.sleep(0.001)
            off()
            
        if digit_one == 3:
            d1.off()
            on3()
            time.sleep(0.001)
            off()
            
        if digit_one == 4:
            d1.off()
            on4()
            time.sleep(0.001)
            off()
            
        if digit_one == 5:
            d1.off()
            on5()
            time.sleep(0.001)
            off()
            
        if digit_one == 6:
            d1.off()
            on6()
            time.sleep(0.001)
            off()
            
        if digit_one == 7:
            d1.off()
            on7()
            time.sleep(0.001)
            off()
            
        if digit_one == 8:
            d1.off()
            on8()
            time.sleep(0.001)
            off()
            
        if digit_one == 9:
            d1.off()
            on9()
            time.sleep(0.001)
            off()
            
        if digit_two == 0:
            d2.off()
            on0()
            time.sleep(0.001)
            off()
            
        if digit_two == 1:
            d2.off()
            on1()
            time.sleep(0.001)
            off()
            
        if digit_two == 2:
            d2.off()
            on2()
            time.sleep(0.001)
            off()
            
        if digit_two == 3:
            d2.off()
            on3()
            time.sleep(0.001)
            off()
            
        if digit_two == 4:
            d2.off()
            on4()
            time.sleep(0.001)
            off()
            
        if digit_two == 5:
            d2.off()
            on5()
            time.sleep(0.001)
            off()
            
        if digit_two == 6:
            d2.off()
            on6()
            time.sleep(0.001)
            off()
            
        if digit_two == 7:
            d2.off()
            on7()
            time.sleep(0.001)
            off()
            
        if digit_two == 8:
            d2.off()
            on8()
            time.sleep(0.001)
            off()
            
        if digit_two == 9:
            d2.off()
            on9()
            time.sleep(0.001)
            off()
            
        if digit_three == 0:
            d3.off()
            on0()
            time.sleep(0.001)
            off()
            
        if digit_three == 1:
            d3.off()
            on1()
            time.sleep(0.001)
            off()
            
        if digit_three == 2:
            d3.off()
            on2()
            time.sleep(0.001)
            off()
            
        if digit_three == 3:
            d3.off()
            on3()
            time.sleep(0.001)
            off()
            
        if digit_three == 4:
            d3.off()
            on4()
            time.sleep(0.001)
            off()
            
        if digit_three == 5:
            d3.off()
            on5()
            time.sleep(0.001)
            off()
            
        if digit_three == 6:
            d3.off()
            on6()
            time.sleep(0.001)
            off()
            
        if digit_three == 7:
            d3.off()
            on7()
            time.sleep(0.001)
            off()
            
        if digit_three == 8:
            d3.off()
            on8()
            time.sleep(0.001)
            off()
            
        if digit_three == 9:
            d3.off()
            on9()
            time.sleep(0.001)
            off()
            
        if digit_four == 0:
            d4.off()
            on0()
            time.sleep(0.001)
            off()
            
        if digit_four == 1:
            d4.off()
            on1()
            time.sleep(0.001)
            off()
            
        if digit_four == 2:
            d4.off()
            on2()
            time.sleep(0.001)
            off()
            
        if digit_four == 3:
            d4.off()
            on3()
            time.sleep(0.001)
            off()
            
        if digit_four == 4:
            d4.off()
            on4()
            time.sleep(0.001)
            off()
            
        if digit_four == 5:
            d4.off()
            on5()
            time.sleep(0.001)
            off()
            
        if digit_four == 6:
            d4.off()
            on6()
            time.sleep(0.001)
            off()
            
        if digit_four == 7:
            d4.off()
            on7()
            time.sleep(0.001)
            off()
            
        if digit_four == 8:
            d4.off()
            on8()
            time.sleep(0.001)
            off()
            
        if digit_four == 9:
            d4.off()
            on9()
            time.sleep(0.001)
            off()

def thread_2():
    while True:
        time.sleep(59)
        active_on.off()
        time.sleep(1)
        active_on.on()
    
if __name__ == "__main__":
    t1 = threading.Thread(target = thread_1)
    t2 = threading.Thread(target = thread_2)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

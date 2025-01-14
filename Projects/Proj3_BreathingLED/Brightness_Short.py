from gpiozero import LED
import time

led = LED(18)
a = 0
b = 0.02
print("Press Ctrl + C to stop program")
while True:
    
    for x in range(0,19):
        for x in range(0,5):
            led.on()
            time.sleep(a)
            led.off()
            time.sleep(b)
        
        a = a + 0.001
        b = b - 0.001
        
    a = 0
    b = 0.02

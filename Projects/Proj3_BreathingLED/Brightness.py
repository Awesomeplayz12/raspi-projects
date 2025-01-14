from gpiozero import LED
import time

led = LED(18)

print("Press Ctrl + C to stop program")
while True:
    
    led.off()
    time.sleep(0.1)
    
    for x in range(0,5):
        led.on()
        time.sleep(0.001)
        led.off()
        time.sleep(0.019)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.002)
        led.off()
        time.sleep(0.018)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.003)
        led.off()
        time.sleep(0.017)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.004)
        led.off()
        time.sleep(0.016)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.005)
        led.off()
        time.sleep(0.015)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.006)
        led.off()
        time.sleep(0.014)
            
    for x in range(0,5):
        led.on()
        time.sleep(0.007)
        led.off()
        time.sleep(0.013)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.008)
        led.off()
        time.sleep(0.012)
    
    for x in range(0,5):
        led.on()
        time.sleep(0.009)
        led.off()
        time.sleep(0.011)
    
    for x in range(0,5):
        led.on()
        time.sleep(0.01)
        led.off()
        time.sleep(0.01)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.011)
        led.off()
        time.sleep(0.009)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.012)
        led.off()
        time.sleep(0.008)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.013)
        led.off()
        time.sleep(0.007)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.014)
        led.off()
        time.sleep(0.006)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.015)
        led.off()
        time.sleep(0.005)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.016)
        led.off()
        time.sleep(0.004)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.017)
        led.off()
        time.sleep(0.003)
        
    for x in range(0,5):
        led.on()
        time.sleep(0.018)
        led.off()
        time.sleep(0.002)
    
    for x in range(0,5):
        led.on()
        time.sleep(0.019)
        led.off()
        time.sleep(0.001)
        
    led.on()
    time.sleep(0.1)

from gpiozero import LED
import time

led = LED(20)

for x in range(0,10):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)

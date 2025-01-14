from gpiozero import LED
import time

led1 = LED(10)
led2 = LED(9)
led3 = LED(11)

led1.on()
time.sleep(1)
led1.off()
time.sleep(1)

led2.on()
time.sleep(1)
led2.off()
time.sleep(1)

led3.on()
time.sleep(1)
led3.off()
time.sleep(1)

led1.on()
led2.on()
time.sleep(1)
led1.off()
led2.off()
time.sleep(1)

led1.on()
led3.on()
time.sleep(1)
led1.off()
led3.off()
time.sleep(1)

led2.on()
led3.on()
time.sleep(1)
led2.off()
led3.off()
time.sleep(1)

led1.on()
led2.on()
led3.on()
time.sleep(1)
led1.off()
led2.off()
led3.off()
time.sleep(1)

from gpiozero import LED
import time

active_on = LED(21)

active_on.off()
time.sleep(1)
active_on.on()

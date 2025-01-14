from gpiozero import LED
import time

print("Enter which color you want to be shown:")
print("1. Blue")
print("2. Green")
print("3. Red")
print("4. Aqua")
print("5. Pink")
print("6. Yellow")
print("7. White")
print("8. Exit")
 
led1 = LED(10)
led2 = LED(9)
led3 = LED(11)

i = input("Enter the number that corresponds to the color \n")

while i != "8":

    if i == "1":
        led1.on()
        time.sleep(1)
        led1.off()
        time.sleep(1)

    if i == "2":
        led2.on()
        time.sleep(1)
        led2.off()
        time.sleep(1)

    if i == "3":
        led3.on()
        time.sleep(1)
        led3.off()
        time.sleep(1)

    if i == "4":
        led1.on()
        led2.on()
        time.sleep(1)
        led1.off()
        led2.off()
        time.sleep(1)

    if i == "5":
        led1.on()
        led3.on()
        time.sleep(1)
        led1.off()
        led3.off()
        time.sleep(1)

    if i == "6":
        led2.on()
        led3.on()
        time.sleep(1)
        led2.off()
        led3.off()
        time.sleep(1)

    if i == "7":
        led1.on()
        led2.on()
        led3.on()
        time.sleep(1)
        led1.off()
        led2.off()
        led3.off()
        time.sleep(1)
        
    print("Enter which color you want to be shown:")
    print("1. Blue")
    print("2. Green")
    print("3. Red")
    print("4. Aqua")
    print("5. Pink")
    print("6. Yellow")
    print("7. White")
    print("8. Exit")
            
    i = input("Enter the number that corresponds to the color \n")

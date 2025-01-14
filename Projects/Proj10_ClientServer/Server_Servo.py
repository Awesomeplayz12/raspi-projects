import socket
import RPi.GPIO as GPIO
import time

password = "1234"

server = socket.socket()
print("Server Created")

server.bind(("192.168.1.20", 21985))

server.listen(3)
print("Waiting for clients")

client, address = server.accept()
print("A client has connected!")

client.send(bytes("What is the password?", "utf-8"))

msg = client.recv(1024).decode()

servoPIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start(5)

if msg == password:
    client.send(bytes("Your password guess was correct!", "utf-8"))
        
    while True:
        message = client.recv(1024).decode()
        
        p.ChangeDutyCycle(5)

        if message == "1":
            #180 degree spin
            p.ChangeDutyCycle(15)
            time.sleep(1)
            
        if message == "2":
            #90 degree spin
            p.ChangeDutyCycle(10)
            time.sleep(1)
            
        if message == "3":
            #45 degree spin
            p.ChangeDutyCycle(7.5)
            time.sleep(1)
                
        elif message == "4":
            p.stop()
            GPIO.cleanup()
            break
        
        else:
            client.send(bytes("Send a valid input", "utf-8"))
            
        p.ChangeDutyCycle(5)
        
else:
    client.send(bytes("Wrong password", "utf-8"))

client.close()
p.stop()
GPIO.cleanup()

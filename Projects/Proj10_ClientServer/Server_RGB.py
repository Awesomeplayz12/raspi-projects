import socket
from gpiozero import LED
import time

b = LED(2)
r = LED(3)
g = LED(4)

password = "1234"

server = socket.socket()
print("Server Created")

server.bind(("192.168.1.20", 9992))

server.listen(3)
print("Waiting for clients")

client, address = server.accept()
print("A client has connected!")

client.send(bytes("What is the password?"))

msg = client.recv(1024).decode()

if msg == password:
    client.send(bytes("Your password guess was correct!"))
    
    while True:
        message = client.recv(1024).decode()
        
        if message == "Red":
            print("Red")
            client.send(bytes("LED turning Red"))
            r.on()
            b.off()
            g.off()
            
        elif message == "Blue":
            print("Blue")
            client.send(bytes("LED turning Blue"))
            r.off()
            b.on()
            g.off()
            
        elif message == "Green":
            print("Green")
            client.send(bytes("LED turning Green"))
            r.off()
            b.off()
            g.on()
            
        elif message == "Cyan":
            print("Cyan")
            client.send(bytes("LED turning Cyan"))
            r.off()
            b.on()
            g.on()
            
        elif message == "Magenta":
            print("Magenta")
            client.send(bytes("LED turning Magenta"))
            r.on()
            b.on()
            g.off()
            
        elif message == "Yellow":
            print("Yellow")
            client.send(bytes("LED turning Yellow"))
            r.on()
            b.off()
            g.on()
        
        elif message == "White":
            print("White")
            client.send(bytes("LED turning White"))
            r.on()
            b.on()
            g.on()
        
        elif message == "Exit":
            r.off()
            g.off()
            b.off()
            break
        
        else:
            print("Client has entered an invalid input, breaking connection")
            r.off()
            g.off()
            b.off()
            break
                
else:
    client.send(bytes("Your password guess was wrong..."))

client.close()


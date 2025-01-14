import socket

server = socket.socket()

server.bind(("192.168.1.7", 9999))
print("Server created")

server.listen(3)
print("Waiting for clients")

client, address = server.accept()
print("A client has connected")

while True:
    client.send("Enter a command".encode())
    message = client.recv(1024).decode()
        
    if message == "on":
        client.send("Turning on clock".encode())
        
    elif message == "off":
        client.send("Turning off clock".encode())
        
    elif message == "load":
        client.send("Loading time to clock".encode())
        
    elif message == "start":
        client.send("Starting clock".encode())
        
    elif message == "reset":
        client.send("Resetting clock".encode())
    
    elif message == "exit":
        client.send("Exiting connection".encode())
        break
    
    else:
        client.send("Invalid input".encode())
    
print("Client disconnected, closing server")
server.close()
client.close()

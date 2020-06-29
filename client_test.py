#use the socket module to create a simple client that starts a connection to the python server and then sends a message

import socket

SRV_PORT = int(input("Enter port: "))
SRV_ADDR = str(input("Type address: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))
message = input('Enter message: ')
s.send(message.encode())
response = s.recv(1024).decode('utf-8')
print(response)
s.close()

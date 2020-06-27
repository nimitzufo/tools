#the classic listener
#few modifications to be made
import socket

SRV_ADDR = input("Type server IP address: ")
SRV_PORT = int(input("Type the server port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print("Server started, waiting for connections... ")
connection, address = s.accept()

print("Client connected with address: ", address)

while 1:
	data = connection.recv(1024)
	if not data: break
	connection.sendall(b' -- Message received -- \n')
	print(data.decode('utf-8'))
connection.close()	

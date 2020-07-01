#a scrip to verify if a remote webserver has the HTTP method OPTION enabled
#given an IP address/hostname and a port, it tries to enumerate all the other HTTP methods allowed if OPTIONS is

import http.client 

print('**If OPTIONS is enabled, this script will return a list of methods**\n')
host = input('Enter host IP: \n')
port = input('Enter port(default = 80): \n')

if port == "":
	port = 80
	
try:
	connection = http.client.HTTPConnection(host, port)
	connection.request('OPTIONS', '/')
	response = connection.getresponse()
	print('Enabled methods are: ', response.getheader('allow'))
	connection.close()	
except ConnectionRefusedError:
	print('Connection failed')	

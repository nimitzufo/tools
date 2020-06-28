#A port scanner
import argparse 
import threading
import socket


def port_scan(_host, _ports):
	try:
		tgt_ip = socket.gethostbyname(_host)
	except socket.herror:
		print(f'couldn\'t find {_host}: Unknown host')
		return
	try:
		tgt_name = socket.gethostbyaddr(tgt_ip) #given an IP addr it returns a tuple with (host name, alias list for the IP addr if any, IP of the host)
		print(f'\nResults for: {tgt_name[0]}')
	except socket.herror:
		print(f'\nResults for: {tgt_ip}')	
		
	socket.setdefaulttimeout(1)	
	
	for _port in _ports:
		t = threading.Thread(target=full_connect_scan, args=(_host, int(_port)))
		t.start()
		
		
def full_connect_scan(host, port):
	screen_lock = threading.Semaphore() #instance of Semaphore
	with socket.socket(socket.AF_INET. socket.SOCK_STREAM) as conn_socket:
		try:
			conn_socket.connect((host, port))
			conn_socket.send(b'gibberish_jibber-jabber_gobbledygook\r\n')
			results = conn_socket.recv(100).decode('utf-8')
			screen_lock.acquire() #semaphore to prevent threads from printing at the same time
			print(f'Target port: {port}/tcp open')
			print(f'  {results}')
		except OSError:
			screen_lock.acquire()
			print(f'Target port: {port}/tcp closed')
		finally:
			screen_lock.release()		


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='A port scanner for reconnaissance'
	                                 ' that looks for TCP open ports at a given '
	                                 'target using a full TCP connect scan', 
	                                 usage='port_scan_c.py TARGET_HOST -p '
	                                 'TARGET_PORTS')
	                                 
	parser.add_argument('tgt_host',metavar='TARGET_HOST', help='specify target host'
	                    ' (IP address or domain name)')
	parser.add_argument('-p', required=True, type=str, metavar='TARGET_PORTS', help='specify target'
	                    ' port[s] separated by comma -- no spaces in between')
	args = parser.parse_args()
	args.tgt_ports = str(args.p).split(',')
	port_scan(tgt_host, tgt_ports)

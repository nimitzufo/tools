#A vulnerability scanner that connects to a TCP socket and reads the banner from a service

import argparse
import socket
import os

def ret_banner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except OSError:
		return			


def check_vuln_banner(banner, b_file):
	with open(b_file) as v_banner:
		for line in v_banner.readlines():
			if line.strip('\n') in v_banner.strip('\n'):
				print(f'server is vulnerable {banner}')
		

def main(b_file, _ip):
	port_list = [21, 22, 23, 25, 80, 110, 115, 137, 138, 139, 143, 443, 1433, 3306, 3389]
	for x in range(0, 255):
		_ip = _ip +'.'+ str(x)
		for _port in port_list:
			_banner = ret_banner(_ip, _port)
			if _banner:
				print(f'{_ip}: {_banner}')
				check_vuln_banner(_banner, b_file)
			

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='A vulnerability scanner that connectos to a TCP socket and reads the banner from a service', usage='vuln_banner_scanner.py BANNER_FILE IP_SCOPE')
	parser.add_argument('banner_file', metavar='BANNER_FILE', help='Enter the file containing vulnerable banners')
	parser.add_argument('ip_scope', metavar='IP_SCOPE', help='Type the target IPv4 address --only the first 3 bytes, or octets')
	args = parser.parse_args()
	print(f'Running \'{__file__}\'')
	main(args.banner_file, args.ip_scope)

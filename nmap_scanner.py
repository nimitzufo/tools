#nmap port scanner(You have to install Python-Nmap to perform nmap scans with python scripts)
#Types of Port Scans:
"""
-TCP SYN SCAN: Also known as a half-open scan, this type of scan initiates a TCP connection
with a SYN packet and waits for a response. A reset packet indicates the port is closed while a
SYN/ACK indicates the port is open.
-TCP NULL SCAN: A null scan sets the TCP flag header to zero. If a RST is received, it indicates
the port is closed.
-TCP FIN SCAN: A TCP FIN Scan sends the FIN to tear down an active TCP connection and
wait for a graceful termination. If a RST is received, it indicates the port is closed.
-TCP XMAS SCAN: An XMAS Scan sets the PSH, FIN, and URG TCP Flags. If a RST is received,
it indicates the port is closed.
"""
import nmap, argparse

def nmap_scan(host, ports):
	nmap_scanner = nmap.PortScanner()
	for port in ports:
		nmap_scanner.scan(host, port)
		state = nmap_scanner[host]['tcp'][int(port)]['state']
		print(f'\n {host} tcp/{port}: {state}')


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Perform nmap scans with python', usage='nmap_scanner.py TARGET_HOST -p TARGET_PORTS')
	parser.add_argument('tgt_host', metavar='TARGET_HOST', help='Enter target host\'s IP number ')
	parser.add_argument('-p', metavar='TARGET_PORTS', help='Target ports separated by a comma -- no spaces')
	args = parser.parse_args()
	args.tgt_ports = str(args.p).split(',')
	nmap_scan(args.tgt_host, args.tgt_ports)
	

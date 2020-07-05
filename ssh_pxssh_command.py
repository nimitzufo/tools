from pexpect import pxssh

def send_command(session, cmd):
	session.sendline(cmd)
	session.prompt()
	print(session.before.decode('utf-8'))

def connect(host, user, pwd):
	try:
		session = pxssh.pxssh()
		session.login(host, user, pwd)
		return session
	except Exception as e:
		print(f' - Error Connect: {e}')
		exit(0)	

if __name__ == '__main__':
	conn = connect('127.0.0.1', 'root', 'toor')
	send_command(conn, 'sudo cat /etc/shadow | grep root')

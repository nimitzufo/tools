#A zip-file password cracker
#argparse to handle CLI
#threading to allow simultaneous testing of multiple passwords
#zipfile to open, read, write, close and list zip files

import argparse
import zipfile
from threading import Thread

def extract_file(z_file, password):
	try:
		z_file.extractall(pwd=password.encode('utf-8'))
		print(f'Password found: {password}')
	except RuntimeError:
		pass	

def main(zip_name, dict_name):
	_zip = zipfile.ZipFile(zip_name)
	with open(dict_name) as _dict:
		for line in _dict.readlines():
			_pwd = line.strip('\n')
			t = Thread(target=extract_file, args=(_zip, _pwd))
			t.start()
	
if __name__=='__main__':
	parser = argparse.ArgumentParser(description='A zip-file password cracker', usage='zip_cracker.py ZIPFILE DICTFILE')
	parser.add_argument('zip_file', metavar='ZIPFILE', help='specify zip file')
	parser.add_argument('dict_file', metavar='DICTFILE', help='specify dictionary file')
	args = parser.parse_args()
	main(args.zip_file, args.dict_file)

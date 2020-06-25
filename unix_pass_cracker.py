#A *Nix Password Cracker
#crypt.METHOD_SHA512 A Modular Crypt Format method with 16 character salt and 86 character hash. This is the strongest method.
#crypt.METHOD_SHA256 Another Modular Crypt Format method with 16 character salt and 43 character hash.
#crypt.METHOD_MD5 Another Modular Crypt Format method with 8 character salt and 22 character hash.
#crypt.METHOD_CRYPT The traditional method with a 2 character salt and 13 characters of hash. This is the weakest method.
#examples of crypt use --if you want to change the method:
#crypt.crypt(getpass.getpass(), crypt.mksalt(crypt.METHOD_SHA512))
#crypt.crypt("password", crypt.mksalt(crypt.METHOD_SHA512))
#I've tested it and it doesn't seem to work well, saving to try and figure it out later

import argparse
from crypt import crypt

def test_pass(c_pwd, dict_file):
	salt = c_pwd[:2]
	with open(dict_file) as dictionary:
		for word in dictionary.readlines():
			pwd = word.strip('\n')
			c_word = crypt(pwd, salt)
			if c_word == c_pwd:
				print(f'password found: {word}')
				return
		print('password not found')
		return		

def main(target_file, dict_file):
	with open(target_file) as pwd_file:
		for line in pwd_file.readlines():
			if ':' in line:
				username = line.split(':')[0]
				_crypt_pass = line.split(':')[1].strip('\n')
				print(f'cracking {username}\'s password')
				test_pass(_crypt_pass, dict_file)

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='An unix password cracker', usage='unix_pass_cracker.py TARGET DICTIONARY')
	parser.add_argument('target', metavar='TARGET', help='file of hashed passwords from the target')
	parser.add_argument('dictionary', metavar='DICTIONARY', help='dictionary file')
	args = parser.parse_args()
	main(args.target, args.dict)
	

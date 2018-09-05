import requests

if __name__ == '__main__':
	url = 'https://www.eventbrite.com/oauth/authorize'
	headers = {'response_type' : 'token' , 'client' : 'DPM6KQJBYZHFLRWPGR'}
	response = requests.get(url, headers = headers)
	if response.status_code == 200:
		response_json = response.json()
		print (response_json)
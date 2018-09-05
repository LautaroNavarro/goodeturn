import requests

if __name__ == '__main__':
	url = 'https://www.eventbriteapi.com/v3/users/me/'
	headers = {'Authorization' : 'Bearer RDJKBMDJHGB2OWWV3FGH' , 'Content-type' : 'application/json'}
	response = requests.get(url, headers = headers)
	if response.status_code == 200:
		response_json = response.json()
		print (response_json)
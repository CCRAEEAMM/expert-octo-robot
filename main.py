import requests

city = input('Your city')
api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': 'eNgNibecnpL//wxV3PydIg==Qvf3KXoJsRKXC85X'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
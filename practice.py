import requests

url = 'https://api.open-meteo.com/v1/forecast'
params = {'latitude': 34.01, 'longitude': 71.58,
'current_weather': True}

headers = { 'Accept': 'application/json' }

response = requests.get(url, params = params, headers = headers)

print(response.status_code)
data = response.json()
print(data['current_weather']['temperature'])
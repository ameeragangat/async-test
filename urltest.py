import requests

url = f"http://api.openweathermap.org/data/2.5/weather?q=Cape Town&appid=5dd4a8b96c4a88cffbc4d0514293f207&units=metric"
response = requests.get(url)
data = response.json()

print(data)
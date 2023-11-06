import requests

request = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(request).json()
print(vastaus["value"])
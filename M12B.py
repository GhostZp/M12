import requests

API_KEY = "c1a1919c68929e907a9a24cd6ec2fef2"

kaupunki = input("Kerro kaupunki nimi: ")
request = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={kaupunki}"
response = requests.get(request)

kelvin = response.json()["main"]["temp"]
kuvaus = response.json()["weather"][0]["description"]

temperature = kelvin - 273.15

print(f"{temperature:.2f} celsius, {kuvaus}.")
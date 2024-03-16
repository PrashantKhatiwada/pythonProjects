import requests
import json
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

city = input("Enter the name of city:\n")
url = f"https://api.weatherapi.com/v1/current.json?key=d10863e58b3c41ca828130339241603&q={city}"

r = requests.get(url)
print(r.text)
weatherDict = json.loads(r.text)
tempCelsius = weatherDict["current"]["temp_c"]
tempFarh = weatherDict["current"]["temp_f"]
condition = weatherDict["current"]["condition"]["text"]


try:
    engine.say(f"Hi, here is the weather details of {city}. The temperature in {city} is {tempCelsius} degree celsius and {tempFarh} degree fahreinheit. The condition there is {condition} ")
    engine.runAndWait()
except Exception as e:
    print(e)
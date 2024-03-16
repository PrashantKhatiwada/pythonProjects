import datetime
import os
import speech_recognition as spr
import pyttsx3
import wikipedia
import webbrowser
import smtplib
import json
import requests

emails = {
    'prashant': 'pkhatiwada58@gmail.com',
    'prakash': 'praks2435@gmail.com',
    'pacific': 'thepacificwaves@gmail.com'
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
# print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am a Virtual Assistant made by Mister Prashant Khatiwada. I am here to make your desktop experience easy and smooth. How can I help you? ")

def takeCommand():
    '''Takes Command from the user using microphone and returns string output'''

    recg = spr.Recognizer()
    with spr.Microphone() as source:
        print("Listening...")
        recg.pause_threshold = 1
        audio = recg.listen(source)
    try:
        print("Recognizing")
        query = recg.recognize_google(audio,language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if query == "quit":
            speak("Sayonara, maukaa meeley feri bhetaulaa")
            break
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send email' in query:
            try:
                speak("Who do you wanna send the email to, sir?")
                person = takeCommand()
                to = emails.get(f'{person}')
                speak(f"What message do you want to send to {to}")
                content = takeCommand()
                sendEmail(to, content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak("Sorry, the email couldn't be send")
        elif 'weather' in query:
            speak("Which city do you want me to tell the weather of?")
            city = takeCommand()
            url = f"https://api.weatherapi.com/v1/current.json?key=d10863e58b3c41ca828130339241603&q={city}"
            r = requests.get(url)
            print(r.text)
            weatherDict = json.loads(r.text)
            tempCelsius = weatherDict["current"]["temp_c"]
            tempFarh = weatherDict["current"]["temp_f"]
            condition = weatherDict["current"]["condition"]["text"]
            speak(f"Here is the weather details of {city}. The temperature in {city} is {tempCelsius} degree celsius and {tempFarh} degree fahreinheit. The condition there is {condition}")







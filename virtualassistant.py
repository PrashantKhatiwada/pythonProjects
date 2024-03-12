import datetime
import speech_recognition as spr
import pyttsx3
import wikipedia
import webbrowser

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

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if query == "quit":
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




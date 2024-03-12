import pyttsx3

textSpeech = pyttsx3.init()

while True:
    inp = input("What do you want me to speak? ")
    if (inp == "q"):
        textSpeech.say("Thanks for using the Robo Speaker. Have a good day!")
        textSpeech.runAndWait()
        break
    else:
        textSpeech.say(inp)
        textSpeech.runAndWait()



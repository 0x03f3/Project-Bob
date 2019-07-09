import random
import pyttsx3
import speech_recognition as sr
from SpeechRecognition import languages

bob = pyttsx3.init()
r = sr.Recognizer();

#pyttxs3 can't handle lists so this is a workaround for random list array passing
randomGreeting = str(languages.english(1)[random.randint(1,len(languages.english(1))-1)])
randomEnquire = str(languages.english(2)[random.randint(1,len(languages.english(2))-1)])
randomFarewell = str(languages.english(3)[random.randint(1, len(languages.english(3))-1)])
randomError = str(languages.english(4)[random.randint(1, len(languages.english(4))-1)])
subroutines = str(languages.english(5))
commandList = str(languages.english(6))

def listen():

#    while True:
#Assign default microphone
    with sr.Microphone() as source:
        print('Listening: ')
        # Capture the audio and translate it into text
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        # take the text and check it against the list of greetings
        if str(text) in languages.english(1):
            # If a greeting is detected bob will respond in kind
            bob.say(str(languages.english(1)[random.randint(1,len(languages.english(1))-1)]))
            bob.runAndWait()

            # Debug print
            print("Greeting")
        elif str(text) in languages.english(3):
            # If a farewell is detected bob will respond in kind
            bob.say(randomFarewell)
            bob.runAndWait()

            # Debug print
            print("Farewell")

        elif str(text) in languages.english(6):
            # If command is detected then respond in kind

            # THIS NEEDS TO BE INDEPENDENT PER COMMAND!
            # CONSIDER IMPLEMENTING A SEPERATE FUNCTION CALL
            # TO STOP THE CONSTANT IF PROCESSING.

            bob.say(subroutines)
            bob.say("Which subroutine would you like to access")
            bob.runAndWait()
            # Debug print
            print("Commands")

        else:

            #You dun goofed
            bob.say(randomError)
            bob.runAndWait()

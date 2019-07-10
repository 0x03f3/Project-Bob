import random
import pyttsx3
import socket
import speech_recognition as sr
from SpeechRecognition import languages
from SpeechRecognition.Subsystems import subsytemControl

#pyttxs3 can't handle lists so this is a workaround for random list array passing
#randomGreeting = str(languages.english(1)[random.randint(1,len(languages.english(1))-1)])
#randomEnquire = str(languages.english(2)[random.randint(1,len(languages.english(2))-1)])
#randomFarewell = str(languages.english(3)[random.randint(1, len(languages.english(3))-1)])
#randomError = str(languages.english(4)[random.randint(1, len(languages.english(4))-1)])
#subroutines = str(languages.english(5))
#commandList = str(languages.english(6))

#### EVENTUALLY REDUCE STATEMENT TO EXTERNAL PROCESSING CALLS.


def listen():

    r = sr.Recognizer();
    # while True:
    #Assign default microphone
    with sr.Microphone() as source:
        print('Listening: ')
        # Capture the audio and translate it into text
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        return text
        # take the text and check it against the list of greetings

def thinking(text):
    #initialize bob inside function
    bob = pyttsx3.init()
    # Greeting
    if str(text) in languages.english(1):
        # If a greeting is detected bob will respond in kind
        bob.say(str(languages.english(1)[random.randint(1,len(languages.english(1))-1)]))
        bob.runAndWait()

        # Debug print
        print("Greeting")

    # Farewell
    elif str(text) in languages.english(3):
        # If a farewell is detected bob will respond in kind
        bob.say(randomFarewell)
        bob.runAndWait()
        # Exit program

        # Debug print
        print("Farewell")

    # Command
    elif str(text) in languages.english(6):
        # If command is detected then respond in kind

        # THIS NEEDS TO BE INDEPENDENT PER COMMAND!
        # CONSIDER IMPLEMENTING A SEPERATE FUNCTION CALL
        # TO STOP THE CONSTANT IF PROCESSING.

        #bob.say(subroutines)
        bob.say("Which subroutine would you like to access")
        bob.runAndWait()
        with sr.Microphone() as source:
            print('Listening: ')
            # Capture the audio and translate it into text
            audio = r.listen(source)
            subroutine = r.recognize_google(audio)
            print(subroutine)
            subroutineReturn = subsytemControl.controlTest(subroutine)
            bob.say(str(subroutineReturn))
            bob.runAndWait()
        # Debug print
        print("Commands Exit")

    else:

        #You dun goofed
        bob.say(randomError)
        bob.runAndWait()

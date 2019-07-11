import random
import pyttsx3
import socket
import speech_recognition as sr
from SpeechRecognition import languages
from SpeechRecognition.Subsystems import subsytemControl
#from SpeechRecognition.Subsystems.Translation import translation

#pyttxs3 can't handle lists so this is a workaround for random list array passing
randomGreeting = str(languages.english(1)[random.randint(1,len(languages.english(1))-1)])
randomEnquire = str(languages.english(2)[random.randint(1,len(languages.english(2))-1)])
randomFarewell = str(languages.english(3)[random.randint(1, len(languages.english(3))-1)])
randomError = str(languages.english(4)[random.randint(1, len(languages.english(4))-1)])
subroutines = str(languages.english(5))
commandList = str(languages.english(6))

#### EVENTUALLY REDUCE STATEMENT TO EXTERNAL PROCESSING CALLS. ###
bob = pyttsx3.init()

def listen():

    r = sr.Recognizer();
    # while True:
    #Assign default microphone
    with sr.Microphone() as source:
        try:
            print('Listening: ')
            # Capture the audio and translate it into text
            audio = r.listen(source)
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            bob.say(str(languages.english(4)[random.randint(1, len(languages.english(4))-1)]))
            bob.runAndWait()
            listen()
        except sr.RequestError:
            bob.say(str(languages.english(4)[random.randint(1, len(languages.english(4))-1)]))
            bob.runAndWait()
            listen()
        # take the text and check it against the list of greetings

def thinking(text):
    #initialize bob inside function
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
        bob.say(str(languages.english(3)[random.randint(1, len(languages.english(3))-1)]))
        bob.runAndWait()
        # Debug print
        print("Farewell")
        # Exit program
        exit()

    # Command
    elif str(text) in languages.english(6):

        bob.say("Would you like to list all subroutines")
        bob.runAndWait()
        affirmation = listen()
        if str(affirmation) in languages.english(7):
            bob.say(str(languages.english(5)))
            bob.runAndWait()
        elif str(affirmation in languages.english(8)):
            bob.say("Okay")
            bob.runAndWait()
        # Add
        bob.say("Which subroutine would you like to access")
        bob.runAndWait()
        input = listen()
        subroutineReturn = subsytemControl.controlTest(input)
        print(subroutineReturn)
        bob.say(str(subroutineReturn))
        bob.runAndWait()

        # Debug print
        print("Commands Exit")

    else:

        #You dun goofed
        bob.say(str(languages.english(4)[random.randint(1, len(languages.english(4))-1)]))
        bob.runAndWait()

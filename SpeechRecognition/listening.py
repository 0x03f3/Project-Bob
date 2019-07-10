import random
import pyttsx3
import socket
import speech_recognition as sr
from SpeechRecognition import languages
from SpeechRecognition.Subsystems import subsytemControl
from SpeechRecognition.Subsystems.Translation import translation

#pyttxs3 can't handle lists so this is a workaround for random list array passing
randomGreeting = str(languages.english(1)[random.randint(1,len(languages.english(1))-1)])
randomEnquire = str(languages.english(2)[random.randint(1,len(languages.english(2))-1)])
randomFarewell = str(languages.english(3)[random.randint(1, len(languages.english(3))-1)])
randomError = str(languages.english(4)[random.randint(1, len(languages.english(4))-1)])
subroutines = str(languages.english(5))
commandList = str(languages.english(6))

#### EVENTUALLY REDUCE STATEMENT TO EXTERNAL PROCESSING CALLS.
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
        bob.say(str(languages.english(4)[random.randint(1, len(languages.english(4))-1)]))
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
#        with sr.Microphone() as source:
#            print('Listening: ')
#            # Capture the audio and translate it into text
#            audio = r.listen(source)
#            subroutine = r.recognize_google(audio)
        test = listen()
        if test == "translation":
            bob.say("what would you like translated")
            bob.runAndWait()
            print("Listening for trnslation text")
            input = listen()
            bob.say("What language would you like to translate that to")
            bob.runAndWait()
            print("Listening for language")
            language = listen()
            if language == "german":
                language = "DE"
            bob.say(translation.translate(input, language))
            bob.runAndWait()
        else:
            subroutineReturn = subsytemControl.controlTest(test)
            print(subroutineReturn)
            bob.say(str(subroutineReturn))
            bob.runAndWait()
            # Debug print
            print("Commands Exit")

    else:

        #You dun goofed
        bob.say(str(languages.english(4)[random.randint(1, len(languages.english(4))-1)]))
        bob.runAndWait()

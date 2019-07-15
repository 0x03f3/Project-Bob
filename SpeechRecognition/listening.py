import random
import pyttsx3
import socket
import speech_recognition as sr
from SpeechRecognition import languages
from SpeechRecognition.Subsystems import subsytemControl


#### EVENTUALLY REDUCE STATEMENT TO EXTERNAL PROCESSING CALLS. ###
bob = pyttsx3.init()

def log(text, response, placement):
    errorOutput = open("SpeechRecognition/Logs/vocalLog.txt","a+")
    errorOutput.write( "User: " + text + "\n" + "Bob " + placement + ": " + response + "\n\n")
    errorOutput.close()

def listen():

    r = sr.Recognizer();
    # while True:
    #Assign default microphone
    with sr.Microphone() as source:
        try:
            print('[+] Listening: ')
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
        # Assign responce for log()
        print("[+] Greeting")
        response = str(languages.english(1)[random.randint(1,len(languages.english(1))-1)])
        # If a greeting is detected bob will respond in kind
        bob.say(response)
        bob.runAndWait()
        # Log vocal input for learning function
        log(text, response, "[+] Greeting")
        # Debug print
        print("[+] Greeting Finished")

    # Farewell
    elif str(text) in languages.english(3):
        print("[+] Farewell")
        # Assign responce for log()
        response = str(languages.english(3)[random.randint(1, len(languages.english(3))-1)])
        # If a farewell is detected bob will respond in kind
        bob.say(response)
        bob.runAndWait()
        # Log vocal input for learning function
        log(text, response, "[+] Farewell")
        print("[+] Farewell Finished")
        # Exit program
        exit()

    # Command
    elif str(text) in languages.english(6):
        print("[+] Subroutine")
        # Ask if the user would like to list subroutines
        bob.say("Would you like to list all subroutines")
        bob.runAndWait()
        # Take user response to subroutine list
        affirmation = listen()
        # If yes then list subroutines
        if str(affirmation) in languages.english(7):
            bob.say(str(languages.english(5)))
            bob.runAndWait()
        # If no then acknowledge and continue subroutine
        elif str(affirmation in languages.english(8)):
            bob.say("Okay")
            bob.runAndWait()
        # Ask which subroutine to access
        bob.say("Which subroutine would you like to access")
        bob.runAndWait()
        # Take user response
        input = listen()
        # Execute the subroutine from /SpeechRecognition/Subsystems/subsytemControl.py
        subroutineReturn = subsytemControl.controlTest(input)
        # Bob says the subroutine return
        bob.say(str(subroutineReturn))
        bob.runAndWait()

        # Debug print
        print("[+] Subroutine Finished")

    else:
        print("[+] Error")
        response = str(languages.english(4)[random.randint(1, len(languages.english(4))-1)])
        #You dun goofed
        bob.say(response)
        bob.runAndWait()
        # Log vocal input for learning function
        log(text, response, "Error")
        print("[+] Error Finished")

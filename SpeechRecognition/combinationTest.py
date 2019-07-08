import speech_recognition as sr
import pyttsx3
import random
import webbrowser
import languages

randomGreeting = str(languages.chinese(1)[random.randint(1,len(languages.chinese(1))-1)])
randomEnquire = str(languages.chinese(2)[random.randint(1,len(languages.chinese(2))-1)])
randomFarewell = str(languages.chinese(3)[random.randint(1, len(languages.chinese(3))-1)])
randomError = str(languages.chinese(4)[random.randint(1, len(languages.chinese(4))-1)])

###############################################################################
#                                                                             #
#                             BASE FUNCTIONS                                  #
#                                                                             #
###############################################################################

def greeting():

    with sr.Microphone() as source:

        print('Greeting Speak: ')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        greetingTerm = "hello"
        words = text.split()
        if greetingTerm in words:
            print("Random Greeting INITIALIZATION")
            engine.say(randomGreeting)
            engine.runAndWait()
        else:
            print("Random Greeting ERROR")
            engine.say(randomError)
            engine.runAndWait()
            greeting()

def request():
    print("random request INITIALIZATION")
    engine.say(randomEnquire)
    engine.runAndWait()

def farewell():

    with sr.Microphone() as source:
        print('Farewell Speak: ')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        farewellTerm = "nothing"
        words = text.split()
        if farewellTerm in words:
            print("Farewell Speak INITIALIZATION")
            engine.say(randomFarewell)
            engine.runAndWait()
        else:
            print("Farewell Speak ERROR")
            engine.say(randomError)
            engine.runAndWait()
            farewell()

#def executeCommand():
#    webbrowser.open('https://www.youtube.com/watch?v=0xiB_S7NTUY')

###############################################################################
#                                                                             #
#                            INITIALIZATION                                   #
#                                                                             #
###############################################################################

engine = pyttsx3.init()
r = sr.Recognizer()

engine.say("Nǐ hǎo")
engine.runAndWait()

greeting()

request()

farewell()

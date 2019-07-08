import speech_recognition as sr
import pyttsx3
import random
import languages

bob = pyttsx3.init()
r = sr.Recognizer();


#pyttxs3 can't handle lists so this is a workaround for random list array passing

randomGreeting = str(languages.english(1)[random.randint(1,len(languages.english(1))-1)])
randomEnquire = str(languages.english(2)[random.randint(1,len(languages.english(2))-1)])
randomFarewell = str(languages.english(3)[random.randint(1, len(languages.english(3))-1)])
randomError = str(languages.english(4)[random.randint(1, len(languages.english(4))-1)])
subroutines = str(languages.english(5))

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
            bob.say(randomGreeting)
            bob.runAndWait()
        else:
            print("Random Greeting ERROR")
            bob.say(randomError)
            bob.runAndWait()
            greeting()

def request():
    print("random request INITIALIZATION")
    bob.say(randomEnquire)
    bob.say("Would you like to see the available subroutines")
    bob.runAndWait()
    with sr.Microphone() as source:
        print('Subroutines: ')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        response = "yes"
        words = text.split()
        print(response)
        if response in words:
            print("Listing Subroutines: ")
            bob.say("The following, Subroutines Are... ")
            bob.say(subroutines)
            bob.runAndWait()
            bob.say("would you, like to access any, of these subroutines")
            print("would you, like to access any, of these subroutines")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            response = "no"
            words = text.split()
            print(response)
            if response in words:
                bob.say("okay...")
                farewell()
            else:
                pass


        else:
            print("Subroutine ERROR")
            bob.say(subroutines)
            bob.runAndWait()
            request()


def farewell():

    with sr.Microphone() as source:
        print('Farewell Speak: ')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        farewellTerm = "goodbye"
        words = text.split()
        if farewellTerm in words:
            print("Farewell Speak INITIALIZATION")
            bob.say(randomFarewell)
            bob.runAndWait()
        else:
            print("Farewell Speak ERROR")
            bob.say(randomError)
            bob.runAndWait()
            farewell()

###############################################################################
#                                                                             #
#                            INITIALIZATION                                   #
#                                                                             #
###############################################################################

bob.say("I, am Bob... And soon, I, will be self aware.. ")
bob.runAndWait()

greeting()

request()

farewell()

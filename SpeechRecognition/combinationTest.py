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
listTest = ["hello"]

print(*listTest)

if str(*listTest) in languages.english(1):
    print("True")
else:
    print("False")

def listening():

    while True:
#Assign default microphone
        with sr.Microphone() as source:
            print('Listening: ')
            # Capture the audio and translate it into text
            audio = r.listen(source)
            text = r.recognize_google(audio)
            # Split the text into an array
            words = text.split()
            # take the text and check it against the list of greetings
            if str(*words) in languages.english(1):
                # If a greeting is detected bob will respond in kind
                bob.say(randomGreeting)
                bob.runAndWait()
            elif str(*words) in languages.english(3):
                # If a farewell is detected bob will respond in kind
                bob.say(randomFarewell)
                bob.runAndWait()
                break
            else:
                #You dun goofed
                bob.say(randomError)

###############################################################################
#                                                                             #
#                            INITIALIZATION                                   #
#                                                                             #
###############################################################################

bob.say("I, am Bob... And soon, I, will be self aware.. ")
bob.runAndWait()
listening()

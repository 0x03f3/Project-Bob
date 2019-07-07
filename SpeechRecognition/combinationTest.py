import speech_recognition as sr
import pyttsx3
import random
import webbrowser

engine = pyttsx3.init()
r = sr.Recognizer()

def greeting():

    greetingList = ["Hello", "Hi", "Hey", "How's it going?", "How are you?",\
                    "What's up", "What's new?", "How's everything", \
                    "How are things?", "How's Life?", "How's your day?", \
                    "How's your day going?", "Good to see you!", \
                    "Nice to see you", "Long time no see", "It's been a while"]

    print(len(greetingList))

    with sr.Microphone() as source:
        print('Speak: ')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        greetingTerm = "hello"
        words = text.split()
        randomGreeting = str(greetingList[random.randint(0,15)]) + "Leo Rose"
        if greetingTerm in words:
            engine.say(randomGreeting)
            engine.runAndWait()
        else:
            print("Error")

def farewell():

    farewellList = ["bye", "bye bye", "See you later", "See you soon", \
                    "Talk to you later", "I must be going", "Take it easy"\
                    "I'm off too", "Goodbye", "Have a good day",\
                    "Have a nice day", "I'll look forward to our next meeting"\
                    "Until next time", "Take care", "It was nice talking to you"\
                    "It was nice seeing you", "Until later", "Peace out",\
                     "I'm out", "I'm off", ]
    print(len(farewellList))

    with sr.Microphone() as source:
        print('Speak: ')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        farewellTerm = "bye"
        words = text.split()
        randomFarewell = str(farewellList[random.randint(0,15)]) + "Leo Rose"
        if farewellTerm in words:
            engine.say(randomFarewell)
            engine.runAndWait()
        else:
            print("Error")

def executeCommand():
    webbrowser.open('https://www.youtube.com/watch?v=0xiB_S7NTUY')

def request():
    introOffer = ["What can I help with today?", "What can I do for you?",\
                  "What will you have me do?"]
    randomOffer = str(introOffer[random.randint(0,2)])
    engine.say(randomOffer)
    engine.runAndWait()

print("Greeting")
greeting()
print("Request")
request()
print("Execute Command")
executeCommand()
print("Farewell")
farewell()

import speech_recognition as sr
import pyttsx3
import random

def greeting():

    greetingList = ["Hello", "Hi", "Hey", "How's it going?", "How are you?",\
                    "What's up", "What's new?", "How's everything", \
                    "How are things?", "How's Life?", "How's your day?", \
                    "How's your day going?", "Good to see you!", \
                    "Nice to see you", "Long time no see", "It's been a while"]

    engine = pyttsx3.init()
    r = sr.Recognizer()

    print(len(greetingList))

    with sr.Microphone() as source:
        print('Speak: ')
        audio = r.listen(source)
        text = r.recognize_google(audio)
        term = "hello"
        words = text.split()
        randomGreeting = str(greetingList[random.randint(0,15)]) + "Friend"
        if term in words:
            engine.say(randomGreeting)
            engine.runAndWait()
        else:
            print("Error")

def request():


greeting()

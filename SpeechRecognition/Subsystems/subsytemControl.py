from SpeechRecognition.Subsystems.Hacking import networkScan
from SpeechRecognition.Subsystems.Internet import browser
from SpeechRecognition.Subsystems.Time import currentTime
from SpeechRecognition.Subsystems.Translation import translation
import pyttsx3
import speech_recognition as sr
from .. import languages
from .. import listening
bob = pyttsx3.init()

currentTime.getTime()



def controlTest(vocalInput):

    if vocalInput == "translation":

        # Take user input for translation
        bob.say("what would you like translated")
        bob.runAndWait()
        print("Listening for translation text")
        input = listening.listen()

        # Take user input for languagae to translate to.
        bob.say("What language would you like to translate that to")
        bob.runAndWait()
        print("Listening for language")
        language = listening.listen()

        #Assign selected language for traslation function
        #PLEASE FIX THIS MONSTROSITY!
        if language == "german":
            language = "DE"
        elif language == "spanish":
            language = "ES"
        elif language == "polish":
            language = "PL"
        elif language == "chinese":
            language = "ZH-CN"
        elif language == "hindi":
            language = "HI"
        elif language == "arabic":
            language = "AR"
        elif language == "portuguese":
            language = "PT"
        elif language == "russian":
            language = "RU"
        elif language == "japanese":
            language = "JA"
        elif language == "korean":
            language = "KO"
        elif language == "french":
            language = "FR"
        #Execute translation and wait for return response.
        return translation.translate(input, language)

    # Vocal time request control
    elif vocalInput == "current time":
        return currentTime.getTime()

    # Vocal date request control
    elif vocalInput == "current date":
        return currentTime.getDate()

    # Vocal network scan request
    elif vocalInput == "network scan":
        print("Running Network Scan, please wait")
        return networkScan.portScan("192.168.0.1")

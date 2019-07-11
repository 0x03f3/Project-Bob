from SpeechRecognition.Subsystems.Hacking import networkScan
from SpeechRecognition.Subsystems.Internet import browser
from SpeechRecognition.Subsystems.Time import currentTime
from SpeechRecognition.Subsystems.Translation import translation
#import pyttsx3
#import speech_recognition as sr
from .. import languages
from .. import listening
#bob = pyttsx3.init()

#currentTime.getTime()



def controlTest(vocalInput):

    if vocalInput == "translation":

        # Take user input for translation
        listening.bob.say("what would you like translated")
        listening.bob.runAndWait()
        print("Listening for translation text")
        input = listening.listen()

        # Take user input for which language to translate to.
        listening.bob.say("What language would you like to translate that to")
        listening.bob.runAndWait()
        print("Listening for language")
        language = listening.listen()

        # Fix for the if column using index() position
        # Languages must be entered in capitalized format.
        languageList = ["English", "German", "Spanish", "Polish", "Hindi"\
                        "Arabic", "Portugese", "Russian", "Japanese", "Korean", \
                        "French"]

        # Nominatim list for translate() function assignement.
        nominatimList = ["EN", "DE", "ES", "PL", "HI", "AR", "PT", "RU", \
                         "JA", "KO", "FR"]

        # Assign selected language as it's Nominatim
        language = nominatimList[int(languageList.index(language))]

        #function return for Bob
        return translation.translate(input, language)

    # Vocal time request control
    elif vocalInput == "current time":
        # Function return for bob
        return currentTime.getTime()

    # Vocal date request control
    elif vocalInput == "current date":
        # Function return for Bob
        return currentTime.getDate()

    # Vocal network scan request
    elif vocalInput == "network scan":
        # Inform user that network scan is in progress
        listening.bob.say("Running Network Scan, please wait")
        listening.bob.runAndWait()
        # Function return for Bob
        return networkScan.portScan("192.168.0.1")

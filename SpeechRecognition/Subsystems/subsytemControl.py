from SpeechRecognition.Subsystems.Hacking import networkScan
from SpeechRecognition.Subsystems.Internet import browser
from SpeechRecognition.Subsystems.Time import currentTime
from SpeechRecognition.Subsystems.Translation import translation

currentTime.getTime()

def controlTest(vocalInput):

#    # Vocal Translation Control
#    if vocalInput == "translation":
#        input = "This is a joke."
#        language = "DE"
#        return translation.translate(input, language)

    # Vocal time request control
    if vocalInput == "current time":
        return currentTime.getTime()

    # Vocal date request control
    elif vocalInput == "current date":
        return currentTime.getDate()

    # Vocal network scan request
    elif vocalInput == "network scan":
        print("Running Network Scan, please wait")
        return networkScan.portScan("192.168.0.1")

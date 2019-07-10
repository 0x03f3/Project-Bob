from SpeechRecognition.Subsystems.Hacking import networkScan
from SpeechRecognition.Subsystems.Internet import browser
from SpeechRecognition.Subsystems.Time import currentTime
from SpeechRecognition.Subsystems.Translation import translation

def controlTest(vocalInput):

    # Vocal Translation Control
    if vocalInput == "translation":
        input = "This is a manually assigned test"
        language = "DE"
        print(translation.translate(input, language))

    # Vocal time request control
    elif vocalInput == "current time":
        return currentTime.getTime()

    # Vocal date request control
    elif vocalInput == "current date":
        return currentTime.getDate()

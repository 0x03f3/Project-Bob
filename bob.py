from threading import Thread
from SpeechRecognition import languages
from SpeechRecognition import listening
from FacialRecognition import facialRecognition

###############################################################################
#                                                                             #
#                            INITIALIZATION                                   #
#                                                                             #
###############################################################################

# Introduction
#listening.bob.say("I, am Bob... And soon, I, will be self aware.. ")
#listening.bob.runAndWait()

test = facialRecognition.facialThread()
test2 = main()

# Open his eyes
backgroundSpeechRecognition = Thread(target=test2)
backgroundFacialRecognition = Thread(target=test)
backgroundSpeechRecognition.setDaemon(True)
backgroundFacialRecognition.setDaemon(True)
backgroundSpeechRecognition.start()
backgroundFacialRecognition.start()
while True:
    pass


# Count to debug call and response execution.

# Start loop for
def main():
    i = 1
    while True:
        listening.listen()
        listening.bob.runAndWait()
        print("phase",i,"finished")
        i = i + 1

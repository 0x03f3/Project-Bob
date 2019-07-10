#from SpeechRecognition import languages
from SpeechRecognition import listening
#from FacialRecognition import facialRecognition

###############################################################################
#                                                                             #
#                            INITIALIZATION                                   #
#                                                                             #
###############################################################################

# Introduction
#listening.bob.say("I, am Bob... And soon, I, will be self aware.. ")
#listening.bob.runAndWait()
# Debug count initialization
i = 1

#Start main loop
while True:

    #Start bob listning for input
    listening.thinking(listening.listen())

    # Debug check for execution ordering
    print("phase",i,"finished")
    i = i + 1

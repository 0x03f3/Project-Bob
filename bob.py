from SpeechRecognition import listening

###############################################################################
#                                                                             #
#                            INITIALIZATION                                   #
#                                                                             #
###############################################################################

# Introduction
#listening.bob.say("I, am Bob... And soon, I, will be self aware.. ")
#listening.bob.runAndWait()

while True:
    #Start bob listning for input
    listening.thinking(listening.listen())

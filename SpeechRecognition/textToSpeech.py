#DOCTUMENTATION: https://pypi.org/project/pyttsx3/

import pyttsx3

#Initialize the voice engine:

engine = pyttsx3.init()

#Speech rate assignment:

#rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
#engine.setProperty('rate', 125)     # setting up new voice rate


#Output volume assignment

#volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
#engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

#Voice value assignment:

#voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#Print all available Voices:

#voices = engine.getProperty('voices')
#for voice in voices:
#    print("Voice:")
#    print(" - ID: %s" % voice.id)
#    print(" - Name: %s" % voice.name)
#    print(" - Languages: %s" % voice.languages)
#    print(" - Gender: %s" % voice.gender)
#    print(" - Age: %s" % voice.age)

engine.say("Hello, My name is Bob. How're you today")

engine.runAndWait()

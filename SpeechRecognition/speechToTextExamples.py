#DOCUMENTATION: https://pypi.org/project/SpeechRecognition/


import speech_recognition as sr

#Test clause for finding the list of audio devices compatible with Microphone()
#To alter the device change Microphone() to Microphone(device_index=<indexNum>)

#Code:
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

#Set Recognizer()
r = sr.Recognizer()

#Assign Microphone and await speech
with sr.Microphone() as source:
    print('Speak: ')
    audio = r.listen(source)

#Assign speech recognizer (Google - Online | Sphinx - Offline) and pass through audio
    try:
        text = r.recognize_google(audio)

#Output formatted text or inform that input was not reconized
        print('You said: {}'.format(text))
    except:
        print('Sorry could not understand your input: ')

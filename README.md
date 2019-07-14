# Project-Bob
Creating a physical AI assistant known as Bob.

## Speech Recognition:

### Subroutines

Access subroutines by saying "Subroutine" or any of the stamenets found within the "commandList" found within:
"/SpeechRecognition/languages.py" 
You can add your own vocal triggers for command execution.

A list of executable conmmands once subroutine has been triggered can be found within: 
"/SpeechRecognition/Subsystems/subsytemControl.py"

The general formatting for executing subroutine commands is as follows: 

```python3

def controlTest(vocalInput):

    if vocalInput == "current time":
        return currentTime.getTime()

```
The command functions will be kept within the subsytem directory based on cammand type: 
"SpeechRecognition/Subsystems/Time/currentTime.py"

### How the Speech Recognition functions:

Bob's main functionallity comes from a single line within "bob.py":

```python3
while True:
    #Start bob listning for input
    listening.thinking(listening.listen())
```

This executes the main "thinking(text)" function to accept input from the "listen()" function.

"thinking(test)" is generally quite a simple function, checking user input against lists found in "/SpeechRecognition/languages.py"

from this he will determin what would be the most appropriate response or subsytem trigger to implement or reply with.

So far he will respind in kind to greetings and farewells in english, this can be changed to 11 different languages all found within "/SpeechRecognition/languages.py" by changing the 
```python3
bob.say(str(languages.english(4)[random.randint(1, len(languages.english(4))-1)]))
```
to something like
```python3
bob.say(str(languages.german(4)[random.randint(1, len(languages.german(4))-1)]))
```
This functionallity is planning on being automated by detecting the users voice inputs and determining their language at startup.

### This is still in development and not yet finished, His name is Bob!

For a visual example of him in action please see the potato quality video here: 

<a href="http://www.youtube.com/watch?feature=player_embedded&v=SO97TJRWmdA
" target="_blank"><img src="http://img.youtube.com/vi/SO97TJRWmdA/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

## Facial Recognition:

The facial recognition system is able to detect individuals and assign the probability of their names, alternatively it is able to recognize if the individual is unknown allowing for further learning and recognition of new people.

Facial recognition data will eventually be interconnect to the speech recognition system via socket data transfers, allowing central processing system.

### Training the facial recognition system:

(This process will eventually be automated via daily training of new individual encounters and asking a known user the people's names)

#### Step 1)

- Place Images within "FacialRecogntion/TrainingData" under a folder with the persons name as the folder title.
- It's best dvised t make sure the images only contain a single front facing face
- The more images of individuals given to "TraningData/<PersonsName>" the greater results for facial detection

#### Step 2)

- Run "FacialRecogntion/extractFaces.py" in order to process the "FacialRecognition/TrainingData/*" images which will populate the "FacialRecogntion/PickleFiles/extraction.pickle" data file

#### Setp 3) 

- Run "FacialRecogntion/training.py" to train the Deep Neural Network and assign the data list values such as face extraction and name labels which will populate the "FacialRecogntion/PickleFiles/faceDetection.pickle" and "FacialRecogntion/PickleFiles/namedLabels.pickle" data files

#### Step 4) 

- You can now run "FacialRecogntion/facialRecognition.py" to initiate the OpenCV video stream that has been trained against the provided images, this will now automatically detect what it predicts each detected face to belong to or alternatively inform you that the face is "Unknown" 


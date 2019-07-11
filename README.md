# Project-Bob
Creating a physical AI assistant known as Bob.

## Current Features:

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

### How he functions:

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

### This is still in development and not yet a finished development, he is bob, and soon he will be self aware!

For a visual example of him in action please see the potato quality video here: 

<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank"><img src="http://img.youtube.com/vi/SO97TJRWmdA/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>


#DOCUMENTATION: https://pypi.org/project/googletrans/
from googletrans import Translator

# Function to take text input and a nominatim and translate the input
# into that Nominatim

def translate(input, language):

    # Assign Translator() to variable
    translator = Translator()
    # Print Debug
    print(str(translator.translate(input, dest=language)))









    # Assign first split
    #Output = str(translator.translate(input, dest=language)).split(",")
    # Print Debug
    #print(Output)
    #translation = str(Output[2]).split("=")
    # Print Debug
    #print(translation)
    # Only want to return the direct translation within the
    #print(str(translation[1]))

#Function to take text input and detect the language being passed.
def languageDetection(input):

    #Assign Translator() to variable
    translator = Translator()
    # Print out the result for readability, remember to change to return.
    return translator.detect(input)

#languageDetection("Это тест")
#translate("hello my name is bob", "DE")

#DOCUMENTATION: https://pypi.org/project/googletrans/
from googletrans import Translator

# Function to take text input and a nominatim and translate the input
# into that Nominatim

def translate(input, language):

    # Assign Translator() to variable
    translator = Translator()

    # Only want to return the direct translation within the
    test = str(translator.translate(input, dest=language))
    test2 = test.split(",")
    test3 = str(test2[2])
    test4 = test3.split("=")
    return str(test4[1])
    # Only want to return the direct translation within the

#Function to take text input and detect the language being passed.
def languageDetection(input):

    #Assign Translator() to variable
    translator = Translator()
    # Print out the result for readability, remember to change to return.
    return translator.detect(input)

#languageDetection("Это тест")
translate("hello", "DE")

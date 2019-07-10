#DOCUMENTATION: https://pypi.org/project/googletrans/

from googletrans import Translator

# Function to take text input and a nominatim and translate the input
# into that Nominatim

def translate(input, language):

    #Assign Translator() to variable
    translator = Translator()

    # Print out the result for readability, remember to change to return.
    print(translator.translate(input, dest=language))


translate("Это тест", "en")


#Function to take text input and detect the language being passed.
def languageDetection(input):

    #Assign Translator() to variable
    translator = Translator()
    # Print out the result for readability, remember to change to return.
    print(translator.detect(input))

#languageDetection("Это тест")

def english(list):

    greetingList = ["Hello", "Hi", "Hey", "How's it going?", "How are you?",\
                    "What's up", "What's new?", "How's everything", \
                    "How are things?", "How's Life?", "How's your day?", \
                    "How's your day going?", "Good to see you!", \
                    "Nice to see you", "Long time no see", "It's been a while"]

    enquireList = ["What can I help with today?", "What can I do for you?",\
                  "What will you have me do?", "How can I help you?"]

    farewellList = ["bye", "bye bye", "See you later", "See you soon", \
                    "Talk to you later", "I must be going", "Take it easy",\
                    "I'm off too", "Goodbye", "Have a good day",\
                    "Have a nice day", "I'll look forward to our next meeting"\
                    "Until next time", "Take care", "It was nice talking to you"\
                    "It was nice seeing you", "Until later", "Peace out"]

    errorHandling = ["Sorry I didn't catch that", "Sorry I wasn't listening"\
                     "Could you repeat that again", "What"]

    if list == 1:
        return greetingList
    elif list == 2:
        return enquireList
    elif list == 3:
        return farewellList
    elif list == 4:
        return errorHandling
    else:
        print("Incorrect")

def german(list):

    greetingList = ["Hallo", "Gutten Tag", "Wie geht's?", "Wie geht es Ihnen?"\
                    "Wie ist alles", "Wie läuft dein Tag", "schön dich zu sehen"\
                    "schön dich wieder zu sehen", "lange nicht gesehen", \
                    "Es ist eine Weile her"]

    enquireList = ["Womit kann ich helfen?", "Was kann ich für Dich tun?",\
                  "Was soll ich tun?", "Wie kann ich Ihnen heute helfen?"]

    farewellList = ["Tschüss", "bis später", "bis bald", "Wir sprechen später"\
                    "Ich muss gehen", "Nimm es nicht so schwer", "Ich bin weg"\
                    "Auf Wiedersehen", "haben Sie einen guten Tag",\
                    "Einen schönen Tag noch", "Ich freue mich auf unser nächstes Treffen"\
                    "es war schön dich wieder zu sehen", "bis zum nächsten Mal"]

    errorHandling = ["Entschuldigung, das habe ich nicht verstanden",\
                     "Entschuldigung, ich habe nicht zugehört"\
                     "Könnten Sie das noch einmal wiederholen?", "Was"]

    if list == 1:
        return greetingList
    elif list == 2:
        return enquireList
    elif list == 3:
        return farewellList
    elif list == 4:
        return errorHandling
    else:
        print("Incorrect")

def spanish():
    pass

def polish():
    pass

def chinese():
    pass

def hindi():
    pass

def arabic():
    pass

def portuguese():
    pass

def bengali():
    pass

def russian():
    pass

def japanese():
    pass

def korean():
    pass

def french():
    pass

def turkish():
    pass

def vietnamese():
    pass

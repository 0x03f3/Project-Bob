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
        print("English Response ERROR")

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
        print("German Response ERROR")

def spanish(list):

    greetingList = ["Hola", "Oye", "cómo te va", "cómo estás",\
                    "que pasa", "qué hay de nuevo", "como esta todo", \
                    "cómo van las cosas", "como es la vida", "como va tu dia", \
                    "que bueno verte", "me alegro de verte",\
                    "mucho tiempo sin verte", "ha sido un tiempo"]

    enquireList = ["En qué puedo ayudar hoy", "Qué puedo hacer por ti",\
                   "Que me quieres hacer", "como puedo ayudarte"]

    farewellList = ["bye", "bye bye", "Hasta luego", "Hasta pronto", \
                    "Hablamos luego", "Debo irme", "Tómalo con calma", \
                    "Yo también me voy", "Adiós", "Que tengas un buen día", \
                    "Que tenga un buen día", "Espero con interés nuestra próxima reunión", \
                    "Hasta la próxima", "Cuídate", "Fue agradable hablar contigo",\
                    "Fue agradable verte", "Hasta más tarde", "Paz fuera"]

    errorHandling = ["Lo siento, no pude captar eso", "Lo siento, no estaba escuchando"
                     "Podrías repetir eso otra vez", "Qué"]

    if list == 1:
        return greetingList
    elif list == 2:
        return enquireList
    elif list == 3:
        return farewellList
    elif list == 4:
        return errorHandling
    else:
        print("Spanish Response ERROR")

def polish(list):

    greetingList = ["Cześć", "Cześć", "Hej", "Jak leci", "Jak się masz", \
                    "Co słychać", "Co nowego", "Jak się ma wszystko", \
                    "Jak się mają sprawy", "Jak tam życie", "Jak się masz?",\
                    "Jak ci mija dzień", "Dobrze cię widzieć",\
                    "Miło cię widzieć", "Dawno nie widziałem", "Minęło trochę czasu"]

    enquireList = ["W czym mogę pomóc dzisiaj", "Co mogę dla ciebie zrobić",\
                   "Co mam zrobić", "Jak mogę ci pomóc"]

    farewellList = ["pa", "pa pa", "Do zobaczenia później", "Do zobaczenia wkrótce",\
                    "Porozmawiaj z tobą później", "Muszę iść", "Spokojnie",\
                    "Ja też jestem", "Do widzenia", "Miłego dnia",\
                    "Miłego dnia", "Czekam na nasze następne spotkanie"\
                    "Do następnego razu", "Uważaj", "Miło było z tobą rozmawiać"\
                    "Miło było cię widzieć", "Do później", "Spokój"]

    errorHandling = ["Przepraszam, że tego nie złapałem", "Przepraszam, że nie słuchałem"\
                     "Czy możesz powtórzyć to jeszcze raz", "Co"]

    if list == 1:
        return greetingList
    elif list == 2:
        return enquireList
    elif list == 3:
        return farewellList
    elif list == 4:
        return errorHandling
    else:
        print("Polish Resopnse ERROR")

def chinese(list):

    greetingList = ["Nǐ hǎo","hāi","hēi","zěnme yàng","Nǐ hǎo ma",\
                    "Shénme shìqíng","shénme shì xīn de","Yīqiè rúhé",\
                    "shìqíng zěnme yàng","Shēnghuó zěnme yàng",\
                    "Jīntiānguò dé zěnme yàng","Nǐ jīntiānguò dé zěnme yàng",\
                    "Hěn gāoxìng jiàn dào nǐ","hǎojiǔ bùjiàn",\
                    "yǐjīng yǒu yīduàn shíjiānle"]

    enquireList = ["Jīntiān wǒ néng bāng dào shénme","Wǒ néng wéi nǐ zuò xiē shénme",\
                   "Nǐ yào wǒ zuò shénme","Wǒ zěnme néng bāng dào nǐ"]

    farewellList = ["Zàijiàn","zàijiàn","jiàn dào nǐ","hěn kuài jiàn dào nǐ",\
                    "shāo hòugēn nǐ shuōhuà","wǒ yīdìng yào qù","fàng qīngsōng",\
                    "wǒ yě líkāile","zàijiàn","zhù nǐ yǒu gè měihǎo de yītiān",\
                    "zhù nǐ yǒu gè měihǎo de yītiān","wǒ qídàizhuó wǒmen de xià yīcì huìyì"\
                    "zhídào xià yīcì","bǎozhòng","hěn gāoxìng hé nǐ shuōhuà"\
                    "hěn gāoxìng jiàn dào nǐ","zhídào yǐhòu","hépíng chūjú"]

    errorHandling = ["Duìbùqǐ, wǒ méiyǒu zhuā dào nàgè","bàoqiàn, wǒ méiyǒu tīng"\
                     "nǐ néng zài chóngfù yīcì ma","shénme"]

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

def hindi(list):

    greetingList = ["hailo", "haay", "he", "yah kaise ho raha hai?",\
                    "aap kaise hain?", "kya ho raha hai", "kya naya hai?", \
                    "kaise sab kuchh hai", "cheejen kaisee hain?",\
                    "kaise jeevan hai?", "aapaka din kaisa hai?",\
                    "aapaka din kaisa chal raha hai?", "gud too yoo yoo!", \
                    "aapako dekhakar achchha laga", "long taim no vyoo", \
                    "thodee der ho gaee"]

    enquireList = ["main aaj kya madad kar sakata hoon",\
                    " main aapake lie kya kar sakata hoon", "aap mere paas kya karenge?",\
                    "main aapakee kaise madad kar sakata hoon"]

    farewellList = ["alavida", "alavida", "baad mein milate hain", "jald hee milate hain",\
                    "aap baad mein baat karen", "mujhe jaana chaahie", "ise aasaan lo",\
                    "main bhee", "alavida", "ek achchha din hai",\
                    "aapaka din shubh ho," "main hamaaree agalee baithak ke lie tatpar hoon",\
                    "agalee baar tak", "dhyaan rakhana", "aapase baat karake achchha laga",\
                    "aapako dekhakar achchha laga", "baad mein", "pees aaut"]

    errorHandling = ["maaph karana, mainne nahin pakada", "maaph karana main sun nahin raha tha"\
                     "kya aap phir se dohara sakate hain", "kya"]

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

def arabic(list):

    greetingList = ["mrhbana" , "mrhbana" , "mrhbana" , "kyf alhal?" , "kyf halk?" , \
                    "ma alamr" , "ma aljdyd?" , "kyf alhal" , \
                    "kif hi al'ashya'?" , "kyf hi alhaya?" , "kyf hu yumak?" , \
                    "kif hal yawmak?" , "mn aljayd 'an 'arak!" , \
                    "jimil 'an arak" , "wqat tawil la 'araa" , "lqad kan alwaqt"]

    enquireList = ["madha yumkinuni 'ana 'usaeid alyawm?" , "madha yumkinuni 'an 'afeal lk?" , \
                   "madha sayakun ladayk ly?" , "kyf yumkinuni musaeidtuka?"]

    farewellList = ["madha yumkinuni 'ana 'usaeid alyawm?" , "madha yumkinuni 'an 'afeal lk?" , \
                   "madha sayakun ladayk ly?" , "kyf yumkinuni msaeidtk?" "wdaea" , "wdaeaan wadaea" , "arak lahqa" , "arak qariba" , \
                    "tuhduth 'iilayk lahqana" , "yjab 'an adhhb" , "khdh al'umur bshul" , \
                    "'ana kharij 'ayda" , "wdaea" , "atamnaa lak yawm jyd" , \
                    "'atmnaaan lak ywmana seydana" , "swaf 'atatlue 'iilaa aijtimaeina altali" \
                    "hataa fi almarat alqadima" , "aetn" , "kan min aljayd 'an 'atahadath 'iilaykum" \
                    "kan min aljayd rwytka" , "htaa waqt lahqa" , "alsalam kharja"]

    errorHandling = ["asafa lm 'atamakan min ailtiqat dhlk" , "asifun lm 'akun 'astame" \
                     "hil ymkn 'an tukarr dhlk marat 'ukhraa" , "madha"]

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

def portuguese(list):

    greetingList = ["Olá", "Olá", "Hey", "Como está indo?", "Como você está?"\
                    "What's up", "O que há de novo?", "Como está tudo", \
                    "Como estão as coisas?", "Como está a vida?", "Como está seu dia?"\
                    "Como vai o seu dia?", "Bom te ver!",\
                    "Prazer em vê-lo", "Muito tempo sem ver", "Já faz um tempo"]

    enquireList = ["Com o que posso ajudar hoje?", "O que posso fazer por você?"\
                   "O que você vai me fazer fazer?", "Como posso ajudá-lo?"]

    farewellList = ["tchau", "tchau tchau", "Vejo você depois", "Vejo você em breve", \
                    "Falo com você depois", "Eu devo ir", "Acalme-se", \
                    "Eu estou fora também", "Adeus", "Tenha um bom dia", \
                    "Tenha um bom dia", "Estou ansioso para nossa próxima reunião" \
                    "Até a próxima vez", "Tome cuidado", "Foi bom conversar com você"\
                    "Foi bom ver você", "Até mais tarde"]

    errorHandling = ["Desculpe eu não peguei isso", "Desculpe eu não estava escutando"\
                     "Você poderia repetir isso de novo", "O que"]

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

def russian():

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

def japanese():

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

def korean():

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

def french():

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

def turkish():

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

def vietnamese():

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

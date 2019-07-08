import datetime

def getTime():
    time = datetime.datetime.now()
    print ("The current time is: " + time.strftime("%H:%M:%S"))

def getDate():

    date = datetime.datetime.now()

    if date.strftime("%m") == "01":
        month = " January "
    if date.strftime("%m") == "02":
        month = " Feburary "
    if date.strftime("%m") == "03":
        month = " March "
    if date.strftime("%m") == "04":
        month = " April "
    if date.strftime("%m") == "05":
        month = " May "
    if date.strftime("%m") == "06":
        month = " June "
    if date.strftime("%m") == "07":
        month = " July "
    if date.strftime("%m") == "08":
        month = " August "
    if date.strftime("%m") == "09":
        month = " September "
    if date.strftime("%m") == "10":
        month = " October "
    if date.strftime("%m") == "11":
        month = " November "
    if date.strftime("%m") == "12":
        month = " December "

    print (date.strftime("The date is the %dth of" + month + "%Y"))

getDate()

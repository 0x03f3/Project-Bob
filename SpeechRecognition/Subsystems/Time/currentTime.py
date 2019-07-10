import datetime

#Function to get the current time ~(Work on output format for bob to speak)
def getTime():

    # Assign datetime to time
    time = datetime.datetime.now()
    #print out the time format for testing, remember to assign return
    return "The current time is " + time.strftime("%H:%M")

def getDate():

    #List of months to make it sound normal when bob speaks
    monthList = [" January ", " Feburary ", " March ", " April ", " May ",\
                 " June ", " July ", " August ", " September ", " October ",\
                 " November", " December "]

    date = datetime.datetime.now()

    # Changed the monster 'if' column into some python voodoo
    month = monthList[int(date.strftime("%m"))-1]

    # As usual remember to
    return date.strftime("The date is the %dth of" + month + "%Y")

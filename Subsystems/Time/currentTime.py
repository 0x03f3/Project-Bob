import datetime

#Function to get the current time ~(Work on output format for bob to speak)
def getTime(input):

    # trigger if statemenet
    if input == "time":
        # Assign datetime to time
        time = datetime.datetime.now()
        #print out the time format for testing, remember to assign return
        print ("The current time is " + time.strftime("%H:%M"))
    else:
        #Inform bob that this function was not needed (Return trigger eventually)
        return "Not After Time"

getTime("time")



def getDate(input):

<<<<<<< HEAD
    #List of months to make it sound normal when bob speaks
    monthList = [" January ", " Feburary ", " March ", " April ", " May ",\
=======
#List of months to make it sound normal when bob speaks
monthList = [" January ", " Feburary ", " March ", " April ", " May ",\
>>>>>>> 9b291b4b959d659d0ccc3677eee14f4270ef3e87
             " June ", " July ", " August ", " September ", " October ",\
             " November", " December "]


    if input == "date":
        date = datetime.datetime.now()

        # Changed the monster 'if' column into some python voodoo
        month = monthList[int(date.strftime("%m"))-1]

        # As usual remember to
        print (date.strftime("The date is the %dth of" + month + "%Y"))

getDate("date")

import webbrowser


#Function to open a web page, start small, build big.
def openURL(input):

    # Assignment of available webpages
    google = "https://www.google.com"
    youtube = "https://www.youtube.com"
    localhost = "https://127.0.0.1"

    # Set website variable to the given input
    if input == "google":
        website = google
    elif input == "youtube":
        website = youtube
    elif input == "localhost":
        website = localhost

    # Execute browser operation
    webbrowser.open(website)

# Works.
#openURL("google")

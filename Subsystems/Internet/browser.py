import webbrowser

def openURL(text):

    google = "https://www.google.com"
    youtube = "https://www.youtube.com"
    localhost = "https://127.0.0.1"

    if text == "google":
        website = google
    elif text == "youtube":
        website = youtube
    elif text == "localhost":
        website = localhost

    webbrowser.open(website)

openURL()

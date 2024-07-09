import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import datetime
import geocoder
import pyautogui
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# BASIC FUNCTIONS:
def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"Master said: {query}")
            return query
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            say("Jarvis couldn't catch that. Could you please repeat?")
            return takeCommand()  # Recursively prompt the user again
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            say("I'm sorry, I'm unable to reach the speech recognition service right now.")
            return ""

 # Set up your Spotify API credentials
SPOTIPY_CLIENT_ID = 'eeaef7a2f6124bc783a1219b7eead300'
SPOTIPY_CLIENT_SECRET = '557ba87bc19f469da3e7fbe795b9c299'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-read-playback-state,user-modify-playback-state"))
def play_song(song_name):
    results = sp.search(q=song_name, limit=1)
    if results['tracks']['items']:
        song_uri = results['tracks']['items'][0]['uri']
        devices = sp.devices()
        if devices['devices']:
            device_id = devices['devices'][0]['id']  # Use the first available device
            sp.start_playback(device_id=device_id, uris=[song_uri])
            say(f"Playing {song_name} on Spotify.")
        else:
            say("No active Spotify devices found.")
    else:
        say("Sorry, I couldn't find that song on Spotify.")

# Location Information Function
def get_location():
    say("Sure sir, fetching your location.")
    print("Locating...")
    try:
        g = geocoder.ip('me', timeout=10)  # Increase the timeout value
        if g.ok:
            return g.city, g.state
        else:
            raise ValueError("Geocoder service failed.")
    except Exception as e:
        print(f"Error occurred: {e}")
        say("Sorry, I couldn't determine your location.")
        return None, None, None

# Taking Screenshots
def take_screenshot():
    say("Sure sir, Could you please tell me what should I name this file?")
    img_name = takeCommand().lower()
    say("Okay sir, Hold on, I am taking the screenshot")
    time.sleep(2)
    img = pyautogui.screenshot()
    img.save(f"{img_name}.png")


if __name__ == '__main__':
    print('J.A.R.V.I.S. IS ON')
    say("JARVIS is online. Hello Sir, how may I assist you today?")

    website_dict = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "github": "https://github.com",
        # Add more websites as needed
    }

    while True:
        query = takeCommand()
        query_lower = query.lower()

        if "open" in query_lower:
            # Extract the website name from the query
            for site in website_dict:
                if site in query_lower:
                    say(f"Yes Sir, Opening {site.capitalize()}")
                    webbrowser.open(website_dict[site])
                    break

        # todo: MAKE A DICTIONARY OF APPS TOO.
        if "visual studio code" in query_lower:
            path = r"C:\Users\hp\OneDrive - Indian Institute of Science\Desktop\Visual Studio Code.lnk"
            if os.path.exists(path):
                os.startfile(path)
                say("Opening Visual Studio Code.")
            else:
                say("Sorry Sir, I could not find the said file.")

        if "open spotify" in query:
            path = r"C:\Users\hp\OneDrive - Indian Institute of Science\Desktop\Spotify - Shortcut.lnk"
            if os.path.exists(path):
                os.startfile(path)
                say("Opening Spotify.")

        if "play" in query_lower and "on spotify" in query_lower:
            start_index = query_lower.find("play") + len("play")
            end_index = query_lower.find("on spotify")

            song_name = query[start_index:end_index].strip()
            play_song(song_name)
            print(song_name)

        elif "the time" in query_lower:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strfTime}")

        # https://ipinfo.io/json for location info
        elif "my location" in query_lower:
            city, state = get_location()
            say(f"I am not sure sir, But I think we are in {city}, in {state} of India")

        elif "screenshot" in query_lower:
            take_screenshot()
            say("Screenshot taken sir. It has been stored in the main folder of your program.")

        elif "power".lower() in query_lower:
            say("Sure Sir, Powering Off.")
            break

        # say(query)

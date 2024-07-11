# J.A.R.V.I.S. - Your Personal AI Assistant

JARVIS is an advanced AI assistant built with Python. It can recognize your voice commands to perform various tasks such as opening websites, launching applications, fetching your location, playing songs on Spotify, taking screenshots, and more.

## Features

- **Voice Command Recognition**: Uses Google's Speech Recognition API to understand your commands.
- **Text-to-Speech**: Responds back to you using `pyttsx3`.
- **Web Browsing**: Opens specified websites.
- **Application Launching**: Opens specified applications on your system.
- **Spotify Integration**: Plays songs on Spotify.
- **Geolocation**: Fetches your current location.
- **Screenshot Capture**: Takes screenshots and saves them with specified names.
- **Time Reporting**: Tells the current time.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/JARVIS.git
    cd JARVIS
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

### Setting Up Spotify API

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create a new application.
2. Note the `Client ID` and `Client Secret`.
3. Set the Redirect URI to `http://localhost:8888/callback`.

### Configuration

Create a file named `config.py` in the root directory and add your Spotify API credentials:

```python
SPOTIPY_CLIENT_ID = 'your_spotify_client_id'
SPOTIPY_CLIENT_SECRET = 'your_spotify_client_secret'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'
```

## Usage
Run the main.py file to start JARVIS:

```sh
python main.py
```
### Example Voice Commands
- **Open Websites**: "Open YouTube", "Open Google", "Open GitHub"
- **Launch Applications**: "Open Visual Studio Code", "Open Spotify"
- **Play Songs on Spotify**: "Play [song name] on Spotify"
- **Fetch Location**: "What is my location?", "Where am I?"
- **Take Screenshot**: "Take a screenshot"
- **Tell Time**: "What is the time?"
- **Greeting**: "Hello Jarvis"

### Notes
- Ensure your microphone is connected and working.
- For Spotify functionality, ensure you have an active device (e.g., the Spotify app open on your phone or computer).

## Troubleshooting
- If you encounter issues with the Spotify API, ensure your device is active and connected.
- If speech recognition fails, check your microphone settings and internet connection.
- For geolocation errors, ensure you have a stable internet connection.

## Acknowledgements

- SpeechRecognition
- pyttsx3
- Webbrowser
- Geocoder
- pyautogui
- Spotipy

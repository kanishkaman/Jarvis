<!DOCTYPE html>
<html>
<head>
    <title>J.A.R.V.I.S. - Your Personal A.I. Assistant</title>
</head>
<body>
    <h1>J.A.R.V.I.S. - Your Personal A.I. Assistant</h1>
    <p>J.A.R.V.I.S. (Just A Rather Very Intelligent System) is a personal assistant project that uses voice commands to perform various tasks. The assistant can open websites, tell the time, play songs on Spotify, fetch location information, take screenshots, and more.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Voice Interaction</strong>: Interact with JARVIS using voice commands.</li>
        <li><strong>Web Browsing</strong>: Open popular websites like YouTube, Google, GitHub, etc.</li>
        <li><strong>App Launching</strong>: Launch applications like Visual Studio Code and Spotify.</li>
        <li><strong>Play Songs on Spotify</strong>: Play specific songs on Spotify using voice commands.</li>
        <li><strong>Location Information</strong>: Fetch and announce the current location.</li>
        <li><strong>Screenshot</strong>: Take a screenshot and save it with a user-specified name.</li>
        <li><strong>Time</strong>: Announce the current time.</li>
    </ul>

    <h2>Installation</h2>
    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.7 or higher</li>
        <li>Virtual Environment (optional but recommended)</li>
    </ul>

    <h3>Dependencies</h3>
    <p>Install the required libraries using pip:</p>
    <pre><code>pip install speechrecognition pyttsx3 webbrowser geocoder pyautogui spotipy requests</code></pre>

    <h3>Setting Up Spotify API</h3>
    <ol>
        <li>Go to the <a href="https://developer.spotify.com/dashboard/applications">Spotify Developer Dashboard</a> and create a new application.</li>
        <li>Note the <code>Client ID</code> and <code>Client Secret</code>.</li>
        <li>Set the Redirect URI to <code>http://localhost:8888/callback</code>.</li>
    </ol>

    <h3>Configuration</h3>
    <p>Create a file named <code>config.py</code> in the root directory and add your Spotify API credentials:</p>
    <pre><code>SPOTIPY_CLIENT_ID = 'your_spotify_client_id'
SPOTIPY_CLIENT_SECRET = 'your_spotify_client_secret'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'</code></pre>

    <h2>Usage</h2>
    <p>Run the <code>main.py</code> file to start JARVIS:</p>
    <pre><code>python main.py</code></pre>

    <h3>Example Voice Commands</h3>
    <ul>
        <li><strong>Open Websites</strong>: "Open YouTube", "Open Google", "Open GitHub"</li>
        <li><strong>Launch Applications</strong>: "Open Visual Studio Code", "Open Spotify"</li>
        <li><strong>Play Songs on Spotify</strong>: "Play [song name] on Spotify"</li>
        <li><strong>Fetch Location</strong>: "What is my location?", "Where am I?"</li>
        <li><strong>Take Screenshot</strong>: "Take a screenshot"</li>
        <li><strong>Tell Time</strong>: "What is the time?"</li>
        <li><strong>Greeting</strong>: "Hello Jarvis"</li>
    </ul>

    <h3>Notes</h3>
    <ul>
        <li>Ensure your microphone is connected and working.</li>
        <li>For Spotify functionality, ensure you have an active device (e.g., the Spotify app open on your phone or computer).</li>
    </ul>

    <h2>Troubleshooting</h2>
    <ul>
        <li>If you encounter issues with the Spotify API, ensure your device is active and connected.</li>
        <li>If speech recognition fails, check your microphone settings and internet connection.</li>
        <li>For geolocation errors, ensure you have a stable internet connection.</li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.</p>

    <h2>Acknowledgements</h2>
    <ul>
        <li><a href="https://pypi.org/project/SpeechRecognition/">SpeechRecognition</a></li>
        <li><a href="https://pypi.org/project/pyttsx3/">pyttsx3</a></li>
        <li><a href="https://docs.python.org/3/library/webbrowser.html">Webbrowser</a></li>
        <li><a href="https://pypi.org/project/geocoder/">Geocoder</a></li>
        <li><a href="https://pypi.org/project/PyAutoGUI/">pyautogui</a></li>
        <li><a href="https://spotipy.readthedocs.io/">Spotipy</a></li>
    </ul>
</body>
</html>


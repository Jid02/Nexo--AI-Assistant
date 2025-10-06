import speech_recognition as sr
import webbrowser
import pyttsx3
#import time
import requests
import json
from openai import OpenAI
import wikipedia
import yt_dlp

# --- Replace with your actual API keys ---
OPENAI_API_KEY = "**"
NEWS_API_KEY = "**"

# --- OpenAI client ---
client = OpenAI(api_key=OPENAI_API_KEY)

# --- Example music library (musicLibrary.py alternative) ---
music = {
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc"
}

# --- Text to speech ---
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)   # voices[1] for female
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

# --- Play YouTube song ---
def play_on_youtube(song):
    try:
        search_url = f"ytsearch1:{song}"  # fetch top result
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
            'default_search': 'ytsearch',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(search_url, download=False)
            if "entries" in info and len(info["entries"]) > 0:
                video_url = info["entries"][0]["webpage_url"]
                speak(f"Playing {song} from YouTube")
                webbrowser.open(video_url)
            else:
                raise Exception("No results found")
    except Exception as e:
        print(f"YouTube play error: {e}")
        speak(f"Sorry, I could not play {song} from YouTube.")

# --- Command processor ---
def processcommand(c):
    print(f"Command received: {c}")
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")

    elif "open gmail" in c:
        webbrowser.open("https://www.gmail.com")

    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com")

    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")

    elif c.startswith("play"):
        parts = c.split(" ", 1)
        if len(parts) > 1:
            song = parts[1].lower()
            if song in music:
                speak(f"Playing {song} from your library")
                webbrowser.open(music[song])
            else:
                play_on_youtube(song)
        else:
            speak("Please tell me which song to play.")

    elif "headlines" in c.lower():
        try:
            r = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
            )
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                print("Top Headlines:\n")
                for article in articles[:5]:
                    print(article["title"])
                    speak(article["title"])
            else:
                speak("Sorry, I could not fetch the news right now.")
        except Exception as e:
            print(f"News API error: {e}")
            speak("Sorry, I could not fetch the news.")

    else:
        # --- Fallback to OpenAI ---
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": 
                     "You are Nexo, a helpful voice assistant. "
                     "Always respond in JSON with this format: "
                     '{"action": "open_site/chat/search/play", "content": "..."}'},
                    {"role": "user", "content": c}
                ],
                response_format={"type": "json_object"}
            )

            ai_reply = response.choices[0].message.content
            data = json.loads(ai_reply)

            # Handle actions
            if data["action"] == "open_site":
                url = data["content"]
                speak(f"Opening {url}")
                webbrowser.open(url)

            elif data["action"] == "chat":
                reply = data["content"]
                print("AI:", reply)
                speak(reply)

            elif data["action"] == "search":
                query = data["content"]
                speak(f"Searching for {query}")
                try:
                    summary = wikipedia.summary(query, sentences=2)
                    #print("Summary:", summary)
                    speak(summary)
                except Exception:
                    speak("I couldn’t find a Wikipedia summary, opening Google.")
                url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
                webbrowser.open(url)

            elif data["action"] == "play":
                song = data["content"].lower()
                if song in music:
                    speak(f"Playing {song} from your library")
                    webbrowser.open(music[song])
                else:
                    play_on_youtube(song)

            else:
                speak("Sorry, I don't know how to handle that yet.")

        except Exception as e:
            print(f"OpenAI API Error: {e}")
            speak("Sorry, I could not process that right now.")

# --- Main loop ---
if __name__ == "__main__":
    speak("Initializing Nexo...")
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:   # keep mic open the whole time
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        while True:
            try:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                try:
                    word = recognizer.recognize_google(audio)
                    print(f"Heard: {word}")
                except sr.UnknownValueError:
                    continue

                if "nexo" in word.lower():
                    # Wake word detected → respond immediately
                    print("Wake word detected!")
                    speak("Yes")

                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)

                    try:
                        command = recognizer.recognize_google(audio)
                        print(f"Recognized command: {command}")
                        processcommand(command)
                    except sr.UnknownValueError:
                        speak("Sorry, I didn’t catch that.")

            except Exception as e:
                print(f"Error: {e}")

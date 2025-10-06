# 🧠 Nexo – The Bridge Between You and Intelligence 🌉

![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Python](https://img.shields.io/badge/Built%20with-Python%203.10+-yellow?style=flat-square\&logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-lightgrey?style=flat-square\&logo=openai)

> **Nexo** is a powerful **AI voice assistant** that listens, understands, and acts — whether that means answering your questions, fetching news, playing music, or opening websites — all through your voice.
> “**Nexo – The bridge between you and intelligence.**” 🌉🧠

---

## 🚀 Overview

**Nexo** combines **speech recognition**, **OpenAI GPT**, and **automation** to provide an interactive, voice-controlled desktop assistant.

It can:

🎙️ Listen to your voice commands

💬 Understand your intent using GPT-based reasoning

🌍 Fetch live information like news, Wikipedia summaries, and Google results

🎵 Play songs from YouTube

🌐 Open popular websites automatically

🗣️ Respond naturally using text-to-speech

---

## 🌟 Features

| Category                     | Description                                                      |
| ---------------------------- | ---------------------------------------------------------------- |
| 🗣️ **Voice Activation**     | Wake up Nexo with the keyword “**Nexo**”.                        |
| 💬 **Conversational AI**     | Uses GPT-4o-mini to understand and reply contextually.           |
| 🔍 **Smart Search**          | Performs Google and Wikipedia lookups for any topic.             |
| 📰 **News Headlines**        | Fetches the latest headlines using the News API.                 |
| 🎧 **Play Music**            | Plays requested songs from YouTube or local library.             |
| 🌐 **Website Shortcuts**     | Opens common sites (Google, YouTube, Instagram, etc.) instantly. |
| 🧩 **JSON-Based AI Control** | GPT replies with structured JSON to trigger accurate actions.    |
| 🧠 **Offline TTS**           | Uses `pyttsx3` for smooth, offline text-to-speech.               |

---

## 🧰 Tech Stack

| Component              | Technology                               |
| ---------------------- | ---------------------------------------- |
| 🎙️ Speech Recognition | `speech_recognition` (Google Speech API) |
| 🧠 AI Intelligence     | `OpenAI GPT-4o-mini`                     |
| 🔈 Text-to-Speech      | `pyttsx3`                                |
| 🌍 Web Control         | `webbrowser`                             |
| 🎵 YouTube Music       | `yt_dlp`                                 |
| 📰 News                | `NewsAPI`                                |
| 🔎 Info Lookup         | `wikipedia`                              |
| 🧾 JSON Logic          | Python built-in `json`                   |

---

## ⚙️ Setup and Installation

Follow these steps to run **Nexo** on your system 👇

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Jid02/nexo-voice-assistant.git
cd nexo-voice-assistant
```

### 2️⃣ Install Dependencies

```bash
pip install speechrecognition pyttsx3 openai requests wikipedia yt_dlp
```

### 3️⃣ Add Your API Keys

```
OPENAI_API_KEY=your_openai_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

### 4️⃣ Configure Microphone Permissions

Ensure your system microphone access is enabled.

### 5️⃣ Run the Program

```bash
python nexo.py
```

---

## 🧠 How It Works

1. **Wake Word Detection** – Listens continuously for the word “Nexo”.
2. **Command Recognition** – Converts speech to text and interprets meaning.
3. **Intent Processing** – Uses GPT JSON output to determine the next action.
4. **Execution** – Opens websites, plays music, fetches news, or responds conversationally.
5. **Voice Feedback** – Uses `pyttsx3` to read the response aloud.

---

## 🔐 Safety & Notes

* 🚫 **Do not share API keys** publicly — use `.env` files or environment variables.
* 🎤 Keep the mic close for better recognition.
* 🧭 Some features (YouTube playback, News) need internet connectivity.
* 💡 You can modify wake words, voices, or add custom commands easily.

---

## 🌈 Example Commands

| Command                       | Action                         |
| ----------------------------- | ------------------------------ |
| “Nexo, open YouTube”          | Opens YouTube in the browser.  |
| “Nexo, play Believer”         | Plays *Believer* from YouTube. |
| “Nexo, tell me the headlines” | Reads top 5 news headlines.    |
| “Nexo, who is Elon Musk?”     | Gives a Wikipedia summary.     |
| “Nexo, open Instagram”        | Opens Instagram in browser.    |

---

## 🔮 Future Enhancements

* 🗓️ Calendar & reminder integration
* 📧 Gmail automation
* 💬 Local chat history memory
* 🔊 Wake word detection using VAD (Voice Activity Detection)
* 🌤️ Weather updates via API

---

## 👩‍💻 Developer

**Developed by:** [Jidnyasa Pawar](https://github.com/Jid02)

💬 *AI enthusiast and coder passionate about building intelligent voice-based tools.*

---

## 📄 License

This project is open source under the **MIT License** — free to use and modify with attribution.

---

## ⭐ Support

If you like **Nexo**, please consider giving it a ⭐ on GitHub —
it motivates continued improvements and helps others discover it!

# 🤖 Jarvis2 — BlenderBot Chatbot

A terminal-based chatbot powered by Facebook’s `blenderbot-400M-distill` and Hugging Face Transformers — brought to life by Mustafaa😒.

---

## 📦 Features

- Natural language conversation
- Built on Facebook's distilled BlenderBot model
- Simple User interaction
- Voice-based chat (optional)
- Clean output formatting

---


### 1. Clone the Repository
```bash
git clone https://github.com/your-username/jarvis2-blenderbot.git
cd jarvis2-blenderbot

2. Install Dependencies
pip install -r requirements.txt

3. Run the Chatbot
python BlenderBot_🤖.py




                    Behind the Code
Jarvis2 loads the BlenderBot model using Hugging Face Transformers:


model_name = "facebook/blenderbot-400M-distill"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
User input is tokenized, processed by the model, and decoded into a human-readable reply:


inputs = tokenizer([user_input], return_tensors="pt")
outputs = model.generate(**inputs)
reply = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]


🆕 Voice Support (Jarvis2 Upgrade)
Jarvis2 now supports speech-based interaction, using the speech_recognition library. You can choose between typing or speaking your input at the start of the session.

🛠️ How It Works
The microphone is accessed via sr.Microphone().

The recognizer listens using engine.listen(source).

Google’s free speech-to-text API converts the audio:


engine.recognize_google(audio)
If speech fails or is unclear, it falls back to text input automatically.

🗣️ Voice Output (Text-to-Speech)
Jarvis2 also speaks replies out loud using Microsoft neural voices, integrated via the edge-tts library.

✨ Key Details
Uses edge_tts.Communicate to convert text to high-quality MP3

Plays audio using playsound

Automatically deletes the audio after playback to keep memory clean

Runs asynchronously using Python’s asyncio

📦 Dependencies
Make sure the following packages are installed (also available in requirements.txt):

pip install transformers
pip install torch
pip install SpeechRecognition
pip install PyAudio
pip install edge-tts
pip install playsound

📂 Branch Information
This is the voice-integration branch.
Main branch = text-only chatbot
Voice branch = upgraded with speech input + output

If you'd like to contribute or extend this feature, create a pull request from your branch into main.

👤 Author
Made with love and constant learning by Mustafaa
Just a normal introvert building an AI that listens and talks back.


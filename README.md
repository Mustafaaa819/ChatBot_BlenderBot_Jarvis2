 🤖 Jarvis2 — BlenderBot Chatbot

A terminal-based chatbot powered by Facebook’s `blenderbot-400M-distill` and Hugging Face Transformers — made it came to life by Mustafaa.

---

## 📦 Features
- Natural language conversation
- Uses Facebook's distilled BlenderBot model
- Simple CLI interface
- Clean output formatting
- Beam search enabled for better responses

---

 🚀 How to Run

1. **Clone the repo**
```bash
git clone https://github.com/your-username/jarvis2-blenderbot.git
cd jarvis2-blenderbot

Install dependencies
pip install -r requirements.txt
Run the chatbot

python BlenderBot_🤖.py

Behind the Code:
BlenderBot is loaded with Hugging Face's Transformers:

model_name = "facebook/blenderbot-400M-distill"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
Input is tokenized and sent to the model for response generation:

inputs = tokenizer([user_input], return_tensors="pt")
outputs = model.generate(**inputs)
reply = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

 Author
Made with love & learning by Mustafaa



 🆕 Voice Input Feature (BlenderBot Jarvis2 Upgrade)

This version adds "voice-based interaction" using the `speech_recognition` library.  
You folks can choose your option if you want to interact with BlenderBot using Text or Speech. (Just Give it a Try)

 🛠️ How it works:
- Microphone is accessed using `sr.Microphone()`
- engine.listen() listens to the user because Microphone is activated and connected to the Recognizer().
- Audio is converted to text via `engine.recognize_google(audio)` (a Google free API to Convert speech to text)
- Falls back to text if speech fails or user chooses typing.

 📦 Additional Requirements:
Make sure the following packages are installed:
```bash
pip install SpeechRecognition
pip install PyAudio



---



 🆕 BlenderBot Speaks back to You (Upgrade Using edge_tts and asyncio):
- Added a Text-to-Speech Library (edge_ttx) for having a word with User in Talking Mode.
- It uses asyncio alongside it which helps pyhton run different things at once.
- async def are called 'coroutines' also called as pausable functions.
- await: When different things are happening at once like saving the audio file and voice processing then await keyword comes in handy, it basically says tp python that wait for this task without crashing the whole program.

- Give it a try:

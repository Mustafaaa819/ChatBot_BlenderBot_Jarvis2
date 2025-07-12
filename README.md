# 🤖 Jarvis2 — BlenderBot Chatbot

A terminal-based chatbot powered by Facebook’s `blenderbot-400M-distill` and Hugging Face Transformers — made it came to life by Mustafaa.

---

## 📦 Features
- Natural language conversation
- Uses Facebook's distilled BlenderBot model
- Simple CLI interface
- Clean output formatting
- Beam search enabled for better responses

---

## 🚀 How to Run

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
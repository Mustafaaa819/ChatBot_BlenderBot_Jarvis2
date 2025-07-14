# What’s happening here?
# BlenderbotTokenizer: Converts text → tokens the model understands.
#
# BlenderbotForConditionalGeneration: A seq2seq model that generates text based on input.
#
# "400M": Refers to the number of parameters — small but chat-ready.


from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import time
import torch
import os,logging,warnings
import speech_recognition as sr #Speech to Text Library.
import asyncio
import edge_tts #Text to Speech Library.
from playsound import playsound


async def speak(text):
    communicate = edge_tts.Communicate(text=text, voice="en-US-GuyNeural")
    await communicate.save("response.mp3")
    playsound("response.mp3")


#SafetyChecks to shut up unnecessary Future Warnings:
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["PYTHONWARNINGS"] = "ignore"
warnings.filterwarnings("ignore")
warnings.simplefilter(action="ignore", category=FutureWarning)
logging.getLogger("transformers").setLevel(logging.ERROR)



#Main Core Logic (Load BlenderBot):
model_name = "facebook/blenderbot-400M-distill"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.padding_side = "right"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

device = torch.device("cpu") #This tells PyTorch where to run your model: on CPU or GPU ,or cuda (for GPU).
model = model.to(device)   #Moves model to CPU/GPU

print("Welcome to the Second Edition of Copy-Paste Jarvis (This time Jarvis2) (First Edition is in the Same Repo, check out ChatBot Transformers: ")

user_name = input("Who's Here at my doorstep, Enter Your Good Name: ")
print("Let Jarvis be Awoken from his eternal Sleep! Loading Jarvis: ")
time.sleep(2)
print("........")
print(f"Throw Your Questions at me {user_name}: ")
time.sleep(1)

engine = sr.Recognizer()   #Creates a Brain that listens to the voice.

choice = input("Do you want to speak or text(s/t):  ")
while True:
    if choice == "s":
        with sr.Microphone() as source:   #Activates mic and connects it to recognizer
            print("Listening....")
            engine.adjust_for_ambient_noise(source, duration=1)  #For louder and noisy places, use duration=3 or 4 secs.
            print("Energy Threshold: ", engine.energy_threshold)
            audio = engine.listen(source, phrase_time_limit=5)  #Records sound from the mic upto the specified limit.

        try:
            input_of_user = engine.recognize_google(audio)
            print(f"{user_name} (via mic): {input_of_user}")

        except sr.UnknownValueError:
            print("Sorry, Jarvis2 wasn't able to understand you.")
            continue
        except sr.RequestError:
            print("No internet Connection. Please connect to Wifi😒.")

    elif choice == "t":
        input_of_user = input(f"{user_name}: ")

    else:
        print("Oopsie, Wrong Choice! Try 's' or 't'. ")
        continue


    byeMsg = f"Good Bye {user_name}! "
    if input_of_user.lower() == "bye" or input_of_user.lower() == "goodbye":
        asyncio.run(speak(byeMsg))
        print("Jarvis2: ", byeMsg)
        break

    #Tokenize the Input:
    inputs = tokenizer([input_of_user], return_tensors="pt", truncation=True, max_length=512)
    inputs = {k: v.to(device) for k, v in inputs.items()}  #This loop Moves input tensors to CPU/GPU

    print("Generating Response...")

    output = model.generate(**inputs, max_length=100, pad_token_id=tokenizer.pad_token_id, eos_token_id=tokenizer.eos_token_id, early_stopping=True, num_beams=3, no_repeat_ngram_size=2)

    reply = tokenizer.decode(output[0], skip_special_tokens=True)

    time.sleep(1)
    print(".....")
    asyncio.run(speak(reply))
    print("Jarvis2: ", reply)




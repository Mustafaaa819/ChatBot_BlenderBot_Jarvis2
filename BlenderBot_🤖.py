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

print("Welcome to the Second Edition of Copy-Paste Jarvis (This time Jarvis2): ")

user_name = input("Who's Talking, Enter Your Good Name: ")
print("Let Jarvis be Awoken from his eternal Sleep! Loading Jarvis: ")
time.sleep(3)
print("........")
print("Start Asking Questions: ")
time.sleep(2)


while True:
    input_of_user = input(f"{user_name}: ")
    byeMsg = f"Good Bye {user_name}! "
    if input_of_user == "bye":
        print("Jarvis2: ", byeMsg)
        break

    #Tokenize the Input:
    inputs = tokenizer([input_of_user], return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}  #This loop Moves input tensors to CPU/GPU

    print("Generating Response...")

    output = model.generate(**inputs, max_length=100, pad_token_id=tokenizer.pad_token_id, eos_token_id=tokenizer.eos_token_id, early_stopping=True, num_beams=3, no_repeat_ngram_size=2)

    reply = tokenizer.decode(output[0], skip_special_tokens=True)

    time.sleep(1)
    print(".....")
    print("Jarvis2: ", reply)





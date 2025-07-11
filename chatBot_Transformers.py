# # from transformers import pipeline, Conversation
# # import pyttsx3
# #
# # engine = pyttsx3.init()
# # voices = engine.getProperty('voices')
# # engine.setProperty('voice',voices[1].id)
# #
# #
# # chatbot = pipeline("text-generation",model="gpt2")
# #
# # while True:
# #     user = input("You: ")
# #     if user.lower() == "exit":
# #         goodBye = "Go Away! Please Don't ever come again here!"
# #         print("Jarvis: ", goodBye)
# #         engine.say(goodBye)
# #         engine.runAndWait()
# #
# #     responses = chatbot(user, max_new_tokens=50, num_return_sequences=1, do_sample=True, pad_token_id=50256 )
# #
# #     text = responses[0]['generated_text']
# #     print("Jarvis: ", text)
# #     engine.say(text)
# #     engine.runAndWait()
# #
# #
#
#
#
#
#
# from transformers import pipeline, Conversation, AutoTokenizer, AutoModelForCausalLM
# import os
# import warnings
# import logging
# #os,warnings and logging are just used to suppress annoying warning from pytorch,transformers etc. and are not part of the core logic.
#
# #Warning logs: Just to shut up internal and external warnings.
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# os.environ['PYTHONWARNINGS'] = 'ignore'
# warnings.filterwarnings('ignore',category=FutureWarning)
# warnings.simplefilter('ignore',FutureWarning)
# logging.getLogger("transformers").setLevel(logging.ERROR)
#
#
# #The Core Setup:
# model_name = "microsoft/DialoGPT-medium"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# tokenizer.padding_side = "left"
# model = AutoModelForCausalLM.from_pretrained(model_name)
#
#
# #Pipeline that contains the model name, task and tokenizer that converts text into tokens, model can understand.
# chatbot = pipeline("conversational", model=model, tokenizer=tokenizer, pad_token_id=tokenizer.eos_token_id)
#
# print("Hello I'm a DialoGPT based Jarvis, ask me anything.")
#
# user_1 = input("Enter Your Name First: ")
# while True:
#     user = input(f"{user_1}: ")
#     goodbye = f"Shutting down the Servers, GoodBye {user_1} "
#     if user == "bye":
#         print("Jarvis: ", goodbye)
#         break
#
#     conv = Conversation(user)
#
#     result = chatbot(conv)
#     reply = result.generated_responses[-1]
#
#     print("Jarvis: ", reply)







from transformers import pipeline, Conversation, AutoTokenizer, AutoModelForCausalLM
import os, logging, warnings
import pyttsx3
import time

#SafetyChecks to shut up unnecessary Future Warnings:
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["PYTHONWARNINGS"] = "ignore"
warnings.filterwarnings("ignore")
warnings.simplefilter(action="ignore", category=FutureWarning)
logging.getLogger("transformers").setLevel(logging.ERROR)

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id if len(voices)>1 else voices[0].id)

model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.padding_side = "left"
model = AutoModelForCausalLM.from_pretrained(model_name)

chatbot = pipeline("conversational",model=model, tokenizer=tokenizer, pad_token_id=tokenizer.eos_token_id)

print("Welcome to the First Ever Copy-Paste Jarvis (unlike Iron-man's): ")

user_1 = input("Who's Talking, Enter Your Good Name: ")
print("Let Jarvis be Awoken from his eternal Sleep! Loading Jarvis: ")
time.sleep(3)
print("........")
print("Start Asking Questions: ")
time.sleep(2)

conv = Conversation()

while True:
    subscriber_input = input(f"{user_1}: ")
    goodBye = f"Good Bye, {user_1}! Don't come back soon!🤖"
    if subscriber_input.lower() == "bye":
        print("Jarvis: ", goodBye)
        engine.say(goodBye)
        engine.runAndWait()
        break

    else:
        # conv = Conversation(subscriber_input)
        conv.add_user_input(subscriber_input)
        result = chatbot(conv)
        reply = result.generated_responses[-1]

        print("Jarvis: ", reply)
        engine.stop()
        engine.say(reply)
        engine.runAndWait()





















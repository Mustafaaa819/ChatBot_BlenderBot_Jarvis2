import torch
from transformers import AutoTokenizer, BlenderbotForConditionalGeneration

#load the model:
try:
    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    model.eval()

except Exception as e:
    print("Model Load Error", e)



def bot_response(user_input):
   if not user_input:
       return "Enter Something Idiot!"

   try:
       inputs = tokenizer([user_input],return_tensors="pt", truncation=True)
       with torch.no_grad():
           reply_ids = model.generate(
               **inputs,
               max_new_tokens = 100,
               do_sample = True,
               top_k = 50,
               top_p = 0.95,
               temperature = 0.7
           )

       reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
       return reply

   except Exception as e:
       return f"Error: {str(e)}"




class Conversation:
    def __init__(self,text):
        self.user_inputs = text.lower()
        self.generated_response = []

    def add_user_inputs(self,text):
        self.user_inputs.append(text)

    def reply_from_model(self,reply):
        self.generated_response.append(reply)
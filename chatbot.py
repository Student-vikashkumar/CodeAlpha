import random
import nltk
from nltk.chat.util import Chat, reflections

# Download the required NLTK data files
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

def basic_chatbot():
    print("Hello! I am a chatbot. Let's chat!")
    print("Type 'bye' to end the conversation.\n")

    responses = {
        "hello": ["Hi there!", "Hello! How can I assist you?", "Hey! Nice to meet you."],
        "how are you": ["I'm just a program, but I'm doing fine!", "I'm great, thank you for asking!"],
        "what is your name": ["I'm Chatbot, your virtual assistant.", "You can call me Chatbot."],
        "bye": ["Goodbye! Have a great day!", "See you soon!", "Bye! Take care."],
        "default": ["I'm not sure how to respond to that.", "Can you rephrase that?", "Interesting! Tell me more."]
    }

    while True:
        user_input = input("You: ").lower()
        
        if user_input == "bye":
            print(random.choice(responses["bye"]))
            break

        # Match user input to predefined responses
        if user_input in responses:
            print("Chatbot:", random.choice(responses[user_input]))
        else:
            print("Chatbot:", random.choice(responses["default"]))

# Run the chatbot
if __name__ == "__main__":
    basic_chatbot()

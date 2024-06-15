import nltk
import random
from nltk.chat.util import Chat, reflections

# Sample conversation pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi! How can I assist you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created for this example.",]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm functioning as expected!",]
    ],
    [
        r"sorry (.*)",
        ["No problem at all!", "It's okay, don't worry about it."]
    ],
    [
        r"I (.*) (location|city) (.*)",
        ["Oh, I have never been to %2, but I hear it's nice!"]
    ],
    [
        r"quit",
        ["Goodbye! Take care.", "It was nice talking to you. Bye!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand you fully.", "Can you please elaborate?"]
    ],
]

# Create the chatbot
def basic_chatbot():
    print("Hi, I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    basic_chatbot()

    

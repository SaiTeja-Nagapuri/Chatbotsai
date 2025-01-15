import random
import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data (only required once)
nltk.download('punkt')

# Predefined conversational patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How are you doing today?", "Hi! How can I help you?"]
    ],
    [
        r"(i am|i'm) (good|fine|okay|doing well)",
        ["That's great to hear! What can I do for you?"]
    ],
    [
        r"what is your name",
        ["I'm ChatBot, your friendly assistant. What's your name?"]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you, %1! How can I assist you today?"]
    ],
    [
        r"how are you",
        ["I'm just a program, but I'm doing great! How about you?"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome! Is there anything else I can help with?"]
    ],
    [
        r"bye|quit|exit",
        ["Goodbye! It was nice chatting with you. Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Could you rephrase?"]
    ]
]

# Chatbot class instance
chatbot = Chat(pairs, reflections)

# Chat function
def start_chat():
    print("Chatbot: Hi! I'm here to chat. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Entry point
if __name__ == "__main__":
    start_chat()

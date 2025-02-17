import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!", "Hi! How can I help?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "Feeling chatty!", "I'm good, thanks for asking!"],
    "what's your name": ["I'm your friendly chatbot!", "Call me ChatGPT Lite!", "I’m just a simple bot."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!", "Bye! Take care!"],
    "default": ["I'm not sure I understand.", "Could you rephrase that?", "Hmm... I don't know about that."]
}

def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Chatbot: Bye! Have a great day!")
            break
        response = responses.get(user_input, responses["default"])
        print("Chatbot:", random.choice(response))

if __name__ == "__main__":
    chatbot()

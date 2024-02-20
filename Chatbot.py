import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, thanks for asking.", "I'm good!"]
    ],
    [
        r"what is your name ?",
        ["You can call me ChatBot.", "I'm ChatBot."]
    ],
    [
        r"what can you do ?",
        ["I can answer your questions and engage in a conversation."]
    ],
    [
        r"(.*) your name ?",
        ["My name is ChatBot.", "I'm ChatBot."]
    ],
    [
        r"(.*) (weather|temperature) ?",
        ["I'm sorry, I don't have access to weather information."]
    ],
    [
        r"(.*) (good|well) (.*)",
        ["That's great!", "I'm glad to hear that."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that.", "Could you please repeat that?"]
    ]
]


chatbot = Chat(pairs, reflections)

def Bot():
    print("Hi! I'm a ChatBot. How can I help you today?")
    print("Enter 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("ChatBot:", response)
Bot()

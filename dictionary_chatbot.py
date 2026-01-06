responses = {
    "hello": "Hi! 😊",
    "how are you": "I'm fine, thanks!",
    "bye": "Goodbye! 👋"
}

print("🤖 Dictionary Based Chatbot Started")
print("Type 'bye' to exit\n")

while True:
    user_message = input("You: ")
    print("Bot:", chatbot_reply(user_message))

    if user_message.lower() == "bye":
        break
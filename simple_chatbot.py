responses = {
    "hello": "Hi! 😊",
    "how are you": "I'm fine, thanks!",
    "bye": "Goodbye! Have a nice day 👋"
}

def chatbot_reply(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "Sorry, I don't understand that.")

print("🤖 Chatbot Started!")
print("Try: hello | how are you | bye\n")

while True:
    user_message = input("You: ")
    response = chatbot_reply(user_message)
    print("Bot:", response)

    if user_message.lower() == "bye":
        break

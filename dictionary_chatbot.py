responses = {
    "hello": "Hi! 😊",
    "how are you": "I'm fine, thanks!",
    "bye": "Goodbye! 👋"
}

print("🤖 Dictionary Based Chatbot Started")

def chatbot_reply(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "Sorry, I don't understand that.")

user_message = input("You: ")
print("Bot:", chatbot_reply(user_message))
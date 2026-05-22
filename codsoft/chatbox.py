print("=== Simple ChatBot ===")
print("Type 'bye' to exit\n")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello!")

    elif "your name" in user:
        print("Bot: My name is ChatBot.")

    elif "how are you" in user:
        print("Bot: I am fine!")

    elif "ai" in user:
        print("Bot: AI means Artificial Intelligence.")

    elif "bye" in user:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
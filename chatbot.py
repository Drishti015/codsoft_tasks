print("=" * 50)
print("🤖 Rule-Based Chatbot")
print("Type 'bye' to exit")
print("=" * 50)

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Bot: I'm doing great. Thanks for asking!")

    elif "your name" in user_input:
        print("Bot: I am a Rule-Based Chatbot.")

    elif "who created you" in user_input:
        print("Bot: I was created using Python and simple if-else statements.")

    elif "python" in user_input:
        print("Bot: Python is a powerful and beginner-friendly programming language.")

    elif "java" in user_input:
        print("Bot: Java is an object-oriented programming language used for many applications.")

    elif "artificial intelligence" in user_input or "ai" in user_input:
        print("Bot: Artificial Intelligence enables machines to learn and make decisions.")

    elif "machine learning" in user_input:
        print("Bot: Machine Learning is a branch of AI where systems learn from data.")

    elif "cloud" in user_input:
        print("Bot: Cloud computing provides storage and computing services over the internet.")

    elif "college" in user_input:
        print("Bot: A college is an institution that provides higher education.")

    elif "help" in user_input:
        print("Bot: You can ask me about Python, Java, AI, Cloud Computing, or general greetings.")

    elif "thank" in user_input:
        print("Bot: You're welcome!")

    elif "time" in user_input:
        from datetime import datetime
        print("Bot: Current time is", datetime.now().strftime("%H:%M:%S"))

    elif "date" in user_input:
        from datetime import datetime
        print("Bot: Today's date is", datetime.now().strftime("%d-%m-%Y"))

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")
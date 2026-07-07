from datetime import datetime

def chatbot():
    print("=" * 40)
    print("🤖 Welcome to CodeAlpha Chatbot!")
    print("Type 'bye' anytime to exit.")
    print("=" * 40)

    while True:
        user = input("\nYou: ").lower().strip()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hello! Nice to meet you.")

        elif "how are you" in user:
            print("Bot: I'm doing great! How about you?")

        elif "your name" in user:
            print("Bot: My name is CodeAlpha ChatBot.")

        elif "my name" in user:
            name = input("Bot: What's your name? ")
            print(f"Bot: Nice to meet you, {name}!")

        elif "time" in user:
            current_time = datetime.now().strftime("%I:%M %p")
            print("Bot: Current time is", current_time)

        elif "date" in user:
            today = datetime.now().strftime("%d-%m-%Y")
            print("Bot: Today's date is", today)

        elif "joke" in user:
            print("Bot: Why do programmers prefer Python?")
            print("Bot: Because it's easy to understand! 😄")

        elif "thank" in user:
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that. Please try something else.")

chatbot()
print("="*50)
print("        🤖 RULE-BASED AI CHATBOT")
print("="*50)
print("Developer : Shubhi Shukla")
print("Project   : Artificial Intelligence - Project 1")
print("Type 'help' to see available commands.")
print("Type 'exit' to quit.")
print("="*50)

while True:

    user = input("\nYou : ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot : Hello! Welcome. How can I help you?")

    elif user == "how are you":
        print("Bot : I am functioning perfectly! 😊")

    elif user == "what is your name":
        print("Bot : I am a Rule-Based AI Chatbot.")

    elif user == "who made you":
        print("Bot : I was created as an Artificial Intelligence project.")

    elif user == "help":
        print("""
Available Commands
------------------
hi
hello
how are you
what is your name
who made you
help
exit
""")

    elif user in ["bye", "exit", "quit"]:
        print("Bot : Thank you for using the chatbot!")
        print("Bot : Have a great day! 👋")
        break

    else:
        print("Bot : Sorry, I don't understand that.")

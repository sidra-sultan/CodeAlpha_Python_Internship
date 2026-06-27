print("Welcome")

while True:
    user_input = input("Type your message: ").lower()

    if user_input in ("hello", "hi", "hey"):
        print("Hi! Nice to meet you.")

    elif user_input == "good morning":
        print("Good Morning! Hope you have a productive day.")

    elif user_input == "good afternoon":
        print("Good Afternoon! How's your day going?")

    elif user_input == "good evening":
        print("Good Evening! How are you feeling today?")

    elif user_input in ("how are you", "how are you doing"):
        print("I'm doing great! Thanks for asking.")

    elif user_input in ("i am feeling good", "i am great", "i am fine"):
        print("That's wonderful to hear!")

    elif user_input in ("i am sad", "i am upset"):
        print("I'm sorry to hear that. I hope tomorrow is better.")

    elif user_input in ("what is your name", "who are you"):
        print("I'm a simple Python chatbot created by Sidra.")

    elif user_input == "who made you":
        print("I was created by Sidra using Python.")

    elif user_input == "what can you do":
        print("I can chat with you and answer some simple questions.")

    elif user_input in ("thank you", "thanks"):
        print("You're welcome!")

    elif user_input == "help":
        print("You can greet me, ask my name, ask how I am, or type 'bye' to exit.")

    elif user_input == "python":
        print("Python is one of the most beginner-friendly programming languages.")

    elif user_input == "codealpha":
        print("CodeAlpha provides internship projects to improve programming skills.")

    elif user_input == "tell me a joke":
        print("Why do programmers prefer dark mode? Because light attracts bugs!")

    elif user_input == "motivate me":
        print("Small progress every day leads to big success. Keep learning!")

    elif user_input == "favorite language":
        print("Python is pretty enjoyable, but every language has its strengths.")

    elif user_input in ("bye", "by"):
        print("Goodbye! Have a wonderful day. 😊")
        break

    else:
        print("I'm sorry, I don't understand that.")
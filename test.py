qna = {
    "hi": "Hey",
    "how are you": "I am fine",
    "what is your name": "My name is Priyanka",
}

while True:
    qs = input("You: ")  # Provide a user-friendly prompt
    qs = qs.strip()  # Remove leading/trailing whitespace

    if qs == "quit":
        break
    elif qs in qna:
        print("Bot:", qna[qs])  # Respond with "Bot:" before the answer
    else:
        print("Bot: I don't know the answer to that question.")

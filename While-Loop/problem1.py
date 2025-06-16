while True:
    user_input = input("Enter something (type 'exit' to quit): ").strip().lower()

    if user_input == 'exit':
        break

    print(f"You entered `{user_input}` — please enter a valid input.")

while True :
    user_message =  input("Please Enter Your message (or type 'exit' to quit):").strip().lower()
    if user_message == 'exit':
        break
    if user_message.isalpha():
        print(f" You entered message is {user_message} ")
    else:
        print("Entered value is not characters")g
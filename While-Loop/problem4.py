#Challenge  # 4: Menu-Based ATM System

"""
✅ Welcome Kira!

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

🧠 Rules:
If user enters 1: print balance

If user enters 2: ask how much to deposit and update balance

If user enters 3: ask how much to withdraw

If amount > balance → show error

Else, subtract and show new balance

If user enters 4: say goodbye and exit

If input is invalid (not 1–4), show error and re-display menu

"""
atm_name = "Anime World"
user_id = "kira"
user_pin = "1234"
user_balance = 5000
attempt = 0
inside_profile_greeting = f'Welcome {user_id}! to {atm_name}'
greeting_message = f"""✅ Welcome {user_id}!

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit"""
condition = True

while condition :
    print(f"Welcome {atm_name} ATM ")
    user_id_input = input("Please enter your user id :").strip().lower()
    if user_id_input == user_id :
        while attempt < 3:
            user_pin_input = input(f"{user_id} Enter your pin :").strip()
            if not user_pin_input.isdigit():
                print("Please Enter Pin in Digits")
                continue
            if user_pin_input == user_pin :
                while condition:
                    print("___________________________")
                    print(greeting_message)
                    user_input = input("Please Choose the Options: [1-4] :").strip()
                    if user_input.isdigit():
                        user_input = int(user_input)
                        if user_input == 1:
                            print(inside_profile_greeting)
                            print(f"{user_id} your current balance is : {user_balance}$")
                            print(f"Thank you for visiting {atm_name} :)")
                        elif user_input == 2:
                            print(inside_profile_greeting)
                            print(f"{user_id} how much u want to deposit ?")
                            deposit_amount = input("Please enter the amount :").strip()
                            if deposit_amount.isdigit():
                                deposit_amount = float(deposit_amount)
                                user_balance += deposit_amount

                            else:
                                print("please enter the valid amount or may be something wrong")
                        elif user_input == 3:
                            print(inside_profile_greeting)
                            withdraw_amount = input("How much you want to withdraw amount :").strip()
                            if withdraw_amount.isdigit():
                                withdraw_amount = int(withdraw_amount)
                                if withdraw_amount < 0:
                                    print("print please enter valid amount :")
                                elif withdraw_amount <= user_balance :
                                    user_balance -= withdraw_amount
                                    print(f"Withdraw {withdraw_amount} Done Take out your money thank you for visiting :)")

                                else:
                                    print("May be Insufficient balance cant withdraw or Something else")
                            else:
                                print("please enter amount in digits")
                        elif user_input == 4:
                            # condition = False
                            # break
                            exit()

                    else:
                        print("please choose numbers from given menu :")

            else:
                attempt += 1
                print("Incorrect Password")

    else:
        print("Please enter valid user id")
        print("Thank You :)")

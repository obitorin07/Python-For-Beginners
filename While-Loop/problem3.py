## 🎯 Challenge #3: ATM PIN System 🏦

atm_pin =  "1234"
user_id = 'kira'
balance = 2500
attempt = 0
while True :
    user_name = input("Enter The User Id :").strip().lower()
    if user_name == user_id :
        while attempt < 3:
            atm_pass = input("Enter Your ATM PIN :").strip()
            if not atm_pass.isdigit():
                print("Please Enter Digits")
                continue
            if atm_pass ==atm_pin:
                print(f"Welcome {user_id}! Your current balance is {balance}.")
                exit()
            attempt += 1
            print(f"Incorrect PIN Attempt Left : {3 - attempt}")
        print('Too many incorrect attempts Try again some time later')
        break

    else:
        print('Please enter valid user id')


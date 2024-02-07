#!/usr/bin/env python3
"""Ask the user if it is raining and convert their answer to lower case
so it doesn’t matter what case they type it in. If they answer “yes”,
ask if it is windy. If they answer “yes” to this second question,
display the answer “It is too windy for an umbrella”, otherwise
display the message “Take an umbrella”. If they did not answer yes
to the first question, display the answer “Enjoy your day”. """

raining =input("It's raining ? yes/no:").lower()
if raining=="yes":
    winds = input("Is it Windy?:").lower()
    if winds=="yes":
        print("then It is too windy for an umbrealla")
    else:
        print("then take an umbrella")
else:
    print("Enjoy Your Day")
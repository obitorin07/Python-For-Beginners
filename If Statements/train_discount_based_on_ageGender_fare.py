#fare discount based on age
female_sr_citizen = 0.7
male_sr_citizen = 0.5
normal_female =0.7
normal_male =1


gender = str(input("What Is You Gender? (Male/Female):")).lower()

if gender == 'male' or gender =='female':
  if gender =='male':
    greet ="Sir"
  else:
    greet ="Mam"
  user_age = int(input(f"What is your age {greet} ?:"))

# else:
#   print("Please Provide Accurate Details") # debug purpose


# if user >= 60:

if gender == "male":
  if user_age >= 60:
    print(f"Sir for u {int(male_sr_citizen * 100)}% of fare is applicable")
  elif user_age < 60:
    print(f"Sir for u {int(normal_male * 100)}% of fare is applicable")
  else:
    print("Please sir Tell me correct age")

elif gender == "female":
  if user_age >=60:
    print(f"Mam for u {int(female_sr_citizen * 100)} % of fare is applicable")
  elif user_age <60:
    print(f"Mam for u {int( normal_female * 100)} % of fare is applicable")

else:
  print("Please Provide information Accuratly Thank You  ")







# elif age <=50:

#   if gender == "male":
#       print(f"Sir for u {int(male * 100)}% of fare is applicable")

#   elif gender == "female":
#     print(f"Mam for u {int(female * 100)} % of fare is applicable")

#   else:
#     print("Sir/Mam Please Tell Me correctly what i am asking to you because i want apply fare discount")

# else:
#   print("Something wrong")




# all comments are i try many scinario to try to make code work correctly
#  or Debug Purpose




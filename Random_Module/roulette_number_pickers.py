#!/use/bin/env python3
import random

#it picks random roulette number between 0 to 36
roulette = random.randint(1, 37)
if (roulette%2)==0:
    print("{}  Please Select Even".format(roulette))
elif roulette==0:
    print(f"{roulette} Please Select Green")
else:
    print("{} Please Select Odd".format(roulette))

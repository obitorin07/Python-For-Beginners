#!/usr/bin/env python3

import random
import string
new_pass =""
password =string.digits+string.ascii_letters+string.punctuation
length_pass =12
for i in range (length_pass):
    new_pass+=random.choice(password)

print(new_pass)


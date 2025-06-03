#Middle Name Extractor!
names = [
    "Rohit Kumar Singh",      # middle name: Kumar
    "Sneha Priya Sharma",     # middle name: Priya
    "Ajay Rao",               # no middle name, just first and last
    "Neha",                   # only one name, no middle or last
    "Rahul Devendra Jadhav"   # middle name: Devendra
]


mid_names = []
for name in names:
    mid = name.split()

    if len(mid) > 2 :
        middle = " ".join(mid[1:-1])
    else:
        middle = ""
    mid_names.append(middle)
print(mid_names)
import random

total = 0       #variable stores sum of all dice rolls
for i in range(1,6):
    dice = random.randint(1,6)
    print("roll", i + 1, ".", dice)
    total += dice
print("total", total)
if total >= 20:
    print("Well done!")
else:
    print("Sorry, you have only ", total)



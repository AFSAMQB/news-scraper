import random

# Computer random number generate karega 1 se 10 tak
computer_number = random.randint(1, 10)

# User se input lena
user_number = int(input("Enter your lucky number from 1 to 10: "))

# Condition check
if user_number == computer_number:
    print("You Win 🎉")
else:
    print("You Lost 😢")

# Optional: Computer ka number bhi show kar dein
print("Computer number was:", computer_number)


class Biryani():
    # rice = 250
    # oil = 50
    # chicken = 100
     #spices = 10
    # price = 300
     def show(self):
         print("Quantity of rice: ", self.rice)
         print("Quantity of oil: ", self.oil)
         print("Quantity of chicken: ", self.chicken)
         print("Quantity of spices: ", self.spices)
         print("Price: ", self.price)

     def spicy(self):
         self.spices = self.spices + 5
     def light(self):
         self.spices = self.spices - 5
     def __init__(self, rice, oil, chicken, spices, price):
         self.rice = rice
         self.oil = oil
         self.chicken = chicken
         self.spices = spices
         self.price = price
#object
b1 = Biryani()
#User menu
print("Press 1 for light spicy Biryani")
print("Press 2 for spices Biryani")

choice = int(input("Enter your choice: "))
if choice == 1:
    b1.light()
    print("\nYour light Biryani will be there soon😊")
    b1.show()

elif choice == 2:
    b1.spicy()
    print("\nYour spicy Biryani will bw there soon😊")
    b1.show()

else:
    print("Plz enter your choice")

b2 = Biryani(13,16,50,100,200)


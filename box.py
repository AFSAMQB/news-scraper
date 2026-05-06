class Box:               #class
    #height = 10          #features
    #width = 20          #features
    #price = 25           #features
    def show(self):             #function, self----is a key word always refer to current object
        print("Height of box is: " , self.height)            #class, object is defied after show function
        print("Width of box is: " , self.width)
        print("Price of box is: " , self.price)
    def inc_price(self):
         self.price = self.price + 5

     def __init__(self, h,w,p):
         self.height = h
         self.width = w
         self.price = (h + w) * 2

# it will no run bez of no object

#b1 = Box()    # default constructor, and it`s work to make a class object, b1 is name of Box object
#b1.inc_price()
#b1.inc_price()
#b1.show()     # show object

b2 = Box(12,15,22)
b2.show()


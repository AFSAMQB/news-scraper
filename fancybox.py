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

    def __init__(self, h, w):
         self.height = h
         self.width = w
         self.price = (h + w) * 2

class FancyBox(Box):
    def __init__(self, h,w,c,s):
         self.color = c
         self.sticker = s
         super().__init__(h,w)    #is to refer or call the parent class    #super() .show()
    def fshow(self):
         print("color is: ", self.color)
         print("sticker is: ", self.sticker)
         super().show()

fb1 = FancyBox(10,10,"blue","Happy Birthday")

fb1.fshow()


from fancybox import FancyBox
class GiftBox(FancyBox):
    def __init__(self, h,w,c,s,g):
        super().__init__(h,w,c,s)
        self.gift = g
    def gshow(self):
        super().show()
        print("gift in the box is: ", self.gift)

g = GiftBox(10,10,"blue","Happy Birthday","Watch")
g.gshow()
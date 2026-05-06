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
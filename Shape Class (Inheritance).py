# Parent class
class Shape:
    def area(self):
        pass

# Child class — Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def area(self):
        return self.length * self.width

# Child class — Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
# Create objects and print areas
rect   = Rectangle(6, 4)
circle = Circle(3)

print("Rectangle Area:", rect.area())    # 6 x 4 = 24
print("Circle Area   :", circle.area())

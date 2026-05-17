from math import pi

# Base class
class Shape:
    def area(self):
        pass

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Creating objects
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Output
print("Circle Area:", round(circle.area(), 2))
print("Rectangle Area:", rectangle.area())
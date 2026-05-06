# Parent class (Base class)
class Animal:
    def speak(self):
        print("Animal makes a sound")


# Child class 1 (Inheritance)
class Dog(Animal):
    # Polymorphism: same method name but different behavior
    def speak(self):
        print("Dog barks")


# Child class 2 (Inheritance)
class Cat(Animal):
    # Polymorphism: same method name but different behavior
    def speak(self):
        print("Cat meows")


# Function to demonstrate polymorphism
def animal_sound(animal):
    # This function works for any object that has speak() method
    animal.speak()


# Creating objects
dog = Dog()
cat = Cat()
animal = Animal()

# Calling function with different objects (Polymorphism in action)
animal_sound(dog)     # Dog class method will run
animal_sound(cat)     # Cat class method will run
animal_sound(animal)  # Animal class method will run
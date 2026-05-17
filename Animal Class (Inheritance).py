#parent class
class Animal:
    def speak(self):
        pass

    def eat(self):
        return "Animal is eating"
    
# child class
class Dog(Animal):
    def speak(self):
        return "WOOF WOOF!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

#object create
dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())
print(dog.eat())
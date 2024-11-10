# Inheritance is a mechanism that allows a class to inherit properties and behaviors from another class.
# The class that inherits properties and behaviors is called the subclass, and the class that is being inherited from is called the superclass.
# Inheritance is a powerful feature that allows for code reuse and polymorphism.

# Example of inheritance:


# Base class (Parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

# Derived class (Child class) that inherits from Animal
class Dog(Animal):
    def speak(self):
        return "Woof Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow Meow!"

# Instantiate objects of the derived classes
dog = Dog("Gruu")
cat = Cat("Ivy")

print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")


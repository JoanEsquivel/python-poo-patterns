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
# The Dog and Cat classes inherit the name attribute from the Animal class, but they can also have their own name attribute.
dog = Dog("Gruu")
cat = Cat("Ivy")

# Notice how the Dog and Cat classes inherit the speak method from the Animal class, but they can also override it with their own implementation.
print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")


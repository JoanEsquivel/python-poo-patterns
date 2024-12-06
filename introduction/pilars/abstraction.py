# https://medium.com/data-bistrot/abstraction-in-python-oop-c4da042f9eaf

# Abstraction is the process of hiding the complex details and showing only essential features of an object.
# It is a fundamental concept in object-oriented programming (OOP) that allows us to create more complex and flexible systems.
# Abstraction is achieved by creating abstract classes and interfaces that define the common behavior and properties of a group of objects.
# These abstract classes and interfaces can then be implemented by concrete classes that provide specific implementations of the behavior and properties.

# Implementing Abstraction in Python
# Python does not have built-in support for abstract classes in the way some other languages do, but it
# offers the abc module which stands for Abstract Base Classes. This module provides the infrastructure for defining custom abstract classes in Python.

# In Python, the @abstractmethod decorator is a tool used in abstract base classes (ABCs) to define methods that must be implemented by subclasses


from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Car is moving")

class Boat(Vehicle):
    def move(self):
        print("Boat is moving")

# In the example, Vehicle serves as an abstract class with a simple interface (move method).
# Car and Boat are concrete implementations of the Vehicle abstract class. 
# Clients interacting with Car or Boat instances don't need to know how move works internally; they only need to know that the method exists.

# They don't need to be concerned with how the move() method is implemented internally in each subclass.
# This abstraction allows clients to use Car and Boat instances interchangeably, relying on the common interface provided by the Vehicle abstract class without needing to understand the specific details of each vehicle's movement mechanism.
# This separation of concerns promotes encapsulation, modularity, and code reusability.

car = Car()
car.move()

boat = Boat()
boat.move()

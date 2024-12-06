# https://programming-21.mooc.fi/part-9/3-encapsulation

# Encapsulation is the concept of bundling data (attributes) and code (methods) that operates on the data into a single unit.
# It is a fundamental principle in object-oriented programming that helps in organizing and protecting data from external interference.
# Encapsulation is achieved by using access modifiers, which control how the attributes and methods of an object can be accessed and modified.
# The main idea is to hide the internal details of an object and expose only the necessary interfaces for interacting with it.

# A common feature in object oriented programming languages is that classes can usually hide their attributes from any prospective clients.
# Hidden attributes are usually called private.
# In Python this privacy is achieved by adding two underscores __ to the beginning of the attribute name:

# NOTES:
# There are ways around the underscore __ notation for hiding attributes, which you may come across if you search for resources online.
# No Python attribute is truly private, and this is intentional on the part of the creators of Python.

# In object oriented programming, methods which are dedicated to accessing and changing attributes are usually called getters and setters.
# Not all Python programmers use the terms "getter" and "setter", but the concept of properties outlined below is very similar, which is why we will use the generally accepted object oriented programming terminology here.
# So, above we created some public methods for accessing private attributes, but there is a more straightforward, "pythonic" way of accessing attributes.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

person = Person("John", 25)

print(person.name)
print(person.__age)

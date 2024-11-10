#Great article about classes: https://realpython.com/python3-object-oriented-programming/

# Object-oriented programming is a programming paradigm that provides a means 
# of structuring programs so that properties and behaviors are bundled into individual objects.

# For example, an object could represent a person with properties like a name, age, and address
# and behaviors such as walking, talking, breathing, and running. Or it could represent an email with
# properties like a recipient list, subject, and body and behaviors like adding attachments and sending.

# Classes allow you to create user-defined data structures. 
# Classes define functions called methods, which identify the behaviors and actions that an object created from the class can perform with its data.
class Dog: 
    # .__init__() sets the initial state of the object by assigning the values of the object’s properties.
    # That is, .__init__() initializes each new instance of the class.

    # self is a reference to the current instance of the class.
    # It is used to access variables that belong to the class.

    # species is a property/attribute of the Dog class.
    species = "Canis familiaris"

    # The __init__() method is used to initialize the object.
    def __init__(self, name, age):
        # name and age are properties/attributes of the Dog class.
        self.name = name
        self.age = age

    # The __str__() method returns a string representation of the object.
    # Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores. 
    def __str__(self):
        return f"{self.name} is {self.age} years old"


    def bark(self):
        print(f"{self.name} is barking")


# Creating an instance of the Dog class.
teddy = Dog("Teddy", 3)
# Printing the string representation of the Dog class.
print(teddy)
# Calling the bark method/behavior on the teddy instance.
teddy.bark()
# Accessing the species property/attribute of the Dog class.
print(teddy.species)
print('---------')

# Creating another instance of the Dog class.
gruu = Dog("Gruu", 12)
# Printing the string representation of the Dog class.
print(gruu)



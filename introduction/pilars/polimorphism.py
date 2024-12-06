# https://www.youtube.com/watch?v=tHN8I_4FIt8
# Polymorphism is the ability of a program to detect the real
# class of an object and call its implementation even when its
# real type is unknown in the current context.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


shapes = [Circle(4), Square(5), Triangle(6, 7)]

for shape in shapes:
    # The area method is called on each shape object,
    # and the result is printed.
    # The actual method implementation is determined by
    # the class of the object at runtime, which is why this
    # is an example of polymorphism.
    print(f"{shape.area()}cm²")

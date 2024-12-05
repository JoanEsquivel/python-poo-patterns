class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Property decorator: allows us to define a method that can be accessed like an attribute (Kind of like a getter)
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    # Setter decorator: allows us to define a method that can be accessed like an attribute (Kind of like a setter)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    # Deleter decorator: allows us to define a method that can be accessed like an attribute (Kind of like a deleter)
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

emp_1 = Employee("John", "Doe")

emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

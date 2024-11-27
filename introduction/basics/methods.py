# Check more details at: https://www.youtube.com/@coreyms/videos
class Employee: 

    raise_amount = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f"{first_name}.{last_name}@company.com"

    def __str__(self):
        return f"{self.first_name} {self.last_name} has a salary of {self.salary}"

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


    # Class method
    @classmethod
    # cls will be the reference to the class
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Static method
    # Static methods are not bound to any instance or class.
    # They are just regular functions that are related to the class.
    @staticmethod
    def is_workday(day):
        # 5 is Saturday, 6 is Sunday
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


employee_1 = Employee("John", "Doe", 50000)
employee_2 = Employee("Jane", "Doe", 60000)


# Using the class method to set the raise amount
# Notice that we are not calling the method on an instance, but on the class itself.
# This is an alternative way to set the raise amount for all instances of the class.
employee_1.set_raise_amount(1.05)
print(f"Employee.raise_amount: {Employee.raise_amount}")
print(f"employee_1.raise_amount: {employee_1.raise_amount}")
print(f"employee_2.raise_amount: {employee_2.raise_amount}")

# Using the static method to check if a day is a workday
import datetime
my_date = datetime.date(2024, 11, 28)
print(Employee.is_workday(my_date))


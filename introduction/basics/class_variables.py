# Check more details at: https://www.youtube.com/@coreyms/videos
class Employee: 

    # Class variable (shared by all instances)
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


employee_1 = Employee("John", "Doe", 50000)
employee_2 = Employee("Jane", "Doe", 60000)

# Print all the attributes of the Employee class.
Employee.raise_amount = 1.05
print(f"Employee.raise_amount: {Employee.raise_amount}")
# Print all the attributes of the employee_1 instance.
# The raise_amount attribute is shared by all instances of the Employee class.
# That is why when we change the raise_amount attribute for the Employee class, it is reflected in the employee_1 and employee_2 instances.
print(f"employee_1.raise_amount: {employee_1.raise_amount}" )
print(f"employee_2.raise_amount: {employee_2.raise_amount}" )

# We can also change the raise_amount attribute for a specific instance.
employee_1.raise_amount = 1.06
print(f"employee_1.raise_amount: {employee_1.raise_amount}" )
print(f"Employee.raise_amount: {Employee.raise_amount}" )


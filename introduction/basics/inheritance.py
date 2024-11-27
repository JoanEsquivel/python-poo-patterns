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


class Developer(Employee):
    # Override the raise_amount attribute of the Employee class.
    raise_amount = 1.10

    def __init__(self, first_name, last_name, salary, programming_language):
        super().__init__(first_name, last_name, salary)
        self.programming_language = programming_language

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        # If the employees parameter is not provided, initialize an empty list.
        # why None, and not an empty list? Good practice https://www.geeksforgeeks.org/default-arguments-in-python/
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
    def print_employees(self):
        for employee in self.employees:
            print(f"--> {employee.first_name} {employee.last_name}")

# Print the full list of methods and attributes of the Developer class.
# print(help(Developer))

developer_1 = Developer("John", "Doe", 50000, "Python")
developer_2 = Developer("Jane", "Doe", 60000, "Java")
developer_3 = Developer("Jim", "Beam", 70000, "C#")

print(developer_1.email)
print(developer_1.programming_language)
print(developer_2.email)
print(developer_2.programming_language)
print(developer_3.email)
print(developer_3.programming_language)

manager_1 = Manager("Sue", "Smith", 90000, [developer_1, developer_2])
manager_1.add_employee(developer_3)
manager_1.remove_employee(developer_2)
manager_1.print_employees()

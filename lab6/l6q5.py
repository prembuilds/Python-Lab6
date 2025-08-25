# Define a class Person with attributes name and age. Derive a class Employee from Person with additional attributes employee_id and salary. Implement a method display_employee() in Employee that prints all the details. Create an instance of Employee and display the information.

class Person:
    def __init__(self, name = "NA", age = "NA"):
        self.name = name
        self.age = age
    
class Employee(Person):

    def __init__(self, name="NA", age="NA", employee_id = 00, salary = 00):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
    
    def display_employee(self):
        print(f"Employee id : {self.employee_id}")
        print(f"Employee name : {self.name}")
        print(f"Employee age : {self.age}")
        print(f"Employee salary : {self.salary}")
    
e1 = Employee(name = "Prem", salary=34000, age = 34, employee_id = 1111)
print(e1.display_employee())
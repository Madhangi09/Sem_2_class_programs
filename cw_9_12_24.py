class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"Name=",{self.name})

class Employee(Person):
    def __init__(self,age):
        self.age=age
    def display(self):
        print(f"Age=",{self.age})
        
class Manager(Person):
    def __init__(self,Id,dept):
        self.Id=Id
        self.dept=dept
    def display(self):
        print(f"Age=",{self.age},"\nDepartment=",{self.dept})

class Student(Employee,Manager):
    def __init__(



    

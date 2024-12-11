#Encapsulation

#1
class Student:
    id=23 #double underscore is private and it'll show an attribute error
    def __init__(self,name):
        self.__name=name
    def display(self):
        print("Name=",self.__name)
s=Student("Mad")
s.display()
print(s.id)

#2
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name=",self.name,"\nAge=",self.age)
name=input()
age=int(input())
s=Student(name,age)
s.display()

#3
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
name=input()
salary=int(input())
emp=Employee(name,salary)
print("Name:",emp.name)
print("Salary:",emp._Employee__salary) # double underscore means private where single refers public

#4
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def displayEmployeeInfo(self):
        print(f"Student Name:",self.name,"\nSalary:",self.salary)
class TL(Employee):
    def __init__(self,name,role,teamsize):
        super().__init__(name,salary)
        self.role=role
        self.teamsize=teamsize
    def displayTLInfo(self):
        self.displayEmployeeInfo()
        print(f"Role:",self.role,"\nTeam Size:",self.teamsize)
name=input()
salary=int(input())
role=input()
teamsize=int(input())
emp=TL(name,salary,role,teamsize)
print("Name:",emp.name)
print("Salary:",emp._Employee__salary)
print("Role:",emp.role)
print("Team size:",emp.teamsize)

        

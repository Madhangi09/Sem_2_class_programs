#1 multi-level inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayPerson(self):
        print("Name=",self.name,"\nAge=",self.age)

class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id=Id
    def displayEmployee(self):
        self.displayPerson()
        print("Id=",self.Id)

class Manager(Employee):
    def __init__(self,name,age,Id,Salary):
        super().__init__(name,age,Id)
        self.Salary=Salary
    def displayManager(self):
        self.displayEmployee()
        print("Salary=",self.Salary)
emp=Manager("Mad",17,23,90000)
emp.displayManager()


#2 hierarchical inheritance
class Director:
    
    
        
        

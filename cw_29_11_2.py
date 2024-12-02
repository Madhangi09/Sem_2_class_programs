#1
class Employee:
    def __init__(self,name,id,position):
        self.name=name
        self.id=id
        self.position=position
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nid:{self.id}\nposition:{self.position}")
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayaddressInfo(self):
        print(f"street name:{self.street}\nstate name:{self.state}\ncountry name:{self.country}")

class EmployeeDetails(Employee,Address):
    def __init__(self,name,id,position,street,state,country):
        super().__init__(name,id,position)
        Address.__init__(self,street,state,country)
    def DisplayEmp(self):
        self.displayEmployeeInfo()
        self.displayaddressInfo()

ed=EmployeeDetails("Mad",23,"Manager","Shen Nagar","TamilNadu","India")
ed.DisplayEmp()

#2
class Student:
    def __init__

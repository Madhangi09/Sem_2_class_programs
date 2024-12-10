#hybrid inheritance
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayEmployeeInfo(self):
        print("Name:",self.name,"\nAge:",self.age)
class Manager(Employee):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id=Id
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print("Id:",self.Id)
class Developer(Employee):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept=dept
    def displayDeveloperInfo(self):
        self.displayEmployeeInfo()
        print("Department:",self.dept)
class TeamLeader(Manager,Developer):
    def __init__(self,name,age,Id,dept,teamsize):
        Employee.__init__(self,name,age)
        self.Id=Id
        self.dept=dept
        self.teamsize=teamsize
    def displayTeamInfo(self):
        print("Team size:",self.teamsize)
name=input()
age=int(input())
Id=input()
dept=input()
Ts=input()
t1=TeamLeader(name,age,Id,dept,Ts)
t1.displayManagerInfo()
t1.displayDeveloperInfo()
t1.displayTeamInfo()


            

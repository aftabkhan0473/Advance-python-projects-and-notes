class Employee:  # Base class
    company = "Google"

    def funName(self):
        print("This is an employee")

class Programmer(Employee):    # here Programmer is a derived class from Employee so Employee is a base class of Programmer
    language = "Python"
    def funName(self):
        print("This is an Programmer")
    
    def funName2(self):
        print("I am also a programmer")
    
e = Employee()
p = Programmer()
print(e.company)
print(p.company)  # clearly programmer execute class attribute of Employee
e.funName()
p.funName()
p.funName2()
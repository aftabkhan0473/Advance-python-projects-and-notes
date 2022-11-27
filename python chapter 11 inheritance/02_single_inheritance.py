class Employee:   # base class
    company = "www.freelancing.com"

    def getInfo(self):
        print(f"This is an employee of {self.company} companay")

class sinlgeinheritance(Employee):  # derive class from a single base class so it is a single inheritance class
    language = "python"
    def getInfo(self):
        print(f"This man know {self.language} language")

e = Employee()
s = sinlgeinheritance()
print(e.company)
print(s.company)
print(s.language)
# print(e.language) # throws error bcz base class not execute attributes and methods(function) of derived class
s.getInfo()
e.getInfo()
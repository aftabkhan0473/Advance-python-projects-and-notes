class Person:
    Home = "Majhaulia"
    Hobby = "Coding"

    def getinfo(self): # funtion in python use self for the argument which is one here
        print(f"The Hobby of this person is {self.Hobby} and Home is {self.Home}")

class Employee:
    company = "Chola Tailor"
    Hobby = "Programming and web developing"
    salary = 3000000

    def getsalary(self):
        print(f"The salary of this Employee is {self.salary} Hobby : {self.Hobby} company : {self.company}")

class Programmer:
    company = "Microsoft"
    salary = 5000000
    peryear = "1 lakh"

    def getsalary(self):
        print(f"company :{self.company} salary : {self.salary} ")

class multipleinheritance(Employee, Person):  # 1st priority Employee and then Person orderedwise priority
    khushi = "coddddding"

class multipleinheritance2(Person, Programmer, Employee): # priority orderwise 1st priority Person then Programmer then Employee
        Wow = "that's cool yar 3 class ko execute kar sakta hai"


p = Person()
e = Employee()
pr = Programmer()
m = multipleinheritance()
m2 = multipleinheritance2()
# print(m.peryear) # throw error bcz m('multipleinheritance') object has no attribute 'peryear'
print(m.Hobby)
print(m.Home)
print(m.khushi)
print(m.salary)
print("################************###########")
print(m2.Hobby)
print(m2.Home)
print(m2.peryear)
print(m2.salary)
# print(m2.khushi) # throw error bcz it is not an attribute in m2
print(m2.Wow)
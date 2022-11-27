# Note - self ke jagah kuch bhi likhe wo execute kar lega jaise yaha ek jagah self and dusre jagah Aftab argument likhe hai and multilevel class sabko execute kar raha so Aftab = self and anything which si place in ths place of self it's just showing that the class contain one argument bsss 
class Person:   # base class
    Hobby = "coding"
    
class Employee(Person):  # single inheritance and also part of a multilevel inheritance
    company = "Chola tailor"
    Hobby = "Programming"
    salary = 200
    def getinfo(self):
        print(f"company : {self.company} and Hobby : {self.Hobby}")

class Programmer(Employee):   # multilevel inheritance
    company = "Pomegranate"
    salary = 1000
    def getsalary(Aftab): # 1st argument is only for showing a argument 
        print(f"company : {Aftab.company} and salary : {Aftab.salary}")

p = Person()
e = Employee()
pr = Programmer()
print(pr.Hobby)
print(pr.salary)
print(pr.company)
pr.getinfo() # here company is taken from class programmer and hobby is from its parent class bcz hobby attribute is not present in this class
pr.getsalary()
e.getinfo()
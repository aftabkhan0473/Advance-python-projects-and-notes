# super can be used in derived class bcz it functionate the funtion of parent class execute 1st which is given in super.()funtion()
class Person:   
    Hobby = "coding"

    def __init__(self):
        print("initializing person")

    # def getinfo(self):
    #     print(f"Hobby : {self.Hobby}")

    def gethobby(self):
        print(f" hobbbbbbbbbby : {self.Hobby}") 
    
class Employee(Person): 
    company = "Chola tailor"
    Hobby = "Programming"
    salary = 200

    def __init__(self):
        # super().__init__()
        print("initializing Employee")

    def getinfo(self):
        super().gethobby() 
        print(f"company : {self.company} and Hobby : {self.Hobby}")

class Programmer(Employee): 
    company = "Pomegranate"
    salary = 1000

    def __init__(self):
        super().__init__()
        print("initializing Programmer")

    def getinfo(Aftab): 
        print(f"company : {Aftab.company} and salary : {Aftab.salary}")

# p = Person()
e = Employee()
# pr = Programmer()
e.getinfo() # here self.hoby 1st execute parent self.info and there is class attribute in self.info has value self.Hobby value of Hobby attribute in Person is 'coding' and  Hobby attribute also present in Employee class which value is 'programming' so the value of self.Hobby is 'programming' not 'coding' because 1st priority is Employee 

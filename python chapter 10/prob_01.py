# Create a class programmer for storing information of few programers working at microsoft
class Programmer:
    company = "Microsoft"    # same for all objects in this class
    wife = "Not define"           # same for all objectis in this class
    home = "India"                     # same for all objects in this class
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print(f"company : {self.company}, programmer name  : {self.name}    , age : {self.age},  salary  : {self.salary}, wife : {self.wife}, home : {self.home}")

Aftab = Programmer("Md Aftab Ali", 19, 1400)
Tassu = Programmer("Tassu", 18, 140)
Shivam = Programmer("Shivam", 21, 87)
Harry = Programmer("Harry", 30, 89)
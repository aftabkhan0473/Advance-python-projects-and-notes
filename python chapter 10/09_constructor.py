class Employee:
    company = "google"



    def functionName(self, signature,dost, phir_hera_pheri):
        print(f"signature who work in {self.company} is {signature}, \n dost is {dost}, \n phir_hera_pheri is {phir_hera_pheri}") 
    @staticmethod
    def greet():
        print("Hello boys ! How are you , I hope you all are good as well as me , so just start our first familiar lecture of python programming")
    @staticmethod
    def time():
        print("The time is exactly same that in your watch so just see your watch to know the time")

    def __init__(self, name, salary, subunit):             # __init__function   also called as constructor method
        self.name = name  # here name is initialize
        self.salary = salary
        self.subunit = subunit

        print(f"i am constructor biru i run as soon as object is created {self.name}\n{self.salary} \n{self.subunit}")
    
    def getdetails(self):
        print(f"name of employee is {self.name}")
        print(f"salary of employee is {self.salary}")
        print(f"subunit of employee is {self.subunit}")

Aftab = Employee("Aftab", 100, "YouTube")  
# Aftab = Employee()  # this throw an error (missing 3 required positional arguments: 'name', 'salary', and 'subunit')
Aftab.__init__("Tassu", 854, "Microsoft")
Aftab.getdetails()
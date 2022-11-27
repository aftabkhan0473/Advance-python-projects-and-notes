class Employee:
    company = "Google"  # here company is a class attribute
    salary = 100   # here salary is a class attribute 

harry = Employee() # harry is an instance(object) of class Employee and also harry is an object to instantiate class Employee
rajni = Employee() # rajni is an instance(object) of class Employee and also rajni is an object to instantiate class Employee
print(rajni.company)
print(harry.company)
Employee.company = "Youtube"
print(rajni.company)
print(harry.company)
rajni.company = "Microsoft"
print(harry.company)
print(rajni.company)
Aftab = Employee()
print(Aftab.company)
print(Employee.company)
harry.salary = 300   # here salary is a instance attribute for harry
rajni.salary = 400    # here salary is a instance attribute for rajni
print(rajni.salary)
print(harry.salary)

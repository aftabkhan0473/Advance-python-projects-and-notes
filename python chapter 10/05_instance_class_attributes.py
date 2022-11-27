class Employee:
    company = "Google"
harry = Employee() # here harry is defined and it is an object because it is instantiate the class Employee
Aftab = Employee() # here Aftab is an object because it instantiate the class Employee
print(harry.company)
print(Aftab.company)
Aftab.salary = 500 # here salary is instance attribute
Tassu = Employee   # here Tassu is defined and object because it instantiate the class Employee
Tassu.car = "BMW"  # car is instacne attribute
print(Tassu.car)
print(Aftab.salary)
# print(Aftab.girlfriend) # throws an error because girlfriend is not present in object/class so it can't implement
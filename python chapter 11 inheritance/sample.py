class Employee:
    company = "YouTube"  # class attribute

a = Employee()
a.company= "Google"  # instance attribute
print(a.company)
print(Employee.company)
Employee.company = "Bharat Gas" # change value of company parmanently 
print(a.company)  # given 1st priority object(instance attribute) then class
print(Employee.company)
b = Employee()
print(b.company) # Means Employee.company change the value of company parmanently
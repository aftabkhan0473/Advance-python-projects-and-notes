class Employee:
    company = "Google"
    def getsalary(self):
        print(f"The salary who are working in {self.company} is {self.salary}")
        # here attribute salary is not present in class so it execute from object(instance) if object have not this attribute then definitely error occured AttributeError: 'Employee' object has no attribute 'salary'

Aftab = Employee() # here Aftab is an object

Aftab.salary = 34000   # here self is Aftab and the attribute is instance attribute

Aftab.getsalary()   # Employee.getsalary(Aftab)              

# both are equal u can evaluate from comparing both  Aftab.friend() here self is Aftab like a.friend(Aftab) in this Aftab is self 

# dekh rahe class can contain undefined thing here salary is undefined but it is present in class but before calling out of the class we define that salary
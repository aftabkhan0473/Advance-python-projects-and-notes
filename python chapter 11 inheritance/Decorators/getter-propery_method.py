# getter method or property method is used to 
class Employee:
    num1 = 54
    num2 = 852
    
    @property
    def summation(self):
        return self.num1 + self.num2

e = Employee()
print(e.summation) # Note here e.summation not used paranthesis bcz its a property internal function but external property if property is not used then e.summation() must be used here
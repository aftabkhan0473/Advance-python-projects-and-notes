# Create a class "Emoloyee" and add salary and increment properties to it. Write a method salaryAfterIncrement method with a @property decorator with a setter which changes the value of increment based on the salary.
class Emoloyee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.increment = value / self.salary

e = Emoloyee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 500
print(e.salary)
print(e.increment)
print(e.salaryAfterIncrement)
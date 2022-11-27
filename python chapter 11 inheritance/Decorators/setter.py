class Employee:
    salary = 54
    salarybonus = 852
    
    @property
    def totalsalary(self):
        return self.salary + self.salarybonus
    
    @totalsalary.setter
    def totalsalary(self, value): # in setter value is not a argument its a given value of totalsalary
        self.salarybonus = value - self.salary


e = Employee()
print(e.totalsalary)
e.totalsalary=100
print(e.salary)
print(e.salarybonus)
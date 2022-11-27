class Employee:
    salary = 50

    # def changesalary(self, sal):
    #     self.__class__.salary = sal  # dunder class method change the parmanent value of salary

    @classmethod   # A decorator has power to change the value of class attribute parmanently
    def changesalary2(cls, sal):
        cls.salary = sal

a = Employee()
print(a.salary)
print(Employee.salary)
a.changesalary2(400)
print(a.salary)
print(Employee.salary)
Employee.salary = 700  # can change the value of salary parmanently
print(a.salary)
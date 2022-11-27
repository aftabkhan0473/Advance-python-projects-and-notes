class programmer:
    hey_man = "Google"
    def func1(self):
        print(f"salary is {self.salary}") # here salary is not defined
a = programmer()
print(a.hey_man)
a.salary = 1500
a.func1()
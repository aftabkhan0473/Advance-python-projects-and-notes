# getsalary contain 0 argument
class Employee:
    company = "Google"
    def getsalary():
        print("salary is 340k")
Employee.getsalary()
print(Employee.company)
# a = Employee()
# a.getsalary()

# get salary contain 1 argument

class busines:
    comp_any = "Microsoft"
    def getsalary(apna_man_se_kuch_bhi_dal_do):
        print(f"Salary is 45k and self is {apna_man_se_kuch_bhi_dal_do}")

busines.getsalary("Aftab")
print(busines.comp_any)
# a = busines()
# a.getsalary()

# get salary contain 1 argument

class shop:
    name = "Chola Tailor"
    def getsalary(dalo_kuch_bhi):
        print("salary is 56k")
shop.getsalary("Rahmat Ali++")
print(shop.name)

#  self get salary contain 1 argument self
class badabusiness:
    business_company = "Netflix"
    def getsalary(self):
        print("salary is 1 dollar")
Aftab = badabusiness()
Aftab.getsalary()
print(badabusiness.business_company)

# self k jagah kuch bhi likh sakte hai beta self is just an default argument for function in class

class Amazon:
    Amazon_company = "india Amazon"
    def getsalary(Namaste_England):
        print("salary is not defined")
PriyaJyoti = Amazon()
PriyaJyoti.getsalary()
print(Amazon.Amazon_company)

# just understand what is self and why we use and argument in funtionName like self or others we want

class a:
    b = "dost"
    def friend(self):
        print(f"My friend is Tassu")
Aftab = a() # here Aftab is an object because it instantiate class a()
Aftab.friend()  # a.friend(Aftab)                  # both are equal u can evaluate from comparing both  Aftab.friend() here self is Aftab like a.friend(Aftab) in this Aftab is self 
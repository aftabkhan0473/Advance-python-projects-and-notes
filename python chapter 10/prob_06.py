class Employee:
    company = "Google"
    def functionName(Aftab):   # self can be replace by any variable you want
        print(f"company : {Aftab.company}") # so all space where self is used where use the variable which you use before in the space of self
a = Employee()
a.functionName()

class YouTube:
    company = "YouTube"
    def YouTubemember(Harry):  # self is harry 
        print(f"company : {Harry.company}")  # self is harry 
b = YouTube()
b.YouTubemember()

class A:
    def __init__(harry, name):  # here self is harry
        harry.name = name
        print(f"Name : {harry.name}")

b = A("Aftab")
# add method, sub method, etc operator overloading method also known as "Magic Method"
class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

a = A(12)
b = A(14)
c = a + b
print(c)

class B:
    def __init__(self,x):
        self.x = x # initialiazing the argument
    def __add__(y,z):
        return y.x + z.x
class C:
    def __init__(self,x):
        self.x = x # initialiazing the argument
    def __add__(self, other):
        return self.x + other.x
    

b = B(122)
c = C(234)
print(b+c) # will find add method in only class b not in c
print(c+b)  #B.__add__(b,c) or C.__add__(b,c) , Note:- print(c+b) will find +(add) operator in only class C not in b in add method is not present in class C then error appeard and print(b+c) find add method in only class b
print(3+4)

class D:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, other):
        print("Let's Add")
        return self.num + other.num

    def __mul__(self, other):
        print("Let's multiply")
        return self.num * other.num
d = D(45)
e = D(100)
f = d + e  # calling add method
g = d * e    # calling multiply method
print(f"{e.num} + {d.num} = {f}")    
print(f"{e.num} * {d.num} = {g}")   
print(d+e)
print(d*e)

class Z:
    def Print(self):
        print("I am Aftab")
        return 5
z = Z()
z.Print() # funtion ko call gya bs kya print ho gya "I am Aftab"
print(z.Print()) # gya print me usse function ko call laga jaise hi funtion ko call laga "I  am Aftab" print ho gya and then 5 store ho gya jo pehle wala print funtion print kar diya that's all.
x = print("I am here")
y = print(x)
w = print(y)
print(w)
print(print(print("Bhootni ke")))
# Write a class complex to represent complex numbers, along with overloaded operator + and * which adds and multiples them

class complex:
    def __init__(self,x,y):
        self.real = x
        self.imaginary = y
    def __add__(self, other):
        return self.real + other.real, self.imaginary + other.imaginary # tuple created

    def  __mul__(self, other):
        return self.real*other.real - self.imaginary*other.imaginary, self.real*other.imaginary + self.imaginary*other.real
c = complex(3,4)
d = complex(5,6)
e = c + d
print(f"Addition of two complex number c and d is{e}")
print(type(e))
f = c * d
print(f"Multiplication of two complex number c and d is {f}")
print(type(f))
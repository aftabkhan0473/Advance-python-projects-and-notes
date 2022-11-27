# Operatorts in python can be overloaded by using following methods
'''
+ : __add__ method
- : __sub__ method
/ : __truediv__method
// : __floordiv__method

# This method is called dunder method or magic method cool yar mast hai means we can use to add to objects even two class evern anything in python using magic method or dunder method or using operator overloading
'''
class A:
    def __init__(self, num):
        self.num = num

    def __truediv__(self, other):
        return self.num / other.num
    
    def __floordiv__(self, other):
        return self.num // other.num
a = A(100)
b = A(40)
print(a/b)  # return proper division
print(a//b)  # return quotient
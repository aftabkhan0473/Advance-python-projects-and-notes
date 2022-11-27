# Write __str__() method to print the vector as follows: 7i + 8J + 10k Assume vector of dimension 3 for this problem...

class Vector:
    def __init__(self, x , y , z):
        self.icap = x
        self.jcap = y
        self.kcap = z
    def __str__(self):
        return f'{self.icap}i + {self.jcap}j + {self.kcap}k'

v = Vector(4,5,6)
v1 = Vector(44,45,46)
print(v)
print(v1)
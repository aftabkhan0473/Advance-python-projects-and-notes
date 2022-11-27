# Create a class 'C2dvector' and use it to create one another class representing a 3-d vector.
class C2dvector:
    def __init__(self, x , y):
        self.x = x 
        self.y = y
    def __str__(self):  # str magic method use to execute given argument...
        return f"{self.x}i + {self.y}j"
class C3dvector(C2dvector):
    def __init__(self,x,y,z):
        self.z = z
        super().__init__(x,y) # here x,y initialize from class C2dvector
    def __str__(self):  # str method use to execute given argument...
        return f"{self.x}i + {self.y}j + {self.z}k" 
c1 = C2dvector(4,6)
c2 = C3dvector(7,8,9)
print(c1)
print(c2)
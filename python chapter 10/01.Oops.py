# Procedure oriented programming
a = 241
b = 34
print("The sum of a and b  is", a +b )


# Object oriented programming
class Number:
    def sum(self,a,b):
        self.a = a
        self.b = b
        return self.a + self.b  # here a and b are not in class attribute so it must be defined in object(instance attribute)

num = Number() # here num is an object because it instantiate the class Number
# num.a = 241   # here a instance attribute created
# num.b = 34          # here b instance attribute created
s = num.sum(241,34)
print(s)
# print(sum(5))
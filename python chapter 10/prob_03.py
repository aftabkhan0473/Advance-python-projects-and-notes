# Create a class with a class attribute a ; create an object from it and set a directly using object a = 0 . Does this change the class attribute
class a:
    a = 1 # class attribute

c = a()
# a.a = 0 # this will change the value of class attribute not instance attribute
c.a=0 # instance attribute
print(c.a)  # instance attribute doesn't change the value of class attribute
print(a.a)

class sample:
    a = "harry"
b = sample()
b.a = "vikky"
# sample.a = "vikky" # this class.classattribute can change the value of class attribute not instance attribute
print(sample.a)
print(b.a)   # so the answer is instance attribute doesn't change the value of class attribute and it is just create an instance attribute of a class attribute
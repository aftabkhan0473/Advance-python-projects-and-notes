# Add a static method in problem 2 to greet the user with hello.
# Write a class 'calculator' capable to finding square, cube and square root of a number
class Calculator:
    def __init__(self, num):
        self.num = num  # here define and store num for next program where i used to self.num()
    
    def square(self):
        print(f"The square of {self.num} is {self.num**2}")
    
    def cube(self):
        print(f"The cube of {self.num} is {self.num**3}")
    
    def squareRoot(self):
        print(f"The squareRoot of {self.num} is {self.num**0.5}")
    
    @staticmethod
    def greet():
        print("*******Hello user! Grand Welcome in our most powerful calculator*********")

b = int(input("Enter the number  :"))
a = Calculator(b)
a.greet()
a.square()
a.cube()
a.squareRoot()
c = Calculator(81)
c.greet()
c.square()
c.squareRoot()
c.cube()
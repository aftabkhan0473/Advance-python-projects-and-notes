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

b = int(input("Enter The number : "))
a = Calculator(b)
a.square()
a.cube()
a.squareRoot()
c = Calculator(81)
c.square()
c.squareRoot()
c.cube()
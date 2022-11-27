class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, other):
        return self.num + other.num
n = Number(9)
print(n) # print address of n 

class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, other):
        return self.num + other.num

    def __str__(self): # str method which is used to  print the self.num given argument
        return f"Decimal Number : {self.num}"
    
    def __len__(self):  # len method
        return 1

n = Number(9)
print(n) # execute in str method and 
print(len(n))
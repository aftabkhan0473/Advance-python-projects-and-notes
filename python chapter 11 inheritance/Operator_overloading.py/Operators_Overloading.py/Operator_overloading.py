# Add basically is a method which operates on + if two integers 1 and 3 combined with this then int.__add__(2,3) operats when two string "Hello" and "World" combined with this then concenating applied by + , str.__add__("Hello", "World") when two list combined with this then mergge applied by + , list.__add__([1,2], [3,4]) so, this + operator which adjust itself by the datatypes this feature in python called operator overloading
a = '5'
b = '6'
print(a + b )
c = "I am here"
d = "Where are you? "          # that's great yarr maza aa gya but what is behind this Why + operator add two numbers what is behind the code
print(d + c)
e = [1,2,3]
f = [4,5,6]
print(e + f)

class Book:
    def __init__(self, price):
        self.price = price  # initializing argument

    def __add__(self, other):    #  add not a constructor it is just a method which operats itself without calling just and yaa it self called itself  on + , having class Book
        return self.price + other.price
a = Book(10)
print(a.price)  # self.price of a
b = Book(20)
print(b.price) # self.price of b

c = a + b # + operator is not predefined for two objects so i defined add method for two object above + means add method ko khojega us class me here add method has two argument self(Her self is not pass argument, its real argument)and other here self = a and other = b , and funtion return self.price + other.price means a.price + b.price ....Yaa
print(c)

print(2+3) 
print(int.__add__(2,3))  
print(int.__sub__(2,3))
print(int.__mul__(2,3))
print(list.__add__([1,2], [3,4]))  #Yaa maine kiya
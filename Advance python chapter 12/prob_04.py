# Write a program to display a/b where a and b are integers if b=0, display infinite by handling the ZerodivisionError.
a = int(input("Enter  number 1: "))
b = int(input("Enter  number 2: "))
try:
    c = a/b
    print(f"{a}/{b} is {c}")
except ZeroDivisionError:
    print(f"{a}/{b} is Infinite")
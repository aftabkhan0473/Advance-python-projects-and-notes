# Using for loop
n = int(input("Enter the number :\n"))
product = 1
for i in range(n):
    product = product * (i+1)  #using for loop
print(product)

# using iteration statements here using for loop in function
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product
print(factorial_iter(6))

# using iterative statements and input function
m = int(input("Enter the number :\n"))
def factorial_iter(m):
    product = 1
    for i in range(m):
        product = product * (i + 1)
    return product  # return is of def not for so when you write return concentrate it is work on def not with other function

a = (f"The factorial of {m} is {factorial_iter(m)}")
print(a)

# Finally Using Recursion 

def factorial_recursive(o):
    if o == 0 or o ==1:
        return 1
    return o * factorial_recursive(o - 1)

d = factorial_recursive(2)
print(d)
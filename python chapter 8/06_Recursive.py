
def factorial_recursive(o):
    if o == 0 or o ==1:
        return 1
    return o * factorial_recursive(o - 1)

d = factorial_recursive(3)
print(d)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

b = factorial(4)
print(b)
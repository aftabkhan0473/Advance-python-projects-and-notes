# write a recursive funtion to calculate the sum of first n natural number

def sum_a_natural_number(a):
        # sum_a_natural_number(a-1) = 1 # we can't assign function call with variable
    if a == 1:
        return 1
    return a + sum_a_natural_number(a-1)

b = sum_a_natural_number(10)
print(b)
c = int(input("Enter the number \n"))
print(f"The sum of {c} natural number is {sum_a_natural_number(c)}")

def sum1(d):
    if d == 1:
        return 1
    return d + sum1(d-1)
e = sum1(10)
print(e)
def Multiplication_table(n):
    for i in range(1,11):
        a = n*i
        print(f"{n} X {i} = {a}")   # return means end 
Multiplication_table(5)

def table(num1):
    print("The multiplication table of ", num1)
    for i in range(1,11):
        print(num1, "X", i, "=", num1*i)

table(6)
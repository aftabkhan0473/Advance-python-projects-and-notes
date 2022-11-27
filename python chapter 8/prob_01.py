def maximum_among(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3
       
a = maximum_among(1,2,3)
print(f"The maximum is {a}")
print("The maximum value is ", a)
# print("The maximum value is " + a)           #     throws errof bcs + operand can             only         concatenate str (not "int") to str
print("The maximum value is " + str(a))
b = maximum_among(11,22,33)
print(f"The maximum is {b}")
c = maximum_among(99,33,34)
print(f"The maximum is {c}")

# second method 

def maximum(number1, number2, number3):
    if number1>number2 and number1>number3:
        return number1
    elif number2>number1 and number2>number3:
        return number2
    else:
        return number3

e = maximum(99,3,33)
print(f"The maximum value is {e}")
f = maximum(0,344334,2343)
print(f"The maximum value is {f}")
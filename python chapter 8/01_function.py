marks1 = [12,34,34,534,534]
marks2 = [234,43,23,12,34]

print("The sum of marks 1 is ", marks1[0] + marks1[1] + marks1[2] + marks1[3] + marks1[4])
print(" The sum of marks 2 is ", marks2[0] + marks2[1] + marks2[2] + marks2[3] + marks2[4])
print("The sum of marks1 using sum function is ", sum(marks1))
print("The sum of marks2 using sum function is ", sum(marks2))

def Addition(marks):
    print("Addition", marks[0] + marks[1] + marks[2] + marks[3] + marks[4])

Addition(marks1)
Addition(marks2)

def a(b):
    c = print("return", b[0] + b[1] + b[2] + b[3] + b[4])
    return c
a(marks2)
a(marks1)
d1 = a(marks2)
d2 = a(marks1)
print("Done")
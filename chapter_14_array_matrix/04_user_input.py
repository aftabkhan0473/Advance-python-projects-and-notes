# Making an array which elements are provided by the user
from array import *
arr = array('i',[])
a = int(input("Enter the length of array: "))
for i in range(a):
    x = int(input(f"Enter element {i+1}: "))
    arr.append(x)
print(f"array : {arr}")

# finding index of some specific element
val = int(input("Enter the element which you want to find index: "))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1

#finding index shortcut using index funtion in array
print(arr.index(val))
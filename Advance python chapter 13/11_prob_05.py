# Writa a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
l = [1,2,3,4,343,234]
# def maximum(a,b):
#     return max(a,b)
maximum = lambda a,b:max(a,b)
a = reduce(maximum,l)
print(a)
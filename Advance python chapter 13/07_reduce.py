# reduce ko import karna padta hai
from functools import reduce
def sum(a,b):
    return a + b
l = [1,2,3,4,5,6,7,8]
print(reduce(sum,l)) # first write function and then list
# reduce applies a rolling computation to sequential pair of elements
# reduce do sequential computation of pair of elements
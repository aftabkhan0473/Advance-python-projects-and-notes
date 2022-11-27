import numpy as np

# shallow copy
arr1 = np.array([1,2,3,4,5])
arr2 = arr1
print(id(arr1))
print(id(arr2)) # storing in same location
arr1[0] = 100
print(arr1)
print(arr2)


arr3 = np.array([1,2,3,4])
arr4 = arr3.view()
arr3[0] = 100
print(arr3)
print(arr4) # update kiye arr3 ko but arr4 bhi update ho gya because arr4 is shallow copy of arr3
print(id(arr4))
print(id(arr3)) # storing in other location

# deep copy :- location different and don't change its value when its copy value change
arr5 = np.array([5,2,23])
arr6 = arr5.copy()
arr5[0] = 100
print(id(arr5))
print(id(arr6))
print(arr5)
print(arr6) # do not change it's 0 index element because it is deep copy of arr5
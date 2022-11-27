import numpy as np
from numpy.core.fromnumeric import sort
arr1 = np.array([1,2,3,4])
arr1 = arr1 + 5 # wow it's so simpole to adding each elements by 5
print(arr1)
arr1 -= 5
arr2 = np.array([5,6,7,8])
arr3 = arr1 + arr2
arr4 = arr1 - arr2
arr5 = arr1 * arr2
print(arr3)
print(arr4)
print(arr5)
arr1[0] = 100  # updating or change the value of element present in array
print("************%Yaa This update the value of o index element ***********&88***********")
print(arr1)

# inbuild funtion in array
print("*************************************  Done  *********************************")
arr = np.array([1,2,3,4,5])
print(sum(arr))
print(max(arr))
print(min(arr))
print(np.log(arr)) # have base 10 of log
print(np.square(arr))
print(np.sqrt(arr))
print(np.sin(arr))
print(np.sin(90))
print(np.cos(arr))
print(np.tan(arr))
print(sort(np.array([5,2,5,1,5,2,1,0])))

# concatenate two array
arr8 = np.array([1,2,3,4])
arr9 = np.array([5,6,7,8,9])
print(np.concatenate([arr8,arr9])) # that's osm bro i like it
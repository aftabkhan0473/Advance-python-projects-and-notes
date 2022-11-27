import numpy as np
arr1 = np.array([[1,2,3],
                 [3,4,3],
])
print(arr1)
print(arr1.dtype)
print(arr1.ndim) # giving dimension of array
print(arr1.shape) # gives tuple of rows and coloumn
print(arr1.size) # size function gives no. of total elements or size of entire matrix

arr2 = arr1.flatten() # flat the matrix in one dimension means matrix m jitna bhi array hoga sabko mila ek bana dega
print(arr2)
# Note:- Matrix ka elements only space ke through alag alag hota hai 

# creating 2d Matrix from 1D
arr2 = np.array([1,2,3,3,4,3])
arr3 = arr2.reshape(2,3) # 2 row and 3 coloumn
arr4 = arr2.reshape(3,2)
print(arr3)
print(arr4)
print("**********Done******\n")

# creatin 3D matrix from 1D
arr5 = np.array([1,2,3,3,4,3,5,6,8,9,0,23])
arr6 = arr5.reshape(2,3,2) # give 3D Matrix having 2 , two dimension array and each of array contain 3 elements

arr7 = arr5.reshape(2,2,3)# 1st argument: No. of 2d array, 2nd: No. of rows in 2d array, 3rd: no of elements in each row

arr8 = arr5.reshape(3,2,2) # 1st argument: No. of 2d array, 2nd: No. of rows in 2d array, 3rd: no of elements in each row
print(arr6)
print(arr6.ndim)
print("\n")
print(arr7)
print(arr7.ndim)
print('\n')
print(arr8)
print(arr8.ndim)
# Matrix property - har ek row me same element hoga and har ek coloumn me same element hoga
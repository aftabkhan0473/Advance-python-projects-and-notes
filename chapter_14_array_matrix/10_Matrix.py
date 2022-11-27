import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])
m = np.matrix(arr)
print(arr)
print(m)

# we can directly evalute matrix by importing numpy and funtion np.matrix
x = np.matrix('1 2 3 ; 4 5 6') # 2 row and 3 coloumn
print(x)

y = np.matrix('1 2 ; 3 4 ; 5 6 ; 7 8')
print(y)

z = np.matrix('1 ; 2 ; 3 ; 4 ; 5')
print(z)

x2 = np.matrix('1 2 3 4 5 ; 6 7 8 9 10') # that's so simple thankyou numpy
print(x2)
print("*************************Done***********************")

# Operation on Matrix
m = np.matrix('1 2 3 3 2 ; 4 5 6 4 3 ; 7 8 9 3 3 ; 10 11 12 3 5 ; 13 14 15 3 6')
print(m)
print(np.diagonal(m))
print(m.min())
print(m.max())
print(m.sum())

# Adding two matrix
m1 = np.matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2 = np.matrix('4 2 3 ; 3 9 8 ; 3 5 1')
m3 = m1 + m2
print(m3)

# Multiplication of two matrix condition = no. of rows == no. of coloumns and adds multiply of each item of row with correspoinding element of coloumnd of 2nd matrix
m4 = m1 * m2
print(m4)  # it's so simple yaa that's cool
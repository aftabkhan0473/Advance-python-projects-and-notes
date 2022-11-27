# Ways of creating array in numpy
# 1.array()
from array import array
import numpy as np
a = np.array([2,3,4,1],float)
print(a)
print(a.dtype)

# 2.linspace()
import numpy as np
arr = np.linspace(0,15,16) # 0 : start, 15 : stop(included), 16 : part(default=50)
print(arr)
print(type(arr))

b = np.linspace(0,15) # by default part is 50
print(b)

#3. arange()
import numpy as np
c = np.arange(1,15,2) # 1: start, 15: stop, 2: step(like step in range function)
print(c)
print(type(c))

# 4.logspace()
import numpy as np
d = np.logspace(1,40,5) # 1: start, 5: stop, 4: part, 1st element 10**1 and ast element 10**40
print(d)
print(d[0]) # 10**1
print(d[1]) # 10**2
print(d[2]) # 10**3
print(d[3]) # 10**4
print(d[-1]) # 10**5
# we can also print elements like this
print('%.2f' %d[0]) # for changing e in normal number
print("%.2f" %d[1])
print("%.2f" %d[2]) # for changing e in number
print("%.2f" %d[3])
print("%.2f" %d[-1])

# 5. zeros()
import numpy as np
e = np.zeros(5) #gives all elements 0 as float 5 times
print(e)
g = np.zeros(5,int)
print(g)

#6.ones()
import numpy as np
f = np.ones(5) #gives all elemenst 1 as float 5 times
print(f)
h = np.ones(5,int)
print(h)
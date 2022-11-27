from array import *
a = array('i',[1,2,3,4,5])

#methods of array
print(a.buffer_info()) # gives address of array and legth of it

print(a.typecode)

a.reverse()
print(a)

a.append(6)
print(a)
for i in range(4):
    a.append(i+7)
print(a)

a.remove(6)
print(a)
for i in range(4):
    a.remove(i+7)
print(a)
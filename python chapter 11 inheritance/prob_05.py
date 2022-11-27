# Write a class vector representing a vector of n dimension. Overload the + and * operator which calculates the sum and the dot product of them

class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 1
        for element in self.vec:
            str1 += f" {element}a{index} +"
            index += 1
        return str1[:-1]
    def __add__(self,other):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + other.vec[i])
        return vector(newlist)  # Wow that's cool here newlist is executed in vector , so str applied in newlist and final result print of the form {element}a{index} + form
    def __mul__(self, other):
        multiple = 0
        for i in range(len(self.vec)):
            multiple += self.vec[i] * other.vec[i]
        return f" {multiple}"

v1 = vector([1,4])
v2 = vector([1,6])
print(v1 + v2) # printing summation of vector1 and vector 2
print(v1*v2) #printing dot product of v1 and v2 vector
# a = [1,3,4,5]
# list1 = []
# index = 0
# for i in range(len(a)):
#     list1 = a[index]
#     index += 1
#     print(list1)
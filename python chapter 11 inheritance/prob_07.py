# Overwrite the __len__() method on vector of problem 5 to display the dimesion of the vector.
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
        return vector(newlist)  
    def __mul__(self, other):
        multiple = 0
        for i in range(len(self.vec)):
            multiple += self.vec[i] * other.vec[i]
        return f" {multiple}"
    def __len__(self):
        return len(self.vec)

v1 = vector([1,4,5,10,234,34,34,343,342323,3434])
v2 = vector([1,6,7,23,435,34])
# print(v1 + v2)
# print(v1*v2)
print(len(v1))
print(len(v2))
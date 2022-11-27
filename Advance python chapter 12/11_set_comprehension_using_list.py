a = [1,2,34,4,5,5,6,6,7,1,2,3,34,343]
# b = set()
# for i in a:
#     b.add(i)
# print(b)

# Using set comprehension
b = set(i for i in a)
print(b)
# # Making list like dict
# a = [1,2,3,4]
# b = ["Aftab", "Tassu", "Narrator", "Laxmi"]
# c = []
# for i in b:
#     for j in a:
#         c.append((i,j)) # Note:- append takes only one argument and see here carefully here also one argument given
# print(c)

a = [1,2,3,4]
b = ["Aftab", "Tassu", "Narrator", "Laxmi"]
# c = {}
# for i,j in zip(a,b):
#     c[i] = j
# print(c)
c = {i:j for i,j in zip(a,b)}
print(c)
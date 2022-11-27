a = [1,3,4,53,9783,23432,13432,3,1,3,4]
# b = []
# for i in a:
#     if i<3444:
#         b.append(i)
# print(b)

# Using list comprehension
b = [i for i in a if i <3444]      # that's osm yar! I literally loved it
print(b)

# set comprehension
c = [1,3,4,53,9783,23432,13432,3,1,3,4]
d = {i for i in c if i < 3444}
print(d)

# Tuple comprehension  # Tuple can't comprehensiate bcz it can't be updated , appended when it is created
# e = [1,3,4,53,9783,23432,13432,3,1,3,4]
# f = (i for i in e if i<3444)
# print(f)
# I want a (letter, num) pair for each letter in 'abcd' and each num in '0123'

my_list = []
for i in 'abcd':
    for a in range(4):
        my_list.append((i,a))
print(my_list)

m = [(i,a) for i in 'abcd' for a in range(4) ]
print(m)
for i in 'Juhi Chawla':
    print(i)

a = ["kalua", "bhatija", "Baklol", "was my fav"]
b = ["aftab", "kaif", "Carryminati", "doctor strange"]
c = {}
for a,b in zip(a,b):
    c[b] = a
print(c)

a = ["kalua", "bhatija", "Baklol", "movie"]
b = ["aftab", "kaif", "Carryminati", "doctor strange"]
d = {z:y for z,y in zip(a,b)}
e = {z:y for z,y in zip(b,a) if z != 'aftab'} # printing a dictionary excluding "aftab" as a key
print(d)
print(e)
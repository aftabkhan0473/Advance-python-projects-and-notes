def square(num):
    return num*num
l = [1,2,3,4]

# Method 1 to find square of all items
# l2 = []
# for item in l:
#     l2.append(square(item))
# print(l2)

# Method 2 to find square of all items using map method
print(list(map(square,l)))  # Wow like list comprehension too shortcut maza aa gya
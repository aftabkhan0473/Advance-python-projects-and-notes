   list1 = [1,3,4,"harry", 3.3, "23", False, None, True]
# index = 0
# for i in list1:
#     print(i, ":", index)
#     index += 1

# Basically enumerate is used for denoting index same but shortcut as above
for a, b in enumerate(list1): # first is always index and the second one is item in list1 so a is index and b is items in list1
    print(b,":",a)
    # print(a,b)
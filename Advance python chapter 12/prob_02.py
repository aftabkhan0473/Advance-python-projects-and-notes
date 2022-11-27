# Write a program to print third, fifth and seventh element from a list using enumerate function.
a = [1,2,3,4,45,6,7,8,9,10,11,23]
for index,item in enumerate(a): # enumerate funtion used for indexing and yaa for check specific elements of specific index
    if index == 2 or index == 4 or index == 6:
        print(f"index {index} element: {item}")
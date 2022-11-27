# Store the multiplication tables generated in problem 3 in a file named Tables.txt.
a = int(input("Enter the number which you want to table: "))
b = [a*i for i in range(1,11)]
print(b) # str(b) and look like same means list and str of list look like same
with open("Tables.txt", 'a') as f:
    f.write(str(b))
    f.write('\n')
# c = [1,2,3,4,5,6,7,8,9,10]
# print(c)
# print(str(c))
#  # clear str of list(a) and only list(a) both looks like same
# filter used to filter the elements of an iterable object without executing its elements
# filter syntax -- print(list(filter(funtion,list)))
def numbers_greater_than_5(num):
    if num>5:
        return True
    else:
        return False
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,124,3443,1234]
g10 = lambda num:num>100  # lambda funtion
print(list(filter(numbers_greater_than_5,l))) # first function then list
print(list(filter(g10,l))) # filter method which return the elements which is True or fullfill condition of funtion
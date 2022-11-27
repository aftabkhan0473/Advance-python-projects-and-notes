# Write a program to filter a list of numbers which are divisible by 5
l = [1,2,3,4,5,6,7,8,12,33,45,45,46,454,24]
divisible_by_5 = lambda a:a%5==0
# def divisible_by_5(num):
#     if num%5 == 0:
#         return True
#     else:
#         return False
print(list(filter(divisible_by_5,l)))
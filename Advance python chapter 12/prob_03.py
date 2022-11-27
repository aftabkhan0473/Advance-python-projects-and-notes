# Write a list comprehension to print a list which contains the multiplication table of a user entered number.
a = int(input("Enter the number which you want to table: "))
b = [a*i for i in range(1,11)]
print(b)
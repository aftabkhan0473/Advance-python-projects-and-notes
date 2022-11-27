Number = int(input("Enter the number       :"))
b = Number # her we store Number in b so that when we change Number then b is stored in the previous form of Number and we can use this for the value given by  user input
reverse_Number = 0
while Number>0:
    Remainder = Number%10
    reverse_Number = (reverse_Number*10)+ Remainder
    Number = Number//10

print(f"The reverse number is : {reverse_Number}")

if b == reverse_Number:
    print("Yes the number is Pelindrome")
else:
    print("No, The number is not Pelindrome")
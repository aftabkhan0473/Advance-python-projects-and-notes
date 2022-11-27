class star:
    a = int(input("Enter the size longest length of star :"))
    for i in range(1,a+1):
        print(" "*(a-i),end=" ")
        print("* "*(i),end=" ")
        print(" "*(a-i))

# take input 65
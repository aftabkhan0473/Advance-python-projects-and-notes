def star_pattern(n):
    for i in range(n):
        a = print("* " * (n-i))
    return a
a = star_pattern(3)    

def star_gojob_pattern(m):
    for i in range(m):
        print(" " * i, end="")
        print("* " * (m-i), end="")
        print(" " * (i))

p = int(input("Enter the number :\n"))
print(f"The gojob star pattern is {star_gojob_pattern(p)}")

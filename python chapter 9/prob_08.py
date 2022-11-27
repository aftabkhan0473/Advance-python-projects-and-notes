# Write a program to make a copy of a text file "this.txt".

with open("this.txt") as f:
    data = f.read()
with open("copy.txt", 'w') as f:
    f.write(data)
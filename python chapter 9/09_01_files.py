# use open and read function to open and read the file
# f = open("sample.txt", 'r') 
f = open("sample.txt") # by default the mode is r
data = f.read()
print(data)
Aftab = f.read(10) # prints 10 characters of file sample.txt
# note one time only one read function work properly
print(Aftab)
f.close()
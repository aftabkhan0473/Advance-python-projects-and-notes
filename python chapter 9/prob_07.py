# Write a program to find out the line number where python is present from problem no 06

# 1. Using while loop 

i = 1
data =True     # if we have a condition to define a variable which is already defined in the loop but for executing loop variable must define before the loop so we can use True bool or " " it help to just define variable 
with open("log.txt") as f:
    while data:
        data = f.readline()
        if "python" in data.lower():
            print("Line Number",i,":",data)
        i += 1

# Using for loop

file = open("log.txt", 'r')
count = 1
for i in file.readlines():
    if "python" in i.lower():
        print("Line Number",count,":",i)
    count += 1

# a = 5
# c = 10
# print("aise hi","Mera Nam Aftab hai",a , ":", c)



    
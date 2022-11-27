# Write a program to find out whether a file is identical and matches the content of another file.
with open('this.txt') as f:
    data1 = f.read()
with open('sample.txt') as d:
    data2 = d.read()
if data1 == data2:
    print("Yes, the content in both file this.txt and sample.txt are mathces and identical")
else:
    print("NO, The content of this.txt and sample.txt are not identical")
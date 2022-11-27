# Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not present, a message without exiting the program must be printed prompting the same.
def readfile(filename):
    try:
        with open(filename, 'r') as  f:
            print(f.read())
    except:
        print(f"The file {filename} is not found")
readfile("1.txt")
readfile("3.txt")
readfile("2.txt")
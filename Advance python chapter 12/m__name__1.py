def greet(name):
    print(f"Good morning, {name}")
print(__name__) # if this is executed from this file then value is '__main__' otherwise means it executed from other file by importing this file then value is the file name i.e 'm__name__1'

if __name__ == "__main__": # by default when a code is run without using any other imported program or external program then the value of __name__ is '__main__'
    n = input("Enter your name: ")
    greet(n)
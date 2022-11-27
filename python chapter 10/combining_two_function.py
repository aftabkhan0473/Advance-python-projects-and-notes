# wow that's cool yaa
def again(funtion, n):
    return funtion(n)

def square(n):
    print(n**2)

again(square, 10)

# again
def add_1(a):
    return a + 1
    
def add_2(b):
    print(b + 2)

add_2(add_1(5))
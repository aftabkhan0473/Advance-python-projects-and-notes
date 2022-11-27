# def func(num):
#     return num + 5
# x = func(5333)
# print(x)

# method 2 using lambda funtion

func = lambda a: a + 5  # lambda funtion is nothing but a shortcut method to define funtion but it can't be denote all funtion it can denot some easy funtion
x = 3
print(func(x))

square = lambda x: x*x
sum = lambda a,b,c: a+b+c
print(square(x))
print(sum(x,1,2))
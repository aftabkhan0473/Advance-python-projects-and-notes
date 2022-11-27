def fahrenheit_of_celsius(n):
    return (n*9/5) + 32

a = int(input('The celsius which you want to convert in fahrenheit :\n'))
print(f"Fahrenheit of {a} degree celsius is {fahrenheit_of_celsius(a)} degree fahrenheit")
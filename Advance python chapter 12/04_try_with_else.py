try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
except Exception as e:
    print(e)
else:  # else executed when try run successfully without getting in except
    print("We were successful!")
print(__name__)
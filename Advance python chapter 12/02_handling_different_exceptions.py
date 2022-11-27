try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(f"1/{a} = {c}")
except ValueError:
    print(f"Please enter a valid value")
except ZeroDivisionError:
    print(f"Make sure you are not dividing by 0")
except: # taking another error excluding valueError and ZeroDivisionError
    print("Other error except valueError and ZeroDivisionError occurred")
print("Thanks for using this code...")
print(__name__)
try:
    a = int(input("Enter a number: "))
    c = 1/a
except:
    print("Error occured!")
    exit()
finally:
    print("this is printed regardless of error or quitting of except funtion")
print(__name__)
print("Thanks for using the program!") # not run bcz except quitting the program when error occured otherwise when try was successful then definitely run
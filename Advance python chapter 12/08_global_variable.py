a = "harry" # Gloabla variable
def func1():
    global a # when function called then it has power to update the value of global variable
    a = "Aftab" # Local variable
    print(f"statement 1 : {a}")
print(f"statement 2 : {a}") # funtion not called so it not evaluated and doesn't change the value of a by global variable
func1() # function call
print(f"statement 3 : {a}") # execute global variable
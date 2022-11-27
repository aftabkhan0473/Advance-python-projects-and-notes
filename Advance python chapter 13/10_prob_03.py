# A list contains the multiplication table of 7. Write a program to convert it to a vertical string of same numbers .
l = [str(7*i) for i in range(1,11)]
print(l) # gaur se dekho here each element is string so join work properly
print("\n".join(l)) # each element ko string me tabdeel karo then join mast tarah se apply hoga
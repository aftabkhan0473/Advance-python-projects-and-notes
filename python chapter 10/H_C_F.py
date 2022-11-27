# write a program a hcf of two numbers
a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
if a==b:
    print(f"H.C.F {a} and {b} is {a}")
elif a>b:
    i = b
    while i>=1:
        if a%i == 0 and b%i == 0:
            print(f"H.C.F of {a} and {b} is {i}")
            break   # if ka condition fulfill karega tabhi to break execute hoga and jaise hi break execute hoga loop break ho jayega and exactly i need this nahi to 1 always sabhi me H.C.F show karega H.C.F to ek hi number n koi hoga and jaise hi wo aaya loop break
        i = i - 1
elif a<b:
    i = a
    while i>=1:
        if a%i == 0 and b%i == 0:
            print(f"H.C.F of {a} and {b} is {i}")
            break  # break is very useful rare for me
        i = i -1
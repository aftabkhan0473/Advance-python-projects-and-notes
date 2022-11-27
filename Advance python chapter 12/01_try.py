while(True):
    print("Press 'q' to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        print("Trying.....")
        a = int(a)
        if (a>7):
            print("Yes, You entered a number greter than 7")
        else:
            print("No, you entered a number less than 7")
    except Exception as e:
        print(f"Error occured! : {e}")
    print("I am also in while loop.")
print("Thanks! for playing this game...")
print(__name__)
# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.
f = open("poems.txt")
t = f.read()
if "twinkle" in t.lower():
    print("Yes, twinkle is present in poems.txt")
else:
    print("No, twinkle is not present  in poems.txt")
f.close()
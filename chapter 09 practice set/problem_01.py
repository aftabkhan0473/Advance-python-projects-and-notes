# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'
with open("file.txt") as f: # One thing i understand that we cannot execute file from another folder
# we can execute file only in theis folder we can create or update
    text = f.read()
if "twinkle" in text:
    print("Yes, twinkle is present in this text")
else:
    print("No, twinkle is not present in thsi text")


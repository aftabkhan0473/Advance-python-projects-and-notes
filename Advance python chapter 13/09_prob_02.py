# Write a program to input name, marks and phone number of a student and format it using the format function like below "The name of the student is Harry his marks are 72 and phone number is 99999888"
name = input("Enter your name: ")
marks = input("Enter your marks: ")
phone = input("Enter your phone number: ")
template = "The name of student is {} and his marks is {} and his phone number is {}"
print(template.format(name,marks,phone))
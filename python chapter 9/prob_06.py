# write a program to mine a log file and find out whether it contains 'python'.
with open("log.txt") as f:
    data = f.read()
if 'python' in data.lower():
    print("Yes, log file contain python")
else:
    print("NO, log file is not contain python")
# Write a python program to rename a file to "rename_by_python.txt".
with open("kholo.txt") as f:
    data = f.read()
with open("renamed_by_python.txt", 'w') as d:
    d.write(data)
import os
os.remove("kholo.txt")
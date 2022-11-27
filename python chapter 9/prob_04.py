with open("sample.txt", 'r') as f:
    data = f.read()
data = data.replace('donkey', '#$%&^#@#') # here data is a string which have a function replace to replace old word into new word
with open("sample.txt", 'w') as d:
    d.write(data)
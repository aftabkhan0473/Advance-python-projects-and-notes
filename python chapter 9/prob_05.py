a = ["donkey", "khachchar", "gadha", "kalua", "bewakoof", "fuckingmote","mote"]
with open("sample.txt") as f:
    data = f.read()
for word in a:
    data = data.replace(word, '@#$%^&*#')
    with open("sample.txt", 'w') as f:
        c = f.write(data)
for b in a:
    print(b)
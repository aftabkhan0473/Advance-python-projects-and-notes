name = "Harry"
channel = "CodeWithHarry"

# Using f string
a = f"His name is {name} and his channel is {channel}"

# Using format method -- like f string
b = "His name is {} and his channel is {}".format(name,channel)
print(a)
print(b)

# other example of format method

Bro = "harry"
Work = "As a programmer"
c = "my bro is {} and he working {}".format(Bro,Work)
d = "my bro is {} and he working {}".format(Work,Bro)
e = "my bro is {1} and he working {0}".format(Bro,Work)
print(e)
print(d)
print(c)

f = "The {} is {}".format("boy", "Harry") # Using format method
g = "The {1} is {0}".format("boy", "Harry")
print(f)
print(g)
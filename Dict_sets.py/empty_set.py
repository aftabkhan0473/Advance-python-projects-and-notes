# Important: This syntax {} will create an empty dictionary not an empty set
a = {}
print(type(a))
b = set() # this is exactly empty set in python wow that's osm
print(type(b))
print(b)

# Adding values in empty sets
b = set()
b.add(1)
b.add(2)
b.add(3)
b.add(4)
b.add(4)
b.add(4) # Adding a value repeatedly doesn't change a set
b.add(4)
print(b)
c = {1,2,3,4,5}
c.add(12)
print(c)
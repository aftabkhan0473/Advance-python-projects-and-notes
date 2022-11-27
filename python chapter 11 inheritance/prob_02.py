# Create a class pets from a class Animals and further Create class Dog from pets. Add a method bark to class Dog.
class Animals:
    pass

class pets(Animals):
    pass

class Dog(pets):
    @staticmethod
    def bark():
        print("bhau bhau!")
d = Dog()
d.bark()
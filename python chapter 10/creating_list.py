# l=[]
# n=int(input("enter the size of list\n"))
# print(type(l))
# for i in range(n):
#   a=int(input(f"enter the element {i+1}\n"))
#   l.append(a)

# #display the list
# print(l)
# print(type(l))
class list:
    def __init__(self, num, seats):
        self.seats = seats
        self.num = num
        l = []
        for i in range(self.seats + 1):
            l.append(i)
        print(l)
        print(type(l))
a = list(89, 35)
d = [1,2,3,4,5]
print(d[-1])

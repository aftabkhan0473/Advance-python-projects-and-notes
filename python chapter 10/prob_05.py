# Write a class 'Train' which has methods to book a ticket get status(no.of seats) and get fare information(price) of trains running under indian railway.
a = '''
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
'''
               # isko sahi karna hai yaar !
class Train:
    name = "Intercity"
    def __init__(self, fair, seats):
        self.fair = fair
        self.seats = seats

    def CancelTicket(self, num):
        self.num = num
        # l = []
        # for i in range(1,self.seats + 1):
        #     if i == num:
        #         continue
        #     l.append(i)
        # e = l
        self.seats = self.seats + 1


    def bookedseats(self):
        if(self.seats>0):
            print(f"Your seat is booked !")
            l = []
            for i in range(1,self.seats + 1):
                l.append(i)
            print(f"Your seat number is {l[-1]}")
            self.seats = self.seats - 1
        else:
            print("Sorry, The train is full ! Try tatkal for book ticket")


    def getStatus(self):
        print(f"The total available in train {self.name} seats are {self.seats}")

    def getFair(self):
        print(f"The price of a ticket is {self.fair}")


Intercity = Train( 90, 20)
Intercity.getStatus()
Intercity.getFair()
Intercity.bookedseats()
Intercity.CancelTicket(5)
Intercity.getStatus()
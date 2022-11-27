# import pandas as pd

# pd.DataFrame()
class RailwayForm:
    Formtype = "Railwayform"  # class attribute
    def printData(self):
        print(f'Name is {self.name}')  # name is not in class attribute so it must be defined in instance attributez
        print(f'train is {self.train}') # train is not in class attribute so it must be defined in instance attribute
    # for i in range(1,11):
    #     print("Yaa i can use class as before i use code but this time code is in a specific class", i)
    #     i += 1
harrysApplication = RailwayForm() # here harrysApplication is an object
harrysApplication.name = "Aftab"   # here instance attribute name is created
harrysApplication.train = "Maurya Express"     # here instance attribute train is created
harrysApplication.printData()
print(RailwayForm.Formtype)
# printData(harrysApplication)
# print(RailwayForm(Formtype))
# Note:- Class can contain undefined things but when you call the class and its methods then undefined things u have to must define undefined thing befor calling the funtion
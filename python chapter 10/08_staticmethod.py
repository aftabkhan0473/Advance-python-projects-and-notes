class Employee:
    company = "google"
    def functionName(self, signature,dost, phir_hera_pheri):
        print(f"signature who work in {self.company} is {signature}, \n dost is {dost}, \n phir_hera_pheri is {phir_hera_pheri}") # function in class can take multiple arguments morethan one

    @staticmethod
    def greet():
        print("Hello boys ! How are you , I hope you all are good as well as me , so just start our first familiar lecture of python programming")
        # if you have not need of self then u write ur function in class without self using staticmethod
    @staticmethod
    def time():
        print("The time is exactly same that in your watch so just see your watch to know the time")

Aftab = Employee()  # parenthesis is very important when object instatiate class here Aftab is object because it instantiate class Employee

Aftab.functionName("Md Aftab Ali", "Tassu", "mast movie")

Aftab.greet()

Aftab.time()
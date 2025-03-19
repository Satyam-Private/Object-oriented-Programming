#function vs methods 
#method is a special fuction which is written inside the class
#where a function is simple function outsider the class
#methods are only accesicble by class member

class Atm:
    #variables are always declared insider the init method
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        options = int(input("""
            1. Enter 1 to create pin 
            2. Enter 2 to deposit 
            3. Enter 3 to withdraw
            4. Enter 4 to check to balance
"""))
    def atm(self , options):
        if(options == 1):
            print("you entered 1 to create pin")


person1 = Atm()
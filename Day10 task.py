class Withdraw():
    def __init__(self,amount):
        amount = float(input("Enter amount to be withdrawn:"))
        self.amount = amount
        self.balance = self.balance - self.amount
        if (self.balance>=self.amount):
            print(self.amount,"Rupees")
            print(self.balance,"Remaining Balance")
        else:
            print("Insufficient balance")

class Deposit():
    def __init__(self,amount):
        amount = float(input("Enter the amount to be deposited: "))
        self.amount = amount
        self.balance = self.balance + self.amount
        print(self.amount,"Deposited amount")
        print(self.balance,"New Balance")

class Bank_Account(Deposit,Withdraw):
    def __init__(self,balance = 455):
        self.balance = balance
        Deposit.__init__(self,0)
        Withdraw.__init__(self,0)

a= Bank_Account()        

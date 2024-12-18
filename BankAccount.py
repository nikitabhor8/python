#Creation of simple application

class BankAccount:
    def __init__(self,initialAmt,accHolder):
        self.balance=initialAmt
        self.name=accHolder
        print("Account is created: ")
        print(f"Account created for '{self.name}' with Opening balance{self.balance:2f}")

    def getData(self):
        print(f"Account  '{self.name}' has balance{self.balance:.2f}")

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Amount deposited successfully")
        self.getData()
        print("Thank You")
        

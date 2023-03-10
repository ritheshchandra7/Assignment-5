#Implement a Banking Account
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def getTitle(self):
        return self.title

    def getBalance(self):
        return self.balance   


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def getIR(self):
       return self.interestRate


result = SavingsAccount("More Rithesh Chandra", 5000, 5)
print("Title:", result.getTitle())
print("Initial Balance(in Rs.):", result.getBalance())
print("Intrest Rate(%):", result.getIR())
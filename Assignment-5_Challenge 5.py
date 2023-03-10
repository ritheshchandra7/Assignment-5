


















#Handling a Bank Account
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    # withdrawal method
    def withdrawal(self, amount):
        self.balance = self.balance - amount
    
    # deposit method
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    # Return Value
    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    # IntrestEarned Method
    def interestAmount(self):
        return (self.balance * self.interestRate / 100)


result = SavingsAccount("More Rithesh Chandra", 2000, 5)
print("Initial Balance (in Rs.):", result.getBalance())
result.withdrawal(1000)
print("Balance after withdrawal (in Rs.):", result.getBalance())
result.deposit(500)
print("Balance after deposit (in Rs.):", result.getBalance())
print("Interest on current balance (in Rs.):", result.interestAmount())
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of ${amount} successful. New balance is: ₦ ${self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return f"Insufficient funds. Current balance is: ₦ ${self.balance}"
        else:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. New balance is: ₦ ${self.balance}"


account = BankAccount("Olorunlambe Khalid", 2750)

print(account.deposit(500))       
print(account.withdraw(200))      
print(account.withdraw(1500))    

from abc import ABC, abstractmethod

# Encapsulation
class Account:
    def __init__(self, account_id, holder_name, balance):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self,amount):
        self.balance +=amount
        print(f"Deposited {amount} New Balance {self.balance}")
    def withdraw(self, amount):
        print(f"Withdrawing {amount} New Balance {self.balance}")
        if amount <= self.balance:
            self.balance -=amount
            print(f"Withdraw {amount} New balance {self.balance}")
        else:
            print("insufficient funds")
    def get_balance(self):
        return self.balance
    def get_holder_name(self):
        return  self.holder_name
# Inheritance
class Customer(Account):
    def __init__(self,account_id, holder_name, balance, phone_number):
        super().__init__(account_id,holder_name, balance)
        self.phone_number =phone_number
# polymorphism
class Transaction:
    def __init__(self,amount):
        self.amount = amount
    def execute(self,account):
        pass
class DepositTransaction(Transaction):
    def execute(self, account):
        pass
class WithdrawTransaction(Transaction):
    def execute(self,account):
        account.withdraw(self.amount)
# Abstraction
class PaymentSystem(ABC):
    @abstractmethod
    def process_transaction(self, amount):
        pass
class MpesaPaymentSystem(PaymentSystem):
    def process_transaction(self,amount):
        print(f"Processing Mpesa payment of {amount}")
# Example usage
mpesa=MpesaPaymentSystem()
account1=Customer(1, "Sheila", 1000, 74535445)

deposit=DepositTransaction(500)
withdraw=WithdrawTransaction(1200)

deposit.execute(account1)
withdraw.execute(account1)

print(f"Balance for {account1.get_holder_name()} is:"
      f"{account1.get_balance()}")

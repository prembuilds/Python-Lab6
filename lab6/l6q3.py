# Define a class BankAccount with private attributes account_number and
# balance. Implement methods to deposit and withdraw money, ensuring that
# the balance cannot go below zero. Provide a method to get the account
# details. Test the class by performing deposit and withdrawal operations.

class BankAccount:

    def __init__(self, account_number=000000, balance=0):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}.")
        else:
            print("Invalid amount. Deposit must be positive.")
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}.")
        else:
            print("Insufficient Balance.")
    
    def get_details(self):
        print(f"Account Number : {self.__account_number}")
        print(f"Available Balance : {self.__balance}")


# Testing
b1 = BankAccount(1111111, 1000)
b1.get_details()

print()

b1.deposit(500)
b1.get_details()

print()

b1.withdraw(5000)
b1.get_details()

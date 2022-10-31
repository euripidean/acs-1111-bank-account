"""
Bank Account Project
"""
import random


class BankAccount:
    """Bank Account Class"""
    def __init__(self, full_name, account_number = random.randint(1,10**8), balance = 0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Add amount to balance"""
        self.balance += amount
        print (f'Amount deposited: ${amount}. New Balance: ${self.balance}.')

    def withdraw(self, amount):
        """Withdraw amount from balance"""
        if (self.balance - amount) <= 0:
            print('Insufficient Funds. Overdraft fee applied.')
            self.balance -= 10
        else:
            self.balance -= amount
            print (f'Amount withdrawn: ${amount}. New balance: ${self.balance}.')

    def get_balance(self):
        """Print and return balance"""
        print(f'Your current balance is: ${self.balance}.')
        return self.balance

    def add_interest(self):
        """Adds monthly interest"""
        interest = self.balance * 0.00083
        self.balance = self.balance + interest

    def print_statement(self):
        """Print statement information"""
        print(f'{self.full_name}\nAccount Number: ****{str(self.account_number)[-4:]}\n Balance: ${self.balance}.')

#Class ends
mitchell_account = ("Mitchell", 33141592, 400000)

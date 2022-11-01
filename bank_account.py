"""
Bank Account Project
"""
import random

ACCOUNT_PROMPT = 'First, we need your account number.'

class BankAccount:
    """Bank Account Class"""
    def __init__(
        self,
        full_name,
        account_number = random.randint(1,10**8),
        balance = 0,
        account_type = 'checking'):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        """Add amount to balance"""
        self.balance += amount
        print (f'Amount deposited: ${amount}. New Balance: ${self.balance:.2f}.')

    def withdraw(self, amount):
        """Withdraw amount from balance"""
        if (self.balance - amount) <= 0:
            print('Insufficient Funds. Overdraft fee applied.')
            self.balance -= 10
        else:
            self.balance -= amount
            print (f'Amount withdrawn: ${amount}. New balance: ${self.balance:.2f}.')

    def get_balance(self):
        """Print and return balance"""
        print(f'Your current balance is: ${self.balance:.2f}.')
        return self.balance

    def add_interest(self):
        """Adds monthly interest"""
        if self.account_type == 'checking':
            interest = self.balance * 0.00083
        else:
            interest = self.balance * 0.001
        self.balance = self.balance + interest

    def print_statement(self):
        """Print statement information"""
        print(f'\nName: {self.full_name}\nAccount Number: ****{str(self.account_number)[-4:]}\nBalance: ${self.balance:.2f}.\n') # pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long


class Bank:
    """Bank Class"""
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

    def create_account(self):
        """Account creation function"""
        full_name = input('Please enter your full name > ')
        while full_name.isdigit():
            full_name = input('Please enter a valid full name without numbers > ')
        balance = (input('What is your starting balance? > '))
        while not balance.isnumeric() or int(balance) < 0:
            balance = input('Please enter a valid positive value > ')
        #Convert balance string to int
        balance = int(balance)
        #Split out multiple words in name to properly capitalize
        name_list = full_name.split(" ")
        for name in name_list:
            i = name_list.index(name)
            fixed_name = name.capitalize()
            name_list[i] = fixed_name
        #Rejoin to standarize full name
        full_name = ' '.join(name_list)
        account =  BankAccount(full_name=full_name, balance=balance)
        #appends account to list
        self.accounts.append(account)
        return account

    def bank_display(self):
        """Decoration for application"""
        print('$'* 25 + '\n')

    def check_amount(self, amount):
        """Check that amount is number greater than zero"""
        while not amount.isnumeric():
            amount = input('Please enter a number: ')
        amount = int(amount)
        while amount < 0:
            amount = input('Please enter a number greater than zero: ')
        amount = int(amount)
        return amount

    def check_account(self):
        """Checks that account number exists with bank and returns object"""
        account_number_list = []
        attempts = 0
        for account in self.accounts:
            account_number_list.append(account.account_number)
        account_number = int(input('Please enter an 8 digit account number: '))
        #Not sure if this is the best way to do this but putting
        # the values in a list helps with all validation points.
        while account_number not in account_number_list:
            if attempts < 2:
                print('Invalid account. Please enter a valid 8 digit account number: ')
            elif attempts == 2:
                print('Last attempt. Please enter a valid account number.')
            elif attempts == 3:
                print('Suspicious activity detected. Ending process.')
                exit()
            account_number = int(input())
            attempts += 1
        for account in self.accounts:
            if account_number == account.account_number:
                return account


    def transfer(self, account, account_to):
        """Transfer to another account"""
        while account == account_to:
            print('You cannot transfer funds to the same account you are transferring from')
            account_to = self.check_account()
        amount = input('How much would you like to transfer? > ')
        amount = self.check_amount(amount)
        account_to.balance += amount
        print(f'Transfer of ${amount} to account ****{str(account_to)[-4:]} successful.')
        account.withdraw(amount)
        return

    def bank_menu(self):
        """Shows menu for banking application"""
        print('What would you like to do?')
        print('1. Create an account')
        print('2. Print your statement')
        print('3. Deposit funds into your account')
        print('4. Withdraw funds from your account')
        print('5. Transfer funds to another account')
        print('6. Change to another account')
        print('7. Exit program. ')

    def enter_account(self, account):
        """If account has not already been set in program, allow user to enter account number"""
        if account is None:
            print(ACCOUNT_PROMPT)
            account = self.check_account()
        return account


    def application(self):
        """Handles user interaction with banking menu"""
        self.bank_display()
        print(f'Welcome to {self.name} bank!\n')
        running = True
        choices = [1,2,3,4,5,6,7]
        account = None
        while running:
            self.bank_display()
            self.bank_menu()
            choice = int(input())
            if choice not in choices:
                print('Please enter  a number that corresponds with your menu choice')
                self.bank_menu()
                choice = int(input('> '))
            elif choice == 1:
                account = self.create_account()
                print(f'Account: {account.account_number} created.\n')
            elif choice == 2:
                account = self.enter_account(account)
                account.print_statement()
            elif choice == 3:
                account = self.enter_account(account)
                amount = input('How much would you like to deposit? > ')
                amount = self.check_amount(amount)
                account.deposit(amount)
            elif choice == 4:
                account = self.enter_account(account)
                amount = input('How much would you like to withdraw? > ')
                amount = self.check_amount(amount)
                account.withdraw(amount)
            elif choice == 5:
                account = self.enter_account(account)
                print('Next enter the account number of the account you would like to transfer to.')
                #Test account numbers that can be used are: 11111111, 22222222 and 33333333
                account_to = self.check_account()
                self.transfer(account, account_to)
            elif choice == 6:
                account = None
                account = self.enter_account(account)
            elif choice == 7:
                running = False
        self.bank_display()
        print('Thank you for using the banking app! ')
        self.bank_display()



#PART ONE - REGULAR GOALS
# mitchell_account = BankAccount("Mitchell", 33141592, 400000)
# mitchell_account.print_statement()
# mitchell_account.add_interest()
# mitchell_account.print_statement()
# mitchell_account.withdraw(150)
# mitchell_account.print_statement()

#PART TWO - INITAL STRETCH GOALS
#Added account type - savings account example
# print('Savings Account example:')
# jane_savings = BankAccount('Jane Harrison', balance=12000, account_type = 'savings')
# jane_savings.print_statement()
# jane_savings.add_interest()
# jane_savings.print_statement()

# #Checking account example
# print('Checking account example:')
# jane_checking = BankAccount('Jane Harrison', balance=12000)
# jane_checking.print_statement()
# jane_checking.add_interest()
# jane_checking.print_statement()

#PART THREE - BANKING APP
#Instance of bank
tangerine = Bank('Tangerine',[])

#create non-application accounts for use with in app:
account1 = BankAccount('Nick Cave', account_number = 11111111, balance=420420)
account2 = BankAccount('Mary Shelley', account_number=22222222, balance=56000)
account3 = BankAccount('Chuck D', account_number=33333333, balance=911911)

#append to Bank accounts list
tangerine.accounts.append(account1)
tangerine.accounts.append(account2)
tangerine.accounts.append(account3)

#enter application
tangerine.application()

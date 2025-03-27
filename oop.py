'''
This is an Object Oriented programming example.
It demonstrates the concept of inheritance, encapsulation, data hiding, and polymorphism.
'''

# The parent class BankAccount
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute (Encapsulation)

    # deposit() method
    """Allows deposit of money into the account."""
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # withdraw() method
    """Allows withdrawal of money from the account."""
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    # get_balance() method
    """Allows viewing of balance (getter method)."""
    def get_balance(self):
        return self.__balance

# Inheritance: SavingsAccount extends BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        '''Child constructor which uses the parent but also adds an attribute interest_rate'''
        super().__init__(account_holder, balance)  # Call parent constructor to define and set interest rate
        self.interest_rate = interest_rate  # Public attribute

    def apply_interest(self):
        """SavingsAccount has a unique method that applies interest to the balance"""
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest of {interest} applied. New balance: {self.get_balance()}")

# Child class CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        '''Child constructor which uses the parent but also adds an extra feature of overdraft_limit'''
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit  # Extra feature for CheckingAccount

    def withdraw(self, amount):
        """Overrides withdraw method to allow overdraft."""
        '''Polymorphism applies by having a child withdraw() method override the parent withdraw() method to allow for the overdraft '''
        if amount <= (self.get_balance() + self.overdraft_limit):
            self.deposit(-amount)  # We deposit a negative amount indicating an overdraft
            print(f"Overdraft allowed. Withdrawn: {amount}. Remaining balance: {self.get_balance()}")
        else:
            print("Withdrawal exceeds overdraft limit.")

# Actual program
savings = SavingsAccount("Mary", 1000, 5)  # Creating Mary's savings account with 1,000 balance and 5% interest rate
checking = CheckingAccount("Mary", 500, 200)  # Creating Mary's checking account with 500 balance and 200 overdraft

savings.deposit(500)
savings.apply_interest()

checking.withdraw(900)  # Allowed with overdraft
checking.withdraw(200)  # Allowed with overdraft